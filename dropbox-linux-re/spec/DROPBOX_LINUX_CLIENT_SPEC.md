# Dropbox Linux Client — Reverse-Engineering & Rebuild Specification

**Target:** official Dropbox Linux desktop client **274.4.4905** (x86_64),
interpreter branch `dbx-desktop-v3.11.14`.
**Acquired:** `https://www.dropbox.com/download?plat=lnx.x86_64` →
`dropbox-lnx.x86_64-274.4.4905.tar.gz` (sha256 `c450ec3e…c727ec96a`).
**Method:** static analysis of the shipped binaries (native libs via strings +
embedded Rust source paths/panic messages + targeted disassembly) and
**de-obfuscation of the Python layer via the client's own interpreter used as a
decryption oracle** (§9). The client was never run as a product; no Dropbox
application module was executed (code objects were deserialized, not run).
**Purpose:** interoperability / architecture understanding.

**Evidence tags:** `[OBS]` observed string/symbol in a binary · `[INF]` inferred
from observed evidence + known behavior of a named vendored crate · `[UNK]` not
determined statically.

## Confidence & corrections (from an adversarial verification pass)

Each section below was authored from the evidence corpus and then independently
re-checked against that corpus. Net corrections applied to the first-pass text:

- **Session/auth:** `RegisterClient` is **EKMS encrypted-folder key enrollment,
  not device registration** — the host-key/`host_int` minting and the full device
  link handshake are **not** present in the native strings (they live in the
  now-decrypted Python layer, §9/§10). The posix keystore is a **file-based store
  (base64 + JSON + digest)**, not libsecret/gnome-keyring (no keyring backend
  strings exist). `Dropbox-Host-Key` vs OAuth `Bearer` per-request selection is
  `[INF]`. `ping_sfe` is `[INF]`; `bolt_subscribe`/`upload_block`/
  `commit_at_head`/`download_block` are `[OBS]`.
- **Transport:** `throttling_factor ∈ [MIN, 1.0]` is `[OBS]`; "server-driven" is
  `[INF]`. Exact HTTP/2 SETTINGS values and any TLS pin policy are `[UNK]`.
- **Endpoints:** the server map being **persisted** into the Apex config DB is
  `[INF]` (the DB and a "recreated the Apex database" log are `[OBS]`).
- **Sync:** real mount invariants are `mounted_nses ⊆ fileid_nses`,
  `mounted_nses ⊆ mountable_nses`, `fileid_nses ⊆ known_nses`. PNM forms are
  `EncryptedFileFilePNM`/`EncryptedFileDirectoryPNM` (no `EncryptedFilePNM`,
  no `DeviceInfoPNM`). `NeedBlocks{blocks:[…]}` is `[OBS]`; "hashes for upload"
  is `[INF]`.
- **Blocks:** the **4 MiB block size is `[INF]`** (no size literal found; a
  `1048576`/1 MiB literal and a 64 KiB rsync-delta threshold are observed);
  `block_hash` length 32 is `[INF]` from SHA-256.
- **Bolt:** `boltserver → bolt.dropbox.com` is an `[INF]` mapping (both tokens
  observed; it is the only bolt-named host).

Consolidated unknowns are in §10.

---
## Architecture & Process Model (Dropbox Linux client 274.4.4905)

This section specifies how to decompose a reimplementation into processes, native build
layers, a Python control plane, and the in-process RPC bridge that joins them. The
client is **one native host process that embeds CPython**; it is not a Python program
that loads native libraries. Everything below is grep-findable in
`corpus/str_libdropbox_core.so.txt` (core) and `corpus/str_libdropbox_tprt.so.txt`
(tprt) unless noted.

---

### 1. Process topology

**1.1 Launcher chain `dropboxd` → `dropbox` → `libdropbox_core.so`** [OBS]
- `dropboxd` is a 425-byte `/bin/sh` environment shim (read directly from disk at
  `.dropbox-dist/dropbox-lnx.x86_64-274.4.4905/dropboxd`). It computes
  `PAR=$(dirname "$(readlink -f "$0")")`, snapshots `OLD_LD_LIBRARY_PATH` (so a
  re-exec'd child's `LD_LIBRARY_PATH` is not corrupted), clears `QT_PLUGIN_PATH=` and
  `QT_STYLE_OVERRIDE=`, then `exec "$PAR"/dropbox "$@"`. A reimplementer must reproduce
  the env sanitation and the idempotent re-exec. [OBS]
- `dropbox` is a ~10 KB stripped ELF PIE whose rpath is `${ORIGIN}:${ORIGIN}/../lib`
  and whose only non-libc undefined symbols are three functions it imports from
  `libdropbox_core.so`: **`bootstrap_application`**, **`bootstrap_run_application`**,
  **`bootstrap_cleanup_application`** [OBS] (launcher UND symbols; the same three names
  appear as exported tokens in the core string table). The launcher is therefore a
  thin `main()` that does `bootstrap_application(argc,argv)` →
  `bootstrap_run_application()` → `bootstrap_cleanup_application()`. [INF]

**1.2 Native host owns the run loop; CPython is embedded, not hosting** [OBS]
The bootstrap crate lives at `desktop/app/lib/core/bootstrap/src/` with modules
`lib.rs`, `cmdline.rs`, `context.rs`, `python.rs`, `electron/mod.rs`,
`electron/linux.rs` [OBS]. It carries a `BootstrapConfig` struct with fields
`runloop_type`, `build_config`, `native_init_hook_fn`, a run-loop enum with variants
`NativeEventLoop` and `ElectronLibrary`, a `BootstrapCommandArgs` type and a `Utility`
command [OBS: token `BootstrapConfigrunloop_typebuild_confignative_init_hook_fnNativeEventLoopElectronLibraryBootstrapCommandArgsUtility`].
A sibling `BootstrapBuildConfig` carries `frozen`, `win_full_msix`, `store_managed`,
`disable_gpu`, `meta_engine_rpc` [OBS: token `BootstrapBuildConfigfrozenwin_full_msixstore_manageddisable_gpumeta_engine_rpc`].

**1.3 Ordered bootstrap sequence** [OBS] (recovered verbatim from one contiguous
string run; a reimplementer should follow this order):
1. `Setting up panic handler with Crashpad` — Google Crashpad minidump handler is
   installed first; panic annotations `crashpad_load_status`, `panic_info`,
   `panic_line`, `panic_file`, and marker `RUST PANICKING` are attached. [OBS]
2. `Setting up apex context` → `Apex context set up, progressing with bootstrapping`
   (error branch: `couldn't fetch path to current process`, `corruptdb_apex`,
   `failed to restart process with /corruptdb_apex`). [OBS]
3. `Calling back into entry point for extra configuration` — this is the
   `native_init_hook_fn` callback into the launcher/caller. [OBS/INF]
4. `Setting up Python runtime` (error: `Failed to initialize Python runtime`). [OBS]
5. `Setting up Electron runtime` / `NOT setting up Electron runtime`. [OBS]
6. `Setting up watchdog` / `NOT setting up watchdog`. [OBS]
7. `Bootstrapping Python`. [OBS]
8. Dispatch into one of three run modes: `Running native application loop` /
   `Running Electron application framework` / `Running Dropbox CLI`
   (`Dropbox CLI panicked`, `Finished Dropbox CLI`, `Failed to parse Dropbox CLI
   arguments`). [OBS]
9. `Application Cleanup: notifying watchdog of clean termination`. [OBS]

**1.4 Python is entered through literal `exec`-string imports** [OBS]
The native host drives Python by compiling and running these exact statements (found as
string literals in core):
- `import dropbox.client.main as _main; _main.main()` — primary daemon entry. [OBS]
- `import dropbox.client.main as _main; _main.linux_event_loop()` — Linux run-loop
  variant used under the native/Electron loop. [OBS]
- `import dropbox.client.main_utility as _main; _main.main_utility()` — the **utility
  process** entry; guarded by `Unexpected return of \`main_utility()\``. [OBS]
The embedding uses the CPython C-API: `Py_Initialize`, `PyImport_AddModule`,
`PyImport_Import` are present in core [OBS]. A reimplementer embeds CPython and invokes
these module entry points rather than running `python main.py`.

**1.5 Process roles** [OBS/INF]
- **`dropbox.client.main`** = the main sync daemon process (hosts the Rust Nucleus sync
  engine in-process plus the Python control plane). [OBS name + INF role]
- **`dropbox.client.main_utility`** = a secondary/utility process spawned by the main
  one [OBS name]. Its exact job is [UNK] from strings, but the `Utility` bootstrap
  command and the separate entry point show it reuses the same host binary with a
  different Python entry (classic "one binary, mode by argv"). [INF]
- Run modes are selected by `runloop_type`: a headless `NativeEventLoop`, an
  `ElectronLibrary` GUI loop, or the one-shot `Dropbox CLI`. [OBS]
- A **Crashpad** handler and a **hang-detection watchdog**
  (`desktop/rust/nucleus/engine_common/src/watchdog.rs`, `engine_common::watchdog`,
  `Hang detection watchdog running...`, `last_observed_hang_state`,
  `fs_engine_phases::watchdog`) run alongside. [OBS]

**1.6 Relevant command-line flags** [OBS] (from clap/Chromium-style flag strings):
`use-meta-engine-rpc`, `crashpad-annotations`, `disable-static-cert-pinning`,
`windows-full-msix`, and the Electron asset bundle `local_views.zip`; Electron/Chromium
flags `--client-install-data=`, `--vmodule=*/components/update_client/*=`. [OBS]

---

### 2. The three Rust build layers (build root `desktop/`)

A reimplementation should keep these three concentric layers; each is a distinct crate
family with its own C-ABI surface.

**(a) apex — application framework** (`desktop/app/lib/apex/`). C-API crates under
`apex/c_api/src/` observed: `analytics.rs`, `auth.rs`, `auto_updater.rs`, `config.rs`,
`context.rs`, `dbxauth.rs`, `dbxconn.rs`, `dbxlog.rs`, `health.rs`, `http_client.rs`,
`keystore.rs`, `metrics.rs`, `stormcrow.rs`, `util.rs` [OBS]; Rust impls under
`apex/rust/{analytics,auth,auto_updater,context,dbxauth,dbxconn,dbxlog,http_client,
keystore,metrics,stormcrow}` [OBS]. Apex is the cross-platform host services layer:
logging/redaction (`dbxlog`), metrics/analytics ingestion, OS keystore, HTTP client,
feature flags (`stormcrow`), connection + server map (`dbxconn/server_map.rs`), auth
(`auth`/`dbxauth`), auto-update. Apex owns the **apex context** singleton (see §4).

**(b) nucleus — sync engine** (`desktop/rust/nucleus/`): the file-sync state machine,
tree/diff/planning, block transfer, filesystem watcher, databases, etc. (crate list in
EVIDENCE §3b). The engine runs in-process inside `dropbox.client.main`. [OBS]

**(c) dropbox — shared crates** (`desktop/rust/dropbox/`): transport/protocol plumbing
shared by apex and nucleus — `grpc_connection`, `pb_service`, `pb_zerocopy`,
`connector`, `throttled_connector`, `proxy_connection`, `hyper_tls_connection`,
`tls_connection`, `system_certs`, `bolt`, `apiv`, `batcher`, `cyclotron`,
`obfuscation`, `dbx_uuid`, `hash_functions`, `dbx-async`, `sqlite_migrate`. [OBS,
EVIDENCE §3c]

Plus a **base** layer under `desktop/app/lib/base/` that carries the RPC machinery this
section is centered on: `tprt/` (wrappers + factory), `cffi_transport/`,
`sqlite_kv_store/`, `system_info/`. [OBS: source paths]

---

### 3. Python control plane vs Rust core split

The Python side is a large control/UI plane (`modules.txt` lists 2858
`dropbox.*`/`apex.*` modules). The split a reimplementer must preserve:

- **Rust core does**: the sync-engine state machine, filesystem watching, block
  transfer, the TLS/HTTP2/gRPC transport to Dropbox servers, databases, auth/keystore
  primitives, metrics/log pipelines. (All the heavy protocol/session logic — the
  Python `.pyc` bodies are encrypted and not the substance; EVIDENCE §2.) [OBS/INF]
- **Python does**: lifecycle orchestration, UI/view-models, CLI command server, auth
  linking flows, camera upload, Bolt signalling glue, feature journeys. Mirrors of the
  apex C-API exist as Python modules `apex.{analytics,auth,auto_updater,config,context,
  dbxconn,dbxlog,health,http_client,lifecycle,memory,metrics,panic,process_metrics,
  stormcrow,util,watchdog}` [OBS].
- **The control-plane ↔ core API is named "Fenix / meta_engine"** on the Python side:
  `dropbox.client.fenix.meta_engine_api`, `dropbox.client.fenix.meta_engine_apis.*`
  (`account_api`, `app_info_api`, `backup_api`, `browser_api`, `file_system_api`,
  `sync_engine_api`, `tray_icon_api`, `notification_dialog_api`, `generic_rpc_api`,
  `markup_api`), each with a `generated_base_classes.*_api_base` and protobuf types in
  `dropbox.client.fenix.generated_types.*_pb2` (incl. `sync_engine_pb2`). [OBS] This is
  the Python face of the native `dropbox_meta_engine.SyncEngineApi` gRPC service
  (EVIDENCE §5). [INF]
- **The GUI (Electron) is a third party** reached over host-local IPC:
  `dropbox.foundation.html_views.electron.ipc.{named_pipe_ipc,socket_ipc,rpc,
  meta_engine_rpc,electron_rpc_reporter,_base,_interface}` [OBS]; the Electron HTML is
  shipped in `local_views.zip` [OBS]. View-models are generated "BIDL" bridges
  (`...bridge_gen.bridge_interface_*`, confirmed by `bidl_gen_test`). [OBS/INF]

---

### 4. The apex context (shared handle for the FFI)

Apex exposes a C-ABI singleton context that both Rust and the Python shims thread
through every call. C-API symbols: `apex_context_create`, `apex_context_configure`,
`apex_context_destroy`, `apex_context_cleanup`, `apex_context_get_current`,
`apex_context_set_current`, `apex_context_get_channel_id`, `apex_context_free_string`
[OBS]; guard string `multiple apex_context crates linked in` [OBS]; backing
`apex.sqlite3`, env `APEX_CONTEXT_WORKER`, trace levels `CRIT/WARN/INFO` [OBS]. Both
`nucleus_python` and `fs_api_python` export an `apex_context` identifier [OBS,
api_*.txt], i.e. the context handle is the first argument of the create calls. A
reimplementer builds one process-wide context, `set_current` on each worker thread, and
passes its `channel_id` to route RPCs. [INF]

---

### 5. The in-process FFI bridge (CPython extension shims)

Three native CPython extensions in `python-pyext/` form the Python↔Rust boundary:
`nucleus_python.cpython-311`, `fs_api_python.cpython-311`, `tprt.cpython-311`. Their
exported identifiers (api_*.txt) define the contract:

**5.1 `nucleus_python`** [OBS, api_nucleus_python.txt]:
- `sync_engine_create(apex_context, account, create_args, ...)` — instantiate the
  Nucleus sync engine for an account; returns an opaque handle. [OBS name; args [INF]
  from `account`, `apex_context`, `create_args` tokens]
- `fs_api_create` is the parallel constructor in `fs_api_python`. [OBS]
- **cffi_transport event pump**: `cffi_transport_send_event`,
  `cffi_transport_receive_event`, `cffi_transport_receive_event_queue_len`,
  `cffi_transport_destroy`, `cffi_transport_destroy_event`, `cffi_transport_stop`.
  [OBS] This is a bidirectional queue: Python pushes request events with
  `send_event`, drains core-produced events with `receive_event` (and checks depth with
  `receive_event_queue_len`). [INF]
- **DFC response polling**: `poll_fp_dfc` + `free_dfc_response` with the response
  triple `resp_data` / `resp_length` / `resp_capacity` (and `raw_ptr`, `consume_raw_ptr`)
  [OBS]. `poll_fp_dfc` drains completed DFC unary responses into a caller-owned buffer
  that `free_dfc_response` releases. [INF] ("fp" also appears as a DB/migration prefix,
  `fp_migrate_fp_dfc_db` / `fp_must_migrate_fp_dfc_db` [OBS]; do not conflate the DFC
  *transport-poll* use here with the FileProvider/"DFC folder" uses elsewhere in the
  corpus.)
- **Logging/telemetry back-channel**: `register_event_logger`, `report_nucleus_event`,
  `report_exception`, with a `severity` enum. [OBS]

**5.2 `fs_api_python`** [OBS, api_fs_api_python.txt]: `fs_api_create`, plus a subset of
the same pump — `cffi_transport_send_event`, `cffi_transport_stop`,
`cffi_transport_destroy`, `report_exception`, and a `tprt_server` reference. [OBS]

**5.3 The `cffi_transport` crate** (`desktop/app/lib/base/cffi_transport/rust/src/
{lib,client,server}.rs`) [OBS] defines two protobuf messages that frame the pump:
- `cffi_transport.TransportEventRequest` — a oneof named `event` (error:
  `missing value for non-nullable oneof 'event' while parsing message
  cffi_transport.TransportEventRequest`). [OBS]
- `cffi_transport.ResponseTransportEvent` — a oneof named `resp`/`event` (error:
  `missing value for non-nullable oneof 'resp' while parsing message
  cffi_transport.ResponseTransportEvent`). [OBS]
