# Source Generated with Decompyle++
# File: retry.pyc (Python 3.11)

from typing import Any, Callable, TypeVar
from dropbox.client_api.exceptions import TransientErrorType, TransientNetworkError
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures.basic import FailedFuture, Future
from dropbox.foundation.futures.sleep import sleep_async
T = TypeVar('T')

def default_legacy_retry(make_request = None, max_tries = None, backoff_period = None, max_backoff_period = (2, 15, 120)):
    pass
# WARNING: Decompyle incomplete

