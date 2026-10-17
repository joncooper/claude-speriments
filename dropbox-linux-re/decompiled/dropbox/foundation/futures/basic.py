# Source Generated with Decompyle++
# File: basic.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import abc
import hashlib
import os
import sys
import threading
import traceback
from contextlib import contextmanager
from enum import Enum
from typing import Any, Callable, cast, Dict, Generic, Iterator, List, Mapping, Optional, overload, Text, Tuple, Type, TypeVar, Union
import six
from build_number import dropbox_version, is_frozen, is_test
from build_number.features import feature_enabled
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.severity import Severity
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.exception_info import ExcInfo, OptExcInfo, typed_exc_info
from dropbox.foundation.reporting import report_app_framework_event
from dropbox.foundation.runtime import Interpreter, panic_with_report
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_bytes
from dropbox.monotonic_time import get_monotonic_time_seconds as time
from dropbox.overrides import report_bad_assumption
from dropbox.sync_engine_boundary.constants import BOUNDARY_FUTURE_COMPLETION_THREAD_POOL, BOUNDARY_PUBLISHED_EVENTS_THREAD_POOL
from dropbox.threading import Condition, Lock
from dropbox.trace import TRACE
_T = TypeVar('_T')
_U = TypeVar('_U')
_Tco = TypeVar('_Tco', covariant = True)
_C = TypeVar('_C', bound = Callable[(..., object)])
_E = TypeVar('_E', bound = Exception)
_K = TypeVar('_K')
_V = TypeVar('_V')
FORCE_FUTURE_HANDLING_IN_TEST = False

class _Data(threading.local):
    pass
# WARNING: Decompyle incomplete

_DATA = _Data()

def blocking_on_main_thread_allowed():
