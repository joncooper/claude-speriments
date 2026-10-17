# Source Generated with Decompyle++
# File: event_reporter.pyc (Python 3.11)

from datetime import timedelta
from time import perf_counter
from typing import Dict, Optional
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, FutureValue
from dropbox.client.features.backup_common.logging_helpers import amp_tag_extras
from dropbox.client.features.external_drive_backup.errors import RequestFailedException
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_action_surface import EdbActionSurface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.event_label import EventLabel
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future

class ExternalBackupEventReporter(EventReporter):
    pass
# WARNING: Decompyle incomplete


class PerformanceEventReporter(ExternalBackupEventReporter):
    pass
# WARNING: Decompyle incomplete


class ManagerBoundaryEventReporter(PerformanceEventReporter):
    pass
# WARNING: Decompyle incomplete


class OperationEventReporter(PerformanceEventReporter):
    pass
# WARNING: Decompyle incomplete


class OperationEventSession:
    
    def __init__(self, account, metrics_reporter = None, session_id = None, source = None, trace_only = (None,), extras = ('account', 'AccountInterface', 'metrics_reporter', 'MetricsReporter', 'session_id', 'str', 'source', 'Optional[EdbSource]', 'trace_only', 'bool', 'extras', 'Optional[Dict[str, str]]')):
        self._account = account
        self._metrics_reporter = metrics_reporter
        self._session_id = session_id
        self._source = source
        self._trace_only = trace_only
        self._extras = extras

    session_id = (lambda self = None: self._session_id)()
    source = (lambda self = None: self._source)()
    
    def update_metadata(self = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def new_reporter(self = None, event = None, **kwargs):
        source = self._source.name.lower() if self._source else 'unknown'
        kwargs['amptag_source'] = source
        if self._extras:
            kwargs.update(self._extras)
    # WARNING: Decompyle incomplete


