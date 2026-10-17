# Source Generated with Decompyle++
# File: network_request_handling.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from time import time as _time
from typing import Callable, NamedTuple, Optional, Text, TypeVar, Union
from mypy_extensions import TypedDict
from dropbox.client.features.home_feed.shared.util.const import EXPECTED_ERRORS, NoopResponse, RateLimitExceeded
from dropbox.client.tray.tray_metrics.tray_network_request_metrics import report_sync_worker_metric, TrayMetricsEndpointName
from dropbox.client_api.exceptions import DropboxResponseClientError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.trace import TRACE
T = TypeVar('T')

def _check_for_noop_response(response_fut = None, request_name = None):
    result = None
    
    try:
        report_sync_worker_metric(request_name, response_fut.state(), EXPECTED_ERRORS, response_fut.exc_info() if response_fut.state() == Future.State.Exception else None)
    except DropboxResponseClientError:
        report_exception(severity = Severity.TRACE, component = DesktopComponent.TRAY)
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.TRAY)

    if response_fut.state() == Future.State.Exception:
        (_, exc, _) = response_fut.exc_info()
        if isinstance(exc, EXPECTED_ERRORS):
            result = NoopResponse()
            TRACE('Server request permanently failed with noop response for %s. Exception: %s', str(request_name), str(exc))
        if not result:
            TRACE('Server request permanently failed with non-noop response for %s. Exception: %s', str(request_name), str(exc))
            return FailedFuture(response_fut.exc_info())
    if response_fut.state() == Future.State.Cancelled:
        result = NoopResponse()
        TRACE('Server request was cancelled for %s.', str(request_name))
    else:
        result = response_fut.result()
    return ResolvedFuture(result)


def make_delayed_request_with_noop_handling(request_fn = None, request_name = None):
    return with_noop_handling(make_delayed_network_call(request_fn), request_name)


def with_noop_handling(fut = None, request_name = None):
    pass
# WARNING: Decompyle incomplete

RateLimitSettings = NamedTuple('RateLimitSettings', [
    ('time_window', int),
    ('runs_per_window', int)])
RateLimitState = TypedDict('RateLimitState', {
    'runs_available': float,
    'last_accrual_time': float,
    'accrual_rate': float })

class AssistantLossyRateLimiter(Actor):
    pass
# WARNING: Decompyle incomplete

