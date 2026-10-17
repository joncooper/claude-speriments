# Dropbox Linux client — reverse-engineering evidence base

**Target:** official Dropbox Linux client, version **274.4.4905** (x86_64), downloaded
from `https://www.dropbox.com/download?plat=lnx.x86_64` →
`https://edge.dropboxstatic.com/dbx-releng/client/dropbox-lnx.x86_64-274.4.4905.tar.gz`.
tarball sha256 `c450ec3e659a4ab556b73304e075d2a5655faf891e085ad178e4282c727ec96a`.
Analysis = **static only** (never executed). Date 2026-10.

Convention: **[OBS]** = directly observed string/symbol in the binaries;
**[INF]** = inference from observed evidence + known OSS crate behavior;
**[UNK]** = not determined from static evidence.

Raw corpus files (stable, on disk):
- `corpus/str_libdropbox_core.so.txt`  — strings -n6 of core (138k lines)
- `corpus/str_libdropbox_tprt.so.txt`  — strings -n6 of transport (32k lines)
- `corpus/modules.txt`                 — 2858 dropbox/apex Python module names
- `corpus/api_tprt.txt`, `api_nucleus_python.txt`, `api_fs_api_python.txt` — FFI identifiers
- `dropbox-dl/extract/.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/` — the extracted client
- `dropbox-dl/py/` — the 3661 extracted (encrypted) .pyc files

---

## 1. Package inventory [OBS]

Distribution root `.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/`:

| File | Size | Role |
|---|---|---|
| `dropbox` | 10 KB | ELF PIE launcher (stripped) |
| `dropboxd` | 425 B | /bin/sh env wrapper → `exec dropbox "$@"` |
| `libdropbox_core.so` | 64 MB | Rust **Nucleus** sync engine + apex core (cdylib, 525 dynsyms) |
| `libdropbox_tprt.so` | 11 MB | **transport** (gRPC/HTTP2) + statically-linked OpenSSL 3.5.5 |
| `libpython3.11.so.1.0` | 17 MB | modified CPython 3.11 (custom pyc magic + encrypted marshal) |
| `python-pypkg.zip` | 54 MB | 3661 `.pyc` (stdlib + `dropbox/*`, `apex/*`) — **encrypted bodies** |
| `python-pyext/*.so` | — | 20 native CPython ext modules (Cython + Rust FFI) |
| `libdropbox_sqlite_ext.so` | 6 KB | SQLite loadable extension (encrypted-DB codec) |
| `libffi.so.8.1.2`, `libatomic.so.1` | — | bundled deps |

Native Python extensions of interest (`python-pyext/`):
`tprt.cpython-311`, `nucleus_python.cpython-311`, `fs_api_python.cpython-311`,
`cryptography.hazmat.bindings._rust.abi3` (pyca/cryptography 10 MB),
`google._upb._message` (protobuf), `fastpath`, `apex._apex`, `allocator_metrics`,
`linuxffi_*`, `posixffi_libc_native`, `linuxinfinite_native`, `nucleus_python`.

## 2. Python obfuscation posture [OBS]

- `.pyc` magic = `b7 34 0d 0a` (stock 3.11 = `a7 0d 0d 0a`). Custom magic.
- `marshal.loads(body[16:])` on dropbox/stdlib pyc → `ValueError: bad marshal data
  (unknown type code)` under stock py3.11 → **marshal type codes remapped**.
- `strings` of `apex/auth.pyc` etc. = high-entropy garbage → **pyc payloads are
  encrypted**; the modified `libpython3.11.so.1.0` decrypts at import.
- Consequence: Python source is **not recoverable** without first recovering the
  interpreter's decrypt routine + marshal/opcode maps from `libpython3.11.so`. The
  protocol/session logic is overwhelmingly in the **native Rust libs**, which are
  stripped but unencrypted and carry rich embedded source paths / panic strings.

## 3. Native architecture (from embedded Rust source paths + panic msgs) [OBS]

Build root `desktop/`. Three Rust layers:

**(a) apex** = application framework (`desktop/app/lib/apex/`), C-API in
`apex/c_api/src/{analytics,auth,auto_updater,config,context,dbxauth,dbxconn,dbxlog,
health,http_client,keystore,metrics,stormcrow,util}` and Rust impl in
`apex/rust/{analytics,auth,auto_updater,context,dbxauth,dbxconn,dbxlog,http_client,
keystore,metrics,metrics_impl,store,stormcrow}`.
- `auth` + `dbxauth` = **authentication client**
- `keystore` (+`posix`) = **OS credential storage**
- `dbxconn` (+`server_map`) = **connection + server map (DROPBOX_HOST)**
- `stormcrow` = feature flags; `auto_updater/linux`; `dbxlog` (redaction + file/crypto)

