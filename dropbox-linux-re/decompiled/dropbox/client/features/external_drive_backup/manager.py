# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

from collections import deque
from datetime import datetime, timezone
from functools import partial
from typing import Any, Callable, cast, Deque, Dict, List, Optional, Set, Text, Tuple
from build_number.platform import IS_MAC
from dropbox.api.v2.datatypes.device_sync import PingServerArg, PingServerResult
from dropbox.api.v2.datatypes.external_drive_backup import CreateBackupWithBackupRootInfo
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.camera_upload.configuration_manager import CameraConfigurationManager
from dropbox.client.features.backup_app.bridge_gen.backup_app_nav_params import BackupAppNavParams
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_schedule import BackupSchedule as BackupScheduleResult, ScheduleDetail as ScheduleDetailResult, ScheduleType as ScheduleTypeResult
from dropbox.client.features.backup_auto_selsync.bi_auto_selsync_manager import BackupAutoSelSyncManager
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, LifetimeReporter, random_session_id
from dropbox.client.features.backup_common.base_manager import BaseBackupManager
from dropbox.client.features.backup_common.scheduling import BackupSchedule, ScheduleType
from dropbox.client.features.backup_common.utils import _Status
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.backup_instance.utils import is_regular_engine_on_fp
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.desktop_rtt_client.rtt_client import DesktopRTTClient
from dropbox.client.features.external_drive_backup.api_utils import start_ncct_trial
from dropbox.client.features.external_drive_backup.constants import ADMIN_POLICY_REFRESH_DELAY_SEC, BUSINESS_ROLE, EDB_ANCHOR_INVARIANT_CHECK_INTERVAL_DEFAULT, EDB_IC_WAIT_AFTER_SETUP_SEC, EDB_PERIODIC_USAGE_REPORTER_DEFAULT, EDB_SEAMLESS_MIGRATION_LONG_POLL_INTERVAL, EdbCustomFoldersVariant, EdbOnboardingUpsellVariant, ExternalDriveArrivalEvent, ExternalDriveBackupUIStrings, LINK_UNLINK_DROPBOX_ACCOUNTS_URL, MAX_PAUSED_PROMPT, PING_SERVER_NUM_ATTEMPTS, RETRY_DELAY_BASE_SECOND
from dropbox.client.features.external_drive_backup.controller import ExternalBackupController
from dropbox.client.features.external_drive_backup.cu_edb_chooser import EDBContextMenuGating, OnboardingSuppressionReasons, suppress_edb_onboarding
from dropbox.client.features.external_drive_backup.drive_events_controller import ExternalDriveEventsController
from dropbox.client.features.external_drive_backup.edb_in_memory_tracker import EDBInMemoryTracker
from dropbox.client.features.external_drive_backup.errors import convert_to_failure, EdbFissionMigrationNeeded, RequestAssertion, RequestFailedException
from dropbox.client.features.external_drive_backup.event_reporter import ManagerBoundaryEventReporter
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger as Logger, ExternalBackupResearchEvent
from dropbox.client.features.external_drive_backup.fission_migration_info import FissionMigrationDictType as BasicFissionMigrationDictType, FissionMigrationInfo as BasicFissionMigrationInfo, FissionMigrationStatus as BasicFissionMigrationStatus, FissionPostMigrationChoice as BasicFissionPostMigrationChoice, SeamlessFissionMigrationInfo, SeamlessFissionMigrationState
from dropbox.client.features.external_drive_backup.gating import edb_platform_drive_types, ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.onboarding import show_external_drive_backup_folder_picker, show_external_drive_backup_permissions
from dropbox.client.features.external_drive_backup.operations import SeamlessMigrationOperation
from dropbox.client.features.external_drive_backup.seamless_migration_controller import SeamlessMigrationController
from dropbox.client.features.external_drive_backup.seamless_migration_scheduler import SeamlessMigrationScheduler
from dropbox.client.features.external_drive_backup.seamless_migration_state_machine import SeamlessMigrationStateMachineWrapper
from dropbox.client.features.external_drive_backup.server_interface import catch_and_convert_network_exceptions
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.types import DeviceAnchorMigrationInfo, SeparatedAnchorsByEngineAndState, SeparatedAnchorsByState
from dropbox.client.features.external_drive_backup.utils import drive_info_to_extra_dict, get_number_of_migrating_drives, is_overquota_upsell, list_anchors_by_uuid_active_engine, list_anchors_by_uuid_both_engines, migration_info_to_extra_dict, seamless_mig_info_to_extra_dict, try_get_device_anchor_mig_info_from_std_da, try_get_device_info_capacity, try_get_status_from_basic_mig_info, validate_device_anchor_target, wrap_generic_func_with_retries
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_action_surface import EdbActionSurface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.external_drive_backup_folder_picker.bridge_gen.external_drive_backup_folder_picker_params import ExternalDriveBackupFolderPickerParams
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function
from dropbox.client.features.sync_everything.v3.url_utils import open_backup_all_on_web
from dropbox.client.features.sync_everything.v3.utils import is_offline, wait_for_fully_synced
from dropbox.client.features.sync_everything.v3.ux_param_utils import get_roles_dict, translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.notifications.legacy_notifications import ExternalDriveBackupLocalConflictStickyNotification
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.client_api.apiv2.generated import device_sync
from dropbox.client_api.connection.exceptions import APIv2EndpointError
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.client_api.exceptions import HTTP401Error, HTTP429Error, TransientNetworkError
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import assert_not_none, report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.environment import is_integration_tests
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface, ViewHandle
from dropbox.foundation.navigation_service.manifest_registry import BACKUP_APP, EXTERNAL_DRIVE_BACKUP_FOLDER_PICKER
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.signals import RepeatedEventSignal, Signal, StandardSignal
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.model.types import FileId
from dropbox.platform import IS_WINDOWS
from dropbox.proto.growth_platform.rtt.triggers_pb2 import DesktopUserActionType
from dropbox.proto.nucleus.device_anchor_pb2 import BreakBackupReason
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo, DeviceAnchorState
from dropbox.url_info import dropbox_url_info
if IS_WINDOWS:
    from dropbox.client.features.external_drive_backup.disk_arbitration.windows import build_drive_info
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, VENTURA
    IS_VENTURA_OR_LATER = MAC_VERSION >= VENTURA
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
ControllerArc = Arc[ExternalBackupController]
MigrationControllerArc = Arc[SeamlessMigrationController]
_UpdateAction = Callable[([], Future[BackupResult])]
_SuccessAction = Callable[([], Future[None])]
_UpdateQueueItem = Tuple[(_UpdateAction, EventReporter, EasyFuture[BackupResult])]

class _TrialModalState:
    
    def __init__(self = None, variant = None, succeeded = None):
        self.variant = variant
        self.succeeded = succeeded



def ExternalBackupManager():
    '''ExternalBackupManager'''
    pass
# WARNING: Decompyle incomplete

ExternalBackupManager = <NODE:27>(ExternalBackupManager, 'ExternalBackupManager', BaseBackupManager[ExternalBackupController])
