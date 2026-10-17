# Source Generated with Decompyle++
# File: timed_event.pyc (Python 3.11)

from __future__ import absolute_import, division
import sys
from collections import namedtuple
from contextlib import contextmanager
from time import time as _time
from typing import Any, Dict, Iterable, Iterator, Sequence, Text
import psutil
from mypy_extensions import TypedDict
from six import integer_types, iteritems
from six.moves import zip
from build_number import dropbox_version
from dropbox.assertions import assert_
from dropbox.client.device_info import get_process_start_time
from dropbox.client_api.hashing import get_block_size, split_blocklist
from dropbox.event import report
from dropbox.functions import make_bytes, make_unicode
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.repr_utils import easy_repr
from dropbox.threading import Lock
from dropbox.trace import TRACE

class TimedEventBase:
    
    def __init__(self = None, **info):
        pass

    
    def info(self = None, name = None, value = None):
        pass

    
    def update(self = None, **info):
        pass

    
    def event(self = None, name = None):
        pass

    timed_event = (lambda self = None, name = None: pass# WARNING: Decompyle incomplete
)()


class TimedEvent(TimedEventBase):
    __slots__ = ('start_time', 'report')
    
    def __init__(self = None, **info):
        self.start_time = get_monotonic_time_seconds() * 1000
        self.report = { }
    # WARNING: Decompyle incomplete

    
    def info(self = None, name = None, value = None):
        self.report[name] = value

    
    def update(self = None, **info):
        self.report.update(info)

    
    def event(self = None, name = None):
        k = name + '_time'
        self.report[k] = int(get_monotonic_time_seconds() * 1000 - self.start_time)
        return self.report[k]

    
    def count(self = None, name = None):
        key = name + '_count'
        if key not in self.report:
            self.report[key] = 1
            return None
        old_val = None.report[key]
    # WARNING: Decompyle incomplete

    timed_event = (lambda self = None, name = None: pass# WARNING: Decompyle incomplete
)()
    
    def __repr__(self = None):
        pass
    # WARNING: Decompyle incomplete


# WARNING: Decompyle incomplete
