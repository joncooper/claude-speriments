# Source Generated with Decompyle++
# File: bridge_interface_external_drive_backup_manager_view_model.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from dropbox.foundation.futures import Future
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_action_surface import EdbActionSurface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_stormcrow_values import EdbStormcrowValues
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.fetch_sub_folders_result import FetchSubFoldersResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.get_dbx_ignore_contents_result import GetDbxIgnoreContentsResult
from dropbox.client.features.users.bridge_gen.role import Role
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface

class ExternalDriveBackupManagerViewModelBridgeInterface(ABC):
    get_active_external_drives = (lambda self = None: pass)()
    start_backup = (lambda self, role, drive = None, session_id = None, source = abstractmethod, rel_ignored_paths = ('role', 'Role', 'drive', 'DriveInfo', 'session_id', 'str', 'source', 'EdbSource', 'rel_ignored_paths', 'List[str]', 'return', 'Future[BackupResult]'): pass)()
    read_dbx_ignore_contents = (lambda self, role = None, session_id = None, source = abstractmethod, device_anchor_fileid = ('role', 'Role', 'session_id', 'str', 'source', 'EdbSource', 'device_anchor_fileid', 'str', 'return', 'Future[GetDbxIgnoreContentsResult]'): pass)()
    custom_folders_start_backup = (lambda self, role, drive = None, session_id = None, source = abstractmethod, rel_ignored_paths = ('role', 'Role', 'drive', 'DriveInfo', 'session_id', 'str', 'source', 'EdbSource', 'rel_ignored_paths', 'List[str]', 'return', 'Future[None]'): pass)()
    custom_folders_discard_drive = (lambda self = None, drive = None: pass)()
    custom_folders_update_selection = (lambda self, role, session_id = None, source = None, device_anchor_fileid = abstractmethod, rel_ignored_paths = ('role', 'Role', 'session_id', 'str', 'source', 'EdbSource', 'device_anchor_fileid', 'str', 'rel_ignored_paths', 'List[str]', 'return', 'Future[BackupResult]'): pass)()
    open_finder_or_explorer = (lambda self = None, role = None: pass)()
    log_product_event = (lambda self, role, event_name, session_id = None, source = None, action_surface = abstractmethod, extras = ('role', 'Role', 'event_name', 'ExternalBackupEvent', 'session_id', 'str', 'source', 'EdbSource', 'action_surface', 'EdbActionSurface', 'extras', 'Optional[Dict[str, str]]', 'return', 'Future[None]'): pass)()
    do_not_show_ux_again_for_drive = (lambda self = None, drive = None: pass)()
    context_for_role = (lambda self = None, role = None: pass)()
    get_account_subscription_type = (lambda self = None, role = None: pass)()
    is_overquota = (lambda self = None, role = None, selected_drives = abstractmethod: pass)()
    is_overquota_upsell = (lambda self = None, role = None, selected_drives = abstractmethod, session_id = ('role', 'Role', 'selected_drives', 'List[DriveInfo]', 'session_id', 'str', 'return', 'Future[bool]'): pass)()
    get_stormcrow_values = (lambda self = None, role = None: pass)()
    fetch_subfolders = (lambda self, role = None, path = None, is_root = abstractmethod, session_id = ('role', 'Role', 'path', 'str', 'is_root', 'bool', 'session_id', 'str', 'return', 'Future[FetchSubFoldersResult]'): pass)()

