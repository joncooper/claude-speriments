# Source Generated with Decompyle++
# File: native_queue.pyc (Python 3.11)

from __future__ import absolute_import
from collections import deque
from typing import Generic, List, Optional, TypeVar
from six.moves.queue import Empty, Full
from dropbox.monotonic_time import get_monotonic_time_seconds as _time
from dropbox.native_threading import NativeCondition, NativeMutex
MYPY = False
if MYPY:
    from typing import Deque
_T = TypeVar('_T')

def Queue():
    '''Queue'''
    
    def __init__(self = None, maxsize = None):
        self.maxsize = maxsize
        self._init(maxsize)
        self.mutex = NativeMutex()
        self.not_empty = NativeCondition(self.mutex)
        self.not_full = NativeCondition(self.mutex)
        self.unfinished_tasks = 0
        self.all_tasks_done = NativeCondition(self.mutex)

    
    def clear(self = None):
        self.mutex
        self._clear()
        self.not_full.notify()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def get_all_and_clear(self = None):
        self.mutex
        ret = self._get_all()
        self._clear()
        self.not_full.notify()
        None(None, None)

    
    def qsize(self = None, include_inflight = None):
        self.mutex
        None(None, None)
        return 
        with None:
            if not None, self._qsize(include_inflight = include_inflight):
                pass

    
    def empty(self = None):
        self.mutex
        None(None, None)
        return 
        with None:
            if not None, self._empty():
                pass

    
    def full(self = None):
        self.mutex
        None(None, None)
        return 
        with None:
            if not None, self._full():
                pass

    
    def task_done(self = None):
        self.all_tasks_done
        if self.unfinished_tasks < 0:
            raise ValueError('task_done() called too many times')
        if self.unfinished_tasks == 0:
            0 = self, self.unfinished_tasks -= 1, .unfinished_tasks
            self.all_tasks_done.notify_all()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def join(self = None):
        self.all_tasks_done
    # WARNING: Decompyle incomplete

    
    def put(self = None, item = None, block = None, timeout = (True, None)):
        self.not_full
        if not block:
            if self._full():
                raise Full
    # WARNING: Decompyle incomplete

    
    def put_nowait(self = None, item = None):
        self.put(item, False)

    
    def get(self = None, block = None, timeout = None):
        self.not_empty
        if not block:
            if self._empty():
                raise Empty
    # WARNING: Decompyle incomplete

    
    def get_nowait(self = None):
        return self.get(False)

    
    def _init(self = None, maxsize = None):
        self.queue = deque()

    
    def _qsize(self = None, include_inflight = None):
        queue_len = len(self.queue)
        return queue_len + self.unfinished_tasks if include_inflight else queue_len

    
    def _empty(self = None):
        return not (self.queue)

    
    def _full(self = None):
        if self.maxsize > 0:
            pass
        return self._qsize() >= self.maxsize

    
    def _put(self = None, item = None):
        self.queue.append(item)

    
    def _get(self = None):
        return self.queue.popleft()

    
    def _get_all(self = None):
        return list(self.queue)

    
    def _clear(self = None):
        self.queue.clear()


Queue = <NODE:27>(Queue, 'Queue', Generic[_T])