Python-side definitions live in `dropbox.proto.cffi_transport.cffi_transport_pb2`. [OBS]
A reimplementer therefore models the FFI as: proto-encoded `TransportEventRequest`s in,
`ResponseTransportEvent`s out, over a length/queue-based channel — not raw structs.
[INF]

---

### 6. The tprt RPC runtime

`tprt` ("transport") is a gRPC-style RPC runtime with **unary** and **server-streaming**
call shapes over pluggable channel backends. Two crate tiers:

**6.1 Wrapper crate** `desktop/app/lib/base/tprt/wrappers/rust/tprt/src/
{lib,client,server}.rs` [OBS]. Demangled symbols show the type model:
- `tprt::Channel::new` + `tprt::ChannelType::dfc` (an enum; `dfc` variant observed)
  [OBS: `4tprtNtB5_11ChannelType3dfc`].
- `tprt::client::Client::new` + Drop [OBS: `4tprt6client...Client3new`].
- `tprt::server::Server::new` + Drop [OBS: `4tprt6server...Server3new`].

**6.2 C ABI** (`api_tprt.txt`, mirrored in both libs) — the stable call surface:
- Client: `tprt_client_new`, `tprt_client_free`, `tprt_client_request_unary`,
  `tprt_client_request_server_stream`, `tprt_client_request_handle_abandon`,
  `tprt_client_register_invalidation_handler`, `tprt_client_stopped`,
  `tprt_connection_reset`. [OBS]
- Server: `tprt_server_new`, `tprt_server_serve`, `tprt_server_free`,
  `tprt_server_cancel`, `tprt_server_done`, `tprt_server_err`,
  `tprt_server_register_unary_handler`,
  `tprt_server_unary_handle_{success,fail,abandon}`, and (stream side)
  `tprt_server_stream_handle_register_invalidation_handler`. [OBS]
- ABI data types: `tprt_buffer` (ptr+len byte buffer), `tprt_error` /
  `tprt_error_domain` / `tprt_error_code_unknown`, and callback typedefs
  `tprt_client_unary_cb`, `tprt_client_stream_cb`, `tprt_server_unary_handler`,
  `tprt_server_stream_handler`. [OBS]
- Call semantics: unary = one request buffer → one completion callback with a response
  buffer or `tprt_error`; server-stream = one request → repeated item callbacks then
  done/err; `abandon` cancels an outstanding handle; `invalidation_handler` is a
  cursor/stream-invalidation signal; `tprt_connection_reset`/`tprt_client_stopped`
  signal channel teardown. [INF from names + gRPC status trailers in EVIDENCE §5]

**6.3 Factory crate** `desktop/app/lib/base/tprt/factory/src/lib.rs` +
`factory_c_api/src/lib.rs` [OBS]. The `TprtFactory` multiplexes RPC channels per
account:
- Struct `TprtFactory` with methods `new`, `serve`, `teardown`, `send_unary`,
  `send_streaming`, and a `Default` impl [OBS: mangled `11TprtFactory{3new,5serve,
  8teardown,10send_unary,14send_streaming}`].
- Keyed by `TprtFactoryKey` → `AccountTprtConnection` in a hash table [OBS].
- Outstanding calls tracked as `TrackedUnaryRequest` / `TrackedStreamRequest` (held via
  `Arc`/`Weak`) [OBS].
- A pre-`serve` backlog `PendingUnary` in a `VecDeque`, drained on serve: log
  `tprt_factory: draining pre-serve unary queue` with fields `queue_depth`,
  `transport`, `service` [OBS]; backpressure log `tprt_factory: unary queue depth
  crossed <N>` [OBS].
- An internal **reactor**: a tokio `mpsc` channel of `ReactorMessage` with an
  `unbounded::Semaphore`, driven by free functions `process_message` and
  `teardown_connection` [OBS].
- Guard: `tprt_factory: serve() called on an already-serving account (service=...)`
  [OBS].

**6.4 Factory C-API for the sync engine** [OBS]:
- Current API: `tprt_factory_sync_engine_dfc_serve(account_id, unary, stream)`,
  `tprt_factory_send_sync_engine_dfc_unary`,
  `tprt_factory_send_sync_engine_dfc_streaming`,
  `tprt_factory_teardown_sync_engine_dfc`. [OBS]
- Deprecated stubs kept for ABI: `tprt_factory_create_sync_engine_dfc_client` and
  `..._server` both log `deprecated stub returning NULL; caller must migrate to
  tprt_factory_sync_engine_dfc_serve(account_id, unary, stream)` /
  `tprt_factory_send_sync_engine_dfc_unary/streaming` [OBS]. So the model evolved from
  explicit client/server creation to a single `serve(account, unary_handler,
  stream_handler)` registration plus `send_*` for outbound calls. A reimplementer
  should build the **new** shape. [INF]
- All factory C entry points validate a UTF-8 `account_id` (`NULL or non-UTF-8
  account_id`) [OBS] — the factory is strictly account-scoped.

---

### 7. DFC vs UDS channel types

`tprt` ships two transport backends, selected by `tprt_transport_type_dfc` /
`tprt_transport_type_uds` [OBS], each with an ops/vtable table (`dfc_tprt_ops`,
`uds_tprt_ops`) [OBS].

**7.1 DFC — in-process framed channel** (the default for Python↔Rust core). [OBS/INF]
- `dfc_tprt_channel_new` / `dfc_tprt_channel_free` [OBS].
- Implemented in Rust as `tprt_factory::DfcTransport::Channel::create_client` and
  `::create_server` [OBS: mangled `12DfcTransportNtB4_7Channel13create_client/
  create_server`]. A `dfc_transport_pair` / `DfcTransport` creates a linked
  client+server endpoint pair in the same address space. [OBS: api_tprt token
  `dfc_transport_pair`]
- This is the channel the `nucleus_python` pump (`cffi_transport_*`, `poll_fp_dfc`,
  `free_dfc_response`) rides on: DFC request/response buffers are moved across the FFI
  with no socket. [INF]

**7.2 UDS — Unix-domain-socket channel, implemented in C++** (cross-process, to a local
daemon). [OBS] The implementation namespace is C++ `uds_tprt_impl`
(Itanium-mangled `_ZN13uds_tprt_impl...`), distinct from the Rust tprt crates:
- Lifecycle/calls: `uds_tprt_client_new/free`, `uds_tprt_server_new/free/serve`,
  `uds_tprt_client_request_unary`, `uds_tprt_client_request_server_stream`,
  `uds_tprt_client_request_handle_abandon`,
  `uds_tprt_server_register_unary_handler`,
  `uds_tprt_server_register_server_stream_handler`,
  `uds_tprt_server_unary_handle_{success,fail,abandon}`,
  `uds_tprt_server_stream_handle_{item,done,fail,abandon}`. [OBS]
- Socket helpers: `make_stream_socket(bool)`, `make_addr(string)`, `accept_cloexec`,
  `set_cloexec`, `set_nonblock`, `suppress_sigpipe`, `read_exact`, `write_all`,
  `wake_all_workers`, `ClientRequest::run`, `PendingResult`. [OBS]
- **Wire framing**: big-endian u32 length prefix — helpers `be32(const u8*)`,
  `put_u32(vector<u8>&, u32)`, `build_response_frame(u32, const u8*, size_t)` [OBS].
  Reimplement as `[4-byte BE length][payload]` request/response frames over
  `AF_UNIX`/`SOCK_STREAM`. [INF]
- **Versioned & unary-only in practice**: error `uds wire version mismatch
  (client/daemon skew)` [OBS] (there is an explicit wire version and a "daemon" peer),
  and error `uds transport does not support streaming` [OBS] — despite a
  `request_server_stream` entry point, the UDS backend rejects streaming, so
  cross-process local RPC is unary request/response only. [OBS]

**Routing conclusion for a rebuild** [INF]: use DFC for the hot in-process
Python↔core path; use UDS for cross-process local IPC to helper/daemon processes
(unary only, length-prefixed, version-checked). The on-the-wire-to-Dropbox path is a
*third* thing — gRPC over HTTP/2+TLS carried by the `dropbox/` shared crates
(EVIDENCE §5), not tprt's local channels.

---

### 8. The bidirectional service map across the FFI

The generated Python stub module names encode call direction at the FFI, and a
reimplementer must respect it: for a given service, exactly one side is the tprt server
(registers handlers via `tprt_server_register_unary_handler`) and the other is the
client. Observed [OBS, modules.txt]:

| Service (proto) | Python module | Direction |
|---|---|---|
| `fs_api.FsApi` | `dropbox.proto.fs_api.fs_api_service_tprt_client` | Python = **client** → Rust fs_api server |
| `nucleus` app service | `dropbox.proto.nucleus.app_service_tprt_client` | Python = **client** → Rust core |
| apex metrics sink | `dropbox.proto.apex.metrics_sink_tprt_client` | Python = **client** |
| `dropbox_meta_engine.SyncEngineApi` (slice) | `dropbox.proto.dropbox_meta_engine.sync_engine_api_slice_tprt_server` | Python = **server** ← Rust core calls in |
| `nucleus_remote_tree_proxy` | `dropbox.proto.nucleus_remote_tree_proxy.remote_tree_proxy_tprt_server` | Python = **server** ← Rust core |

So the bridge is genuinely bidirectional: Python both calls the engine (sync status,
fs_api, app service) and *implements* a "slice" of the sync-engine API and a remote-tree
proxy that the Rust core invokes. [OBS direction from `_tprt_client`/`_tprt_server`
suffixes; INF semantics]. The CLI command path is also tprt:
`dropbox.client.cli.{commandserver,control_thread,tprt_control_endpoint}` [OBS].

Supporting proto corpus (all `dropbox.proto.*`, generated `*_pb2`) [OBS]: `nucleus.*`
(`app_service_pb2`, `sync_engine_pb2`, `sync_engine_status_pb2`, `reactive_api_pb2`,
`file_event_pb2`, `fsw_pb2`, `device_anchor_pb2`, `link_container_pb2`, …),
`fs_api.fs_api_service_pb2`, `bolt.bolt_pb2`, `sync.{cursor,list,remote_ops,root,
xattr}_pb2`, `sync_frontend.*`, `encryption.encryption_types_pb2`,
`apex.{account,dbxconn,metrics_sink,stormcrow,auto_updater}_pb2`.

---

### 9. Reimplementation blueprint (minimal viable decomposition)

1. **One native host binary** with a tiny launcher (`bootstrap_application` /
   `_run` / `_cleanup`) and a `BootstrapConfig{runloop_type, build_config,
   native_init_hook_fn}` selecting `NativeEventLoop` | `ElectronLibrary` | CLI. Install
   crash + hang watchdogs before anything else, then apex context, then embed CPython.
2. **Apex context** singleton (`apex_context_create/configure`, per-thread
   `set_current`, `get_channel_id`) carrying logging, metrics, keystore, HTTP client,
   feature flags, server map.
3. **Nucleus sync engine** created in-process via `sync_engine_create(apex_context,
   account, …)`; a parallel `fs_api_create` for the filesystem-facing API.
4. **FFI pump**: model it as proto `TransportEventRequest` in / `ResponseTransportEvent`
   out, driven by `cffi_transport_send_event` / `receive_event` and
   `poll_fp_dfc`/`free_dfc_response` for DFC unary responses — not as hand-rolled C
   structs.
5. **tprt runtime**: implement `Channel{ChannelType::Dfc|Uds}`, `Client`, `Server` with
   unary + server-stream (DFC); a `TprtFactory` keyed by `account_id` exposing
   `serve(account_id, unary_handler, stream_handler)` + `send_unary`/`send_streaming`,
   a pre-serve `PendingUnary` queue, `Tracked{Unary,Stream}Request` tables, and an mpsc
   reactor.
6. **UDS backend** for local cross-process IPC: `AF_UNIX`/`SOCK_STREAM`, BE-u32
   length-prefixed frames, a wire-version handshake, unary only.
7. **Service wiring** per §8: Python is client of fs_api/app_service/metrics and server
   of the sync_engine_api slice + remote_tree_proxy; the GUI is a separate Electron
   process over named-pipe/socket IPC rendering `local_views.zip`.
8. **Server-facing transport** (separate from tprt): gRPC/HTTP2/TLS via the `dropbox/`
   shared crates to the hosts in the DROPBOX_HOST map.

---

### 10. Gaps / [UNK]
- Exact byte layout of a DFC frame/event beyond "proto `TransportEventRequest` /
  `ResponseTransportEvent` over a queue" (header fields, correlation IDs). [UNK]
- The concrete job of `main_utility()` (which utility: updater host? crash reporter?
  camera-upload worker?) — only the entry point and `Utility` command are observable.
- Whether `main()` vs `linux_event_loop()` map 1:1 to `NativeEventLoop` vs
  `ElectronLibrary`, or are selected independently. [UNK]
- The UDS wire version number and handshake message. [UNK]
- The signature/argument order of `sync_engine_create` / `fs_api_create` beyond the
  observed `apex_context`, `account`, `create_args` identifiers. [UNK]
- Thread model: how many tokio runtimes, and whether the GIL is released around every
  DFC poll. [UNK]## Transport & Wire Protocol — Rebuild Spec

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
- Full `.proto` field layouts for every service/method.## Session & Authentication — rebuild spec

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
## Server Topology & Endpoints

This section specifies the complete server addressing model a reimplementer must reproduce: the embedded `DROPBOX_HOST` server map, the per-server configuration schema, how each gRPC service family is routed (local loopback transport vs. HTTP/2-to-server), and the routing/override headers and environment variables. All evidence is from `scratchpad/corpus/str_libdropbox_core.so.txt` (hereafter **core**) and `scratchpad/corpus/api_tprt.txt` unless noted.

---

### 1. The `DROPBOX_HOST` server map [OBS]

The client ships a built-in server map keyed by a **logical server name** → **hostname**. It lives in `app/lib/apex/rust/dbxconn/src/server_map.rs` [OBS] (also `apex/rust/dbxconn/src/lib.rs`, `apex/c_api/src/dbxconn.rs` [OBS]). The default map is stored as one concatenated literal that begins with the token `baseDROPBOX_HOST` [OBS]:

```
baseDROPBOX_HOST webserver www.dropbox.com metaserver client.dropbox.com
authserver apiv2server api.dropbox.com metaexcserver d.dropbox.com
blockexcserver dl-debug.dropbox.com t8 t8.dropbox.com d6 d6.dropbox.com
staticserver cfl.dropboxstatic.com boltserver …
```

(whitespace added; the on-disk bytes are unseparated). The literal is read into the Apex config DB — the recovery string `recreated the Apex database DROPBOX_HOST…` [OBS] shows the map is persisted into/seeded from `apex.sqlite3`/`config.dbx`, so a deployment can override any entry in config.

**Reimplementer's server table.** Logical name = the map key; host = the paired value. The hostname→name pairing is directly observed from literal adjacency; `boltserver`/`wopi`/`nsfserver`/`apiv2blockserver` hosts are reconstructed as noted.

| Logical server name (map key) | Hostname | Default scheme/port | Role | Evidence tier |
|---|---|---|---|---|
| `webserver` | `www.dropbox.com` | https / 443 | Web UI, OAuth consent, download/landing | [OBS] name+host adjacent |
| `metaserver` | `client.dropbox.com` | https / 443 | Desktop sync control plane (metadata: subscribe/list/commit namespace protocol) | [OBS] name+host; role [INF] |
| `authserver` | `api.dropbox.com` | https / 443 | Device auth / token endpoints | [OBS] both names share one host |
| `apiv2server` | `api.dropbox.com` | https / 443 | API v2 RPC (apiv2_client) | [OBS] `apiv2server` adjacent to `api.dropbox.com` |
| `apiv2blockserver` | (not in literal) [UNK] | https / 443 [INF] | API v2 block-data variant | [OBS] name `apiv2serverapiv2blockserver`; host [UNK] |
| `metaexcserver` | `d.dropbox.com` | https / 443 | Meta "exception" (error/escalation) channel | [OBS] name+host adjacent |
| `blockexcserver` | `dl-debug.dropbox.com` | https / 443 | Block "exception" / debug block fetch | [OBS] name+host adjacent |
| `t8` | `t8.dropbox.com` | https / 443 | Legacy Dropbox edge host | [OBS] name+host; role [UNK] |
| `d6` | `d6.dropbox.com` | https / 443 | Legacy Dropbox edge host | [OBS] name+host; role [UNK] |
| `staticserver` | `cfl.dropboxstatic.com` | https / 443 | Static asset CDN | [OBS] name+host adjacent |
| `boltserver` | `bolt.dropbox.com` | https / 443 | Long-lived push/notification channel (Bolt) | [OBS] both tokens present; pairing [INF] |
| `nsfserver` | (not in literal) [UNK] | https / 443 [INF] | Block storage + rsync delta (`nsf.Nsf`) | [OBS] token `nsfserver/nsf.Nsf/PutRsyncBlock`; host [UNK] |
| (WOPI/Office) | `wopi.dropbox.com` | https / 443 | MS Office WOPI co-authoring | [OBS] host + URL pattern |

Notes:
- `authserver` and `apiv2server` are **two distinct logical names mapped to the same host** `api.dropbox.com` [OBS] (`…authserverapiv2serverapi.dropbox.com…`). A reimplementer keeps them as separate map keys so service code can target "auth" vs "apiv2" independently while they resolve to one host.
- `bolt.dropbox.com` and `wopi.dropbox.com` appear as separate rodata literals [OBS] (`content-location bolt.dropbox.com`, `https://wopi.dropbox.com/wopi/files/oid_…`); they are not inline in the base literal because `strings` orders by address, not logical order.
- `apiv2blockserver` and `nsfserver` are observed **server-name keys** with no co-located hostname literal; their resolved hosts are [UNK] from static strings (resolved from config/metaserver bootstrap at runtime, or alias an existing host).

