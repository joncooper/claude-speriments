# Source Generated with Decompyle++
# File: thread_usage.pyc (Python 3.11)

from __future__ import absolute_import, division
import itertools
from typing import Dict, Iterable, List, NamedTuple, Optional, Tuple
import psutil
from apex.metrics import Metric, MetricsReporter
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.threading import Lock
from dropbox.threadutils import get_thread_cpu_counter_name
if IS_MAC:
    import mac_thread_times
elif IS_WINDOWS:
    import winerror
ThreadTuple = NamedTuple('ThreadTuple', [
    ('id', int),
    ('user_time', int),
    ('system_time', int)])
METRIC_NAMESPACE = 'desktop_threading_performance'
ONE_MIN_IN_MICROSECONDS = 60000000

def _get_flow_state():
    FlowTracker = FlowTracker
    import dropbox.client.flow_tracker
    return 'active' if FlowTracker.instance().has_active_flows() else 'idle'


def _seconds_to_microseconds(sec = None):
    return int(sec * 1e+06)


class ThreadUsageTracker:
    
    def __init__(self = None, metrics_reporter = None, top_n = None, check_interval = (5, 600, 30), cpu_threshold = ('metrics_reporter', 'MetricsReporter', 'top_n', 'int', 'check_interval', 'int', 'cpu_threshold', 'float', 'return', 'None')):
        self._lock = Lock()
        self._proc = None
        self._thread_times_fn = self._threads_mac if IS_MAC else self._threads_windows_and_linux
        self._acquire_fail_counter = itertools.count()
    # WARNING: Decompyle incomplete

    
    def _reset(self = None):
        self._cumulative_times = { }
        self._last_checked = None
        self._exceeded_threshold = False
        self._max_cpu = 0

    
    def _threads_windows_and_linux(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _threads_mac(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_cumulative_times(self = None):
        by_name = { }
        threads = self._thread_times_fn()
    # WARNING: Decompyle incomplete

    
    def _first_time(self = None):
        
        try:
            self._cumulative_times = self._get_cumulative_times()
            self._last_checked = get_monotonic_time_seconds()
            return None
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.CORE_METRICS)
            return None


    
    def _calculate_top(self = None):
        new_entries = self._get_cumulative_times()
        delta_names = []
        for thread_name, thread in new_entries.items():
            prev_entry = self._cumulative_times.get(thread_name, ThreadTuple(0, 0, 0))
            deltas = (thread.user_time - prev_entry.user_time, thread.system_time - prev_entry.system_time)
            if prev_entry.id != thread.id:
                deltas = (thread.user_time, thread.system_time)
            delta_names.append((thread_name, deltas[0], deltas[1]))
            self._cumulative_times = new_entries
            delta_names.sort(key = (lambda x: x[1] + x[2]), reverse = True)
            return delta_names[:self._top_n]()

    
    def _do_check(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _poll(self = None, cpu_percent = None):
        pass
    # WARNING: Decompyle incomplete

    
    def poll(self = None, cpu_percent = None):
        acquired = self._lock.acquire(False)
        if not acquired:
            next(self._acquire_fail_counter)
            return None
        
        try:
            self._poll(cpu_percent)
            self._lock.release()
            return None
        except:
            self._lock.release()



