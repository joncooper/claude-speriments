# Source Generated with Decompyle++
# File: message_queue.pyc (Python 3.11)

from __future__ import absolute_import
import abc
import collections
import functools
import heapq
import random as insecure_random
import threading
import time
import traceback
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, cast, Deque, Dict, List, NamedTuple, Optional, overload, Sequence, Text, Tuple, Type, TypeVar
from apex.metrics import MetricsReporter
from build_number import dropbox_version
from build_number.channel import BuildChannel
from dropbox.client.app_state_monitor import GLOBAL_APP_STATE_MONITOR
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.task_metrics import TaskTimingMetricReporter
from dropbox.gui import message_sender
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.native_event import AutoResetEvent
from dropbox.threading import RLock
from dropbox.threadutils import SafeValue, Stoppable
from dropbox.trace import TRACE
MYPY = False
_CB = TypeVar('_CB', bound = Callable)
_CBNone = TypeVar('_CBNone', bound = Callable[(..., None)])
_Arg0 = TypeVar('_Arg0')
_Arg1 = TypeVar('_Arg1')
_Arg2 = TypeVar('_Arg2')
_Arg3 = TypeVar('_Arg3')
_Result = TypeVar('_Result')
_TEST_ONLY_IGNORE_DELAY = False

class MessageQueueMeta(ABCMeta):
    pass
# WARNING: Decompyle incomplete


def MessageQueue():
    '''MessageQueue'''
    post_message = (lambda cls = None, delay = None, safe_value = classmethod, func = ('delay', 'float', 'safe_value', 'Optional[SafeValue]', 'func', 'Callable[..., Any]', 'args', 'Any', 'kwargs', 'Any', 'return', 'None'): cls._early_queue_lock# WARNING: Decompyle incomplete
)()
    on_queue = (lambda cls, f, block, delay = None, debounce = None, handle_exceptions = classmethod, on_exception = (None, False, 0, False, None, None, None), block_only_on_main_thread = ('f', 'Optional[Callable[..., Any]]', 'block', 'bool', 'delay', 'float', 'debounce', 'bool', 'handle_exceptions', 'Optional[bool]', 'on_exception', 'Optional[Callable[[BaseException, ExcInfo], None]]', 'block_only_on_main_thread', 'Optional[bool]', 'kwargs', 'Any', 'return', 'Callable[..., Any]'): pass# WARNING: Decompyle incomplete
)()
    on_queue_returns_none = (lambda cls = None, block = None, delay = classmethod, debounce = (False, 0, False, None), handle_exceptions = ('block', 'bool', 'delay', 'float', 'debounce', 'bool', 'handle_exceptions', 'Optional[bool]', 'return', 'Callable[[_CBNone], _CBNone]'): cls.on_queue(None, block, delay, debounce, handle_exceptions))()
    on_queue_blocking = (lambda cls = None: cls.on_queue(None, block = True))()
    on_queue_nonblocking = (lambda cls = None, f = classmethod: cls.on_queue(f, block = False))()()
    on_queue_nonblocking = (lambda cls = None, f = classmethod: cls.on_queue(f, block = False))()()
    on_queue_nonblocking = (lambda cls = None, f = classmethod: cls.on_queue(f, block = False))()()
    on_queue_nonblocking = (lambda cls = None, f = classmethod: cls.on_queue(f, block = False))()()
    on_queue_nonblocking = (lambda cls = None, f = classmethod: cls.on_queue(f, block = False))()()
    on_queue_nonblocking = (lambda cls = None, f = None: cls.on_queue(f, block = False))()
    _consume_early_tasks = (lambda cls: cls._early_queue_lockearly_queue = cls._early_queuecls._early_queue = NoneTRACE('Posting %d early messages ...', len(early_queue))# WARNING: Decompyle incomplete
)()
    assert_on_queue = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    _is_main_thread = (lambda cls: False)()
    _should_post = (lambda self: raise NotImplementedError())()
    _call_after = (lambda self, f: raise NotImplementedError())()
    _call_later = (lambda self = abstractmethod, f = abstractmethod, delay = abstractmethod, safe_value = ('f', 'Callable[..., Any]', 'delay', 'float', 'safe_value', 'Optional[SafeValue]', 'args', 'Any', 'kwargs', 'Any', 'return', 'None'): raise NotImplementedError())()

MessageQueue = <NODE:27>(MessageQueue, 'MessageQueue', metaclass = MessageQueueMeta)

def instrumented_message_queue_perf_timer():
    return time.perf_counter()


def instrumented_message_queue_monotonic_timer():
    return time.monotonic()


def instrumented_message_queue_random():
    return insecure_random.random()

INSTRUMENTED_MESSAGE_QUEUE_SAMPLE_RATE = {
    BuildChannel.stable: 1e-05,
    BuildChannel.beta: 0.0005,
    BuildChannel.internal_alpha: 1 }.get(dropbox_version.channel, 0)
INSTRUMENTED_MESSAGE_QUEUE_EXECUTION_TIME_THRESHOLD = 0.05
INSTRUMENTED_MESSAGE_QUEUE_DELAY_TIME_THRESHOLD = 0.2
INSTRUMENTED_MESSAGE_QUEUE_MAX_DELAY = 5
INSTRUMENTED_MESSAGE_QUEUE_DELAY_TRACE_THROTTLE = 5

class InstrumentedMessageQueueMeta(ABCMeta, MessageQueueMeta):
    pass
# WARNING: Decompyle incomplete


def InstrumentedMessageQueue():
    '''InstrumentedMessageQueue'''
    pass
# WARNING: Decompyle incomplete

InstrumentedMessageQueue = <NODE:27>(InstrumentedMessageQueue, 'InstrumentedMessageQueue', MessageQueue, metaclass = InstrumentedMessageQueueMeta)

class StoppableMessageQueue(MessageQueue, Stoppable):
    pass
# WARNING: Decompyle incomplete

_ScheduledTask = NamedTuple('_ScheduledTask', [
    ('target_time', float),
    ('entry_count', int),
    ('safe_value', Optional[SafeValue]),
    ('f', Callable[(..., Any)]),
    ('args', Sequence[Any]),
    ('kwargs', Dict[(Text, Any)])])

class MessageQueueThread(threading.Thread, StoppableMessageQueue):
    pass
# WARNING: Decompyle incomplete


class InstrumentedMessageQueueThread(MessageQueueThread, InstrumentedMessageQueue):
    pass
# WARNING: Decompyle incomplete

