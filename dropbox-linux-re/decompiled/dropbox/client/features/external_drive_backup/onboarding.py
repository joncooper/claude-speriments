# Source Generated with Decompyle++
# File: onboarding.pyc (Python 3.11)

from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup_folder_picker.bridge_gen.external_drive_backup_folder_picker_params import ExternalDriveBackupFolderPickerParams
from dropbox.client.features.external_drive_backup_permissions.bridge_gen.external_drive_backup_permissions_nav_params import ExternalDriveBackupPermissionsNavParams
from dropbox.client.features.sync_everything.v3.ux_param_utils import translate_role
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.manifest_registry import EXTERNAL_DRIVE_BACKUP_FOLDER_PICKER, EXTERNAL_DRIVE_BACKUP_PERMISSIONS

def show_external_drive_backup_permissions(navigation_service = None, drive_info = None, session_logging_id = None, source = ('navigation_service', 'NavigationServiceInterface', 'drive_info', 'DriveInfo', 'session_logging_id', 'str', 'source', 'EdbSource', 'return', 'None')):
    return navigation_service.navigate(EXTERNAL_DRIVE_BACKUP_PERMISSIONS, view_key = 'external_drive_backup_permissions', parameter = ExternalDriveBackupPermissionsNavParams(session_logging_id = session_logging_id, drive_info = drive_info, source = source), load_policy = NavigationLoadPolicy.CREATE_ALWAYS).ground(component = DesktopComponent.SYNC_EVERYTHING)


def show_external_drive_backup_folder_picker(navigation_service, role = None, drive_info = None, session_id = None, source = ('navigation_service', 'NavigationServiceInterface', 'drive_info', 'DriveInfo', 'session_id', 'str', 'source', 'EdbSource', 'return', 'None')):
    return navigation_service.navigate(EXTERNAL_DRIVE_BACKUP_FOLDER_PICKER, view_key = 'external_drive_backup_folder_picker', parameter = ExternalDriveBackupFolderPickerParams(session_logging_id = session_id, role = translate_role(role), root_path = drive_info.mount_path, drive_info = drive_info, source = source), load_policy = NavigationLoadPolicy.CREATE_ALWAYS).ground(component = DesktopComponent.SYNC_EVERYTHING)