### 2. Per-server configuration schema [OBS]

Each server entry is a nested struct. The display/format string is `Server Name: {}, Host: {}, Port: {}` [OBS], and the serde field paths are [OBS]:

- `server.server_name`  — the logical key (e.g. `metaserver`)
- `server.host.host_name`  — the DNS name (e.g. `client.dropbox.com`)
- `server.host.port`  — the TCP port (`content-location bolt.dropbox.com server.host.port` [OBS])

So the reimplementer's config model is:

```
ServerMap = Map<ServerName, Server>
Server    = { server_name: String, host: Host }
Host      = { host_name: String, port: u16 }   // scheme implicit = https
```

No `scheme` field is present in the schema [OBS: only `server.host.host_name` and `server.host.port` observed], and **no literal `443`/`:443` appears in either binary** [OBS: negative — grep for `:443`/`=443` returns nothing]. Transport scheme is therefore implicit HTTPS (TLS) for all server-bound traffic; confirmed by the one fully-qualified URL in the map universe, `https://wopi.dropbox.com/wopi/files/oid_([0-9]+)$` [OBS]. Default port 443 is [INF].

A minimal config file a reimplementer supplies (one row per logical server, port overridable):

```
[server.metaserver]   host_name="client.dropbox.com"  port=443
[server.authserver]   host_name="api.dropbox.com"     port=443
[server.apiv2server]  host_name="api.dropbox.com"     port=443
[server.boltserver]   host_name="bolt.dropbox.com"    port=443
[server.staticserver] host_name="cfl.dropboxstatic.com" port=443
…
```

### 3. gRPC service families → logical target & transport [OBS]

Transport runtime is **tprt** (gRPC over HTTP/2), content-type `application/grpc+proto`, HTTP/2 pseudo-headers `:authority :method :scheme :path :status` [OBS, core]. tprt exposes two channel kinds [OBS, api_tprt.txt]: `tprt_transport_type_dfc` (in-process framed channel) and `tprt_transport_type_uds` (Unix-domain socket). gRPC `:path` strings recovered from core give the full service catalog. Services split into **local loopback** (Python/FsProvider ⇄ Rust core over DFC/UDS, no network) and **server-bound** (DFC→HTTP/2→Dropbox host).

| gRPC service (`package.Service`) | Representative methods [OBS] | Target | Transport |
|---|---|---|---|
| `dropbox_meta_engine.SyncEngineApi` | `GetSyncEngineStatus`, `LookupByFileId`, `LookupByLocalPath`, `UpdateHydrationPolicy` | **Local** sync-engine control | DFC/UDS loopback [INF] |
| `fs_api.FsApi` | `mergeFromDropbox`, `UnmergeFromDropbox`, `RenameIntoDropbox`, `bindFromDropbox`, `CreateEphemeralTempDir`, `CreateTempVolume`, `CreateFile`, `CreateBreadcrumbs`/`RemoveBreadcrumbs`, `DeleteDeviceAnchor`, `GetPublishedEvents`/`ExtPublishedEvents` | **Local** filesystem-provider bridge | DFC/UDS loopback [INF] |
| `nucleus.NucleusAPI` | `GetSyncEngineStatus`, `HydratePlaceholder`, `LookupByFileId(Batch)`, `LookupPropsByLocalPath`, `GetSyncProgress`, `GetSyncFailuresSummary`, `CancelRecall`, `UpdateFeatureConfig`, … | **Local** engine control | DFC/UDS loopback [INF] |
| `nucleus.NucleusPhaseAgnosticAPI` | `GetAccount`, `EnumerateRemoteDir`, `CreateDeviceAnchor`/`DeleteDeviceAnchor`, `CheckBlockExistsForPeer`, `GetBlockForPeer`, `GetAndSubscribeToSyncProgressForFileId`, `BindIntoDropbox`, `CheckConsistency`, `Echo`/`EchoStream`, … | **Local** engine control | DFC/UDS loopback [INF] |
| `nucleus.ReverseNucleusAPI` | `SubscribeToBolt`, `GetBlockFromPeer`, `PublishEvent`, `ShowFSWDialog`, `IsFswRuleSuppressed`, `FswRuleSuppress`, `Echo` | **Local**, reverse direction (core → host app callbacks) | DFC/UDS loopback [INF] |
| `nucleus.DebugEngineNetwork` / `nucleus.NetworkMutator` | `CreateFile`, `CreateDirectory`, `ConvertToMount`, `FreezeNetwork`/`UnfreezeNetwork`, `PurgePath`, `SetDeviceFolder`, `SetMountReadOnly`, `SetNamespaceProperties` | **Local**, test/debug only | DFC/UDS loopback [INF] |
| `nsf.Nsf` | `GetBlock`, `PutBlock`, `GetBlockSignature`, `GetRsyncBlock`, `PutRsyncBlock` | **Server** `nsfserver` (block storage + rsync delta) | DFC→HTTP/2→host [OBS pairing] |
| (Bolt) `network::boltGrpcV2` | subscribe via `nucleus.ReverseNucleusAPI/SubscribeToBolt`; `BoltChannelToken` | **Server** `boltserver` = `bolt.dropbox.com` | DFC→HTTP/2→host [INF] |
| `application_metrics.AmpIngestion` | `Record` | **Server** analytics ingestion (AMP) | DFC→HTTP/2→host [INF] |

The binding `nsf.Nsf → nsfserver` is directly observed in the literal `nsfserver/nsf.Nsf/PutRsyncBlock/nsf.Nsf/PutBlock/nsf.Nsf/GetRsyncBlock/nsf.Nsf/GetBlockSignature…` [OBS]. The P2P/LAN methods `CheckBlockExistsForPeer`, `GetBlockForPeer`, `GetBlockFromPeer` plus the feature flag `rust_p2p_fpn_with_self_sign` [OBS] indicate a **peer-to-peer LAN block channel with self-signed TLS**, a separate transport target from the server map.

### 4. Bolt push channel endpoint [OBS]

- Subscription is initiated by the local method `/nucleus.ReverseNucleusAPI/SubscribeToBolt` [OBS]; the core crate is `bolt_connection/src/lib.rs` and `bolt/src/default.rs`, error type `network::boltGrpcV2Error` (`ProtoError`, `MissingResponse…`) [OBS].
- The session handle is `struct BoltChannelToken with 5 elements` [OBS]; recovered field names in order: `app_id`, `unique_id`, `channel_id`, `token`, `channel_states` [OBS: literal `app_idunique_idchannel_idINTERNALtokenchannel_states`].
- Channel lifecycle/error states include `InvalidHost` and `ClientInitiatedReconnect` [OBS] — reconnect/redirect signals a reimplementer must model on the Bolt stream.
- Endpoint host: `boltserver` → `bolt.dropbox.com` [OBS tokens; pairing INF].

### 5. WOPI (Office co-authoring) endpoint [OBS]

The WOPI integration targets `wopi.dropbox.com` with the exact URL grammar `https://wopi.dropbox.com/wopi/files/oid_([0-9]+)$` [OBS] (a regex anchored on a numeric object id). Related identifiers: `get_wopi_src`, `wopi_src`, `get_coauth_supported_by_server`, `desktop_wopi_coauth` [OBS]. A reimplementer builds the WOPI `src` URL as `https://wopi.dropbox.com/wopi/files/oid_<oid>`.

### 6. Routing & override headers [OBS]

Requests to Dropbox hosts carry Dropbox-specific headers (core). Routing-relevant ones:

| Header | Purpose | Evidence |
|---|---|---|
| `Dropbox-Host-Key` | Desktop host-key auth (paired with `host_id`/`host_int`) | [OBS] `Dropbox-Host-Key` |
| `X-Dropbox-UID` | Account UID selector | [OBS] |
| `X-Dropbox-Path-Root` | Namespace/path-root scoping | [OBS] `X-Dropbox-Path-Root` |
| `X-Dropbox-Traffic-Tier` | Traffic class/QoS routing | [OBS] `X-Dropbox-Traffic-Tier` |
| `X-Dropbox-Metro-Pref` | Preferred metro (datacenter/region) | [OBS] `X-Dropbox-Metro-Pref` |
| `X-Dropbox-Backend` (value `stage`) | Backend/stage routing selector | [OBS] `X-Dropbox-Backendstage` |
| `X-DBX-RUN-TYPE` | Dev/automation run type | [OBS] `X-DBX-RUN-TYPE` |
| `X-Dropbox-Request-Id`, `X-Dropbox-Force-Request-Tracing` | Tracing | [OBS] |
| `X-Dropbox-App-Name`, `X-Dropbox-App-Version`, `X-Dropbox-User-Agent`, `User-Agent` | Client identity; UA = `Dropbox-lnx.x86_64-274.4.4905` | [OBS] |
| `X-Dropbox-Locale`, `Dropbox-API-User-Locale` | Locale | [OBS] |

### 7. Environment / dev-stage overrides [OBS]

The host map and routing can be overridden at startup via environment variables [OBS]:

- `DROPBOX_HOST` — override the base host map; a **`devbox`** variant is present, with dev OAuth app credentials `devboxdropboxdesktopappkey` / `devboxdropboxdesktopappsecret` [OBS].
- `DBUSESTAGE` / `DBNOUSESTAGE` — force on/off the staging backend (emits `X-Dropbox-Backend: stage`) [OBS].
- `DBDEV_METRO_PREF` — set `X-Dropbox-Metro-Pref` [OBS].
- `DBDEV`, `DBDEV_RUN_TYPE` (→ `X-DBX-RUN-TYPE`), `DBDEV_AUTOMATION`, `DBDEV_REQUEST_TRACING`, `DBDEV_LNM_FETCH_PROPERTIES` — dev harness knobs [OBS].
- apiv2 uses OAuth: `apiv2_client/src/client.rs`, `apiv2_keys/_bs.out_dir/keys.rs`, feature flag `nucleus_apiv2_oauth`; error types `ApiV2Endpoint`, `struct ApiV2ApiError with 2 elements` [OBS].

### 8. Summary of transport routing for a reimplementer

1. Load `ServerMap` (defaults in §1, overridable via config DB / `DROPBOX_HOST`).
2. Local control-plane gRPC families (`SyncEngineApi`, `FsApi`, `nucleus.*`) ride **DFC/UDS loopback** — no entry in the server map, no TLS.
3. Server-bound families resolve their logical name in the map, then open an **HTTPS/HTTP-2 gRPC** channel: `nsf.Nsf`→`nsfserver`; Bolt→`boltserver` (`bolt.dropbox.com`); AMP metrics→ingestion; apiv2/auth→`api.dropbox.com`; metadata sync (subscribe/list/commit)→`metaserver` (`client.dropbox.com`).
4. Attach the Dropbox headers (§6); select stage/metro via env (§7).
5. WOPI co-authoring is a distinct HTTPS endpoint `https://wopi.dropbox.com/wopi/files/oid_<oid>`.
6. LAN block sync is a separate self-signed-TLS peer channel (`*ForPeer`/`*FromPeer`), not in the host map.## Nucleus Sync Protocol — Rebuild Specification

Scope: the per-namespace metadata sync protocol implemented by the Rust `nucleus`
engine inside `libdropbox_core.so`. This is the "control-plane" of sync (what the tree
looks like); block content transfer (`nsf.Nsf`) is touched only where the protocol
drives it. All identifiers below are observed in
`corpus/str_libdropbox_core.so.txt` unless noted. Tags: **[OBS]** observed token,
**[INF]** inference from observed evidence + known crate behavior, **[UNK]** undetermined.

> Note on the corpus: the string table is concatenated Rust literals with no
> separators, so quoted tokens are substrings (grep -F findable). Where a quote shows
> two field names run together (e.g. `root_ns_idhidden_setcursor`), those are adjacent
> struct fields / format-string args, reported as a field list.

---

### 1. Layering: three gRPC surfaces [OBS]

The engine exposes/consumes three distinct gRPC service namespaces, all carried as
`application/grpc+proto` over HTTP/2 (see transport dimension). A reimplementer must
build all three:

| Service | Direction | Role |
|---|---|---|
| `sync_frontend.Meta/*` | client → Dropbox server | **the sync protocol proper** (cursor, list, commit, ack, resync, reassociate) [OBS] |
| `nsf.Nsf/*` | client → server | block storage + rsync delta (`GetBlock`, `PutBlock`, `GetBlockSignature`, `GetRsyncBlock`, `PutRsyncBlock`) [OBS] |
| `nucleus.NucleusAPI` / `nucleus.NucleusPhaseAgnosticAPI` / `nucleus.ReverseNucleusAPI` | local UI/FS process ⇄ engine (UDS/DFC) | control plane (lookup, hydrate, pause, subscribe-to-bolt callback) [OBS] |
| `dropbox_meta_engine.SyncEngineApi/*` | local | thin stable facade: `GetSyncEngineStatus`, `LookupByFileId`, `LookupByLocalPath`, `UpdateHydrationPolicy` [OBS] |

**`sync_frontend.Meta/` methods (the server-facing sync RPC — the heart of this spec) [OBS]:**
`GetInitialCursor`, `GetNamespaceInfo`, `LinearizedList`, `ConsistentCutList`,
`CommitAtHead`, `AcknowledgeCommits`, `Reassociate`, `GetResyncState`,
`SetResyncState`, `AllocateFileId`, `CanChangeFileId`, `CheckConsistency`,
`GetFileInformation`, `GetPendingUploads`, `ReportPendingUploads`,
`CommunicateCommand`, `LogSyncGoldMetrics`, `PingUtf`, `GetGolgiMigrationFileIds`,
`GetSymlinkMigrationFileIds`.
The internal snake_case method dispatch names are also present: `get_initial_cursor`,
`get_namespace_info`, `linearized_list`, `consistent_cut_list`, `commit_at_head`,
`acknowledge_commits`, `change_fileid`, `allocate_file_id`, `check_consistency`,
`get_file_information`, `communicate_command`, plus block ops `upload_block`,
`download_block`, `block_signature`, `upload_rsync_block`, and `fast_forward` [OBS].

---

### 2. Core data model [OBS/INF]

A reimplementer must model these primitives (crate `nucleus/common`):

- **FileId** (`nucleus/common/src/fileid.rs`): a globally-unique id for a synced
  object; `fileid.is_root()` exists [OBS `assertion failed: !fileid.is_root()`]. Server
  can **reassign** a FileId (see §6), and FileIds are server-**allocated**
  (`AllocateFileId`) and **changeable** (`CanChangeFileId`/`change_fileid`) [OBS].
- **ns_id** (namespace id, `BLOB`): the shared-folder/root partition. Stored as a SQL
  `BLOB` [OBS `ns_id BLOB,`]. Keys cursors, mounts, and the `update_info`/`transplant`
  tables.
- **oid** (object id) + **HLC** (Hybrid Logical Clock): every node carries an `oid`
  and an `hlc` [OBS `root oid missing its hlc`, `oid missing its hlc`,
  `ExtendedAttributeOidFileIdHlc`]. The engine maintains a monotonic watermark
  `head_hlc` with the invariant `hlc >= self.inner_info.head_hlc`
  [OBS `assertion failed: hlc >= self.inner_info.head_hlc`]. HLC flavors observed:
  `latest_hlc`, `first_hlc`, `read_hlc`, `incomplete_hlc`, `attribution_hlc_adjustment`.
  [INF] HLC provides total causal ordering of mutations across devices; `read_hlc` is
  the snapshot point a commit is computed against.
- **head**: the engine's authoritative sync position is a struct `inner_info.head`
  containing **`ns_cursors`** (a per-namespace cursor map) and `head_hlc`
  [OBS `self.inner_info.head.ns_cursors`, `self.inner_info.head_hlc`]. Mount bookkeeping
  carries `mounted_nses` and `unmounted_nses` sets with invariant
  `mounted_nses.is_subset(&known_nses)` [OBS].
