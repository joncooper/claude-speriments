# Source Generated with Decompyle++
# File: perf_session.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import binascii
import collections
import contextlib
import os
import random as insecure_random
import time
from typing import Callable, Deque, Dict, Generator, List, Optional, Text, TypeVar
from build_number import dropbox_version
from typing_extensions import Literal
from dropbox.client.flow_tracker import FlowTracker
from dropbox.client.system_status.system_monitor_wrapper import SystemStatusMonitorWrapper
from dropbox.event import report
from dropbox.event_names import PERF_SESSIONS_EVENT
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures.basic import Future
from dropbox.foundation.performance.bridge_gen.bridge_interface_perf_session import PerfSessionBridgeInterface
from dropbox.foundation.performance.bridge_gen.checkpoint_behavior import CheckpointBehavior
from dropbox.foundation.performance.bridge_gen.if_ended import IfEnded
from dropbox.foundation.performance.bridge_gen.on_dupe import OnDupe
from dropbox.foundation.performance.bridge_gen.perf_session_amp_logging_namespace import PerfSessionAmpLoggingNamespace
from dropbox.foundation.performance.bridge_gen.perf_session_data import PerfSessionData
from dropbox.foundation.performance.bridge_gen.timing_record import TimingRecord
from dropbox.foundation.performance.checkpoint_strategy import NullCheckpointStrategy, PerfSessionCheckpointStrategy
from dropbox.foundation.performance.interface import PerfSessionInterface
from dropbox.foundation.performance.perf_session_amp import PerfSessionAMPMetrics
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.functions import make_unicode
from dropbox.stopwatch import global_sw
from dropbox.threading import Lock
_T = TypeVar('_T')
_V = TypeVar('_V')

def get_perf_timestamp():
    return time.perf_counter()

PERF_SESSION_DATA_BUFFER_SIZE = 1000

class PerfSession(PerfSessionInterface):
    pass
# WARNING: Decompyle incomplete

RACY_OPTIONAL_CHECKPOINT = CheckpointBehavior(on_dupe = OnDupe.ASSERT, if_ended = IfEnded.IGNORE)
perf_session_stopwatch_span = (lambda perf_session = None, span_name = None: pass# WARNING: Decompyle incomplete
)()
