# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)

from __future__ import absolute_import, division
import re
from collections import deque
from typing import Any, Callable, Deque, Dict, Optional, Set, Text, Tuple
from six import integer_types, iteritems
from build_number import is_test
from dropbox.assertions import assert_
from dropbox.functions import make_unicode
from dropbox.observable import watchable
from dropbox.threading import Lock
from dropbox.trace import TRACE
AGGREGATE_TIMEOUT = 3600
TABLE_NAME_REGEXP = re.compile(make_unicode('^[a-z0-9\\_\\-]*$'))
_DEFERRED_REPORTS: 'Optional[Deque[Tuple[str, bool, Dict[str, object]]]]' = None if is_test() else deque(maxlen = 10)
_REPORTING_LOCK = Lock()
_process_report = (lambda data_name = None, trace = None: pass# WARNING: Decompyle incomplete
)()

def report(data_name = None, trace = None, **info):
    pass
# WARNING: Decompyle incomplete


def add_report_handler(handler = None):
    _process_report.pre.add_handler(handler)


def _get_deferred_reports():
    pass
# WARNING: Decompyle incomplete


def flush_deferred_reports():
    _REPORTING_LOCK
# WARNING: Decompyle incomplete

report_aggregate_event = (lambda data_name = None, data = None, ts = watchable(), approx_timeout = (None, AGGREGATE_TIMEOUT): pass# WARNING: Decompyle incomplete
)()

def sanitize_event_extra_dict(extra_dict = None):
    updated_dict = { }
# WARNING: Decompyle incomplete


def sanitize_event_extra_dict_and_ensure_whitelisted(extra_dict = None, whitelist_fields = None):
    pass
# WARNING: Decompyle incomplete


def make_decorated_exception_name(error = None):
    errclass = error.__class__.__name__
    
    def _get_errno(error = None, attr_name = None):
        if not hasattr(error, attr_name):
            return None
        v = getattr(error, attr_name)
        return v if isinstance(v, integer_types) else None

    for attr_name in ('unsigned_err', 'winerror', 'errno'):
        errno = _get_errno(error, attr_name)
        if errno:
            fmt = '%s_%d' if errno < 16000 else '%s_0x%08x'
            
            return None, fmt % (errclass, errno)
        return errclass