**(b) nucleus** = sync engine (`desktop/rust/nucleus/`). Crates incl:
`protocol`(+`states`), `network`, `nucleus_bolt_connection`, `remote_command`,
`remote_canopy`, `remote_service`, `remote_file_information`, `canopy`,
`canopy_scheduler`, `planning`, `pre_local`, `tree`, `tree_diff`, `mount_table`,
`device_anchor`, `coauth`(+`coauth_types`), `encryption`, `smart_sync`,
`instant_files`, `block_transfer`(+`_types`), `block_source`, `block_finder`,
`block_compression`, `local_block_cache`, `local_block_index`, `fileid_manager`,
`nucleus_path`, `database`, `platform_db`, `fs`, `fs_engine`(+`_phases`,
`_scheduler`,`_operating_modes`), `fs_common`, `fsw` (fs watcher), `migration`,
`conflict`, `resync`, `sync_issues`, `intent_manager`, `link_container`,
`reassociate`, `recall_tracker`, `segments`, `dbxignore`, `deleted_files_manager`.

**(c) dropbox** shared crates (`desktop/rust/dropbox/`):
`grpc_connection`, `pb_service`, `pb_zerocopy`, `connector`, `throttled_connector`,
`proxy_connection`, `hyper_tls_connection`, `tls_connection`, `system_certs`,
`bolt`, `apiv`, `remote_service`, `batcher`, `cyclotron`, `obfuscation`,
`dbx_uuid`, `hash_functions`, `dbx-async`, `dbx-collections`, `sqlite_migrate`.

**Vendored OSS (pin exact wire behavior) [OBS]:**
`hyper-0.14.31`, `h2-0.3.26` (HTTP/2), `http-0.2.8`, `httparse-1.8.0`,
`tokio-1.49.0`, `tokio-openssl-0.6.1`, `tokio-native-tls-0.3.0`, `tokio-util-0.7.4`,
`openssl-0.10.73` → **OpenSSL 3.5.5 (27 Jan 2026)** statically in tprt,
`rusqlite-0.39.0`, `serde-1.0.215`, `serde_json-1.0.133`,
`brotli-5.0.0`/`brotli-decompressor-4.0.0`, `regex-automata-0.4.9`,
`aho-corasick-1.1.3`, `quick-xml-0.32.0` (WOPI/WebDAV XML).
Rust toolchain commit `c871d09d1cc32a649f4c5177bb819646260ed120`.

## 4. Process & transport model [OBS/INF]

FFI identifiers (`api_*.txt`):
- **tprt** C-ABI (gRPC RPC): `tprt_client_new/free`,
  `tprt_client_request_unary`, `tprt_client_request_server_stream`,
  `tprt_client_request_handle_abandon`, `tprt_client_register_invalidation_handler`,
  `tprt_client_stopped`, `tprt_connection_reset`; server side
  `tprt_server_new/serve/cancel/done/err`, `tprt_server_register_unary_handler`,
  `tprt_server_unary_handle_{success,fail,abandon}`.
- Two transport types: `tprt_transport_type_dfc`, `tprt_transport_type_uds`.
  Channels: `dfc_tprt_channel_new`, `dfc_transport_pair`, `uds_tprt_channel_new/free`,
  `uds_transport_client`, `uds_transport_server`.
- Factory for sync engine: `create_sync_engine_client_from_factory`,
  `tprt_factory_send_sync_engine_dfc_unary`, `tprt_factory_teardown_sync_engine_dfc`,
  `teardown_sync_engine_from_factory`.
- **nucleus_python**: `sync_engine_create`, `apex_context`, `poll_fp_dfc`,
  `free_dfc_response`, `cffi_transport_{send_event,receive_event,
  receive_event_queue_len,destroy,stop}`, `register_event_logger`,
  `report_nucleus_event`, `report_exception`.
- **fs_api_python**: `fs_api_create`, `cffi_transport_{send_event,stop,destroy}`.

[INF] Model: a Python control/UI process drives a Rust core. `tprt` is a gRPC-style
RPC runtime offering **unary** and **server-streaming** calls over two channel kinds:
- **DFC** = in-process framed channel (Python ⇄ Rust core, and to servers). Events
  pumped via `cffi_transport_send_event`/`receive_event` + `poll_fp_dfc`.
