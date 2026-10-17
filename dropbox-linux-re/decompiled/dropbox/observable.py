# Source Generated with Decompyle++
# File: observable.pyc (Python 3.11)

from __future__ import absolute_import
import functools
from typing import Any, Callable, Generic, Iterator, List, Optional, TypeVar
from dropbox.callbacks import Handler
MYPY = False
FuncType = Callable[(..., None)]
_F = TypeVar('_F', bound = FuncType)
_X = TypeVar('_X')
_default_observable_handle_exc: 'Optional[Callable[[], None]]' = None

def set_default_observable_handle_exc(handle_exc = None):
    global _default_observable_handle_exc
    _default_observable_handle_exc = handle_exc


def _TypedWatchable():
    '''_TypedWatchable'''
    
    def __init__(self, f = None, handle_exc = None, name = None, trace = ('f', '_F', 'handle_exc', 'Optional[Callable[[], None]]', 'name', 'str', 'trace', 'bool', 'return', 'None')):
        self.pre = Handler[_F](handle_exc = handle_exc, name = name, trace = trace)
        self.__call__ = f
    # WARNING: Decompyle incomplete


_TypedWatchable = <NODE:27>(_TypedWatchable, '_TypedWatchable', Generic[_F])

def watchable(name = None, trace = None):
    pass
# WARNING: Decompyle incomplete


def Observable():
    '''Observable'''
    
    def __init__(self = None, val = None, recursive = None, handle_exc = (True, _default_observable_handle_exc)):
        self.data = val
        self.handler = Handler(recursive = recursive, handle_exc = handle_exc)

    
    def register(self = None, handler = None):
        self.handler.add_handler(handler)

    
    def unregister(self = None, handler = None):
        self.handler.remove_handler(handler)

    
    def get(self = None):
        return self.data

    
    def set(self = None, data = None):
        self.data = data
        self.handler.run_handlers(data)


Observable = <NODE:27>(Observable, 'Observable', Generic[_X])

def ObservableList():
    '''ObservableList'''
    
    def __init__(self = None, val = None, recursive = None, handle_exc = (None, True, _default_observable_handle_exc)):
