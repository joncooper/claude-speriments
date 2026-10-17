# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

import json
from typing import Optional
import six
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.event import report
from dropbox.proto.logging_events.logging_events_pb2 import LogEvent

def report_nucleus_event(log_event = None, account = None):
    extra_dict = { }
    for field in log_event.additional_fields:
        value = json.loads(field.value)
        if not isinstance(value, (six.string_types, bytes)):
            value = json.dumps(value)
        extra_dict[field.key] = value
        if log_event.table in ('nucleus-product-analytics', 'nucleus-bkup-product-analytics'):
            report(log_event.table, trace = False, event = log_event.event_type, severity = log_event.severity, extra = extra_dict, account = account)
            return None
        report(log_event.table, trace = False, event_type = log_event.event_type, severity = log_event.severity, extra = extra_dict, account = account)
        return None


def create_metrics_reporter(amp_metrics_reporter = None):
    return amp_metrics_reporter.child({ })

