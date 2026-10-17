# Source Generated with Decompyle++
# File: client.pyc (Python 3.11)

import concurrent
import random
import socket
import ssl
import threading
import time
import uuid
from collections import defaultdict, namedtuple
from typing import Any, Callable, Dict, List, Optional, Text
from apex.metrics import Metric, MetricsReporter
from six import iteritems, itervalues
from six.moves import range
from six.moves.http_client import BadStatusLine
from event import P2PLogger
from sec import P2PHTTPSConnection
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report_aggregate_event
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.functions import make_str
from dropbox.shared.util import head
from dropbox.ssl.assertions import allow_non_dropbox_ssl_policy
from dropbox.threading import Condition, Lock
from dropbox.threadutils import ThreadPool
from dropbox.trace import TRACE
Peer = namedtuple('Peer', [
    'p2p_uuid',
    'ip_addr',
    'port'])

class ConnectionDeadError(Exception):
    pass


class RequestState(object):
    NOT_STARTED = 0
    CHECKING = 1
    GETTING = 2
    DONE = 3
    
    def __init__(self):
        self.state = self.NOT_STARTED

    
    def aggregate_dict(self):
        return {
            'not_started': 1 if self.state == self.NOT_STARTED else 0,
            'checking': 1 if self.state == self.CHECKING else 0,
            'getting': 1 if self.state == self.GETTING else 0,
            'done': 1 if self.state == self.DONE else 0 }



class PeerConnection(object):
    HEADERS = {
        'Connection': 'Keep-Alive' }
    
    def __init__(self, peer = None, ns_id = None, context = None, connection_timeout = ('peer', 'Peer', 'ns_id', 'int', 'context', 'ssl.SSLContext', 'connection_timeout', 'float', 'return', 'None')):
        self._peer = peer
        self._ns_id = ns_id
        self._connection = P2PHTTPSConnection(host = peer.ip_addr, port = peer.port, timeout = connection_timeout, context = context, sni_name = str(ns_id))

    
    def __repr__(self):
        return f'''<PeerConnection {self._peer!r}, ns={self._ns_id!r}>'''

    
    def _submit_request(self, method, path):
        TRACE('Requesting %r %r from %r', method, path, self)
        allow_non_dropbox_ssl_policy()
        self._connection.request(method, path, headers = self.HEADERS)
        response = self._connection.getresponse()
        code = response.status
        content = response.read()

    
    def check(self, blockhash):
        path = '/blocks/%d/%s' % (self._ns_id, make_str(blockhash))
        (code, _) = self._submit_request('HEAD', path)
        if code == 200:
            return True
        if None == 404:
            return False
        if None == 403:
            TRACE('Received a 403 return code -- probably a cert was rotated and we were late to get it')
            raise ConnectionDeadError('Received 403 return code')
        if code == 500:
            TRACE('check: 500 from %r, %r', self, path)
            return False
        report_bad_assumption('check: unexpected return code %r from %r, %r', code, self, path)
        return False

    
    def get(self, blockhash):
        path = '/blocks/%d/%s' % (self._ns_id, make_str(blockhash))
        (code, content) = self._submit_request('GET', path)
        if code == 200:
            return content
        if None == 404:
            TRACE('P2P get failed')
            return None
        if None == 500:
            TRACE('check: 500 from %r, %r', self, path)
            return None
        report_bad_assumption('get: unexpected return code %r from %r, %r', code, self, path)

    
    def close(self):
        self._connection.close()



class PeerConnectionPool(object):
    
    def __init__(self, peer, ns_id = None, context = None, num_conns = None, connection_timeout = (0,), pool_recreation_retry_count = ('peer', 'Peer', 'ns_id', 'int', 'context', 'ssl.SSLContext', 'num_conns', 'int', 'connection_timeout', 'float', 'pool_recreation_retry_count', 'Optional[int]', 'return', 'None')):
        self.peer = peer
        self.ns_id = ns_id
        self.pool_recreation_retry_count = pool_recreation_retry_count
        self._num_conns = num_conns
        self._connections = []
        self._free_connections = []
        for _ in range(num_conns):
            new_conn = PeerConnection(peer = peer, ns_id = ns_id, context = context, connection_timeout = connection_timeout)
            self._connections.append(new_conn)
            self._free_connections.append(new_conn)
            self._availability_cond = Condition()
            self._alive = True
            return None

    
    def get_connection(self, timeout = (0,)):
        timeout_end = time.time() + timeout
        self._availability_cond
    # WARNING: Decompyle incomplete

    
    def release(self, connection):
        self._availability_cond
        if self._alive:
            if self.pool_recreation_retry_count:
                TRACE('Resetting retry count (ns_id=%r, uuid=%r) from %s retries to 0', self.ns_id, self.peer.p2p_uuid, self.pool_recreation_retry_count)
                self.pool_recreation_retry_count = 0
            self._free_connections.append(connection)
            self._availability_cond.notify(1)
        else:
            connection.close()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def close(self):
        self._availability_cond
    # WARNING: Decompyle incomplete



