## Session & Authentication — rebuild spec

Static-only analysis of `libdropbox_core.so` (`str_libdropbox_core.so.txt`) and `libdropbox_tprt.so` (`str_libdropbox_tprt.so.txt`). All auth logic lives in **core**; tprt carries only `Proxy-Authorization: Basic %s` and X.509/TLS strings [OBS], so a reimplementer puts all Dropbox-level auth in the HTTP/gRPC request layer above the transport.

### 0. Executive model (how the pieces fit)

There are **two distinct credential systems**, both terminating at the Authorization header of the APIv2 client, plus a key-management service that is *not* session auth:

1. **Host-key (classic desktop)** — a device holds a `host_id` (public) + `host_int` (secret "host key"). [OBS/INF]
2. **OAuth2 bearer** — per-account `refresh_token` persisted; short-lived `access_token` minted on demand at `/oauth2/token`. [OBS]
3. **EKMS `register_client`** — encrypted-folder client-key enrollment; shares the name "RegisterClient" but is the encrypted-folder/coauth subsystem, **not** device registration. [OBS] Keep distinct (this corrects the §7 reading in EVIDENCE.md).

The single HTTP client that reaches Dropbox servers is `desktop/rust/dropbox/apiv2_client/src/client.rs` [OBS]. It emits `POST` + `Content-Type: application/json` and sets the `Authorization` header to one of two schemes — `Dropbox-Host-Key <value>` or `Bearer <value>` [OBS]. The modern sync/notify path (`nucleus/network/src/bolt.rs`) is driven by the OAuth bearer tokens [OBS]; host-key is the legacy scheme the same client still supports.

### 1. The APIv2 client — exact per-request shape [OBS]

File: `desktop/rust/dropbox/apiv2_client/src/client.rs`. Adjacent literals (one contiguous blob in the corpus):

```
POST  application/json  Content-Type
Dropbox-Host-Key <sp>
Bearer <sp>
...
Authorization   X-Dropbox-Path-Root   X-Dropbox-Traffic-Tier
Failed to construct POST request
/2/ekms/get_namespace_public_key  /2/ekms/enroll_clients
/2/ekms/get_encrypted_team_key_list_with_client_key  /2/ekms/get_file_keys
/2/ekms/get_namespace_key  /2/ekms/get_pending_clients
/2/ekms/get_team_enrollment_status  /2/ekms/get_team_public_key
/2/ekms/register_client  /2/ekms/register_file_key_batch
```

A reimplementer must reproduce, for every `/2/...` call:
- Method `POST`, body `application/json`.
- **One** `Authorization` header, value = `"Dropbox-Host-Key " + host_key` **or** `"Bearer " + access_token` [OBS: the two trailing-space prefixes sit immediately before the `Authorization` header name — [INF] they are Authorization *scheme* prefixes, not separate header names]. Which scheme is chosen per call/account = **[UNK]** from static evidence.
- Optional `X-Dropbox-Path-Root` (root-namespace selection) and `X-Dropbox-Traffic-Tier`. [OBS]
- Logical server targets named `apiv2server` / `apiv2blockserver` [OBS] → host `api.dropbox.com` (see §6).

Other APIv2 endpoints seen reached through the same client (same header contract): `/2/files/get_thumbnail_batch`, `/2/stormcrow_servicer/get_assignments`, `/2/wopi/get_file_checksum`, `/2/wopi/is_coauth_supported_for_user`, `/2/wopi/get_wopi_metadata`, `/pap_event_logging.EventLoggingApiV2/LogRecords` [OBS]. Error envelope is `struct ApiV2ApiError with 2 elements` (`error`, `error_summary`) and `struct AuthError with 1 element` [OBS].

### 2. OAuth2 token subsystem (apex `auth` + `dbxauth`) [OBS]

**Token endpoint.** `desktop/app/lib/apex/rust/auth/src/connection.rs` builds the refresh request. Contiguous literals: `access_token expires_in grant_type refresh_token /oauth2/token` and the serializer `url::form_urlencoded::Serializer` (`form_urlencoded-1.2.2`) [OBS]. The request just above in the corpus is `application/x-www-form-urlencoded Content-Type` [OBS].

