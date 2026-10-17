# Source Generated with Decompyle++
# File: monitored_thread_pool.pyc (Python 3.11)

from time import perf_counter, time
from typing import Callable, Dict, Optional, Text, TypeVar
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.periodic import PeriodicScheduler
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.foundation.futures.basic import overrides
from dropbox.foundation.futures.thread import ThreadFuture, ThreadJob, ThreadPoolExecutor
from dropbox.sync_engine_boundary.monitored_thread_pool_metrics import AMP_NAMESPACE, METRIC_NAME_PREFIX, MonitoredThreadPoolHangReporter, SampledThreadPoolMetrics
_T = TypeVar('_T')

class MonitoredThreadJob(ThreadJob):
    pass
# WARNING: Decompyle incomplete


class MonitoredThreadPoolExecutor(ThreadPoolExecutor):
    pass
# WARNING: Decompyle incomplete


class _SystemSleepMonitor:
    
    def __init__(self = None):
        self._start_time = time()
        self._end_time = None

    
    def end_job(self = None):
        self._end_time = time()

    
    def did_not_sleep_during_job(self = None):
        if self._end_time or self._end_time < self._start_time:
            return True
        return not SystemStatusMonitorWrapper.did_sleep_between(self._start_time, self._end_time)


