# Source Generated with Decompyle++
# File: transient_simple_metric.pyc (Python 3.11)

from dropbox.client.transient_simple_metric.allowed_simple_metric import SimpleMetricCategoryWhitelist
from dropbox.event import AGGREGATE_TIMEOUT, report_aggregate_event
from dropbox.trace import TRACE
TRANSIENT_SIMPLE_METRIC_SPECIAL_TAG = 'transient_simple_metric'

def report_transient_simple_metric(category = None, event_name = None, count = None, aggregate_timeout = (AGGREGATE_TIMEOUT,)):
    metric = f'''{category.value!s}-{event_name!s}'''
    TRACE("[Simple Metric] Metric 'client-simple-metric-%s' incremented by %s", metric, count)
    report_aggregate_event(TRANSIENT_SIMPLE_METRIC_SPECIAL_TAG, {
        metric: count }, approx_timeout = aggregate_timeout)

