# Source Generated with Decompyle++
# File: preferences_service.pyc (Python 3.11)

import os
from datetime import datetime, timezone
from enum import Enum, StrEnum, unique
from typing import Any, cast, Dict, List, Optional, Text, TypedDict
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.camera_upload.camera_upload_metric_logger import CameraEvent, MetricsLogger as CameraLogger
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_accounts
from dropbox.client.features.cloud_files_migration.gating import should_migrate_to_cloud_files
from dropbox.client.features.cloud_files_migration.migration_manager import CloudFilesMigrationManager
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.file_provider_migration.config import FPMigrationStateStore
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_AUTO_MIGRATION_DEADLINE_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_OPT_OUT_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_OPT_OUT_STORMCROW, FILE_PROVIDER_AUTO_MIGRATION_SCHEDULED_DATE_CONFIG_KEY
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FileProviderMigrationExtraKeys, FileProviderMigrationLogger, FPMigrationEligibilityCheckKeys
from dropbox.client.features.file_provider_migration.implementation import FileProviderMigrationController, FileProviderMigrationControllerWrapper
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.types import FileProviderMigrationState
from dropbox.client.features.file_provider_migration.ui.controllers.pre_migration_flow import PreMigrationFlowController
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_action_surface import FileProviderActionSurface
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_migration_event import FileProviderMigrationEvent
from dropbox.client.features.flexible_filenames.gating import get_flexible_filenames_on_variant, get_flexible_filenames_rules, save_flexible_filenames_rules
from dropbox.client.features.smart_sync_removal_mitigation.helpers import ss_removal_mitigation_degraded_placeholders_enabled
from dropbox.client.features.smarter_smart_sync.constants import SSAutoevictPolicy
from dropbox.client.features.smarter_smart_sync.feature import SmarterSmartSyncFeature
from dropbox.client.features.smarter_smart_sync.logger import log_ss_autoevict_user_actions, PolicyChangeReason
from dropbox.client.features.smarter_smart_sync.smarter_smart_sync_policy import SmarterSmartSyncPolicyController
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeInterval
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.journeys.cx_utils import fix_dropbox_permissions, fix_hardlinks, get_folders_to_hard_reset, reset_folder_os_location_hard, reset_folder_os_location_normal, reset_fsw
from dropbox.client.fenix.types.account import ServerAccount
from dropbox.client.fenix.utils import convert_to_local_account, get_account_linked_or_from_cache
from dropbox.client.multiaccount.role import Roles
from dropbox.client.office.constants import OfficeAddInFailureReason
from dropbox.client.status.label import StatusLabel
from dropbox.client.theme_manager.theme_manager import get_os_theme_setting, get_theme_preference, set_theme_setting_to_value
from dropbox.client.theme_manager.types import Theme
from dropbox.client.tray.tray_runtime_controller import TrayRuntimeController
from dropbox.client.ui.common.preferences import clear_cu_device_from_list, refresh_office_addin_enabled, set_web_locale, should_show_infinite_settings, update_root_policy
from dropbox.client.ui.common.selective_sync_v4 import show_selsync_mev
from dropbox.client.ui.common.sync_everything_preferences import handle_sync_everything_settings
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.client.util import enable_p2p_default
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import sanitize_event_extra_dict
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONish
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2 import destroying
from dropbox.i18n import format_time, get_available_languages, get_current_code, set_user_interface_language, system_lang_code
from dropbox.infinite import dod_for_non_fp_enabled, infinite_exposed
from dropbox.infinite.preferences import InfinitePolicy, InfinitePolicyController
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.preferences import OPT_LANG
from dropbox.proto.nucleus.app_service_pb2 import FlexibleFilenamesConfigReply, UpdateConfigReply, UpdateConfigReq
from dropbox.proto.nucleus.sync_engine_pb2 import FlexibleFilenamesConfig, UpdatableAppConfig, UserConfig
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.sync_root.gating import is_file_provider_root_type
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.finder import restart as _restart_finder
    from dropbox.mac.version import MAC_VERSION, MOJAVE, MONTEREY_1205
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
AvailableUpdatesType = <NODE:12>()

class PreferencesEventNames(StrEnum):
    LAUNCH_SETUP_WIZARD_SUCCESS = 'launch_setup_wizard_prefs_success'
    LAUNCH_SETUP_WIZARD_FAILED = 'launch_setup_wizard_prefs_failed'
    LAUNCH_SELECTIVE_SYNC_SUCCESS = 'launch_selective_sync_prefs_success'
    LAUNCH_SELECTIVE_SYNC_FAILED = 'launch_selective_sync_prefs_failed'


def report_preferences_event(account = None, event_name = unique, session_id = None, extra = (None,)):
    new_event = NonUserLoggingEvent(event_name = event_name.value, feature_session_id = session_id, action_surface = 'preferences_ui', source = '', component = DesktopComponent.PREFERENCES_UI, extra_hive_dict_pii = sanitize_event_extra_dict(extra) if extra else None)
    DesktopLogger.log_event(new_event, account)


class NonAuthenticatedAccount(ServerAccount):
    ui_flags: 'Dict[str, Any]' = 'NonAuthenticatedAccount'


def convert_to_non_authenticated_account(account = None):
    pass
# WARNING: Decompyle incomplete


class PreUnlinkState(TypedDict):
    account_has_backup_schedule: 'bool' = 'PreUnlinkState'


class SetLanguageState(Enum):
    CANCELLED_IMPORTING = 'cancelled_importing'
    PROMPT_RESTART = 'prompt_restart'
    DONE = 'done'


class PreferencesService(Actor):
    pass
# WARNING: Decompyle incomplete

