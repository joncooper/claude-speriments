## Bolt notification channel — rebuild spec

Bolt is Dropbox's long-lived change-notification channel. In this build it is implemented across four Rust compilation units (all inside `libdropbox_core.so`, none in `libdropbox_tprt.so`), exposed to the rest of the engine as a local gRPC method, and mirrored by a Python client layer. It is the mechanism a reimplementer uses to learn *that* something changed; the actual metadata delta is then pulled by the `list` phase.

### 1. Code map (where Bolt lives) [OBS]

Four embedded Rust source paths, all under `desktop/rust/`:

| Module ident | Source path | Role (name + strings) |
|---|---|---|
| `bolt::default` | `desktop/rust/dropbox/bolt/src/default.rs` | generic subscriber manager + run loop (the `dropbox/bolt` crate) |
| `network::bolt` | `desktop/rust/nucleus/network/src/bolt.rs` | low-level HTTP/2 client that talks to `bolt.dropbox.com` |
| `engine_common::bolt` | `desktop/rust/nucleus/engine_common/src/bolt.rs` | engine-shared helpers ("Reconfiguring bolt") |
| `nucleus_bolt_connection` | `desktop/rust/nucleus/nucleus_bolt_connection/src/lib.rs` | binds the sync-engine protocol to the bolt subsystem |

Python side (`modules.txt`) [OBS]: `dropbox.client.bolt.{__init__,base,payloads,signalling,types}`, `dropbox.client.features.bolt.{bolt_client_for_app,bolt_client_wrapper}`, plus feature consumers `dropbox.api.v2.datatypes.backup_bolt` and `dropbox.client.contacts.polaris.contacts_bolt_update_manager`. [INF] Bolt is a shared account-wide push fabric used by multiple features (sync/nucleus, Computer Backup, Contacts), keyed per app — hence `bolt_client_for_app`.

The vendored HTTP stack (`hyper-0.14.31` ×225, `h2-0.3.26` ×278, `grpc_connection`) is compiled into `libdropbox_core.so` as well as `tprt`, so the Bolt long-poll is issued directly from core, not proxied through the `tprt` FFI. [OBS: `hyper-0.14`, `h2-0.3` counts in core]

### 2. Server endpoint & wire request [OBS]

- Host: logical server `boltserver` → `bolt.dropbox.com` in the embedded `DROPBOX_HOST` map (`Server Name: {}, Host: {}, Port: {}`). Port not individually recovered [UNK].
- The `network::bolt` compilation unit contains one contiguous run of request-building literals:
  `...dropbox-desktop` `274.4.4905` `stable` `Content-Type` `Connection` `keep-alive` `X-Dropbox-UID` `/2/notify/subscribe` `source` `nucleus`.
  So the Bolt request is an HTTP/2 request to path **`/2/notify/subscribe`** with:
  - `X-Dropbox-UID: <account uid>` [OBS header name]
  - `Connection: keep-alive` [OBS]
  - a `Content-Type` header (value not captured — not `application/grpc+proto`; that string belongs to the nsf/sync path) [OBS name, value UNK]
  - a `source=nucleus` discriminator (query param or field) distinguishing the caller app [OBS tokens `source`,`nucleus`; INF it is `source=nucleus`]
  - User-Agent composed from `dropbox-desktop` / `274.4.4905` / `stable` (client name / version / release channel) [OBS; INF assembly]
- Error enum in `network::bolt` (contiguous: `GrpcV2Error ProtoError MissingResponseContext ResponseCode BadFileId Message`) [OBS]. The leading `GrpcV2Error` plus the sibling messages **"Expected a unary response but got multiple data frames"** and **"Expected a unary response but got nothing"** show the Bolt call is framed as a **GrpcV2 *unary* request/response over HTTP/2**, not a streaming RPC. [OBS]

**Transport correction vs. prior hypothesis:** EVIDENCE.md guessed "likely HTTP/2 server-stream." The observed strings contradict a server stream: the code explicitly rejects a multi-frame response ("Expected a unary response but got multiple data frames"). [INF] Bolt is a **long-poll of unary GrpcV2 requests**: the client POSTs a subscribe request carrying its channel tokens; the server holds the connection open until a subscribed channel has a delta (or a timeout elapses) and returns a single unary response; the client then immediately re-issues (reconnects). The "long-lived channel" is this reconnect loop, not one streamed RPC.

### 3. Authentication [OBS/INF]

Immediately adjacent to the Bolt request literals in `network::bolt` are **`[OAuth] Retrieving access token for account`** and **`[OAuth] Failed to retrieve access token`** [OBS]. [INF] Bolt authenticates with a per-account **OAuth2 bearer access token** (plus the `X-Dropbox-UID` account selector), i.e. it uses the apiv2/auth-server OAuth credential rather than the classic `Dropbox-Host-Key` used by the core sync protocol. Exact header carrying the token = [UNK] (bearer in `Authorization` is the conventional [INF]). The token-fetch sits in the request-send path, so the client must mint/refresh the access token before each (re)connect.

