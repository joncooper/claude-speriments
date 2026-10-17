# Source Generated with Decompyle++
# File: network_utils.pyc (Python 3.11)

from typing import Any, Callable, Union
from dropbox.client.features.transfer.constants import FileTransfersApiErrorBase, FileTransfersApiServerError, FileTransfersApiTooManyEmailsError, FileTransfersApiTransientError, FileTransfersApiUnknownError
from dropbox.client.features.transfer.types import FileTransfersApiResponse
from dropbox.client_api.exceptions import DropboxServerError, is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.trace import TRACE

def _request_and_handle(request_fn = None):
    
    try:
        results = request_fn()
        return results
    except DropboxServerError:
        e = None
        TRACE('[FileTransfers] API endpoint returns error code: %r and data: %r', e.code, e.data)
        if _is_too_many_emails_error(e):
            del e
            return None
        del e
        return None
        None = 
        del e
        except Exception:
            e = None
            if is_transient_error(e):
                report_exception(severity = Severity.TRACE, component = DesktopComponent.FILE_TRANSFER)
                del e
                return None
            report_exception(severity = Severity.WARN, component = DesktopComponent.FILE_TRANSFER)
            del e
            return None
            None = 
            del e



def make_api_request(request_fn = None):
    pass
# WARNING: Decompyle incomplete


def _is_too_many_emails_error(error = None):