→ Reproduce: `POST /oauth2/token` to the apiv2/auth server, body `application/x-www-form-urlencoded` with `grant_type=refresh_token&refresh_token=<rt>` [OBS field names]; response JSON parsed for `access_token` + `expires_in` [OBS]. `grant_type=refresh_token` is the only grant literal present. Client-authentication method (whether the baked-in app key/secret go in the body as `client_id`/`client_secret` or as HTTP Basic) is **[UNK]** — no `client_id`/`client_secret` literals appear at the token call, and the only `Basic ` strings are in `analytics/src/ssa_connection.rs` and the tprt proxy.

**App credentials.** `bazel-out/.../desktop/rust/dropbox/apiv2_keys/_bs.out_dir/keys.rs` holds compiled-in keys; override env-var names observed: `DROPBOX_HOST`, `devboxdropboxdesktopappkey`, `devboxdropboxdesktopappsecret` [OBS]. [INF] the client ships an OAuth app key + secret; the literal secret value is baked into `keys.rs`, not a plain string.

**Token-cache state machine** (`desktop/app/lib/apex/rust/auth/src/client.rs`, module `auth::client`) [OBS panic/log strings]:
- `[OAuth] Adding refresh token for account twice`
- `failed to queue refresh for new account`
- `[OAuth] Attempted to remove non-existent account from cache`
- `Hit APIv2 endpoint specific error when refreshing token`
- `Programming error: No account info found for account`
- `Programming error: Unable to serialize refresh request`
- `Too many transient errors when refreshing access token`
- `Unauthorized to make APIv2 request`

And from the bolt/network caller (`nucleus/network/src/bolt.rs`): `[OAuth] No refresh token registered for account`, `[OAuth] Refreshing access token for account`, `[OAuth] Attempting to retrieve access token`, `[OAuth] Newly refreshed token is too close to expiration`, `[OAuth] Encountered an error while refreshing access token`, `[OAuth] Retrieving access token for account`, `[OAuth] Failed to retrieve access token`, metrics `refresh/success_attempts`, `refresh/failure_attempts`, `failure_reason` [OBS].

→ Behavior to reproduce [INF from these strings + typical refresh-token caches]: tokens are held **per `account_id`**; `access_token` is cached and refreshed lazily when near expiry ("too close to expiration"); refresh is queued/serialized per account; transient failures are retried up to a cap then surfaced as `Unauthorized to make APIv2 request`.

**FFI surface** (exported C-ABI symbols of core; Python control process calls them) [OBS]:
- `oauth_register_refresh_token` — store `(account_id, refresh_token)`.
- `oauth_retrieve_access_token` — return a fresh access token (via a token callback).
- `oauth_remove_account` — drop an account's tokens.
- `dbxauth_retrieve_accounts`, `dbxauth_destroy_accounts`, `dbxauth_destroy_error` — enumerate persisted accounts.
- `monitor_session_id` — session-id monitor.
C-API arg validation strings (`desktop/app/lib/apex/c_api/src/auth.rs`): `invalid utf-8 data in account_id`, `invalid utf-8 data in refresh_token`, `invalid utf-8 data in access token`, `token callback was null` [OBS] → confirms the `(account_id, refresh_token)` in / `access_token` out-via-callback shape.

### 3. Account record & host-key fields (dbxauth) [OBS]

`desktop/app/lib/apex/rust/dbxauth/src/lib.rs` deserializes the account row. Field list (contiguous), the authoritative account struct a reimplementer must model:

```
cached_ui_flags role root_ns home_ns host_int host_id account_id
dropbox_path home_ns_path root_ns_fileid home_ns_fileid root_layout
email user displayname [host secret] is_team_admin
non_team_sharing_disabled team_file_transfers_disabled
team_send_for_signature_disabled team_id
```

