# Source Generated with Decompyle++
# File: nucleus_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from abc import ABC, abstractmethod
from typing import Callable, Collection, ContextManager, Dict, Iterable, List, Optional, Text, Tuple, Union
from dropbox.client.authentication.account import Account
from dropbox.foundation.futures import Future
from dropbox.infinite.pager import PageRequest
from dropbox.model.types import FileId, NsId
from dropbox.proto.nucleus.app_service_pb2 import FPCutoverDryRunExtraData, StartFPCutoverDryRunReply, StartFPCutoverReply, UpdateConfigReply, UpdateConfigReq
from dropbox.proto.nucleus.common_api_types_pb2 import LookupSyncIconReply
from dropbox.proto.nucleus.network_state_pb2 import NetworkState
from dropbox.proto.nucleus.published_event_pb2 import EncryptionErrorEvent, FPShadowCutoverCompleted
from dropbox.proto.nucleus.reactive_api_pb2 import MovedToTrash, MovedToTrashSummary
from dropbox.proto.nucleus.sync_failures_pb2 import GetSyncFailuresSummaryReq
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath, ServerPath
from dropbox.sync_engine_boundary.device_anchor_interface import SyncEngineDeviceAnchorInterface
from dropbox.sync_engine_boundary.device_folder_interface import SyncEngineDeviceFolderInterface
from dropbox.sync_engine_boundary.file_locking.file_locking_sync_interface import SyncEngineFileLockingInterface
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
from dropbox.sync_engine_boundary.infinite.infinite_interface import NucleusInfiniteInterface
from dropbox.sync_engine_boundary.infinite.recall_events import InfiniteRecallEvent
from dropbox.sync_engine_boundary.link_container_interface import SyncEngineLinkContainerInterface
from dropbox.sync_engine_boundary.nucleus_p2p import P2PMetaDownloader
from dropbox.sync_engine_boundary.nucleus_selective_sync_inteface import NucleusSelectiveSyncInterface
from dropbox.sync_engine_boundary.selective_sync_by_path_interface import SelectiveSyncByPathInterface
from dropbox.sync_engine_boundary.sync_engine_file_props_client_interface import SyncEngineFilePropsClientInterface
from dropbox.sync_engine_boundary.transfer_status import TransferStatusSnapshot
from dropbox.sync_engine_boundary.types import AdditionalAttributes, CallbackRemovalToken, ConflictResolutionAttempt, DropboxFolderDiskInfo, FilesystemInfo, FileTypeFilter, MountChangeOperation, MoveToDeletedCache, TypedDirectoryEntry
from dropbox.sync_engine_boundary.types.debug_info import DebugInfo
from dropbox.sync_engine_boundary.types.engine_waits import ActiveEngineWaits
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.sync_engine_boundary.types.sync_engine_status import SyncEngineStatus
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailuresSummary, SyncOpFailed
from dropbox.sync_engine_boundary.types.sync_icon import SyncIcon
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress, SyncProgressForFile
from dropbox.sync_engine_boundary.types.sync_queue import SyncPriority, SyncQueueSnapshot
MYPY = False
if MYPY:
    from dropbox.sync_engine_boundary.file_locking.file_locking_interface import FileLockingInterface
    from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus

class SyncEngineBasicInterface(ABC):
    account = (lambda self = None: raise NotImplementedError())()()
    file_system = (lambda self = None: raise NotImplementedError())()()
    get_main_root_ns = (lambda self = None: raise NotImplementedError())()
    version = (lambda self = None: raise NotImplementedError())()
    is_file_provider = (lambda self = None: raise NotImplementedError())()


