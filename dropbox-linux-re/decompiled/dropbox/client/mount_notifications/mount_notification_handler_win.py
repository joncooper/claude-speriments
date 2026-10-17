# Source Generated with Decompyle++
# File: mount_notification_handler_win.pyc (Python 3.11)

import sys
import time
from typing import Callable, Optional, Set, Text
from apex.metrics import Metric, MetricsReporter, Stats
from dropbox.client.mount_notifications.common_event import CommonEvent, MountChangeKind
from dropbox.client.mount_notifications.mount_notification_handler_base import MountNotificationHandler
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.native_event import AutoResetEvent
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE, WARNING

try:
    import wmi
    _WMI_IMPORT_EXC_INFO = None
except Exception:
    _WMI_IMPORT_EXC_INFO = sys.exc_info()

SLEEP_TIME_SEC = 10

class DiskPollingThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class MountNotificationHandlerWin(MountNotificationHandler):
    pass
# WARNING: Decompyle incomplete