- **UDS** = Unix-domain-socket channel for cross-process local IPC (sync engine ⇄
  other local processes / helpers).
Processes seen: `dropbox.client.main`, `dropbox.client.main_utility` [OBS].

## 5. Wire protocol = gRPC over HTTP/2 + TLS [OBS]

- Content-Type `application/grpc+proto` [OBS]; trailers `grpc-status`,
  `grpc-message`, `Canceled` [OBS]; HTTP/2 pseudo-headers `:path :authority
  :method :scheme :status` [OBS].
- Carried by vendored `h2-0.3.26` + `hyper-0.14.31`; TLS by `openssl-0.10.73`
  (OpenSSL 3.5.5) via `hyper_tls_connection`/`tls_connection`/`system_certs`;
  connection mgmt via `connector`/`throttled_connector`/`proxy_connection`.
- Protobuf: `pb_service` (service defs), `pb_zerocopy` (zero-copy decode);
  Python side has `google._upb._message`.

**gRPC services/methods recovered from `:path` strings [OBS]:**
- `dropbox_meta_engine.SyncEngineApi/` : `GetSyncEngineStatus`, `LookupByFileId`,
  `LookupByLocalPath`, `UpdateHydrationPolicy`
- `fs_api.FsApi/` : `mergeFromDropbox`, `UnmergeFromDropbox`, `RenameIntoDropbox`,
  `bindFromDropbox`, `DeleteDeviceAnchor`, `CreateEphemeralTempDir`,
  `CreateTempVolume`, `CreateFile`, `CreateBreadcrumbs`/`RemoveBreadcrumbs`,
  `GetPublishedEvents`/`ExtPublishedEvents`
- `nsf.Nsf/` : `GetBlock`, `PutBlock`, `GetBlockSignature`, `GetRsyncBlock`,
  `PutRsyncBlock`  ← **block storage + rsync delta protocol**
- `nucleus.DebugEngineNetwork/` : `CreateFile`, `CreateDirectory`, `ConvertToMount`,
  `FreezeNetwork`, `PurgePath`, `SetDeviceFolder` (test/debug only)
- `application_metrics.AmpIngestion/Record`
[INF] `SyncEngineApi`/`FsApi` run over **UDS/DFC** (local); `nsf.Nsf` + sync
protocol run over **DFC→HTTP/2** to Dropbox servers.

**Dropbox HTTP headers [OBS]:** `Dropbox-Host-Key`, `X-Dropbox-UID`,
`X-Dropbox-Path-Root`, `X-Dropbox-Traffic-Tier`, `X-Dropbox-Request-Id`,
`X-Dropbox-App-Name`, `X-Dropbox-App-Version`, `X-Dropbox-User-Agent`,
`Dropbox-API-User-Locale`, `X-Dropbox-Locale`, `X-Dropbox-Force-Request-Tracing`,
`X-Dropbox-Metro-Pref`, `X-Dropbox-Backend`, `User-Agent` (`Dropbox-lnx.x86_64-274…`).

## 6. Server topology [OBS]

Embedded `DROPBOX_HOST` map (schema: `Server Name: {}, Host: {}, Port: {}`,
fields `server.server_name`, `server.host.host_name`):

| logical server | host |
|---|---|
| webserver | www.dropbox.com |
| metaserver | client.dropbox.com |
| authserver / apiv2server | api.dropbox.com |
| metaexcserver (meta exception) | d.dropbox.com |
| blockexcserver (block exception) | dl-debug.dropbox.com |
| t8 | t8.dropbox.com |
| d6 | d6.dropbox.com |
| staticserver | cfl.dropboxstatic.com |
| boltserver | bolt.dropbox.com |
| (WOPI/Office) | wopi.dropbox.com |

Server map code: `apex/rust/dbxconn/src/server_map`.

## 7. Session & authentication [OBS/INF]

- **Host-key model** [OBS/INF]: `Dropbox-Host-Key` header + `X-Dropbox-UID`;
  tokens `host_id`(9), `host_int`(6). Classic desktop pairing: device holds a
  host_id (public) + host_int (secret host key); authenticates requests via
  `Dropbox-Host-Key`.
- **Device registration** [OBS]: `RegisterClient`/`RegisterClientResponse` RPC;
  `link_*`(29) linking vocabulary; `machine_id`(8), `session_id`(11).
- **coauth / OAuth2** [OBS]: `apex/rust/auth`, `dbxauth`; `refresh_token`,
  `access_token`, `bearer`, `oauth2`. NOTE: the heavy `coauth`(54) hits are mostly
  the **encrypted-folder** key-exchange subsystem (see §9), not session auth —
  keep the two distinct. [INF] OAuth tokens likely used for apiv2/auth-server
  flows; host key for the desktop sync protocol. Exact binding = [UNK].
