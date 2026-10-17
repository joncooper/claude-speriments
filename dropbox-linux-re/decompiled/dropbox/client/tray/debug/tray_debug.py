# Source Generated with Decompyle++
# File: tray_debug.pyc (Python 3.11)

import functools
import json
import os
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from typing import Any, Callable, cast, Dict, List, Mapping, NamedTuple, Optional, Sequence, Text, Tuple, TypeVar
from uuid import uuid4
from weakref import WeakSet
from mypy_extensions import KwArg, VarArg
from build_number import BUILD_KEY, is_electron_application, is_store_managed
from build_number.features import feature_enabled
from dropbox.camera import Device
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.autorestart import CONFIG_AUTORESTART_ATTEMPTS, show_autorestart_notification_maybe_quit, show_hit_limit_notification_maybe_quit
from dropbox.client.background_worker import on_background_thread
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.configuration.manager import ConfigurationManager
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.delete_on_unlink import DeleteOnUnlink
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.apollo_alerts.view_model.apollo_alerts_vm import ApolloAlertsVM
from dropbox.client.features.apollo_alerts.view_model.bridge_gen.alert_result_record import AlertResultRecord
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_schedule import BackupSchedule
from dropbox.client.features.backup_app.view_model.bridge_gen.schedule_detail import ScheduleDetail
from dropbox.client.features.backup_app.view_model.bridge_gen.schedule_type import ScheduleType
from dropbox.client.features.backup_auto_selsync.auto_selsync_manager import AutoSelSyncManager
from dropbox.client.features.backup_auto_selsync.auto_selsync_result import BackupAutoSelSyncResult
from dropbox.client.features.backup_auto_selsync.bi_auto_selsync_manager import BackupAutoSelSyncManager
from dropbox.client.features.backup_auto_selsync.gating import BackupAutoSelSyncFeature
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.constants import CONFIG_KEY_COMPUTER_BACKUP_LAST_JOB_TIME, CONFIG_KEY_COMPUTER_BACKUP_SCHEDULE, CONFIG_KEY_EXTERNAL_DRIVE_BACKUP_LAST_JOB_TRIGGERED_TIME, CONFIG_KEY_EXTERNAL_DRIVE_BACKUP_SCHEDULE, EDB_ANCHOR_EXTENSION
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.backup_instance.utils import BI_TRACE
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.backup_quota_exempt_picker.bridge_gen.backup_quota_exempt_picker_nav_params import BackupQuotaExemptPickerNavParams
from dropbox.client.features.backup_restorations_onboarding.bridge_gen.backup_restorations_onboarding_nav_params import BackupRestorationsOnboardingNavParams
from dropbox.client.features.backup_restorations_onboarding.bridge_gen.eligible_backups import EligibleBackups
from dropbox.client.features.backup_sku_onboarding.bridge_gen.backup_sku_onboarding_nav_params import BackupSkuOnboardingNavParams
from dropbox.client.features.backup_unlimited_storage_modal.view_model.bridge_gen.backup_unlimited_storage_modal_nav_params import BackupUnlimitedStorageModalNavParams
from dropbox.client.features.bug_reporter.types import BugType
from dropbox.client.features.computer_backup.manager import ComputerBackupManager
from dropbox.client.features.computer_backup_custom_folder_picker.bridge_gen.computer_backup_custom_folder_picker_params import ComputerBackupCustomFolderPickerParams
from dropbox.client.features.copy_to_dropbox.constants import ExternalContextMenuSharingSurface
from dropbox.client.features.copy_to_dropbox.utils import debug_launch_external_context_menu_sharing_view
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import PAPLoggingEvent
from dropbox.client.features.external_drive_backup.constants import CONFIG_KEY_EDB_FAT_VENTURA_CAPACITY_UPDATED_UUIDS, CONFIG_KEY_EDB_ONBOARDING_DO_NOT_SHOW_UUIDS, CONFIG_KEY_EDB_ONBOARDING_UUIDS_COUNTS, CONFIG_KEY_EDB_PAUSED_BUBBLE_COUNTER, CONFIG_KEY_EDB_REMEDIATED_UUIDS, CONFIG_KEY_EDB_UNBIND_ALERT_SHOWN_UUIDS, ExternalDriveArrivalEvent
from dropbox.client.features.external_drive_backup.disk_arbitration import debug_list_drives
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.fission_migration_info import FissionMigrationInfo as BasicFissionMigrationInfo, FissionMigrationStatus as BasicFissionMigrationStatus
from dropbox.client.features.external_drive_backup.integration_test import ExternalDriveBackupIntegrationTest
from dropbox.client.features.external_drive_backup.manager import _Status, ExternalBackupManager
from dropbox.client.features.external_drive_backup.server_interface import ServerInterface
from dropbox.client.features.external_drive_backup.types import SeparatedAnchorsByEngineAndState
from dropbox.client.features.external_drive_backup.utils import list_anchors_by_uuid_both_engines
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup_folder_picker.bridge_gen.external_drive_backup_folder_picker_params import ExternalDriveBackupFolderPickerParams
from dropbox.client.features.external_drive_backup_permissions.bridge_gen.external_drive_backup_permissions_nav_params import ExternalDriveBackupPermissionsNavParams
from dropbox.client.features.file_locking.file_locking_controller import FileLockingAccessor
from dropbox.client.features.file_locking.file_locking_error_alert import FileLockingErrorAlert
from dropbox.client.features.file_provider_migration.constants import FILE_PROVIDER_AUTO_MIGRATION_DAY_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_DEADLINE_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_HOUR_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_MODAL_LAST_DEADLINE_SHOWN_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_MODAL_LAST_SNOOZED_TIME_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_OPT_OUT_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_SCHEDULED_DATE_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_STICKY_MIGRATION_TIME_SHOWN_WHEN_LAST_DISMISSED_CONFIG_KEY, FILE_PROVIDER_AUTO_MIGRATION_TEN_MINUTE_REMINDER_LAST_TIME_SHOWN_CONFIG_KEY, FILE_PROVIDER_MIGRATION_BETA_EXITED_FROM_MOUNTED, FILE_PROVIDER_MIGRATION_LAST_DISMISSED_TIME, FILE_PROVIDER_MIGRATION_NOTIFICATION_LAST_SHOWN_CONFIG_KEY
from dropbox.client.features.file_provider_migration.implementation import DebugEligibilityChecker as FPMigrationDebugEligibilityChecker, FileProviderMigrationController
from dropbox.client.features.file_provider_migration.migration_notifications import DEFAULT_NUM_DAYS_TO_DISMISS
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.types import FileProviderMigrationState
from dropbox.client.features.file_provider_migration.ui.controllers.post_migration_ui_controller import INTERIM_CAROUSEL_VIEW_KEY
from dropbox.client.features.file_provider_migration.ui.controllers.pre_migration_flow import PreMigrationFlowController
from dropbox.client.features.file_requests.ui.menu_actions import create_file_request
from dropbox.client.features.flexible_filenames.consts import FFN_SHOWN_KEY
from dropbox.client.features.flexible_filenames.controller import FlexibleFilenamesController, FlexibleFileNameStickyVariant
from dropbox.client.features.flexible_filenames.gating import save_flexible_filenames_rules
from dropbox.client.features.local_view_basic_example.view_model.bridge_gen.local_view_basic_example_params import BasicRecord, LocalViewBasicExampleParams
from dropbox.client.features.move_to_trash.notification_controller import MoveToTrashNotificationController
from dropbox.client.features.os_consent.os_consent_flow import OSConsentFlow
from dropbox.client.features.sync_and_storage.constants import SyncAndStorageEntryPoint
from dropbox.client.features.sync_and_storage.utils import launch_sync_and_storage_view
from dropbox.client.features.sync_error.controller.sync_error_controller import SyncErrorController
from dropbox.client.features.sync_error.controller.sync_error_notification_controller import SlowSyncErrorStickyVariant, SyncErrorNotificationController
from dropbox.client.features.sync_error.model.sync_error_logger import SyncErrorLogger
from dropbox.client.features.sync_everything.constants import CONFIG_KEY_COMPUTER_BACKUP_FORCED_MIGRATION_PROMPT_TS, CONFIG_KEY_COMPUTER_BACKUP_MIGRATION_SOURCE, CONFIG_KEY_COMPUTER_BACKUP_PRE_MIGRATION_DEVICE_STATE, CONFIG_KEY_SYNC_EVERYTHING_SEEN_MORE_FOLDERS_TOAST, CONFIG_KEY_SYNC_EVERYTHING_STICKY_DISMISSED
from dropbox.client.features.sync_everything.gating import get_known_folders
from dropbox.client.features.sync_everything.v3.api_utils import list_backups
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.delay_injection import DebugDelayManager
from dropbox.client.features.sync_everything.v3.device_state import KnownFolder
from dropbox.client.features.sync_everything.v3.integration_test import SyncEverythingIntegrationTest
from dropbox.client.features.sync_everything.v3.notification_controller import sync_everything_notification_debug_functions
from dropbox.client.features.sync_everything.v3.sync_everything_manager import SyncEverythingManager
from dropbox.client.features.sync_everything.v3.utils import debug_known_folder_locations, fixup_dock, get_highly_problematic_applications, get_problematic_applications
from dropbox.client.features.sync_everything.v3.ux_param_utils import translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_unlimited_storage_modal_actions import BackupUnlimitedStorageModalActions
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.platform_type import PlatformType
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything_carousel.bridge_gen.sync_everything_carousel_nav_params import SyncEverythingCarouselNavParams
from dropbox.client.features.sync_everything_preferences.bridge_gen.sync_everything_preferences_nav_params import SyncEverythingPreferencesNavParams
from dropbox.client.features.tour.ui.bridge_gen.tour_variant import TourVariant
from dropbox.client.features.tour.ui.bridge_gen.tour_variant_nav_params import TourVariantNavParams
from dropbox.client.features.tray_promotion_dialog.constants import TRAY_PROMOTION_ATTEMPTS_PENDING, TRAY_PROMOTION_DIALOG_NEXT_SCHEDULED_TIME, TRAY_PROMOTION_MAX_ATTEMPTS, TRAY_PROMOTION_STATE_CONFIG_KEY, TrayPromotionState
from dropbox.client.features.users.bridge_gen.role import Role as UserRole
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.multiaccount.selector import MultiAccountSelector
from dropbox.client.notifications.constants import BLUENOTE_NOTIFICATION_ID, CURRENT_NOTIFICATIONS_VERSION, GENERIC_TEMPLATE, NEMO_CAMPAIGN_ID
from dropbox.client.notifications.legacy_notifications import LegacyUserNotification, PairedUserNotification
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.notifications.notification_adapter import UserNotificationControllerAdapter
from dropbox.client.notifications.types import NotificationTok, UserNotificationSeenState, UserNotificationStatus
from dropbox.client.presence.model import PresenceInfo, PresenceStatus
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.client.theme_manager.theme_manager import set_theme_setting_to_value
from dropbox.client.theme_manager.types import Theme
from dropbox.client.tray.debug.tray_debug_sub_menu_items.app_shell import get_app_shell_subitems
from dropbox.client.tray.debug.tray_debug_sub_menu_items.basic_oq import get_basic_oq_subitems
from dropbox.client.tray.debug.tray_debug_sub_menu_items.basic_user_to_team import get_basic_user_to_team_subitems
from dropbox.client.tray.debug.tray_debug_sub_menu_items.business_basic import get_business_basic_subitems, launch_business_basic_sharing_onboarding
from dropbox.client.tray.debug.tray_debug_sub_menu_items.cf_migration import get_cf_migration_subitems
from dropbox.client.tray.debug.tray_debug_sub_menu_items.debug_onboarding import get_onboarding_subitems, launch_welcome_flow
from dropbox.client.tray.debug.tray_debug_sub_menu_items.esv_items import get_esv_subitems
from dropbox.client.tray.debug.tray_debug_sub_menu_items.file_info import get_file_info_subitems
from dropbox.client.tray.debug.tray_debug_sub_menu_items.preferences import get_pref_subitems
from dropbox.client.tray.debug.tray_debug_sub_menu_items.sprig import get_sprig_subitems
from dropbox.client.tray.debug.tray_debug_sub_menu_items.tray import get_tray_subitems
from dropbox.client.ui.common.auth_error import show_multiaccount_disabled_alert, show_unlink_failure_dialog
from dropbox.client.ui.common.dialog_constants import IconType
from dropbox.client.ui.common.dialogs import DialogController, NativeDialogController
from dropbox.client.ui.common.dropbox_menu import AfterTrayMenuAction, MenuComponent, MenuItem, Separator, SubMenu
from dropbox.client.ui.common.filesys_no_longer_supported import EndOfSupportFileSystemAlert
from dropbox.client.ui.common.fp_shadow_migration import show_fp_shadow_migration_complete_notification, show_fp_shadow_migration_in_progress_notification, show_fp_shadow_migration_unmigrated_files_notification
from dropbox.client.ui.common.quota_usage_notification_ui import QuotaUsageNotificationUI
from dropbox.client.ui.common.selective_sync_v4 import show_selsync_mev
from dropbox.client.ui.common.tray_feature_checker import DEBUG_SHOW_ALL_IN_TRAY
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason, TrayUpdateOptionsReason
from dropbox.client.ui.common.uikit import BaseUIKit, Closeable, on_ui_thread, on_ui_thread_blocking, on_ui_thread_returns_none
from dropbox.client.users import UserInfo
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exceptions import SuppressedExceptionMixin
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.disk_space_status import DebugDiskSpaceManager, DiskSpaceState, DiskSpaceVariant
from dropbox.foundation.disk_space_status.disk_space_variant import DiskSpaceVariantReason
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import EasyFuture, Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.html_views.bridge.interface import ViewBridgeSerializable
from dropbox.foundation.html_views.common.threading import assert_on_ui_thread
from dropbox.foundation.html_views.electron.electron_dialog_constants import DialogIconType, ElectronDialogCallbackInfo
from dropbox.foundation.html_views.electron.ipc import JSONDict, JSONish
from dropbox.foundation.html_views.electron.managed_electron_view import ManagedElectronView, ManagedElectronViewDefinition
from dropbox.foundation.html_views.local.common.features import LocalViewFeatures
from dropbox.foundation.navigation_service.interface import MachineNavigationManifest, UserNavigationManifest
from dropbox.foundation.navigation_service.manifest_registry import BACKUP_QUOTA_EXEMPT_PICKER, BACKUP_RESTORATIONS_ONBOARDING, BACKUP_SKU_ONBOARDING, BACKUP_UNLIMITED_STORAGE_MODAL, COMPUTER_BACKUP_CUSTOM_FOLDER_PICKER, COMPUTER_BACKUP_SSB_MODAL, DEBUG_BRIDGE_CALL_PROFILER_VIEW, DEBUG_MENU_OVERRIDE_STORMCROW, EXTERNAL_DRIVE_BACKUP_FOLDER_PICKER, EXTERNAL_DRIVE_BACKUP_PERMISSIONS, FP_MIGRATION_EDUCATION_CAROUSEL, FP_MIGRATION_INTERIM_CAROUSEL, LOCAL_VIEW_BASIC_EXAMPLE, SYNC_EVERYTHING_CAROUSEL, SYNC_EVERYTHING_PREFERENCES, TOUR_CAROUSEL
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.harmony.badge.badge_errors import BadgeErrors
from dropbox.harmony.models.harmony_user import HarmonyUser
from dropbox.harmony.utility.constants import BeaconPlatform, HarmonyInteractionStates
from dropbox.i18n import trans
from dropbox.model.types import FileId
from dropbox.nucleus.migration import SyncEngineMigration
from dropbox.nucleus.migration_constants import SyncEngineState
from dropbox.nucleus.migration_state import SyncEngineStateManager
from dropbox.pap.events.enums.export_funnel_pb2 import ExportFunnel
from dropbox.pap.events.enums.file_type_pb2 import FileType
from dropbox.pap.events.video_edit.export_video_project_pb2 import Export_VideoProject
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.proto.nucleus.app_service_pb2 import FlexibleFilenamesConfigReply, FPCutoverDryRunExtraData, UpdateConfigReq
from dropbox.proto.nucleus.device_anchor_pb2 import BreakBackupReason
from dropbox.proto.nucleus.reactive_api_pb2 import MovedToTrash as MovedToTrashProto, MovedToTrashSummary as MovedToTrashSummaryProto
from dropbox.proto.nucleus.sync_engine_pb2 import FlexibleFilenamesConfig, UpdatableAppConfig, UserConfig
from dropbox.proto.pap.event_state_pb2 import EventState
from dropbox.shared.quota_info import QuotaEntityData, QuotaInfo
from dropbox.shared.server_path import MRCasedServerPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.debug_interface import SyncEngineDebugInterface
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockErrorType
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIKextInstallFlowSource
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo, DropboxFolderDiskInfo
from dropbox.sync_engine_boundary.types.backup_sync_progress import SyncProgressForDeviceAnchorSummary
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.sync_root.types import RemovalMode, SyncRootType
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.notifications.controller import UserNotificationController
_P = TypeVar('_P', bound = Optional[ViewBridgeSerializable])

