# Source Generated with Decompyle++
# File: system_usage.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import threading
import time
from collections import defaultdict, deque
from typing import Any, Callable, Deque, Dict, Iterable, Optional, Tuple
import psutil
from apex.memory import rust_heap_memory_usage, rust_sqlite_memory_usage
from apex.metrics import Metric, MetricsReporter, Stats
from apex.process_metrics import heap_usage
from apex.util import process_architecture
from build_number import is_test
from dropbox.client.authentication.linked_host_telemetry import get_linked_host_count_for_telemetry, has_mti_team_accounts, HAS_MTI_TEAM_ACCOUNTS_TAG, LINKED_HOST_COUNT_TAG
from dropbox.client.flow_tracker import FlowTracker
from dropbox.client.gandalf import Gandalf
from dropbox.client_typing import JSONable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.metrics.thread_usage import ThreadTuple
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.threadutils import get_thread_cpu_counter_name
from dropbox.trace import TRACE
if IS_MAC:
    import mac_thread_times
import allocator_metrics
MYPY = False
if MYPY:
    from dropbox.metrics.thread_usage import ThreadUsageTracker
CPU_STORMCROW = 'desktop-measure-thread-cpu'

def seconds_to_microseconds(s = None):
    return int(s * 1e+06)


class SystemMetricsPoller(object):
    MAX_NUM_POLL = 125
    
    def __init__(self = None, thread_usage_tracker = None, metrics_reporter = None):
        metrics_reporter = metrics_reporter.child({
            'application_arch': process_architecture() })
        self._metrics_reporter = metrics_reporter
        self._process = psutil.Process()
        self._cpu_data = deque([], SystemMetricsPoller.MAX_NUM_POLL)
        self._rss_memory_data = deque([], SystemMetricsPoller.MAX_NUM_POLL)
        self._vms_memory_data = deque([], SystemMetricsPoller.MAX_NUM_POLL)
        self._cumulative_thread_times = defaultdict((lambda : defaultdict(int)))
        process_start_delta = max(time.time() - self._process.create_time(), 0)
        self._thread_reporting_started_at = seconds_to_microseconds(get_monotonic_time_seconds() - process_start_delta)
        self._gandalf = None
        self._thread_usage_tracker = thread_usage_tracker

    _STATS_METRICS = {
        'python_raw': Metric('desktop_perf', 'memory/python/raw'),
        'python_object': Metric('desktop_perf', 'memory/python/object'),
        'rss': Metric('desktop_perf', 'memory/rss'),
        'heap': Metric('desktop_perf', 'memory/heap'),
        'heap_error': Metric('desktop_perf', 'memory/heap_fetch_error'),
        'heap_time': Metric('desktop_perf', 'memory/heap_fetch_time_micros'),
        'rust': Metric('desktop_perf', 'memory/heap/rust'),
        'rust_sqlite': Metric('desktop_perf', 'memory/heap/rust/sqlite') }
    
    def _get_stats(self = None):
        tags = { }
        
        try:
            tags[LINKED_HOST_COUNT_TAG] = str(get_linked_host_count_for_telemetry())
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.CORE_METRICS)

        
        try:
            tags[HAS_MTI_TEAM_ACCOUNTS_TAG] = str(has_mti_team_accounts()).lower()
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.CORE_METRICS)

        reporter = self._metrics_reporter.child(tags) if tags else self._metrics_reporter
        stats = { }
        for key, metric in self._STATS_METRICS.items():
            stats[key] = reporter.create_stats(metric, { })
            return stats

    
    def get_min_interval_in_minutes(self = None):
        return 1

    
    def poll(self = None):
        ret = { }
        cpu_pct = self._process.cpu_percent()
        ret['main_cpu'] = cpu_pct
        self._cpu_data.append(cpu_pct)
        flow_tracker = FlowTracker.instance()
        ret['has_active_flows'] = flow_tracker.has_active_flows()
        self._thread_usage_tracker.poll(cpu_pct)
        stats = self._get_stats()
        am = allocator_metrics.metrics()
        stats['python_raw'].record(am.allocated_raw_bytes)
        stats['python_object'].record(am.allocated_object_bytes)
        stats['rust'].record(rust_heap_memory_usage())
        stats['rust_sqlite'].record(rust_sqlite_memory_usage())
        
        try:
            hu = heap_usage()
            stats['heap'].record(hu.size_in_use)
            stats['heap_time'].record(hu.time_to_retrieve_micros)
        except OSError:
            stats['heap_error'].record(1)
            report_exception(severity = Severity.WARN, component = DesktopComponent.CORE_METRICS)
        except IndexError:
            stats['heap_error'].record(1)
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.CORE_METRICS)

        pmem = self._process.memory_info()
        stats['rss'].record(pmem.rss)
        ret['main_rss'] = pmem.rss
        self._rss_memory_data.append(pmem.rss)
        self._vms_memory_data.append(pmem.vms)
        return ret

    
    def _clear_poll_data(self = None):
        self._cpu_data.clear()
        self._rss_memory_data.clear()
        self._vms_memory_data.clear()

    
    def _get_and_update_thread_difference(self = None, tname = None, utime = None, stime = ('tname', 'str', 'utime', 'int', 'stime', 'int', 'return', 'Tuple[int, int]')):
        delta_user_time = utime - self._cumulative_thread_times[tname]['user_time']
        delta_system_time = stime - self._cumulative_thread_times[tname]['system_time']
        if delta_user_time < 0 or delta_system_time < 0:
            delta_user_time = utime
            delta_system_time = stime
        self._cumulative_thread_times[tname]['user_time'] = utime
        self._cumulative_thread_times[tname]['system_time'] = stime
        return (delta_user_time, delta_system_time)

    
    def _thread_reporting_enabled(self = None):
        if self._gandalf is not None:
            pass
        return self._gandalf.allows_any_account(CPU_STORMCROW)

    
    def _calculate_thread_times(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def trace_report_debugging(self = None):
        trace_report = False
        (memory_percent, swap_percent) = self._get_system_memory_pressure()
        if memory_percent > 90 or swap_percent > 70:
            trace_report = True
        if trace_report:
            report = self.build_report(False, get_monotonic_time_seconds())
            TRACE('System metrics trace_report_debugging: %s', report)
            return None

    
    def _get_system_memory_pressure(self = None):
        
        try:
            svmem = psutil.virtual_memory()
            sswap = psutil.swap_memory()
            return (svmem.percent, sswap.percent)
        except Exception:
            e = None
            TRACE('Failure getting system memory information (%s: %s)', type(e), e)
            e = None
            del e
            return (0, 0)
            e = None
            del e


    
    def build_report(self = None, should_report = None, ts = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf


