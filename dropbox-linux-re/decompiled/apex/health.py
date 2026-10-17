# Source Generated with Decompyle++
# File: health.pyc (Python 3.11)

import itertools
from concurrent.futures import Future
from typing import Dict, Iterator
from apex._apex import ffi, lib
_CALLBACK_ID: 'Iterator[int]' = itertools.count()
_CALLBACK_CONTEXTS: 'Dict[int, Future[None]]' = { }
handle_ping_boundary_thread_response = (lambda context = None: future = _CALLBACK_CONTEXTS.pop(int(ffi.cast('unsigned long', context)))future.set_result(None))()

class HealthMonitoring:
    
    def __init__(self = None, ctx = None):
        self.context = ctx

    
    def ping_boundary_thread(self = None):
        callback_id = next(_CALLBACK_ID)
        fut = Future()
        _CALLBACK_CONTEXTS[callback_id] = fut
        lib.health_monitoring_ping_boundary_thread(self.context, ffi.cast('void *', callback_id), lib.handle_ping_boundary_thread_response)
        return fut


