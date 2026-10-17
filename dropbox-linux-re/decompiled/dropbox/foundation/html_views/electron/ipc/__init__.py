# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import sys
from typing import TypeVar, Union
from build_number import BUILD_KEY
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.foundation.html_views.electron.ipc._interface import ElectronIpc, ElectronIpcConnectionState, JSONDict, JSONish
from dropbox.trace import TRACE
if IS_WINDOWS:
    from dropbox.foundation.html_views.electron.ipc.named_pipe_ipc import ElectronNamedPipeIpc
else:
    from dropbox.foundation.html_views.electron.ipc.socket_ipc import ElectronSocketIpc
_T = TypeVar('_T')

def get_ipc_address():
    return getattr(sys, 'electron_ipc_address')


def create_socket_server(ipc_thread_name = None):
    pass
# WARNING: Decompyle incomplete

