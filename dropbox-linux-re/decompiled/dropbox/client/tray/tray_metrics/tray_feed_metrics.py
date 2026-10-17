# Source Generated with Decompyle++
# File: tray_feed_metrics.pyc (Python 3.11)

from enum import Enum
from dropbox.client.tray.tray_metrics.common import TrayMetrics
from dropbox.enum_utils import auto, AutoLowerNameEnum, StrAsPrefixlessValueTrait

class TrayMetricsFeedDataMetric(Enum):
    ENTRY_COUNT = 'tray_content_feature_entry_count'


class TrayFeedMetricsFeature(Enum):
    NOTIFICATIONS = 'notifications'


class TrayMetricsFeedDataStage(AutoLowerNameEnum, StrAsPrefixlessValueTrait):
    RAW = auto()
    PROCESSED = auto()
    BRIDGED = auto()
    VIEWED = auto()


def report_feed_content_metrics(feature = None, stage = None, count = None):
    tags = {
        'feature': feature.value,
        'stage': stage.value }
    TrayMetrics.log_tray_metric_with_tags(TrayMetricsFeedDataMetric.ENTRY_COUNT.value, tags, count)