def splash_callback(message = None):
    pass
# WARNING: Decompyle incomplete

test_office_addin_popup_electron_win = (lambda dialog_controller = None: OfficeSplashScreen = OfficeSplashScreenimport dropbox.client.ui.electron.officeOfficeSplashScreen(dialog_controller, splash_callback('Office Add-In: Accept'), splash_callback('Office Add-In: Decline'), splash_callback('Office Add-In: Close')))()

def test_office_addin_popup(dialog_controller = None):
    test_office_addin_popup_electron_win(dialog_controller)


def _mock_mbox_selector():
    selector = MultiAccountSelector('Pick the account you want your photos to sync to:', 'Choose a Dropbox to save to', 'Personal Dropbox', 'Business Dropbox', 'Choose a Dropbox', 'Please pick which Dropbox to use as the destination for all photos from this device.')
    account = Account()
    account.role = Roles.BUSINESS
    account.team = 'ACME LLC'
    AccountString = AccountString
    import dropbox.client.ui.common.strings
    selector.set_disabled(account, AccountString('Camera Uploads have been disabled for <Personal> by the admin.'))
    return selector

test_camera_upload_popup_mac = (lambda dialog_controller = None: get_camera_splash_screen = get_camera_splash_screenimport dropbox.client.ui.cocoa.cameraCameraStrings = CameraStringsimport dropbox.client.ui.common.camera_stringsget_camera_splash_screen(dialog_controller, splash_callback('Camera upload: START'), splash_callback('Camera upload: CANCEL'), splash_callback('Camera upload: NEVER'), CameraStrings.splash_never_ever_button, CameraStrings.splash_import_videos, _mock_mbox_selector(), True, True)get_camera_splash_screen(dialog_controller, splash_callback('Camera upload: START'), splash_callback('Camera upload: CANCEL'), splash_callback('Camera upload: NEVER'), CameraStrings.splash_never_ever_button, CameraStrings.splash_import_videos, _mock_mbox_selector(), False, False))()
test_ptp_warning_message_mac = (lambda dialog_controller = None: show_ptp_warning_splash_screen = show_ptp_warning_splash_screenimport dropbox.client.ui.common.camerashow_ptp_warning_splash_screen(dialog_controller, Device(0), splash_callback('PTP Warning: CANCEL')))()
test_camera_upload_popup_win = (lambda dialog_controller = None: CameraStrings = CameraStringsimport dropbox.client.ui.common.camera_stringsget_splash_dialog = get_splash_dialogimport dropbox.client.ui.win32.cameraget_splash_dialog(dialog_controller, splash_callback('Camera upload: START'), splash_callback('Camera upload: CANCEL'), splash_callback('Camera upload: NEVER'), CameraStrings.splash_never_ever_button, False, CameraStrings.splash_import_videos, True, _mock_mbox_selector()))()

