## Transport & Wire Protocol — Rebuild Spec

Scope: everything a reimplementer must put on the wire to speak to Dropbox servers, and the local RPC runtime (`tprt`) that carries the same call model in-process and across Unix sockets. All evidence is from `corpus/str_libdropbox_core.so.txt` (core/Nucleus), `corpus/str_libdropbox_tprt.so.txt` (transport lib) and `corpus/api_tprt.txt` (FFI symbols). Note: `tprt.so` statically links OpenSSL 3.5.5; `libdropbox_core.so` contains the vendored `hyper-0.14.31` / `h2-0.3.26` HTTP/2 stack **and** the Dropbox `grpc_connection_2`, `connector`, `tls_connection`, `proxy_connection_2` crates. The gRPC wire constants live in **core**, not tprt.

### 0. Crate layout (observed source paths)

The transport is split across these crates (all `[OBS]`, paths embedded in panic strings):

| Crate / path | Role |
|---|---|
| `desktop/rust/dropbox/grpc_connection_2/src/{transport.rs, grpc_framing.rs, fifo.rs}` | gRPC length-prefixed framing + HTTP/2 transport glue |
| `desktop/rust/dropbox/connector/src/{lib.rs, plain.rs}` | TCP connector (threadpool `connector-thread…`) |
| `desktop/rust/dropbox/throttled_connector/src/lib.rs` | rate/permit-limited connector wrapper |
| `desktop/rust/dropbox/proxy_connection_2/src/{lib.rs, http_proxy/mod.rs, socks_proxy.rs}` | HTTP CONNECT + SOCKS proxy |
| `desktop/rust/dropbox/tls_connection/src/{lib.rs, imp.rs, openssl_conn.rs, native_tls_conn.rs}` | TLS over OpenSSL (primary) or native-tls |
| `desktop/rust/dropbox/hyper_tls_connection/src/lib.rs` | hyper↔TLS adapter |
| `desktop/rust/dropbox/system_certs/src/lib.rs` | system CA trust-store probing |
| `desktop/rust/dropbox/pb_service/src/lib.rs`, `pb_zerocopy/src/lib.rs` | protobuf service defs / zero-copy decode |
| `desktop/rust/dropbox/apiv2_client/src/client.rs` | REST/JSON apiv2 client (same connector stack) |
| `desktop/rust/nucleus/network/src/{transport.rs, connection.rs, connectivity.rs, meta.rs, auth.rs, block.rs, bolt.rs, ekms.rs, retry.rs, failure_manager.rs, reassociate.rs}` | Nucleus-side gRPC client, connection lifecycle, per-service calls |
| `desktop/app/lib/base/tprt/{factory/src/lib.rs, factory_c_api/src/lib.rs, wrappers/rust/tprt/src/{client.rs, server.rs, lib.rs}}` | the `tprt` RPC runtime + C ABI |

Vendored versions confirmed by embedded path strings: `hyper-0.14.31/src/proto/h2/client.rs` `[OBS]`, `h2-0.3.26` `[OBS]`, `openssl-0.10.73` `[OBS]`, `tokio-1.49.0` `[OBS]`, and the OpenSSL banner `OpenSSL 3.5.5 27 Jan 2026` `[OBS, tprt]`.

### 1. The `tprt` RPC runtime — call model and channel abstraction

`tprt` is a gRPC-shaped RPC runtime exposed over a C ABI (`api_tprt.txt`). It is transport-agnostic over two channel kinds `[OBS]`: `tprt_transport_type_dfc` and `tprt_transport_type_uds`.

**Client-side C ABI `[OBS, api_tprt.txt / tprt.so]`:**
- lifecycle: `tprt_client_new`, `tprt_client_free`, `tprt_client_stopped`, `tprt_connection_reset`
- calls: `tprt_client_request_unary`, `tprt_client_request_server_stream`
- cancellation: `tprt_client_request_handle_abandon` (caller-initiated cancel of an outstanding call)
- out-of-band: `tprt_client_register_invalidation_handler` (server/connection signals that cached state is stale)
- a unary completion callback symbol `tprt_client_unary_cb…`

