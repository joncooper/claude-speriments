# Source Generated with Decompyle++
# File: seamless_migration_controller.pyc (Python 3.11)

import functools
from typing import Any, Callable, Dict, List, Optional, Tuple, TypeVar
from uuid import UUID
from dropbox.api.v2.datatypes.external_drive_backup import EligibleMigrationType, IsEligibleForSeamlessMigrationResult, NotEligibleMigrationEnum, PollXopStatusResult, SetupSeamlessMigrationResult, XopStatusEnum
from dropbox.client.authentication.account import Account
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.backup_instance.types import BackupInstance
from dropbox.client.features.external_drive_backup.constants import IS_ELIGIBLE_SEAMLESS_NUM_ATTEMPTS, RETRY_DELAY_BASE_SECOND, SETUP_SEAMLESS_NUM_ATTEMPTS
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.errors import RequestAssertion, RequestFailedException
from dropbox.client.features.external_drive_backup.event_reporter import ManagerBoundaryEventReporter, OperationEventReporter
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.fission_migration_info import SeamlessFissionMigrationState
from dropbox.client.features.external_drive_backup.operations import AbortSeamlessMigrationOperation, BreakAnchorForBasicOperation, HandleAllAnchorsMigrationOperation, PauseEngineAndCreateAnchorMigrationOperation, SeamlessMigrationOperation, StartSeamlessMoveMigrationOperation
from dropbox.client.features.external_drive_backup.seamless_migration_state_machine import SeamlessMigrationStateMachineWrapper
from dropbox.client.features.external_drive_backup.server_interface import catch_and_convert_network_exceptions, ServerInterface
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.types import DeviceAnchorMigrationInfo, SeparatedAnchorsByEngineAndState
from dropbox.client.features.external_drive_backup.utils import list_anchors_by_uuid_both_engines, migration_info_to_extra_dict, strip_apiv2_id_prefix, try_get_device_anchor_mig_info_from_std_da, wrap_generic_func_with_retries
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.constants import CONTROLLER_START_UP_TIMEOUT
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.async_tools import future_function, future_sequence, WrapsFutureProtocol
from dropbox.client.features.sync_everything.v3.utils import wait_for_fully_synced
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import ExecutionContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.basic import EasyFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo
_Result = TypeVar('_Result')

def on_manager_thread(self = None):
    pass
# WARNING: Decompyle incomplete

EDBControllerRunCallback = Callable[([
    ExternalBackupEvent,
    str,
    SeamlessMigrationOperation], Future[BackupResult])]
EDBControllerSetupCallback = Callable[([
    Account,
    str,
    DriveInfo,
    FileId], Future[BackupResult])]
EDBManagerRefreshCallback = Callable[([
    Account,
    str,
    DeviceAnchorMigrationInfo], Future[None])]
EDBManagerICCallback = Callable[([
    bool], Future[BackupResult])]

class SeamlessMigrationController(Destroyable):
    pass
# WARNING: Decompyle incomplete

