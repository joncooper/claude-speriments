# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

import hashlib
import time
import uuid
from concurrent.futures import Future
from typing import Any, Callable, Dict, List, Literal, Optional
from apex.metrics import Metric, MetricsReporter
from cffi_transport.exceptions import ServiceNotAvailableException
from google.protobuf.empty_pb2 import Empty as EmptyPb
from google.protobuf.service import RpcController
from six import iteritems
from client import P2PClient
from discovery import P2PDiscoveryThread
from event import P2PLogger
from sec import NamespaceSSLCertMap
from server import P2PServer, P2PServerThread
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import report_aggregate_event
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.foundation.futures import ResolvedFuture
from dropbox.functions import make_bytes
from dropbox.model.types import NsId
from dropbox.proto.nucleus.app_service_pb2 import AddP2PKeyContainer, AddP2PKeysContainer, DeleteP2PKeyContainer, GetBlockFromPeerReply, UpdateP2PKeysReply, UpdateP2PKeysReq
from dropbox.sync_engine_boundary.constants import P2P_STOP_SUSPEND
from dropbox.threading import Lock
from dropbox.threadutils import ThreadPool
from dropbox.trace import TRACE
P2P_STOP_PAUSED = 'paused'
P2P_STOP_DISABLED = 'disabled'
MAX_UPDATE_P2P_KEYS_PER_RPC = 128
UpdateP2PKeysOutcome = Literal[('success-false', 'connection-invalidated', 'rpc-exception')]

class P2PConfigManager(object):
    
    def __init__(self):
        self.connection_timeout = 1
        self.get_connection_timeout = 0.2
        self.p2p_timeout = 1
        self.max_conns_per_block = 5
        self.head_request_pool_size = 2
        self.get_request_pool_size = 4
        self.client_pool_size = 2
        self.peer_connection_retries = 5

    
    def get_conns_per_pool(self):
        return self.get_request_pool_size + self.head_request_pool_size

    
    def update_configs(self, configs):
        changed = False
        for key, value in iteritems(configs):
            if not hasattr(self, key):
                TRACE('Trying to update P2P config key which does not exist: %r', key)
                report_bad_assumption('Trying to update P2P config key which does not exist')
                continue
            if getattr(self, key) != value:
                setattr(self, key, value)
                changed = True
            return changed



