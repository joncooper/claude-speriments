# Source Generated with Decompyle++
# File: extension_crash_reporter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import sys
import time
from build_number import BUILD_KEY, is_prod
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.high_trace import send_mac_crash_log
from dropbox.client.periodic import PeriodicScheduler
from dropbox.overrides import report_bad_assumption
from dropbox.platform import IS_MAC
from dropbox.sqlite3_exceptions import DatabaseOrDiskFullError, DiskIOError
from dropbox.sqlite3_helpers import Cursor
from dropbox.trace import TRACE
if getattr(sys, 'dropbox_mac_is_translated', False) and is_prod():
    PROCESS_NAMES_TO_REPORT = [
        'dropboxactivityprovider',
        BUILD_KEY.lower()]
else:
    PROCESS_NAMES_TO_REPORT = [
        'dropboxactivityprovider']

class ExtensionCrashReporter(object):
    PERIODIC_REFRESH_TIME_MINUTES = 30
    DEDUPLICATION_TIME_INTERVAL = 5
    
    def __init__(self = None, local_config = None, periodic_scheduler = None):
        if IS_MAC:
            self._local_config = local_config
            periodic_scheduler.register_job('ExtensionCrashReporting', self.PERIODIC_REFRESH_TIME_MINUTES, self._report_all)
            return None

    
    def _report_all(self = None):
        for process_name in PROCESS_NAMES_TO_REPORT:
            self.report_now(process_name)
            return None

    
    def report_now(self = None, process_name = None):
        if not IS_MAC:
            return None
        if None not in PROCESS_NAMES_TO_REPORT:
            report_bad_assumption('Tried to report crash for process name %s that is not being watched' % process_name)
        local_config_key = 'last_%s_crash_event' % process_name
        current_time = time.time()
        last_report_time = self._local_config.config_dict.get(local_config_key, 0)
        if current_time - last_report_time < self.DEDUPLICATION_TIME_INTERVAL:
            return None
        send_mac_crash_log(process_name, last_report_time - 1)
        
        try:
            self._local_config.config_dict[local_config_key] = int(current_time)
            return None
        except (DatabaseOrDiskFullError, DiskIOError, Cursor.UnableToOpenSQLiteDatabase):
            e = None
            TRACE('!! Unable to set last report time, may send duplicate crash reports, cause: %r', e)
            e = None
            del e
            return None
            e = None
            del e



