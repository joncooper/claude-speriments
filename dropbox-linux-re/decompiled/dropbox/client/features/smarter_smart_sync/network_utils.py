# Source Generated with Decompyle++
# File: network_utils.pyc (Python 3.11)

from typing import Any, Callable, Text
from dropbox.client.features.smarter_smart_sync.model.common import SSSAPIErrorType, SSSAPIResponse
from dropbox.client_api.exceptions import DropboxServerError, is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.trace import TRACE

def request_and_handle(request_fn = None):
    
    try:
        results = request_fn()
        return SSSAPIResponse(error = None, data = results, http_code = None)
    except DropboxServerError:
        e = None
        TRACE('[SSS] API endpoint returns error code: %r and data: %r', e.code, e.data)
        del e
        return None
        None = 
        del e
        except Exception:
            e = None
            if is_transient_error(e):
                err = SSSAPIErrorType.TRANSIENT_ERROR
            else:
                err = SSSAPIErrorType.UKNOWN_ERROR
            report_exception(severity = Severity.TRACE, component = DesktopComponent.SMART_SYNC_AUTO_EVICT)
            del e
            return None
            None = 
            del e



def make_api_request(request_fn = None):
    pass
# WARNING: Decompyle incomplete