- `host_int` = the **secret host key**; its redaction placeholder in logs is the literal `[host secret]` [OBS]. `host_id` = the public device/host identifier. Both are classic desktop pairing tokens.
- `account_id` identifies the user/account; `team_id` + the `*_disabled`/`is_team_admin` flags are team policy.
- A failure to decrypt the DB surfaces as `Cannot decrypt database` [OBS] (ties to §5 keystore).

The **keystore C-API Account** struct (`desktop/app/lib/apex/c_api/src/keystore.rs`) is a parallel view carrying the credential across FFI [OBS]:
```
Personal|Business  host_key  business  ui_flags  host_id  account_id
root_mount_path root_ns_id home_ns_id root_ns_fileid home_ns_fileid
root_layout home_ns_path has_tmf email user_display_name
host_display_name appdata_path instance_id is_primary config
```
→ `host_key` here is the same secret as `host_int`. Note `is_primary` (multi-account; one primary) and `instance_id`.

`host_id`/`host_int` also surface in sync-object metadata: the blob `...PlaceholderCountSyncObject host_id paired_host_key user_id paired_user_id account_id device_id root_ns_id home_ns_id...` [OBS] shows a per-object `paired_host_key`/`paired_user_id`/`device_id` triple (anti-relocation binding of a placeholder to the device). The metrics layer classifies host ids with the regex `HOST_ID.*[0-9]+(n|i)*(ro)*[a-z]*$` and tags `classic`/`nucleus`/`nucleus_readonly`/`isotope` [OBS].

### 4. Local persistence of the session [OBS]

- `config.dbx`: key/value table queried with `SELECT key, value FROM config;` [OBS].
- `instance.dbx` (aka `instance_db`): `SELECT id, appdata_path, uid, master FROM instance WHERE active = 1 AND uid > 0;` [OBS]. So the active account is picked by `active = 1 AND uid > 0`; columns `id`, `appdata_path`, `uid`, `master`. `master` = the per-instance master key that gates DB decryption. Note `uid` (numeric user id) is distinct from `account_id`/`aid` — an assertion `old_start_uid < old_start_aid` [OBS] confirms uid ≠ aid.
- Databases are the encrypted `.dbx` SQLite files (codec in `libdropbox_sqlite_ext.so`); PRAGMAs observed: `journal_mode = WAL`, `synchronous = FULL`, `fullfsync = true`, `journal_size_limit = 10485760` [OBS].

### 5. Credential storage: keystore (`apex/rust/keystore`) [OBS]

FFI symbols [OBS]: `keystore_create`, `keystore_create_user_key`, `keystore_retrieve_database_key`, `keystore_retrieve_user_key`, `keystore_destroy`. Two key kinds: a **database_key** (decrypts the `.dbx`/`master`) and a **user_key**. Error enum: `KeyStoreError`, `SqliteError`, `JsonError`, `MissingField`, `EmptyConfig` [OBS].

Backend (`desktop/app/lib/apex/rust/keystore/src/posix.rs`): stores a **JSON blob** (field `hostkeys` seen) that is **base64-encoded** (the base64 alphabet + `Cannot base64 decode` are inline) and **integrity-checked by a digest** (`Digest is not what is expected`, `JSON value is not a string: `, `Invalid payload of size `) [OBS].

**Correction to EVIDENCE.md §7:** I find **no** `libsecret`/`secret_service`/`org.freedesktop.secret`/`gnome-keyring`/`kwallet`/`dbus` SecretService strings anywhere in core or tprt [OBS absence]. The posix keystore as observed is a **file-based, JSON + base64 + digest** store, not an OS keyring. Treat "OS keyring" as **[UNK]/unsupported** unless it lives in the encrypted Python layer. The digest algorithm and the key-wrapping scheme are **[UNK]**.

### 6. Server topology relevant to auth [OBS]

