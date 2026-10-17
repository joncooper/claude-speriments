# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

import os
from typing import List, Optional, Text, Tuple
from dropbox.api.v2.datatypes.external_drive_backup import ExternalDriveBackupStateEnum, ExternalDriveEntry, ListBackupsResult as ListDriveBackupsResult
from dropbox.client.authentication.account import Account
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_status import BackupStatus
from dropbox.client.features.backup_app.view_model.bridge_gen.device_backup_info import DeviceBackupInfo
from dropbox.client.features.backup_app.view_model.bridge_gen.external_drive_backup_info import ExternalDriveBackupInfo
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.constants import EDB_ANCHOR_EXTENSION
from dropbox.client.features.computer_backup.constants import BackupStatus as ComputerBackupAnchorsBackupStatus
from dropbox.client.features.external_drive_backup.constants import EDB_DEFAULT_NAME, ExternalDriveBackupUIStrings
from dropbox.client.features.external_drive_backup.edb_in_memory_tracker import EDBInMemoryTracker
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.types import SeparatedAnchorsByEngineAndState
from dropbox.client.features.external_drive_backup.utils import is_drive_parent_of_dropbox_folder, is_drive_parent_of_dropboxbackup_folder, is_large_edb_drive
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.sync_everything.constants import DeviceStatus
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.device_state import DeviceState
from dropbox.client.features.sync_everything.v3.errors import RequestFailedException
from dropbox.client.features.sync_everything.v3.utils import is_offline
from dropbox.client.features.sync_everything.v3.ux_param_utils import translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.platform_type import PlatformType
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.constants import KNOWN_FOLDER_NAME_MAP
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.client.ui.common.preferences_utils import PanelNames
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.types.ids import FileID
from dropbox.model.types import FileId
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo, DeviceAnchorState

def get_user_context_from_role(machine_context = None, role = None):
    account_models = machine_context.account_manager.account_models
    for account, model in account_models.items():
        if account.role and translate_role(account.role) == role:
            
            return None, model.user_context
        return None


def get_team_account_and_user_context(machine_context = None):
    account_models = machine_context.account_manager.account_models
    for account, model in account_models.items():
        if account.is_dfb_user:
            
            return None, (account, model.user_context)
        return (None, None)


def device_state_to_device_backup_info(device_state, device_id, platform, has_migration_status, role, root_fileid, home_mount_path = None, backup_status = None, display_name = None, last_backed_up_ms = ('device_state', 'DeviceState', 'device_id', 'str', 'platform', 'PlatformType', 'has_migration_status', 'bool', 'role', 'Optional[BIDLRole]', 'root_fileid', 'Optional[str]', 'home_mount_path', 'Optional[str]', 'backup_status', 'Optional[ComputerBackupAnchorsBackupStatus]', 'display_name', 'Optional[str]', 'last_backed_up_ms', 'Optional[float]', 'return', 'DeviceBackupInfo')):
    pass
# WARNING: Decompyle incomplete


def get_device_backup_info_status(device_state = None, backup_status = None):
    if device_state.status == DeviceStatus.ENABLED:
        if backup_status == ComputerBackupAnchorsBackupStatus.BACKUP_PAUSED:
            return BackupStatus.PAUSED
        return None.DONE
    return None.NOT_ENABLED


def get_platform_type():
    if IS_MAC:
        return PlatformType.MAC
    return PlatformType.WIN if None else PlatformType.UNKNOWN


def _get_drive_name_from_path(path = None):
    name = os.path.basename(path)
    (basename, ext) = os.path.splitext(name)
    if ext == EDB_ANCHOR_EXTENSION:
        return basename


def both_engine_result_to_drive_backup_info_list(eng_result = None, user_context = None, role = None):
    pass
# WARNING: Decompyle incomplete


def get_newly_added_external_drive_backup(separated_anchors_by_eng_and_state = None, role = None, machine_context = None):
    session_id = random_session_id()
    newly_added_edb_infos = []
    if not (ExternalDriveBackupFeature.enable_edb_setup_from_desktop_surface(machine_context) or role == BIDLRole.BUSINESS) and ExternalDriveBackupFeature.backup_allowed_for_team_sku(machine_context):
        return newly_added_edb_infos
    eligible_plugin_edb = EDBInMemoryTracker.get_eligible_plugged_in_drives()
    for drive_id, drive_info in eligible_plugin_edb.items():
        is_fission = not separated_anchors_by_eng_and_state.is_uuid_in_fss(drive_id)
        if not _has_been_backed_up(separated_anchors_by_eng_and_state, drive_id) and _is_parent_of_dropbox_or_dropboxbackup(role, machine_context, drive_info, session_id):
            newly_added_edb_infos.append(_drive_info_to_drive_backup_info(drive_info, is_fission, role))
        return newly_added_edb_infos


def _is_parent_of_dropbox_or_dropboxbackup(role = None, machine_context = None, drive_info = None, session_id = ('role', 'Optional[BIDLRole]', 'machine_context', 'MachineContext', 'drive_info', 'DriveInfo', 'session_id', 'str', 'return', 'Optional[bool]')):
