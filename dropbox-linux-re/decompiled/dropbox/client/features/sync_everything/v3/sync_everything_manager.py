# Source Generated with Decompyle++
# File: sync_everything_manager.pyc (Python 3.11)

from collections import deque
from datetime import datetime, timezone
from enum import auto, Enum
from functools import partial
from typing import Any, Callable, cast, Deque, Dict, List, Mapping, Optional, Set, Text, Tuple
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.role_change_handler import RoleChangeHandler
from dropbox.client.authentication.types import AccountId
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, LifetimeReporter, random_session_id
from dropbox.client.features.backup_common.errors import report_and_trace_transient_network_errors, report_exception_and_ignore
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_accounts
from dropbox.client.features.computer_backup.constants import CBFolderId
from dropbox.client.features.external_drive_backup.edb_in_memory_tracker import EDBInMemoryTracker
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.utils import list_anchors_for_se_accounts
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.state_machine import ReadOnlyStateMachine as FPStateMachine
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.constants import ADMIN_POLICY_REFRESH_DELAY_SEC, BackupDisableType, CBOA_FORCED_MIGRATION_MAX_PROMPTS, CBOA_FORCED_MIGRATION_PROMPTS_ROLLING_WINDOW_DAYS, CONFIG_KEY_SHADOW_MIGRATION_CBOS_REBIND_DONE, DeviceStatus, FIFTEEN_MINUTES_AS_SECONDS, FOLDER_RESTORE_DELAY_SEC, InvariantCheckMode, KnownFolderRequest, MAX_FOLDER_RESTORE_ATTEMPTS, MoreFoldersToastType, REMOTE_ACCOUNT_DELETE_TIMEOUT, ROLE_CHANGE_TIMEOUT, SYNC_EVERYTHING_EXPLORER_AUTO_REBIND_KILLSWITCH_NAME, SYNC_EVERYTHING_INVARIANT_INTERVAL_DEFAULT, SYNC_EVERYTHING_INVARIANT_RUNS_FOR_CHECK_QUOTA_EXEMPT, SYNC_EVERYTHING_METRICS_REPORT_INTERVAL_DEFAULT, SYNC_EVERYTHING_USAGE_REPORT_INTERVAL_DEFAULT
from dropbox.client.features.sync_everything.gating import BackupSkuModalFeature, SyncEverythingFeature
from dropbox.client.features.sync_everything.nav_service import show_backup_app, show_backup_restorations_onboarding, show_backup_sku_modal, show_backup_sku_onboarding, show_sync_everything_onboarding, show_sync_everything_preferences
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.api_utils import force_disable_other_backups, get_device_state, list_backups
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function, if_none, safe_value_to_future
from dropbox.client.features.sync_everything.v3.config_utils import se_active_device_folders, se_active_device_name, se_is_active, se_is_active_account
from dropbox.client.features.sync_everything.v3.device_state import DeviceState, KnownFolder
from dropbox.client.features.sync_everything.v3.errors import ICRecoveryAction, MetricReporterAssertion, RecoveryActionType, RequestAssertion, RequestFailedException, ServerMismatchResult
from dropbox.client.features.sync_everything.v3.event_reporter import ManagerBoundaryEventReporter, OperationEventReporter, SyncEverythingEventReporter
from dropbox.client.features.sync_everything.v3.fs_utils import get_os_folder_root_file_count
from dropbox.client.features.sync_everything.v3.fully_synced_tracker import FirstSyncLoggingData, FullySyncedTracker
from dropbox.client.features.sync_everything.v3.ic_backoff import ICBackoffController
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE, SE_WARN
from dropbox.client.features.sync_everything.v3.notification_controller import SyncEverythingNotifier
from dropbox.client.features.sync_everything.v3.operations import EnableSanityOperation
from dropbox.client.features.sync_everything.v3.os_folder_state import FolderGroup, FolderLocationType, OSFolderInterface, OSFolderState
from dropbox.client.features.sync_everything.v3.role_change_auto_rebind_data import RoleChangeAutoRebindData
from dropbox.client.features.sync_everything.v3.role_change_notification import notify_role_change_intent
from dropbox.client.features.sync_everything.v3.server_interface import catch_and_convert_network_exceptions_send_email, DeviceNotFoundError, DeviceStatusError, EmailType, parse_apiv2_error, ServerInterface
from dropbox.client.features.sync_everything.v3.sync_engine_monitor import SyncEngineMonitor
from dropbox.client.features.sync_everything.v3.sync_everything_controller import SyncEverythingController
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingErrorName, SyncEverythingEvent, SyncEverythingLogger, SyncEverythingUnlinkType, SyncEverythingUsage
from dropbox.client.features.sync_everything.v3.url_utils import open_server_folder
from dropbox.client.features.sync_everything.v3.utils import AggregateNucleusStats, FolderUpdateCallback, FolderUpdateHandler, get_dropbox_usage, get_os_folder_nucleus_stats, is_offline, OSFolderNucleusStats, RestoreEvent, wait_for_fully_synced, while_unpaused, wrap_with_retries
from dropbox.client.features.sync_everything.v3.ux_param_utils import get_backups_dict, get_roles_dict
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.constants import ACTION_SURFACE_MAP
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult, OperationResultData
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType
from dropbox.client.ui.common.sync_everything_strings import SyncEverythingStrings
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.client_api.exceptions import DropboxResponseClientError, DropboxResponseServerError, DropboxServerError, HTTP401Error, HTTP409Error, HTTP429Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate
from dropbox.foundation.account_manager.bridge_gen.account_update_type import AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context import ContextInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.infinite import is_user_running_cloud_files
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DeleteSuppressRestoredInfo, DeviceAnchorInfo, DeviceAnchorState, DropboxFolderDiskInfo
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def _return_ok_op(_ = None):
    return ResolvedFuture(RedirectStatus(RedirectRequestStatus.OK))


