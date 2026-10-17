# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from collections import deque
from typing import Callable, Deque, Dict, Optional, Union
from apex.metrics import Metric, MetricsReporter
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.threading import Lock
from dropbox.trace import TRACE
TRAY_METRICS_NAMESPACE = 'desktop_tray'
PLATFORM_VERSION_TAG_NAME = 'platform_version'
TRAY_METRICS_MAX_TAGS = 10

class TrayMetrics:
    _metrics_reporter: 'Optional[MetricsReporter]' = None
    _tray_metrics_queue: 'Deque[Callable[[MetricsReporter], None]]' = deque()
    _lock = Lock()
    insert_metrics_reporter = (lambda metrics_reporter = None: TRACE('[TrayMetrics] Inserting metrics reporter.')TrayMetrics._lockTrayMetrics._metrics_reporter = metrics_reporterTrayMetrics._process_queue(metrics_reporter)None(None, None)Nonewith None:
if not None:
pass)()
    remove_metrics_reporter = (lambda : TRACE('[TrayMetrics] Removing metrics reporter.')TrayMetrics._lockTrayMetrics._metrics_reporter = NoneNone(None, None)Nonewith None:
if not None:
pass)()
    log_tray_metric = (lambda *: pass# WARNING: Decompyle incomplete
)()
    log_tray_metric_with_tags = (lambda tray_metric = None, tags = None, tray_metric_data = None, *, verbose, metrics_reporter = None, 