**Server-side C ABI `[OBS]`:** `tprt_server_new/serve/cancel/done/err/free`, handler registration `tprt_server_register_unary_handler` and `tprt_server_register_server_stream_handler`, and per-call completion `tprt_server_unary_handle_{success,fail,abandon}` plus streaming `tprt_server_stream_handle_{item,done,fail,abandon}` and `tprt_server_stream_handle_register_invalidation_handler`. These confirm the **two call shapes**: *unary* (`success`/`fail`/`abandon`) and *server-streaming* (`item`* then `done`/`fail`/`abandon`).

**UDS variants** mirror the same surface `[OBS]`: `uds_tprt_channel_new/free`, `uds_transport_client`, `uds_transport_server`, `uds_tprt_client_request_unary`, `uds_tprt_client_request_server_stream`, `uds_tprt_server_register_{unary,server_stream}_handler`, `uds_tprt_server_stream_handle_{item,done,fail,abandon}`. [INF] UDS carries the identical gRPC call semantics over a Unix-domain socket for cross-process local IPC.

**DFC channel + factory `[OBS]`:** `dfc_tprt_channel_new`, `dfc_transport_pair`, and the Rust types `DfcTransport`, `ChannelType::dfc` (mangled `…ChannelType3dfc`, `…12DfcTransport…Channel13create_client`/`create_server`), `DfcSyncEngine`. The sync engine is wired through a **factory**: Rust type `TprtFactory` with methods `new`/`serve`/`teardown`/`send_unary`/`send_streaming` (mangled `11TprtFactory{3new,5serve,8teardown,10send_unary,14send_streaming}`), keyed by `TprtFactoryKey` → `AccountTprtConnection` (an `Arc`-shared per-account connection). The C entrypoints are `tprt_factory_send_sync_engine_dfc_unary` and `tprt_factory_send_sync_engine_dfc_streaming` `[OBS]`, with teardown `tprt_factory_teardown_sync_engine_dfc` / `teardown_sync_engine_from_factory` and `create_sync_engine_client_from_factory`. A deprecation note in the binary tells callers to "migrate to tprt_factory_send_sync_engine_dfc_unary/streaming" `[OBS]`.

**Queue/backpressure `[OBS]`:** the factory maintains a pre-serve unary queue — strings `tprt_factory: unary queue depth crossed`, `tprt_factory: draining pre-serve unary queue`, with fields `queue_depth`, `transport`, `service`. [INF] calls submitted before the channel is serving are buffered, and a depth watermark emits a metric. Internal request-tracking types `PendingUnary` / `TrackedUnaryRequest` `[OBS]`.

[INF] Model: Python/UI drives the Rust core over **DFC** (in-process framed channel); cross-process local helpers use **UDS**; and the same `grpc_connection_2` stack takes DFC/factory calls out to Dropbox servers over **HTTP/2**. `cffi_transport.TransportEventRequest` `[OBS]` is the DFC event envelope pumped by `cffi_transport_send_event`/`receive_event` (see nucleus_python FFI).

### 2. gRPC-over-HTTP/2 wire framing (`grpc_connection_2`)

Standard gRPC framing `[OBS/INF]`. The wire constants are defined together in one string blob in `grpc_connection_2`:

- **Content-Type:** `application/grpc+proto` `[OBS]` (binary proto). An alternate `application/grpc-web+proto` `[OBS]` is present in the same constant table — [INF] used for the gRPC-web transcoding path (works over HTTP/1.1, proxy-friendly).
- **Message frame `[OBS/INF]`:** classic gRPC — 1-byte compression flag + 4-byte big-endian length + message bytes. Evidence: `Unsupported compression flag:` and `gRPC framing error:` in `grpc_framing.rs`. [INF] unknown compression flags are rejected; default flag is `0` (identity).
- **Unary response assembly `[OBS]`:** exactly one DATA message is expected — errors `Expected a unary response but got multiple data frames` and `Expected a unary response but got nothing`, plus `Missing trailers`.
- **Server-stream response assembly `[OBS]`:** `server stream queue must start with Headers` and `poll_response called after …` — i.e. HEADERS, then N DATA frames (each one message), then trailers.
- **Trailers `[OBS]`:** `grpc-status`, `grpc-message`, `grpc-status-details-bin` (binary Status details), and the sentinel `Canceled`. Parsed into a Rust error struct with fields `request_id`, `grpc_status`, `grpc_message`, `grpc_status_details`, `transport_error` `[OBS]`.
- **Timeout `[OBS]`:** `grpc-timeout` header is set; `Invalid timeout` / `overflow when adding durations` are the construction errors.
- **TE requirement `[OBS]`:** `TE header not set to trailers; val=` and `TE headers not set to "trailers" are illegal in HTTP/2 r…` — the client MUST send `te: trailers`.

