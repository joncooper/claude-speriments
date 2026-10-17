# Source Generated with Decompyle++
# File: base_event_reporter.pyc (Python 3.11)

from time import perf_counter
from typing import Any, Dict, Optional, Text, TypeVar
from uuid import uuid4
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.event_label import EventLabel
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2 import Destroyable
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
ExtraDict = Dict[(Text, Any)]
FutureValue = TypeVar('FutureValue')

def random_session_id():
    return uuid4().hex[0:16]


def trace_event(msg = None, **kwargs):
    tmp = msg
# WARNING: Decompyle incomplete


class EventReporter:
    
    def __init__(self, event_name = None, session_id = None, trace_only = None, amp_only = (None, False, False, False), amp_only_force_fail_to_hive = ('event_name', 'Text', 'session_id', 'Optional[Text]', 'trace_only', 'bool', 'amp_only', 'bool', 'amp_only_force_fail_to_hive', 'bool', 'return', 'None'), **kwargs):
