# Source Generated with Decompyle++
# File: combined_metrics_poller.pyc (Python 3.11)

import threading
from collections import deque
from typing import Any, Deque, Dict, List, Optional, Set, Tuple
from apex.metrics import Metric, MetricsReporter, Set as MetricsSet, Stats, TagSet
from build_number import is_electron_application
from dropbox.client.authentication.linked_host_telemetry import HAS_MTI_TEAM_ACCOUNTS_TAG, has_mti_team_accounts_tag, LINKED_HOST_COUNT_TAG, linked_host_count_tag
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.stormcrow import NoStormcrowDataError
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.fenix.resource_monitoring_service import ResourceMonitoringService
    from dropbox.client_typing import JSONable
    from dropbox.foundation.html_views.metrics.html_view_metrics_reporter import HtmlViewMetricsReporter
    from dropbox.foundation.stormcrow import MachineStormcrowInterface
    from dropbox.metrics.system_usage import SystemMetricsPoller
CPU_PERCENT_METRIC_NAME = 'cpu/percent_by_proc_type'
CPU_PERCENT_METRIC = Metric('desktop_perf', CPU_PERCENT_METRIC_NAME)
MEM_RSS_METRIC_NAME = 'memory/rss_by_proc_type'
MEM_RSS_METRIC = Metric('desktop_perf', MEM_RSS_METRIC_NAME)
CPU_PERCENT_BY_VIEW_METRIC_NAME = 'cpu/percent_by_view'
CPU_PERCENT_BY_VIEW_METRIC = Metric('desktop_perf', CPU_PERCENT_BY_VIEW_METRIC_NAME)
MEM_RSS_BY_VIEW_METRIC_NAME = 'memory/rss_by_view'
MEM_RSS_BY_VIEW_METRIC = Metric('desktop_perf', MEM_RSS_BY_VIEW_METRIC_NAME)
GPU_CPU_PERCENT_METRIC_NAME = 'gpu/cpu_percent'
GPU_CPU_PERCENT_METRIC = Metric('desktop_perf', GPU_CPU_PERCENT_METRIC_NAME)
GPU_MEM_RSS_METRIC_NAME = 'gpu/mem_rss'
GPU_MEM_RSS_METRIC = Metric('desktop_perf', GPU_MEM_RSS_METRIC_NAME)
GPU_HIGH_ACTIVE_VIEW_METRIC_NAME = 'high_gpu/active_view'
GPU_HIGH_ACTIVE_VIEW_METRIC = Metric('desktop_perf', GPU_HIGH_ACTIVE_VIEW_METRIC_NAME)
GPU_HIGH_CPU_THRESHOLD = 50
COMBINED_MACHINES_BY_VIEW_METRIC = Metric('desktop_perf', 'cpu/combined/machines_by_view')
MISSING_PID_BY_VIEW_METRIC_NAME = 'views/missing_pid_count'
MISSING_PID_BY_VIEW_METRIC = Metric('desktop_perf', MISSING_PID_BY_VIEW_METRIC_NAME)
VIEW_PERSISTENCE_THRESHOLD_MINUTES = 5

def _linked_host_count_tags():
    
    try:
        return linked_host_count_tag()
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.CORE_METRICS)
        return 



def _has_mti_team_accounts_tags():
    
    try:
        return has_mti_team_accounts_tag()
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.CORE_METRICS)
        return 


GPU_METRICS_STORMCROW = 'desktop-gpu-metrics-enabled'
PER_VIEW_METRICS_STORMCROW = 'desktop-per-view-metrics-enabled'
PER_VIEW_CPU_THRESHOLD_TRACKING_STORMCROW = 'desktop-per-view-cpu-threshold-tracking-enabled'
ALLOWED_VIEW_METADATA_TAG_KEYS = frozenset([
    'variant'])
MAX_VIEW_METADATA_TAG_VALUE_LEN = 64

class MovingCounter:
    
    def __init__(self = None, max_size = None, threshold = None):
        self._max_size = max_size
        self._threshold = threshold
        self._values = deque([], max_size)
        self._count_above_threshold = 0

    
    def add(self = None, value = None):
        if len(self._values) == self._max_size:
            oldest_value = self._values.popleft()
            if oldest_value > self._threshold:
                pass
        self._values.append(value)
        if value > self._threshold:
            return None
        return self, self._count_above_threshold -= 1, ._count_above_threshold

    
    def count(self = None):
        return self._count_above_threshold



class ViewOverCPUThresholdMetric:
    MINUTES_IN_DAY = 1440
    DEFAULT_CPU_THRESHOLD = 20
    DEFAULT_MINUTES_PER_DAY_THRESHOLD = 5
    
    def __init__(self = None, metrics_reporter = None, view_name = None, cpu_threshold = (DEFAULT_CPU_THRESHOLD, DEFAULT_MINUTES_PER_DAY_THRESHOLD), minutes_per_day_threshold = ('metrics_reporter', 'MetricsReporter', 'view_name', 'str', 'cpu_threshold', 'int', 'minutes_per_day_threshold', 'int', 'return', 'None')):
        self.cpu_threshold = cpu_threshold
        self.minutes_per_day_threshold = minutes_per_day_threshold
        self.view_name = view_name
        self._minutes_over_threshold_per_day_counter = MovingCounter(self.MINUTES_IN_DAY, cpu_threshold)

    
    def observe(self = None, cpu_pct = None):
