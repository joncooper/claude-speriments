# Source Generated with Decompyle++
# File: UDCL.pyc (Python 3.11)

import random as insecure_random
from collections import deque
from typing import Callable, Deque, NamedTuple, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.logging_event import _GenericLoggingEvent, NonUserLoggingEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.threading import Lock
from dropbox.trace import TRACE
Span = NamedTuple('Span', [
    ('start', int),
    ('end', int)])
SpanCacheItem = NamedTuple('SpanCacheItem', [
    ('key', str),
    ('start', int)])
LoggerFunction = Callable[([
    _GenericLoggingEvent,
    Optional[AccountInterface]], None)]
CACHE_SIZE = 8192
HIVE_ERROR_SAMPLE_RATE = 0.0001

def get_current_time_ms():
    return round(1000 * get_monotonic_time_seconds())


class UDCLSpanManager:
    _starts_cache: 'Deque[SpanCacheItem]' = deque(maxlen = CACHE_SIZE)
    _lock = Lock()
    _has_logged_eviction: 'bool' = False
    _has_logged_start_not_found: 'bool' = False
    _logger: 'Optional[LoggerFunction]' = None
    register_logger = (lambda cls = None, logger = None: cls._logger = logger)()
    _log_cache_eviction = (lambda cls = None, cache_item = None: pass# WARNING: Decompyle incomplete
)()
    _log_start_not_found = (lambda cls = None, key = None: pass# WARNING: Decompyle incomplete
)()
    start_span = (lambda cls = None, key = None, manual_timestamp_ms = classmethod: TRACE('UDCLSpanManager.start_span for %s', key)cls._lockif not manual_timestamp_ms:
current_time = get_current_time_ms()if len(cls._starts_cache) == cls._starts_cache.maxlen:
removed_item = cls._starts_cache.popleft()cls._log_cache_eviction(removed_item)cls._starts_cache.append(SpanCacheItem(key = key, start = current_time))None(None, None)Nonewith None:
if not None:
pass)()
    finish_span = (lambda cls = None, key_to_measure = None, manual_timestamp_ms = classmethod: TRACE('UDCLSpanManager.finish_span searching for %s', key_to_measure)cls._lockfor item in cls._starts_cache:
if item.key == key_to_measure:
if not manual_timestamp_ms:
end_time = get_current_time_ms()ret_value = Span(start = item.start, end = end_time)cls._starts_cache.remove(item)TRACE('UDCLSpanManager.finish_span %s', ret_value)None(None, None)cls._log_start_not_found(key_to_measure)None(None, None)Nonewith None:
if not None:
pass)()
    reset = (lambda cls = None: cls._lockcls._starts_cache.clear()cls._has_logged_eviction = Falsecls._has_logged_start_not_found = FalseNone(None, None)Nonewith None:
if not None:
pass)()

