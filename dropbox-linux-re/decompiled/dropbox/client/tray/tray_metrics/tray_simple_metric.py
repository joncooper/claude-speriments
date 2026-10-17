# Source Generated with Decompyle++
# File: tray_simple_metric.pyc (Python 3.11)

from dropbox.client.tray.tray_metrics.common import TrayMetrics
from dropbox.enum_utils import auto, AutoLowerNameEnum

class TRAY_SIMPLE_METRIC(AutoLowerNameEnum):
    READY_STATE_HELPER_TIMEOUT = auto()
    MISSED_STAR_ACK = auto()


def report_tray_simple_metric(tray_simple_metric = None, tray_metric_data = None):
    TrayMetrics.log_tray_metric_with_tags(tray_simple_metric.value, { }, tray_metric_data)

