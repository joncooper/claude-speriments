# Source Generated with Decompyle++
# File: interrupt_counter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from dropbox.monotonic_time import get_monotonic_time_seconds

class InterruptCounter:
    DEFAULT_MAX_INTERRUPT_TIME = 86400
    
    def __init__(self = None, max_time = None):
        self._max_time = max_time
        self._prev_time = None
        self.count = 0

    
    def increment(self = None):
        current_time = get_monotonic_time_seconds()
        if self._prev_time and current_time - self._prev_time < self._max_time:
            return None
        None = None
        self._prev_time = current_time


