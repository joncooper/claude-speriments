# Source Generated with Decompyle++
# File: electron_rpc_reporter.pyc (Python 3.11)

from typing import Dict, Optional
from apex.metrics import Metric, MetricsReporter
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
RPC_CALLS_METRIC_NAME = '/electron_rpc_calls/num_calls'
AMP_NAMESPACE = 'desktop_ui_framework'
if IS_WINDOWS:
    pass
elif IS_MAC:
    pass

OPERATING_SYSTEM = 'linux'

class ElectronRpcReporter:
    _shared_metrics_reporter: 'Optional[MetricsReporter]' = None
    set_metrics_reporter = (lambda cls = None, metrics_reporter = None: ElectronRpcReporter._shared_metrics_reporter = metrics_reporter)()
    has_metrics_reporter = (lambda cls = None: cls._shared_metrics_reporter is not None)()
    report_event = (lambda cls = None, type_of_call = None, sub_topic = classmethod, logging_topic = ('type_of_call', 'str', 'sub_topic', 'str', 'logging_topic', 'str', 'return', 'None'): tags = {
'type_of_call': type_of_call,
'sub_topic': sub_topic,
'topic': logging_topic }metric_name = cls._get_metric_name()cls._report_amp_metric(metric_name, tags, 1))()
    _report_amp_metric = (lambda cls = None, metric_name = None, tags = classmethod, value = ('metric_name', 'str', 'tags', 'Dict[str, str]', 'value', 'int', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    report_ipc_event = (lambda cls = None, thread_name = None, error_code = classmethod: tags = {
'os': OPERATING_SYSTEM,
'thread_name': thread_name }if error_code:
tags['error_code'] = str(error_code)metric = '/electron_ipc/error_count'cls._report_ipc_amp_metric(metric, tags))()
    _report_ipc_amp_metric = (lambda cls = None, metric_name = None, tags = classmethod: if cls._shared_metrics_reporter:
cls._shared_metrics_reporter.create_stats(Metric(AMP_NAMESPACE, metric_name), tags).record(1)NoneTRACE("Reporting amp event when shared metric is not initialized: metric= '%s' with tags='%r'", metric_name, tags))()
    _get_metric_name = (lambda cls = None: metric_name = AMP_NAMESPACE + RPC_CALLS_METRIC_NAMEmetric_name)()

