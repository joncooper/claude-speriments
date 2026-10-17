# Source Generated with Decompyle++
# File: fp_client.pyc (Python 3.11)

from concurrent.futures import Future, InvalidStateError
from time import sleep
from typing import Any, Callable, Dict, Optional, Set, Text, Tuple, TypeVar
import tprt
from apex.metrics import Metric, MetricsReporter
from cffi_transport.exceptions import ServiceNotAvailableException
from Foundation import NSError, NSXPCConnection
from base import NucleusThinClientBase
from exceptions import NucleusConnectionInvalidatedError, NucleusConnectionTimeoutError
from dropbox.backoff import Backoff, TruncatedExponentialBackoff
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.mac.internal import autoreleasepool
from dropbox.model.types import NsId
from dropbox.proto.nucleus.app_service_tprt_client import NucleusAPIClient, NucleusPhaseAgnosticAPIClient
from dropbox.sqlite3_exceptions import ConnectionClosedError
from dropbox.sync_root.fp_helpers import fp_domain_id_from_local_config, fp_retrieve_boundary_connection
from dropbox.threading import Condition, Lock
from dropbox.trace import TRACE
CONNECTION_RETRIEVAL_TIMEOUT: 'Optional[float]' = None
RECONNECTION_RETRIEVAL_TIMEOUT = 5
INITIAL_CONNECTION_RETRIEVAL_SLEEP = 1
MAX_CONNECTION_RETRIEVAL_SLEEP = 60
CONNECTION_RETRIEVAL_BACKOFF_MULTIPLIER = 2
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_Result = TypeVar('_Result')

class NucleusFpThinClient(NucleusThinClientBase):
    
    def __init__(self, account, local_config, restart_fn = None, handle_fp_reconnected_fn = None, metrics_reporter = None, set_connecting_engine_status_label_fn = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'restart_fn', 'Callable[[], None]', 'handle_fp_reconnected_fn', 'Callable[[], None]', 'metrics_reporter', 'MetricsReporter', 'set_connecting_engine_status_label_fn', 'Callable[[bool], None]', 'return', 'None')):
        self._account = account
        self._local_config = local_config
        self._restart_fn = restart_fn
        self._connection_lock = Condition()
        self._handle_fp_reconnected_fn = None
        self._metrics_reporter = metrics_reporter
        self._in_progress_futures_lock = Lock()
        self._in_progress_futures = set()
        self._connection = None
        self._raw_client = None
        self._nucleus_client = None
        self._nucleus_phase_agnostic_client = None
        self._connection_retrieval_timer = self._metrics_reporter.create_timer(Metric('client_sync_events', 'fp_thin_client/connection_retrieval_time'), { })
        self._should_reset_connection_retrieval_timer = True
        self._connection_time_timer = self._metrics_reporter.create_timer(Metric('client_sync_events', 'fp_thin_client/connection_time'), { })
        self._connection_success_reporter = self._metrics_reporter.create_stats(Metric('client_sync_events', 'fp_thin_client/connection_success_rate'), { })
        set_connecting_engine_status_label_fn(True)
        TRACE('[FPClient] Retrieving connection, blocking until retrieved')
        self._last_connection_error = None
        self._connection_backoff_helper = TruncatedExponentialBackoff(INITIAL_CONNECTION_RETRIEVAL_SLEEP, MAX_CONNECTION_RETRIEVAL_SLEEP, CONNECTION_RETRIEVAL_BACKOFF_MULTIPLIER)
        self._retrieve_connection()
        self._wait_for_connection()
        self._handle_fp_reconnected_fn = handle_fp_reconnected_fn
        set_connecting_engine_status_label_fn(False)

    
    def root_ns(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_queue_stats(self = None):
        return { }

    
    def stop(self = None, stop_reason = None):
        pass

    
    def get_in_progress_futures_len(self = None):
        self._in_progress_futures_lock
        None(None, None)
        return 
        with None:
            if not None, len(self._in_progres