# Source Generated with Decompyle++
# File: transport_adapter.pyc (Python 3.11)

import datetime as dt
import random as insecure_random
import threading
from concurrent.futures import Future
from typing import Any, Callable, Optional, Sequence, Text, Type
import tprt
from apex.metrics import Metric, MetricsReporter
from apex.panic import is_panicking
from cffi_transport.cffi_interface import CFFIInterface
from cffi_transport.exceptions import ServiceError, ServiceNotAvailableException
from cffi_transport.transport import TransportChannel
from cffi_transport.utilities import get_method_name
from google.protobuf.descriptor import MethodDescriptor
from google.protobuf.message import Message
from google.protobuf.service import RpcChannel, RpcController, Service
from build_number import BuildChannel, dropbox_version, is_frozen, is_test
from exceptions import NucleusClientError
from logging import create_metrics_reporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.exceptions import NucleusPanicException
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.overrides import report_bad_assumption
from dropbox.proto.nucleus.app_service_tprt_client import NucleusAPIClient, NucleusPhaseAgnosticAPIClient
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.threadutils import is_main_thread
from dropbox.trace import TRACE
MAIN_THREAD_DELAY_THRESHOLD = 5
RECV_EVENTS_THREAD_NAME = 'RECV_EVENTS'
API_LATENCY_SAMPLE_RATE = {
    BuildChannel.stable: 1e-05,
    BuildChannel.beta: 0.001,
    BuildChannel.internal_alpha: 0.1 }.get(dropbox_version.channel, 0.001)

def _assert_safe_to_make_blocking_call(cb_thread_names = None):
    thread_name = threading.current_thread().name
# WARNING: Decompyle incomplete


class NucleusTransportAdapter(TransportChannel):
    pass
# WARNING: Decompyle incomplete


def forward_tprt_exception(exception_class = None, method_name = None, base_expection = None):
    
    try:
        new_msg = 'tprt exception endpoint = {}'.format(method_name)
        if base_expection:
            raise exception_class(new_msg), base_expection
        raise exception_class(new_msg)
    except exception_class:
        e = None
        del e
        return None
        None = 
        del e



class NucleusTprtTransportAdapter(RpcChannel):
    
    def __init__(self = None, raw_tprt_client = None, amp_metrics_reporter = None, backup_mode = ('raw_tprt_client', 'tprt.Client', 'amp_metrics_reporter', 'MetricsReporter', 'backup_mode', 'Optional[BackupModeArgs]', 'return', 'None')):
        self._nucleus_client = NucleusAPIClient(raw_tprt_client)
        self._nucleus_phase_agnostic_client = NucleusPhaseAgnosticAPIClient(raw_tprt_client)
        self._amp_metrics_reporter = amp_metrics_reporter
        self._amp_ns = 'client_bkup_sync_events' if backup_mode else 'client_sync_events'

    
    def trace(self = None, method_name = None, msg = None):
        TRACE('TPRT [%r] - %r', method_name, msg)

    
    def CallMethod(self, method_descriptor, rpc_controller = None, request = None, response_class = None, done = ('method_descriptor', 'MethodDescriptor', 'rpc_controller', 'RpcController', 'request', 'Message', 'response_class', 'Type[Message]', 'done', 'Optional[Callable[[Message], None]]', 'return', 'Any')):
        pass
    # WARNING: Decompyle incomplete

    
    def get_method(self = None, method_name = None):
        if hasattr(NucleusAPIClient, method_name):
            if self._nucleus_client:
                return getattr(self._nucleus_client, method_name)
            raise NucleusClientError('Nucleus client does not available in process')
        if hasattr(NucleusPhaseAgnosticAPIClient, method_name):
            if self._nucleus_phase_agnostic_client:
                return getattr(self._nucleus_phase_agnostic_client, method_name)
            raise NucleusClientError('Nucleus phase agnostic client not available in process')
        raise AttributeError("'%.50s' has no attribute '%.400s'" % (type(self).__name__, method_name))



def report_timing_cb_helper(fut, amp_metrics_reporter, amp_ns = None, method_name = None, start_time = None, transport = ('fut', 'Future', 'amp_metrics_reporter', 'MetricsReporter', 'amp_ns', 'str', 'method_name', 'str', 'start_time', 'float', 'transport', 'str', 'return', 'None')):
    end_time = get_monotonic_time_seconds()
    elapsed_time = end_time - start_time
    if elapsed_time < 0:
        TRACE('Negative elapsed time? Start: %r end: %r method: %r', start_time, end_time, method_name)
        return None
# WARNING: Decompyle incomplete

