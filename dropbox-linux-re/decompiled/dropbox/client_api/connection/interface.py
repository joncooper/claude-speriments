# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from dataclasses import dataclass
from typing import Any, List, Optional, Tuple, Union


stone_validators
from typing_extensions import Protocol
import stone.backends.python_rsrc.stone_validators, backends, python_rsrc
from dropbox.foundation.futures.basic import Future
HostKeyAuth = <NODE:12>()
OAuthTokenAuth = <NODE:12>()
AppAuth = <NODE:12>()
NoAuth = <NODE:12>()
ClientAuth = Union[(HostKeyAuth, OAuthTokenAuth, AppAuth, NoAuth)]

class ApiRequestProtocol(Protocol):
    
    def apiv2_request(self, host, auth, endpoint, headers, args = None, arg_validator = None, result_validator = None, error_validator = ('host', 'str', 'auth', 'ClientAuth', 'endpoint', 'str', 'headers', 'List[Tuple[str, str]]', 'args', 'Any', 'arg_validator', 'bv.Validator', 'result_validator', 'bv.Validator', 'error_validator', 'bv.Validator', 'return', 'Future[Any]')):
        pass



class ApiRequestProtocolContainer(Protocol):
    new_conn = (lambda self = None: pass)()

