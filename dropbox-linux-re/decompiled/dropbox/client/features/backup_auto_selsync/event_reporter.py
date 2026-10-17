# Source Generated with Decompyle++
# File: event_reporter.pyc (Python 3.11)

from datetime import timedelta
from time import perf_counter
from typing import Dict, Optional
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_auto_selsync.auto_selsync_result import BackupAutoSelSyncResult
from dropbox.client.features.backup_auto_selsync.logging import AutoSelSyncLogger
from dropbox.client.features.backup_auto_selsync.types import BackupAutoSelSyncEvent, BackupAutoSelSyncEventLabel
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, FutureValue
from dropbox.client.features.backup_common.logging_helpers import amp_tag_extras
from dropbox.exception import ExcInfo
from dropbox.foundation.futures import Future

class AutoSelsyncEventReporter(EventReporter):
    pass
# WARNING: Decompyle incomplete


class PerformanceEventReporter(AutoSelsyncEventReporter):
    pass
# WARNING: Decompyle incomplete


class OperationEventReporter(PerformanceEventReporter):
    pass
# WARNING: Decompyle incomplete

