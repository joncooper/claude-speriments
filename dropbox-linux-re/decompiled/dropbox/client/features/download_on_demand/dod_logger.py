# Source Generated with Decompyle++
# File: dod_logger.pyc (Python 3.11)

from enum import StrEnum, unique
from typing import Any, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.download_on_demand.logging_helpers import non_pii_extras
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_bad_assumption
from dropbox.sync_root.accessor import RootManagerAccessor
DownloadOnDemandLoggingEvent = <NODE:12>()
ROOT_TYPE_CALL_TIMEOUT_SECONDS = 5

def _report_event(account = None, event = None, session_id = unique, **extra_dict):
    pass
# WARNING: Decompyle incomplete


class DownloadOnDemandLogger:
    report_event = (lambda account = None, event = None, session_id = staticmethod: pass# WARNING: Decompyle incomplete
)()
    report_user_exposed_to_dod = (lambda account = None, session_id = None: pass# WARNING: Decompyle incomplete
)()
    report_dod_get_infinite_options_event = (lambda account = None, session_id = None: pass# WARNING: Decompyle incomplete
)()

