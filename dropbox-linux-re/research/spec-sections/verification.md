# Verification report

## architecture-process — verdict: solid (checked 54, confirmed 54)
  gap: Exact byte layout of a DFC frame/event (header fields, correlation IDs) beyond the proto messages TransportEventRequest/ResponseTransportEvent carried over a queue.
  gap: Concrete role of the main_utility() process (updater host vs crash reporter vs camera-upload worker) - only its entry point and the Utility bootstrap command are observable.
  gap: Whether main() vs linux_event_loop() map 1:1 onto the NativeEventLoop vs ElectronLibrary runloop_type, or are chosen independently.
  gap: The UDS wire version number and the exact handshake message framing.
  gap: Argument order/signature of sync_engine_create and fs_api_create beyond the observed apex_context/account/create_args identifiers.
  gap: Thread/runtime model: number of tokio runtimes and GIL-release discipline around poll_fp_dfc.
  gap: Whether apex_context_get_channel_id is the key used to route DFC RPCs to the right account connection (inferred, not proven).

## transport-wire — verdict: minor-fixes (checked 55, confirmed 54)
- [overreach-inf-as-obs] 37. server-driven throttling factor bounded <=1.0 (TOKEN: MINIMUM_THROTTLING_FACTOR_VALUE)
    → Keep the observable part: throttling_factor is asserted to lie in [MINIMUM_THROTTLING_FACTOR_VALUE, 1.0] (bounded <=1.0). Drop or re-tag `server-driven` as [INF]/unverified unless a separate token shows the factor originates from a server r
  gap: Exact numeric HTTP/2 SETTINGS values (initial_window_size, max_frame_size, max_concurrent_streams) Dropbox sends are not in strings — only the h2 parameter names are observable; defaults vs hyper's ar
  gap: Whether gRPC-level message compression (grpc-encoding gzip/br) is ever negotiated — only identity/flag-0 is evidenced; brotli in the corpus belongs to block/content compression and HTTP content-encodi
  gap: Per-request binding rule between Dropbox-Host-Key (sync gRPC path) and OAuth Bearer (apiv2 REST path) — which services use which credential is INF, not fully pinned.
  gap: Full .proto field layouts (message/field numbers) for nsf.Nsf, nucleus.NucleusAPI, fs_api.FsApi, SubscribeToBolt — not recoverable from the string corpus.
  gap: DFC frame header byte layout (beyond 'gRPC-over-framed-channel') is not spelled out in strings; the length/flag layout for the in-process channel is inferred from gRPC framing conventions.
  gap: Exact gRPC max message size and any TLS certificate pinning policy are not evidenced (no pin strings found).
  gap: The precise ordering/casing of X-Dropbox-* headers as serialized on the wire is inferred from concatenated constant tables, not from an ordered header-list dump.

## session-auth — verdict: minor-fixes (checked 54, confirmed 52)
- [overreach-inf-as-obs] Sync-frontend gRPC method names carried over the authenticated connection include bolt_subscribe and ping_sfe (claim 53, [OBS])
    → Keep bolt_subscribe (+upload_block/commit_at_head/download_block) as [OBS] method names. Downgrade ping_sfe to [INF] or drop it, noting it is a real string but in a different blob adjacent to get_file_information... and a Read/Write permiss
