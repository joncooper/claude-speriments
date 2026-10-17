# Source Generated with Decompyle++
# File: rpcserver.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import functools
from typing import Any, Optional
from winrpcserver_native import ffi, lib
from dropbox.exception.exception_decorators import handle_exceptions, handle_exceptions_ex_2
from dropbox.threadutils import StoppableThread
RPC_SERVER_THREAD: 'Optional[RPCServerThread]' = None
E_FAIL = -2147467259
S_OK = 0

def rpc_function(argument):
    pass
# WARNING: Decompyle incomplete


class RPCServerThread(StoppableThread):
    pass
# WARNING: Decompyle incomplete