**gRPC status code enum `[OBS]`** (tonic/canonical order, recovered contiguously): `Ok, Unknown, InvalidArgument, …, AlreadyExists, ResourceExhausted, FailedPrecondition, Aborted, OutOfRange, Unimplemented, Unavailable, Unauthenticated`; plus `DeadlineExceeded` and `Canceled` observed separately. [INF] the usual gaps (Cancelled, NotFound, PermissionDenied, Internal, DataLoss) are present but fell outside the string window.

**Services/methods seen as `:path` values `[OBS]`** (Package.Service/Method → `:path` = `/Package.Service/Method`):
- `nsf.Nsf/{GetBlock, PutBlock, GetBlockSignature, GetRsyncBlock, PutRsyncBlock}` — block storage + rsync delta (server-bound, over HTTP/2)
- `nucleus.NucleusAPI/{GetSyncProgress, GetSyncEngineStatus, HydratePlaceholder, LookupByFileId, LookupByFileIdBatch, FetchByteRange, CancelRecall, …}`
- `nucleus.NucleusPhaseAgnosticAPI/{KeepAlive, BindIntoDropbox, CheckConsistency, …}` and `nucleus.ReverseNucleusAPI/SubscribeToBolt`
- `nucleus.DebugEngineNetwork/{CreateFile, FreezeNetwork, SetDeviceFolder, …}` (debug only)
- `fs_api.FsApi/{CreateFile, mergeFromDropbox, UnmergeFromDropbox, RenameIntoDropbox, bindFromDropbox, CreateTempVolume, CreateEphemeralTempDir, DeleteDeviceAnchor, GetPublishedEvents, …}` (local, UDS/DFC)
- `dropbox_meta_engine.SyncEngineApi/{GetSyncEngineStatus, LookupByFileId, LookupByLocalPath, UpdateHydrationPolicy}` (local)
- `application_metrics.AmpIngestion/Record`
- `ns.NetworkMutator/…`, `dir_fileid.DeletedFilesManager/resurrectListing`, `cffi_transport.TransportEventRequest`

### 3. Exact HTTP/2 request shape a reimplementer must send

For a server-bound gRPC unary call (e.g. `nsf.Nsf/GetBlock`), open an HTTP/2 stream and send a HEADERS frame then one length-prefixed DATA frame. Pseudo-headers in h2 canonical order `[OBS: literal ":authority:method:scheme:path:protocol" in core]`:

```
:method = POST
:scheme = https
:authority = <logical host, e.g. client.dropbox.com or bolt.dropbox.com>
:path = /nsf.Nsf/GetBlock          # "/" + Package.Service + "/" + Method
```

Regular headers (observed constants; exact casing as emitted):
```
content-type: application/grpc+proto          # [OBS]
te: trailers                                  # [OBS] REQUIRED
grpc-timeout: <n><unit>                        # [OBS] optional deadline
user-agent: Dropbox-lnx.x86_64-274.4.4905…     # [OBS] "Dropbox-lnx" prefix
Dropbox-Host-Key: <host_int secret>           # [OBS] desktop host-key auth
X-Dropbox-UID: <account uid>                  # [OBS]
X-Dropbox-App-Name: <app>                     # [OBS]
X-Dropbox-App-Version: <ver>                  # [OBS]
X-Dropbox-User-Agent: dropbox-desktop274.4.4905stable  # [OBS] (version + "stable" channel)
Dropbox-API-User-Locale / X-Dropbox-Locale    # [OBS]
X-Dropbox-Path-Root: <root ns>                # [OBS]
X-Dropbox-Traffic-Tier: <tier>                # [OBS]
X-Dropbox-Request-Id: <uuid>                  # [OBS] (x-dropbox-request-id; dbx_uuid crate)
X-Dropbox-Force-Request-Tracing / X-Dropbox-Metro-Pref / X-Dropbox-Backend  # [OBS] optional
```
The exact client-version token `dropbox-desktop274.4.4905stable` is emitted by core `[OBS]` — it is `dropbox-desktop` + version + release channel (`stable`), carried in `X-Dropbox-User-Agent`. The DATA frame body is `[00][len:u32-be][protobuf]`. The response is HEADERS (`:status 200`, `content-type: application/grpc+proto`), one DATA frame, then a trailers HEADERS frame carrying `grpc-status`/`grpc-message`/`grpc-status-details-bin`.