- [overreach-inf-as-obs] The single Dropbox-facing HTTP client is apiv2_client/client.rs and sets Authorization to either Dropbox-Host-Key or Bearer on POST application/json (claim 1, [
    → Mark 'single' as [INF] (e.g. 'the primary APIv2 HTTP client'). The per-request shape (POST, application/json, one Authorization header = Dropbox-Host-Key <val> or Bearer <val>) stays [OBS].
  gap: Exact host_int minting/derivation and the full device-registration/linking handshake are not present in the native strings; RegisterClient is EKMS encrypted-folder enrollment, not device registration.
  gap: OAuth client-authentication method at /oauth2/token is undetermined: no client_id/client_secret literals appear at the token call, and the only Basic auth strings are in analytics (ssa_connection.rs) 
  gap: The rule that selects Authorization: Dropbox-Host-Key vs Bearer per request/account/endpoint is not determinable statically.
  gap: config.dbx/instance.dbx codec algorithm, the keystore digest algorithm, and how database_key/user_key/master are derived or wrapped are not recoverable from strings.
  gap: No OS-keyring backend strings (libsecret/secret_service/gnome-keyring/kwallet/dbus SecretService) exist in core or tprt, contradicting EVIDENCE.md's 'libsecret/keyring' claim; the observed posix keyst
  gap: Exact value bound to X-Dropbox-UID (numeric uid from the instance row vs account_id) is inferred, not proven; uid and aid are known to be distinct.
  gap: Whether machine_id is actually derived from /etc/machine-id or /var/lib/dbus/machine-id is inferred from adjacent strings only, not proven.
  gap: Python source (apex/auth.pyc etc.) is encrypted, so the orchestration above the native FFI (which calls oauth_register_refresh_token/dbxauth_retrieve_accounts) could not be read.

## endpoints-topology — verdict: minor-fixes (checked 27, confirmed 26)
- [overreach-inf-as-obs] The server map is persisted into/seeded from the Apex config database (token 'recreated the Apex databaseDROPBOX_HOST'), tagged [OBS].
    → Downgrade from [OBS] to [INF]. What is genuinely observed: an Apex config DB exists (apex.sqlite3 appears 2x, config.dbx 1x) and a recovery log string 'recreated the Apex database' exists. That the DROPBOX_HOST map itself is persisted into 
  gap: Resolved hostnames for logical server names nsfserver and apiv2blockserver are not present as literals in the static corpus (likely resolved at runtime from config/metaserver bootstrap, or aliased to 
  gap: No literal port number (e.g. 443) appears in either binary; the 443/https default is inferred from the config schema's host.port field plus the one observed https:// WOPI URL. Actual configured ports 
  gap: No scheme field exists in the server config schema (only host_name and port), so whether any logical server is ever addressed over plain HTTP vs HTTPS is not determinable statically; all evidence poin
  gap: The precise roles of legacy hosts t8.dropbox.com and d6.dropbox.com are not pinned down by surrounding strings (historically notification/command edge hosts), only that they are map entries.
  gap: The exact binding of which logical server the subscribe/list/commit namespace sync protocol dials (assumed metaserver=client.dropbox.com) is inferred, not shown by a direct name→protocol literal.
  gap: Whether boltserver and the WOPI/apiv2 hosts are reached directly or via a connection proxy/throttled connector layer is not resolved here (transport-layer dimension).
  gap: The on-disk ordering and any additional (non-default/overlay) server-map entries beyond the base literal were not recovered; only the baseDROPBOX_HOST default set is observed.

## sync-protocol — verdict: minor-fixes (checked 46, confirmed 46)
- [misread] Mount bookkeeping invariant quoted as mounted_nses.is_subset(&known_nses) [OBS] (section 2, head bullet)
    → Quote the real invariants: mounted_nses.is_subset(&fileid_nses), mounted_nses.is_subset(&mountable_nses), and separately fileid_nses.is_subset(&known_nses).
- [misread] PNM variant 'EncryptedFilePNM' listed [OBS] (section 2, PNM bullet)
    → List the observed forms EncryptedFileFilePNM / EncryptedFileDirectoryPNM rather than a non-existent EncryptedFilePNM.
- [not-found] PNM variant 'DeviceInfoPNM' listed [OBS] (section 2, PNM bullet)
    → Drop DeviceInfoPNM as a PNM variant, or re-label it as the adjacent DeviceInfo/DeviceInfoEntity token.
- [misread] Quoted constraint 'Updating mount_table multiple times in a single CanopyWriteBatch is unexpected' [OBS] (section 3)
    → Trim the quote to the literal substring that exists, or mark the ' is unexpected' gloss as paraphrase.
- [overreach-inf-as-obs] Claim 13: 'Server returns a list of needed block hashes for upload' (TOKEN NeedBlocks{blocks: [)
    → State the observed part ('NeedBlocks carries a blocks list') as [OBS] and tag the 'block hashes / for upload' reading as [INF]. Minor.
  gap: Exact protobuf field numbers / wire tag layout for CommitRequest, ConsistentCutListPage, HlcLinearizedPage, and SignedConsistentCutCursor are not recoverable from the string table (only field names ob
  gap: HLC encoding details (physical timestamp vs logical counter bit widths) and the cryptographic signature scheme over SignedConsistentCutCursor are undetermined.
  gap: Whether GetInitialCursor / GetNamespaceInfo returns all namespaces at once or one per ns, and the exact first-link ordering, is not determinable from strings.
  gap: Bolt long-poll wire framing and the precise mapping from has_delta channels to ns_ids is not recoverable (only the client-side token struct and run-loop logs are observed).
  gap: Content block size constant is unconfirmed: SHA256 is the dominant hash token (167 hits) but no 4194304/4 MiB literal was found; a single 1048576 (1 MiB) literal appears without clear block-boundary c
  gap: Distinction between when LinearizedList vs ConsistentCutList is used at runtime (both methods and both page types exist; the selection policy is not in the strings).

## block-storage — verdict: minor-fixes (checked 72, confirmed 71)
- [misread] #51 LBC re-hash verification and kill switch — TOKEN: local_block_cache/hash_verify_failedlocal_block_cache/kill_switch_off
    → Both metric strings genuinely exist in str_libdropbox_core.so.txt as separate entries (local_block_cache/hash_verify_failed and local_block_cache/kill_switch_off), so the CLAIM's substance (LBC has re-hash-verify and kill-switch metrics) ho
  gap: Primary block size constant not found as a literal string (e.g. 4194304/4 MiB); the 4 MiB figure is [INF] from Dropbox's public content-hash spec, not observed. Only the 64 KiB rsync-delta minimum thr
  gap: block_hash digest length (32 bytes) is [INF] from SHA-256; the corpus stores it as an opaque BLOB and no explicit length literal was found.
  gap: The exact rsync signature algorithm (weak rolling checksum type + strong hash) is [INF] from classic rsync/librsync behavior; no librsync crate or algorithm constant (e.g. adler/MD4) was observed in t
  gap: GetBlock/PutBlock protobuf request field layout (offsets, format selector, namespace/path-root binding) is not recoverable from strings; only reply type names and error fields were observed.
  gap: The precise block-source try-order could not be confirmed from a definitive ordering string; the enum run order (NetworkFetcher, LocalBlockCache, P2PBlockSource, InstantFiles, DownloadManager) is [OBS
  gap: Whether InstantFiles uses the same nsf.Nsf GetBlock/PutBlock or a distinct fast-path endpoint is unresolved; only the crate (instant_files download/upload) and a block-source variant name were observe
  gap: Upload-token (token BLOB) contents/format and server-side validation semantics are opaque; only the cache schema and lifecycle were observed.
  gap: On-disk LBC store file layout (directory structure, per-block filenames, sharding) is [INF]; store.rs references put/read but no path template string was recovered.
  gap: The commit_batch concrete size-limit numeric thresholds (max proto_size, max blocks, max total_bytes) were not found as literals.
  gap: Exact production block-server hostname is [UNK]; only blockexcserver=dl-debug.dropbox.com (exception host) and the BLOCK_SERVER routing tier are observed, with production host selected via the server 

## notifications-bolt — verdict: minor-fixes (checked 32, confirmed 31)
- [overreach-inf-as-obs] Logical server boltserver maps to bolt.dropbox.com in the embedded DROPBOX_HOST map (section 2, presented under an [OBS] heading with an arrow as if read direct
    → Tag the mapping [INF] (or [OBS tokens / INF mapping]): observed = the logical name 'boltserver' and the host 'bolt.dropbox.com' both exist in the DROPBOX_HOST string region; inferred (strongly, as the only bolt-named host) = boltserver reso
  gap: Exact GrpcV2 framing bytes and the Content-Type header value used for the Bolt request were not recovered (only the header name 'Content-Type' is present).
  gap: The precise header carrying the OAuth bearer token for Bolt (e.g. Authorization) is not observable from strings; only [OAuth] retrieval log lines are present.
  gap: Full field membership of the 3-element vs 5-element BoltChannelToken variants could not be disambiguated; only the pooled field names channel_id/token/channel_states (+rev/deprecated_revision in an ad
  gap: The server-side long-poll timeout value and the boltserver port are unknown; only client-side 'Bolt request timed out' and bolt_migration/reconnect_interval_ms exist.
  gap: Whether Bolt ever falls back to the classic Dropbox-Host-Key auth (instead of OAuth) is undetermined.
  gap: The exact serialization/meaning of the opaque 'token' field and how it derives from the namespace list cursor is not determined from static strings.
  gap: Could not confirm from strings whether a single Bolt connection multiplexes all app_ids or whether 'use_separate_bolt' opens a dedicated connection per app; only the flag name is observed.

## persistence-crypto — verdict: solid (checked 40, confirmed 40)
  gap: Exact .dbx page-codec algorithm (cipher mode, page/reserve-byte layout, IV derivation, per-page MAC) is undetermined: no SQLCipher pragmas or codec symbol names in strings; codec is compiled C inside 
  gap: database_key / user_key derivation and the posix keystore file path/format: only base64+JSON+digest behavior is observed; no filename, no KDF, no digest algorithm.
  gap: Whether nucleus.sqlite3 / apex.sqlite3 are plaintext or encrypted is inferred from the .sqlite3 (vs .dbx) naming, not proven; no codec attach observed for them specifically.
  gap: Vault.db schema, tables, and PRAGMAs are unknown beyond the filename and .dbx-vault/.dbx-passwords/.dbx-backup folder markers.
  gap: HPKE info/AAD strings, the exact AES-256-GCM nonce derivation for content blocks, and how per-revision keys bind to block indices are not recoverable from strings.
  gap: Where the serialized client key pair and team-key fingerprint are persisted on disk (which DB/table) is not pinned down; only that corruption/fingerprint-mismatch events exist.
  gap: The .pyc body cipher and marshal/opcode remap live in the modified libpython3.11.so.1.0 and were not lifted; algorithm and key are unknown (a REA pseudo-code attempt on libpython timed out, per corpus
  gap: Ambiguous filename: the dbxignore default-rule string yields 'filehistorytoolkit.dbx' vs EVIDENCE's 'binfilehistorytoolkit.dbx' (the 'bin' is the tail of $RECYCLE.BIN); exact spelling unconfirmed.
