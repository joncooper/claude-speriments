# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import abc
import datetime as dt
from dataclasses import dataclass
from types import TracebackType
from typing import Mapping
TagSet = Mapping[(str, str)]
Metric = <NODE:12>()

class Stats(abc.ABC):
    record = (lambda self = None, value = None: pass)()
    record_duration = (lambda self = None, value = None: pass)()


class Timer(abc.ABC):
    reset = (lambda self = None: pass)()
    record = (lambda self = None: pass)()


class Counter(abc.ABC):
    reset = (lambda self = None: pass)()
    increment = (lambda self = None, value = None: pass)()
    record = (lambda self = None: pass)()
    decrement = (lambda self = None, value = None: pass)()


class Set(abc.ABC):
    observe = (lambda self = None, value = None: pass)()


class MetricsReporter(abc.ABC):
    child = (lambda self = None, tags = None: pass)()
    create_stats = (lambda self = None, metric = None, tags = abc.abstractmethod: pass)()
    create_timer = (lambda self = None, metric = None, tags = abc.abstractmethod: pass)()
    create_counter = (lambda self = None, metric = None, tags = abc.abstractmethod: pass)()
    create_set = (lambda self = None, metric = None, tags = abc.abstractmethod: pass)()

