# Source Generated with Decompyle++
# File: wrapped_thin_client.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from contextlib import contextmanager
from typing import Generator, Union
from cffi_transport.exceptions import ServiceNotAvailableException
from google.protobuf.empty_pb2 import Empty as EmptyPb
from google.protobuf.service import RpcController
from thin_client.client import NucleusThinClient, NucleusThinTprtClient
from dropbox.exception.exceptions import NucleusPanicException
from dropbox.lock_ordering import NonRecursiveLock
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveRequest
from dropbox.threading import RWLock
from dropbox.trace import TRACE

class WrappedNucleusThinClient:
    
    def __init__(self = None):
        self._ptr = None
        self._request_lock = NonRecursiveLock(base_lock = RWLock(), acquire_methods = ('acquire_read', 'acquire_write'), release_methods = ('release_read', 'release_write'))

    
    def __getattr__(self, item):
        self._request_lock
        None(None, None)
        return 
        with None:
            if not None, getattr(self._ptr, item):
                pass

    requests_blocked = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def set_instance(self = None, nucleus_thin_client = None):
        pass
    # WARNING: Decompyle incomplete

    
    def running_locked(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def resume_locked(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def stop(self = None, stop_reason = None):
        pass
    # WARNING: Decompyle incomplete


