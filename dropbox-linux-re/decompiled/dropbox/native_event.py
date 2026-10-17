# Source Generated with Decompyle++
# File: native_event.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Optional
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.native_threading import NativeCondition
from dropbox.trace import TRACE

class AutoResetEvent(object):
    
    def __init__(self = None):
        self._cond = NativeCondition()
        self._is_set = False
        self._allow_reset = True

    
    def set_forever(self = None):
        self._cond
        self._allow_reset = False
        self._is_set = True
        self._cond.notify()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def set(self = None):
        self._cond
        self._is_set = True
        self._cond.notify()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    push = set
    
    def is_set(self = None):
        return self._is_set

    isSet = is_set
    
    def clear(self = None):
        return self.wait(0)

    
    def wait(self = None, timeout = None):
        self._cond
    # WARNING: Decompyle incomplete

    
    def pre_wait(self = None, timeout = None):
        return timeout

    
    def post_wait(self = None):
        pass


