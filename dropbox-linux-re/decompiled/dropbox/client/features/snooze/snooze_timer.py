# Source Generated with Decompyle++
# File: snooze_timer.pyc (Python 3.11)

from datetime import datetime, timedelta
from typing import Callable, Optional
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeCalculator, SnoozeTimeInterval
from dropbox.client.notifications.loud_notifications.local_time_getter import LocalTimeGetter
from dropbox.client.notifications.loud_notifications.time_monitor_wrapper import SystemTimeMonitorWrapper
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.trace import TRACE

class SnoozeTimer:
    
    def __init__(self = None, end_time = None, on_time_up_callback = None):
        self._end_time = end_time
        self._scheduled_timer = None
        self._on_time_up_callback = on_time_up_callback
        self._callback_registered = False
        self._schedule_snooze_timer()
        self._system_time_monitor = SystemTimeMonitorWrapper.get_instance()
        self._register_time_change_callback()

    end_time = (lambda self = None: self._end_time)()
    
    def _register_time_change_callback(self = None):
        if not self._callback_registered:
            self._system_time_monitor.add_time_changed_callback(self._turn_off_if_snooze_time_is_out_of_bounds)
            self._callback_registered = True
            return None

    
    def _unregister_time_change_callback(self = None):
        if self._callback_registered:
            self._system_time_monitor.remove_time_changed_callback(self._turn_off_if_snooze_time_is_out_of_bounds)
            self._callback_registered = False
            return None

    
    def _schedule_snooze_timer(self = None):
        if self._end_time:
            current_time = LocalTimeGetter.get_local_time()
            end_time = self._normalize_end_time(self._end_time, current_time)
            self._end_time = end_time
            seconds_remaining = (end_time - current_time).total_seconds()
            self.schedule_timeup_callback(seconds_remaining)
            return None

    
    def schedule_timeup_callback(self = None, delay = None):
        pass
    # WARNING: Decompyle incomplete

    
    def turn_off(self = None):
        self._end_time = None
    # WARNING: Decompyle incomplete

    
    def set_end_time(self = None, time_interval = None):
        if time_interval is SnoozeTimeInterval.INDEFINITELY:
            report_bad_assumption('Trying to set end time for snooze indefinitely which has no timer end time', component = DesktopComponent.TRAY)
            return None
        current_time = LocalTimeGetter.get_local_time()
        new_end_time = SnoozeTimeCalculator.calculate_snooze_end_time(time_interval, current_time)
        time_in_seconds = (new_end_time - current_time).total_seconds()
        self._end_time = new_end_time
        self._register_time_change_callback()
        self.schedule_timeup_callback(time_in_seconds)

    
    def set_end_time_by_date(self = None, date = None):
        if date == datetime.max:
            self._end_time = date
            return None
        current_time = LocalTimeGetter.get_local_time()
        normalized_date = self._normalize_end_time(date, current_time)
        time_in_seconds = (normalized_date - current_time).total_seconds()
        self._end_time = normalized_date
        self._register_time_change_callback()
        self.schedule_timeup_callback(time_in_seconds)

    
    def _normalize_end_time(self = None, end_time = None, current_time = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _turn_off_if_snooze_time_is_out_of_bounds(self = None):
        pass
    # WARNING: Decompyle incomplete


