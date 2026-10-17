# Source Generated with Decompyle++
# File: perf_session_amp.pyc (Python 3.11)

from typing import Dict, Optional
from apex.metrics import Metric, MetricsReporter
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.foundation.performance.bridge_gen.perf_session_data import PerfSessionData
from dropbox.trace import TRACE

class PerfSessionAMPMetrics:
    _metrics_reporter: 'Optional[MetricsReporter]' = None
    insert_metrics_reporter = (lambda metrics_reporter = None: TRACE('[PerfSessionAMPMetrics] Inserting metrics reporter.')PerfSessionAMPMetrics._metrics_reporter = metrics_reporter)()
    remove_metrics_reporter = (lambda : TRACE('[PerfSessionAMPMetrics] Removing metrics reporter.')PerfSessionAMPMetrics._metrics_reporter = None)()
    log_perf_session_to_amp = (lambda namespace = None, perf_session_data = None, flow_activity = staticmethod: metrics_reporter = PerfSessionAMPMetrics._metrics_reporterif not metrics_reporter:
TRACE('[PerfSessionAMPMetrics] Not logging perf session data to AMP since metrics reporter is unavailable. group_name - %r', perf_session_data.group_name)Noneif None.extras.get('host_entered_sleep', False):
TRACE('[PerfSessionAMPMetrics] Not logging perf session data to AMP since host went to sleep. group_name - %r', perf_session_data.group_name)Nonemetric = None + perf_session_data.group_nameSYNC_ACTIVITY_FLOW = 'sync_activity_flow'APOLLO_WINDOW_FLOW_NAME = 'apollo_window_manager_delegate_active_flow'tags = {
'sync': str(flow_activity.get(SYNC_ACTIVITY_FLOW, False)),
'collab_browse': str(flow_activity.get(APOLLO_WINDOW_FLOW_NAME, False)) }if perf_session_data.sub_group_name:
tags['sub_group_name'] = perf_session_data.sub_group_name# WARNING: Decompyle incomplete
)()

