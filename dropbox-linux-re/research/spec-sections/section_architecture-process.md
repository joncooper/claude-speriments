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
  DFC poll. [UNK]