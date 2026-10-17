# Source Generated with Decompyle++
# File: event_reporter.pyc (Python 3.11)

from datetime import timedelta
from time import perf_counter
from typing import Dict, Optional
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_auto_selsync.auto_selsync_result import BackupAutoSelSyncResult
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, FutureValue
from dropbox.client.features.backup_common.logging_helpers import amp_tag_extras
from dropbox.client.features.backup_instance.backup_instance_logging import BackupInstanceLogger
from dropbox.client.features.backup_instance.types import BackupInstanceEvent, BackupInstanceEventLabel
from dropbox.exception import ExcInfo
from dropbox.foundation.futures import Future

class BackupInstanceEventReporter(EventReporter):
    pass
# WARNING: Decompyle incomplete


class PerformanceEventReporter(BackupInstanceEventReporter):
    pass
# WARNING: Decompyle incomplete


class OperationEventReporter(PerformanceEventReporter):
    pass
# WARNING: Decompyle incomplete