From the bootstrap `DROPBOX_HOST` map (`desktop/app/lib/core/bootstrap/src/context.rs`), one contiguous blob: `webserver=www.dropbox.com`, `metaserver=client.dropbox.com`, `authserver`+`apiv2server=api.dropbox.com`, `metaexcserver=d.dropbox.com`, `blockexcserver=dl-debug.dropbox.com`, `t8=t8.dropbox.com`, `d6=d6.dropbox.com`, `staticserver=cfl.dropboxstatic.com`, `boltserver=bolt.dropbox.com` [OBS]. Map schema printed as `Server Name: {}, Host: {}, Port: {}` with fields `server.server_name`, `server.host.host_name`, `server.host.port` [OBS].

→ `/oauth2/token` and `/2/...` go to **`api.dropbox.com`** (authserver/apiv2server) [INF]; the Bolt notify channel goes to **`bolt.dropbox.com`** [OBS].

### 7. Modern notify/sync auth — Bolt channel [OBS]

`desktop/rust/nucleus/network/src/bolt.rs` (module `network::bolt`): emits headers `Content-Type`, `Connection: keep-alive`, `X-Dropbox-UID`, path `/2/notify/subscribe`, `source`/`nucleus`, and the user-agent trio `dropbox-desktop` / `274.4.4905` / `stable` [OBS]. The OAuth refresh strings (§2) are inline in this same module [OBS].

→ Reproduce the long-poll/notify subscribe as: HTTP/1.1 keep-alive `POST /2/notify/subscribe` carrying `X-Dropbox-UID: <uid>` and an OAuth `Authorization: Bearer <access_token>`, plus request-tracing header `x-dropbox-request-id` [OBS]. [INF] `X-Dropbox-UID` value = the account's numeric `uid` (from the `instance` row). The sync-frontend gRPC method short-names carried over this connection (`network::failure_manager` list): `bolt_subscribe`, `linearized_list`, `get_initial_cursor`, `acknowledge_commits`, `commit_at_head`, `upload_block`/`download_block`(`_with_token`), `block_signature`, `upload_rsync_block`/`download_rsync_block`(`_with_token`), `check_consistency`, `consistent_cut_list`, `get_namespace_info`, `can_change_fileid`, `communicate_command`, `reassociate`, `ping_sfe`, plus `get_file_keys`/`register_client`/… (EKMS) [OBS]. gRPC content types `application/grpc+proto` / `application/grpc-web+proto`; network error enum includes `Unauthorized`, `ApiV2Endpoint`, `RateLimited`, `HttpError`, `InvalidHost`, `ClientInitiatedReconnect` [OBS]. The encrypted-folder bolt channel additionally uses a `BoltChannelToken with 5 elements` + `bolt_token` returned by EKMS [OBS] — distinct from the OAuth path.

### 8. Device identity: machine_id & device_anchor [OBS]

**machine_id** — `desktop/app/lib/core/machine_id/src/{cache.rs,stormcrow_flag.rs}`, module `machine_id::cache`. Log line `Device: machine_id = ` [OBS]. The machine-id enablement flag is persisted under the home dir (`.dropbox_…`) with a stormcrow flag key and GUID `2f34f783-7350-4a35-b90e-3ffec774987d` [OBS]; strings `Writing stormcrow flag to disk`, `read_machine_id_stormcrow_flag_from_cache`, `write_machine_id_stormcrow_flag_to_disk` [OBS]. `machine_id` is submitted in stormcrow `/2/stormcrow_servicer/get_assignments` requests alongside `device_id`, `sys_model`, `locale`, `true_processor_arch`, `seed`, `tags` [OBS]. The literals `/var/lib/dbus/machine-id` and `/etc/machine-id` appear in core [OBS]; [INF] the Dropbox `machine_id` likely derives from the systemd/D-Bus machine-id (not proven — the strings are adjacent to unrelated crates).

**device_anchor** — `desktop/rust/nucleus/device_anchor/` (modules `list_api`, `constraints::{unique_target,dbx_descendant,only_folders,target_writable}`) [OBS]. Fields `device_anchor_path`, `device_anchor_fileid`, `device_anchor_active`, states `MOUNTED`/`FILE_PROVIDER`; errors `CORRUPTED_DEVICE_ANCHOR`, `INVALID_DEVICE_ANCHOR`, `DEVICE_ANCHOR_NOT_FOUND`, `TARGET_IS_DESCENDANT_OF_D…`, `DropboxFolderUnderDeviceAnchor` [OBS]. On-disk marker is the xattr `user.com.dropbox.device_anchor` [OBS]. → [INF] a per-device/per-account anchor binding the local Dropbox folder (and Computer-Backup roots) to this device via a fileid + xattr; it is an **identity/anti-relocation** marker, independent of the network session credential.

