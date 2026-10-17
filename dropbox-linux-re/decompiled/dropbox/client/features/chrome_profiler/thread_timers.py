# Source Generated with Decompyle++
# File: thread_timers.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, NamedTuple, Optional
import psutil
from dropbox.platform import IS_MAC
from dropbox.trace import TRACE
if IS_MAC:
    import mac_thread_times
ThreadTimingTuple = NamedTuple('ThreadTimingTuple', [
    ('user_time', int),
    ('system_time', int)])
CachedThreadTimingData = NamedTuple('CachedThreadTimingData', [
    ('ts', int),
    ('data', Dict[(int, ThreadTimingTuple)])])
STALE_THRESHOLD_MICROSEC = 10000

def seconds_to_microseconds(sec = None):
    return int(sec * 1e+06)


class ThreadTimers(object):
    
    def __init__(self = None):
        self._process = psutil.Process()
        self._thread_fn = self._threads_mac if IS_MAC else self._threads_windows_and_linux
        self._cached_data = None

    
    def _threads_windows_and_linux(self = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self._process.threads()())

    
    def _threads_mac(self = None):
        return mac_thread_times.thread_times()()

    
    def get_timing_for_thread(self = None, thread_id = None, current_ts = None):
        if self._cached_data and current_ts - self._cached_data.ts < STALE_THRESHOLD_MICROSEC:
            return self._cached_data.data.get(thread_id)
        
        try:
            self._cached_data = CachedThreadTimingData(current_ts, self._thread_fn())
        except Exception:
            e = None
            TRACE('!!! failed to get threading info: %r', e)
            e = None
            del e
        except:
            e = None
            del e

        if self._cached_data:
            return self._cached_data.data.get(thread_id)


