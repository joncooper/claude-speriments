# Source Generated with Decompyle++
# File: bridge_interface_api_v2_client_untyped.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Dict
from dropbox.foundation.futures import Future
from dropbox.client.features.api_v2.bridge_gen.api_v2_raw_response import ApiV2RawResponse
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface

class ApiV2ClientUntypedBridgeInterface(ABC):
    untyped_api_v2_request = (lambda self, url = None, args_string = None, headers = abstractmethod, context = ('url', 'str', 'args_string', 'str', 'headers', 'Dict[str, str]', 'context', 'UserContextBridgeInterface', 'return', 'Future[ApiV2RawResponse]'): pass)()

