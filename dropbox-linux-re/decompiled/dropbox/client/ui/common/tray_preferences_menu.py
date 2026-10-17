# Source Generated with Decompyle++
# File: tray_preferences_menu.pyc (Python 3.11)

from typing import Any, Callable, Dict, List, Optional, Text, Tuple
from build_number import IS_MAC, IS_WINDOWS
from dropbox.client.authentication.account import Role
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.camera_upload.types import CUDeviceUID
from dropbox.client.features.backup_app.view_model.bridge_gen.external_drive_backup_info import ExternalDriveBackupInfo
from dropbox.client.features.backup_app.view_model.view_model import BackupAppViewModel
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper, DeviceStateWithStatus
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_folder_status import FolderStatusBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.client.multiaccount.role import Roles
from dropbox.client.notifications.preference_settings import NotificationPreferencesStringMapping
from dropbox.client.tray.logging.pap_logging_helpers import log_select_desktop_surface_action_tray_low_ui
from dropbox.client.ui.common.dialog_constants import IconType
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem, Separator, SubMenu
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client.ui.common.preferences import change_client_language, clear_cu_device_from_list, get_cu_devices_list, get_cu_label_for_device, should_show_infinite_settings, update_root_policy
from dropbox.client.ui.common.strings import AccountString, UI, UIStrings
from dropbox.client.ui.common.tray_preferences_menu_utils import are_there_advisory_errors, are_there_folder_with_errors, get_list_of_folders_with_advisory_errors, get_list_of_folders_with_errors, should_show_full_error, should_show_partial_error
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.client.util import enable_p2p_default
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.signals import Signal, StandardSignal
from dropbox.i18n import get_available_languages
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.preferences import OPT_LANG, OPT_P2P, OPT_PHOTO, OPT_SCREENSHOTS, OPT_STARTUP, OPT_VIDEO
from dropbox.sync_root.gating import is_file_provider_root_type
if IS_WINDOWS:
    from dropbox.client.ui.native.location_changer import DropboxLocationChanger
    from dropbox.client.ui.win32.preferences.bandwidth import show_bandwidth_settings_dialog
    from dropbox.client.ui.win32.preferences.proxy import show_proxy_settings_dialog
    from dropbox.client.ui.win32.selective_sync_win32 import SelectiveSyncWin32
elif IS_MAC:
    from AppKit import NSObject
    from dropbox.client.ui.cocoa.dropbox_controls import LocationButton
    from dropbox.client.ui.cocoa.preferences.preferences import show_bandwidth_settings_dialog, show_proxy_settings_dialog
    from dropbox.client.ui.cocoa.selective_sync_v2 import SelectiveSyncSheetv2
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class TrayPreferencesStrings(UIStrings):
    preferences_menu = UI('Preferences')
    system_language_menu = UI('Language')
    startup = UI('Open Dropbox upon startup')
    unlink_dropbox = UI('Sign out')
    notifications_menu = UI('Notifications')
    network_menu = UI('Network')
    bandwidth = UI('Bandwidth...')
    proxy = UI('Proxy...')
    lan_sync = UI('LAN Sync')
    sync_menu = UI('Sync')
    selective_sync = UI('Selective Sync...')
    move_dropbox = UI('Move Dropbox...')
    default_state_menu = UI('Default sync preference')
    online_only = UI('Online-only')
    available_offline = UI('Available offline')
    sign_in = UI('Sign in')
    unlink_settings_on_web = UI('Unlink these accounts in Settings on web')
    accounts = UI('Accounts')
    backups_menu = UI('Backups')
    screenshots_menu = UI('Screenshots')
    camera_uploads_menu = UI('Camera Uploads')
    camera_uploads_enabled = UI('Enabled')
    camera_uploads_disabled = UI('Disabled')
    camera_uploads_import_video = UI('Import Videos')
    camera_uploads_remove_devices = UI('Forget Device')
    screenshots_singleaccount = UI('Save screenshots to Dropbox')
    screenshots_multiaccount = AccountString('Save screenshots to your <personal> Dropbox')
    screenshots_off = UI("Don't save screenshots to Dropbox")
    backup_menu_disable = UI('Disable %(backup_name)s Backup')
    cancel_and_disable_backup_button_while_unlinking = UI('Cancel and Disable Backup First')
    continue_anyway_button_while_unlinking = UI('Continue Anyway')
    external_drive_backup_menu_business = UI('Delete External Drive Backups (%(team_name)s)')
    external_drive_backup_menu_personal = UI('Delete External Drive Backups (Personal)')
    account_role_business = UI('Business')


class DisableBackupStrings(UIStrings):
    disable_backup_error_caption = UI("Couldn't disable backup")
    disable_backup_error_caption_partial = UI("Couldn't disable backup for some folders")
    disable_backup_error_message_partial = UI('Folders that failed to disable:\n')
    disable_backup_error_caption_advisory = UI('Backup is disabled, but some files are still stored in your Dropbox folder')
    disable_backup_error_message_advisory = UI('Folders with leftover content:\n')
    disable_backup_error_caption_success = UI('Backup disabled')
    disable_backup_error_message_success = UI('Backup is now disabled for all selected folders')
    general_backup_disable_failed = UI('Backup Disable Failed')
    confirmation_disable_backup_caption = UI('Are you sure you want to disable backup?')
    confirmation_delete_backup_caption = UI('Are you sure you want to delete backup?')
    external_drive_backup_disabled = UI('External Drive Backup Deleted')
    external_drive_backup_disabled_failed = UI('External Drive Backup Delete Failed')


class TrayPreferencesMenu(Destroyable):
    pass
# WARNING: Decompyle incomplete