### 4. Data structures (proto/serde messages) [OBS field names + element counts]

Recovered serde "expecting" messages and field-name tables (names are exact tokens; membership/typing is partly [INF]):

- `struct ChannelId with 2 elements` — fields `app_id`, `unique_id`. [OBS] A ChannelId identifies one logical channel: `app_id` selects the feature/app, `unique_id` the specific stream (e.g. a namespace). [INF]
- `struct BoltChannelToken with 3 elements` and a separate `struct BoltChannelToken with 5 elements` [OBS] — two distinct definitions exist (one in `dropbox/bolt`, one in nucleus). Observed field tokens clustered with it: `channel_id`, `token`, `channel_states` (and in an adjacent token struct `rev`, `deprecated_revision`). [INF] A BoltChannelToken = `{ channel_id: ChannelId, token: <opaque server cursor/position>, ... }`; `token` is the opaque resumption position the server uses to decide `has_delta`.
- `struct SubscribeToBoltReply with 2 elements` [OBS]. Reply fields observed: `has_delta` (bool) and per-channel `channel_states` whose per-entry state is `updated` or `invalid` (strings `has_delta`, `invalid`, `updated`, `channel`). [INF] Reply ≈ `{ has_delta: bool, channel_states: [ {channel_id, token, updated|invalid} ] }`.
- Related/adjacent proto messages in the same subsystem [OBS]: `CommunicateCommandResponse` (oneof `response_body`), `nucleus.UpgradeFromClassicArgs` (oneof `timeout`), `RegisterClientResponse`, `RegisterFileKeyBatchResponse`, `GetTeamPublicKeyResponse`, `ApiV2ApiError` (`error`, `error_summary`). These travel the same remote-command rail as Bolt (§6).
- Error/token variants [OBS]: `BoltTokenMissing`, `BoltTokenNextCommand`, `AuthorizationTokenMissing` (these appear as enum variants in the engine error type alongside `TeamKeyNotFound`, `InodeBlocklisted`).

### 5. Subscriber manager / run loop — `dropbox/bolt/src/default.rs` [OBS]

State and lifecycle strings (exact), giving the reimplementer the control flow:

- Startup: **`Initializing bolt run loop`**; state var **`should_reconnect`**.
- Idle: **`No subscriptions; waiting for subscribe call`**; **`Seems like the LongPoller was dropped!`** (a `LongPoller` task owns the outstanding request). [OBS] Confirms the long-poll design and a dedicated poller task.
- Per-iteration: **`Making Bolt request`** with counters `num_tokens` / `outstanding_tokens`.
- Completion: **`Bolt request succeeded`** (fields `request_id`, `request_size`, `response_size`), **`Bolt response`** / **`Bolt response status `**, **`Bolt request timed out`**.
- Dispatch: **`Handling bolt response`**; **`Signalling and unsubcribing subscribers of bolt update`** (fields `channel`, `subscribers_to_signal`, states `invalid`/`updated`).
- Subscriber registry: **`Updated bolt subscriber state`** (keyed by `subscriber_id`), **`Received bolt subscribe request without any new tokens. Programmer error?`**, **`Constructed empty bolt subscriber reply. Context: subscriber_tokens`**, assertion `!self.channel_state.contains_key(&new_token.channel_id)`, and revision dedup **`Already have a newer revision for bolt subscriber`** (so each channel carries a monotonically increasing revision; stale pushes are dropped).
- Teardown: **`Ending bolt run loop because our channel has terminated`**.

[INF] Reconstructed loop: maintain `channel_state: Map<ChannelId, {token, revision, subscribers}>`; while any subscriptions exist, issue a long-poll Bolt request carrying all current tokens; on response, for each channel marked `updated` store the new token (if revision newer) and signal its local subscribers, for `invalid` drop/resubscribe; on timeout, reconnect; if no subscribers, park until the next `subscribe` call.

### 6. Local gRPC surface + remote-command rail [OBS]

- Local method: **`/nucleus.ReverseNucleusAPI/SubscribeToBolt`** [OBS] (sibling methods on that service: `GetBlockFromPeer`, `PublishEvent`, `Echo`, `FswRuleSuppress`, `ShowFSWDialog`). Request = `BoltChannelToken`(s), response = `SubscribeToBoltReply`. [INF] This is how an in-process/peer caller (file-provider engine, Python `bolt_client_wrapper`, LAN peer) subscribes through nucleus; `source=nucleus` on the outbound request identifies this caller.
- Bolt is also one entry in nucleus's **remote-command** vocabulary (`desktop/rust/nucleus/remote_command/src/lib.rs`). One contiguous run enumerates the command kinds [OBS]:
  `reassociate`, `bolt_subscribe`, `upload_block`, `commit_at_head`, `download_block`, `block_signature`, `linearized_list`, `can_change_fileid`, `check_consistency`, `get_initial_cursor`, `get_namespace_info`, `upload_rsync_block`, `acknowledge_commits`, `communicate_command`, `consistent_cut_list`, `get_pending_uploads`, `download_rsync_block`, `get_file_information...`.
  Also seen: `Remote command (bolt_subscribe)`, `bolt_subscribe (resync)`, `bolt_subscribe (instant_files)` [OBS]. [INF] `bolt_subscribe` is the command that (re)arms the notification channel; it is driven both by the normal protocol loop, by resync, and by the instant-files/streaming-sync path.

