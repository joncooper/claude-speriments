# Source Generated with Decompyle++
# File: threading.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import threading
from contextlib import contextmanager
from typing import Any, Callable, Dict, Generator, Iterator, Optional, Tuple, Union
from dropbox.trace import TRACE
Lock = threading.Lock
RLock = threading.RLock

def Condition(lock = None):
    pass
# WARNING: Decompyle incomplete


class RWLock(object):
    
    def __init__(self = None):
        self.base_lock = Lock()
        self.write_condition = Condition(self.base_lock)
        self.read_condition = Condition(self.base_lock)
        self.writer_request = False
        self.num_readers = 0

    
    def _acquire_read_unlocked(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def acquire_read(self = None):
        self.base_lock
        None(None, None)
        return 
        with None:
            if not None, self._acquire_read_unlocked():
                pass

    
    def _release_read_unlocked(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def release_read(self = None):
        self.base_lock
        self._release_read_unlocked()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _acquire_write_unlocked(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def acquire_write(self = None):
        self.base_lock
        None(None, None)
        return 
        with None:
            if not None, self._acquire_write_unlocked():
                pass

    
    def _release_write_unlocked(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def release_write(self = None):
        self.base_lock
        self._release_write_unlocked()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    release = release_read
    acquire = acquire_read
    __enter__ = acquire
    
    def __exit__(self = None, *n, **kw):
        self.release()

    write_lock = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def locked(self = None):
        self.base_lock
        if not self.num_readers:
            None(None, None)
            return 
        with None:
            if not self.num_readers:
                pass
        bool

    
    def write_locked(self = None):
        self.base_lock
        None(None, None)
        return 
        with None:
            if not None, self.writer_request:
                pass



class PausableAction(object):
    
    def __init__(self = None, action = None):
        self._action = action
        self._lock = Lock()
        self._pauses = 0
        self._actionScheduled = False
        self._actionTaken = False
        self._args = None
        self._kw_args = None

    
    def pause(self = None):
        self._lock
        None(None, None)
        return None
        with None:
            if not self, self._pauses += 1, ._pauses:
                pass

    
    def unpause(self = None):
        self._lock
        if self._pauses <= 0:
            if self._actionScheduled:
                not (self._actionTaken) = self, self._pauses -= 1, ._pauses
                self._actionTaken = willTakeAction
                None(None, None)
            else:
                with None:
                    if not self._actionScheduled:
                        pass
                self, self._pauses -= 1, ._pauses
    # WARNING: Decompyle incomplete

    
    def __call__(self = None, *args, **kw_args):
        self._lock
        if self._actionScheduled:
            TRACE('Dropping second call to PausableAction')
            None(None, None)
            return None
        self._actionScheduled = None
        self._args = args
        self._kw_args = kw_args
        if self._pauses <= 0:
            if self._actionScheduled:
                willTakeAction = not (self._actionTaken)
                self._actionTaken = willTakeAction
                None(None, None)
            else:
                with None:
                    if not self._actionScheduled:
                        pass
    # WARNING: Decompyle incomplete

    paused = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