def test_camera_upload_popup(dialog_controller = None):
    if IS_MAC:
        test_camera_upload_popup_mac(dialog_controller)
        return None
    test_camera_upload_popup_win(dialog_controller)


def test_screenshot_popup(dialog_controller = None, use_mock_mbox = None):
    ScreenshotsSplashScreen = ScreenshotsSplashScreen
    import dropbox.client.ui.electron.screenshots
    ScreenshotsSplashScreen(dialog_controller, splash_callback('Screenshot: ALWAYS'), splash_callback('Screenshot: NEVER'), splash_callback('Screenshot: CLOSE'), is_linked = True, mbox_selector = _mock_mbox_selector() if use_mock_mbox else None, confirm_choice_text = {
        'title': 'Confirm choice',
        'message': 'Are you sure?' })


def test_screenshot_selsync_popup(dialog_controller = None):
    ScreenshotsSelsyncSplashScreen = ScreenshotsSelsyncSplashScreen
    import dropbox.client.ui.electron.screenshots
    ScreenshotsSelsyncSplashScreen(dialog_controller, splash_callback('ScreenshotSelSync: TURN OFF SEL SYNC'), splash_callback('ScreenshotSelSync: TURN OFF SCREENSHOTS'), splash_callback('ScreenshotSelSync: CLOSE'))