- **PNM = Per-Node Metadata** (server's node representation in list/commit payloads):
  variants `FilePNM`, `DirectoryPNM`, `SymlinkPNM`, `EncryptedFilePNM`,
  `BlockwiseDirectoryPNM`, `DeviceInfoPNM`; carried as `PNMList` with `PNMAttribute`
  (key/`serialized_value`) and `PNMBehaviors` [OBS `PNMListFilePNMDirectory…`,
  `PNMAttributeserialized_value`, `PNMBehaviorsDir`]. A node's content identity is
  `content_hash` + `blocklist`; node fields seen: `mtime`, `permissions`,
  `visibility`, `hidden_state`, `is_encrypted_folder_stub`, `target_fileid`,
  `logical_size`, `xattr_hash`, `coauth_checksum`, `written_content_hash`,
  `hydration_policy_differs_from_parent`, `should_encrypt` [OBS].
- **sync.Object / Operation protos**: top-level message family `sync.*` —
  `sync.Object`, `sync.Edit`, `sync.ListOperation`, `sync.CommitOperation`,
  `sync.CommitResult` [OBS]. Namespace properties ride in `TargetNSProperties`:
  `ns_type`, `ns_derived_properties`, `can_mount_shared_folders`,
  `is_team_shared_folder`, `in_team_folder`, `is_confidential`,
  `only_owner_can_update_acl`, `forbid_non_team_sharing`,
  `is_user_on_same_team_as_owner`, `team_id`, `writable`, `is_no_access`,
  `is_encrypted_folder` [OBS].

---

### 3. Namespaces & mount_table [OBS]

Crate `nucleus/mount_table/src/mount_table.rs`. Sync is **per-namespace**; namespaces
are grafted into a single user-visible tree via a mount table.

- **home namespace**: `home_ns_fileid` anchors the user root
  [OBS `can't get path of nonexistent home_ns_fileid`]; `root_ns_id` is the root
  partition [OBS].
- **mount record fields**: `target_root_fileid`, `target_ns_id`, `mount_point_fileid`,
  `mount_fileid`, `mount_to_root_fileid` [OBS]. A mount binds a child namespace's root
  under a parent node.
- mount/unmount is a first-class commit op (`CommitUnmount`, `ConvertToMount`) and a
  list event (`Mount?`, `unmount notifications`) [OBS `have type Mount?`,
  `Not bubbling unmount notifications because we are going through initial…`].
  Constraint: "Updating mount_table multiple times in a single CanopyWriteBatch is
  unexpected" [OBS].
- persistence: `update_info(fileid, ns_id, is_delete, transplant_record)` and a
  `transplant(ns_id, path_hash, path_state)` table drive cross-namespace moves
  ("transplants") [OBS `SELECT fileid, ns_id, is_delete, transplant_record FROM update_info`,
  `DELETE FROM transplant WHERE ns_id=? AND path_hash=?`].

[INF] Reimplementer: keep a map `ns_id → NamespaceState { root_fileid, cursor, mount
points, ns_properties }`; the canopy tree is the union of mounted namespaces with mount
points splicing child ns roots into parent directories. Unmounting a namespace drops
its cursor from `head.ns_cursors`
[OBS `cursor.remove(&ns).expect("Mounted namespace not in \`head\`")`].

---

### 4. The canopy: three-tree model, diff, rebase, planning, pre_local [OBS/INF]

The in-memory synced tree is the **canopy** (crate `nucleus/canopy`, files
`inner.rs`, `inner/remote_state.rs`, `local.rs`, `planner.rs`, `fill.rs`,
`finalize.rs`, `finalize_reconstruct.rs`, `persistence.rs`) [OBS]. It is mutated only
via a `CanopyWriteBatch` [OBS], scheduled by `nucleus/canopy_scheduler`
(`prepare.rs`, `commit.rs`, `deferred_writes.rs`) [OBS].

**Three trees** (classic Dropbox three-way merge; crate `nucleus/planning/src/trees/`):
`RemoteTree`, `SyncedTree` (the last agreed base), `LocalTree`, plus `RemoteSnapshot`
and `WrappedTree` wrappers [OBS, file paths `planning/src/trees/{remote_tree,synced_tree,
local_tree,remote_snapshot,wrapped_tree,conflict,diff}.rs`]. The engine computes
**frontiers** (the dirty edge of each side): `local_frontier`, remote frontier,
counters `num_remote_dirties`/`num_local_dirties`, with frontier invalidation events
`frontier_node_invalidated` [OBS `Initialized frontiernum_remote_dirtiesnum_local_dirties`].

**Diff** (`nucleus/planning/src/diff/{local,frontier}.rs`, `nucleus/tree_diff`):
produces typed diffs `LocalDiffAdd`, `LocalDiffEdit`, `LocalDiffHash`, `LocalDiffMove`,
`LocalDiffUnmount`, and `RemoteDiffAdd`, `RemoteDiffEdit`, `RemoteDiffMove`,
`RemoteDiffDelete` [OBS].

**Rebase/plan** (`nucleus/planning/src/rebase/{local,remote,helpers}.rs`,
`nucleus/canopy/src/planner.rs`): rebases one side's diffs over the other to produce an
executable op plan. Observed planner routines: `Planner/rebase_remote_op()`,
`Planner/resolve_remote_cycle()`, `rebase_local_add_remote_add_same_fileid()`,
`Planner/one_way_sync_conflict()`, `resolve_local_cycle` [OBS]. The plan is a sequence
of **CanopyOperation**s. Reconstruct ops (apply remote→disk): `ReconstructAdd`,
`ReconstructEdit`, `ReconstructDelete` (`CanopyOperation::ReconstructDeleteNode`),
`ReconstructMove`, `ReconstructRecall`, `ReconstructHide`, `ReconstructMoveIn/Out`,
`RemakePlaceholder` [OBS]. Commit ops (apply local→server): `CommitAdd`, `CommitEdit`,
`CommitDelete`, `CommitMove`, `CommitUnmount` with "Full" variants
(`CommitAddFullOperation`, `CommitEditFullOperation`, `CommitDeleteFullOperation`,
`CommitMoveFullOperation`) [OBS]. LocalFixup ops (self-heal disk without server round
trip): `LocalFixupMove`, `LocalFixupMakeDirectory`, `LocalFixupMetadata`,
`LocalFixupBreakDeviceAnchor`, `LocalFixupIgnoreUnsyncable`, `ResolveRemoteDirectoryDelete`,
`FetchPlaceholderInfo`, `ReportConflictFailure`, `PlanningWrite`,
`UnreconstructableCollision`, `RemoveAlternateSyncedName`, `UpdateCoauthChecksum`,
`UnignoreFetchOid`, `DeleteTypeChange`, `FallbackMove`,
`ReconstructDeleteMoveToTrashFallback` [OBS].

**pre_local** (crate `nucleus/pre_local`): before a plan writes to disk, it is validated
against a set of **constraints** (file paths `pre_local/src/constraints/*.rs`).
Observed constraints (each surfaces as a `PreLocal*` wait/error): `FileIdUniqueness`,
`FileIdExistence`, `DirFileIdConsistency`, `InodeUniqueness`, `CaseUniqueness`,
`HashDeletedPaths`, `DeletedInodeVerification`, `IgnoredStateConsistency`,
`PlaceholderConsistency`, `FlexibleFilenamesConsistency`, `FPPackageXattrsConsistency`,
`DeviceAnchorTargetUniqueness`, `DeviceAnchorTargetFileIdConsistency`,
`DeviceAnchorDescendantVerification`, `ResolverExists`, `ConstraintLoopingFileId`
[OBS `PreLocalFileIdUniqueness…`]. The pre_local manager also runs a **reindexer**
(`pre_local/src/reindexer.rs`) and a **resolver** for dirty paths
(`pre_local/src/resolver/{dirty_paths,observations}.rs`) [OBS]. Reconstruction output
is materialized as **disk_intents** (`fs_engine_scheduler/src/disk_intent/mod.rs`):
`insert_disk_intents`/`clear_disk_intents`, executed by scheduler tasks
`reconstruct`, `planning_write`, `placeholder`, `hash`, `commit`, `local_fixup`,
`move_to_trash_info` [OBS].

[INF] Pipeline per namespace: **list → merge into RemoteTree → diff vs SyncedTree →
rebase against LocalTree → plan CanopyOperations → pre_local constraint check →
disk_intents (reconstruct to disk) / commit intents (push to server)**.

---

### 5. The per-namespace protocol state machine [OBS/INF]

State machine crate `nucleus/protocol`, states in `nucleus/protocol/src/states/`:
`subscribe.rs`, `list.rs`, `commit.rs`, `commit_ack.rs`, `mod.rs` [OBS]. The top-level
**protocol transition** enum is `{ Commit, CommitAck, Subscribe }`
[OBS `Protocol transitionCommitCommitAckSubscribe`]. Additional engine states:
`InitialState`, `LocalTransactionState`, `GetResyncState`, `SetResyncState`,
`PropagateUncommittableState` [OBS]. The protocol runs as a **ProtocolWorker** whose
sub-phases appear in the engine-wait tracker: `ProtocolWorkerConsistentCut`,
`ProtocolWorkerLinearizedList`, `ProtocolWorkerCommit`, `ProtocolWorkerCommitAck`
[OBS].

**Startup — `InitialState`:** obtain a cursor. `get_initial_cursor` →
`GetInitialCursorResponse`/`InitialCursorResponse`(+`InitialCursorResponseOid`)
[OBS `Got initial cursor from network`, `GetInitialCursorResponseOid`]. The combined
bootstrap loop is literally named `get_intial_cursor_and_list_loop` [OBS, sic — typo in
source]. Cursor is required before anything else: subscribe, commit, and commit-ack all
assert a cursor is present (`Entered subscribe without a cursor?`,
`Entered Commit without a cursor?`, `Entered commit ack without a cursor, relisting`)
[OBS].

**Subscribe (`states/subscribe.rs`):** register for change notifications over Bolt (see
§10). Maintains `subscriber_tokens`/`subscriber_id`; detects "no remote ops" and
`list_up_to_date` [OBS]. When Bolt signals a delta, transition to list.

**List (`states/list.rs`):** two list mechanisms exist —
1. **LinearizedList** (`sync_frontend.Meta/LinearizedList`) → `LinearizedListResponse`
   carrying `HlcLinearizedPage` [OBS]. Request fields: `root_ns_id`, `hidden_set`,
   `cursor`, and an `InitialList` flag [OBS `Making list requestroot_ns_idhidden_setcursorInitialList`].
2. **ConsistentCutList** (`sync_frontend.Meta/ConsistentCutList`) →
   `ConsistentCutListResponse` of `ConsistentCutListPage`s [OBS]. This is the newer,
   snapshot-consistent list (crate `nucleus/protocol/src/consistent_cut/*.rs`:
   `differential_update.rs`, `path_state_processing.rs`, `transplant.rs`, `stats.rs`).
   Each page carries `cursor_type`, `cursor_size`, `transplant_segments`,
   `differential_updates`, plus stats `num_differential_records`, `num_tombstones`,
   `num_filtered_selsync_v2`, `superseded_reasons`
   [OBS `Received consistent cut pagefinishcursor_typecursor_sizetransplant_segmentsdifferential_updates`].
   The protocol enters/finalizes a cut: `EnterConsistentCut` /
   `FinalizedConsistentCut()` [OBS]. Lists feed `RemoteTree` (`canopy/inner/remote_state.rs`).

**Commit (`states/commit.rs`, `protocol/src/commit.rs`, `commit_intents.rs`):** push
local changes. Preconditions enforced: a cursor and non-empty outstanding intents
(`Must have outstanding intents!`, `Should not have outstanding intents before committing!`)
[OBS]. Sends `CommitAtHead` with the commit batch; see §6.

**CommitAck (`states/commit_ack.rs`):** after a successful commit, acknowledge
(`AcknowledgeCommits`) and reconcile the local tree against a consistent cut. If the cut
is aborted mid-ack, relist and retry
[OBS `ConsistentCut aborted during ack; trying again`, `Entered commit ack without a cursor, relisting`].
Phases logged: `beginning_commit_ack`, `commit_ack_received_results`,
`cancelled_commit_ack` [OBS].

**PropagateUncommittableState:** marks nodes that cannot be committed (permission,
quota, filename, etc.) as "uncommittable" and unsyncs them
[OBS `PropagateUncommittableState: Synced node found, unsyncing...`,
`UpdateUncommittableStateOperation`, op `MarkUncommittable`]. Reason taxonomy is large
(see the `TaskSchedulerXCommitError*` and `PendingSetNotEmptyX*` enums, e.g.
`AccountOverQuota`, `UploadSharingViolation`, `UploadPermissionDenied`, `FileNameError`,
`FileTooLarge`, `DeleteWithUnsyncableDescendant`) [OBS].

[INF] Reimplementer loop per namespace (pseudocode):
```
state = InitialState
cursor = GetInitialCursor(ns_id)              # persisted in head.ns_cursors[ns_id]
Subscribe(ns_id, cursor)                      # bolt channel token
loop:
    wait for bolt delta OR local dirty OR timer
    page = ConsistentCutList(ns_id, cursor, hidden_set)   # or LinearizedList
    while page: merge differential_updates+transplant_segments into RemoteTree
               cursor = page.next_cursor
    diff = diff(RemoteTree, SyncedTree); rebase against LocalTree -> plan
    pre_local.validate(plan); apply reconstruct ops to disk (disk_intents)
    if outstanding local intents:
        res = CommitAtHead(ns_id, read_hlc, mount_table, commit_batch)
        handle res (NeedBlocks -> upload -> retry; FileIdReassigned; IllegalMount)
        AcknowledgeCommits(...)               # commit_ack, reconcile via consistent cut
    advance SyncedTree = RemoteTree ⋈ committed; persist cursor + head_hlc
```

---

### 6. Cursors & deltas [OBS/INF]

- **Cursor types** (crate `nucleus/common/src/cursors.rs`): per-namespace `NSCursor`
  (held in `head.ns_cursors`), plus specialized cursors `SECCursor`, `TSSCursor`,
  `ExtraSyncStateCursor`, and a `migration_base_cursor` [OBS]. The consistent-cut cursor
  is the signed, server-verifiable `SignedConsistentCutCursor` wrapping a
  `ConsistentCutCursor` with a `signature` and `over_quota_deletion_generation`
  [OBS `SignedConsistentCutCursor`, `consistent_cut_cursorsignature`,
  `ConsistentCutCursortarget_cursorstarget_protocol_versiontarget_root_`].
- **Cursor invalidation**: on invalid/dropped cursor the engine refetches
  (`Canopy missing list cursor, likely due to cursor invalidation`,
  `received_invalid_cursors`, `Skipping all tombstones because we had no prior cursor`)
  [OBS].
- **fast_forward**: `fast_forward` advances a namespace cursor without a full list
  (used heavily by reassociate) [OBS, 15 occurrences; `reassociate_fast_forward_directory_fileid_mismatch`].
- **Deltas** are `differential_updates` + `transplant_segments` within consistent-cut
  pages; tombstones mark deletions [OBS].

[INF] A reimplementer must persist `head.ns_cursors[ns_id]` and `head_hlc` durably
(see `persist_migration_cursor`, `persist_extra_sync_state` [OBS]) and present the cursor
on each `ConsistentCutList`/`LinearizedList`; the server returns the next cursor in each
page, and an opaque signed cursor must be echoed back verbatim.

---

### 7. Commit path in detail [OBS/INF]

Request `CommitRequest`/`CommitAtHead` carries the commit batch, the `read_hlc`, and the
`mount_table`, logged as `Attempting server commit … mount_table num_commits` →
`Completed server commit … tree_snapshot read_hlc`
[OBS `ad_hlcAttempting server commitmount_tablenum_commits`,
`Completed server committree_snapshot`]. Batch is size-capped
(`commit_batch_over_size_limit` with `tokens_size`, `proto_size`; `batch_size_limit`)
[OBS].

Response `sync.CommitResult` is a oneof `status` with variants [OBS, parse error string
`non-nullable oneof 'status' while parsing message sync.CommitResult`]:
- **`CommitResult_NeedBlocks`** — server lacks block content; payload is a list of
  needed block hashes [OBS `NeedBlocks{blocks: [`, `Received NeedBlocks for`]. Client
  uploads via `nsf.Nsf/PutBlock` (or rsync delta `PutRsyncBlock` after
  `GetBlockSignature`/`GetRsyncBlock`, using the Rust `fast_rsync` crate:
  `fast_rsync::Signature`, `fast_rsync::diff`) [OBS], then re-commits.
  Upload authorization/resumption uses a SQLite table **`file_block_upload_tokens`**
  `(fileid, block_hash, ts, token)` with indexes `_block_hash_idx`, `_prune_idx`
  [OBS `VALUES(:fileid, :block_hash, :ts, :token)`,
  `nucleus/database/src/sqlite/block_upload_tokens.rs`].
- **`CommitResult_FileIdReassigned`** — server reassigned the FileId (collision); client
  must adopt the new id and patch its trees [OBS].
- **`CommitResult_IllegalMount`** — the commit touched a mount illegally [OBS].
- plus error paths `CommitRequestError::CommitAckConsistentCutAborted`,
  `CommitRequestError::OverQuota`, `OqCommitPrevented`, `BbMonthlyUploadLimitExceeded`,
  `FileTooLarge`, `GetFileInformationFailed` [OBS].

A commit acknowledgement is `CommitAcknowledgement` /
`CommitAcknowledgementReply`/`Response` returned/confirmed via `AcknowledgeCommits`
[OBS]. Pending uploads are tracked server-side via `GetPendingUploads` /
`ReportPendingUploads` [OBS].

Intent lifecycle (crate `nucleus/intent_manager`): commit candidates are **intents**;
the engine must "have outstanding intents" before committing and marks them acked after
`commit_ack` [OBS `Intent manager should be marked`, `outstanding_commit_intents`,
`commit_intents_at_startup`].

---

### 8. Conflict handling [OBS/INF]

Conflicts are detected during rebase (`nucleus/planning/src/trees/conflict.rs`,
`Planner/conflict()`) and `nucleus/conflict/src/lib.rs`. Observed conflict kinds:
- `server_indicated_conflict` (server says this change conflicts) [OBS].
- `EditFastForwardConflict` — local edit vs remote fast-forward [OBS].
- `FilenameConflict` / case-uniqueness: "Executing case conflict rename",
  "Generating rename…", "Failed to find conflict filename" [OBS].
- `ConflictError::ConcurrentMove`, `resolve_local_cycle`/`resolve_remote_cycle` for
  move cycles [OBS].
- selective-sync conflicts: `is_selsync_conflict()`, `selsync'd remote add`,
  `local add collides with selsync stub` [OBS].
- `EncryptedFolderConflict`, `RACL conflict`, `UserFileLockingConflict` [OBS].
- resolution produces a **conflicted copy**: `conflicted_copy`,
  `IgnoredConflictedCopy`, `HostConflictedCopy`, `UserFileLockingConflict`,
  `potential_fp_package_conflicted_copy_stat` [OBS]. [INF] A conflicting local node is
  renamed to a "conflicted copy" and both versions are kept, matching Dropbox's
  documented behavior.

---

### 9. Resync & reassociate [OBS/INF]

**Resync** (crate `nucleus/resync`): a full re-hash-and-relist recovery path. Server
state is read/written via `GetResyncState`/`SetResyncState`
(`GetResyncStateResponse`/`SetResyncStateResponse`, fields `state`, `resync_id`, and
a `weight`/`reason` with variants `Lightweight`, `ReadWrite`, `ScheduledResync`)
[OBS]. Local phases (crate `fs_engine_phases`): `resync_hash_and_list.rs`
(`ResyncHashAndListPhase`), `resync_reassociate.rs` (`ResyncReassociatePhase`) [OBS].
Triggers logged: `Performing a resync.`, `Resyncing due to failed canopy initialization`,
`downgrade-triggered resync`, `resync_invalid_bolt_channel`, `Scheduled resync`,
`lightweight_resync_dropped_cursor` [OBS]. A resync re-establishes the cursor and
rebuilds RemoteTree from scratch.

**Reassociate** (`sync_frontend.Meta/Reassociate`, crate `nucleus/reassociate`,
`network/src/reassociate.rs`): matches local inodes to server FileIds after a
disruption (e.g. team join, migration). Request `ReassociateRequest` carries
`dir_fileid`, `inode`, `locally_synced_blocklist`, `exists_in_remote_tree`,
`migration_state`, `migration_base_cursor` [OBS]. Response
`ReassociateResponse`/`ReassociateResponse_Result` is `Found`/`NotFound`
(`FileIdReassociateResponse_Result_NotFound`), and uses `fast_forward` to advance the
cursor [OBS `reassociate_found`, `reassociate_not_found`,
`reassociate_skipping_remote_delete`].

---

### 10. Bolt notification channel [OBS/INF]

Crate `nucleus/network/src/bolt.rs` + `nucleus/nucleus_bolt_connection`; endpoint
`bolt.dropbox.com` [OBS]. Replaces the legacy notify long-poll.

- **Token**: `BoltChannelToken` is a 5-field struct `{channel_id, token, app_id,
  unique_id, …}` [OBS `struct BoltChannelToken with 5 elements`, `BoltChannelTokenchannel_idtoken`].
- **Subscribe**: client calls (local) `nucleus.ReverseNucleusAPI/SubscribeToBolt` →
  `SubscribeToBoltReply` which reports `has_delta` per channel
  [OBS `SubscribeToBolt returnedreplyhas_delta`]. `bolt_subscribe` is also a remote
  command [OBS `Remote command (bolt_subscribe)`].
- **Run loop**: a long-poller (`Making Bolt request … num_tokens`,
  `Initializing bolt run loop`, `Ending bolt run loop because our channel…`,
  `No subscriptions; waiting for subscribe call`, `LongPoller was dropped`) [OBS]. When
  a channel's revision advances, the engine signals subscribers
  (`Signalling and unsubscribing subscribers of bolt update`) which drives the list
  phase for that namespace [OBS]. `Already have a newer revision for bolt subscriber`
  guards stale notifications [OBS].

[INF] Reimplementer: hold one `BoltChannelToken` per subscribed namespace/channel; issue
a batched long-poll listing all tokens; server returns which channels changed
(`has_delta`); for each changed channel, run `ConsistentCutList` from the saved cursor.

---

### 11. Hydration, smart_sync, instant_files [OBS/INF]

**Hydration policy** governs whether a file's content is materialized on disk
("local") or a placeholder ("online_only"). Model:
`HydrationPolicy`/`EffectiveHydrationPolicy` with CRDT-style ticks `hydration_state`,
`state_tick`, `move_tick`
[OBS `EffectiveHydrationPolicyhydration_statestate_tick`,
`LocalDiffAddHydrationPolicyhydration_statemove_tickstate_tick`]. Per-node it is
`Local` / `OnlineOnly`; a node can differ from its parent
(`HydrationPolicyDiffersFromParentCount`, `hydration_policy_differs_from_parent`) [OBS].
Policy counts rolled up as `local_policies`/`online_only_policies` [OBS].

**Control**: `UpdateHydrationPolicy` (both `dropbox_meta_engine.SyncEngineApi/` and
`nucleus.NucleusPhaseAgnosticAPI/`; req `UpdateHydrationPolicyReq` with
`err_if_default_or_unknown`, `SingleOwnerType`, `ContentsLockedWithNoAccess`) and
`HydratePlaceholder`/`HydratePlaceholderReq` (with `HydratePlaceholderReq_Driver`) [OBS].
Hydration execution logs: `Requesting hydration of root`, `Finishing hydration`,
`Stating final file`, `infinite_hydration_start_success`/`_completed`/`_start_failure`
(the "infinite" / smart-sync path) [OBS]. De-hydration/recall reasons include
`AutoEvictionFollowingUnintendedRecall`, `AutoEvictionFollowingEncryptedHydration`,
`ExternalOnDemand`, `UserCancellation`, `SelectiveSyncTeamPolicy` [OBS].

**smart_sync** (crate `nucleus/smart_sync`, files `oracle.rs`, `policy.rs`,
`boundary.rs`): decides hydration boundaries. `oracle` evaluates policy
(`oracle_clock`, `oracle_setup_time`), `boundary` defines the online-only/local border,
`policy` the rules; `SmartSyncMoveToTrash` handles eviction [OBS].

**instant_files** (crate `nucleus/instant_files`, files `download.rs`, `upload.rs`,
`download_manager.rs`): "Streaming Sync" — eager/streaming block transfer for on-demand
hydration. `InstantFilesDownloadManager {src_fileid, dest_fileid}` pulls blocks
(can use a `P2PBlockSource`); has its own `bolt_subscribe (instant_files)` and
`pending_uploads (instant_files)` workers and an `InstantFilesUploadWorker` [OBS].

**Selective sync** is represented in the protocol as the **hidden set**: list requests
carry `hidden_set`/`hidden_path_hashes`; nodes carry `hidden_state`; `GetHiddenState`/
`UpdateHiddenState`/`SetPathIgnoredState` local APIs manage it; `is_selsync_root`,
`selsync_v2` [OBS].

---

### 12. Local control-plane (SyncEngineApi + NucleusAPI) [OBS]

What a reimplementer must expose to the UI/FS-provider process (over UDS/DFC):

- `dropbox_meta_engine.SyncEngineApi/`: `GetSyncEngineStatus`, `LookupByFileId`,
  `LookupByLocalPath`, `UpdateHydrationPolicy` [OBS].
- `nucleus.NucleusAPI/`: `GetSyncEngineStatus`, `GetSyncProgress`,
  `GetSyncFailuresSummary`, `LookupByFileId`(+`Batch`), `LookupPropsByLocalPath`,
  `LookupSyncIcon`, `HydratePlaceholder`, `CancelRecall`, `FetchByteRange`,
  `GetRemoteSyncedIgnoredFiles`, `UpdateFeatureConfig`, `SuppressFSWs` [OBS].
- `nucleus.NucleusPhaseAgnosticAPI/`: `LookupByLocalPath`, `LookupNamespaces`,
  `LookupMountPointUnderFileId`, `GetNamespaceInfo`-equivalents,
  `MergeIntoDropbox`/`UnmergeFromDropbox`/`BindIntoDropbox`/`UnbindFromDropbox`,
  `TriggerList` (force a list pass), `Pause`/`Unpause`, `UpdateHydrationPolicy`,
  `UpdatePriorityHint`, `EnumerateRemoteDir`, `GetSyncQueueSnapshot`,
  `CreateDeviceAnchor`/`ListDeviceAnchors`, `EarlyRetrySync`, `KeepAlive` [OBS].
- `nucleus.ReverseNucleusAPI/`: engine→app callbacks incl. `SubscribeToBolt`,
  `PublishEvent`, `GetBlockFromPeer` [OBS].

`LookupByLocalPath` reply distinguishes `FSValid` / `InsideDropbox` / `DBXValid` /
`DBXInvalid` states [OBS `LookupByLocalPathReply_FSValid_InsideDropbox_DBXValid`].

---

### 13. Engine-wait "not synced" taxonomy (completion signal) [OBS]

To know "am I fully synced?", the engine aggregates outstanding work. A reimplementer
should expose the same signal; the observed reasons a namespace is **not** up to date:
`ProtocolWorkerConsistentCut`, `ProtocolWorkerLinearizedList`, `ProtocolWorkerCommit`,
`ProtocolWorkerCommitAck`, `PendingSetNotEmpty`, `PendingSetCapped`, `EnumerateChanges`,
`AnchorPlannerNotSynced`, `PreLocalNotEmpty`, `PreLocalNotFound`,
`GlobalSyncStateNotEmpty`, `ProtocolNotSynced`, `EncryptedStubsNotEmpty`, `DFCNotEmpty`,
`FileEventsNotEmpty`, `CloudFilesMigrationRunning` [OBS]. Fully-synced path logs
`fully_synced`, `incremental_sync … fully_synced`, `list_up_to_date`, `Canopy UpToDate`
[OBS].

---

### 14. Gaps / [UNK]
- Exact protobuf field numbers/wire layout of `CommitRequest`, `ConsistentCutListPage`,
  `HlcLinearizedPage`, and `SignedConsistentCutCursor` (field names observed; tag
  numbers not recoverable from strings).
- Exact HLC encoding (physical-ns + logical-counter widths) and the signature algorithm
  over `SignedConsistentCutCursor`.
- Precise `GetInitialCursor` vs `GetNamespaceInfo` ordering at first link, and whether a
  single call returns all namespaces or one per ns.
- Exact Bolt long-poll wire framing and how `has_delta` channels map to ns_ids.
- Content block size constant (SHA256 is the dominant hash; a lone `1048576` appears but
  the classic 4 MiB block boundary is not confirmed by a numeric literal).## Block Storage & Transfer — rebuild spec

All identifiers below were recovered by grepping the native string tables:
`/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/corpus/str_libdropbox_core.so.txt` (core/Nucleus) and
`/tmp/claude-0/-home-user-claude-speriments/259f29e2-6459-5b23-98f4-515a390c56f5/scratchpad/corpus/str_libdropbox_tprt.so.txt` (transport). The block subsystem lives entirely in `libdropbox_core.so` under `desktop/rust/nucleus/`.

### 1. Service surface: the `nsf.Nsf` gRPC service

[OBS] Exactly five block RPCs are exposed as gRPC `:path` strings, all under one service `nsf.Nsf` served by host `nsfserver`:

- `/nsf.Nsf/GetBlock`
- `/nsf.Nsf/PutBlock`
- `/nsf.Nsf/GetBlockSignature`
- `/nsf.Nsf/GetRsyncBlock`
- `/nsf.Nsf/PutRsyncBlock`

[OBS] The server string `idHostClientInitiatedReconnectnsfserver/nsf.Nsf/PutRsyncBlock/nsf.Nsf/PutBlock/nsf.Nsf/GetRsyncBlock/nsf.Nsf/GetBlockSignature/nsf.Nsf/GetBlock/sync_frontend.Meta/Reassociate` concatenates the five block paths next to the metadata service, confirming they are distinct services. [OBS] Reply message type names recovered: `GetBlockReply`, `PutBlockReply`, `GetBlockSignatureReply`, `GetRsyncBlockReply` (e.g. the run `GetBlockReplyGetBlockSignatureReply`, and `ResponseContextPutBlockReply`). [INF] Each RPC is unary gRPC-over-HTTP/2 (`application/grpc+proto`, per EVIDENCE §5) routed to the Dropbox **block server** tier (see §12), carried by the vendored `h2-0.3.26`/`hyper-0.14.31` stack in `libdropbox_tprt.so`.

[OBS] Block replies carry a wrapper envelope: strings `GrpcV2Error`, `ProtoError`, `MissingResponseContext`, `ResponseCode`, `ResponseContext`, and `ResponseCodeBadFileId` show a `ResponseContext{ response_code, message }` is returned alongside each block reply; `BadFileId` is one enumerated response code. [INF] A reimplementer must wrap each `*Reply` in a response-context that reports a block-server status code (at least `BadFileId`, plus a generic/unknown path) in addition to gRPC trailers `grpc-status`/`grpc-message`.

### 2. File → block model (blocklist)

[OBS] A file's content is modeled as an ordered **blocklist**: identifier `blocklist` appears >100×, with messages `local blocklist must be filled in prior to commit`, `should always have a blocklist during commit`, `Expected blocklist:` / `, Actual blocklist:`, `Every node in ... must have a blocklist`, and the per-node fields `blocklist`, `content_hash`, `attr_data`, `mtime` carried in SyncedTree update records (`blocklistFileContentcontent_hash`). [INF] The blocklist is the authoritative content representation of a file: an ordered sequence of block hashes; file size is the sum of block lengths. A directory/symlink node has no blocklist; a regular file always has one at commit time.

[OBS] The file-level content identity is derived **from the blocklist**: identifiers `checksum_from_blocklist`, and the error `Coauth: checksum from blocklist does not match checksum from local metadata`, and `blocklist_hash` (in the PNM record run `PNMList_unrecognizedblocklist_hashxattr_hashmtimepnmoid`). [INF] `content_hash` / `blocklist_hash` is a digest computed over the ordered blocklist (the classic Dropbox content-hash construction: hash of the concatenation of per-block hashes), not over the raw file bytes directly. This matches Dropbox's publicly documented content-hash algorithm (SHA-256 of each ≤4 MiB block, then SHA-256 of the concatenated block digests).

[OBS] Blocklists are persisted and compared across the three trees Nucleus maintains: `local_blocklist`, `locally_synced_blocklist`, `synced_blocklist`, plus `Coauth: synced blocklist does not match remote blocklist`. [INF] Sync reconciliation compares local vs. locally-synced vs. remote blocklists to decide add/edit/no-op.

### 3. Block hashing — which algorithm, where

[OBS] Block hashes are produced by a function `BlockHash::from_data` (string `BlockHash::from_data` appears twice, e.g. `perform fp preparation task. Retrying...BlockHash::from_data`). [OBS] The hash-function implementation crate is `desktop/rust/dropbox/hash_functions/src/imp.rs`.

[OBS] The only cryptographic digest primitives present are OpenSSL's (statically linked OpenSSL 3.5.5): symbols `SHA256`, `SHA256 block transform for x86_`, `SHA256 multi-block transform fo`, `EVP_MD_get_block_size`. The only vendored Rust hash crates are **non-cryptographic** map/RNG hashers: `rapidhash-4.4.1`, `wyhash-0.6.0`, `hashbrown-*`, plus `sha1_smol-1.0.0`. No `sha2`, `blake2`, or `blake3` Rust crate is vendored.

[OBS] `BLAKE2b`/`BLAKE2s` strings (`BLAKE2B-512:BLAKE2b512:1.3.6.1.4.1.1722.12.2.1.`, `blake2b512_internal_final`, `ossl_blake2b_get_ctx_params`) are present, but every one is an **OpenSSL algorithm-registry / OID string**, i.e. part of the statically linked OpenSSL provider table, not a block-hashing call site.

[INF] Therefore block content hashing uses **SHA-256 (via OpenSSL EVP)**, not BLAKE. BLAKE2 is merely compiled into the bundled OpenSSL and is not evidenced as the block-addressing hash. This corrects EVIDENCE §9's open question: SHA-256 is the block/content hash; BLAKE presence is an OpenSSL artifact.

[OBS] `block_hash` is stored as a SQLite `BLOB` (`block_hash BLOB NOT NULL`), i.e. raw digest bytes, not hex. [INF] 32-byte SHA-256 digests. [OBS] An MD5 hasher also exists (`Couldn't create MD5 hasher`, `Couldn't update MD5 hasher`) [INF] used for a legacy/compat checksum, not block addressing.

### 4. Chunking / block size

[OBS] Files are split into fixed-size blocks (no content-defined/rolling-hash chunking evidenced for the primary split). The rsync-delta path has an explicit minimum-size gate: `Block size less than 64KB.No parent block` in the `upload_rsync_block` failure path. [OBS] Config field `max_full_blocks_buffered` bounds how many whole blocks are buffered in memory during transfer; `enable_extended_block_upload_logging` and `block_format` sit beside it.

[INF] The primary chunker emits uniform blocks (Dropbox classic = **4 MiB** max per block); the exact constant (e.g. 4194304) was not found as a literal string in the corpus, so the size is [INF] not [OBS]. A block below 64 KiB is never delta-encoded — it is uploaded whole via `PutBlock`. [OBS] The HTTP/2 layer's own `CHUNK_SIZE_MAX_BYTES`, `chunked`, `transfer-encoding: chunked` strings are HTTP/1 transfer-encoding machinery in `hyper`, unrelated to Dropbox block chunking — do not conflate.

### 5. Block compression

[OBS] Two block wire formats, enumerated as `Uncompressed` / `Brotli` (string `block_transfer::uploadsuccessUncompressedBrotliBlock`), selected per transfer and echoed back in error records as `requested_block_format` (fields `requested_block_format`, `block_hash`, `block_size`, `decompression_error`). [OBS] A second enum run `regularrsyncuncompressedbrotli` pairs the transfer *kind* (`regular` vs `rsync`) with the compression (`uncompressed` vs `brotli`). [OBS] Compression crate is `brotli-5.0.0` (+ `brotli-decompressor-4.0.0`); error strings `brotli decompress failed` and `Unrecoverable decom...pression error ... when we asked for uncompressed?`.

[OBS] Compression crate module: `desktop/rust/nucleus/block_compression/src/lib.rs`. [OBS] Compression telemetry fields: `compression_quality`, `block_compression_time`, `compression_with_wait`, `only_compression_ms`, `compression_with_wait_ms`, `uncompressed_size_bytes`. [INF] The client Brotli-compresses a block before `PutBlock`, choosing a quality level; if the compressed form is not smaller it falls back to `Uncompressed`. On download it decompresses according to `requested_block_format`; a mismatch ("asked for uncompressed" but got compressed) is a hard error.

### 6. Upload path (PutBlock / commit) + upload-token dedup

[OBS] Upload is implemented in `desktop/rust/nucleus/block_transfer/src/upload.rs`; `block_source::on_disk` reads the plaintext block from the local file. Upload telemetry (`network/upload_block/...`): `duration_ms`, `size_bytes`, `uncompressed_size_bytes`, `compression_with_wait_ms`, `only_compression_ms`; aggregate `upload_blocks/estimated_bandwidth_per_sec`, `upload_blocks/total_size`, `upload_file/uploaded_bytes`, `upload_file/skipped_canopy_bytes`, `upload_file/skipped_already_uploaded_bytes`, `upload_file/bandwidth_bytes_per_second`.

[OBS] **Upload-token dedup cache** — exact schema from core SQL (`desktop/.../sqlite/block_upload_tokens.rs`):
```
CREATE TABLE IF NOT EXISTS file_block_upload_tokens (
    fileid BLOB NOT NULL,
    block_hash BLOB NOT NULL,
    ts INTEGER NOT NULL,
    token BLOB NOT NULL,
    PRIMARY KEY(fileid, block_hash)
) WITHOUT ROWID;
CREATE INDEX file_block_upload_tokens_block_hash_idx ON file_block_upload_tokens (block_hash, ts);
CREATE INDEX file_block_upload_tokens_prune_idx     ON file_block_upload_tokens (ts);
INSERT OR REPLACE INTO file_block_upload_tokens(fileid, block_hash, ts, token) VALUES(:fileid,:block_hash,:ts,:token);
```
[OBS] Operations: `persist_block_upload_token`, `fetch_block_upload_tokens_for_fileid`, `count_block_upload_tokens`, `clear_block_upload_tokens`, `prune_block_upload_tokens`; metrics `block_upload_tokens/remaining`, `block_upload_tokens/pruned`. [INF] Protocol: after a successful `PutBlock`, the server returns an opaque **upload token** proving the block is stored; the client caches `(fileid, block_hash) → token` keyed by timestamp. At commit, the client presents cached tokens for blocks already on the server instead of re-uploading them (this is the `skipped_already_uploaded_bytes` accounting). Tokens are pruned by age (`ts`, `prune_idx`).

[OBS] **Commit** is the metadata push that references the uploaded blocklist. `CommitRequest` variants: `CommitRequestAdd`, `CommitRequestEdit`, `CommitRequestMove` (`dst_ns_id`, `ds...`), `CommitRequestDelete` (`fileid`). Commit error enum `CommitRequestError`: `FileTooLarge`, `InternetError`, `OqCommitPrevented`, `OverQuota`, `TeamFolderOverQuota`, `UnknownError`. Upload operation context strings `CommitAdd`/`CommitEdit`. [OBS] Commit traffic goes through `sync_frontend.Meta` (not `nsf.Nsf`): methods include `CommitAtHead`, `AcknowledgeCommits`, `GetPendingUploads`, `ReportPendingUploads`, `GetInitialCursor`, `LinearizedList`, `ConsistentCutList`, `CommunicateCommand`, `AllocateFileId`, `GetNamespaceInfo`, `GetResyncState`/`SetResyncState`, `Reassociate`.

[OBS] **Commit batching** (`commit_batch`): telemetry event `commit_batch_stats` with counters `adds`, `edits`, `moves`, `deletes`; and a guard event `commit_batch_over_size_limit` with fields `tokens_size`, `proto_size`, `blocks`, `total_bytes`, `requests`. [INF] The client batches multiple file operations into one commit RPC, but caps the batch by serialized protobuf size, number of blocks, number of upload tokens, and total bytes; when a batch would exceed a limit it is split (the `over_size_limit` event fires).

[OBS] Resumable uploads: `sync_frontend.Meta/GetPendingUploads` + `ReportPendingUploads`, plus the uploader config run `Block uploader configurationconfiglong_block_upload_waitactive_fileids_statesactive_fileidsin_progress_empty`. [INF] The client can query/report in-flight uploads so an interrupted large-file upload resumes rather than restarting.

### 7. Download path (GetBlock) + block_finder + block_source dispatch

[OBS] Download is implemented across `block_transfer/src/download.rs` and `block_transfer/src/range_download.rs`. Telemetry (`network/...`): `block_download_latency/duration_ms`, `block_download_success/duration_ms`, `block_download_success/size/delta_bytes`.

[OBS] **block_finder** (`desktop/rust/nucleus/block_finder/src/{block_finder.rs,decode_block.rs,network_fetcher.rs,logging_events.rs}`) resolves where to get a needed block from. Events: `network/block_finder_attempt`, `network/block_finder_success`, `network/block_finder_error`, `network/block_finder_block_missing`; decode stage `decode_block.rs`; missing-block escalation events `reconstruct_block_missing` (field `block_needed`) and `external_recall_block_missing`.

[OBS] **block_source** roles (`desktop/rust/nucleus/block_source/src/{on_disk.rs,p...}`, field `block_source_name`, error `Error occurred while fetching block from source`). The block-source dispatch enum is the concatenated run `...NetworkFetcherLocalBlockCacheP2PBlockSourceInstantFilesDownloadManager...`. [INF] When a block is needed the finder tries sources in priority order: already-on-disk (`on_disk`/`LocalBlockCache`) → peer (`P2PBlockSource`) → fast path (`InstantFiles`) → server (`NetworkFetcher`/`DownloadManager`). `Found block locally` and `Skipping dataless local block` confirm the local-first behaviour.

[OBS] **Flow control / ticketing**: `block_transfer/src/block_ticketer.rs` and `dynamic_ticketer.rs` implement a `TicketMaster` that hands out a bounded number of concurrent-transfer "tickets" (`TicketMasterInner(max_tickets=`, `num_tickets=`, `Can't request no tickets`, `adjusted_max_tickets`/`old_max_tickets`/`direction`/`bandwidth`, `current bandwidth = `). [OBS] Configured by `MAX_DOWNLOADS`, `max_downloads`, `max_uploads`, `max_full_blocks_buffered` (`Using network blocks configmax_downloadsmax_uploads`). [INF] The dynamic ticketer adjusts the concurrency ceiling up/down based on measured bandwidth per direction (upload vs download), throttling parallel `GetBlock`/`PutBlock` calls.

### 8. Local block cache (LBC) + local block index + on-disk store

[OBS] **local_block_cache** crate `desktop/rust/nucleus/local_block_cache/src/{cache.rs,index.rs,store.rs}`; logged as `LocalBlockCache` / tag `[LBC]`. Index table (`index.sqlite`), exact schema:
```
CREATE TABLE IF NOT EXISTS lbc_blocks (
    hash BLOB PRIMARY KEY,
    length INTEGER NOT NULL,
    last_access_ms INTEGER NOT NULL,
    inserted_as_prefetch INTEGER NOT NULL,
    prefetch_time_ms INTEGER NOT NULL
) WITHOUT ROWID;   -- versioned via PRAGMA user_version
SELECT hash, length, last_access_ms, inserted_as_prefetch, prefetch_time_ms FROM lbc_blocks;
INSERT OR REPLACE INTO lbc_blocks(hash,length,last_access_ms,inserted_as_prefetch,prefetch_time_ms) VALUES(...);
UPDATE lbc_blocks SET last_access_ms = :ts WHERE hash = :hash;
DELETE FROM lbc_blocks WHERE hash = ?;
```
[INF] `index.rs` keeps the SQLite row per cached block (hash → length, LRU `last_access_ms`, whether it arrived via prefetch, and prefetch latency). `store.rs` is the on-disk block byte store (`[LBC] put_block store write failed (fail-soft)`, `LocalBlockCache::put_block_io`, `LocalBlockCache::read_block`, `from_wire`); writes are fail-soft (a store write failure does not abort the download). `cache.rs` is the policy/coordinator.

[OBS] LBC operations and metrics (`local_block_cache/...`): `hit`, `miss`, `hit_recall`, `evicted`, `put_committed`, `put_failed`, `put_skipped_resident`, `hash_verify_failed`, `kill_switch_off`, `prefetch/hit_prefetched`, `prefetch/evicted_unread`, `usage_stats/{current_bytes,resident_blocks,cap_bytes,fill_fraction}`, and a reconcile pass `reconcile/{runs,rows_reaped,bytes_reclaimed,files_deleted,scan_incomplete,accounting_drift}`. [OBS] Prefetch has a `LBC_PREFETCH window_policy`. [OBS] Tunables (Stormcrow/config keys): `desktop_nucleus_local_block_cache_cap_bytes`, `desktop_nucleus_local_block_cache_prefetch...`, `desktop_nucleus_local_block_cache_serve_extra_present_bytes`. [INF] Cache is a size-capped (`cap_bytes`) LRU keyed by block hash; a reconcile sweep reconciles the SQLite index against the on-disk store (reaping orphan rows, deleting orphan files, correcting byte accounting). `hash_verify_failed` shows blocks are re-hashed on read to detect corruption. There is a runtime kill-switch (`kill_switch_off`, "gate off at startup; cache will not be constructed").

[OBS] **local_block_index** crate `desktop/rust/nucleus/local_block_index/src/lib.rs`: a reverse index mapping a needed block hash to a location in an already-synced on-disk file. Strings: `Block hash should have at least one location`, `Block index is missing fileid for block hash`, `fileid given by local block index`, `partial block index must be within file bounds`, `partial verify: block index out of bounds`. [INF] Given a block hash required to materialize a file, the index finds another local file (by `fileid` + offset) that already contains that block, so the block is read from disk (dedup) instead of downloaded — and the same index lets the client answer peers' `CheckBlockExistsForPeer`/`GetBlockForPeer` (§10).

### 9. rsync delta protocol (GetBlockSignature / GetRsyncBlock / PutRsyncBlock)

[OBS] Delta sync operates at the level of a single block against a **parent block** (the same block index in the previous version of the file). Strings: `must have parent block data`, `No parent block`, `Block size less than 64KB` (the gate), `Failed to calculate rsync delta`, `Failed to get block rsync signature`, `Failed to upload rsync block`.

[OBS] `upload_rsync_block` telemetry carries the delta accounting: fields `compression_quality`, `uncompressed_delta_size`, `patch_size`, `block_size`, `block_hash`, `error_string`, `elapsed_time`, `success`; wire metrics `network/upload_rsync_block/duration_ms`, `network/upload_rsync_block/size_bytes`. [OBS] Signature retry/abort: `Block_signature failed too many times`, `Block_signature failed for a non-transient reason`, `not supported for this signature type`.

[INF] Delta-upload sequence a reimplementer must build (edit of a large file):
1. For each changed block ≥ 64 KiB that has a parent block, call `GetBlockSignature(parent block_hash)` → `GetBlockSignatureReply` carrying an rsync-style signature (rolling weak checksum + strong hash table) of the parent block.
2. Locally compute an rsync **delta/patch** of the new block against that signature (`patch_size` = compressed delta, `uncompressed_delta_size` = raw delta).
3. Brotli-compress the patch (`compression_quality`) and upload it via `PutRsyncBlock` (parent `block_hash` + patch) instead of the full block via `PutBlock`. Blocks < 64 KiB or with no parent fall back to full `PutBlock`.

[INF] Delta-download is the mirror: `GetRsyncBlock` returns a patch against a block the client already has locally; `block_download/must have parent block data` shows the client supplies/holds the parent and applies the patch to reconstruct the target block, verifying the result hashes to the expected `block_hash`.

### 10. Peer-to-peer / LAN block source

[OBS] A LAN-sync block path exists under the phase-agnostic Nucleus API, separate from `nsf.Nsf`: `nucleus.NucleusPhaseAgnosticAPI/GetBlockForPeer` and `/CheckBlockExistsForPeer`, with reverse-direction messages `GetBlockForPeerReq`, `GetBlockFromPeerReply`, `CheckBlockExistsForPeerReq`, and errors `GetBlockForPeer Block not found`, `Ignoring GetBlockForPeer while paused`, `Peer Block not found`. [OBS] P2P transport/crypto: `P2PError` with `TcpBindFailure`/`UdpBindFailure`/`InvalidUri`, `UpdateP2PKeysReq`, `P2PKeyContainer`, magic/cmd framing (`lengthcmdmagicP2P`), result event `p2p_block_download_result` (fields `block_hash`, `error_string`, `latency`), corruption guard `network/p2p/p2p_rust_corrupt_block_detected`. [INF] On a LAN the client can serve/fetch blocks directly from peer devices (using `local_block_index` to answer "do I have this block"), authenticated with exchanged P2P keys, falling back to the block server on miss/corruption.

### 11. fs_api.FsApi file operations

[OBS] The `fs_api.FsApi` gRPC service (local, over UDS/DFC) mediates filesystem materialization. Recovered methods: `mergeFromDropbox`, `UnmergeFromDropbox`, `RenameIntoDropbox` (`RenameIntoDropboxRequest`), `bindFromDropbox`, `DeleteDeviceAnchor`, `CreateEphemeralTempDir`, `CreateTempVolume` (`DropTempVolumeReq`), `CreateFile`, `CreateBreadcrumbs`/`RemoveBreadcrumbs`, `GetPublishedEvents`/`ExtPublishedEvents`. Parallel verbs exist on `nucleus.NucleusPhaseAgnosticAPI` (`BindIntoDropbox`, `UnbindFromDropbox`, `RenameIntoDropbox`). [INF] These move a fully-materialized file from a temp volume into the synced tree ("into Dropbox") once its blocklist is committed, and back out; they are the bridge between block materialization and the user-visible filesystem.

[OBS] Smart-sync / placeholder hydration ties block download to file access: `UpdateHydrationPolicy` (SyncEngineApi), `EffectiveHydrationPolicy`, `HydrationPolicyHidden`, `dematerialization_failed`, `is_dataless_file`, `Hydrating external placeholder`, `Can't access blocks` (when hydrating), `infinite_hydration_completed`. [INF] A dataless placeholder triggers a block download (via block_finder → GetBlock) on access to hydrate it; dematerialization drops the local bytes but keeps the blocklist.

### 12. Server routing & transport

[OBS] A service-tier routing enum names the block server distinctly: run `UNKNOWN_SERVICEBLOCK_SERVERSYNC_FRONTENDBOLT_SERVERAPI_V2` (with rate buckets `OPS_RATE`/`BYTES_RATE`). [INF] `GetBlock`/`PutBlock`/rsync RPCs route to `BLOCK_SERVER`; commits/listing to `SYNC_FRONTEND`; push notifications to `BOLT_SERVER`. Per EVIDENCE §6 the block exception host is `dl-debug.dropbox.com` (`blockexcserver`); the production block endpoint is selected via the `DROPBOX_HOST`/server-map (`apex/rust/dbxconn/src/server_map`).

### 13. Encrypted-folder blockwise encryption (interaction with blocks)

[OBS] For encrypted folders/Vault the blocklist exists in two forms: `plaintext_blocklist`, `encrypted_plaintext_blocklist`, `plaintext_blocklist_encryption_extras`, with `encryption_scheme` and `keyid`, implemented in `desktop/rust/nucleus/encryption/src/blocklist_crypto.rs`. [OBS] Errors: `intext size not supported for blockwise derived encryption`, `derived encryption.blocklist length mismatch`, `Plaintext blocklist decryption failed`, `Encrypted plaintext blocklist with a missing key reached ca...`, `Coauth: placeholder checksum out of sync with blocklist`. [INF] Block bytes are encrypted per-block with a key derived per file (blockwise derived encryption); the server stores and transfers ciphertext blocks while the client keeps a plaintext blocklist and a mapping to the encrypted blocklist, the two required to be equal length. This is distinct from TLS and from the session host-key.

### 14. Summary of the end-to-end block protocol a reimplementer must build

[INF] (1) Split file into uniform blocks (≤4 MiB [INF]); (2) hash each block with SHA-256 (`BlockHash::from_data`) → `block_hash` (raw 32-byte BLOB); the ordered list is the blocklist; (3) the file content_hash/checksum is a digest over that blocklist; (4) for each block not already proven present (no cached upload token, not found locally/at a peer): Brotli-compress and `PutBlock` (or, for an edited large block with a parent, `GetBlockSignature`→compute delta→`PutRsyncBlock`), receiving an upload token cached in `file_block_upload_tokens`; (5) commit the blocklist + metadata via `sync_frontend.Meta/CommitAtHead`, batched under size caps, presenting cached tokens; (6) on download, `block_finder` resolves each needed block from local disk / `local_block_cache` / peer / `nsf.Nsf/GetBlock` (or `GetRsyncBlock` patch), decompresses per `requested_block_format`, verifies the hash, caches it in `lbc_blocks`, and `fs_api.FsApi/mergeFromDropbox` materializes the file.## Bolt notification channel — rebuild spec

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
- The precise header that carries the OAuth bearer, and whether host-key is ever used as a fallback for Bolt.## Persistence & Crypto — rebuild spec

Static analysis of `libdropbox_core.so` (Nucleus + apex), the 6 KB `libdropbox_sqlite_ext.so`, and the on-disk `.pyc` files. All DDL/SQL/scheme tokens below are concatenated Rust string literals recovered by `strings`; file-source paths (`desktop/rust/...`) are embedded panic/source paths. Several EVIDENCE.md claims are **corrected** here (noted inline).

### 1. SQLite stack, PRAGMAs, and the `.dbx` codec [OBS/INF/UNK]

- SQLite is a **patched vendored build**: `desktop/rust_patched_vendor/libsqlite3-sys-0.37.0/src/error.rs` [OBS] driven by `rusqlite-0.39.0` [OBS from EVIDENCE/§1]. "patched" + the error string `Cannot decrypt database` [OBS] indicate a **page codec compiled into the C SQLite amalgamation** (not a separate library).
- **CORRECTION to EVIDENCE.md:** `libdropbox_sqlite_ext.so` is **NOT** the encryption codec. Its only exports are `sqlite3_dropboxsqliteext_init` / `sqlite3_extension_init` [OBS, dynsym] and its only data strings are `invalid arguments`, `DIRTRAVERSE`, `server_path_ns`, `server_path_rel` [OBS]. It is a small loadable extension providing a `DIRTRAVERSE` virtual table and `server_path_ns`/`server_path_rel` path-decomposition scalar functions. A reimplementer should model it as an auxiliary SQL helper, not crypto.
- **No SQLCipher.** There is no `PRAGMA key`, `PRAGMA cipher_*`, `sqlite3_key`, `sqlite3_rekey`, `sqlite3_activate_see`, or `sqlcipher` anywhere in either corpus [OBS-absence]. The `cipher_*` tokens present (`cipher_from_algorithm`, `cipher_generic_block_update`, `cipher_asn`, `cipher_ctx`) are **OpenSSL EVP provider internals**, not a DB codec [INF]. So the `.dbx` format is Dropbox's own page codec, keyed out-of-band (see §2), **not** a PRAGMA-keyed SQLCipher DB.
- **Exact `.dbx` page algorithm = [UNK]** from strings (the codec is compiled C with no stringy function names). What a reimplementer can rely on: OpenSSL 3.5.5 is statically present in core too (`OpenSSL 3.5.5`, `openssl-0.10.73`, `openssl-sys-0.9.109` [OBS]) and the generic cipher tables include `AES-256-GCM`/`AES-256-CBC`; combined with the keystore's `database_key` (§2) the codec almost certainly does AES page encryption with a per-DB key [INF]. Page header/reserve-byte layout, IV derivation, and per-page MAC are unresolved [UNK].
- **PRAGMAs applied on open** [OBS, all literal]: `PRAGMA journal_mode = WAL`, `PRAGMA synchronous = EXTRA` (also `= FULL` seen), `PRAGMA secure_delete = false`, `PRAGMA locking_mode = EXCLUSIVE`, `PRAGMA page_size = 4096`, `PRAGMA auto_vacuum = 0`, `PRAGMA automatic_index = false`, `PRAGMA cache_spill = true`, `PRAGMA fullfsync = true`, `PRAGMA cache_size = -8192` (≈8 MiB), `PRAGMA wal_autocheckpoint = 4000`, `PRAGMA journal_size_limit = 10485760` and `= 536870912`. Schema versioning uses `PRAGMA user_version` with `code_version`/`user_version` compared (`UnknownUserVersionGreaterThanCodeVersion`, `ExpiredDatabaseVersion` [OBS]); migrations run via `desktop/rust/dropbox/sqlite_migrate/src/lib.rs` [OBS].

### 2. Keystore and the DB-key / host-secret chain [OBS/INF/UNK]

- apex C-API `desktop/app/lib/apex/c_api/src/keystore.rs`, impl `apex/rust/keystore/src/{lib,posix}.rs` [OBS]. Exported FFI: `keystore_create`, `keystore_create_user_key`, `keystore_retrieve_database_key`, `keystore_retrieve_user_key`, `keystore_destroy` [OBS]. So there are **two managed secrets: a `user_key` and a `database_key`**; `keystore_retrieve_database_key` supplies the key the `.dbx` codec uses [INF].
- **Linux backend is file-based, not Secret Service.** There are **no** `libsecret`, `org.freedesktop.secret`, `SecretService`, `gnome-keyring`, or `kwallet` strings in either binary [OBS-absence]. The posix keystore instead handles base64 + JSON + an integrity digest: `Cannot base64 decode`, `JSON value is not a string:`, `Digest is not what is expected` [OBS]. [INF] the Linux keystore is a local file storing base64-encoded JSON key material with a verification digest (consistent with legacy `~/.dropbox/` host-key storage); exact file path and the digest/derivation algorithm are [UNK].
- **`config.dbx` / `instance.dbx` (encrypted) are read by `apex/rust/dbxauth/src/lib.rs`** [OBS]. Observed SQL: `SELECT id, appdata_path, uid, master FROM instance WHERE active = 1 AND uid > 0` [OBS] — the `instance` table columns are `id, appdata_path, uid, master, active`; and `SELECT key, value FROM config` [OBS] with observed **string config keys**: `host_int`, `host_id`, `account_id`, `email`, `user`/`displayname`, `role`, `dropbox_path`, `home_ns`/`root_ns`, `home_ns_path`, `root_ns_fileid`/`home_ns_fileid`, `root_layout`, `cached_ui_flags`, `is_team_admin`, `team_id`, `non_team_sharing_disabled`, `team_file_transfers_disabled`, `team_send_for_signature_disabled` [OBS]. `host_int` is the secret host key; log redaction renders it as the literal `[host secret]` [OBS]. The dbxauth in-memory config object additionally carries `host_key`, `root_mount_path`, `root_ns_id`, `home_ns_id`, `has_tmf`, `user_display_name`, `host_display_name`, `instance_id`, `is_primary` [OBS]. A reimplementer must model `config.dbx` as the encrypted store of the device's host-key credential + account/namespace bootstrap data, with its codec key held by the keystore.
- A generic key-value helper (`desktop/app/lib/base/sqlite_kv_store/rust/src/lib.rs`) issues `SELECT key, value FROM <tbl> WHERE key = ?` / range scans [OBS]; it backs config-style tables.

### 3. Database files and schemas [OBS/INF]

Encrypted (`.dbx`) [OBS filenames]: `config.dbx`, `instance.dbx` (appears as `instance_dbinstance.dbx`), `dropboxignore.dbx`, `dbxignore_hash_failure.dbx`, `dbxignore_rules_updated.dbx`, `rulesnum.dbx`, `value.dbx`, `filehistorytoolkit.dbx`. Plaintext SQLite [OBS filenames]: `nucleus.sqlite3`, `fp_shadow_copy_nucleus.sqlite3`, `apex.sqlite3`, `index.sqlite`. Vault: `Vault.db` [OBS] with on-disk folder markers `.dbx-vault`, `.dbx-passwords`, `.dbx-backup` [OBS].

- **CORRECTIONS to EVIDENCE.md file list:** `Q.sqlite` is **not a real file** — every occurrence is `%Q.sqlite_sequence` / `%Q.sqlite_stat1` / `%Q.sqlite_stat4`, i.e. SQLite's own `%Q` printf format in ANALYZE/VACUUM SQL [OBS]. `vacuum_db.sqlite` is likewise **not a file** — it is the `vacuum_db.sqlite_master` attached-DB alias SQLite uses internally during `VACUUM` (`INSERT INTO vacuum_db.sqlite_master SELECT*`) [OBS]. `binfilehistorytoolkit.dbx` should read `filehistorytoolkit.dbx`; the `bin` prefix is the tail of `$RECYCLE.BIN` in the default-ignore pattern string (`...system volume information$recycle.bin` + `filehistorytoolkit.dbx` + `ignore` + `**/*.pape...`) [OBS].

**Nucleus sync-metadata schema** (source `desktop/rust/nucleus/database/src/...`, DB `nucleus.sqlite3` [INF from path+filename co-location]), exact DDL [OBS]:

- `config_table.rs`: `CREATE TABLE config (key INTEGER PRIMARY KEY, value BLOB NOT NULL)` — note the **nucleus config key is INTEGER-keyed** (distinct from the string-keyed apex `config` in `config.dbx`). Access: `SELECT value FROM config WHERE key = ?`, `INSERT OR REPLACE INTO config (key, value) VALUES (?, ?)`, `DELETE FROM config WHERE key = ?`.
- `fp_local_tree.rs`: `CREATE TABLE fp_local_tree (itemid INTEGER NOT NULL, creation_id BLOB, version INTEGER PRIMARY KEY, fileid BLOB, dir_itemid INTEGER, filename BLOB, metadata BLOB, latest BOOL NOT NULL)` with indexes `fp_local_tree_itemid`, unique `fp_local_tree_latest_itemid`/`_latest_fileid`/`_latest_creation_id` (WHERE latest), `fp_local_tree_not_latest`, unique `_latest_dir_itemid_index (dir_itemid, filename) WHERE latest`, `_dir_itemid_by_name_index`, `_dir_itemid_by_version_index`. This is a **versioned local-tree table** (each node row is a `version`; `latest` flags the live row; `metadata` is a protobuf BLOB). Insert columns: `(itemid, version, fileid, dir_itemid, filename, metadata, latest, creation_id)`.
- `transplant` (consistent-cut): `CREATE TABLE transplant(ns_id BLOB NOT NULL, path_hash BLOB NOT NULL, path_state BLOB NOT NULL, fileid BLOB, parent_path_hash BLOB NOT NULL, sjid INTEGER NOT NULL, PRIMARY KEY (ns_id, path_hash))`. Upsert keyed on `(ns_id, path_hash)` with `sjid < excluded.sjid` guard [OBS].
- `update_info`: `CREATE TABLE update_info(row_id INTEGER PRIMARY KEY, fileid BLOB NOT NULL, ns_id BLOB, is_delete BOOL, transplant_record BLOB, CHECK ((ns_id IS NOT NULL AND is_delete IS NOT NULL) OR (ns_id IS NULL AND is_delete IS NULL AND transplant_record IS NOT NULL)))` + unique index `update_info_node_fileid ON update_info(fileid) WHERE ns_id IS NOT NULL` [OBS].
- `deleted_files.rs`: `CREATE TABLE IF NOT EXISTS deleted_files (identifier BLOB PRIMARY KEY, prune_after INTEGER NOT NULL, dirtied_on INTEGER, original_data BLOB NOT NULL, last_observed_stat BLOB)` + index on `(dirtied_on, prune_after) WHERE last_observed_stat IS NOT NULL`; legacy sibling `fp_deleted_files (identifier, original_path, stat)` [OBS].
- `block_upload_tokens.rs`: `CREATE TABLE IF NOT EXISTS file_block_upload_tokens (fileid BLOB NOT NULL, block_hash BLOB NOT NULL, ts INTEGER NOT NULL, token BLOB NOT NULL, PRIMARY KEY(fileid, block_hash)) WITHOUT ROWID` + `_block_hash_idx(block_hash, ts)` + `_prune_idx(ts)`; proto `proto_database::persistence::UploadBlockToken` [OBS]. Caches per-block upload authorization tokens.
- `db_fileid_map.rs` (Linux inode↔fileid + synced xattrs): `CREATE TABLE IF NOT EXISTS fs_linux_fileids (fh BLOB PRIMARY KEY, fileid BLOB NOT NULL) WITHOUT ROWID` and `CREATE TABLE IF NOT EXISTS fs_linux_xattrs (fh BLOB NOT NULL, name TEXT NOT NULL, data BLOB NOT NULL, PRIMARY KEY (fh, name))` [OBS].
- Local block cache (DB `index.sqlite`): `CREATE TABLE IF NOT EXISTS lbc_blocks (hash BLOB PRIMARY KEY, length INTEGER NOT NULL, last_access_ms INTEGER NOT NULL, inserted_as_prefetch INTEGER NOT NULL, prefetch_time_ms INTEGER NOT NULL) WITHOUT ROWID` [OBS]; from `nucleus/local_block_cache/src/index.rs`.

### 4. Node metadata (PNM) and on-disk crypto state [OBS/INF]

- **PNM = `per_node_metadata`** (protobuf) — confirmed by `per_node_metadata/deserialize/...` and `message per_node_metadata.PNMXattrValue` [OBS]. Node metadata is stored (in `fp_local_tree.metadata` BLOB and as the `user.com.dropbox.attributes` xattr) as a `PNMList` of typed attributes. Crypto-relevant PNM attribute types [OBS tokens]: `PNMListEncryptedFileDirectory`, `PNMAttributePerRevisionKeyInfo`, `PNMListContentEncryptionExtrasFile`, `PNMBlockwiseDirectory`, `PNMBlockAuthorizationToken`, `SymmetricCryptoExtras`, `PNMDeviceInfo`; and node-content types `EncryptedFile`, `PerRevisionKeyInfo`, `ContentEncryptionExtras`, `Blockwise`, `SymmetricCryptoExtras` [OBS]. Error `Could not parse EncryptedFile from PNM!` [OBS].
- **Synced Dropbox xattrs a reimplementer must preserve** [OBS literal names]: `user.com.dropbox.attributes`, `user.com.dropbox.posix.executable`, `user.com.dropbox.internal`, `user.com.dropbox.device_anchor_target`, plus the macOS-origin set synced on all platforms: `user.com.dropbox.apple.ResourceFork`, `...apple.FinderInfo`, `...apple.metadata:_kMDItemUserTags`, `kMDItemFinderComment`, `kMDItemOMUserTags(/Time)`, `kMDItemStarRating`. Device-anchor xattr: `com.dropbox.device_anchor`. On-disk marker names: `.dropbox.attr`/`.dropbox.attrs`, `.dropbox.cache`, `.dropbox.device_anchor`, `.dropbox.external.fileid`, `.dropbox.external.writable`, `.dropbox.placeholder`; appdata dir `.dropbox` (plus `.dropbox-migrated`, `.dropbox-relocate...`) [OBS].

### 5. Encrypted-Folder / Vault key hierarchy — EKMS [OBS/INF]

Source crate `desktop/rust/nucleus/encryption/src/` [OBS], modules: `ekms.rs`, `key_crypto.rs`, `key_verification.rs`, `content_crypto/{mod,blockwise,helpers}.rs`, `blocklist_crypto.rs`, `client_key_pair.rs`, `file_key_batching.rs`, `team_key_cache.rs`, `metadata.rs`, `symmetric_schemes/aes256_gcm.rs`, `random.rs` [OBS]. **EKMS = the server-backed Encryption Key Management Service.**

**Crypto schemes (exact literals) [OBS]:**
- Asymmetric key-wrapping = **HPKE (RFC 9180)**: `HPKE_DHKEM_P256_HKDF_SHA256_HKDF_SHA256_AES256_GCM` and the Auth-mode variant `SENDER_AUTH_HPKE_DHKEM_P256_HKDF_SHA256_HKDF_SHA256_AES256_GCM` (lowercase form `sender_auth_hpke_dhkem_p256_hkdf_sha256_hkdf_sha256_aes256_gcm`). I.e. DHKEM(P-256, HKDF-SHA256) + KDF HKDF-SHA256 + AEAD AES-256-GCM, in base and sender-authenticated modes [OBS]. HPKE error set `EncapError/DecapError/OpenError/ValidationError`, `Invalid ciphertext length`, `Algorithm mismatch` [OBS].
- Symmetric metadata = `AES_256_GCM_META_EXTRAS` [OBS]; symmetric content = `symmetric_schemes/aes256_gcm.rs`, with field validators `wrong nonce length`, `wrong key len`, `wrong tag length`, `wrong extras length` [OBS].
- Private keys are serialized **PKCS#8**: `Converting a fresh private key into PKCS8 should always be possible`, public keys DER: `Converting a fresh public key into DER should always be possible` [OBS]. (NB: `EncryptedPrivateKeyInfo` occurrences in core are **OpenSSL default-provider encoder names** — `dh_to_EncryptedPrivateKeyInfo_der_encode`, `structure=EncryptedPrivateKeyInfo` — not direct evidence of Dropbox using PKCS#8-encrypted key files; this corrects EVIDENCE.md's §8 attribution [OBS].)
- RNG: `encryption/src/random.rs` uses OpenSSL `RAND_bytes`, plus `getrandom`/`rand_core` [OBS].

**EKMS wire endpoints** (apiv2 `/2/ekms/*`, [INF] on `api.dropbox.com`) [OBS paths]: `register_client`, `register_file_key_batch`, `get_file_keys`, `get_namespace_key`, `get_namespace_public_key`, `get_team_public_key`, `get_encrypted_team_key_list_with_client_key`, `get_team_enrollment_status`, `get_pending_clients`, `enroll_clients`. Internal method names: `load_file_key(s)`, `register_client`, `register_file_key(_batch)`, `acknowledge_file_key`, `load_cached_file_key`, `enroll_pending_clients`, `get_next_pending_clients`, `get_team_enrollment_status`, `has_access_to_namespace_key` [OBS].

**Key-hierarchy data structures (recovered field layouts)** [OBS]:
- `EncryptedKeyPair` { `app_id`, `unique_id`, `encrypted_key_data`, `encrypting_key_id`, `encrypted_private_key_data` } — a key pair whose private half (`encrypted_private_key_data`) is wrapped under the key named by `encrypting_key_id` (HPKE) [OBS].
- `PublicKey` (must carry a key id: `Namespace public key from server must contain a key id`) [OBS].
- `EncryptedFileKey` / `EncryptedFileKeys`, `EncryptedKeyPair(s)` returned by responses (`successful GetFileKeysResponse must contain EncryptedKeyPairs`/`EncryptedFileKeys`, `GetNamespaceKeyResponse must contain EncryptedKeyPairs`, `RegisterFileKeyBatchResponse must contain Vec<EncryptedFileKey>`, `RegisterClientKeyResponse must contain PublicKey`) [OBS].
- `PerRevisionKeyInfo` { `encrypted_key_data`, `encryption_extras` } [OBS] — the per-revision file key, wrapped.
- `CiphertextInfo` (the file's top-level descriptor; also `FileCiphertextInfo`/`ReconstructFileCiphertextInfo`) { `crypto_scheme`, `content_encryption_extras`, `key_id`, `per_revision_key_info` } [OBS].
- `EncryptedFile` (PNM body) { `keyid`, `encryption_scheme`, `plaintext_blocklist_encryption_extras`, `encrypted_plaintext_blocklist`, `plaintext_file_size`, `content_encryption_extras`, `per_revision_key_info` } [OBS].
- `Blockwise` { `set_auth_tag`, `block_encryption_extras`, `encrypted_hmac_key`, `hmac_key_encryption_extras` } [OBS] — blockwise content AEAD with a per-file HMAC key that is itself encrypted.
- `blocklist_crypto`: `Blocklist must be a multiple of BLOCK_HASH_SIZE`, errors `AuthenticationFailure`/`UnknownScheme`/`InvalidCryptoExtras` [OBS].

**Key-tree / enrollment model** [INF from above + log strings]: device holds a **client key pair** (`client_key_pair.rs`; persisted and integrity-checked — `serialized_client_key_pair_corrupted`, `is_backup_mode` [OBS]). The client `register_client`s its public key with EKMS; a team admin/other client `enroll_clients` by HPKE-wrapping the **team key** to each pending client's public key (`get_pending_clients` → `enroll_clients`). The **team key** wraps **namespace keys** (`get_namespace_key` returns encrypted key pairs; `Could not decrypt private namespace key`, `Could not find namespace key in get_namespace_key chain!` imply a walk up a key chain [OBS]). A **namespace key** wraps per-file **file keys** (`get_file_keys`, `register_file_key_batch`; `creating a file key for ROOT_FILE_ID is not allowed` [OBS]). A file key derives a **per-revision key** (`PerRevisionKeyInfo`), which with AES-256-GCM + the `Blockwise`/`ContentEncryptionExtras` encrypts file content block-by-block. **Key verification** (`key_verification.rs`, `ensure_team_key_fingerprint`) checks a `team_key_fingerprint` stored in the Nucleus DB against one supplied by the Python app, rejecting non-authenticated schemes (`Detected a key created with a non-authenticated key crypto scheme ... Aborting`) [OBS]. Team-enrollment change notifications arrive over a **Bolt** channel (`team enrollment bolt channel invalidated` [OBS]).
- Error/status vocabulary [OBS]: `TeamKeyNotFound`, `ExpiredNamespaceKey`/`expired namespace key`, `NoGeneratedClientKey`, `MalformedResponse`, `KeyMismatch`, `root_key_id`, `team_key_ids`, `client_key_id`/`client_key_scheme`, `root_key_id_from_server_differs`, `encrypted_team_key_not_found`, `file_key_not_found`, `too_many_keys`.
- Encrypted-folder placement state (Nucleus): folder behavior enum `ENCRYPTED_FOLDER` with flags `encrypt_descendants`, `initially_selsync`, `suppress_selsync`, `suppress_shared_link`, `suppress_ns_partition`, `suppress_mount_notification`; node flags `is_in_encrypted_folder`, `is_encrypted_root`, `is_confidential_folder`, `confidential_mount_fileid`, `should_encrypt`; disk ops `HydrateEncryptedPlaceholder`/`LocalFixupHydrateEncryptedPlaceholder`, conflict reasons `encrypted_folder_conflict`, `cloud_doc_in_encrypted_folder`, `symlink_in_encrypted_folder` [OBS]. Vault/Passwords/Family are folder behaviors `VAULT_FOLDER`/`PASSWORDS_APP`/`FAMILY_SHARED_FOLDER` with lifecycle states `PreSetupLifeVault`/`PostSetupLifeVault`, `passwords_pre_setup`/`_post_setup`, and FSW rule `block_move_shared_folder_to_vault` [OBS]; `Vault.db` is Vault's local DB (schema/PRAGMAs [UNK]).

**CORRECTION:** `coauth` is **co-authoring (Office/WOPI), not the encrypted-folder subsystem** — `coauthoring`, `calculate_coauth_checksum`, `IsCoauthSupportedForUser`, `https://wopi.dropbox.com/wopi/files/oid_`, and `coauth_checksum`/`coauth_checksum_dirty`/`needs_coauth_checksum` node-metadata fields [OBS]. It computes a per-file checksum over the blocklist to coordinate live Office edits and is unrelated to EKMS. EVIDENCE.md §7/§9 conflated `coauth` with the key-exchange system; keep them separate.

### 6. Python `.pyc` encryption posture [OBS/INF/UNK]

- Custom `.pyc` magic **`b7 34 0d 0a`** (stock CPython 3.11 = `a7 0d 0d 0a`) [OBS, verified on `.pyc` headers on disk]. The 4 bytes after magic are `01 00 00 00` → the PEP 552 **hash-based** bit flag set, so the 16-byte header is `magic(4) + flags(4=0x01) + source-hash(8)` rather than `mtime+size` [OBS/INF].
- Bodies (offset 16+) are **high-entropy / encrypted**: a sampled module body uses all 256 byte values with near-uniform frequency [OBS, measured]. 3,628 `.pyc` present [OBS].
- Consequence: both the marshal type-code remap and the body cipher live inside the modified `libpython3.11.so.1.0`, which decrypts at import; **the decryption algorithm/key is [UNK]** from this corpus (recovering it requires lifting the interpreter's import/decrypt routine). Python source is therefore not statically recoverable; the persistence/crypto logic above is authoritative because it lives in the unencrypted (stripped) Rust `libdropbox_core.so`.

### 7. What a reimplementer must model (summary)
1. An AES-keyed `.dbx` page codec (algorithm [UNK]) whose key = keystore `database_key`; a file-based posix keystore holding base64-JSON key material + integrity digest (no OS Secret Service).
2. `config.dbx`/`instance.dbx`: encrypted `instance(id, appdata_path, uid, master, active)` + string-keyed `config(host_int, host_id, account_id, …)`; the host-key credential lives here.
3. `nucleus.sqlite3` (plaintext) with the exact DDL in §3 (versioned `fp_local_tree`, `transplant`, `update_info`, `deleted_files`, `file_block_upload_tokens`, `fs_linux_fileids/xattrs`) + INTEGER-keyed `config`; `index.sqlite` for `lbc_blocks`; `apex.sqlite3` for apex context.
4. PNM (`per_node_metadata` protobuf) as the node-metadata container, including the `EncryptedFile`/`PerRevisionKeyInfo`/`Blockwise`/`ContentEncryptionExtras` crypto attributes, persisted in `fp_local_tree.metadata` and the `user.com.dropbox.attributes` xattr.
5. The EKMS key hierarchy: client-key-pair → (HPKE, sender-auth, DHKEM-P256/HKDF-SHA256/AES-256-GCM) team key → namespace key → file key → per-revision key → AES-256-GCM blockwise content, served over `/2/ekms/*`, with team-key fingerprint verification and Bolt enrollment notifications.---

## 9. Python layer: obfuscation scheme and de-obfuscation

The control plane is Python, shipped only as `.pyc` inside `python-pypkg.zip`
(3,628 modules) and run by a **modified CPython 3.11.14** (`libpython3.11.so.1.0`,
branch `dbx-desktop-v3.11.14`). Four independent protections, in load order:

1. **Custom pyc magic** `b7 34 0d 0a` (stock 3.11 = `a7 0d 0d 0a`). [OBS]
2. **Encrypted marshal payload.** Each `.pyc` is a PEP-552 hash-based header
   (`flags=0x01`, an 8-byte field that is a shared constant across most modules,
   not a per-file source hash) followed by an encrypted marshalled code object.
   Whole-body entropy ≈ 7.9–8.0 bits/byte including stdlib modules, so decryption
   is universal. [OBS] Decryption is wired into their patched
   **`PyMarshal_ReadObjectFromString`**: on their interpreter
   `marshal.loads(body[16:])` returns a live code object; on stock 3.11 the same
   bytes raise `ValueError: bad marshal data`. [OBS] Crypto primitives come from
   the statically-linked OpenSSL 3.5.5 (both AES and ChaCha20 present). The exact
   cipher and key are `[UNK]` — not required for de-obfuscation because the
   client's own interpreter performs the decryption (below). A same-length XOR of
   two equal-size modules does **not** cancel (5/153 zero bytes), ruling out a
   fixed-keystream XOR; the cipher is block- or per-file-keyed. [OBS]
3. **Permuted opcode numbering.** Opcode integers are renumbered by a fixed
   permutation; operand bytes and inline-cache layout are unchanged, and
   `CACHE`(0), `RESUME`(0x97), `STORE_NAME`(0x5a) are fixed points, while e.g.
   their `0x7d`→`LOAD_CONST`, `0x8e`→`LOAD_NAME`, `0x83`→`BINARY_OP`,
   `0x23`→`RETURN_VALUE`, `0x91`→`LOAD_CLASSDEREF`. [OBS] The full 108-opcode
   map was recovered (see below).
4. **Remapped marshal type codes** — not separately cracked; the oracle
   unmarshals for us.

### 9.1 De-obfuscation method (oracle + transcoder)

Build a C harness that embeds the shipped `libpython3.11.so.1.0`
(`Py_InitializeFromConfig` with `module_search_paths = [python-pypkg.zip,
python-pyext]`). Booting the interpreter at all exercises its decryptor (it loads
`encodings`/`codecs` from the encrypted zip). A controlled driver then reads each
module's raw bytes and calls `marshal.loads(body[16:])` — their patched marshal
**decrypts + deserializes without executing the module** — and exports each code
object as a plain tree.

The opcode permutation is recovered by compiling an identical ~170-file corpus on
both their interpreter and stock 3.11, aligning equal-length instruction streams,
and majority-voting `their_byte → opname` (zero conflicts; covers every opcode
used across all 3,628 modules). A host transcoder remaps each `co_code` opcode
byte (every even offset) `their → stock` and re-marshals to a standard 3.11
`.pyc`.

**Result:** all 3,628 modules transcoded to stock `.pyc` with 0 errors, readable
by any stock-3.11 `dis`/decompiler. Validated against ground truth: transcoded
`abc` disassembles correctly and its top-level API matches the genuine
`/usr/lib/python3.11/abc.py` (47/48 name overlap; the 1 diff is 3.11.14↔3.11.17
patch noise). Tooling: `oracle/` (harness + drivers + `opcode_map.json` +
`transcode.py` + README).

### 9.2 Python control plane (now readable) — key findings

With the payloads decrypted, the control-plane vocabulary that was previously
unreadable resolves (counts = occurrences in module string constants): `oauth`
464, `bolt` 828, `subscribe` 217, `host_id` 197, `host_int` 160, `nonce` 222,
`client_api` 294, `hostkey` 89, `access_token` 53, `refresh_token` 24,
`Dropbox-Host-Key` 3. [OBS] Recovered module structure, directly relevant to
session/transport:

- `apex/auth.py` → class **`OAuthClient`**, `retrieve_token_callback`,
  `_RETRIEVE_TOKEN_ID`, `_RETRIEVE_TOKEN_CONTEXTS`, `refresh_token`,
  `access_token` — the OAuth token client above the native `dbxauth` FFI. [OBS]
- `apex/http_client.py` → class **`HttpClient`**, `Response`/`ResponseHead`, and
  typed errors `ReceiverDropped`, `ClientInitiatedReconnect`, `Timeout`,
  `ProtocolError`, `InvalidHost`, plus `_error_from_response_proto`. [OBS]
- `apex/context.py` → the config tree `Config`/`ApexContext` with
  `DatabaseConfig`, `LoggingConfig`, `MetricsConfig`, `AnalyticsConfig`,
  **`StormcrowConfig`**, `AutoUpdaterConfig`, `HostInformation`, `force_http1`. [OBS]
- `apex/dbxconn.py` → class **`Connection`**. [OBS]

This confirms, at the Python level, that both the host-key and the OAuth
(`refresh_token`/`access_token`) credentials are managed here, and that the
device-link / `host_int` orchestration the native layer did not expose is in
these (now-readable) modules — recoverable as a follow-on by disassembling the
linking modules (`dropbox/client/**`, `apex/auth.py`, `dbxauth`).

---
---

## 10. Consolidated open questions (what a rebuild still needs to pin)

**Transport / wire**
- Exact HTTP/2 SETTINGS values Dropbox sends (initial window, max frame, max
  concurrent streams) — only the h2 parameter names are observed.
- DFC in-process frame header byte layout (length/flag/correlation-id) beyond
  "gRPC-over-framed-channel"; UDS handshake version and framing.
- gRPC max message size; whether gRPC-level message compression is ever
  negotiated (only identity/flag-0 evidenced); TLS cert-pinning policy
  (`disable-static-cert-pinning` flag exists; no pin literals found).
- Full `.proto` field numbers/layouts for `nsf.Nsf`, `fs_api.FsApi`,
  `dropbox_meta_engine.SyncEngineApi`, Bolt `SubscribeToBolt` — not in strings.

**Session / auth**
- `host_int` minting/derivation and the full device-registration/link handshake
  (now in the decrypted Python, not yet lifted).
- Per-request rule selecting `Dropbox-Host-Key` vs OAuth `Bearer`.
- OAuth client-authentication method at `/oauth2/token` (no client_id/secret
  literals at the token call).
- Exact value bound to `X-Dropbox-UID` (instance uid vs account_id); whether
  `machine_id` derives from `/etc/machine-id` vs `/var/lib/dbus/machine-id`.

**Endpoints**
- Resolved hostnames for `nsfserver` / `apiv2blockserver` (runtime-resolved);
  production block-server host (only `blockexcserver=dl-debug.dropbox.com`
  exception host observed). No literal port (443 inferred); no scheme field.

**Sync / blocks**
- Protobuf field numbers for `CommitRequest`, `ConsistentCutListPage`,
  `HlcLinearizedPage`, `SignedConsistentCutCursor`; HLC bit layout and the
  signature scheme over the cursor.
- Content block size (4 MiB is `[INF]`; a 1 MiB literal exists, 64 KiB rsync
  threshold observed); `block_hash` digest length (32 `[INF]`); exact rsync
  weak+strong hash algorithms; block-source try-order.

**Notifications**
- Bolt request Content-Type / GrpcV2 framing bytes; which header carries the
  Bolt bearer token; long-poll timeout and port; 3- vs 5-field
  `BoltChannelToken`; single multiplexed connection vs `use_separate_bolt`.

**Persistence / crypto**
- `.dbx` page-codec algorithm (cipher mode, reserve bytes, IV, per-page MAC) —
  compiled C, no SQLCipher pragmas; `database_key`/`user_key` derivation and the
  posix keystore file path/format/KDF/digest.
- Encrypted-folder/Vault: HPKE info/AAD, AES-256-GCM nonce derivation, how
  per-revision keys bind to block indices; where the client key pair / team-key
  fingerprint are persisted.
- The `.pyc` body **cipher and key** inside `libpython3.11.so.1.0` (a Ghidra
  pass on the patched marshal timed out; the oracle made it unnecessary for
  de-obfuscation but the primitive identity remains `[UNK]`).

## 11. Minimal rebuild checklist (interoperable client, own account/data)

1. TLS (OpenSSL/BoringSSL-class) + HTTP/2 client; gRPC framing
   `application/grpc+proto`, `grpc-status`/`grpc-message` trailers.
2. Account auth: obtain OAuth tokens and/or a host key; send `Dropbox-Host-Key`
   + `X-Dropbox-UID` (sync gRPC) or `Authorization: Bearer` (apiv2) with the
   `X-Dropbox-*` request headers (§5).
3. Server map (§6): dial `client.dropbox.com` (metaserver) for the sync gRPC
   services; `bolt.dropbox.com` for notifications; block servers via the routing
   tier; `api.dropbox.com` for apiv2.
4. Per-namespace sync loop (§9 of the sync section): subscribe (Bolt) → list
   (cursor delta) → commit/commit_ack, maintaining the Canopy tree + mount table.
5. Block layer (§block): content-hash files into blocks, `nsf.Nsf`
   `GetBlock/PutBlock` (+rsync `GetBlockSignature`/`*RsyncBlock`), blocklists,
   batched commit, local block cache.
6. Local state: SQLite (`nucleus.sqlite3`, `config.dbx`, …); the `.dbx` codec is
   the main unknown to replace or reimplement.

*End of specification. Sections 1–8 were authored by a parallel analysis fan-out
and independently verified; §9–11 and the corrections in the header were added
from the Python de-obfuscation and the verification pass.*
