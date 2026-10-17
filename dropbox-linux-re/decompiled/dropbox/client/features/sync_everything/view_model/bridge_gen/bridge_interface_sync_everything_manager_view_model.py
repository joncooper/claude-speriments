# Source Generated with Decompyle++
# File: bridge_interface_sync_everything_manager_view_model.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from dropbox.foundation.futures import Future
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_fetch_sub_folders_result import ComputerBackupFetchSubFoldersResult
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_get_dbx_ignore_contents_result import ComputerBackupGetDbxIgnoreContentsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_unlimited_storage_modal_actions import BackupUnlimitedStorageModalActions
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_folder_metadata import FolderMetadataBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_operation_result import OperationResultBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_state import DeviceState
from dropbox.client.features.sync_everything.view_model.bridge_gen.eligible_roles import EligibleRoles
from dropbox.client.features.sync_everything.view_model.bridge_gen.in_use_provider import InUseProvider
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.product_logging_event import ProductLoggingEvent
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.bridge_gen.stormcrow_values import StormcrowValues
from dropbox.client.features.users.bridge_gen.role import Role
from dropbox.client.features.users.bridge_gen.user_info import UserInfo
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface

class SyncEverythingManagerViewModelBridgeInterface(ABC):
    stop_redirect = (lambda self, logging_session_id = None, source = None, role = abstractmethod, is_turning_off_feature = ('logging_session_id', 'str', 'source', 'Source', 'role', 'Optional[Role]', 'is_turning_off_feature', 'Optional[bool]', 'return', 'Future[OperationResultBridgeInterface]'): pass)()
    update_redirect = (lambda self, folders, ignored_paths, logging_session_id, device_name, source, should_unmerge = None, quota_exempt = None, role = abstractmethod, is_sanity_check = ('folders', 'Dict[str, str]', 'ignored_paths', 'Dict[str, List[str]]', 'logging_session_id', 'str', 'device_name', 'str', 'source', 'Source', 'should_unmerge', 'bool', 'quota_exempt', 'bool', 'role', 'Optional[Role]', 'is_sanity_check', 'Optional[bool]', 'return', 'Future[OperationResultBridgeInterface]'): pass)()
    restore_device = (lambda self, folders, anchor_folders, logging_session_id, device_name = None, restore_device_id = None, source = abstractmethod, role = ('folders', 'Dict[str, str]', 'anchor_folders', 'Dict[str, str]', 'logging_session_id', 'str', 'device_name', 'str', 'restore_device_id', 'str', 'source', 'Source', 'role', 'Optional[Role]', 'return', 'Future[OperationResultBridgeInterface]'): pass)()
    start_cb_migration = (lambda self, device_name = None, logging_session_id = None, source = abstractmethod, role = ('device_name', 'str', 'logging_session_id', 'str', 'source', 'Source', 'role', 'Optional[Role]', 'return', 'Future[OperationResultBridgeInterface]'): pass)()
    ready_future = (lambda self = None: pass)()
    log_product_event = (lambda self, event_name = None, session_id = None, action_surface = abstractmethod, extra_json = ('event_name', 'ProductLoggingEvent', 'session_id', 'str', 'action_surface', 'Optional[ActionSurface]', 'extra_json', 'Optional[str]', 'return', 'Future[None]'): pass)()
    is_overquota = (lambda self = None, folders_selected = None, session_id = abstractmethod, role = ('folders_selected', 'List[str]', 'session_id', 'str', 'role', 'Optional[Role]', 'return', 'Future[bool]'): pass)()
    get_account_quota_info = (lambda self = None, role = None: pass)()
    get_device_state = (lambda self = None: pass)()
    get_host_name = (lambda self = None, selected_role = None: pass)()
    get_trial_experiment = (lambda self = None, role = None: pass)()
    open_url_authenticated = (lambda self = None, relative_url = None: pass)()
    context_for_role = (lambda self = None, role = None: pass)()
    open_icloud_preferences = (lambda self = None: pass)()
    open_full_disk_access_preferences = (lambda self = None: pass)()
    unpause_sync_engines = (lambda self = None: pass)()
    open_folder = (lambda self = None, folder = None: pass)()
    get_account_subscription_type = (lambda self = None, role = None: pass)()
    get_folder_metadata = (lambda self, folders = None, session_id = None, allow_consent = abstractmethod, role = ('folders', 'List[str]', 'session_id', 'str', 'allow_consent', 'bool', 'role', 'Optional[Role]', 'return', 'Future[Dict[str, FolderMetadataBridgeInterface]]'): pass)()
    get_folder_size = (lambda self = None, path = None, session_id = abstractmethod, role = ('path', 'str', 'session_id', 'str', 'role', 'Optional[Role]', 'return', 'Future[int]'): pass)()
    cancel_update_redirect = (lambda self = None: pass)()
    get_home_folder_name = (lambda self = None, selected_role = None: pass)()
    get_eligible_roles = (lambda self = None: pass)()
    mark_quota_exempt = (lambda self, context = None, device_id = None, source = abstractmethod, session_id = ('context', 'UserContextBridgeInterface', 'device_id', 'str', 'source', 'Source', 'session_id', 'str', 'return', 'Future[OperationResultBridgeInterface]'): pass)()
    list_backups_for_role = (lambda self = None, session_id = None, source = abstractmethod, role = ('session_id', 'str', 'source', 'Source', 'role', 'Optional[Role]', 'return', 'Future[ListBackupsResult]'): pass)()
    list_backups_for_user = (lambda self = None, session_id = None, source = abstractmethod, context = ('session_id', 'str', 'source', 'Source', 'context', 'UserContextBridgeInterface', 'return', 'Future[ListBackupsResult]'): pass)()
    get_next_backup_name_for_role = (lambda self, session_id = None, source = None, role = abstractmethod, allow_reuse = ('session_id', 'str', 'source', 'Source', 'role', 'Role', 'allow_reuse', 'bool', 'return', 'Future[Optional[str]]'): pass)()
    preview_on_web = (lambda self = None, role = None, device_name = abstractmethod: pass)()
    get_stormcrow_values = (lambda self = None: pass)()
    show_backup_app = (lambda self, role, session_logging_id, action_surface, source = None, params = None, inital_selected_id = abstractmethod, parent_id = ('role', 'Role', 'session_logging_id', 'str', 'action_surface', 'ActionSurface', 'source', 'Source', 'params', 'Optional[BackupAppParams]', 'inital_selected_id', 'Optional[str]', 'parent_id', 'Optional[int]', 'return', 'Future[None]'): pass)()
    show_custom_folders_selector = (lambda self, role, session_id, action_surface, source, backup_info = None, ignored_paths = None, anchor_folders_limit = abstractmethod, selected_folders = ('role', 'Role', 'session_id', 'str', 'action_surface', 'ActionSurface', 'source', 'Source', 'backup_info', 'BackupInfo', 'ignored_paths', 'Dict[str, List[str]]', 'anchor_folders_limit', 'Optional[int]', 'selected_folders', 'Optional[Dict[str, bool]]', 'return', 'Future[None]'): pass)()
    show_onboarding_carousel = (lambda self, role, session_logging_id, action_surface = None, source = None, ignored_paths = abstractmethod, folders = ('role', 'Role', 'session_logging_id', 'str', 'action_surface', 'ActionSurface', 'source', 'Source', 'ignored_paths', 'Dict[str, List[str]]', 'folders', 'Optional[Dict[str, str]]', 'return', 'Future[None]'): pass)()
    backup_sku_unlimited_reminder_ready = (lambda self = None: pass)()
    dismiss_backup_sku_unlimited_reminder = (lambda self = None: pass)()
    over_quota_reminder_ready = (lambda self = None: pass)()
    dismiss_over_quota_reminder = (lambda self = None: pass)()
    backup_trial_upsell_ready = (lambda self = None: pass)()
    dismiss_backup_trial_upsell = (lambda self = None: pass)()
    backup_onedrive_in_use_provider_modal_dismissed = (lambda self = None: pass)()
    dismiss_onedrive_in_use_provider_modal = (lambda self = None: pass)()
    get_user_info_for_role = (lambda self = None, role = None: pass)()
    get_device_id = (lambda self = None: pass)()
    show_backup_unlimited_storage_modal = (lambda self, session_logging_id = None, action = None, selected_backup = abstractmethod, role = ('session_logging_id', 'str', 'action', 'BackupUnlimitedStorageModalActions', 'selected_backup', 'BackupInfo', 'role', 'Role', 'return', 'Future[None]'): pass)()
    is_cb_using_anchors = (lambda self = None: pass)()
    get_accounts_with_anchors_gating_enabled = (lambda self = None: pass)()
    open_backup_all_on_server = (lambda self = None, role = None: pass)()
    get_folder_to_other_providers_map = (lambda self = None, folders = None, role = abstractmethod, session_id = ('folders', 'List[str]', 'role', 'Role', 'session_id', 'str', 'return', 'Future[Optional[Dict[str, List[InUseProvider]]]]'): pass)()
    fetch_l1_folders = (lambda self = None, role = None, session_id = abstractmethod: pass)()
    fetch_subfolders = (lambda self = None, role = None, folder = abstractmethod, session_id = ('role', 'Role', 'folder', 'str', 'session_id', 'str', 'return', 'Future[ComputerBackupFetchSubFoldersResult]'): pass)()
    read_dbx_ignore_contents = (lambda self, role = None, folder_id = None, session_id = abstractmethod, source = ('role', 'Role', 'folder_id', 'str', 'session_id', 'str', 'source', 'Source', 'return', 'Future[ComputerBackupGetDbxIgnoreContentsResult]'): pass)()
    get_allowed_folders = (lambda self = None: pass)()
    get_selected_folders_for_self_serve_migration = (lambda self = None, source = None: pass)()
    restart_app = (lambda self = None, role = None, session_logging_id = abstractmethod, action_surface = ('role', 'Role', 'session_logging_id', 'str', 'action_surface', 'ActionSurface', 'return', 'Future[None]'): pass)()

