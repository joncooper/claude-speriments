# Source Generated with Decompyle++
# File: yappi_profiler.pyc (Python 3.11)

import base64
import gzip
import io
import os
import tempfile
import time
from typing import Optional
from build_number import dropbox_version, is_test
from typing_extensions import Protocol
from yappi import clear_stats as yappi_clear_stats, get_func_stats as yappi_get_func_stats, is_running as yappi_is_running, start as yappi_start, stop as yappi_stop, YFuncStats
from dropbox.assertions import assert_
from dropbox.client.flow_tracker import FlowTracker
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.trace import TRACE

class ProfilerState(Protocol):
    
    def tick(self = None, cpu_percent = None):
        pass


STORMCROW_FEATURE = 'desktop-high-cpu-yappi-profile'
MEASURE_STATE_DEFAULT_INTERVAL = 120
RATE_LIMIT_DEFAULT_INTERVAL = 1800

class Baton:
    
    def __init__(self = None, high_cpu_threshold = None, gandalf = None):
        self.high_cpu_threshold = high_cpu_threshold
        self.gandalf = gandalf

    
    def set_gandalf(self = None, gandalf = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return 'Baton({}, {})'.format(self.high_cpu_threshold, self.gandalf)



class IdleState(ProfilerState):
    pass
# WARNING: Decompyle incomplete


class MeasuringState(ProfilerState):
    pass
# WARNING: Decompyle incomplete


class RateLimitedState(ProfilerState):
    pass
# WARNING: Decompyle incomplete


class YappiProfiler:
    
    def __init__(self = None, high_cpu_threshold = None, gandalf = None):
        self._baton = Baton(high_cpu_threshold, gandalf)
        self._state = IdleState(self._baton)

    
    def tick(self = None, cpu_percent = None):
        self._state = self._state.tick(cpu_percent)

    
    def set_gandalf(self = None, gandalf = None):
        self._baton.set_gandalf(gandalf)


