# Source Generated with Decompyle++
# File: reporter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import numbers
from time import time as _time
from typing import Callable, Dict, Optional
import six
from build_number import dropbox_version
from dropbox.client.gandalf import Gandalf
from dropbox.client_typing import JSONable
from dropbox.event import report
from dropbox.fd_leak_debugging import debug_fd_leak
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.threading import Lock

class PeriodicMetricsReporter:
    DEFAULT_REPORT_INTERVAL = 3600
    INTERNAL_ALPHA_REPORT_INTERVAL = 600
    
    def __init__(self = None):
        self._last_report = None
        self._last_report_time = get_monotonic_time_seconds()
        self._gandalf = None
        self._reporters_lock = Lock()
        self._reporters = { }
        self._report_interval = self.DEFAULT_REPORT_INTERVAL
        if dropbox_version.is_internal_alpha():
            self._report_interval = self.INTERNAL_ALPHA_REPORT_INTERVAL
            return None

    
    def add_reporter(self = None, name = None, reporter = None):
        self._reporters_lock
    # WARNING: Decompyle incomplete

    
    def remove_reporter(self = None, name = None):
        self._reporters_lock
        self._reporters.pop(name, None)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def interval(self = None):
        return self._report_interval

    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf

    
    def try_report(self = None):
        now = get_monotonic_time_seconds()
        should_report = now - self._last_report_time > self._report_interval
        if not should_report:
            return None
        total_report = {
            None: _time() }
        self._reporters_lock
        our_reporters = self._reporters.copy()
        None(None, None)
    # WARNING: Decompyle incomplete


