## Block Storage & Transfer — rebuild spec

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

[INF] (1) Split file into uniform blocks (≤4 MiB [INF]); (2) hash each block with SHA-256 (`BlockHash::from_data`) → `block_hash` (raw 32-byte BLOB); the ordered list is the blocklist; (3) the file content_hash/checksum is a digest over that blocklist; (4) for each block not already proven present (no cached upload token, not found locally/at a peer): Brotli-compress and `PutBlock` (or, for an edited large block with a parent, `GetBlockSignature`→compute delta→`PutRsyncBlock`), receiving an upload token cached in `file_block_upload_tokens`; (5) commit the blocklist + metadata via `sync_frontend.Meta/CommitAtHead`, batched under size caps, presenting cached tokens; (6) on download, `block_finder` resolves each needed block from local disk / `local_block_cache` / peer / `nsf.Nsf/GetBlock` (or `GetRsyncBlock` patch), decompresses per `requested_block_format`, verifies the hash, caches it in `lbc_blocks`, and `fs_api.FsApi/mergeFromDropbox` materializes the file.