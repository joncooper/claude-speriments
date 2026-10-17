# Source Generated with Decompyle++
# File: api_v2.pyc (Python 3.11)

from typing import Dict
from bridge_gen.api_v2_raw_response import ApiV2RawResponse
from bridge_gen.bridge_interface_api_v2_client_untyped import ApiV2ClientUntypedBridgeInterface
from dropbox.client_api.connection_util import ConnectionResponse
from dropbox.client_api.exceptions import DropboxServerError
from dropbox.exception import ExcInfo
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool

class ApiV2ClientException(Exception):
    pass


def _get_response_data(response = None):
    return ResolvedFuture(ApiV2RawResponse(status = 200, data = response.data.decode('utf-8')))

_catch_http_error = (lambda error = None, _ = None: pass# WARNING: Decompyle incomplete
)()

class ApiV2ClientUntyped(ApiV2ClientUntypedBridgeInterface):
    
    def __init__(self = None):
        pass

    
    def untyped_api_v2_request(self, url = None, args_string = None, headers = None, context = ('url', 'str', 'args_string', 'str', 'headers', 'Dict[str, str]', 'context', 'UserContextBridgeInterface', 'return', 'Future[ApiV2RawResponse]')):
        pass
    # WARNING: Decompyle incomplete


