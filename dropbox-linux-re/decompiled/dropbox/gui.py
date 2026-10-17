# Source Generated with Decompyle++
# File: gui.pyc (Python 3.11)

from __future__ import absolute_import
import functools
import random as insecure_random
import sys
import threading
import time
from typing import Any, Callable, Optional, Text, TypeVar
from build_number import BuildChannel, dropbox_version, is_frozen
from dropbox.client.app_state_monitor import GLOBAL_APP_STATE_MONITOR
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import _native_symbolize, db_thread
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.threading import RLock
from dropbox.threadutils import SafeValue, StoppableThread
from dropbox.trace import TRACE, trace_locals, trace_stack
MAIN_THREAD_NAME = 'MainThread'
_C = TypeVar('_C', bound = Callable[(..., Any)])

def spawn_thread_with_name(name, daemon = (None,)):
    pass
# WARNING: Decompyle incomplete


def running_on_thread_named(thread_name = None):
    pass
# WARNING: Decompyle incomplete


def is_running_on_thread_named(thread_name = None):
    return threading.current_thread().name == thread_name


def assert_not_on_main_thread():
    pass
# WARNING: Decompyle incomplete


def is_on_main_thread():
    return threading.current_thread() is threading.main_thread()

_enable_trace_warn_if_called_on_main_thread = False

def enable_trace_warn_if_called_on_main_thread():
    global _enable_trace_warn_if_called_on_main_thread
    _enable_trace_warn_if_called_on_main_thread = True


def disable_trace_warn_if_called_on_main_thread():
    global _enable_trace_warn_if_called_on_main_thread
    _enable_trace_warn_if_called_on_main_thread = False


def trace_warn_if_called_on_main_thread(func = None):
    pass
# WARNING: Decompyle incomplete


def message_sender(nonblocking_message_f, on_success, on_exception, block, handle_exceptions, dont_post, debounce, block_only_on_main_thread = (None, None, False, None, is_on_main_thread, False, None)):
    pass
# WARNING: Decompyle incomplete


class MessageQueueException(Exception):
    pass


def assert_message_queue(f = None, assertion = None):
    pass
# WARNING: Decompyle incomplete

INSTRUMENTED_EVENT_HANDLER_SAMPLE_RATE = {
    BuildChannel.beta: 0.0001,
    BuildChannel.internal_alpha: 1 }.get(dropbox_version.channel, 0)
INSTRUMENTED_EVENT_HANDLER_EXECUTION_TIME_THRESHOLD = 0.05
EVENT_HANDLER_INSTRUMENTATION_ENABLED = not dropbox_version.is_stable()

def event_handler(func = None, thread_name = None, do_trace_locals = None):
    pass
# WARNING: Decompyle incomplete