### 7. Relationship to the protocol `subscribe` → `list` phases [OBS/INF]

The per-namespace protocol state machine (`nucleus/protocol/src/states/{subscribe,list,commit,commit_ack,mod}.rs`) is driven by Bolt:

- `protocol::states::subscribe` strings: **`Entered subscribe without a cursor?`**, `calling_subscribe`, and the run `list_reply_cursor subscribe` [OBS]. [INF] The `subscribe` state takes the namespace's current cursor, derives/holds a `BoltChannelToken` for it, and arms Bolt (`bolt_subscribe`).
- When the Bolt reply carries `has_delta`/`updated` for that channel, the worker advances to `list`. `list.rs` strings: `List processor error with no remote ops?`, `list_up_to_date`, `list_reply_cursor`, `num_ops` [OBS]. [INF] `list` pulls the remote metadata delta by cursor, producing `list_reply_cursor` (the next cursor), which feeds the next `subscribe`.
- Protocol transition enum literals include `Commit`, `CommitAck`, `Subscribe` (run `CommitCommitAckSubscribeto...`) [OBS], confirming the loop `subscribe → list → commit → commit_ack`.

So: **Bolt `has_delta` is the edge-trigger that moves a namespace from `subscribe` to `list`.** Without Bolt, the engine would have to poll `list`.

### 8. Configuration, migration & metrics [OBS]

- Stormcrow feature flags: **`desktop_nucleus_use_separate_bolt`** (gates whether Bolt runs on its own connection/loop), **`stormcrow_variant_subscribe`**, `sync_protocol_improvements_variant`. On a flag change, `engine_common::bolt` logs **`Reconfiguring bolt`** (with `variant_changed`) and `bolt_migration/stormcrow_changed` fires. [OBS]
- Migration knob: **`bolt_migration/reconnect_interval_ms`** [OBS] — the reconnect cadence for the long-poll loop (used by the "Bolt vs legacy notify" migration).
- Legacy path still present: **`/2/notify/subscribe`** is the classic Dropbox notify long-poll URL, now wrapped in GrpcV2 as the Bolt transport. [OBS] [INF] "Bolt migration" = moving the legacy `notify` long-poll onto the Bolt rail.
- Metrics counters (exact tokens) [OBS]: `bolt/request/bytes`, `bolt/response/success/duration`, `bolt/response/success/bytes`, `bolt/response/failed`; and the shared network family `network/request_success/{duration,request_size,response_size}`, `network/error_resolution/{duration,count}`, `network/error/{period,count}`.
- `tprt` FFI exposes generic invalidation callbacks `notify` / `notify_cancel` / `notify_done` / `notify_err` (`api_tprt.txt`) — these are the gRPC-level invalidation-handler hooks, distinct from the Bolt notify endpoint; a reimplementer should not conflate them. [OBS]

### 9. Minimal reimplementation recipe [INF, from the above OBS]

1. Obtain an OAuth2 access token for the account; know the account `uid`.
2. For each namespace you track, hold a `BoltChannelToken { channel_id: {app_id, unique_id}, token }`. Seed `token` from the namespace's current list cursor (or an empty/initial token).
3. Open an HTTP/2 TLS connection to `bolt.dropbox.com`; POST `/2/notify/subscribe` carrying all current channel tokens, with `X-Dropbox-UID`, `Connection: keep-alive`, the OAuth bearer, UA `dropbox-desktop/274.4.4905 stable`, and `source=nucleus`. Frame it as a GrpcV2 unary request.
4. Block (server long-poll) for the single unary response. Parse `SubscribeToBoltReply { has_delta, channel_states: [{channel_id, token, updated|invalid}] }`.
5. For every channel with `has_delta`/`updated`: store the new `token` (ignore if its revision is not newer) and trigger that namespace's `list` (pull delta by cursor). For `invalid`: resubscribe fresh.
6. Reconnect immediately (or after `reconnect_interval_ms` on timeout/error) and repeat. Report `bolt/response/*` and `bolt/request/bytes` metrics.

### Residual unknowns [UNK]
- Exact wire bytes of the GrpcV2 framing and the `Content-Type` value Bolt uses.
- Exact serialization of `token` (opaque blob vs. structured) and how `rev`/`deprecated_revision` bind to a channel.
- Full field membership of the 3- vs 5-element `BoltChannelToken` variants.
- Server-side long-poll timeout value; the `boltserver` port.
- The precise header that carries the OAuth bearer, and whether host-key is ever used as a fallback for Bolt.