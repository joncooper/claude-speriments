# Source Generated with Decompyle++
# File: snooze_sync_controller.pyc (Python 3.11)

import uuid
from datetime import datetime
from typing import Callable, cast, Optional
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.wrapper import LocalConfigurationWrapper
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeInterval
from dropbox.client.features.snooze.snooze_timer import SnoozeTimer
from dropbox.client.features.snooze_sync.logging import report_event, SnoozeSyncEvent
from dropbox.client.notifications.loud_notifications.local_time_getter import LocalTimeGetter
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountManager
from dropbox.sqlite3_helpers import Cursor
from dropbox.trace import TRACE

class SnoozeSyncController:
    
    def __init__(self = None, account_manager = None, times_up_callback = None):
        self._account_manager = account_manager
        self._times_up_callback = times_up_callback
        self._indefinite_snooze_on = False
        self._snooze_timer = None

    _snooze_end_time = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    timer_started = (lambda self = None: self._snooze_timer is not None)()
    
    def get_snooze_end_time(self = None):
        return self._snooze_end_time

    
    def is_snooze_on(self = None):
