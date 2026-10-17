# Source Generated with Decompyle++
# File: model.pyc (Python 3.11)

from collections import OrderedDict
from datetime import datetime
from enum import IntEnum
from functools import partial
from typing import Callable, Optional
from dropbox.callbacks import Handler
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.snooze.snooze_time_calc import SnoozeTimeInterval
from dropbox.client.features.snooze.snooze_timer import SnoozeTimer
from dropbox.client.notifications.loud_notifications.local_time_getter import LocalTimeGetter
from dropbox.client.notifications.strings import TimeIntervalStrings
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.i18n import format_time
from dropbox.preferences import OPT_DND_END_TIME, OPT_DND_TIME_INTERVAL
from dropbox.webdebugger.server import WebDebugger

class DNDTimeInterval(IntEnum):
    UNKNOWN = 0
    THIRTY_MINUTES = 1
    ONE_HOUR = 2
    UNTIL_AFTERNOON = 3
    UNTIL_END_OF_DAY = 4
    UNTIL_TOMORROW = 5


class DoNotDisturbController:
    
    def __init__(self = None, local_config = None):
        self._local_config = local_config
        if WebDebugger.is_enabled():
            WebDebugger.register('notifications/do_not_disturb/enable', self._debug_dnd)
        end_time = self._local_config.config_dict.get(OPT_DND_END_TIME, None)
        self._snooze_timer = SnoozeTimer(end_time = end_time, on_time_up_callback = self._on_dnd_time_up)
        self._dnd_changed_handlers = Handler(handle_exc = partial(report_exception, severity = Severity.WARN))

    _dnd_end_time = (lambda self = None: self._snooze_timer.end_time)()
    
    def add_dnd_changed_handler(self = None, callback = None):
        self._dnd_changed_handlers.add_handler(callback)

    
    def remove_dnd_changed_handler(self = None, callback = None):
        self._dnd_changed_handlers.remove_handler(callback)

    
    def is_dnd_on(self = None):
        return self._dnd_end_time is not None

    
    def turn_dnd_off(self = None, logging_tag = None):
        
        try:
            self._local_config.update_preferences({
                OPT_DND_END_TIME: None })
            old_dnd_end_time = self._dnd_end_time
            self._snooze_timer.turn_off()
            self._local_config.update_preferences({
                OPT_DND_TIME_INTERVAL: SnoozeTimeInterval.UNKNOWN })
            self._report_dnd_logging(location = logging_tag, is_checked = False)
            if old_dnd_end_time != self._dnd_end_time:
                self._dnd_changed_handlers.run_handlers(self._dnd_end_time)
                return None
            return None
        except Exception:
            report_exception(severity = Severity.DEBUG, component = DesktopComponent.TRAY)
            return None


    
    def set_dnd_end_time(self = None, time_interval = None, logging_tag = None):
        
        try:
            old_dnd_end_time = self._dnd_end_time
            self._snooze_timer.set_end_time(time_interval)
            self._local_config.update_preferences({
                OPT_DND_END_TIME: self._dnd_end_time })
            self._local_config.update_preferences({
                OPT_DND_TIME_INTERVAL: time_interval })
            self._report_dnd_logging(location = logging_tag, is_checked = True, time_interval = time_interval)
            if old_dnd_end_time != self._dnd_end_time:
                self._dnd_changed_handlers.run_handlers(self._dnd_end_time)
                return None
            return None
        except Exception:
            report_exception(severity = Severity.DEBUG, component = DesktopComponent.TRAY)
            return None


    
    def _debug_dnd(self = None):
        self.set_dnd_end_time(SnoozeTimeInterval.UNTIL_TOMORROW, 'webdebugger')

    
    def get_dnd_end_time(self = None):
        return self._dnd_end_time

    
    def get_formatted_end_time(self = None):
        if self._dnd_end_time:
            formatted_dnd_end_time = format_time(self._dnd_end_time)
            return PrefStrings.dnd_end_time_label % {
                'end_time': formatted_dnd_end_time }

    
    def _on_dnd_time_up(self = None):
        self.turn_dnd_off('dnd_time_up')

    
    def _report_dnd_logging(self = None, location = None, is_checked = None, time_interval = (None,)):
        report('preferences', event_name = 'dnd_settings_changed', extra = dict(location = str(location), checked = str(is_checked).lower(), interval = str(time_interval)))



class DNDTimeIntervalsStringMapping:
    get_dnd_time_intervals = (lambda : intervals = [
(SnoozeTimeInterval.THIRTY_MINUTES, TimeIntervalStrings.thirty_minutes),
(SnoozeTimeInterval.ONE_HOUR, TimeIntervalStrings.one_hour_label)]current_hour = LocalTimeGetter.get_local_time().hourif current_hour < 13:
intervals.append((SnoozeTimeInterval.UNTIL_AFTERNOON, TimeIntervalStrings.until_afternoon_label))if current_hour < 17:
intervals.append((SnoozeTimeInterval.UNTIL_END_OF_DAY, TimeIntervalStrings.until_end_of_day_label))intervals.append((SnoozeTimeInterval.UNTIL_TOMORROW, TimeIntervalStrings.until_tomorrow_label))OrderedDict(intervals))()

