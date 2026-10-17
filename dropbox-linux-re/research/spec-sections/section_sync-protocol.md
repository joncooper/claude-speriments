## Nucleus Sync Protocol — Rebuild Specification

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
  the classic 4 MiB block boundary is not confirmed by a numeric literal).