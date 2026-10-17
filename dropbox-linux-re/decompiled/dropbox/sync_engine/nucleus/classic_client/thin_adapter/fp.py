# Source Generated with Decompyle++
# File: fp.pyc (Python 3.11)

import contextlib
from concurrent.futures import Future
from typing import Callable, cast, ContextManager, Dict, FrozenSet, List, Optional, Text, Tuple
import tprt
from apex.context import ApexContext
from google.protobuf.empty_pb2 import Empty as EmptyProto
from google.protobuf.service import RpcController as RpcControllerProto
from classic_client.callback_processor import CallbackProcessor, ReactivePayload
from thin_client.base import NucleusThinClient
from thin_client.exceptions import NucleusConnectionInvalidatedError, NucleusConnectionTimeoutError
from thin_client.fp_client import NucleusFpThinClient
from adapter import ThinAdapter
from event_publisher import EventPublisher, PublishedEventWrapper
from fp_dump import file_provider_dump
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.periodic import PeriodicScheduler
from dropbox.client.util import enable_p2p_default
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connectivity_watch.watch_interface import ConnectivityState, ConnectivityWatchInterface
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.foundation.futures import Future as DBXFuture, ResolvedFuture
from dropbox.foundation.transitional.wrapper_future import create_and_wrap_future
from dropbox.fs_api.fs_api_thin_client import FsApiThinClient
from dropbox.metrics.reporter import PeriodicMetricsReporter
from dropbox.model.types import FileId
from dropbox.preferences import OPT_P2P
from dropbox.proto.nucleus.app_service_pb2 import UpdateConfigReq as UpdateConfigReqProto
from dropbox.proto.nucleus.published_event_pb2 import FileProviderDumpRequestedEvent as FileProviderDumpRequestedEventProto
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveEvent as ReactiveEventProto, ReactiveRequest as ReactiveRequestProto
from dropbox.proto.nucleus.sync_engine_pb2 import NetworkConfig
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE

def get_reactive_payload_to_method():
    pass
# WARNING: Decompyle incomplete

_REACTIVE_PAYLOAD_TO_METHOD = get_reactive_payload_to_method()

class FpAdapter(ThinAdapter):
    
    def __init__(self, account, local_config, gandalf, periodic_scheduler, restart_fn, apex_context, periodic_metrics_reporter = None, sync_root_type = None, set_connecting_engine_status_label_fn = None, connectivity_watch = (None,), on_fp_reconnected = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'gandalf', 'Gandalf', 'periodic_scheduler', 'PeriodicScheduler', 'restart_fn', 'Callable[[], None]', 'apex_context', 'ApexContext', 'periodic_metrics_reporter', 'PeriodicMetricsReporter', 'sync_root_type', 'SyncRootType', 'set_connecting_engine_status_label_fn', 'Callable[[bool], None]', 'connectivity_watch', 'ConnectivityWatchInterface', 'on_fp_reconnected', 'Optional[Callable[[], None]]', 'return', 'None')):
        self._account = account
        self._gandalf = gandalf
        self._local_config = local_config
        self._periodic_scheduler = periodic_scheduler
        self._fs = SyncEngineFactory.make_default_file_system()
        self._restart_fn = restart_fn
        self._on_fp_reconnected = on_fp_reconnected
        self._nucleus_thin_client = NucleusFpThinClient(account, local_config, restart_fn, self.handle_fp_reconnected, apex_context.metrics_reporter, set_connecting_engine_status_label_fn)
        self._callback_processor = CallbackProcessor(account, self._gandalf, self._fs, (lambda _: pass), self._app_restart, self._file_provider_dump, sync_root_type = sync_root_type, on_migration_to_nucleus_completed = None, config = None, amp_metrics_reporter = apex_context.metrics_reporter, periodic_scheduler = self._periodic_scheduler, backup_mode = None)
        self._event_publisher = EventPublisher(handle_publish_event = self._callback_processor.handle_published_event_internal, account = account, nucleus_thin_client = self.thin_client(), periodic_metrics_reporter = periodic_metrics_reporter, gandalf = self._gandalf, backup_mode = None, fs_api_thin_client = None)
        self._event_publisher.start()
        self._set_initial_p2p_enabled()
        self._listen_for_network_changes(connectivity_watch)

    
    def _listen_for_network_changes(self = None, connectivity_watch = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_reconnect_rpcs(self = None):
