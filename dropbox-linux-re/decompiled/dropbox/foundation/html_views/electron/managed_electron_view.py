# Source Generated with Decompyle++
# File: managed_electron_view.pyc (Python 3.11)

from typing import Callable, Dict, Literal, NamedTuple, Optional, Text, Union
from dropbox.foundation.futures.basic import Future
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc, InvocationCallback, SignalCallback

class ManagedElectronViewDefinition(NamedTuple):
    name: 'str' = 'ManagedElectronViewDefinition'
    signal_handlers: 'Optional[Dict[Text, SignalCallback]]' = None
    invocation_handlers: 'Optional[Dict[Text, InvocationCallback]]' = None


class UseAfterCloseException(Exception):
    pass


class ManagedElectronViewError(NamedTuple):
    name: 'str' = 'ManagedElectronViewError'
    details: 'Optional[str]' = None


class ManagedElectronView:
    
    def __init__(self, rpc = None, session_id = None, close = None, show = ('rpc', 'ElectronRpc', 'session_id', 'str', 'close', 'Callable[[], None]', 'show', 'Callable[[], None]')):
        self.session_id = session_id
        self._is_closed = False
        self._rpc = rpc
        self._close = close
        self._show = show

    
    def send_rpc_signal(self = None, signal = None, args = None):
        if self._is_closed:
            raise UseAfterCloseException('Attempted to send an RPC signal to a closed view')
        self._rpc.send_signal(signal, args)

    
    def invoke_rpc_method(self = None, method = None, args = None):
        if self._is_closed:
            raise UseAfterCloseException('Attempted to invoke an RPC method on a closed view')
        return self._rpc.invoke_method(method, args)

    
    def close(self = None):
        if not self._is_closed:
            self._close()
            return None

    
    def show(self = None):
        if not self._is_closed:
            self._show()
            return None

    
    def handle_closed(self = None):
        self._is_closed = True
        self._rpc.destroy()



class MEVSpawnSuccess(NamedTuple):
    mev: 'ManagedElectronView' = 'MEVSpawnSuccess'


class MEVSpawnFailure(NamedTuple):
    error: 'ManagedElectronViewError' = 'MEVSpawnFailure'

ManagedElectronViewResult = Union[(MEVSpawnSuccess, MEVSpawnFailure)]
