# Source Generated with Decompyle++
# File: seamless_migration_scheduler.pyc (Python 3.11)

import os
from dataclasses import dataclass
from functools import partial
from typing import Any, Callable, Dict, List, Optional, Tuple
import psutil
from dropbox.api.v2.datatypes.external_drive_backup import EligibleMigrationType, IsEligibleForSeamlessMigrationResult
from dropbox.client.authentication.account import Account
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, random_session_id
from dropbox.client.features.external_drive_backup.constants import IS_ELIGIBLE_SEAMLESS_NUM_ATTEMPTS, RETRY_DELAY_BASE_SECOND, SeamlessFissionMigrationVariant
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.event_reporter import ManagerBoundaryEventReporter
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger as Logger
from dropbox.client.features.external_drive_backup.fission_migration_info import FissionMigrationStatus, SeamlessFissionMigrationState
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.seamless_migration_state_machine import SeamlessMigrationStateMachineWrapper
from dropbox.client.features.external_drive_backup.server_interface import catch_and_convert_network_exceptions, ServerInterface
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.types import DeviceAnchorMigrationInfo, MaybeReconstructDeviceAnchorMigInfo, SeamlessMigrationIneligbileReason, SeparatedAnchorsByEngineAndState
from dropbox.client.features.external_drive_backup.utils import compute_driving_seamless_variant, disk_usage_and_vmem_to_extra_dict, get_list_device_anchor_mig_info, get_reconstructed_mig_info, is_maybe_reconstruct_in_abort_state, list_anchors_by_uuid_both_engines, migration_info_to_extra_dict, wrap_generic_func_with_retries
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function, future_sequence
from dropbox.client.features.sync_everything.v3.utils import is_offline
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.basic import ResolvedFuture
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.raii2 import destroying
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
EDBAttemptSeamlessFuncType = Callable[([
    Account,
    str,
    DeviceAnchorMigrationInfo], Future[BackupResult])]
_UpdateAction = Callable[([], Future[BackupResult])]
EDBAbortSeamlessFuncType = Callable[([
    Account,
    str,
    DeviceAnchorMigrationInfo], Future[BackupResult])]
EDBAttemptBasicFuncType = Callable[([
    Account,
    str,
    DeviceAnchorMigrationInfo], Future[BackupResult])]
EDBUpdateFuncType = Callable[([
    _UpdateAction,
    EventReporter], Future[BackupResult])]
ListDeviceMigInfo = List[MaybeReconstructDeviceAnchorMigInfo]
MaybeAttemptMigrationInfo = <NODE:12>()

class SeamlessMigrationScheduler(Actor):
    pass
# WARNING: Decompyle incomplete

