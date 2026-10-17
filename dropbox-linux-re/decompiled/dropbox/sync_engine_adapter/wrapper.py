# Source Generated with Decompyle++
# File: wrapper.pyc (Python 3.11)

from typing import Any, Dict
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.sync_engine_interface import SyncEngineClassicInterface
from dropbox.threading import Lock
MYPY = False
if MYPY:
    Parent = SyncEngineClassicInterface
    NucleusParent = NucleusInterface
else:
    Parent = object
    NucleusParent = object

class _StubNucleusWrapper(SyncEngineClassicInterface, NucleusInterface):
    
    def _service_not_available_future(self = None, *_args, **_kwargs):
        return FailedFuture.create(ServiceNotAvailableException())

    
    def _service_not_available(self = None, *_args, **_kwargs):
        raise ServiceNotAvailableException

    allow_user_access = _service_not_available_future
    begin_dropbox_move = _service_not_available_future
    bind_into_dropbox = _service_not_available_future
    break_backup_by_fileid = _service_not_available_future
    break_backup_by_target_path = _service_not_available_future
    change_fileid_hidden_set = _service_not_available_future
    check_fp_eligibility = _service_not_available_future
    container_state = _service_not_available_future
    contains_mount_points = _service_not_available_future
    create_breadcrumbs = _service_not_available_future
    create_device_anchor = _service_not_available_future
    debug_dbx_ignore_consistency_check = _service_not_available_future
    debug_sfj_consistency_checker = _service_not_available_future
    delete_device_anchor = _service_not_available_future
    dematerialize_container = _service_not_available_future
    deny_user_access = _service_not_available_future
    dirty_paths = _service_not_available_future
    estimate_fp_migration_duration = _service_not_available_future
    filesystem_info = _service_not_available_future
    fp_cutover_go_no_go = _service_not_available_future
    get_active_engine_waits = _service_not_available_future
    get_bugreporter_stats = _service_not_available_future
    get_conflicted_path = _service_not_available_future
    get_current_computer_backup_progress = _service_not_available_future
    get_current_device_anchor_progress = _service_not_available_future
    get_dbx_ignore_contents = _service_not_available_future
    get_debug_info = _service_not_available_future
    get_device_anchor_metadata_by_path = _service_not_available_future
    get_dropbox_folder_disk_info = _service_not_available_future
    get_fileid_hidden_set = _service_not_available_future
    get_infinite_placeholder_count = _service_not_available_future
    get_metrics = _service_not_available_future
    get_namespace_properties = _service_not_available_future
    get_os_folder_path = _service_not_available_future
    get_remote_mount_points = _service_not_available_future
    get_sync_engine_status = _service_not_available_future
    get_sync_failures_summary = _service_not_available_future
    get_sync_progress = _service_not_available_future
    get_sync_status = _service_not_available_future
    get_sync_status_by_path = _service_not_available_future
    get_tag = _service_not_available_future
    get_temp_dir_on_dropbox_volume = _service_not_available_future
    hidden_set_add = _service_not_available_future
    hidden_set_remove = _service_not_available_future
    induce_nucleus_oom = _service_not_available_future
    induce_nucleus_panic = _service_not_available_future
    induce_nucleus_remote_inconsistencies = _service_not_available_future
    infinite_cancel_batch = _service_not_available_future
    infinite_cancel_page_request = _service_not_available_future
    infinite_ensure_recalled = _service_not_available_future
    infinite_evict_batch = _service_not_available_future
    infinite_handle_page_request = _service_not_available_future
    infinite_is_entry_evicted = _service_not_available_future
    infinite_recall_batch = _service_not_available_future
    is_in_read_only_namespace_by_path = _service_not_available_future
    is_monitored_by_path = _service_not_available_future
    list_containers = _service_not_available_future
    list_device_anchors = _service_not_available_future
    list_dir_by_file_type = _service_not_available_future
    lookup_local_path_properties = _service_not_available_future
    lookup_local_path_properties_batch = _service_not_available_future
    lookup_local_properties_by_fileid = _service_not_available_future
    lookup_local_properties_by_fileid_batch = _service_not_available_future
    lookup_lock_state = _service_not_available_future
    lookup_mount_point = _service_not_available_future
    lookup_properties_by_fileid = _service_not_available_future
    lookup_properties_by_fileid_batch = _service_not_available_future
    lookup_properties_by_local_path = _service_not_available_future
    lookup_remote_properties_by_fileid = _service_not_available_future
    lookup_remote_properties_by_fileid_batch = _service_not_available_future
    lookup_sync_icon = _service_not_available_future
    materialize_container = _service_not_available_future
    merge_into_dropbox = _service_not_available_future
    mr_server_to_fileid = _service_not_available_future
    notify_shadow_domain_created = _service_not_available_future
    notify_shadow_domain_deleted = _service_not_available_future
    pause_device_anchor = _service_not_available_future
    pause_engine = _service_not_available_future
    ping_sync_frontend = _service_not_available_future
    prepare_for_fp_migration = _service_not_available_future
    queue_resync = _service_not_available_future
    record_upcoming_folder_delete = _service_not_available_future
    register_tag_for_camera_uploads = _service_not_available_future
    remove_breadcrumbs = _service_not_available_future
    rename_into_dropbox = _service_not_available_future
    resolve_device_anchor = _service_not_available_future
    resume_device_anchor = _service_not_available_future
    resync_file = _service_not_available_future
    retry_over_quota_commits = _service_not_available_future
    rr_server_to_fileid = _service_not_available_future
    set_dbx_ignore_contents = _service_not_available_future
    set_path_ignored_state = _service_not_available_future
    start_shadow_migration_cutover = _service_not_available_future
    start_shadow_migration_cutover_dryrun = _service_not_available_future
    subscribe_to_backup_progress = _service_not_available_future
    suppress_fsws = _service_not_available_future
    test_only_echo = _service_not_available_future
    trigger_list = _service_not_available_future
    trigger_reconstruct = _service_not_available_future
    unbind_from_dropbox = _service_not_available_future
    unmerge_from_dropbox = _service_not_available_future
    unpack_fp_package = _service_not_available_future
    unpause_engine = _service_not_available_future
    update_config = _service_not_available_future
    update_infinite_operating_mode = _service_not_available_future
    update_priority_hint_by_fileid = _service_not_available_future
    validate_device_anchor_target = _service_not_available_future
    account = (lambda self = None: self._service_not_available())()
    deprecated_on_move_to_deleted_cache = _service_not_available
    deprecated_remove_on_move_to_deleted_cache_callback = _service_not_available
    device_folders_using_app_fs = _service_not_available
    file_locking_interface = (lambda self = None: self._service_not_available())()
    file_system = (lambda self = None: self._service_not_available())()
    get_download_status_snapshot = _service_not_available
    get_hash_status_snapshot = _service_not_available
    get_main_root_ns = _service_not_available
    get_p2p_meta_downloader = _service_not_available
    get_percent_complete = _service_not_available
    get_upload_status_snapshot = _service_not_available
    infinite_on_recall_event = _service_not_available
    is_file_provider = _service_not_available
    is_ready = _service_not_available
    on_applied_hidden_default = _service_not_available
    on_client_key_enrolled = _service_not_available
    on_computer_backup_progress = _service_not_available
    on_conflict_resolution_attempt = _service_not_available
    on_delete_suppressed_dir_restored = _service_not_available
    on_device_anchor_progress = _service_not_available
    on_device_anchor_unbind = _service_not_available
    on_encryption_error_event = _service_not_available
    on_engine_ready_for_redirection = _service_not_available
    on_fp_shadow_cutover_completed = _service_not_available
    on_hidden_set_changed = _service_not_available
    on_link_container_changed = _service_not_available
    on_mount_changed = _service_not_available
    on_moved_to_trash = _service_not_available
    on_moved_to_trash_summary = _service_not_available
    on_network_state_changed = _service_not_available
    on_new_team_key_fingerprint = _service_not_available
    on_one_way_sync_remediation = _service_not_available
    on_paths_sync_status_changed = _service_not_available
    on_pause_resume = _service_not_available
    on_queue_changed = _service_not_available
    on_remote_update = _service_not_available
    on_silly_labrador_event = _service_not_available
    on_sync_completed_summary = _service_not_available
    on_sync_engine_status = _service_not_available
    on_sync_failed = _service_not_available
    on_sync_progress = _service_not_available
    on_sync_progress_changed_by_fileid = _service_not_available
    remove_backup_sync_progress_callback = _service_not_available
    remove_delete_suppressed_dir_restored = _service_not_available
    remove_on_applied_hidden_default_callback = _service_not_available
    remove_on_conflict_resolution_attempt_callback = _service_not_available
    remove_on_device_anchor_unbind = _service_not_available
    remove_on_engine_ready_for_redirection = _service_not_available
    remove_on_hidden_set_changed_callback = _service_not_available
    remove_on_link_container_changed = _service_not_available
    remove_on_mount_changed_callback = _service_not_available
    remove_on_paths_sync_status_changed = _service_not_available
    remove_on_pause_resume = _service_not_available
    remove_on_queue_changed_callback = _service_not_available
    remove_on_remote_update = _service_not_available
    remove_on_sync_completed_summary_callback = _service_not_available
    remove_on_sync_failed_callback = _service_not_available
    remove_on_sync_progress_callback = _service_not_available
    remove_on_sync_progress_changed_by_fileid = _service_not_available
    remove_one_way_sync_remediation_callback = _service_not_available
    remove_silly_labrador_event_callback = _service_not_available
    rr_local_to_probable_local_path = _service_not_available
    selsync_manager = _service_not_available
    set_infinite_page_response_callback = _service_not_available
    update_account_properties = _service_not_available
    version = _service_not_available
    cleanup = _service_not_available
    convert_local = _service_not_available
    echo = _service_not_available
    get_dropbox_folder_disk_info_classic = _service_not_available
    get_last_local_revision_by_fileid_classic = _service_not_available
    get_last_local_revision_classic = _service_not_available
    get_local_file_status_classic = _service_not_available
    get_mount_points_under_path_classic = _service_not_available
    get_namespace_properties_classic = _service_not_available
    get_p2p_meta_downloader_classic = _service_not_available
    get_path_properties = _service_not_available
    get_temp_dir_on_dropbox_volume_classic = _service_not_available
    infinite_cancel_batch_classic = _service_not_available
    infinite_evict_batch_classic = _service_not_available
    infinite_recall_batch_classic = _service_not_available
    is_changed_classic = _service_not_available
    is_cloud_content = _service_not_available
    is_in_read_only_namespace = _service_not_available
    is_monitored = _service_not_available
    is_mount = _service_not_available
    list_dirs_classic = _service_not_available
    local_to_server = _service_not_available
    lookup_local_fileids = _service_not_available
    mount_relative_server_path = _service_not_available
    on_cdm_relocation_request_restart = _service_not_available
    on_conflict_resolution_attempt_classic = _service_not_available
    on_pause_resume_classic = _service_not_available
    register_tag_classic = _service_not_available
    remove_infinite_on_recall_event_callback = _service_not_available
    remove_on_conflict_resolution_attempt_callback_classic = _service_not_available
    remove_on_pause_resume_classic_callback = _service_not_available
    rename_into_dropbox_classic = _service_not_available
    root_relative_server_path_fast = _service_not_available
    running = (lambda self = None: self._service_not_available())()
    selsync_manager_classic = _service_not_available
    server_to_local_fast = _service_not_available
    start = _service_not_available
    stop = _service_not_available
    update_priority_hint = _service_not_available

_STUB_NUCLEUS_WRAPPER = _StubNucleusWrapper()

class SyncEngineWrapper(Parent, UserSingleton):
    pass
# WARNING: Decompyle incomplete

SyncEngineClassicInterface.register(SyncEngineWrapper)

class NucleusWrapper(NucleusParent, UserSingleton):
    pass
# WARNING: Decompyle incomplete

NucleusInterface.register(NucleusWrapper)
