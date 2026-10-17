# Source Generated with Decompyle++
# File: callbacks.pyc (Python 3.11)

from __future__ import absolute_import
import weakref
from typing import Any, Callable, Generic, Optional, Tuple, TypeVar
from dropbox.functions import lrudict
from dropbox.handler import _CB, Handler as _Handler
from dropbox.trace import TRACE
_default_handler_handle_exc: 'Optional[Callable[[], None]]' = None

def set_default_handler_handle_exc(handle_exc = None):
    global _default_handler_handle_exc
    _default_handler_handle_exc = handle_exc


def _trace_before_run(name = None, handler = None, priority = None):
    TRACE('Running %s handler %r with priority %r', name, handler, priority)


def Handler():
    '''Handler'''
    pass
# WARNING: Decompyle incomplete

Handler = <NODE:27>(Handler, 'Handler', _Handler[_CB])
_KeyT = TypeVar('_KeyT')

def HandlerDict():
    '''HandlerDict'''
    
    def __init__(self = None, cache_size = None, recursive = None, handle_exc = (100, True, None)):
        self._handlers = lrudict(cache_size = cache_size)
        self._recursive = recursive
        self._handle_exc = handle_exc

    
    def add_handler(self = None, key = None, callback = None, priority = (0,)):
        if key in self._handlers:
            handler = self._handlers[key]
        else:
            handler = Handler(recursive = self._recursive, handle_exc = self._handle_exc, name = repr(key))
            self._handlers[key] = handler
        handler.add_handler(callback, priority)

    
    def remove_handler(self = None, key = None, callback = None):
        if key not in self._handlers:
            return None
        handler = None._handlers[key]
        handler.remove_handler(callback)
        if handler.count() == 0:
            del self._handlers[key]
            return None

    
    def remove_handlers_by_key(self = None, key = None):
        self._handlers.pop(key, None)

    
    def run_handlers(self = None, key = None, *n, **kw):
        if key not in self._handlers:
            return None
    # WARNING: Decompyle incomplete


HandlerDict = <NODE:27>(HandlerDict, 'HandlerDict', Generic[(_KeyT, _CB)])

def create_weakref_callback(instance, unbound_callback):
    pass
# WARNING: Decompyle incomplete

