# Source Generated with Decompyle++
# File: nucleus_decorators.pyc (Python 3.11)

import sys
import traceback
from functools import wraps
from typing import Any, Callable, TypeVar
from thin_client.exceptions import SERVICE_UNAVAILABLE_EXCEPTIONS
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import FailedFuture, Future
from dropbox.metrics.function_usage import logged_method
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException
from dropbox.trace import TRACE
_E = TypeVar('_E', bound = Exception)

def boundary_api(func = None):
    pass
# WARNING: Decompyle incomplete

