# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

from datetime import datetime, timezone
from functools import partial
from operator import attrgetter
from typing import Any, Callable, Dict, List, Mapping, Optional, Set, Text, Tuple
from build_number.platform import IS_MAC, IS_WINDOWS
from types import SeparatedAnchorsByEngineAndState
from dropbox.api.v2.datatypes.external_drive_backup import CreateBackupWithBackupRootInfo, ExternalDriveBackupStateEnum, ExternalDriveEntry, ListBackupsResult
from dropbox.api.v2.datatypes.files import DeleteResult
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.apollo_alerts.model.apollo_alerts import AlertResult, ApolloAlerts
from dropbox.client.features.backup_app.view_model.bridge_gen.schedule_type import ScheduleType
from dropbox.client.features.backup_common.base_event_reporter import LifetimeReporter, random_session_id
from dropbox.client.features.backup_common.errors import report_exception_and_ignore
from dropbox.client.features.backup_common.metric_sampler import MetricSampler
from dropbox.client.features.backup_common.scheduling import BackupSchedule, BackupScheduler
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.backup_instance.types import BackupInstance
from dropbox.client.features.external_drive_backup.constants import DISABLED_EDB_STATE_ENUMS, EDB_ONE_QUOTA_EXEMPT_IC_RUN_NAME, EdbHiveAnchorState, ExternalDriveArrivalEvent, ExternalDriveBackupUIStrings, MAX_DESTROY_BLOCKING_TIME_SEC, SeamlessFissionMigrationVariant, VALID_ANCHOR_STATES
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.edb_progress_tracker import EDBProgressTracker
from dropbox.client.features.external_drive_backup.errors import EDBICRecoveryAction, EDBICRecoveryActionType, RequestFailedException
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventReporter
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger as Logger
from dropbox.client.features.external_drive_backup.fully_synced_tracker import FirstSyncLoggingData, FullySyncedTracker
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.operations import CustomFolderUpdateSelectionsOperation, DeleteDeviceAnchorOperation, Operation, PauseBackupOperation, RemediateBackupOperation, RenameBackupOperation, ResumeBackupOperation, SeamlessMigrationOperation, StartBackupOperation
from dropbox.client.features.external_drive_backup.seamless_migration_state_machine import SeamlessMigrationStateMachineWrapper
from dropbox.client.features.external_drive_backup.server_interface import catch_and_convert_network_exceptions, ServerInterface
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE, EDB_WARN
from dropbox.client.features.external_drive_backup.utils import drive_info_to_extra_dict, has_been_one_hour, list_anchors_by_uuid_both_engines, strip_apiv2_id_prefix, strip_device_anchor_extension
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_action_surface import EdbActionSurface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.constants import CONTROLLER_START_UP_TIMEOUT, FIFTEEN_MINUTES_AS_SECONDS
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function, future_sequence, if_none
from dropbox.client.features.sync_everything.v3.utils import _is_paused, AggregateNucleusStats, get_nucleus_aggregate_stats, is_offline, wait_for_fully_synced
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationType
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_unexpected_none
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.navigation_service.interface import ViewHandle
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.types.ids import FileID
from dropbox.fsutil import FileSystem
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DeviceAnchorInfo, DeviceAnchorState, DeviceAnchorTargetType, DeviceAnchorUnbindInfo, DeviceAnchorUnbindReason, ErredDeviceAnchorInfo, HangReason, ListDeviceAnchorsResult, OneWaySyncRemediationInfo
from dropbox.sync_engine_boundary.types.remote_props import RemoteLocationProperties
from dropbox.url_info import dropbox_url_info
if IS_WINDOWS:
    from disk_arbitration.windows import build_drive_info
if IS_MAC:
    from disk_arbitration.mac import build_drive_info
UnbindAlertCallback = Callable[([
    UserContext,
    Optional[DriveInfo],
    str], Future[None])]
ShowCFSCallback = Callable[([
    UserContext,
    DriveInfo,
    str,
    EdbSource,
    Optional[str],
    Optional[List[str]],
    Optional[bool]], Future[Optional[ViewHandle]])]
MigrationAbortCallback = Callable[([
    FileId], Future[BackupResult])]

class ExternalBackupController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

