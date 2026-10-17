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
6. LAN block sync is a separate self-signed-TLS peer channel (`*ForPeer`/`*FromPeer`), not in the host map.