class SERoleChangeWrapper:
    
    def __init__(self = None, role_change_handler = None):
        self._role_change_handler = role_change_handler
        if not self._role_change_handler:
            report_bad_assumption('Null role change handler supplied', component = DesktopComponent.SYNC_EVERYTHING)
        self._registered = False
        self._on_change = None

    
    def register(self = None, on_change = None):
        if self._role_change_handler:
            self._on_change = on_change
            self._role_change_handler.add_role_change_callback(on_change)
            self._registered = True
            return None

    
    def deregister(self = None):
        if self._registered and self._role_change_handler and self._on_change:
            self._role_change_handler.remove_role_change_callback(self._on_change)
        self._registered = False
        self._on_change = None



class _Status(Enum):
    WAITING_FP = auto()
    WAITING_FOR_START = auto()
    WAIT_FOR_SYNC_ENGINES = auto()
    EARLY_START = auto()
    READY_TO_START = auto()
    STARTING = auto()
    UPDATING = auto()
    READY = auto()
    
    def valid_transition(self = None, next_status = None):
        allowed_transitions = [
            (_Status.WAITING_FP, _Status.WAITING_FOR_START),
            (_Status.WAITING_FOR_START, _Status.WAIT_FOR_SYNC_ENGINES),
            (_Status.WAIT_FOR_SYNC_ENGINES, _Status.EARLY_START),
            (_Status.EARLY_START, _Status.READY_TO_START),
            (_Status.READY_TO_START, _Status.STARTING),
            (_Status.STARTING, _Status.READY),
            (_Status.READY, _Status.UPDATING),
            (_Status.UPDATING, _Status.READY)]
        return (self, next_status) in allowed_transitions


_UpdateAction = Callable[([], OperationResult)]
_UsageInfo = Tuple[(Optional[DropboxFolderDiskInfo], Dict[(OSFolderID, int)], Dict[(OSFolderID, OSFolderNucleusStats)])]

class SyncEverythingManager(SingletonActor):
    pass
# WARNING: Decompyle incomplete

