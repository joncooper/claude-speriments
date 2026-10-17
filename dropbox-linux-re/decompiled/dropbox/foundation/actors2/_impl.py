# Source Generated with Decompyle++
# File: _impl.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import abc
from _weakref import ref as WeakRef
from collections import deque
from contextlib import contextmanager
from enum import IntEnum
from threading import current_thread, Thread
from time import perf_counter
from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Text, TypeVar
import six
from apex.metrics import MetricsReporter
from build_number import dropbox_version, is_test
from build_number.channel import BuildChannel
from six.moves.queue import Empty
from exception_info import typed_exc_info
from futures import Future
from futures.basic import BaseFuture
from runtime import panic_with_report
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.foundation.asynchronous.exec_ctx import ExecutionContext
from dropbox.foundation.futures.basic import allow_blocking_on_main_thread
from dropbox.foundation.futures.thread import current_thread_named
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.raii2._shared_impl.base import SuperDestroyable
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.foundation.task_metrics import TaskTimingMetricReporter
from dropbox.threading import Condition, Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from typing import Deque
_T = TypeVar('_T')
_FutureT = TypeVar('_FutureT', bound = Future[Any])
actor_using_current_thread = (lambda actor = None: pass# WARNING: Decompyle incomplete
)()

def ActorWork():
    '''ActorWork'''
    execute_and_queue_next = (lambda self = None: pass)()
    do_execute = (lambda self = None: pass)()
    cancel = (lambda self = None: pass)()

ActorWork = <NODE:27>(ActorWork, 'ActorWork', metaclass = abc.ABCMeta)

def ActorThreadPool():
    '''ActorThreadPool'''
    dequeue_work = (lambda self = None, work_item = None: pass)()
    submit = (lambda self = None, job = None: pass)()
    stop = (lambda self = None: pass)()

ActorThreadPool = <NODE:27>(ActorThreadPool, 'ActorThreadPool', metaclass = abc.ABCMeta)

class _ActorWork(ActorWork, BaseFuture):
    pass
# WARNING: Decompyle incomplete


class _ActorThreadPool(ActorThreadPool, Destroyable):
    pass
# WARNING: Decompyle incomplete


class AutocancellerMixin(SuperDestroyable):
    pass
# WARNING: Decompyle incomplete


class ActorLifetime(IntEnum):
    INITIALIZING = 1
    RUNNING = 2
    DESTROYED = 3


class Actor(AutocancellerMixin, Destroyable, ExecutionContext):
    pass
# WARNING: Decompyle incomplete

