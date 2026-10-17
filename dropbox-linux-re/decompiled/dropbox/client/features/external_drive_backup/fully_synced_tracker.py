# Source Generated with Decompyle++
# File: fully_synced_tracker.pyc (Python 3.11)

import functools
from datetime import datetime, timezone
from typing import Any, Callable, cast, Dict, Optional, TypeVar
from dropbox.client.authentication.types import AccountId
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.errors import convert_to_failure
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventReporter, OperationEventSession
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE, EDB_WARN
from dropbox.client.features.external_drive_backup.types import SeparatedAnchorsByState
from dropbox.client.features.external_drive_backup.utils import drive_info_to_extra_dict, list_anchors_by_uuid_active_engine
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.v3.async_tools import assert_on_actor_thread, WrapsFutureProtocol
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import ExecutionContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, sleep_async
from dropbox.foundation.raii2 import Destroyable
from dropbox.model.types import FileId
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DeviceAnchorState
from dropbox.sync_engine_boundary.types.sync_progress import SyncedCursor, SyncPhase, SyncProgress
_Result = TypeVar('_Result')

def on_parent_thread(self = None):
    pass
# WARNING: Decompyle incomplete


class PersistedDriveInfo:
    
    def __init__(self = None, drive_info = None):
        self.uuid = drive_info.id
        self.drive_name = drive_info.name
        self.mount_path = drive_info.mount_path
        self.raw_logging_fields = drive_info_to_extra_dict(drive_info)

    
    def __repr__(self = None):
        return easy_repr(self, 'uuid', 'drive_name', 'mount_path', 'raw_logging_fields')

    
    def add_extra_logging_fields(self = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class PersistedSyncLoggingData:
    
    def __init__(self, session_id, start_time = None, account_id = None, drive_info = None, source_name = ('session_id', 'str', 'start_time', 'int', 'account_id', 'AccountId', 'drive_info', 'PersistedDriveInfo', 'source_name', 'str', 'return', 'None')):
        self.session_id = session_id
        self.start_time = start_time
        self.drive_info = drive_info
        self.source_name = source_name
        self.account_id = account_id

    
    def __repr__(self = None):
        return easy_repr(self, 'session_id', 'start_time', 'account_id', 'drive_info')



class FirstSyncLoggingData:
    
    def __init__(self, session_id, start_time, user_context = None, drive_info = None, source = None, token = ('session_id', 'str', 'start_time', 'int', 'user_context', 'UserContext', 'drive_info', 'PersistedDriveInfo', 'source', 'EdbSource', 'token', 'Optional[CallbackRemovalToken]', 'return', 'None')):
        self.session_id = session_id
        self.start_time = start_time
        self.user_context = user_context
        self.drive_info = drive_info
        self.source = source
        self.token = token

    
    def __repr__(self = None):
        return easy_repr(self, 'session_id', 'start_time', 'user_context', 'drive_info', 'token')

    
    def get_persisted_data(self = None):
        account_id = self.user_context.account_id
        if not account_id:
            report_bad_assumption('invalid account id', full_stack = True, component = DesktopComponent.SYNC_EVERYTHING)
            raise AssertionError('invalid account id')
        return PersistedSyncLoggingData(self.session_id, self.start_time, account_id, self.drive_info, self.source.name)

    from_persisted_data = (lambda data = None, user_context = None: source = EdbSource.__members__.get(data.source_name, EdbSource.UNKNOWN)FirstSyncLoggingData(data.session_id, data.start_time, user_context, data.drive_info, source, token = None))()

FullySyncedHandler = Callable[([
    FirstSyncLoggingData], Future[None])]

class FullySyncedTracker(Destroyable):
    pass
# WARNING: Decompyle incomplete

