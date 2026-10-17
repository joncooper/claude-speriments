# Source Generated with Decompyle++
# File: tray_foundation_metrics.pyc (Python 3.11)

from enum import Enum
from dropbox.client.tray.tray_metrics.common import PLATFORM_VERSION_TAG_NAME, TrayMetrics
from dropbox.enum_utils import auto, AutoLowerNameEnum
from dropbox.foundation.platform_version import PLATFORM_VERSION

class TRAY_FOUNDATION_METRIC(Enum):
    THREAD_HANG = 'tray_foundation_metric_thread_hang'


class TRAY_FOUNDATION_METRIC_TAGS(AutoLowerNameEnum):
    THREAD_NAME = auto()


class TRAY_FOUNDATION_METRIC_THREAD_NAME(AutoLowerNameEnum):
    ACTOR_THREAD_POOL = auto()
    MAIN = auto()
    NOTIFICATIONS = auto()
    NUCLEUS_NOT_RESPOND = auto()
    NUCLEUS_DISCONNECTED = auto()


def report_thread_metric(metric = None, thread_name = None):
    TrayMetrics.log_tray_metric_with_tags(metric.value, {
        PLATFORM_VERSION_TAG_NAME: PLATFORM_VERSION,
        TRAY_FOUNDATION_METRIC_TAGS.THREAD_NAME.value: thread_name.value }, 1)

