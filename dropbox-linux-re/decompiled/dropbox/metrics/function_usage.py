# Source Generated with Decompyle++
# File: function_usage.pyc (Python 3.11)

from contextlib import contextmanager
from datetime import datetime
from functools import wraps
from time import monotonic
from typing import Any, Callable, cast, Dict, Generator, Generic, List, Optional, Tuple, TypeVar
from apex.metrics import Metric, MetricsReporter, Stats
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, ResolvedFuture
_Func = TypeVar('_Func', bound = Callable[(..., Any)])
_Result = TypeVar('_Result')

class FuncMetricsMixin:
    
    def __init__(self, reporter, metric = None, kill_switch = None, amp_tags_factory = None, tags_update_interval_sec = (None, None, 3600, True), use_event_tags = ('reporter', 'MetricsReporter', 'metric', 'Metric', 'kill_switch', 'Optional[Callable[[], bool]]', 'amp_tags_factory', 'Optional[Callable[[], Dict[str, str]]]', 'tags_update_interval_sec', 'Optional[float]', 'use_event_tags', 'Optional[bool]')):
        self._FuncMetricsMixin__metric = metric
        self._FuncMetricsMixin__reporter = reporter
        self._FuncMetricsMixin__loggers = { }
    # WARNING: Decompyle incomplete

    
    def flush_metrics(self = None):
        for logger in self._FuncMetricsMixin__loggers.values():
            logger.flush_all()
            return None

    
    def logged_function(self = None, func_name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __log_freq_sample(self = None, event = None):
        if event not in self._FuncMetricsMixin__loggers:
            self._FuncMetricsMixin__loggers[event] = FrequencyLogger(self._FuncMetricsMixin__reporter, self._make_metric(event), self._make_tags(event))
        self._FuncMetricsMixin__loggers[event].log_sample(datetime.now())

    
    def __log_future_completion(self = None, event = None, fut = None):
        pass
    # WARNING: Decompyle incomplete

    __log_wall_time_and_errors = (lambda self = None, event = None: pass# WARNING: Decompyle incomplete
)()
    
    def _make_tags(self = None, event = None, exc_type = None):
        if self._FuncMetricsMixin__use_event_tags:
            event_tags = {
                'exception_type': exc_type,
                'event': event } if exc_type else {
                'event': event }
        elif exc_type:
            pass
        
        event_tags = { }
        if not self._cached_tag:
            return event_tags
    # WARNING: Decompyle incomplete

    
    def _make_metric(self = None, event = None, metric_name_suffix = None):
        if self._FuncMetricsMixin__use_event_tags:
            return Metric(self._FuncMetricsMixin__metric.ns, self._FuncMetricsMixin__metric.name + metric_name_suffix)
        return Metric(self._FuncMetricsMixin__metric.ns, self._FuncMetricsMixin__metric.name + event + '/' + metric_name_suffix)


_MF = TypeVar('_MF', bound = Callable[(..., Any)])

def logged_method(func = None):
    pass
# WARNING: Decompyle incomplete


class FrequencyLogger:
    
    def __init__(self = None, reporter = None, metric = None, tags = ('reporter', 'MetricsReporter', 'metric', 'Metric', 'tags', 'Dict[str, str]')):
        self._last_sample = None
        self._time_struct_indices_and_labels = [
            (7, 'd'),
            (3, 'h'),
            (4, 'm'),
            (5, 's')]
        self._buckets = self._make_buckets(reporter, metric, tags)
        self._counts = self._make_counts()

    
    def log_sample(self = None, ts = None):
        curr = ts.timetuple()
    # WARNING: Decompyle incomplete

    
    def flush_all(self = None):
        for i, recorder in self._buckets:
            recorder.record(self._counts[i])
            self._counts = self._make_counts()
            return None

    
    def _make_counts(self = None):
        count_dict = dict()
        for i, _ in self._time_struct_indices_and_labels:
            count_dict[i] = 0
            return count_dict

    
    def _make_buckets(self = None, reporter = None, metric = None, tags = ('reporter', 'MetricsReporter', 'metric', 'Metric', 'tags', 'Dict[str, str]', 'return', 'List[Tuple[int, Stats]]')):
        pass
    # WARNING: Decompyle incomplete



def CachedThunk():
    '''CachedThunk'''
    
    def __init__(self = None, thunk = None, time_func = None, interval = ('thunk', 'Callable[[], _Result]', 'time_func', 'Callable[[], float]', 'interval', 'float')):
        self._thunk = thunk
        self._time_func = time_func
        self._interval = interval
        self._value = thunk()
        self._last_thunked = time_func()

    
    def __call__(self = None):
        current_time = self._time_func()
        if current_time - self._last_thunked > self._interval:
            self._value = self._thunk()
            self._last_thunked = current_time
        return self._value


CachedThunk = <NODE:27>(CachedThunk, 'CachedThunk', Generic[_Result])
