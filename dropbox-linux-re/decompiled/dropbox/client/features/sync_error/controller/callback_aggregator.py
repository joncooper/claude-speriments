# Source Generated with Decompyle++
# File: callback_aggregator.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import math
from abc import ABC, abstractmethod
from time import sleep
from typing import Callable, Generic, Iterator, List, Optional, TypeVar
from apex.metrics import Metric, MetricsReporter
from dropbox.client.features.sync_error.controller.ordered_set import OrderedSet
from dropbox.client.sync_ui_update_thread import SyncUIUpdateThread
from dropbox.exception.reporting import report_rare_event
from dropbox.metrics.function_usage import FuncMetricsMixin, logged_method
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.threading import Lock
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
_CBArgs = TypeVar('_CBArgs')
_PerItemCallback = Callable[([
    _CBArgs], None)]
_PerBatchCallback = Callable[([], None)]
_AMP_NAMESPACE = 'client_sync_errors'

def CallList():
    '''CallList'''
    __len__ = (lambda self = None: pass)()
    __iter__ = (lambda self = None: pass)()
    pop_n = (lambda self = None, count = None: pass)()
    add = (lambda self = None, item = None: pass)()

CallList = <NODE:27>(CallList, 'CallList', ABC, Generic[_CBArgs])

def BasicCallList():
    '''BasicCallList'''
    
    def __init__(self = None):
        self._data = []

    
    def __iter__(self = None):
        return self._data.__iter__()

    
    def __len__(self = None):
        return len(self._data)

    
    def add(self = None, item = None):
        self._data.append(item)

    
    def pop_n(self = None, count = None):
        count = min(len(self), count)
        next_items = self._data[0:count]
        remaining_items = self._data[count:]
        self._data = remaining_items
        return next_items


BasicCallList = <NODE:27>(BasicCallList, 'BasicCallList', CallList, Generic[_CBArgs])

def DeduplicatingCallList():
    '''DeduplicatingCallList'''
    
    def __init__(self = None):
        self._data = OrderedSet()

    
    def __len__(self = None):
        return len(self._data)

    
    def __iter__(self = None):
        return self._data.__iter__()

    
    def add(self = None, item = None):
        self._data.add(item)

    
    def pop_n(self = None, count = None):
        next_items = []
        for _ in range(count):
            if len(self._data) == 0:
                pass
            else:
                next_items.append(self._data.pop(last = False))
            return next_items


DeduplicatingCallList = <NODE:27>(DeduplicatingCallList, 'DeduplicatingCallList', CallList, Generic[_CBArgs])

def BatchCallbackAggregator():
    '''BatchCallbackAggregator'''
    pass
# WARNING: Decompyle incomplete

BatchCallbackAggregator = <NODE:27>(BatchCallbackAggregator, 'BatchCallbackAggregator', Generic[_CBArgs], FuncMetricsMixin)
