# Source Generated with Decompyle++
# File: operations.pyc (Python 3.11)

from abc import ABC, abstractmethod
from functools import partial
from os.path import exists
from typing import Any, Dict, List, Optional, Tuple
from uuid import UUID
from build_number.platform import IS_MAC
from dropbox import fsutil
from dropbox.api.v2.datatypes.external_drive_backup import CreateBackupResult, CreateBackupWithBackupRootInfo, GetEligibilityInfoResult, IneligibleReason, SeamlessFissionMigrationStateEnum, StartSeamlessMigrationResult
from dropbox.client.features.backup_app.view_model.bridge_gen.schedule_type import ScheduleType
from dropbox.client.features.backup_common.constants import DEFAULT_IGNORED_GLOBS, EDB_ANCHOR_EXTENSION
from dropbox.client.features.backup_common.utils import convert_dbx_ignore_line_to_path, DEFAULT_IGNORED_GLOBS_V123, path_to_glob, unescape_v123_glob
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.backup_instance.types import BackupInstance
from dropbox.client.features.external_drive_backup.constants import CREATE_BACKUP_NUM_ATTEMPTS, EDB_SEAMLESS_MIGRATION_WAIT_FOR_FISSION_TIMEOUT, ExternalDriveBackupUIStrings, NonFissionSetupReason, RETRY_DELAY_BASE_SECOND, START_SEAMLESS_NUM_ATTEMPTS
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.edb_progress_tracker import EDBProgressTracker
from dropbox.client.features.external_drive_backup.errors import convert_to_failure, EdbFissionMigrationNeeded, RequestAssertion, RequestFailedException
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventReporter, OperationEventSession
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.fission_migration_info import SeamlessFissionMigrationState
from dropbox.client.features.external_drive_backup.gating import edb_platform_drive_types, ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.seamless_migration_state_machine import SeamlessMigrationStateMachineWrapper
from dropbox.client.features.external_drive_backup.server_interface import catch_and_convert_network_exceptions, catch_and_convert_network_exceptions_create_backup, ServerInterface
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.utils import _is_remote_path_occupied, contains_invalid_exclamation_character_class, drive_info_to_extra_dict, strip_apiv2_id_prefix, wrap_generic_func_with_retries
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.v3.async_tools import assert_not_on_actor_thread, async_queued_local_function, future_function
from dropbox.client.features.sync_everything.v3.event_reporter import EventReporter
from dropbox.client.features.sync_everything.v3.utils import home_mount_path, wait_for_fully_synced
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.types.ids import FileID
from dropbox.fsutil import FileSystem
from dropbox.model.types import FileId
from dropbox.proto.nucleus.dbxignore_pb2 import DBXIgnoreVersion
from dropbox.proto.nucleus.device_anchor_pb2 import BreakBackupReason
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.device_anchor_interface import DeviceAnchorError, TargetDoesNotExist
from dropbox.sync_engine_boundary.file_system_exceptions import OperationNotPermittedError
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import DbxIgnoreContents, DeviceAnchorInfo, DeviceAnchorState, DeviceAnchorTargetType, ListDeviceAnchorsResult
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION, VENTURA
    IS_VENTURA_OR_LATER = MAC_VERSION >= VENTURA

class EmptyDriveName(Exception):
    pass


class EmptyFissionInstanceException(Exception):
    pass


class Operation(ABC, Actor):
    pass
# WARNING: Decompyle incomplete


class StartBackupOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class RemediateBackupOperation(StartBackupOperation):
    pass
# WARNING: Decompyle incomplete


class ResumeBackupOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class RenameBackupOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class PauseBackupOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class DeleteDeviceAnchorOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class CustomFolderUpdateSelectionsOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class SeamlessMigrationOperation(Operation):
    pass
# WARNING: Decompyle incomplete


class PauseEngineAndCreateAnchorMigrationOperation(SeamlessMigrationOperation):
    pass
# WARNING: Decompyle incomplete


class StartSeamlessMoveMigrationOperation(SeamlessMigrationOperation):
    pass
# WARNING: Decompyle incomplete


class HandleAllAnchorsMigrationOperation(SeamlessMigrationOperation):
    pass
# WARNING: Decompyle incomplete


class AbortSeamlessMigrationOperation(SeamlessMigrationOperation):
    pass
# WARNING: Decompyle incomplete


class BreakAnchorForBasicOperation(SeamlessMigrationOperation):
    pass
# WARNING: Decompyle incomplete

