# Source Generated with Decompyle++
# File: trace.pyc (Python 3.11)

import contextlib
import functools
import os
import sys
import threading
import traceback
from pprint import pformat
from typing import Any, Callable, cast, Dict, Iterator, List, Optional, Text, TypeVar, Union
from apex.util import rust_thread_name
from six import iteritems, reraise, string_types
import build_number
from dropbox.account_context import deduce_account
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.handler_registries import _trace_handler, run_trace_handlers
from dropbox.trace_filter import TraceFilter
EMPHASIS_PREFIX = '!!'
SQL_PREFIX = 'SQL:'

class TraceSegment:
    __slots__ = ('emphasis', 'host_int', 'filename', 'lineno', 'threadname', 'segment', '_preformatted')
    
    def __init__(self, host_int, filename = None, lineno = None, threadname = None, seg = (False,), emphasis = ('host_int', 'int', 'filename', 'Text', 'lineno', 'int', 'threadname', 'Text', 'seg', 'bytes', 'emphasis', 'bool', 'return', 'None')):
        self.host_int = host_int if host_int else ''
        self.filename = filename
        self.lineno = lineno
        self.threadname = threadname
        self.segment = seg
        self.emphasis = emphasis
        self._preformatted = None

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete



def debugging_run_type():
    return os.getenv('DBDEV_RUN_TYPE')

_trace_filter: 'Optional[TraceFilter]' = None

def TRACE(string = None, *n, **kw):
    pass
# WARNING: Decompyle incomplete

CallableT = TypeVar('CallableT', bound = Callable)

def redact_pii(value = None):
    pass
# WARNING: Decompyle incomplete


def trace_call(f = None):
    pass
# WARNING: Decompyle incomplete


def trace_stack():
    '%s'('\n'.join, (lambda .0: pass# WARNING: Decompyle incomplete
)(''.join(traceback.format_stack()).split('\n')()))


def trace_locals(_locals = None):
    
    try:
        for k, v in iteritems(_locals):
            TRACE('!! %s : %s,', k, pformat(v)[:1000])
            
            try:
                continue
                except Exception:
                    TRACE('!! %s : <bad repr>,', k)
                    
                    try:
                        continue
                        
                        try:
                            return None
                        except Exception:
                            TRACE('!! trace_locals: error iterating on %r', _locals)
                            return None
                            except Exception:
                                TRACE('!! trace_locals: <bad repr>')
                                return None






def reraise_exc_handler():
    exc = sys.exc_info()
# WARNING: Decompyle incomplete

_is_debugging = True

def set_debugging(bool_ = None):
    global _is_debugging
    _is_debugging = bool_


def is_debugging():
    return _is_debugging

_is_thread_profiling = False

def set_thread_profiling(bool_ = None):
    global _is_thread_profiling
    _is_thread_profiling = bool_


def is_thread_profiling():
    return _is_thread_profiling

debugging_override = (lambda on = None: pass# WARNING: Decompyle incomplete
)()

def DEVELOPER_WARNING(str_ = None, *n):
    
    try:
        calling_frame = traceback.extract_stack(limit = 2)[-2]
        filename = calling_frame.filename
        lineno = calling_frame.lineno
    except IndexError:
        filename = '???'
        lineno = 0

# WARNING: Decompyle incomplete


def WARNING(str_ = None, *n):
    
    try:
        calling_frame = traceback.extract_stack(limit = 2)[-2]
        filename = calling_frame.filename
        lineno = calling_frame.lineno
    except IndexError:
        filename = '???'
        lineno = 0

# WARNING: Decompyle incomplete


def trace_threads():
    for frame in sys._current_frames().values():
        TRACE('!! **** %r ********', frame)
        '%s'('\n'.join, (lambda .0: pass# WARNING: Decompyle incomplete
)(''.join(traceback.format_stack(frame)).split('\n')()))
        return None


def format_stack_frame(th = None):
    pass
# WARNING: Decompyle incomplete


def dump_python_stacks():
    formatted_str = ''
    th = threading.current_thread()
# WARNING: Decompyle incomplete


class Tracer(object):
    _pre_initialized_buffer_lock = threading.Lock()
    _pre_initialized_buffer: 'List[Text]' = []
    _trace_handler_lock = threading.RLock()
    warning = (lambda str_ = None: pass# WARNING: Decompyle incomplete
)()
    info = (lambda string = None: if n:
try:
string %= nexcept Exception:
string = '!! Bad trace formatting from line: ' + string + ' with args' + repr(n)if not isinstance(string, string_types):
string = '!! PLEASE FIX: TRACE was called with non-string %r' % string# WARNING: Decompyle incomplete
)()
    debug = (lambda str_ = None: pass# WARNING: Decompyle incomplete
)()
    _handle_trace = (lambda segs = None: first = next(segs)if first.emphasis:
Tracer._trace_handler_lockrun_trace_handlers(first)for seg in segs:
run_trace_handlers(seg)None(None, None)Nonewith None:
if not None:
passNonerun_trace_handlers(first)for seg in segs:
Tracer._trace_handler_lockrun_trace_handlers(seg)None(None, None)with None:
if not None:
passcontinue)()


def construct_structured_trace(trace = None, **kw):
    pass
# WARNING: Decompyle incomplete