**Device linking/unlinking** — the launcher CLI verbs include `unlink` and `unlinkr` (`bootstrap/src/context.rs`, alongside `install`, `restart`, `migrate_sparse_to_full`) [OBS]. [UNK] the device-registration/unlink **wire RPC**: there is no native "link device" RPC in these libs; `RegisterClient`/`RegisterClientResponse` is EKMS encrypted-folder client enrollment, not device registration [OBS]. Initial pairing (minting `host_id`/`host_int`/`refresh_token`) is [INF] performed via the web login / the encrypted Python layer and is not recoverable from these native strings.

### 9. Common request headers (all auth flows) [OBS]

Built in `desktop/rust/dropbox/dbx-struct-diff/src/lib.rs`: `X-Dropbox-App-Name`, `X-Dropbox-App-Version`, `User-Agent`, `X-Dropbox-User-Agent`, `Dropbox-API-User-Locale`, `X-Dropbox-Locale`, `X-Dropbox-Backend`, `X-Dropbox-Metro-Pref`, `X-Dropbox-Force-Request-Tracing`, `X-DBX-RUN-TYPE` [OBS]. User-Agent base is `DropboxDesktopClient/` and/or `Dropbox-lnx.x86_64-274.4.4905` [OBS]; app-name/version/channel = `dropbox-desktop` / `274.4.4905` / `stable` [OBS]. Env overrides: `DBDEV_METRO_PREF`, `DBUSESTAGE`/`DBNOUSESTAGE`, `DBDEV_RUN_TYPE`, `DBDEV_REQUEST_TRACING` [OBS].

### 10. Minimal reproduction sequence a reimplementer must build

1. Load the active account from `instance.dbx` (`active=1 AND uid>0` → `id, appdata_path, uid, master`), decrypting via the keystore `database_key`; read the account fields (`host_id`, `host_int`, `account_id`, `email`, namespaces, team flags) from the dbxauth row [OBS].
2. For the OAuth path: with the per-account `refresh_token`, `POST https://api.dropbox.com/oauth2/token` body `application/x-www-form-urlencoded` `grant_type=refresh_token&refresh_token=<rt>` (+ app-key client auth, mechanism [UNK]); parse `access_token`/`expires_in`; cache per account, refresh before expiry [OBS/INF].
3. For every `/2/...` APIv2 call: `POST` JSON to `api.dropbox.com` with `Authorization: Bearer <access_token>` **or** `Authorization: Dropbox-Host-Key <host_int>`, plus the common headers (§9), optional `X-Dropbox-Path-Root`/`X-Dropbox-Traffic-Tier` [OBS]; choice of scheme per endpoint [UNK].
4. For notify/sync: open a keep-alive connection to `bolt.dropbox.com`, `POST /2/notify/subscribe` with `X-Dropbox-UID: <uid>` + Bearer token; run the gRPC sync-frontend methods over HTTP/2 [OBS].

### 11. Open gaps [UNK]
- Exact `host_int` minting/derivation and the full device-registration/link handshake (not in native strings).
- OAuth client-authentication at `/oauth2/token` (body `client_id`/`client_secret` vs Basic) — no such literals near the call.
- Rule selecting `Dropbox-Host-Key` vs `Bearer` per request/account.
- `config.dbx`/`instance.dbx` codec algorithm and keystore digest/key-wrap algorithm; derivation of `master`/`database_key`.
- Whether any OS keyring is used at all (no keyring strings observed in native libs).
- Precise value bound to `X-Dropbox-UID` (`uid` vs `account_id`) — uid and aid are distinct per assertion, Bearer/UID both present but binding not proven.
