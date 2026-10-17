# Source Generated with Decompyle++
# File: snooze_sync_controller_wrapper.pyc (Python 3.11)

import uuid
from datetime import datetime
from typing import Callable, cast, Dict, Optional, Union
SnoozeLogCallback = Callable[([
    str,
    Optional[str],
    str,
    Optional[str]], None)]
ENTRY_POINT_USER = 'user'
ENTRY_POINT_AUTO_TIMER = 'autoTimer'
_SNOOZE_EVENT_THIRTY_MINUTES = 'thirty_minutes'
_SNOOZE_EVENT_HOUR = 'hour'
_SNOOZE_EVENT_TOMORROW = 'tomorrow'
_SNOOZE_EVENT_INDEFINITELY = 'indefinitely'
_SNOOZE_EVENT_RESUME = 'resume'
_SNOOZE_EVENT_RESTORED_SNOOZE = 'restored_snooze'

def _snooze_event_for_interval(interval = None):
    if interval == SnoozeTimeInterval.THIRTY_MINUTES:
        return _SNOOZE_EVENT_THIRTY_MINUTES
    if None == SnoozeTimeInterval.ONE_HOUR:
        return _SNOOZE_EVENT_HOUR
    if None in (SnoozeTimeInterval.UNTIL_AFTERNOON, SnoozeTimeInterval.UNTIL_END_OF_DAY):
        return _SNOOZE_EVENT_TOMORROW
    if None == SnoozeTimeInterval.UNTIL_TOMORROW:
        return _SNOOZE_EVENT_TOMORROW
    if None == SnoozeTimeInterval.INDEFINITELY:
        return _SNOOZE_EVENT_INDEFINITELY

from typing_extensions import Protocol
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeInterval
from dropbox.client.features.snooze_sync.snooze_sync_constants import CONFIG_KEY_SNOOZE_SYNC_CORRELATION_ID, CONFIG_KEY_SNOOZE_SYNC_END_TIME
from dropbox.client.features.snooze_sync.snooze_sync_controller import SnoozeSyncController
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.threading import Lock
from dropbox.trace import TRACE

class PauseSyncing(Protocol):
    
    def __call__(self = None, user_initiated_pause = None):
        pass


_CACHE_NOT_LOADED: 'object' = object()

class SnoozeSyncControllerWrapper(SingletonActor):
    pass
# WARNING: Decompyle incomplete