class NucleusInterface(ABC, SyncEngineBasicInterface, NucleusInfiniteInterface, NucleusSelectiveSyncInterface, SyncEngineFilePropsClientInterface, SyncEngineDeviceFolderInterface, SyncEngineDeviceAnchorInterface, SyncEngineFileLockingInterface, SyncEngineLinkContainerInterface):
    file_locking_interface = (lambda self = None: raise NotImplementedError())()
    begin_dropbox_move = (lambda self = None: raise NotImplementedError())()
    contains_mount_points = (lambda self = None, fileid = None: raise NotImplementedError())()
    debug_sfj_consistency_checker = (lambda self = None: raise NotImplementedError())()
    debug_dbx_ignore_consistency_check = (lambda self = None: raise NotImplementedError())()
    selsync_manager = (lambda self = None: raise NotImplementedError())()
    get_bugreporter_stats = (lambda self = None: raise NotImplementedError())()
    get_conflicted_path = (lambda self = None, old_local_path = None, new_base = abstractmethod, reason = (None,), dirname = ('old_local_path', 'LocalPath', 'new_base', 'Text', 'reason', 'Text', 'dirname', 'Optional[Text]', 'return', 'Future[LocalPath]'): raise NotImplementedError())()
    get_dropbox_folder_disk_info = (lambda self = None: raise NotImplementedError())()
    get_download_status_snapshot = (lambda self = None: raise NotImplementedError())()
    get_upload_status_snapshot = (lambda self = None: raise NotImplementedError())()
    get_hash_status_snapshot = (lambda self = None: raise NotImplementedError())()
    get_percent_complete = (lambda self = None: raise NotImplementedError())()
    get_metrics = (lambda self = None: raise NotImplementedError())()
    get_namespace_properties = (lambda self = None: raise NotImplementedError())()
    get_sync_failures_summary = (lambda self = None, sample_limit = None, category = abstractmethod: raise NotImplementedError())()
    get_remote_mount_points = (lambda self = None, include_hidden = None: raise NotImplementedError())()
    get_sync_progress = (lambda self = None: raise NotImplementedError())()
    get_sync_engine_status = (lambda self = None: raise NotImplementedError())()
    get_sync_status = (lambda self = None, fileid = None: raise NotImplementedError())()
    get_sync_status_by_path = (lambda self = None, local_path = None: raise NotImplementedError())()
    get_active_engine_waits = (lambda self = None: raise NotImplementedError())()
    get_debug_info = (lambda self = None: raise NotImplementedError())()
    unpack_fp_package = (lambda self = None, path = None: raise NotImplementedError())()
    get_tag = (lambda self = None, fileid = None: raise NotImplementedError())()
    list_dir_by_file_type = (lambda self = None, dir_path = None, file_type_filter = abstractmethod: raise NotImplementedError())()
    lookup_mount_point = (lambda self = None, namespace = None: pass)()
    lookup_sync_icon = (lambda self = None, path = None, on_changed = abstractmethod: raise NotImplementedError())()
    get_temp_dir_on_dropbox_volume = (lambda self = None: raise NotImplementedError())()
    on_sync_progress = (lambda self = None, callback = None: raise NotImplementedError())()
    on_queue_changed = (lambda self = None, callback = None: raise NotImplementedError())()
    on_sync_failed = (lambda self = None, callback = None: raise NotImplementedError())()
    on_sync_progress_changed_by_fileid = (lambda self = None, fileid = None, callback = abstractmethod, subscriber_id = ('fileid', 'FileId', 'callback', 'Callable[[SyncProgressForFile], None]', 'subscriber_id', 'str', 'return', 'CallbackRemovalToken'): raise NotImplementedError())()
    on_sync_completed_summary = (lambda self = None, callback = None: raise NotImplementedError())()
    on_remote_update = (lambda self = None, callback = None: raise NotImplementedError())()
    on_hidden_set_changed = (lambda self = None, callback = None: raise NotImplementedError())()
    on_pause_resume = (lambda self = None, callback = None: raise NotImplementedError())()
    on_mount_changed = (lambda self = None, callback = None: raise NotImplementedError())()
    on_encryption_error_event = (lambda self = None, callback = None: raise NotImplementedError())()
    on_client_key_enrolled = (lambda self = None, callback = None: raise NotImplementedError())()
    on_new_team_key_fingerprint = (lambda self = None, callback = None: raise NotImplementedError())()
    on_conflict_resolution_attempt = (lambda self = None, callback = None: raise NotImplementedError())()
    on_applied_hidden_default = (lambda self = None, callback = None: raise NotImplementedError())()
    on_paths_sync_status_changed = (lambda self = None, callback = None: raise NotImplementedError())()
    on_moved_to_trash = (lambda self = None, callback = None: raise NotImplementedError())()
    on_moved_to_trash_summary = (lambda self = None, callback = None: raise NotImplementedError())()
    on_network_state_changed = (lambda self = None, callback = None: raise NotImplementedError())()
    on_sync_engine_status = (lambda self = None, callback = None: raise NotImplementedError())()
    pause_engine = (lambda self = None: raise NotImplementedError())()
    prepare_for_fp_migration = (lambda self = None: raise NotImplementedError())()
    check_fp_eligibility = (lambda self = None: raise NotImplementedError())()
    estimate_fp_migration_duration = (lambda self = None: raise NotImplementedError())()
    notify_shadow_domain_created = (lambda self = None, shadow_to_mounted_socket_path = None, mounted_to_shadow_socket_path = abstractmethod: raise NotImplementedError())()
    notify_shadow_domain_deleted = (lambda self = None: raise NotImplementedError())()
    start_shadow_migration_cutover = (lambda self, shadow_domain_location = None, new_dropbox_path = None, dfc_location = abstractmethod, dfc_database_location = ('shadow_domain_location', 'str', 'new_dropbox_path', 'str', 'dfc_location', 'str', 'dfc_database_location', 'str', 'return', 'Future[StartFPCutoverReply]'): raise NotImplementedError())()
    start_shadow_migration_cutover_dryrun = (lambda self = None, shadow_domain_location = None, extra_data = abstractmethod: raise NotImplementedError())()
    fp_cutover_go_no_go = (lambda self = None, go = None: raise NotImplementedError())()
    on_fp_shadow_cutover_completed = (lambda self = None, callback = None: raise NotImplementedError())()
    ping_sync_frontend = (lambda self = None: raise NotImplementedError())()
    record_upcoming_folder_delete = (lambda self = None, local_path = None: raise NotImplementedError())()
    remove_on_applied_hidden_default_callback = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_sync_progress_callback = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_queue_changed_callback = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_sync_failed_callback = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_sync_progress_changed_by_fileid = (lambda self = None, fileid = None, subscriber_id = abstractmethod: raise NotImplementedError())()
    remove_on_sync_completed_summary_callback = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_remote_update = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_mount_changed_callback = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_conflict_resolution_attempt_callback = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_hidden_set_changed_callback = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_pause_resume = (lambda self = None, token = None: raise NotImplementedError())()
    remove_on_paths_sync_status_changed = (lambda self = None, token = None: raise NotImplementedError())()
    register_tag_for_camera_uploads = (lambda self = None, rr_server_path = None: raise NotImplementedError())()
    rr_server_to_fileid = (lambda self = None, rr_server_path = None: raise NotImplementedError())()
    mr_server_to_fileid = (lambda self = None, mr_server_path = None: raise NotImplementedError())()
    rr_local_to_probable_local_path = (lambda self = None, rr_server_path = None: raise NotImplementedError())()
    rename_into_dropbox = (lambda self = None, src_local_path = None, dst_rr_server_path = abstractmethod, additional_attributes = (None,): raise NotImplementedError())()
    queue_resync = (lambda self = None: raise NotImplementedError())()
    set_path_ignored_state = (lambda self = None, path = None, ignore_state = abstractmethod: raise NotImplementedError())()
    trigger_list = (lambda self = None: raise NotImplementedError())()
    trigger_reconstruct = (lambda self = None, server_path = None: raise NotImplementedError())()
    resync_file = (lambda self = None, local_path = None: raise NotImplementedError())()
    unpause_engine = (lambda self = None: raise NotImplementedError())()
    update_account_properties = (lambda self = None: raise NotImplementedError())()
    update_priority_hint_by_fileid = (lambda self = None, fileid = None, priority = abstractmethod: raise NotImplementedError())()
    infinite_on_recall_event = (lambda self = None, callback = None: raise NotImplementedError())()
    is_monitored_by_path = (lambda self = None, local_path = None: raise NotImplementedError())()
    is_ready = (lambda self = None: raise NotImplementedError())()
    is_in_read_only_namespace_by_path = (lambda self = None, local_path = None: raise NotImplementedError())()
    filesystem_info = (lambda self = None, path = None: raise NotImplementedError())()
    get_p2p_meta_downloader = (lambda self = None: raise NotImplementedError())()
    retry_over_quota_commits = (lambda self = None: pass)()
    infinite_is_entry_evicted = (lambda self = None, fileid = None: raise NotImplementedError())()
    infinite_handle_page_request = (lambda self = None, request = None: raise NotImplementedError())()
    get_infinite_placeholder_count = (lambda self = None: raise NotImplementedError())()
    test_only_echo = (lambda self = None, message = None, echo_back = abstractmethod: pass)()
    induce_nucleus_oom = (lambda self = None: raise NotImplementedError())()
    induce_nucleus_panic = (lambda self = None: raise NotImplementedError())()
    induce_nucleus_remote_inconsistencies = (lambda self = None: raise NotImplementedError())()
    deprecated_on_move_to_deleted_cache = (lambda self = None, callback = None: raise NotImplementedError())()
    deprecated_remove_on_move_to_deleted_cache_callback = (lambda self = None, callback = None: raise NotImplementedError())()
    update_config = (lambda self = None, request = None: raise NotImplementedError())()