test_camera_quota_popup = (lambda dialog_controller = None: quota_splash_screen_show = quota_splash_screen_showimport dropbox.client.ui.common.cameraCameraStrings = CameraStringsimport dropbox.client.ui.common.camera_stringscancel_text = CameraStrings.splash_cancel_buttonmessage = CameraStrings.quota_subheading_nosizenodevicequota_splash_screen_show(dialog_controller, splash_callback('Camera upload over quota: UPGRADE'), splash_callback('Camera upload over quota: CANCEL'), cancel_text, None, None, message)quota_splash_screen_show(dialog_controller, splash_callback('Camera upload over quota: UPGRADE'), splash_callback('Camera upload over quota: CANCEL'), cancel_text, splash_callback('Camera upload over quota: NEVER'), CameraStrings.splash_never_ever_button, message))()
test_kext_install_ui = (lambda ui_kit = None, account_manager = None: if not ui_kit:
TRACE('!! No UIKit!')None# WARNING: Decompyle incomplete
)()

class DebugTrayOptionStrings(object):
    launch_local_view_basic_example = 'Launch Local View Basic Example'
    relaunch_lv_basic_example = 'Relaunch Local View Basic Example'
    launch_dropabout = 'Launch Dropabout'
    launch_perf_test = 'Launch Dropabout as Perf Test (120 seconds)'
    launch_previews = 'Launch Previews Demo'
    launch_account_pairing = 'Launch Account Pairing Demo'


