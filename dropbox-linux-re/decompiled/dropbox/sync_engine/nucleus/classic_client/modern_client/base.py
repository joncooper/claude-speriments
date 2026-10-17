# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from functools import partial
from typing import Callable, cast, Dict, Iterable, Optional, Set, Text, TypeVar
from apex.context import ApexContext
from apex.metrics import Metric
from google.protobuf.empty_pb2 import Empty as EmptyPb
from google.protobuf.service import RpcController
import build_number
from thin_client.base import NucleusThinClient
from thin_client.exceptions import NucleusConnectionInvalidatedError
from thin_adapter.adapter import ThinAdapter
from thin_adapter.in_proc import InProcAdapter
from debug_thin_client import DebugThinClient
from modern_thin_client import ModernThinClient

stormcrows
from dropbox.client.authentication.account import Account
import dropbox.fs_api.stormcrows, fs_api
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.file_provider_logging.autolog import start_fp_autolog_loop
from dropbox.client.fsw.fsw_nucleus_args import FSWManagerArgs
from dropbox.client.gandalf import Gandalf
from dropbox.client.periodic import PeriodicScheduler
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.hashing import base64_to_digest
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileevents import FileEvents
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.runtime import ExitCode, panic_with_report
from dropbox.fs_api.fs_api_thin_client import FsApiThinClient
from dropbox.fs_api.lifecycle import FsApiCreateParameters, FsApiLifecycleManager
from dropbox.infinite.pager import PageFileRequest, PageResponse
from dropbox.metrics.constants import LOOKUP_FILEID_BATCH_ENABLED_TAG, SYNC_ROOT_TYPE_TAG
from dropbox.metrics.function_usage import FuncMetricsMixin
from dropbox.metrics.reporter import PeriodicMetricsReporter
from dropbox.model.types import NsId
from dropbox.nucleus.bolt_client import NucleusBoltClient
from dropbox.nucleus.migration_constants import NucleusMigrationArgs
from dropbox.nucleus.nucleus_server_configs import get_server_configs
from dropbox.proto.fs_api.fs_api_service_pb2 import TemporaryDirectoryArgs
from dropbox.proto.nucleus.app_service_pb2 import CheckBlockExistsForPeerReq, GetBlockForPeerReq
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.sync_engine_boundary.constants import LOOKUP_BY_FILEID_BATCH_ENABLED_STORMCROW
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException, SyncEngineStoppedError
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
from dropbox.sync_engine_boundary.monitored_thread_pool import MonitoredThreadPoolExecutor
from dropbox.sync_engine_boundary.nucleus_interface import SyncEngineBasicInterface
from dropbox.sync_engine_boundary.nucleus_p2p import P2PAdapter
from dropbox.sync_root.interface import SyncRootType
_ResponseType = TypeVar('_ResponseType')
_OutputType = TypeVar('_OutputType')

def _make_modern_thin_client(base_client = None, boundary_thread_pool = None):
    modern_thin_client = ModernThinClient(base_client, boundary_thread_pool)
    if debugging_features_are_enabled():
        modern_thin_client = DebugThinClient.from_base_client(modern_thin_client)
    return modern_thin_client


class NucleusModernClientBase(FuncMetricsMixin, SyncEngineBasicInterface):
    
    def __init__(self, account, sync_root_type, conn, local_config, metadata_directory, file_events, migration_args, shell_touch, clear_shell_state, nucleus_bolt_client, restart_fn, client_session_id, gandalf, fsw_args, periodic_scheduler, use_fake_network, apex_context, boundary_thread_pool = None, periodic_metrics_reporter = None, set_connecting_engine_status_label_fn = None, backup_mode = (tuple,), linked_accounts_provider = ('account', 'AccountInterface', 'sync_root_type', 'SyncRootType', 'conn', 'DropboxConnection', 'local_config', 'LocalConfigurationInterface', 'metadata_directory', 'Text', 'file_events', 'FileEvents', 'migration_args', 'NucleusMigrationArgs', 'shell_touch', 'Callable[[Text], None]', 'clear_shell_state', 'Callable[[Text], None]', 'nucleus_bolt_client', 'NucleusBoltClient', 'restart_fn', 'Callable[[], None]', 'client_session_id', 'Optional[Text]', 'gandalf', 'Gandalf', 'fsw_args', 'FSWManagerArgs', 'periodic_scheduler', 'PeriodicScheduler', 'use_fake_network', 'bool', 'apex_context', 'ApexContext', 'boundary_thread_pool', 'MonitoredThreadPoolExecutor', 'periodic_metrics_reporter', 'PeriodicMetricsReporter', 'set_connecting_engine_status_label_fn', 'Callable[[bool], None]', 'backup_mode', 'Optional[BackupModeArgs]', 'linked_accounts_provider', 'Callable[[], Iterable[AccountInterface]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def cleanup(self = None):
        self.adapter.cleanup_engine()
    # WARNING: Decompyle incomplete

    
    def is_file_provider(self = None):
        return self._sync_root_type == SyncRootType.FILE_PROVIDER

    account = (lambda self = None: cast(Account, self._account))()
    file_system = (lambda self = None: self.fs)()
    
    def get_main_root_ns(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def version(self = None):
        engine_code = 'n'
        return f'''{build_number.VERSION}{engine_code}{self._sync_root_type.abbreviation()}'''

    
    def _check_block_exists_for_peer(self = None, block_hash = None, authorized_ns_id = None):
        
        try:
            reply = self.modern_thin_client.CheckBlockExistsForPeer(RpcController(), CheckBlockExistsForPeerReq(block_hash = base64_to_digest(block_hash), authorized_ns_id = authorized_ns_id), None).wait_for_result()
        except (SyncEngineStoppedError, ServiceNotAvailableException):
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.NUCLEUS)
            return False
            except NucleusConnectionInvalidatedError:
                return False

        return reply.exists

    
    def _get_block_for_peer(self = None, block_hash = None, authorized_ns_id = None):
        
        try:
            reply = self.modern_thin_client.GetBlockForPeer(RpcController(), GetBlockForPeerReq(block_hash = base64_to_digest(block_hash), authorized_ns_id = authorized_ns_id), None).wait_for_result()
        except (SyncEngineStoppedError, ServiceNotAvailableException):
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.NUCLEUS)
            return None
            except NucleusConnectionInvalidatedError:
                return None

        if reply.WhichOneof('block') == 'found':
            return reply.found

    
    def _get_namespaces(self = None):
        
        try:
            resp = self.modern_thin_client.LookupNamespaces(RpcController(), EmptyPb(), None).wait_for_result()
        except (SyncEngineStoppedError, ServiceNotAvailableException):
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.NUCLEUS)
            return 
            except NucleusConnectionInvalidatedError:
                return 

        return (lambda .0: pass# WARNING: Decompyle incomplete
)(resp.namespaces())


