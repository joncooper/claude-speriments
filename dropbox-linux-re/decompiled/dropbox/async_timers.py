# Source Generated with Decompyle++
# File: async_timers.pyc (Python 3.11)

from __future__ import absolute_import
from collections import namedtuple
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.threading import Lock
from dropbox.timed_event import TimedEventDict, UploadTimedEventDict
_ASYNC_TIMERS_PARAMS = [
    ('desktop_login', 30000),
    ('screenshot', 30000),
    ('reconstruct_file', 86400000)]
_SUB_ASYNC_TIMERS_PARAMS = [
    (UploadTimedEventDict, ('commit_file', 86400000))]
_ASYNC_TIMERS_NAMES = _ASYNC_TIMERS_PARAMS()
_SUB_ASYNC_TIMERS_NAMES = _SUB_ASYNC_TIMERS_PARAMS()
_ASYNC_TIMERS_CLS = namedtuple('AsyncTimers', _ASYNC_TIMERS_NAMES + _SUB_ASYNC_TIMERS_NAMES)
_ASYNC_TIMERS = None
_ASYNC_TIMERS_LOCK = Lock()

def async_timers():
    _ASYNC_TIMERS_LOCK
# WARNING: Decompyle incomplete

DEFAULT_WAIT = 900

class EventTimeoutHandler(object):
    
    def __init__(self, wait_secs = (DEFAULT_WAIT,)):
        self.wait_secs = wait_secs
        self.last_call = 0

    
    def __call__(self):
        cur_time = get_monotonic_time_seconds()
        if cur_time > self.last_call + self.wait_secs:
            for timer_dict in async_timers():
                timer_dict.report_expired_events()
                self.last_call = cur_time
                return None
                return None


