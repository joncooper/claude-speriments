# Source Generated with Decompyle++
# File: fully_synced_tracker.pyc (Python 3.11)

import functools
from datetime import datetime
from typing import Any, Callable, cast, List, Optional, Set, TypeVar
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountId
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.features.sync_everything.constants import DeviceStatus
from dropbox.client.features.sync_everything.v3.async_tools import assert_on_actor_thread, future_function, future_sequence, WrapsFutureProtocol
from dropbox.client.features.sync_everything.v3.device_state import DeviceState
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE, SE_WARN
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingErrorName, SyncEverythingLogger
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import ExecutionContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers
from dropbox.foundation.raii2 import destroying
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.trace import WARNING
_Result = TypeVar('_Result')

def on_manager_thread():
    
    def on_actor(func = None, track_metrics = None):
        pass
    # WARNING: Decompyle incomplete

    return on_actor


class PersistedSyncLoggingData:
    
    def __init__(self, session_id, start_time = None, account_id = None, prev_state = None, next_state = ('session_id', 'str', 'start_time', 'int', 'account_id', 'AccountId', 'prev_state', 'DeviceState', 'next_state', 'DeviceState', 'return', 'None')):
        self.session_id = session_id
        self.start_time = start_time
        self.account_id = account_id
        self.prev_state = prev_state
        self.next_state = next_state

    
    def __repr__(self = None):
        return easy_repr(self, 'session_id', 'start_time', 'account_id', 'prev_state', 'next_state')



class FirstSyncLoggingData:
    
    def __init__(self, session_id, start_time, user_context = None, prev_state = None, next_state = None, token = ('session_id', 'str', 'start_time', 'int', 'user_context', 'UserContext', 'prev_state', 'DeviceState', 'next_state', 'DeviceState', 'token', 'Optional[CallbackRemovalToken]', 'return', 'None')):
        self.session_id = session_id
        self.start_time = start_time
        self.user_context = user_context
        self.prev_state = prev_state
        self.next_state = next_state
        self.token = token

    
    def __repr__(self = None):
        return easy_repr(self, 'session_id', 'start_time', 'user_context', 'prev_state', 'next_state', 'token')

    
    def get_persisted_data(self = None):
        account_id = self.user_context.account_id
        if not account_id:
            report_bad_assumption('invalid account id', component = DesktopComponent.SYNC_EVERYTHING)
            raise AssertionError('invalid account id')
        return PersistedSyncLoggingData(self.session_id, self.start_time, account_id, self.prev_state, self.next_state)

    from_persisted_data = (lambda data = None, account_manager = None: matched_account = Nonefor account in account_manager.linked_accounts:
if account.account_id == data.account_id:
matched_account = accountif not matched_account:
report_bad_assumption('no matching account', component = DesktopComponent.SYNC_EVERYTHING)Nonematched_account = cast(Account, matched_account)model = account_manager.account_models.get(matched_account, None)if not model:
report_bad_assumption('no matching model', component = DesktopComponent.SYNC_EVERYTHING)NoneFirstSyncLoggingData(data.session_id, data.start_time, model.user_context, data.prev_state, data.next_state, token = None))()

FullySyncedHandler = Callable[([
    FirstSyncLoggingData], Future[None])]

class FullySyncedTracker:
    
    def __init__(self, manager_exec_ctx = None, machine_config = None, metrics_reporter = None, on_fully_synced_handler = ('manager_exec_ctx', 'ExecutionContext', 'machine_config', 'MachineConfigurationWrapper', 'metrics_reporter', 'MetricsReporter', 'on_fully_synced_handler', 'FullySyncedHandler', 'return', 'None')):
        self._accounts_with_callback = set()
        self._machine_config = machine_config
        self._metrics_reporter = metrics_reporter
        self._on_fully_synced_handler = on_fully_synced_handler
        self._manager_exec_ctx = manager_exec_ctx

    
    def _assert_on_manager_thread(self = None):
        
        try:
            assert_on_actor_thread(cast(Actor, self._manager_exec_ctx))
            return None
        except AssertionError:
            report_bad_assumption('not on manager thread', component = DesktopComponent.SYNC_EVERYTHING)
            raise 


    _get_device_state = (lambda self = None: current_state = self._machine_config.sync_everything_device_state# WARNING: Decompyle incomplete
)()
    _on_sync_progress = (lambda self = None, logging_data = None, sync_progress = on_manager_thread(): if sync_progress.phase != SyncPhase.SYNCED:
Noneif None.user_context.account not in self._accounts_with_callback:
SE_TRACE('ignoring duplicate fully synced event for account %r', logging_data.session_id, logging_data.user_context.account)NoneNone._deregister_callback(logging_data)self._on_fully_synced_handler(logging_data).ground(component = DesktopComponent.SYNC_EVERYTHING))()
    
    def _persist_callback(self = None, data = None):
        self._assert_on_manager_thread()
        persisted_data = data.get_persisted_data()
        existing = self._machine_config.sync_everything_persisted_sync_callbacks.copy()
        if persisted_data.account_id in existing:
            report_bad_assumption('account id already has persisted data', component = DesktopComponent.SYNC_EVERYTHING)
            return None
        existing[persisted_data.account_id] = None
        self._machine_config.sync_everything_persisted_sync_callbacks = existing

    
    def _unpersist_callback(self = None, persisted_data = None):
        self._assert_on_manager_thread()
        existing = self._machine_config.sync_everything_persisted_sync_callbacks.copy()
        if persisted_data.account_id not in existing:
            report_bad_assumption('account id has no persisted data', component = DesktopComponent.SYNC_EVERYTHING)
            return None
        del None[persisted_data.account_id]
        self._machine_config.sync_everything_persisted_sync_callbacks = existing

    
    def _deregister_callback(self = None, data = None):
        self._assert_on_manager_thread()
    # WARNING: Decompyle incomplete

    _register_callback = (lambda self = None, user_context = None, session_id = on_manager_thread(), logging_data = (False,), skip_persist = ('user_context', 'UserContext', 'session_id', 'str', 'logging_data', 'FirstSyncLoggingData', 'skip_persist', 'bool', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    
    def on_update_redirect(self = None, user_context = None, session_id = None, curr_state = ('user_context', 'UserContext', 'session_id', 'str', 'curr_state', 'DeviceState', 'return', 'Callable[[Future[RedirectStatus]], Future[RedirectStatus]]')):
        pass
    # WARNING: Decompyle incomplete

    register_persisted_callbacks = (lambda self = None, account_manager = FutureHelpers.flatten: persisted_data = self._machine_config.sync_everything_persisted_sync_callbacks.copy()futures = []for _, data in persisted_data.items():
SE_TRACE('got persisted data %r', data.session_id, data)full_data = FirstSyncLoggingData.from_persisted_data(data, account_manager)if full_data:
SE_TRACE('reregistering callback for %r', data.session_id, full_data.user_context.account)futures.append(functools.partial(self._register_callback, full_data.user_context, full_data.session_id, full_data, True))continueSE_WARN('could not reregister callback for %r', data.session_id, data.account_id)primary_account = account_manager.linked_accounts[0] if len(account_manager.linked_accounts) > 0 else NoneSyncEverythingLogger.report_error_count_incl_hive(self._metrics_reporter, primary_account, SyncEverythingErrorName.persisted_callback_dropped, data.session_id)self._unpersist_callback(data)future_sequence(futures))()()
    has_ongoing_sync = (lambda self = None, account = None: persisted_callbacks = self._machine_config.sync_everything_persisted_sync_callbacks.copy()account.account_id in persisted_callbacks)()

