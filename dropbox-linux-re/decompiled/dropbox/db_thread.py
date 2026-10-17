# Source Generated with Decompyle++
# File: db_thread.pyc (Python 3.11)

from __future__ import absolute_import
import re
from typing import Any, Callable, cast, Optional, Text, Type, TypeVar
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.platform import IS_MAC
from dropbox.threadutils import set_thread_cpu_counter_name
from dropbox.trace import TRACE
if IS_MAC:
    from Foundation import NSThread
    from dropbox.mac.internal import autoreleasepool
CallableT = TypeVar('CallableT', bound = Callable)

def _native_symbolize(name = None, f = None):
    pass
# WARNING: Decompyle incomplete

_PYTHON_IDENTIFIER_REGEX = re.compile('^[A-Za-z_][A-Za-z0-9_]*$')
_PYTHON_ILLEGAL_CHARS_REGEX = re.compile('[^A-Za-z0-9_]+')

def _py_symbolize(name = None, func = None):
    if not _PYTHON_IDENTIFIER_REGEX.search(name):
        name = '_x_' + _PYTHON_ILLEGAL_CHARS_REGEX.sub('_', name)
# WARNING: Decompyle incomplete

T = TypeVar('T', bound = Type)

def _make_watched_thread(c = None, component = None):
    pass
# WARNING: Decompyle incomplete


def db_thread(c = None, component = None):
    newc = _make_watched_thread(c, component)
    return newc


def db_thread_with_task_timing(c = None, component = None, group_name = None):
    newc = _make_watched_thread(c, component)
    newc.configure_task_timing_reporter(component, group_name)
    return newc

