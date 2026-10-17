# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import math
import threading
from enum import Enum
from typing import List, Optional, Set
from dropbox.db_thread import db_thread
from dropbox.foundation.futures.basic import CancelledFuture, EasyFuture, Future, ResolvedFuture
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.runtime import panic_on_exception
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import group_by
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.native_threading import NativeCondition

def _SleepFuture():
    '''_SleepFuture'''
    pass
# WARNING: Decompyle incomplete

_SleepFuture = <NODE:27>(_SleepFuture, '_SleepFuture', EasyFuture[None])

class _SleepScheduler(Destroyable):
    pass
# WARNING: Decompyle incomplete


def _initialize_module():
    _SleepScheduler._is_shutting_down = False
    _SleepScheduler.instance = _SleepScheduler()
    return _SleepScheduler.instance


def sleep_async(time = None):
    if _SleepScheduler._is_shutting_down:
        return ResolvedFuture(None)
# WARNING: Decompyle incomplete