- **Credential storage** [OBS]: `apex/rust/keystore/{lib,posix}` + apex c_api
  `keystore` → OS keystore (libsecret/keyring) with file fallback; durable config
  in encrypted `config.dbx` (§8).
- **device_anchor** [OBS]: `device_anchor`(91), `device_anchor_path`,
  `device_anchor_fileid`, xattr `com.dropbox.device_anchor`. [INF] a per-device
  marker/fileid anchoring the local Dropbox folder to this device+account (identity
  + anti-relocation), distinct from the network session credential.

## 8. Local persistence [OBS]

Encrypted SQLite (`.dbx`) via `libdropbox_sqlite_ext.so` codec (`codec`×117,
`EncryptedPrivateKeyInfo`×64). Files: `config.dbx`, `instance.dbx`,
`nucleus.sqlite3`, `apex.sqlite3`, `index.sqlite`, `Vault.db`,
`binfilehistorytoolkit.dbx`, `dropboxignore.dbx`, `dbxignore_*.dbx`, `Q.sqlite`,
`vacuum_db.sqlite`, `fp_shadow_copy_nucleus.sqlite3`.
Tables incl. `config`, `fp_local_tree`, `transplant`, `update_info`.
PRAGMAs: `journal_mode`(WAL), `synchronous`, `secure_delete`, `locking_mode`,
`wal_autocheckpoint`, `page_size`, `auto_vacuum`, `cache_size`, `fullfsync`.

## 9. Sync engine protocol (Nucleus) [OBS/INF]

- **Protocol state machine** `nucleus/protocol/src/states/`: `subscribe`, `list`,
  `commit`, `commit_ack`, `mod` [OBS]; states incl. `InitialState`,
  `LocalTransactionState`, `Get/SetResyncState`, `PropagateUncommittableState`.
  [INF] Per-namespace loop: **subscribe** (register for change notifications) →
  **list** (pull remote metadata delta by cursor) → **commit**/**commit_ack**
  (push local changes, await server ack).
- **Namespaces/mounts** [OBS]: `ns_id`(73), `mount_table`, `home_ns_fileid`,
  mount/unmount logic; `nucleus/canopy` = the synced tree; `tree_diff`, `planning`
  (sync plan), `pre_local` (apply-to-disk constraints).
- **Blocks** [OBS]: `nsf.Nsf/{GetBlock,PutBlock,GetBlockSignature,GetRsyncBlock,
  PutRsyncBlock}`; `blocklist`(105), `block_hash`, `content_hash`, `SHA256`(167),
  `BLAKE`(20), `chunk`/`chunked`, `commit_batch`, `block_compression`,
  `local_block_cache`, `local_block_index`. [INF] Files split into blocks (Dropbox
  classic = 4 MiB), each hashed (SHA256 historically; BLAKE present); file = ordered
  blocklist; delta updates via rsync signatures/blocks; blocks compressed; cached
  locally.
- **Notifications (Bolt)** [OBS]: `bolt.dropbox.com`, `nucleus_bolt_connection`,
  `BoltChannelToken`, `subscribeToBolt`, `bolt_request`, `bolt_migration`,
  `dropbox/bolt`. [INF] Bolt is the long-lived push channel: client holds a
  BoltChannelToken, subscribes per namespace; server pushes change signals that
  drive the `list` phase. Replaces the legacy `notify` long-poll.
- **Encrypted folders / Vault** [OBS]: `coauth`(54), `coauth_request`,
  `coauth_metadata`, `GetFileKeys`, `RegisterFileKeyBatch`, `GetNamespaceKey`,
  `TeamKeyListWithClientKey`, `IsCoauthSupportedForUser`, `encrypted_folder`,
  `file_key`, `encrypting_keys`, `encryption_scheme`, `encrypted_key_data`,
  `EncryptedPrivateKeyInfo` (PKCS#8), `Vault.db`. [INF] per-file content keys
  wrapped by namespace/team keys; client registers file keys; key hierarchy
  separate from transport TLS.

## 10. Open questions / [UNK]
- Exact host_int derivation and the OAuth-vs-host-key request binding.
- config.dbx codec algorithm + key source (keystore vs derived).
- DFC frame format details (header layout) beyond "gRPC-over-HTTP/2".
- Bolt subscribe/token wire format.
- Exact block size + whether SHA256 or BLAKE3 is the current content hash.
