# Source Generated with Decompyle++
# File: event_reporter.pyc (Python 3.11)

from datetime import timedelta
from time import perf_counter
from typing import Dict, Optional, Text
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, FutureValue, random_session_id
from dropbox.client.features.backup_common.logging_helpers import amp_tag_extras
from dropbox.client.features.computer_backup.computer_backup_logging import ComputerBackupLogger
from dropbox.client.features.computer_backup.errors import RequestFailedException
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event_label import ComputerBackupEventLabel
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future

class ComputerBackupEventReporter(EventReporter):
    pass
# WARNING: Decompyle incomplete


class PerformanceEventReporter(ComputerBackupEventReporter):
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
