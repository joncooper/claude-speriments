# Source Generated with Decompyle++
# File: dispatch.pyc (Python 3.11)

from __future__ import absolute_import
import sys
import time
from abc import abstractmethod
from heapq import heappop, heappush
from itertools import count
from threading import Event, Thread
from typing import Any, Callable, Generic, List, Optional, Tuple, TypeVar, Union
from six import reraise
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.native_event import AutoResetEvent
from dropbox.threading import RLock
from dropbox.threadutils import set_thread_cpu_counter_name
from dropbox.trace import TRACE
_T = TypeVar('_T')

class TaskError(Exception):
    pass


class TaskTimeoutError(TaskError):
    pass


class TaskRunningError(TaskError):
    pass


class TaskBadStateError(TaskError):
    pass


def Worker():
    '''Worker'''
    
    def __init__(self = None, group = None, name = None):
        Thread.__init__(self, group = group, name = name, target = self._run)
        self.daemon = True
        self.activity_event = AutoResetEvent()
        self.work_items = []
        self.lock = RLock()
        self.counter = count()
        self._should_run = True

    
    def dispatch(self = None, action = None, on_complete = None, trace_unhandled_exc = (None, True)):
        return self.dispatch_at(time.time(), action, on_complete, trace_unhandled_exc)

    
    def delay(self = None, delta = None, action = None, on_complete = (None, True), trace_unhandled_exc = ('delta', 'float', 'action', 'Callable[..., _T]', 'on_complete', 'Optional[Callable[[Task], None]]', 'trace_unhandled_exc', 'bool', 'return', 'ActionTask[_T]')):
        return self.dispatch_at(time.time() + delta, action, on_complete, trace_unhandled_exc)

    
    def dispatch_at(self = None, time = None, action = None, on_complete = (None, True), trace_unhandled_exc = ('time', 'float', 'action', 'Callable[..., _T]', 'on_complete', 'Optional[Callable[[Task], None]]', 'trace_unhandled_exc', 'bool', 'return', 'ActionTask[_T]')):
        if not callable(action):
            raise TypeError('action must be callable()')
        t = ActionTask(action, on_complete = on_complete, trace_unhandled_exc = trace_unhandled_exc)
        self.lock
        priority = time
        count = next(self.counter)
        entry = (priority, count, t)
        heappush(self.work_items, entry)
        if entry == self.work_items[0]:
            self.activity_event.set()
        None(None, None)

    
    def stop(self = None):
        TRACE('Stopping dispatch worker')
        self._should_run = False
        self.activity_event.set()

    
    def _run(self = None):
        TRACE('Starting dispatch worker')
        set_thread_cpu_counter_name(self.name)
        wait_time = None
    # WARNING: Decompyle incomplete


Worker = <NODE:27>(Worker, 'Worker', Thread, Generic[_T])

class Unset(object):
    pass


def Task():
    '''Task'''
    
    def __init__(self = None, on_complete = None, trace_unhandled_exc = None):
        self._error = None
        self._value = Unset()
        self._is_success = False
        self._is_complete = False
        self._completion = Event()
        self._lock = RLock()
        self._on_complete = on_complete
        self._trace_unhandled_exc = trace_unhandled_exc

    error = (lambda self = None: if not self._completion.is_set():
raise TaskRunningError('Task is not yet complete')if self._is_success:
raise TaskBadStateError('Task succeeded')self._error)()
    value = (lambda self = None: if not self._completion.is_set():
raise TaskRunningError('Task is not yet complete')if not self._is_success:
raise TaskBadStateError('Task failed')# WARNING: Decompyle incomplete
)()
    is_complete = (lambda self = None: self._completion.is_set())()
    is_success = (lambda self = None: if not self._completion.is_set():
raise TaskRunningError('Task is not yet complete')self._is_success)()
    is_fail = (lambda self = None: if not self._com