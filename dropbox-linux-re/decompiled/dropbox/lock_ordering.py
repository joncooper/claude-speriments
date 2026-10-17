# Source Generated with Decompyle++
# File: lock_ordering.pyc (Python 3.11)

from __future__ import absolute_import
import contextlib
import functools
import gc
import itertools
import os
import pprint
import threading
import time
import traceback
from collections import defaultdict
from typing import Any, Callable, DefaultDict, Dict, Iterable, List, Optional, Set, Tuple, Type
from dropbox.threading import Lock
from dropbox.trace import TRACE
BROKEN_LOCK_TRACING = False

class _OrderedLock:
    
    def __init__(self, tracker, base_lock, acquire_methods = None, release_methods = None, fname = None, line_no = ((),), context_managers = ('tracker', "'OrderedLockTracker'", 'base_lock', 'Any', 'acquire_methods', 'Tuple[str, ...]', 'release_methods', 'Tuple[str, ...]', 'fname', 'str', 'line_no', 'str', 'context_managers', 'Tuple[Tuple[str, str, str], ...]')):
        self.base_lock = base_lock
        self.tracker = tracker
        self.fname = fname
        self.line_no = line_no
        for maker, methods in ((self.make_acquirer, acquire_methods), (self.make_releaser, release_methods)):
            for method_name in methods:
                setattr(self, method_name, maker(method_name))
                self.default_acquire = getattr(self, acquire_methods[0])
                self.default_release = getattr(self, release_methods[0])
                for context_manager, acquire_method, release_method in context_managers:
                    setattr(self, context_manager, functools.partial(self.context_manager_factory, getattr(self, acquire_method), getattr(self, release_method)))
                    return None

    context_manager_factory = (lambda self, acquire_fn, release_fn: pass# WARNING: Decompyle incomplete
)()
    
    def make_acquirer(self = None, method_name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def make_releaser(self = None, method_name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self):
        self.default_acquire()

    
    def __exit__(self, *n, **kw):
        self.default_release()

    
    def __getattr__(self, name):
        return getattr(self.base_lock, name)

    
    def __repr__(self):
        return f'''<OrderedLock {self.base_lock!r}>'''



def _just_raise(string):
    raise Exception(string)


class NonRecursiveLockRecursionError(Exception):
    pass
# WARNING: Decompyle incomplete


class NonRecursiveLock(object):
    
    def __init__(self = None, base_lock = None, acquire_methods = None, release_methods = (None, ('acquire',), ('release',))):
        if not base_lock:
            pass
        self.lock = Lock()
        self.local = threading.local()
        for maker, method_names in ((self.make_acquirer, acquire_methods), (self.make_releaser, release_methods)):
            for method_name in method_names:
                setattr(self, method_name, maker(method_name))
                self.default_acquire = getattr(self, acquire_methods[0])
                self.default_release = getattr(self, release_methods[0])
                return None

    
    def locked(self):
        return self.lock.locked()

    
    def make_acquirer(self, method_name):
        pass
    # WARNING: Decompyle incomplete

    
    def make_releaser(self, method_name):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self):
        self.default_acquire()

    
    def __exit__(self, *n, **kw):
        self.default_release()

    
    def __getattr__(self, name):
        return getattr(self.lock, name)



class OrderedLockTracker(object):
    
    def __init__(self = None, action = None, default_lock_type = None):
        self.local = threading.local()
        self.parent_child_lock = threading.RLock()
        self.parent_child_map = { }
        self.child_parent_map = { }
        if not action:
            
            def action(a, b, msg):
                return _just_raise(msg)

        self.action = action
        self.handling = False
        self.default_lock_type = default_lock_type
        if BROKEN_LOCK_TRACING:
            self.broken_lock_pairs = _make_lookup_table(_read_broken_locks())
            return None
        self.broken_lock_pairs = None

    
    def allocate_lock(self, base_lock, acquire_methods = None, release_methods = None, fname = None, line_no = (None, ('acquire',), ('release',), '', '', ()), context_managers = ('base_lock', 'Any', 'acquire_methods', 'Tuple[str, ...]', 'release_methods', 'Tuple[str, ...]', 'fname', 'str', 'line_no', 'str', 'context_managers', 'Tuple[Tuple[str, str, str], ...]', 'return', '_OrderedLock')):
