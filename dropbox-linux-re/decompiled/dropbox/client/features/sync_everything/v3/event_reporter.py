# Source Generated with Decompyle++
# File: event_reporter.pyc (Python 3.11)

from datetime import timedelta
from time import perf_counter
from typing import Dict, Optional, Text
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, FutureValue, random_session_id
from dropbox.client.features.backup_common.logging_helpers import amp_tag_extras
from dropbox.client.features.sync_everything.v3.errors import RequestFailedException
from dropbox.client.features.sync_everything.v3.event_label import EventLabel
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future
MYPY = False
if MYPY:
    pass

class SyncEverythingEventReporter(EventReporter):
    pass
# WARNING: Decompyle incomplete


class PerformanceEventReporter(SyncEverythingEventReporter):
    pass
# WARNING: Decompyle incomplete


class ManagerBoundaryEventReporter(PerformanceEventReporter):
    pass
# WARNING: Decompyle incomplete


class OperationEventReporter(PerformanceEventReporter):
    pass
# WARNING: Decompyle incomplete


class OperationEventSession:
    
    def __init__(self, account = None, metrics_reporter = None, session_id = None, source = ('account', 'AccountInterface', 'metrics_reporter', 'MetricsReporter', 'session_id', 'Optional[Text]', 'source', 'Optional[Source]'), **extras):
