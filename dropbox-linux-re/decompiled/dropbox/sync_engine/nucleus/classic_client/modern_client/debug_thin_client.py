# Source Generated with Decompyle++
# File: debug_thin_client.pyc (Python 3.11)

from typing import Any, Callable, cast, Text, TypeVar
from thin_client.exceptions import NucleusUnavailableError
from modern_thin_client import ModernThinClient, ModernThinClientResult
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.sync_engine_boundary.debug_interface import SyncEngineDebugInterface
from dropbox.trace import TRACE
_T = TypeVar('_T')

class FakeDisconnectException(Exception):
    pass


def ModernThinClientResultWithDelay():
    '''ModernThinClientResultWithDelay'''
    pass
# WARNING: Decompyle incomplete

ModernThinClientResultWithDelay = <NODE:27>(ModernThinClientResultWithDelay, 'ModernThinClientResultWithDelay', ModernThinClientResult[_T])

def ModernThinClientResultWithError():
    '''ModernThinClientResultWithError'''
    pass
# WARNING: Decompyle incomplete

ModernThinClientResultWithError = <NODE:27>(ModernThinClientResultWithError, 'ModernThinClientResultWithError', ModernThinClientResult[_T])

class DebugThinClient(SyncEngineDebugInterface):
    from_base_client = (lambda base_client = None: cast(ModernThinClient, DebugThinClient(base_client)))()
    
    def __init__(self = None, base_client = None):
        self._base_client = base_client

    
    def _inject_debug_behaviors(self = None, item = None):
        if item in SyncEngineDebugInterface._excluded_functions:
            return None
        if None._trace_calls:
            TRACE('DEBUG -- Thin client call: %s', item)
        if SyncEngineDebugInterface._simulate_disconnect:
            NucleusFpThinClient = NucleusFpThinClient
            import thin_client.fp_client
            if isinstance(self._base_client._base_client, NucleusFpThinClient):
                self._base_client._base_client._connection_invalidated()
            raise NucleusUnavailableError('Disconnect during: {}'.format(item))

    
    def _create_delayed_thin_client_call(self = None, item = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _create_unavailable_thin_client_call(self = None, item = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, item = None):
        self._inject_debug_behaviors(item)
        if item in SyncEngineDebugInterface._excluded_functions or item in SyncEngineDebugInterface._excluded_delay_functions:
            return getattr(self._base_client, item)
        if None._simulate_service_not_available:
            return self._create_unavailable_thin_client_call(item)
        if None._simulate_delay > 0:
            return self._create_delayed_thin_client_call(item)
        return getattr(self._base_client, item)


