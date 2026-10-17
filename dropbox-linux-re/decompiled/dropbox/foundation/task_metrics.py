# Source Generated with Decompyle++
# File: task_metrics.pyc (Python 3.11)

from __future__ import annotations
import os
import random as insecure_random
from abc import abstractmethod
from contextlib import contextmanager
from enum import Enum
from functools import partial
from threading import current_thread
from time import perf_counter
from typing import Callable, Dict, Iterator, List, NamedTuple, Optional, OrderedDict, Text, Tuple, Union
from apex.metrics import Counter, Metric, MetricsReporter, Stats
from build_number import dropbox_version, is_test
from build_number.channel import BuildChannel
from trace import TRACE
from dropbox.components.desktop_components import DesktopComponent
from dropbox.threading import Lock

def is_run_box():
    return os.environ.get('RUN_BOX', None) == 'USING_RUN_BOX'


class TaskEventName(Enum):
    INITIAL = 'initial'
    QUEUED = 'queued'
    STARTED = 'started'
    ENDED = 'ended'


class TaskLifecycleName(Enum):
    DELAY = 'task_delay_sec'
    EXECUTION = 'task_execution_sec'

METRIC_NAMESPACE = 'desktop_threading_performance'
# WARNING: Decompyle incomplete
