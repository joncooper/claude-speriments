# Source Generated with Decompyle++
# File: in_proc.pyc (Python 3.11)

import contextlib
import errno
import os
import time
from typing import Callable, cast, ContextManager, Dict, FrozenSet, Generator, Iterable, List, Optional, Text, Tuple, Union
from apex.context import ApexContext
from cffi_transport.exceptions import ServiceNotAvailableException
from google.protobuf.empty_pb2 import Empty as EmptyProto
from google.protobuf.service import RpcController as RpcControllerProto
from build_number.platform import IS_MAC
from classic_client.callback_processor import CallbackProcessor
from classic_client.wrapped_thin_client import WrappedNucleusThinClient
from thin_client.base import NucleusThinClient as NucleusThinClientBase
from thin_client.client import get_sync_engine_create_args, NucleusThinClient, NucleusThinTprtClient
from thin_client.exceptions import NucleusNotAvailableDuringMoveDropbox, UnhandledUnknownFileEventError
from thin_client.fsw import NucleusMoveArbiterUI
from thin_client.reverse_app_service import NucleusReverseAppService
from adapter import ThinAdapter
from common import is_tprt_enabled
from event_publisher import EventPublisher
from fp_dump import file_provider_dump
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.encrypted_folder.manager import EncryptedFolderManager
from dropbox.client.features.flexible_filenames.gating import get_flexible_filenames_rules
from dropbox.client.features.sync_error.contants import NEED_TO_FIX_PERMISSIONS_CONFIG_KEY
from dropbox.client.fsw.fsw_nucleus_args import FSWManagerArgs
from dropbox.client.gandalf import Gandalf
from dropbox.client.nucleus_cdm_relocation import NucleusCdmRelocationMigration
from dropbox.client.periodic import PeriodicScheduler
from dropbox.client.util import enable_p2p_default
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.directoryevent import DirectoryEvent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileevents import FileEvents, UnrecoverableWatchError
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.transitional.wrapper_future import create_and_wrap_future
from dropbox.fs_api.fs_api_thin_client import FsApiThinClient
from dropbox.metrics.reporter import PeriodicMetricsReporter
from dropbox.model.types import FileId
from dropbox.nucleus.bolt_client import NucleusBoltClient
from dropbox.nucleus.migration_constants import NucleusMigrationArgs, SyncEngineState
from dropbox.nucleus.nucleus_server_configs import get_server_configs
from dropbox.preferences import get_local_block_cache_preferences, OPT_P2P
from dropbox.proto.nucleus import file_event_pb2
from dropbox.proto.nucleus.app_service_pb2 import SendFileEventReq, UpdateConfigReq
from dropbox.proto.nucleus.cdm_relocation_pb2 import CdmJoin
from dropbox.proto.nucleus.published_event_pb2 import FileProviderDumpRequestedEvent as FileProviderDumpRequestedEventProto, PublishedEvent
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs, CdmRelocationMode, FlexibleFilenamesConfig, FPShadowConfig, NetworkConfig, SyncEngineCreateArgs, UserConfig
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.exceptions import NucleusNotAvailableDuringAppShutdown, SyncEngineStoppedError
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_engine_boundary.nucleus_p2p import P2PBlockDownloader
from dropbox.sync_engine_boundary.nucleus_types import make_nucleus_account, make_nucleus_network_config
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.interface import SyncRootType
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    MigrationCompletedInfoValue = PublishedEvent.MigrationCompletedInfo.V

class InProcAdapter(ThinAdapter):
    
    def __init__(self, account, conn, local_config, metadata_directory, file_events, migration_args, shell_touch, clear_shell_state, nucleus_bolt_client, restart_fn, client_session_id, gandalf, fsw_args, periodic_scheduler, version, use_fake_network, p2p_block_downloader, apex_context, periodic_metrics_reporter = None, sync_root_type = None, backup_mode = None, fs_api_thin_client = (tuple,), linked_accounts_provider = ('account', 'AccountInterface', 'conn', 'DropboxConnection', 'local_config', 'LocalConfigurationInterface', 'metadata_directory', 'Text', 'file_events', 'FileEvents', 'migration_args', 'NucleusMigrationArgs', 'shell_touch', 'Callable[[Text], None]', 'clear_shell_state', 'Callable[[Text], None]', 'nucleus_bolt_client', 'NucleusBoltClient', 'restart_fn', 'Callable[[], None]', 'client_session_id', 'Optional[Text]', 'gandalf', 'Gandalf', 'fsw_args', 'FSWManagerArgs', 'periodic_scheduler', 'PeriodicScheduler', 'version', 'Text', 'use_fake_network', 'bool', 'p2p_block_downloader', 'Optional[P2PBlockDownloader]', 'apex_context', 'ApexContext', 'periodic_metrics_reporter', 'PeriodicMetricsReporter', 'sync_root_type', 'SyncRootType', 'backup_mode', 'Optional[BackupModeArgs]', 'fs_api_thin_client', 'Optional[FsApiThinClient]', 'linked_accounts_provider', 'Callable[[], Iterable[AccountInterface]]', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def thin_client(self = None):
        return self.nucleus_thin_client

    
    def callback_processor(self = None):
        return self._callback_processor

    
    def pause(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def unpause(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def cleanup_engine(self = None):
        self._remove_watch_ready = self.file_events.remove_watch_async(self.dirty_watch)
        self._initialized = False
        self.wrapped_thin_client.requests_blocked()
        self._stop_engine_locked(NucleusNotAvailableDuringAppShutdown())
        None(None, None)

    
    def begin_dropbox_move(self = None, hidden_fileids = None):
        pass
    # WARNING: Decompyle incomplete

    
    def restart_app_and_sync_engine(self = None):
        self.app_restart()

    
    def get_bugreporter_stats(self = None):
        return self._get_queue_stats(reset_totals = False).items()()

    
    def is_ready(self = None):
        return self._initialized

    
    def is_migrating(self = None):
        return self._migration_args.migration_state == SyncEngineState.MIGRATING_CLASSIC_TO_NUCLEUS

    network_settings_changed = (lambda self = None, network_config = None: args = UpdateConfigReq()args.config.network_config.CopyFrom(network_config)self.nucleus_thin_client.UpdateConfig(RpcControllerProto(), args, None).result())()
    _bolt_stormcrow_changed = (lambda self = None: 