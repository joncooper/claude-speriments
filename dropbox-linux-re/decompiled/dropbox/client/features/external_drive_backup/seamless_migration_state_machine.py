# Source Generated with Decompyle++
# File: seamless_migration_state_machine.pyc (Python 3.11)

from typing import Dict, Iterable, List, Optional, Tuple
from uuid import UUID
from dropbox.api.v2.datatypes.external_drive_backup import ReadSeamlessMigrationStateResult, SeamlessFissionMigrationStateEnum, UpdateSeamlessMigrationStateResult
from dropbox.client.configuration.wrapper import LocalConfigurationWrapper
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.errors import report_exception_and_ignore
from dropbox.client.features.external_drive_backup.constants import FISSION_UNPAUSED_ANCHOR_NUM_ATTEMPTS, FSS_ANCHOR_BREAK_COMPLETE_NUM_ATTEMPTS, FSS_ANCHOR_DELETE_COMPLETE_NUM_ATTEMPTS, REFRESH_SEAMLESS_NUM_ATTEMPTS, RETRY_DELAY_BASE_SECOND, UPDATE_SEAMLESS_NUM_ATTEMPTS
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventReporter
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger as Logger
from dropbox.client.features.external_drive_backup.fission_migration_info import SeamlessFissionMigrationDictType, SeamlessFissionMigrationInfo, SeamlessFissionMigrationState
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.server_interface import catch_and_convert_network_exceptions, ServerInterface
from dropbox.client.features.external_drive_backup.types import SeparatedAnchorsByEngineAndState
from dropbox.client.features.external_drive_backup.utils import list_anchors_by_uuid_both_engines, wrap_generic_func_with_retries
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.helpers import FutureHelpers
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.model.types import FileId
from dropbox.repr_utils import easy_repr
from dropbox.trace import TRACE

class ConfigStore:
    
    def __init__(self = None, config = None):
        self._local_config = config

    edb_seamless_fission_mig_info = (lambda self = None: self._local_config.edb_seamless_fission_mig_info)()
    
    def set_state(self, anchor_fileid, state, drive_uuid = None, drive_capacity = None, xop_id = None, drive_name = (None, None, None, None, None), drive_mount_path = ('anchor_fileid', 'FileId', 'state', 'SeamlessFissionMigrationState', 'drive_uuid', 'Optional[str]', 'drive_capacity', 'Optional[int]', 'xop_id', 'Optional[UUID]', 'drive_name', 'Optional[str]', 'drive_mount_path', 'Optional[str]', 'return', 'None')):
        seamless_migration_info = self.edb_seamless_fission_mig_info
        if anchor_fileid in seamless_migration_info:
            current_state = seamless_migration_info[anchor_fileid]
            current_state.migration_status = state
            current_state.drive_uuid = drive_uuid if drive_uuid else current_state.drive_uuid
            current_state.drive_capacity = drive_capacity if drive_capacity else current_state.drive_capacity
            current_state.xop_id = xop_id if xop_id else current_state.xop_id
            current_state.drive_name = drive_name if drive_name else current_state.drive_name
            current_state.drive_mount_path = drive_mount_path if drive_mount_path else current_state.drive_mount_path
            seamless_migration_info[anchor_fileid] = current_state
    # WARNING: Decompyle incomplete

    
    def get_migration_info(self = None, anchor_fileid = None):
        seamless_migration_info = self.edb_seamless_fission_mig_info
        if anchor_fileid in seamless_migration_info:
            return seamless_migration_info[anchor_fileid]

    
    def get_state(self = None, anchor_fileid = None):
        seamless_migration_info = self.edb_seamless_fission_mig_info
        if anchor_fileid in seamless_migration_info:
            return seamless_migration_info[anchor_fileid].migration_status
        return None.UNKNOWN

    
    def get_drive_uuid(self = None, anchor_fileid = None):
        seamless_migration_info = self.edb_seamless_fission_mig_info
        if anchor_fileid in seamless_migration_info:
            return seamless_migration_info[anchor_fileid].drive_uuid

    
    def get_drive_capacity(self = None, anchor_fileid = None):
        seamless_migration_info = self.edb_seamless_fission_mig_info
        if anchor_fileid in seamless_migration_info:
            return seamless_migration_info[anchor_fileid].drive_capacity

    
    def get_xop(self = None, anchor_fileid = None):
        seamless_migration_info = self.edb_seamless_fission_mig_info
        if anchor_fileid in seamless_migration_info:
            return seamless_migration_info[anchor_fileid].xop_id

    
    def get_drive_name(self = None, anchor_fileid = None):
        seamless_migration_info = self.edb_seamless_fission_mig_info
        if anchor_fileid in seamless_migration_info:
            return seamless_migration_info[anchor_fileid].drive_name

    
    def get_drive_mount_path(self = None, anchor_fileid = None):
        seamless_migration_info = self.edb_seamless_fission_mig_info
        if anchor_fileid in seamless_migration_info:
            return seamless_migration_info[anchor_fileid].drive_mount_path



class SeamlessMigrationStateMachine(Actor):
    pass
# WARNING: Decompyle incomplete


class SeamlessMigrationStateMachineWrapper(SingletonActor):
    pass
# WARNING: Decompyle incomplete