class P2PClient(object):
    
    def __init__(self, p2p_uuid, ssl_context_fn, p2p_config = None, logger = None, metrics_reporter = None, account = (None, None), rust_p2p_variant = ('p2p_uuid', 'int', 'ssl_context_fn', 'Callable[[int], ssl.SSLContext]', 'p2p_config', 'Any', 'logger', 'P2PLogger', 'metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'rust_p2p_variant', 'Optional[Text]', 'return', 'None')):
        self._config = p2p_config
        self._p2p_uuid = p2p_uuid
        self._ssl_context_fn = ssl_context_fn
        self._peers = defaultdict(dict)
        self._peers_lock = Lock()
        self._thread_pool_head = ThreadPool('p2p-request-threadpool-head', pool_size = 1, max_num_threads = self._config.head_request_pool_size, expected_exceptions = [
            ConnectionDeadError], account = account)
        self._thread_pool_get = ThreadPool('p2p-request-threadpool-get', pool_size = 1, max_num_threads = self._config.get_request_pool_size, expected_exceptions = [
            ConnectionDeadError], account = account)
        self._logger = logger
    # WARNING: Decompyle incomplete

    
    def shutdown(self, do_join = (False,)):
        self._thread_pool_head.shutdown(wait = do_join)
        self._thread_pool_get.shutdown(wait = do_join)
        for ns_dict in self._peers.values():
            for pool in ns_dict.values():
                pool.close()
                return None

    
    def reset_namespace(self, ns_id):
        self._peers_lock
        if ns_id not in self._peers:
            None(None, None)
            return None
        p2p_uuids = list(self._peers[ns_id])
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def _create_pool(self, peer = None, ns_id = None, context = None, pool_recreation_retry_count = ('peer', 'Peer', 'ns_id', 'int', 'context', 'ssl.SSLContext', 'pool_recreation_retry_count', 'int', 'return', 'PeerConnectionPool')):
        pool_size = self._config.get_conns_per_pool()
        return PeerConnectionPool(peer = peer, ns_id = ns_id, context = context, num_conns = pool_size, connection_timeout = self._config.connection_timeout, pool_recreation_retry_count = pool_recreation_retry_count)

    
    def discovery_callback(self, version, p2p_uuid, ip_addr, port, namespaces):
        pass
    # WARNING: Decompyle incomplete

    
    def p2p_get(self, hash_to_nses, timeout = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_block_from_pool(self, pool, blockhash, get_semaphore, state, request_id):
        future = None
    # WARNING: Decompyle incomplete

    
    def _fetch_block(self, pool, conn, blockhash, state, request_id):
        state.state = state.GETTING
        self._logger.report_client_get_state_change(request_id = request_id, peer_uuid = str(pool.peer.p2p_uuid), state = state.state)
        
        try:
            result = conn.get(blockhash)
            if not result:
                self._logger.report_client_get_peer_failure(request_id = request_id, peer_uuid = str(pool.peer.p2p_uuid), state = state.state, expected = False, reason = 'no_result')
            pool.release(conn)
            state.state = state.DONE
            self._logger.report_client_get_state_change(request_id = request_id, peer_uuid = str(pool.peer.p2p_uuid), state = state.state)
        except:
            state.state = state.DONE
            self._logger.report_client_get_state_change(request_id = request_id, peer_uuid = str(pool.peer.p2p_uuid), state = state.state)

        return result

    
    def _start_requests(self, hash_to_nses):
        futures = set()
        for blockhash, nses in iteritems(hash_to_nses):
            request_id = Text(uuid.uuid4())
            get_semaphore = threading.Semaphore(1)
            if len(nses) != 1:
                self._logger.report_client_get_atypical_ns_number(request_id = request_id, num_nses = len(nses), nses = list(nses))
            if len(nses) == 0:
                report_bad_assumption('Block %r had 0 namespaces', blockhash)
                self._logger.report_client_get_start(request_id = request_id, num_possible_peers = 0, num_peers = 0, peer_uuids = None, ns_id = None)
                self._logger.report_client_get_failure(request_id = request_id, expected = False, reason = 'block_had_no_ns_references')
                continue
            ns = head(nses)
            pools = None
            self._peers_lock
            if ns not in self._peers:
                self._logger.report_client_get_start(request_id = request_id, num_possible_peers = 0, num_peers = 0, peer_uuids = None, ns_id = ns)
                self._logger.report_client_get_failure(request_id = request_id, expected = True, reason = 'no_peers_for_selected_ns')
                None(None, None)
                continue
            pools = list(itervalues(self._peers[ns]))
            None(None, None)
        with None:
            if not None:
                pass
        num_possible_peers = len(pools)
        if not pools:
            self._logger.report_client_get_start(request_id = request_id, num_possible_peers = 0, num_peers = 0, peer_uuids = None, ns_id = ns)
            self._logger.report_client_get_failure(request_id = request_id, expected = True, reason = 'no_peers_for_selected_ns_anymore')
            continue
        if len(pools) > self._config.max_conns_per_block:
            pools = random.sample(pools, self._config.max_conns_per_block)
        request_id(request_id = num_possible_peers, num_possible_peers = len(pools), num_peers = (lambda .0: [ str(x.peer.p2p_uuid) for x in .0 ]), peer_uuids = pools(), ns_id = ns)
        for pool in pools:
            state = RequestState()
            future = self._thread_pool_head.submit(self._get_block_from_pool, pool, blockhash, get_semaphore, state, request_id)
            future.blockhash = blockhash
            future.pool = pool
            future.state = state
            future.request_id = request_id
            futures.add(future)
            return futures

    
    def _resolve_completed_futures(self, done_futures):
        results = []
    # WARNING: Decompyle incomplete


