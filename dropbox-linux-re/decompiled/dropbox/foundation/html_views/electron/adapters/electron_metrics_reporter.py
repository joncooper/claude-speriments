# Source Generated with Decompyle++
# File: electron_metrics_reporter.pyc (Python 3.11)

import json
import os
from typing import Dict, List, Optional, Text, Tuple
from apex.metrics import Counter, Metric, MetricsReporter
from dropbox.client.ui.common.uikit import FrameworkProps, record_view_event, report_ui_framework_event, report_ui_framework_event_restricted
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.performance.bridge_gen.bridge_interface_perf_session import PerfSessionBridgeInterface
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.foundation.performance.bridge_gen.perf_session_data import PerfSessionData
from dropbox.foundation.performance.bridge_gen.timing_record import TimingRecord
from dropbox.foundation.performance.perf_session import PerfSession
from dropbox.foundation.raii2 import Destroyable
from dropbox.trace import TRACE

class ElectronMetricsReporter(Destroyable):
    pass
# WARNING: Decompyle incomplete