def _journey_display_name(journey = None):
    name = journey.name
    if name.endswith('_FLOW'):
        name = name[:-len('_FLOW')]
    return name.replace('_', ' ').title()


class _ElectronViewSections(NamedTuple):
    runtime: 'Sequence[MenuComponent]' = ()
    mev: 'Sequence[MenuComponent]' = ()
    esv: 'Sequence[MenuComponent]' = ()
    sync_and_storage: 'Sequence[MenuComponent]' = ()
    onboarding: 'Sequence[MenuComponent]' = ()
    tray: 'Sequence[MenuComponent]' = ()
    os_integration: 'Sequence[MenuComponent]' = ()
    support: 'Sequence[MenuComponent]' = ()


class TrayDebugMenu(object):
    
    def __init__(self = None, dropbox_app = None, disk_space_manager = None):
        self.dropbox_app = dropbox_app
        self._disk_space_manager = disk_space_manager
        self._debug_menu = None
        self._sample_views = WeakSet()

    _requires_feature = (lambda feature = None, menu_items = None: if feature_enabled(feature):
menu_items)()
    
    def _create_navservice_menu_item(self = None, title = None, manifest = None, parameter = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _create_navservice_primary_user_menu_item(self = None, title = None, manifest = None, parameter = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def create_debug_menu_options(self = None):
        pass
    # WARNING: Decompyle incomplete

    _group = (lambda label = None, sections = None: subitems = []for section in sections:
subitems.extend(section)if not subitems:
[][
SubMenu(label = label, subitems = subitems)])()
    
    def app_and_runtime_group(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def view_frameworks_group(self = None, electron = None):
        return self._group('View Frameworks', [
            electron.runtime,
            electron.mev,
            electron.esv,
            self._group('Dialogs', [
                self.electron_dialog,
                self.native_dialog_menu,
                self.electron_alert_migration_debug_menu,
                self.native_dialog_migration_debug_menu]),
            self.splash_screens,
            self.theme_manager,
            self.low_ui,
            self._group('Local Views (Deprecated)', [
                self.local_views_debug_menu])])

    
    def tray_group(self = None, electron = None):
        return self._group('Tray', [
            self._group('General', [
                self.tray_debug_menu,
                self.promotion_menu]),
            electron.tray])

    backup_group = (lambda self = None: self._group('Backup', [
self.computer_backup_menu,
self.computer_backup_anchors_menu,
self.external_backup_menu,
self.backup_auto_sel_sync_menu,
self.backup_instance_menu]))()
    
    def os_integration_group(self = None, electron = None):
        sections = [
            electron.os_integration,
            self.system_event_testing_menu,
            self.external_context_menu_sharing_debug_menu]
        if IS_MAC:
            sections.append(self.open_preferenes_window)
        if IS_WINDOWS:
            sections.append(self.browser_launcher_debug_menu)
            sections.append(self.windows_theme_debug_menu)
        return self._group('OS Integration', sections)

    
    def support_and_diagnostics_group(self = None, electron = None):
        return self._group('Support Diagnostics', [
            self.cx_support_tool,
            electron.support])

    ss_removal_mitigation_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    promotion_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    dod_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    splash_screens = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    local_views_debug_menu = (lambda self = None: if not LocalViewFeatures.is_feature_only_enabled():
[]context = Nonerole = Roles.BUSINESStry:
context = self._get_user_context()backups = None if context and context.account.role else list_backups('debug', context, Source.DEBUG).block().result().backups_list if context else []enabled_backups = backups()platform_type = PlatformType.MAC if IS_MAC else PlatformType.WINlocal_views_demos_menu_subitems = (self._create_navservice_primary_user_menu_item(DebugTrayOptionStrings.launch_local_view_basic_example, LOCAL_VIEW_BASIC_EXAMPLE, LocalViewBasicExampleParams(name = 'Test Param', color = 'red', child_record = BasicRecord(name = 'Test Basic Record Name'))), self._create_navservice_primary_user_menu_item(DebugTrayOptionStrings.relaunch_lv_basic_example, LOCAL_VIEW_BASIC_EXAMPLE, parameter = LocalViewBasicExampleParams(name = 'Test Param', color = 'blue', child_record = BasicRecord(name = 'Test Re-nav Record Name'))), self._create_navservice_primary_user_menu_item('Backup Quota Exempt Picker', BACKUP_QUOTA_EXEMPT_PICKER, parameter = BackupQuotaExemptPickerNavParams(session_logging_id = 'debug_id', source = Source.DEBUG)), self._create_navservice_primary_user_menu_item('Backup SKU Onboarding', BACKUP_SKU_ONBOARDING, parameter = BackupSkuOnboardingNavParams(session_logging_id = 'debug_id', backups = enabled_backups, source = Source.DEBUG)), self._create_navservice_menu_item('Computer Backup Carousel', SYNC_EVERYTHING_CAROUSEL, parameter = SyncEverythingCarouselNavParams(source = Source.DEBUG, ignored_paths = { })), self._create_navservice_menu_item('External Drive Backup Permissions', EXTERNAL_DRIVE_BACKUP_PERMISSIONS, parameter = ExternalDriveBackupPermissionsNavParams(drive_info = DriveInfo(id = '0', name = 'debug_hdd', mount_path = 'test/debug', current_usage = 4.75668e+10, current_capacity = '128', fs_type = 'NTFS', is_writable = True, is_remote = False), session_logging_id = 'logging_id_debug', source = EdbSource.DEBUG)), self._create_navservice_menu_item('External Drive Backup Folder Picker', EXTERNAL_DRIVE_BACKUP_FOLDER_PICKER, parameter = ExternalDriveBackupFolderPickerParams(session_logging_id = 'logging_id_debug', role = translate_role(role), root_path = 'test/debug', source = EdbSource.DEBUG, drive_info = DriveInfo(id = '0', name = 'debug_hdd', mount_path = 'test/debug', current_usage = 4.75668e+10, current_capacity = '128', fs_type = 'NTFS', is_writable = True, is_remote = False))), self._create_navservice_menu_item('Computer Backup Custom Folder Picker', COMPUTER_BACKUP_CUSTOM_FOLDER_PICKER, parameter = ComputerBackupCustomFolderPickerParams(session_logging_id = 'logging_id_debug', role = translate_role(role), root_path = os.path.expanduser('~'), source = Source.DEBUG, ignored_paths = { }, selected_folders = None, backup_info = BackupInfo(device_id = 'debug_id_0', device_status = DeviceSyncStatus.ENABLED, name = 'Test Computer Backup Anchor', quota_exempt = False, device_backup_platform = platform_type, folders = [
'DESKTOP',
'DOCUMENTS',
'DOWNLOADS'], anchor_folders = [], last_timestamp_utc = 0x5CD111C085700))), self._create_navservice_menu_item('Backup Restorations Onboarding Carousel', BACKUP_RESTORATIONS_ONBOARDING, parameter = BackupRestorationsOnboardingNavParams(session_logging_id = 'logging_id_debug', eligible_roles = {
'PERSONAL': 'Personal Dropbox',
'BUSINESS': 'Acme Dropbox' }, eligible_backups = [
EligibleBackups(role = 'PERSONAL', backups = [
BackupInfo(device_id = 'debug_id_0', device_status = DeviceSyncStatus.ENABLED, name = 'debug_name', quota_exempt = False, device_backup_platform = platform_type, folders = [
'DESKTOP'], last_timestamp_utc = 0x5CD111C085700),
BackupInfo(device_id = 'debug_id_1', device_status = DeviceSyncStatus.ENABLED, name = 'debug_name (1)', quota_exempt = False, device_backup_platform = platform_type, folders = [
'DOCUMENTS',
'PICTURES'], last_timestamp_utc = 0x5CC2847634700)]),
EligibleBackups(role = 'BUSINESS', backups = [
BackupInfo(device_id = 'debug_id_2', device_status = DeviceSyncStatus.ENABLED, name = 'debug_name (2)', quota_exempt = False, device_backup_platform = platform_type, folders = [
'DOCUMENTS',
'DOWNLOADS'], last_timestamp_utc = 0x5CC3F8FDA2F00),
BackupInfo(device_id = 'debug_id_3', device_status = DeviceSyncStatus.ENABLED, name = 'debug_name (3)', quota_exempt = False, device_backup_platform = platform_type, folders = [
'PICTURES'], last_timestamp_utc = 0x5CB854C22EF00)])], source = Source.DEBUG, show_cb_onboarding_restoration = False, home_path = os.path.expanduser('~'))), self._create_navservice_menu_item('Backup Unlimited Storage Modal', BACKUP_UNLIMITED_STORAGE_MODAL, parameter = BackupUnlimitedStorageModalNavParams(session_logging_id = 'logging_id_debug', action = BackupUnlimitedStorageModalActions.ERROR, device_name = 'mac', role = UserRole.PERSONAL, selected_backup = BackupInfo(device_id = 'C02GC0VQMD6V', device_status = DeviceSyncStatus.ENABLED, name = 'debug_name (3)', quota_exempt = False, device_backup_platform = platform_type, folders = [
'PICTURES'], last_timestamp_utc = 0x5CB854C22EF00))), self._create_navservice_menu_item('Computer Backup Preferences', SYNC_EVERYTHING_PREFERENCES, parameter = SyncEverythingPreferencesNavParams(source = Source.DEBUG)), self._create_navservice_menu_item('Computer Backup SSB Modal', COMPUTER_BACKUP_SSB_MODAL))local_views_debug_menu_subitems = (self._create_navservice_menu_item('HTML Bridge Calls', DEBUG_BRIDGE_CALL_PROFILER_VIEW),)[
SubMenu(label = 'Demos', subitems = local_views_demos_menu_subitems),
SubMenu(label = 'Debug Tools', subitems = local_views_debug_menu_subitems)])()
    electron_view_sections = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    native_dialog_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    electron_alert_migration_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    native_dialog_migration_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _create_bolt_stormcrow_menu(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _create_flexible_filenames_menu(self = None, adapter = None, account = None, local_config = ('adapter', 'SyncEngineAdapter', 'account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'return', 'List[MenuComponent]')):
        pass
    # WARNING: Decompyle incomplete

    nucleus_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    file_provider_simulation_menu = (lambda self = None: menu_items = self.file_provider_simulation_menu_delay_submenumenu_items.extend(self.modern_client_api_submenu)(lambda .0: [ MenuItem(n, v) for n, v in .0 ])(SyncEngineDebugInterface.debug_menu_commands().items()())
        return [
            SubMenu(label = 'Modern Client Debug', subitems = menu_items)]
)()
    modern_client_api_submenu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    file_provider_simulation_menu_delay_submenu = (lambda self = None: menu_items = SyncEngineDebugInterface.debug_menu_delay_commands().items()()[
SubMenu(label = 'Start ThinClient delay', subitems = menu_items)])()
    file_provider_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    update_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    notifications_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    harmony_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    electron_dialog = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    external_context_menu_sharing_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    low_ui = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    theme_manager = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    tray_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _override_stormcrow(self = None, stormcrow = None, variant = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _switch_tray_gates(self = None, rule_overrides = None, toggle = None):
        for stormcrow, variant in rule_overrides.items():
            if toggle:
                if variant == 'OFF':
                    variant = 'ON'
                elif variant == 'ON':
                    variant = 'OFF'
            self._override_stormcrow(stormcrow, variant)
            return None

    
    def _toggle_pinned(self = None):
        pass
    # WARNING: Decompyle incomplete

    _is_tray_pinned = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _close_tray(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _close_and_open_tray(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_fetch_params(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_user_context(self = None):
        
        try:
            (_, user_context) = self._get_fetch_params()
            return user_context
        except Exception:
            e = None
            TRACE('_get_user_context exception %r', e)
            e = None
            del e
            return None
            e = None
            del e


    sync_root_debug_menu = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _debug_root_manager_simulate_grant_permission(self = None, account = None):
        if account:
            self.dropbox_app.root_manager.debug_set_consent(account, True)
            return None
        None.dropbox_app.root_manager.debug_grant_all_consent()

    
    def _trigger_consent_flow(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _send_fp_domain_change_notification(self = None):
        if IS_MAC:
            NSFileProviderDomainDidChange = NSFileProviderDomainDidChange
            import FileProvider
            NSNotificationCenter = NSNotificationCenter
            import Foundation
            NSNotificationCenter.defaultCenter().postNotificationName_(NSFileProviderDomainDidChange)
            return None

    auto_restart_debug_menu = (lambda self = None: [
SubMenu(label = 'Auto Restart', subitems = (MenuItem('Test CPR restart notification', self.test_cpr_restart_notification), MenuItem('Test CPR hit limit notification', self.test_cpr_hit_limit_notification), MenuItem('Clear autorestart attempts', self.clear_autorestart_attempts_from_config)))])()
    auto_update_failure_debug_menu = (lambda self = None: auto_update_failure_menu = SubMenu(label = 'Auto Update Failure Messaging', subitems = (MenuItem('Set Disk State Fine V1', self._set_disk_state_healthy_v1), MenuItem('Set Disk State Low V1', self._set_disk_state_low_v1), MenuItem('Set Disk State Full V1', self._set_disk_state_full_v1), MenuItem('Set Disk State Fine V2', self._set_disk_state_healthy_v2), MenuItem('Set Disk State Low V2', self._set_disk_state_low_v2), MenuItem('Set Disk State Full V2', self._set_disk_state_full_v2), MenuItem('Set Disk State Full V2 + SelSync', self._set_disk_state_selsync_v2), MenuItem('Set Disk State Low V1 + Manage Space', self._set_disk_state_manage_space_v1), MenuItem('Set Disk State Full V1 + Manage Space', self._set_disk_state_manage_space_v1_full), MenuItem('Set Disk State Low V2 + Manage Space', self._set_disk_state_manage_space_v2), MenuItem('Set Disk State Full V2 + Manage Space', self._set_disk_state_manage_space_v2_full), MenuItem('Set Disk State Full V2 + Manage Space + SelSync', self._set_disk_state_manage_space_selsync_v2_full), MenuItem('reset', self._reset_disk_state), MenuItem('Enforce disk state check', self._enforce_disk_state_check)))[
auto_update_failure_menu])()
    
    def test_send_many_notifs(self = None):
        self.test_bluenote_quote()
        self.test_bluenote_task()
        self.test_bluenote_thumbnail()
        self.test_bluenote_avatar()
        self.test_bluenote_multiple_actions()
        self.test_bluenote_open_file()
        self.test_bluenote_open_folder()
        self.test_bluenote_open_preferences()
        self.test_bluenote_open_standalone_server_view()
        self.test_bluenote_open_tray()
        self.test_bluenote_open_url()
        self.test_bluenote_xml_unfriendly()

    
    def test_long_notification(self = None):
        controller = UserNotificationControllerAdapter.instance().get_primary_controller()
        if not controller:
            return None
        surface_action = {
            'action_name': None,
            'params': {
                'url_path': 'test' } }
        message = "It's clear that our business deliverables and KPI synergies are at risk if\n                we do not action enough product-market fit before the quarterly MVP earnings review. Can you engage\n                your stakeholders and get user and dev QA-PM buy-in to set expectations on our company mission and\n                earnings engagement retention clickthrough metrics, in case we have to engage fallback strategy\n                documentation review contingencies? "
        notif = self._create_bluenote_notification(controller, identifier = 75, surface_action = surface_action, message = message)
        controller.on_received_notifications([
            notif])

    
    def _create_bluenote_notification(self, controller, identifier, surface_action, button_actions, image, title, message = None, preview = None, notification_object = None, loud_is_persistent = (None, None, None, None, None, None, None, False, None), preference_bucket = ('controller', 'UserNotificationController', 'identifier', 'int', 'surface_action', 'Optional[Dict[str, Any]]', 'button_actions', 'Optional[List[Dict[str, Any]]]', 'image', 'Optional[Dict[str, Any]]', 'title', 'Optional[str]', 'message', 'Optional[str]', 'preview', 'Optional[Dict[str, Any]]', 'notification_object', 'Optional[Dict[str, Any]]', 'loud_is_persistent', 'bool', 'preference_bucket', 'Optional[Text]', 'return', 'Dict[Text, Any]')):
        if not button_actions:
            button_actions = []
        return {
            'nid': max(controller._nid, controller._popup_nid) + 1,
            'type_id': BLUENOTE_NOTIFICATION_ID,
            'target_object_key': str(controller._uid + identifier),
            'payload': {
                'json_data': json.dumps({
                    'object': notification_object,
                    'desktop': {
                        'payload': {
                            'template_type': GENERIC_TEMPLATE,
                            'template_version': CURRENT_NOTIFICATIONS_VERSION,
                            'home_params': {
                                'message': 'Test message here! Click me' if not message else message },
                            'loud_params': {
                                'message': 'Test loud message! Click me' if not message else 'Loud: ' + message,
                                'title': 'Test loud title' if not title else title,
                                'is_persistent': loud_is_persistent },
                            'preview': preview,
                            'surface_action': surface_action,
                            'button_actions': button_actions,
                            'image': image,
                            'notification_preferences_bucket': preference_bucket },
                        'campaign_info': {
                            'campaignId': 1234,
                            'versionId': 1234 } } }) },
            'status': UserNotificationStatus.UNREAD.value,
            'seen_state': UserNotificationSeenState.UNSEEN.value,
            'feed_time': time.time() }

    
    def _create_test_bluenote_quote_notif(self = None, identifier = None):
        controller = UserNotificationControllerAdapter.instance().get_primary_controller()
        if not controller:
            return { }
        surface_action = {
            'action_name': None,
            'params': {
                'url_path': 'test' } }
        preview = {
            'quote': "This is a test quote and I'm going to say a lot of things about this doc very cool. Just for fun though I'm going to say a lot so the quote is really long and it takes a while to readand fills up a ton of space." }
        return self._create_bluenote_notification(controller, identifier = identifier, surface_action = surface_action, message = 'Angela Gong commented on foo.bar', preview = preview)

    
    def test_notifs_batch(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def test_bluenote_quote(self = None):
        controller = UserNotificationControllerAdapter.instance().get_primary_controller()
        if not controller:
            return None
        None.on_received_notifications([
            self._create_test_bluenote_quote_notif(100)])

    
    def test_bluenote_task(self = None):
        controller = UserNotificationControllerAdapter.instance().get_primary_controller()
        if not controller:
            return None
        surface_action = {
            'action_name': None,
            'params': {
                'url_path': 'test' } }
        preview = {
            'tasks': {
                'tasks': [
                    {
                        'id': '',
                        'name': 'Finish all the debug menu items',
                        'is_complete': True }],
                'task_endpoint': '' } }
        notification = self._create_bluenote_notification(controller, identifier = 99, surface_action = surface_action, message = 'Donald Trump completed 1 task in First 100 Days of Presidency', preview = preview)
        controller.on_received_notifications([
            notification])

    
    def test_bluenote_thumbnail(self = None):
        controller = UserNotificationControllerAdapter.instance().get_primary_controller()
        if not controller:
            return None
        surface_action = {
            'action_name': None,
            'params': {
                'url_path': 'test' } }
        preview = {
            'show_thumbnail': True,
            'quote': 'Make sure you read through this doc quickly' }
        notification_object = {
            'name': 'test.pdf',
            'url': '',
            'ignore': False,
            'thumbnail_url': '',
            'type': 'dropbox-file',
            'id': '1234' }
        notification = self._create_bluenote_notification(controller, identifier = 98, surface_action = surface_action, message = 'Click to open a folder', preview = preview, notification_object = notification_object)
        controller.on_received_notifications([
            notification])

    
    def test_three_notifs(self = None):
        self.test_bluenote_open_folder()
        self.test_bluenote_open_file()
        self.test_bluenote_open_preferences()

    
    def test_bluenote_open_folder(self = None):
        controller = UserNotificationControllerAdapter.instance().get_primary_controller()
        if not controller:
            return None
        surface_action = {
            'action_name': None,
            'params': {
                'server_path': '2:/',
                'backup_url_path': 'home' } }
        notification = self._create_bluenote_notification(controller, identifier = 97, surface_action = surface_action, message = 'Click to open a folder')
        controller.on_received_notifications([
            notification])

    
    def test_bluenote_open_file(self = None):
        controller = UserNotificationControllerAdapter.instance().get_primary_controller()
        if not controller:
            return None
        button_actions = [
            {
                'action_name': None,
                'label': 'Open File',
                'params': {
                    '