# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

from typing import Any, Callable, Optional, Text
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client_api.connection.exceptions import APIv2EndpointError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture

class ComputerBackupException(Exception):
    pass


class RequestFailedException(ComputerBackupException):
    pass
# WARNING: Decompyle incomplete

_CatchHandler = Callable[([
    Exception,
    ExcInfo], FailedFuture[Any])]
convert_to_failure = (lambda status_code = None, debug_message = None, report_severity = future_function: pass# WARNING: Decompyle incomplete
)()
convert_to_apiv2_failure = (lambda report_severity = None: pass# WARNING: Decompyle incomplete
)()

class RequestAssertion(RequestFailedException):
    pass
# WARNING: Decompyle incomplete