class P2PManager(object):
    VERSION = (2, 0)
    
    def __init__(self, get_block_fn, check_block_fn = None, metrics_reporter = None, account = None, rust_p2p_enabled = (None, False, None), rust_p2p_variant = ('get_block_fn', 'Callable[[bytes, NsId], Optional[bytes]]', 'check_block_fn', 'Callable[[bytes, NsId], bool]', 'metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'rust_p2p_variant', 'Optional[str]', 'return', 'None')):
        self._config = P2PConfigManager()
        self._logger = P2PLogger()
        self._get_block_fn = get_block_fn
        self._check_block_fn = check_block_fn
        self._account = account
        self._metrics_reporter = metrics_reporter
        self._rust_p2p_variant = rust_p2p_variant
        self.p2p_running = False
        self.rust_p2p_enabled = rust_p2p_enabled
        self._start_stop_lock = Lock()
        self._stop_states = {
            P2P_STOP_SUSPEND: False,
            P2P_STOP_DISABLED: True,
            P2P_STOP_PAUSED: True }
        self._p2p_uuid = uuid.uuid4().int
        self._server = None
        self._server_thread = None
        self._discovery_thread = None
        self._client = None
        self.modern_thin_client = None
        self._ns_certs = NamespaceSSLCertMap(retain_key_material = rust_p2p_enabled)
        self._client_threadpool = None
        if not rust_p2p_enabled:
            self._client_threadpool = ThreadPool('p2p-client-threadpool', pool_size = self._config.client_pool_size, max_num_threads = self._config.client_pool_size, account = account)
        TRACE('Created P2P manager with uuid %r', self._p2p_uuid, account = self._account)

    
    def _start(self):
        if self.p2p_running or self.rust_p2p_enabled:
            return None
        TRACE('Starting P2P', account = self._account)
        
        try:
            self._client_threadpool.set_pool_size(new_pool_size = self._config.client_pool_size, max_num_threads = self._config.client_pool_size)
            self._server = P2PServer(self._get_block_fn, self._check_block_fn, self._ns_certs.get_context)
            self._server_thread = db_thread(P2PServerThread)(self._server, self._account)
            self._discovery_thread = db_thread(P2PDiscoveryThread)(version = self.VERSION, port = self._server.port, p2p_uuid = self._p2p_uuid, namespaces_callback = self.get_p2p_namespaces, account = self._account)
            self._client = P2PClient(self._p2p_uuid, self._ns_certs.get_context, self._config, self._logger, self._metrics_reporter, self._account, rust_p2p_variant = self._rust_p2p_variant)
            self._discovery_thread.add_discovery_callback(self._client.discovery_callback)
            self._server_thread.start()
            self._discovery_thread.start()
            self.p2p_running = True
            return None
        except Exception:
            TRACE('P2P could not start up', account = self._account)
            report_exception(component = DesktopComponent.SEC_NETWORKING)
            return None


    
    def _stop(self, do_join = (False,)):
        if not self.p2p_running:
            return None
        TRACE('Stopping P2P', account = self._account)
        self.p2p_running = False
        self._server_thread.signal_stop()
        self._discovery_thread.signal_stop()
        if do_join:
            self._server_thread.join()
            self._discovery_thread.join()
        self._client.shutdown(do_join = do_join)
        self._client = None
        self._server = None
        self._server_thread = None
        self._discovery_thread = None

    
    def set_stopped(self, reason, value):
        self._start_stop_lock
        if reason not in self._stop_states:
            report_bad_assumption('Invalid p2p stop state %r', reason)
            None(None, None)
            return None
        if None._stop_states[reason] == value:
            TRACE('No change in p2p stop state for reason:%r with value:%r', reason, value)
            None(None, None)
            return None
        self._stop_states[reason] = None
        TRACE('Set p2p stop state %r to %r: P2P state is now: %r', reason, value, self._stop_states, account = self._account)
        if any(self._stop_states.values()):
            self._stop()
        else:
            self._start()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def shutdown(self, do_join = (True,)):
        TRACE('P2P Shutting down', account = self._account)
        self._start_stop_lock
        self._stop(do_join = do_join)
        if self._client_threadpool:
            self._client_threadpool.shutdown(wait = do_join)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def get_server_port(self):
        self._start_stop_lock
        if self._server:
            None(None, None)
            return 
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def set_modern_thin_client(self, modern_thin_client):
        self.modern_thin_client = modern_thin_client

    
    def get_p2p_namespaces(self = None):
        return self._ns_certs.get_nses()

    
    def handle_namespace_unmount(self = None, namespace = None):
        TRACE('P2P saw namespace %r unmounted', namespace, account = self._account)
        if self.modern_thin_client:
            self.log_if_call_fails(self.modern_thin_client.UpdateP2PKeys(RpcController(), UpdateP2PKeysReq(delete_key = DeleteP2PKeyContainer(ns_id = namespace)), None))
        self._ns_certs.remove_ns(namespace)
        self._start_stop_lock
        if self._client:
            self._client.reset_namespace(namespace)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def ns_p2p_key_map_request(self = None, ns_list = None):
        return self._ns_certs.get_md5s(ns_list)

    
    def update_key(self, ns, key, cert, md5):
        is_new_ns = self._ns_certs.update_cert(ns, key, cert, md5)
        self._start_stop_lock
        if self._client:
            self._client.reset_namespace(ns)
        None(None, None)

    
    def handle_list(self, ret, **kwargs):
        new_key_map = ret.get('ns_p2p_key_map', { })
        new_keys = False
        key_map_containers = []
        for ns, key_dict in iteritems(new_key_map):
            ns = int(ns)
            md5 = key_dict['md5']
            cert = key_dict['cert']
            key = key_dict['pk']
            if self.is_invalid_key_cert_md5(ns, key, cert, md5, ns):
                continue
            if self.modern_thin_client:
                key_map_containers.append(AddP2PKeyContainer(ns_id = ns, private_key = key, cert = cert, md5 = md5))
            if self.update_key(ns, key, cert, md5):
                new_keys = True
            if key_map_containers and self.modern_thin_client:
                self._send_add_key_containers(key_map_containers)
        self._start_stop_lock
        if new_keys and self._discovery_thread:
            self._discovery_thread.force_broadcast()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def is_invalid_key_cert_md5(self, ns, key, cert, md5, ns_id):
        if not key or cert:
            if not key and cert:
                report_bad_assumption('Received empty P2P key and cert for ns %r', ns_id)
            elif not key:
                report_bad_assumption('Received empty P2P key for ns %r', ns_id)
            else:
                report_bad_assumption('Received empty P2P cert for ns %r', ns_id)
            return True
        md5_val = hashlib.md5(make_bytes(cert + key)).hexdigest()
        if md5_val != md5:
            report_bad_assumption('Hash of P2P key cert %r did not match: %r', md5_val, md5)
            return True

    
    def push_all_keys(self = None):
        if not self.modern_thin_client:
            return None
        key_map_containers = None
        for ns, key_data in self._ns_certs.get_all_key_materials().items():
            (key, cert, md5) = key_data
            if self.is_invalid_key_cert_md5(ns, key, cert, md5, ns):
                continue
            key_map_containers.append(AddP2PKeyContainer(ns_id = ns, private_key = key, cert = cert, md5 = md5))
            if not key_map_containers:
                return None
            TRACE('Sending full key map with %r p2p key(s) to rust via UpdateP2PKeys', len(key_map_containers))
            self._send_add_key_containers(key_map_containers)
            return None

    
    def _send_add_key_containers(self = None, key_map_containers = None):
        modern_thin_client = self.modern_thin_client
    # WARNING: Decompyle incomplete

    
    def _report_update_p2p_keys_outcome(self = None, outcome = None):
        self._metrics_reporter.create_stats(Metric('client_sync_events', 'p2p/update_p2p_keys_outcome'), {
            'outcome': outcome }).record(1)

    
    def log_if_call_fails(self, res):
        pass
    # WARNING: Decompyle incomplete

    
    def download_blocks(self, hash_to_nses, dl_callback):
        self._start_stop_lock
        if not self.p2p_running:
            TRACE('Skipping p2p: it is disabled', account = self._account)
            None(None, None)
            return 
        None(None, None)

    
    def download_block(self = None, block_hash = None, ns_id = None, dl_callback = ('block_hash', 'bytes', 'ns_id', 'NsId', 'dl_callback', 'Callable[[int, float], None]', 'return', 'GetBlockFromPeerReply')):
        ret = self.download_blocks(hash_to_nses = {
            block_hash: {
                ns_id} }, dl_callback = dl_callback)
        if not ret:
            return GetBlockFromPeerReply(not_found = EmptyPb())
    # WARNING: Decompyle incomplete

    
    def download_block_async(self = None, block_hash = None, ns_id = None, dl_callback = ('block_hash', 'bytes', 'ns_id', 'NsId', 'dl_callback', 'Callable[[int, float], None]', 'return', 'Future[GetBlockFromPeerReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def download_blocks_async(self, hash_to_nses, dl_callback):
        return self._client_threadpool.submit(self.download_blocks, hash_to_nses, dl_callback)

    
    def update_configs(self, configs):
        changed = self._config.update_configs(configs)
        TRACE('P2PManager update_configs called: changed = %r', changed, account = self._account)
        if changed:
            self._start_stop_lock
            if self.p2p_running:
                TRACE('Restarting P2PManager because of config change', account = self._account)
                self._stop(do_join = True)
                self._start()
                TRACE('Restarted P2PManager because of config change', account = self._account)
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        return changed


