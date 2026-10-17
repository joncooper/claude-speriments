# Source Generated with Decompyle++
# File: trace_report.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import re
import sys
import threading
import time
import traceback
from collections import OrderedDict
from hashlib import md5
from typing import cast, List, Optional, Text, Tuple
from apex.panic import RustPanicError
from dropbox.exception.exceptions import JavascriptError, PythonBridgeError
MYPY = False
if MYPY:
    from dropbox.exception import ExcInfo
MAX_REPORT_LENGTH = 16384

try:
    import pywintypes
except Exception:
    pywintypes = None

_RANDOM_URI_HOST = re.compile(Text('(?P<scheme>[-+.a-zA-Z0-9()<> _$]+)://[0-9a-f]{32}'))
_QUERY_AND_FRAGMENT = re.compile(Text('[?#].*$'))

def _get_normalized_stack_and_hash(stack_list = None):
    stack = ''.join(stack_list)
    stack = _RANDOM_URI_HOST.sub('\\g<scheme>://random_host', stack)
    stack = _QUERY_AND_FRAGMENT.sub('', stack)
    stack = stack.replace('\\', '/').replace('.pyc"', '.py"').replace('.pyo"', '.py"').replace('"dropbox/_sync_engine_packages/release_candidate/', '"dropbox/sync_engine/').replace('"dropbox/_sync_engine_packages/stable/', '"dropbox/sync_engine/')
    hash = md5(stack.encode('utf-8')).hexdigest()
    return (stack, hash)


def make_python_report(exc_info = None):
    (exc_type, val, tb) = exc_info
    formatted_exc = traceback.format_exception(exc_type, val, tb)
# WARNING: Decompyle incomplete


def make_javascript_report(exc_info = None):
    pass
# WARNING: Decompyle incomplete


def make_real_javascript_report(js_stack_trace = None):
    (report, stack_hash) = _get_normalized_stack_and_hash([
        js_stack_trace])
    report = 'JavaScript Exception\n' + report
    return (report, stack_hash)


def make_mixed_report(exc_info = None):
    pass
# WARNING: Decompyle incomplete


def make_report(exc_info = None):
    pass
# WARNING: Decompyle incomplete


class ExceptionCounter(object):
    
    def __init__(self = None, capacity = None, trace_interval = None):
        self._exceptions = OrderedDict()
        self._exceptions_lock = threading.Lock()
        self.capacity = capacity
        self.trace_interval = trace_interval

    
    def record_exception(self = None, exc_hash = None):
        cur_time = time.time()
        self._exceptions_lock
        if exc_hash not in self._exceptions:
            self._exceptions[exc_hash] = (cur_time, 1)
            if len(self._exceptions) > self.capacity:
                self._exceptions.popitem(last = False)
            None(None, None)
            return (True, 1)
        (last_logged_time, count) = None._exceptions.pop(exc_hash)
        if cur_time - last_logged_time > self.trace_interval:
            self._exceptions[exc_hash] = (cur_time, 1)
            None(None, None)
            return 
        None(None, None)
        return 
        with None:
            if not (None, count + 1, self._exceptions[exc_hash]), (False, count):
                pass


