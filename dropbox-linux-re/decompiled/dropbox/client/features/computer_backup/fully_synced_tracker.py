# Source Generated with Decompyle++
# File: fully_synced_tracker.pyc (Python 3.11)

import functools
from datetime import datetime, timezone
from typing import Any, Callable, cast, Dict, Optional, TypeVar
from dropbox.client.authentication.types import AccountId
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.backup_instance.types import BackupInstance
from dropbox.client.features.computer_backup.computer_backup_state import ComputerBackupState
from dropbox.client.features.computer_backup.constants import BackupStatus, ComputerBackupStatus
from dropbox.client.features.computer_backup.trace import CB_TRACE, CB_WARN
from dropbox.client.features.sync_everything.v3.async_tools import assert_on_actor_thread, future_function, WrapsFutureProtocol
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import ExecutionContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2 import Destroyable
from dropbox.model.types import FileId
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
_Result = TypeVar('_Result')

def on_parent_thread(self = None):
    pass
# WARNING: Decompyle incomplete


class PersistedSyncLoggingData:
    
    def __init__(self, session_id, source_name, start_time, account_id = None, anchor_fileid = None, prev_state = None, next_state = ('session_id', 'str', 'source_name', 'str', 'start_time', 'int', 'account_id', 'AccountId', 'anchor_fileid', 'FileId', 'prev_state', 'ComputerBackupState', 'next_state', 'ComputerBackupState', 'return', 'None')):
        self.session_id = session_id
        self.source_name = source_name
        self.start_time = start_time
        self.account_id = account_id
        self.anchor_fileid = anchor_fileid
        self.prev_state = prev_state
        self.next_state = next_state

    
    def __repr__(self = None):
        return easy_repr(self, 'session_id', 'start_time', 'account_id', 'anchor_fileid', 'prev_state', 'next_state')



class FirstSyncLoggingData:
    
    def __init__(self, session_id, source, start_time, user_context, anchor_fileid = None, prev_state = None, next_state = None, token = ('session_id', 'str', 'source', 'Source', 'start_time', 'int', 'user_context', 'UserContext', 'anchor_fileid', 'FileId', 'prev_state', 'ComputerBackupState', 'next_state', 'ComputerBackupState', 'token', 'Optional[CallbackRemovalToken]', 'return', 'None')):
        self.session_id = session_id
        self.source = source
        self.start_time = start_time
        self.user_context = user_context
        self.anchor_fileid = anchor_fileid
        self.prev_state = prev_state
        self.next_state = next_state
        self.token = token

    
    def __repr__(self = None):
        return easy_repr(self, 'session_id', 'start_time', 'user_context', 'anchor_fileid', 'prev_state', 'next_state', 'token')

    
    def get_persisted_data(self = None):
        account_id = self.user_context.account_id
        if not account_id:
            report_bad_assumption('invalid account id')
            raise AssertionError('invalid account id')
        return PersistedSyncLoggingData(self.session_id, self.source.name, self.start_time, account_id, self.anchor_fileid, self.prev_state, self.next_state)

    from_persisted_data = (lambda data = None, user_context = None: source = Source.__members__.get(data.source_name, Source.UNKNOWN)FirstSyncLoggingData(data.session_id, source, data.start_time, user_context, data.anchor_fileid, data.prev_state, data.next_state, token = None))()

FullySyncedHandler = Callable[([
    FirstSyncLoggingData,
    int], Future[None])]
GetComputerBackupStateCallback = Callable[([], ComputerBackupState)]

class FullySyncedTracker(Destroyable):
    pass
# WARNING: Decompyle incomplete

