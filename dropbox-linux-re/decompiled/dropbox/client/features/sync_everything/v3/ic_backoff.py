# Source Generated with Decompyle++
# File: ic_backoff.pyc (Python 3.11)

from datetime import datetime
from typing import Callable, Dict, NamedTuple
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.features.sync_everything.constants import IC_EXP_BACKOFF_EXP_BASE, IC_EXP_BACKOFF_INITIAL_DELAY_SEC, IC_EXP_BACKOFF_MAX, IC_FOLDER_MISSING_MAX_BACKOFF
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.errors import RecoveryActionType
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.foundation.futures import Future
from dropbox.threading import Lock
ICBackoffTimer = NamedTuple('ICBackoffTimer', [
    ('next_check_ts', int),
    ('attempts', int)])
ICBackoffTimers = Dict[(RecoveryActionType, ICBackoffTimer)]

class ICBackoffController:
    
    def __init__(self = None, machine_config = None):
        self._machine_config = machine_config
        self._folder_missing_counter = 0
        self._lock = Lock()

    
    def _ic_backoff_time(self = None, action = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_backing_off(self = None, action = None):
        self._lock
        currtime = datetime.utcnow().timestamp()
        backoff_time = self._ic_backoff_time(action)
        SE_TRACE('Comparing curr time %s vs next allowed time %s for %s', None, currtime, backoff_time, action)
        if currtime < backoff_time:
            None(None, None)
            return True
        None(None, None)
        return False
        with None:
            if not None:
                pass

    
    def reset_backoff_timer(self = None, action = None):
        self._lock
        infos = self._machine_config.sync_everything_ic_backoff_timers.copy()
        if action in infos:
            del infos[action]
        self._machine_config.sync_everything_ic_backoff_timers = infos
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def increase_backoff_timer(self = None, action = None):
        self._lock
        infos = self._machine_config.sync_everything_ic_backoff_timers.copy()
        currtime = int(datetime.utcnow().timestamp())
        if action in infos:
            backoff_info = infos[action]
            new_time_offset = min(int(IC_EXP_BACKOFF_INITIAL_DELAY_SEC * pow(IC_EXP_BACKOFF_EXP_BASE, backoff_info.attempts)), IC_EXP_BACKOFF_MAX)
            new_backoff_info = ICBackoffTimer(next_check_ts = currtime + new_time_offset, attempts = backoff_info.attempts + 1)
        else:
            new_backoff_info = ICBackoffTimer(next_check_ts = currtime + IC_EXP_BACKOFF_INITIAL_DELAY_SEC, attempts = 1)
        SE_TRACE('Updating backoff info for %s to %s, %s attempts', None, action, new_backoff_info.next_check_ts, new_backoff_info.attempts)
        infos[action] = new_backoff_info
        self._machine_config.sync_everything_ic_backoff_timers = infos
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def handle_ic_backoff_timers(self = None, action = None):
        pass
    # WARNING: Decompyle incomplete

    regardless_clear_ic_backoff_timers = (lambda self = None, fut = None: self._lockself._machine_config.sync_everything_ic_backoff_timers = { }None(None, None)with None:
if not None, fut:
pass)()
    
    def on_folder_missing(self = None):
        self._lock
        None(None, None)
        return None
        with None:
            if not self, self._folder_missing_counter += 1, ._folder_missing_counter:
                pass

    
    def allow_folder_missing(self = None):
        self._lock
        if self._folder_missing_counter > IC_FOLDER_MISSING_MAX_BACKOFF:
            None(None, None)
            return True
        None(None, None)
        return False
        with None:
            if not None:
                pass

    
    def reset_folder_missing(self = None):
        self._lock
        self._folder_missing_counter = 0
        None(None, None)
        return None
        with None:
            if not None:
                pass


