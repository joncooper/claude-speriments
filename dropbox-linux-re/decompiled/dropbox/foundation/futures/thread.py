# Source Generated with Decompyle++
# File: thread.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import functools
import os
from contextlib import contextmanager
from threading import current_thread, Thread
from typing import Any, Callable, Iterator, List, Optional, Text, Tuple, TypeVar
from six.moves.queue import Empty, Queue
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_rare_event
from dropbox.foundation.futures import CancelledFuture, EasyFuture, Future
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.threading import Lock
from dropbox.trace import TRACE
_T = TypeVar('_T')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_U = TypeVar('_U')
FiveArgRawFunc = Callable[([
    _T,
    _T2,
    _T3,
    _T4,
    _T5], _U)]
FiveArgWrappedFunc = Callable[([
    _T,
    _T2,
    _T3,
    _T4,
    _T5], Future[_U])]
current_thread_named = (lambda name = None: pass# WARNING: Decompyle incomplete
)()

def ThreadFuture():
    '''ThreadFuture'''
    pass
# WARNING: Decompyle incomplete

ThreadFuture = <NODE:27>(ThreadFuture, 'ThreadFuture', EasyFuture[_T])

class ThreadJob:
    
    def __init__(self = None, future = None, fn = None, debug_name = ('future', 'ThreadFuture[_T]', 'fn', 'Callable[[], _T]', 'debug_name', 'Optional[Text]', 'return', 'None')):
        self._future = future
        self._fn = fn
        self._debug_name = debug_name

    
    def run(self = None):
        if self._future.cancelled():
            return None
        if None._debug_name:
            current_thread_named(self._debug_name)
            self._future.run_and_set_from(self._fn)
            None(None, None)
            return None
        with None:
            if not None:
                pass
        return None
        self._future.run_and_set_from(self._fn)

    
    def cancel(self = None):
        return self._future.cancel()



class _ThreadWorker(Thread):
    pass
# WARNING: Decompyle incomplete


class ThreadPoolExecutor(Destroyable):
    pass
# WARNING: Decompyle incomplete


class GlobalPool(Destroyable):
    pass
# WARNING: Decompyle incomplete