**apiv2 REST path (same connector/TLS stack, different framing) `[OBS]`:** `apiv2_client/src/client.rs` issues `POST` with `content-type: application/json` (also `application/octet-stream` for binary like thumbnails), authenticated via `Authorization: Bearer <access_token>` `[OBS: "Bearer " and "[OAuth] Failed to retrieve access token"]`, plus `X-Dropbox-Path-Root` and `X-Dropbox-Traffic-Tier`. Endpoints seen `[OBS]`: `/2/ekms/{get_file_keys, get_namespace_key, register_client, register_file_key_batch, get_team_public_key, get_pending_clients, enroll_clients, …}`, `/2/files/get_thumbnail_batch`, `/2/stormcrow_servicer/get_assignments`, `/2/wopi/{get_wopi_metadata, get_file_checksum, is_coauth_supported_for_user}`, and the legacy long-poll `/2/notify/subscribe` (emitted with `Connection: keep-alive` `[OBS: "keep-aliveX-Dropbox-UID/2/notify/subscribe"]`). [INF] apiv2 uses OAuth bearer; the desktop sync gRPC path uses the `Dropbox-Host-Key` header.

### 4. TLS & ALPN (`tls_connection`, `system_certs`, OpenSSL 3.5.5)

- TLS is primarily OpenSSL (`tls_connection/src/openssl_conn.rs`) with a `native_tls_conn.rs` alternative `[OBS]`; the hyper adapter is `hyper_tls_connection` `[OBS]`.
- **ALPN `[OBS]`:** client advertises `h2`; `ALPN must be configured when using` (hyper's h2-requires-ALPN guard), and on success `ALPN upgraded to HTTP/2` / `alpn_selected`. If `h2` is not negotiated the connector falls back: `upgrade_h2 with Fallback::Http1Only`, `Fallback to http 1.1`, `Negotiated unsupported protocol`, `no application protocol negotiated` `[OBS]`. So the reimplementer MUST offer ALPN `h2` and may negotiate HTTP/1.1 as fallback.
- **Trust store `[OBS]`:** `system_certs/src/lib.rs` probes OpenSSL-style roots — `SSL_CERT_DIR`, `certs/ca-certificates.crt`, `certs/ca-root-nss.crt`, `certs.pem`, `bundle.pem` — i.e. standard openssl-probe locations. Hostname verification and cert-chain verification via OpenSSL (`X509_STORE_CTX…`, server CertificateVerify). OpenSSL banner `OpenSSL 3.5.5 27 Jan 2026` `[OBS, tprt]`. [INF] certificate pinning not evidenced in strings → [UNK] whether any pin is applied.

### 5. Connection management (`connector`, `throttled_connector`, `proxy_connection_2`, backoff)

- **Connector `[OBS]`:** `connector/src/lib.rs` runs a dedicated `connector-thread…` pool; `connect timeout`, `failed to connect to server`, `connect error`/`connect failure` are the outcomes. Plain-TCP variant `connector/src/plain.rs`.
- **Throttled connector `[OBS]`:** `throttled_connector/src/lib.rs` + `throttler/src/rate_controlled_asio.rs`. Permit-based gate: `MAX_PERMITS`, `cannot add more than MAX_PERMITS permits`, `MINIMUM_THROTTLING_FACTOR_VALUE <= self.throttling_factor`, `throttling_factor <= 1.0`. Server-driven throttle config: `ThrottleMode` (`ThrottleModeHttpProxyHeader`), `FlatThrottleSettings` (`bps`), error `RateLimited` `[OBS]`. [INF] a semaphore caps concurrent connections and a server-supplied throttling factor (0..1, in bits/sec) rate-limits.
- **Proxy `[OBS]`:** `proxy_connection_2` supports HTTP CONNECT and SOCKS. HTTP: `CONNECT %s:%s HTTP/1.0`, `%s: HTTP CONNECT %s`, `HTTP/1.1 CONNECT request stripping path:`, `Invalid CONNECT request`, proxy auth `Proxy-Authorization: Basic %s`, `Proxy-Connection: Keep-Alive`. SOCKS: `socks_proxy.rs`, tokens `Socks`/`Socks5`. Env vars read: `HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY` (+ lowercase) `[OBS]`; `ELECTRON_PROXY_S…` suggests Electron proxy settings are also consulted `[OBS]`.
- **Backoff/retry `[OBS]`:** `nucleus/network/src/retry.rs` + `failure_manager.rs`. Counter path `backoff/retry/num_tries`, a geometric multiplier (`mult >= 0.0`), fields `elapsed_backoff`, `backoff_cumulative`, and a transient/permanent classification `Transient`/`Retryable`/`Nontransient`/`Perm…`. [INF] exponential backoff with jittered multiplier gating reconnects and retriable gRPC statuses.
- **HTTP/2 lifecycle (h2-0.3.26 internals, `[OBS]`):** SETTINGS (`header_table_size`, `enable_push`, `max_concurrent_streams`, `initial_window_size`, `max_frame_size`, `max_header_list_size`; `received settings ACK; applying`), flow control (`update_initial_window_size`, `recv_stream_window_update`, `WINDOW_UPDATE`), `RST_STREAM`, `GOAWAY` (`GOAWAY stream IDs shouldn't…`, reason enum `ResetGoAwayReasonIo` / `ServerPushResetGoAway`), and PING keepalive (`conn.ping_pong`, `recv PING ack that we never s…`, `keep-alive`). Application-level reconnect reasons: `ClientInitiatedReconnect` / `CLIENT_INITIATED_RECONNECT`, `DEPRECATED_CLIENT…`, `SERVER_PUSH` `[OBS]`. Connectivity surfaced as `NetworkConnectivity` / `EngineConnected` / `EngineDisconnected` (`nucleus/network/src/connectivity.rs`) `[OBS]`.

### 6. Bolt reverse-stream (push channel over the same transport)

[OBS] `nucleus.ReverseNucleusAPI/SubscribeToBolt` returns `SubscribeToBoltReply`; the credential is `BoltChannelToken` (proto struct, variants with 3 and 5 fields) carrying fields `channel_id`, `token`, `app_id`, `unique_id`. Host `bolt.dropbox.com`; crate `nucleus/nucleus_bolt_connection/src/lib.rs` and `nucleus/network/src/bolt.rs`. [INF] Bolt is a long-lived **server-streaming** gRPC call (reverse direction) that pushes change signals; `NucleusPhaseAgnosticAPI/KeepAlive` keeps it alive. The `tprt_client_register_invalidation_handler` hook is [INF] how the client reacts to Bolt-driven invalidation.

### 7. protobuf layer
`pb_service/src/lib.rs` holds service/method descriptors; `pb_zerocopy/src/lib.rs` provides zero-copy decode of proto messages off the gRPC DATA frames `[OBS]`. Python side decodes via `google._upb._message` (upb). [INF] message bodies are standard proto3 wire format; the reimplementer needs the `.proto` schemas for each service above (not recoverable from strings → [UNK]).

### Key uncertainties
- Exact gRPC message max size / whether gRPC-level compression (gzip/br) is ever negotiated (only `identity`/flag-0 evidenced; brotli present but used by block/content compression and HTTP content-encoding, not proven as a gRPC `grpc-encoding`).
- Exact HTTP/2 SETTINGS values (window/frame sizes) Dropbox sends — only the parameter names are observable, not the numeric defaults chosen over hyper's.
- Binding rule between `Dropbox-Host-Key` (sync gRPC) and OAuth `Bearer` (apiv2) per request — [UNK].
- Full `.proto` field layouts for every service/method.