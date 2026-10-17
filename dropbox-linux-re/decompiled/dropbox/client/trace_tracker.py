# Source Generated with Decompyle++
# File: trace_tracker.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from collections import OrderedDict
from datetime import date, timedelta
from typing import Any, Dict, FrozenSet, Set, Text

class TraceTracker(object):
    MAX_TRACE_PER_DAY = 1073741824
    MAX_TRACE_PER_MONTH = 10 * MAX_TRACE_PER_DAY
    CONFIG_KEY = 'trace_tracker'
    
    def __init__(self = None):
        self._bytes_sent_per_day = OrderedDict()
        self._total_bytes_sent_past_month = 0
        self._sent_trace_paths = set()

    
    def __setstate__(self = None, state = None):
        self._bytes_sent_per_day = state.get('_bytes_sent_per_day', OrderedDict())
        self._total_bytes_sent_past_month = state.get('_total_bytes_sent_past_month', 0)
        self._sent_trace_paths = state.get('_sent_trace_paths', set())

    
    def already_sent(self = None, trace_path = None):
        return trace_path in self._sent_trace_paths

    
    def over_trace_quota(self = None):
