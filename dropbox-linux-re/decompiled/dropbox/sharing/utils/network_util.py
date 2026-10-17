# Source Generated with Decompyle++
# File: network_util.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Callable, Optional, Text
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client_api.exceptions import DropboxServerError, is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future
from dropbox.foundation.transitional.connection_pool import make_delayed_network_call
from dropbox.sharing.constants.error_tuple import ErrorTuple
from dropbox.sharing.constants.network_response import NetworkResponse

class SharingNetworkStrings(UIStrings):
    server_error_msg = UI('We are unable to process your request. Please try again later.')
    transient_network_error_msg = UI('Check your internet connection and try again.')
    error_generic_msg = UI('We encountered an unexpected error.')


class RequestError(Exception):
    pass
# WARNING: Decompyle incomplete


def request_and_handle(request_fn = None):
    
    try:
        results = request_fn()
        return NetworkResponse(data = results)
    except DropboxServerError:
        e = None
        if e.data and 'user_message' in e.data:
            user_message = e.data['user_message']
            msg = user_message.get('text') if 'text' in user_message else user_message
            is_msg_generic = False
        else:
            msg = SharingNetworkStrings.server_error_msg
            is_msg_generic = True
        del e
        return None
        None = 
        del e
        except Exception:
            e = None
            transient_error = is_transient_error(e)
            if transient_error:
                msg = SharingNetworkStrings.transient_network_error_msg
            else:
                msg = SharingNetworkStrings.error_generic_msg
            report_exception(severity = Severity.TRACE, component = DesktopComponent.SHARING)
            del e
            return None
            None = 
            del e



def make_api_request(request_fn = None):
    pass
# WARNING: Decompyle incomplete

