# Source Generated with Decompyle++
# File: ic_disable_backup_backoff.pyc (Python 3.11)

from datetime import datetime
from typing import Callable, Dict, List, NamedTuple
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.features.computer_backup.computer_backup_state import KnownCBFolder
from dropbox.client.features.computer_backup.constants import CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_EXP_BASE, CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_INITIAL_DELAY_SEC, CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_MAX, CBFolderId
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.foundation.futures import Future
from dropbox.threading import Lock
ICDisableBackupBackoffTimer = NamedTuple('ICDisableBackupBackoffTimer', [
    ('next_disable_ts', int),
    ('attempts', int)])
ICDisableBackupBackoffTimers = Dict[(CBFolderId, ICDisableBackupBackoffTimer)]

class ICDisableBackupBackoffController:
    
    def __init__(self = None, machine_config = None):
        self._machine_config = machine_config
        self._folder_missing_counter = 0
        self._lock = Lock()

    
    def _ic_disable_backup_backoff_time(self = None, folder_id = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_disable_backup_backing_off(self = None, folder_id = None):
        self._lock
        currtime = datetime.utcnow().timestamp()
        backoff_time = self._ic_disable_backup_backoff_time(folder_id)
        CB_TRACE('Comparing curr time %s vs next allowed time %s for %s', None, currtime, backoff_time, folder_id)
        if currtime < backoff_time:
            None(None, None)
            return True
        None(None, None)
        return False
        with None:
            if not None:
                pass

    
    def reset_disable_backup_backoff_timer(self = None, folder_id = None):
        self._lock
        infos = self._machine_config.computer_backup_ic_disable_backup_backoff_timers.copy()
        if folder_id in infos:
            del infos[folder_id]
        self._machine_config.computer_backup_ic_disable_backup_backoff_timers = infos
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def increase_disable_backup_backoff_timer(self = None, folder_id = None):
        self._lock
        infos = self._machine_config.computer_backup_ic_disable_backup_backoff_timers.copy()
        currtime = int(datetime.utcnow().timestamp())
        if folder_id in infos:
            backoff_info = infos[folder_id]
            new_time_offset = min(int(CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_INITIAL_DELAY_SEC * pow(CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_EXP_BASE, backoff_info.attempts)), CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_MAX)
            new_backoff_info = ICDisableBackupBackoffTimer(next_disable_ts = currtime + new_time_offset, attempts = backoff_info.attempts + 1)
        else:
            new_backoff_info = ICDisableBackupBackoffTimer(next_disable_ts = currtime + CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_INITIAL_DELAY_SEC, attempts = 1)
        CB_TRACE('Updating backoff info for %s to %s, %s attempts', None, folder_id, new_backoff_info.next_disable_ts, new_backoff_info.attempts)
        infos[folder_id] = new_backoff_info
        self._machine_config.computer_backup_ic_disable_backup_backoff_timers = infos
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def handle_ic_disable_backup_backoff_timers(self = None, invalid_folders = None):
        pass
    # WARNING: Decompyle incomplete

    regardless_clear_ic_disable_backup_backoff_timers = (lambda self = None, fut = None: self._lockself._machine_config.computer_backup_ic_disable_backup_backoff_timers = { }CB_TRACE('Clearing all IC backoff timers', None)None(None, None)with None:
if not None, fut:
pass)()

