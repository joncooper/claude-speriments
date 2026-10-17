# Source Generated with Decompyle++
# File: stopwatch.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import random as insecure_random
import time
import uuid
from typing import Dict
import stopwatch_global
from six import iteritems
from stopwatch import AggregatedReport, format_report, StopWatch
from build_number.features import feature_enabled
from dropbox.client.ui.common.tray_popup_constants import TrayPerformanceMetrics
from dropbox.event import report
from dropbox.trace import TRACE
DEFAULT_REPORT_FRAC = 0.001
EVENT_REPORT_FRAC_CONFIG_MAP: 'Dict[str, float]' = {
    'dump_filecache_for_nucleus_migration': 1,
    'DropboxConnection creation': 1,
    'metadata_batch': 1,
    'dbfseventsd-connect': 1,
    '_trace_stacks': 1,
    'mac_proxy_fetch_system': 1,
    'mac_proxy_fetch_pac_file': 1,
    'd3d11_GetAdapterInfo': 1,
    TrayPerformanceMetrics.TRAY_ICON_CLICK: 1,
    TrayPerformanceMetrics.TRAY_CONTENT_INITIAL_LOAD: 1,
    TrayPerformanceMetrics.TRAY_CONTENT_LOAD: 1 }

def export_aggregated_timers(aggregated_report = None):
    root_timer_data = aggregated_report.root_timer_data
    values = aggregated_report.aggregated_values
    annotations = root_timer_data.trace_annotations()
    exception = annotations.pop('Exception', None)
    root_time_ms = values[root_timer_data.name][0]
# WARNING: Decompyle incomplete


def global_sw():
    return stopwatch_global.global_sw()


def global_sw_init():
    stopwatch_global.global_sw_init(time_func = time.perf_counter, export_aggregated_timers_func = export_aggregated_timers)

