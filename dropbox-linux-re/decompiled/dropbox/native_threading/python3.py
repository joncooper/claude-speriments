# Source Generated with Decompyle++
# File: python3.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from threading import Condition, Lock, RLock
from types import TracebackType
from typing import Callable, Optional, Type, TypeVar, Union
from typing_extensions import Literal
_T = TypeVar('_T')

class NativeMutex(object):
    
    def __init__(self = None):
        self._mutex = Lock()

    
    def acquire(self = None, blocking = None):
        return self._mutex.acquire(blocking = blocking)

    
    def release(self = None):
        self._mutex.release()

    
    def __enter__(self = None):
        return self.acquire()

    
    def __exit__(self = None, type = None, value = None, traceback = ('type', 'Optional[Type[BaseException]]', 'value', 'Optional[BaseException]', 'traceback', 'Optional[TracebackType]', 'return', 'Literal[False]')):
        self.release()
        return False

    
    def locked(self = None):
        if self.acquire(blocking = False):
            self.release()
            return False



class NativeRecursiveMutex(object):
    
    def __init__(self = None):
        self._mutex = RLock()

    
    def acquire(self = None, blocking = None):
        return self._mutex.acquire(blocking = blocking)

    
    def release(self = None):
        self._mutex.release()

    
    def __enter__(self = None):
        return self.acquire()

    
    def __exit__(self = None, type = None, value = None, traceback = ('type', 'Optional[Type[BaseException]]', 'value', 'Optional[BaseException]', 'traceback', 'Optional[TracebackType]', 'return', 'Literal[False]')):
        self.release()
        return False

    
    def locked(self = None):
        if self._mutex._is_owned():
            return True
        if None.acquire(blocking = False):
            self.release()
            return False



class NativeCondition(object):
    
    def __init__(self = None, lock = None):
        pass
    # WARNING: Decompyle incomplete

    
    def acquire(self = None, blocking = None):
        return self._cond.acquire(blocking = blocking)

    
    def release(self = None):
        self._cond.release()

    
    def wait(self = None, timeout = None):
        return self._cond.wait(timeout = timeout)

    
    def wait_for(self = None, predicate = None, timeout = None):
        return self._cond.wait_for(predicate, timeout = timeout)

    
    def notify(self = None, n = None):
        self._cond.notify(n = n)

    
    def notify_all(self = None):
        return self._cond.notify_all()

    
    def __enter__(self = None):
        return self.acquire()

    
    def __exit__(self = None, exc_type = None, exc_value = None, exc_traceback = ('exc_type', 'Optional[Type[BaseException]]', 'exc_value', 'Optional[BaseException]', 'exc_traceback', 'Optional[TracebackType]', 'return', 'Literal[False]')):
        self.release()
        return False


