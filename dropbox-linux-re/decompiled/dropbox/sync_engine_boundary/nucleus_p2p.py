# Source Generated with Decompyle++
# File: nucleus_p2p.pyc (Python 3.11)

from abc import ABC, abstractmethod
from concurrent.futures import Future
from typing import Any, Callable, Dict, Optional, Set, Tuple, Union
from apex.metrics import MetricsReporter
from google.protobuf.service import RpcController
from sync_engine.nucleus.classic_client.modern_client.modern_thin_client import ModernThinClient
from sync_engine.p2p.manager import P2P_STOP_DISABLED, P2P_STOP_PAUSED, P2PManager
from sync_engine.threads import NucleusThread
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread_returns_none
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.util import enable_p2p_default
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.list_legacy.out_of_band_response import OutOfBandResponse
from dropbox.model.types import NsId
from dropbox.native_queue import Queue
from dropbox.preferences import OPT_P2P
from dropbox.proto.nucleus.app_service_pb2 import GetBlockFromPeerReply, UpdateConfigReq
from dropbox.proto.nucleus.sync_engine_pb2 import UpdatableAppConfig, UserConfig
from dropbox.sync_engine_boundary.types import MountChangeOperation
from dropbox.trace import TRACE
P2P_STOP_TIMEOUT = 5

class P2PBlockDownloader(ABC):
    get_block_from_peer = (lambda self = None, block_hash = None, ns_id = abstractmethod: raise NotImplementedError)()


class P2PMetaDownloader(ABC):
    
    def handle_server_response(self = None, response = None):
        raise NotImplementedError

    
    def get_namespace_key_map(self = None):
        raise NotImplementedError



class P2PSyncManagement(ABC):
    
    def handle_mount_change(self = None, mount_change_op = None):
        raise NotImplementedError

    
    def add_preferences_callback(self = None, config = None):
        raise NotImplementedError

    
    def set_stopped(self = None, reason = None, value = None):
        raise NotImplementedError



class NoOpP2PMetaDownloader(P2PMetaDownloader):
    
    def __init__(self = None):
        pass

    
    def handle_server_response(self = None, response = None):
        pass

    
    def get_namespace_key_map(self = None):
        return { }



class P2PAdapter(P2PMetaDownloader, P2PBlockDownloader, P2PSyncManagement):
    
    def __init__(self, account, get_block_fn, check_block_fn = None, get_namespaces_fn = None, metrics_reporter = None, rust_p2p_enabled = (False, None), rust_p2p_variant = ('account', 'AccountInterface', 'get_block_fn', 'Callable[[bytes, NsId], Optional[bytes]]', 'check_block_fn', 'Callable[[bytes, NsId], bool]', 'get_namespaces_fn', 'Callable[[], Set[NsId]]', 'metrics_reporter', 'MetricsReporter', 'rust_p2p_variant', 'Optional[str]', 'return', 'None')):
        self.account = account
        self._modern_thin_client = None
        self._rust_p2p_enabled = rust_p2p_enabled
        self._rust_p2p_variant = rust_p2p_variant
        self.p2p_manager_thread = db_thread(P2PManagerThread, component = DesktopComponent.NUCLEUS)(account = self.account, get_block_fn = get_block_fn, check_block_fn = check_block_fn, metrics_reporter = metrics_reporter, rust_p2p_enabled = rust_p2p_enabled, rust_p2p_variant = rust_p2p_variant)
        self.start()
        self.get_namespaces_fn = get_namespaces_fn

    
    def set_modern_thin_client(self = None, thin_client = None):
        self._modern_thin_client = thin_client
        self.p2p_manager_thread.set_modern_thin_client(thin_client)

    
    def push_all_keys(self = None):
        self.p2p_manager_thread.push_all_keys()

    
    def start(self = None):
        TRACE('P2PAdapter: Starting NUCLEUS_P2P_THREAD')
        self.p2p_manager_thread.start()
        self.set_stopped(P2P_STOP_PAUSED, False)

    
    def stop(self = None):
        TRACE('P2PAdapter: Stopping P2P')
        self.p2p_manager_thread.signal_stop()
        self.p2p_manager_thread.join(timeout = P2P_STOP_TIMEOUT)
        if self.p2p_manager_thread.is_alive():
            report_bad_assumption('P2P Manager thread did not stop in time!')
        self.p2p_manager_thread.shutdown()

    
    def handle_server_response(self = None, response = None):
        self.p2p_manager_thread.add_event('handle_server_response', args = ({
            'ns_p2p_key_map': response.ns_p2p_key_map },))

    
    def get_namespace_key_map(self = None):
        if self.get_namespaces_fn:
            namespaces = self.get_namespaces_fn()
            return self.p2p_manager_thread.get_key_map(namespaces)

    
    def get_block_from_peer(self = None, block_hash = None, ns_id = None):
        
        def unimplemented_p2p_callback(raw_size = None, time_delta = None):
            TRACE('[NUCLEUS_P2P] !!!! callback is unimplemented. raw_size: %d time_delta: %d', raw_size, time_delta)

        return self.p2p_manager_thread.download_block_async(ns_id = ns_id, block_hash = block_hash, callback = unimplemented_p2p_callback)

    
    def handle_mount_change(self = None, mount_change_op = None):
        if mount_change_op.is_mount is False:
            self.p2p_manager_thread.add_event(event_type = 'handle_namespace_unmount', args = (mount_change_op.ns_id,))
            return None

    
    def add_preferences_callback(self = None, config = None):
        TRACE('Called P2P preferences callback with OPT_P2P %r', config[OPT_P2P])
        self.set_stopped(P2P_STOP_DISABLED, not config[OPT_P2P])
        if self._rust_p2p_enabled:
            p2p_enabled = bool(config.config_dict.get(OPT_P2P, enable_p2p_default()))
            self._call_update_config_p2p_enabled(p2p_enabled)
            return None

    
    def _update_config_p2p_enabled_impl(self = None, p2p_enabled = None):
        pass
    # WARNING: Decompyle incomplete

    _call_update_config_p2p_enabled = (lambda self = None, p2p_enabled = None: self._update_config_p2p_enabled_impl(p2p_enabled))()
    
    def set_stopped(self = None, reason = None, value = None):
        TRACE('P2P set stopped called with reason: %r value: %r', reason, value)
        self.p2p_manager_thread.add_event(event_type = 'set_stopped', args = (reason, value))



class NoOpP2PAdapter(P2PAdapter):
    
    def start(self = None):
        TRACE('NoOpP2PAdapter: Starting NUCLEUS_P2P_THREAD')

    
    def stop(self = None):
        TRACE('NoOpP2PAdapter: Stopping NUCLEUS_P2P_THREAD')
        self.p2p_manager_thread.shutdown()
        self.p2p_manager_thread.signal_stop()

    
    def handle_server_response(self = None, response = None):
        pass

    
    def get_namespace_key_map(self = None):
        return { }

    
    def get_block_from_peer(self = None, block_hash = None, ns_id = None):
        return Future()

    
    def handle_mount_change(self = None, mount_change_op = None):
        pass

    
    def add_preferences_callback(self = None, config = None):
        pass

    
    def set_stopped(self = None, reason = None, value = None):
        pass



class P2PManagerThread(NucleusThread):
    pass
# WARNING: Decompyle incomplete

