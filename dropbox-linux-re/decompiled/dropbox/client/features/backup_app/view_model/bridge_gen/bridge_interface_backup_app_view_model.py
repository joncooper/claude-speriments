# Source Generated with Decompyle++
# File: bridge_interface_backup_app_view_model.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from dropbox.foundation.futures import Future
from dropbox.foundation.signals import Signal
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_schedule import BackupSchedule
from dropbox.client.features.backup_app.view_model.bridge_gen.device_backup_info import DeviceBackupInfo
from dropbox.client.features.backup_app.view_model.bridge_gen.external_drive_backup_info import ExternalDriveBackupInfo
from dropbox.client.features.backup_app.view_model.bridge_gen.team_features import TeamFeatures
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_sync_progress import EdbSyncProgress
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_operation_result import OperationResultBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.cb_sync_progress import CbSyncProgress
from dropbox.client.features.sync_everything.view_model.bridge_gen.product_logging_event import ProductLoggingEvent
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.users.bridge_gen.role import Role
from dropbox.client.features.users.bridge_gen.user_info import UserInfo

class BackupAppViewModelBridgeInterface(ABC):
    log_event = (lambda self, event, role, session_logging_id = None, source = None, action_surface = abstractmethod, extra_json = ('event', 'ProductLoggingEvent', 'role', 'Role', 'session_logging_id', 'str', 'source', 'Source', 'action_surface', 'Optional[ActionSurface]', 'extra_json', 'Optional[str]', 'return', 'Future[None]'): pass)()
    get_local_device_state = (lambda self = None: pass)()
    get_local_external_drive_backups = (lambda self = None, role = None, session_logging_id = abstractmethod: pass)()
    get_eligible_plugged_in_drives = (lambda self = None, role = None, session_logging_id = abstractmethod: pass)()
    get_all_plugged_in_external_drives = (lambda self = None, session_logging_id = None: pass)()
    get_team_features = (lambda self = None, session_logging_id = None: pass)()
    get_drive_setup_signal = (lambda self = None: pass)()
    get_drive_plugged_in_signal = (lambda self = None: pass)()
    get_drive_unplugged_signal = (lambda self = None: pass)()
    get_dbx_ignore_contents_changed_signal = (lambda self = None: pass)()
    get_cb_backup_sync_progress_signal = (lambda self, session_id = None, fileid = None, role = abstractmethod, source = ('session_id', 'str', 'fileid', 'str', 'role', 'Role', 'source', 'Optional[Source]', 'return', 'Future[Signal[CbSyncProgress]]'): pass)()
    get_edb_backup_sync_progress_signal = (lambda self, session_id = None, fileid = None, role = abstractmethod, source = ('session_id', 'str', 'fileid', 'str', 'role', 'Role', 'source', 'Optional[EdbSource]', 'return', 'Future[Signal[EdbSyncProgress]]'): pass)()
    open_backup_on_server = (lambda self = None, role = None, device_name = abstractmethod, params = ('role', 'Role', 'device_name', 'Optional[str]', 'params', 'Optional[Dict[str, str]]', 'return', 'Future[None]'): pass)()
    open_rewind_on_server = (lambda self = None, role = None, device_name = abstractmethod: pass)()
    open_deleted_files_on_server = (lambda self = None, role = None, device_name = abstractmethod, params = ('role', 'Role', 'device_name', 'Optional[str]', 'params', 'Optional[Dict[str, str]]', 'return', 'Future[None]'): pass)()
    open_account_plan_on_server = (lambda self = None, role = None: pass)()
    open_backup_in_finder_or_explorer = (lambda self = None, role = None, fileid = abstractmethod: pass)()
    show_tray = (lambda self = None: pass)()
    open_preferences_bandwidth_tab = (lambda self = None: pass)()
    show_backup_app = (lambda self, role, session_logging_id, action_surface, source = None, initial_selected_id = None, params = abstractmethod, parent_id = ('role', 'Role', 'session_logging_id', 'str', 'action_surface', 'ActionSurface', 'source', 'Source', 'initial_selected_id', 'Optional[str]', 'params', 'Optional[BackupAppParams]', 'parent_id', 'Optional[int]', 'return', 'Future[None]'): pass)()
    show_backup_sku_modal = (lambda self, role = None, session_logging_id = None, action_surface = abstractmethod, source = ('role', 'Role', 'session_logging_id', 'str', 'action_surface', 'ActionSurface', 'source', 'Source', 'return', 'Future[None]'): pass)()
    start_external_drive_backup = (lambda self = None, role = None, session_logging_id = abstractmethod, device_id = ('role', 'Role', 'session_logging_id', 'str', 'device_id', 'str', 'return', 'Future[Optional[BackupResult]]'): pass)()
    pause_backup = (lambda self, role = None, session_logging_id = None, fileid = abstractmethod, is_fission = ('role', 'Role', 'session_logging_id', 'str', 'fileid', 'Optional[str]', 'is_fission', 'Optional[bool]', 'return', 'Future[Optional[BackupResult]]'): pass)()
    resume_backup = (lambda self, role = None, session_logging_id = None, fileid = abstractmethod, is_fission = ('role', 'Role', 'session_logging_id', 'str', 'fileid', 'Optional[str]', 'is_fission', 'Optional[bool]', 'return', 'Future[Optional[BackupResult]]'): pass)()
    rename_backup = (lambda self, role = None, device_id = None, new_display_name = abstractmethod, session_logging_id = ('role', 'Role', 'device_id', 'str', 'new_display_name', 'str', 'session_logging_id', 'str', 'return', 'Future[OperationResultBridgeInterface]'): pass)()
    rename_external_drive_backup = (lambda self, role, session_logging_id = None, new_display_name = None, fileid = abstractmethod, is_fission = ('role', 'Role', 'session_logging_id', 'str', 'new_display_name', 'str', 'fileid', 'Optional[str]', 'is_fission', 'Optional[bool]', 'return', 'Future[Optional[BackupResult]]'): pass)()
    delete_external_drive_backup = (lambda self, role = None, session_logging_id = None, fileid = abstractmethod, source = ('role', 'Role', 'session_logging_id', 'str', 'fileid', 'Optional[str]', 'source', 'Optional[EdbSource]', 'return', 'Future[Optional[BackupResult]]'): pass)()
    list_computer_backups_for_role = (lambda self, session_logging_id, source = None, role = None, include_last_ts = abstractmethod, remote_only = ('session_logging_id', 'str', 'source', 'Source', 'role', 'Role', 'include_last_ts', 'bool', 'remote_only', 'Optional[bool]', 'return', 'Future[List[DeviceBackupInfo]]'): pass)()
    list_external_backups_for_role = (lambda self, session_logging_id, role = None, include_last_ts = None, remote_only = abstractmethod, keep_id_prefix = ('session_logging_id', 'str', 'role', 'Role', 'include_last_ts', 'bool', 'remote_only', 'Optional[bool]', 'keep_id_prefix', 'Optional[bool]', 'return', 'Future[List[ExternalDriveBackupInfo]]'): pass)()
    show_custom_folders_for_cb = (lambda self, role, backup_info, session_logging_id, source, action_surface = None, anchor_folders_limit = None, preselected_path = abstractmethod, unselected_paths = ('role', 'Role', 'backup_info', 'BackupInfo', 'session_logging_id', 'str', 'source', 'Source', 'action_surface', 'ActionSurface', 'anchor_folders_limit', 'Optional[int]', 'preselected_path', 'Optional[str]', 'unselected_paths', 'Optional[List[str]]', 'return', 'Future[None]'): pass)()
    show_custom_folder_for_edb = (lambda self, role, session_logging_id = None, drive_uuid = None, anchor_fileid = abstractmethod, rel_ignore_paths = ('role', 'Role', 'session_logging_id', 'str', 'drive_uuid', 'str', 'anchor_fileid', 'Optional[str]', 'rel_ignore_paths', 'Optional[List[str]]', 'return', 'Future[None]'): pass)()
    get_user_info_for_role = (lambda self = None, role = None: pass)()
    set_device_quota_exempt = (lambda self, role = None, device_id = None, source = abstractmethod, session_logging_id = ('role', 'Role', 'device_id', 'str', 'source', 'Source', 'session_logging_id', 'str', 'return', 'Future[OperationResultBridgeInterface]'): pass)()
    set_drive_quota_exempt = (lambda self, role = None, session_logging_id = None, source = abstractmethod, fileid = ('role', 'Role', 'session_logging_id', 'str', 'source', 'EdbSource', 'fileid', 'str', 'return', 'Future[Optional[BackupResult]]'): pass)()
    show_restoration = (lambda self, role, backups = None, source = None, action_surface = abstractmethod, session_logging_id = ('role', 'Role', 'backups', 'List[BackupInfo]', 'source', 'Source', 'action_surface', 'ActionSurface', 'session_logging_id', 'str', 'return', 'Future[None]'): pass)()
    is_cb_using_anchors = (lambda self = None: pass)()
    toggle_automatic_backup = (lambda self = None, should_enable = None: pass)()
    update_cb_schedule = (lambda self = None, schedule = None: pass)()
    backup_cb_now = (lambda self = None: pass)()
    backup_edb_now = (lambda self = None, anchor_fileid = None: pass)()
    get_cb_schedule = (lambda self = None: pass)()
    get_edb_schedule = (lambda self = None, anchor_fileid = None: pass)()
    update_edb_schedule = (lambda self = None, schedule = None, anchor_fileid = abstractmethod: pass)()
    track_event_to_sprig = (lambda self = None, event_name = None: pass)()
    set_migrate_cb_on_restart = (lambda self = None: pass)()

