# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

from typing import Callable, TypeVar
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.errors import RequestFailedException
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import ResolvedFuture
_DefaultType = TypeVar('_DefaultType')
_ReportHandler = Callable[([
    Exception,
    ExcInfo], ResolvedFuture[_DefaultType])]
report_exception_and_ignore = (lambda report_severity = None, default = None: pass# WARNING: Decompyle incomplete
)()
report_and_trace_transient_network_errors = (lambda default = None: pass# WARNING: Decompyle incomplete
)()
