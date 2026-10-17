# Source Generated with Decompyle++
# File: listener.pyc (Python 3.11)

from __future__ import annotations
import os
import socket
from concurrent.futures import Future
from typing import Any, Callable, Dict, Optional, Protocol
import tprt
from apex.metrics import Metric
from build_number import BUILD_KEY
from backend import EngineRemoteTreeProxyBackend, RemoteEntry, RemoteReadErrorCode, RemoteReadFailure, RemoteTreeProxyBackend, ServedRange
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC
from dropbox.proto.nucleus_remote_tree_proxy import remote_tree_proxy_pb2 as pb
from dropbox.proto.nucleus_remote_tree_proxy.remote_tree_proxy_tprt_server import RemoteTreeProxyServer, RemoteTreeProxyService
from dropbox.threading import Lock
from dropbox.trace import TRACE
if IS_MAC:
    from Foundation import NSFileManager
_DROPBOX_TEAM_ID = 'G7HH3F8CAK'
_SOCKET_FILENAME = 'rtree.sock'
_STORMCROW_RULE = 'desktop-nucleus-fskit-prototype'
_FETCH_METRIC_NS = 'client_sync_events'
_FETCH_METRIC_NAME = 'remote_tree_proxy/fetch_byte_range'
_RESULT_SERVED = 'served'

def _result_label(code = None):
    return code.name.lower()

_MAX_FETCH_LENGTH = 15728640
_MAX_FETCH_ALIGNMENT = 16777216
_MAX_ENUMERATE_REPLY_BYTES = 15728640
_ENTRY_FRAMING_BYTES = 6
_MAX_SOCKET_PATH_BYTES = 103
_BIND_PROBE_TIMEOUT_S = 2

def _app_group_id():
    return f'''{_DROPBOX_TEAM_ID}.com.getdropbox.{BUILD_KEY.lower()}.sync'''


def _socket_path():
    url = NSFileManager.defaultManager().containerURLForSecurityApplicationGroupIdentifier_(_app_group_id())
# WARNING: Decompyle incomplete


class SampleRecorder(Protocol):
    
    def record(self = None, value = None):
        pass



class SampleRecorderFactory(Protocol):
    
    def create_stats(self = None, metric = None, tags = None):
        pass



class _FetchResultCounters:
    
    def __init__(self = None, metrics_reporter = None):
        self._counters = { }
    # WARNING: Decompyle incomplete

    
    def record(self = None, result = None):
        counter = self._counters.get(result)
    # WARNING: Decompyle incomplete



def _as_pb_enum(ordinal = None):
    return ordinal


class _RemoteTreeProxyServiceImpl(RemoteTreeProxyService):
    
    def __init__(self = None, backend = None, metrics_reporter = None):
        self._backend = backend
        self._fetch_counters = _FetchResultCounters(metrics_reporter)

    
    def _to_pb_entry(self = None, e = None):
        return e.filename(filename = e.fileid, fileid = _as_pb_enum(e.type), type = e.content_hash, content_hash = e.size, size = e.mtime, mtime = (lambda .0: [ _as_pb_enum(a) for a in .0 ]), attributes = e.attributes())

    
    def FetchByteRange(self = None, rpc_controller = None, Request = None, done_unused = (None,)):
        fut = Future()
        
        try:
            if Request.length > _MAX_FETCH_LENGTH or Request.alignment > _MAX_FETCH_ALIGNMENT:
                self._fetch_counters.record(_result_label(RemoteReadErrorCode.REJECTED))
                fut.set_result(self._fetch_error(RemoteReadErrorCode.REJECTED))
                return fut
            result = None._backend.fetch_byte_range(Request.fileid, Request.content_hash, Request.offset, Request.length, Request.alignment)
            if isinstance(result, ServedRange):
                self._fetch_counters.record(_RESULT_SERVED)
                fut.set_result(pb.FetchByteRangeReply(served = pb.ServedRange(data = result.data, range_file_path = result.range_file_path, aligned_offset = result.aligned_offset, aligned_length = result.aligned_length, content_hash = result.content_hash)))
            else:
                self._fetch_counters.record(_result_label(result.code))
                fut.set_result(self._fetch_error(result.code, result.stale_revision_new_content_hash, result.stale_revision_new_size))
        except Exception:
            exc = None
            fut.set_exception(exc)
            exc = None
            del exc
        except:
            exc = None
            del exc

        return fut

    
    def _fetch_error(self = None, code = None, stale_revision_new_content_hash = None, stale_revision_new_size = (b'', 0)):
        return pb.FetchByteRangeReply(error = pb.FetchByteRangeError(code = _as_pb_enum(code), stale_revision_new_content_hash = stale_revision_new_content_hash, stale_revision_new_size = stale_revision_new_size))

    
    def EnumerateRemoteDir(self = None, rpc_controller = None, Request = None, done_unused = (None,)):
        fut = Future()
    # WARNING: Decompyle incomplete

    
    def _enumerate_reply_within_budget(self = None, entries = None):
        reply = pb.EnumerateRemoteDirReply(entries = pb.RemoteEntries())
        used = _ENTRY_FRAMING_BYTES
        for e in entries:
            pb_entry = self._to_pb_entry(e)
            used += pb_entry.ByteSize() + _ENTRY_FRAMING_BYTES
            if used > _MAX_ENUMERATE_REPLY_BYTES:
                return None
            None.entries.entries.append(pb_entry)
            return reply

    
    def _enumerate_error(self = None, code = None):
        return pb.EnumerateRemoteDirReply(error = pb.RemoteReadError(code = _as_pb_enum(code)))

    
    def LookupRemoteEntry(self = None, rpc_controller = None, Request = None, done_unused = (None,)):
        fut = Future()
        
        try:
            result = self._backend.lookup_remote_entry(Request.dbx_rr_path)
            if isinstance(result, RemoteReadFailure):
                fut.set_result(self._lookup_error(result.code))
            else:
                fut.set_result(pb.LookupRemoteEntryReply(found = self._to_pb_entry(result)))
        except Exception:
            exc = None
            fut.set_exception(exc)
            exc = None
            del exc
        except:
            exc = None
            del exc

        return fut

    
    def _lookup_error(self = None, code = None):
        return pb.LookupRemoteEntryReply(error = pb.RemoteReadError(code = _as_pb_enum(code)))



class RemoteTreeProxyListener:
    
    def __init__(self = None, backend = None, socket_path = None, metrics_reporter = (None,)):
        self._backend = backend
        self._socket_path = socket_path
        self._metrics_reporter = metrics_reporter
        self._server = None
        self._service_server = None

    
    def start(self = None):
        self._server = tprt.uds_transport_server(self._socket_path)
        self._service_server = RemoteTreeProxyServer(self._server, _RemoteTreeProxyServiceImpl(self._backend, self._metrics_reporter))
        self._server.serve()
        if not os.path.exists(self._socket_path) or self._dial_succeeds():
            self.stop()
            raise RuntimeError(f'''remote-tree proxy listener failed to bind {self._socket_path}''')
        TRACE('remote-tree proxy listener serving over %s', self._socket_path)

    
    def _dial_succeeds(self = None):
        probe = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        
        try:
            probe.settimeout(_BIND_PROBE_TIMEOUT_S)
            probe.connect(self._socket_path)
            probe.close()
            return True
        except OSError:
            
            try:
                probe.close()
                return False
                
                try:
                    pass
                except:
                    probe.close()




    
    def stop(self = None):
        pass
    # WARNING: Decompyle incomplete



def _maybe_start_listener(thin_client_provider = None, metrics_reporter = None):
    if not IS_MAC:
        return None
    path = _socket_path()
# WARNING: Decompyle incomplete


class RemoteTreeProxyStartup:
    
    def __init__(self, gandalf = None, sync_engine_adapter = None, account = None, add_quit_handler = (None,), metrics_reporter = ('gandalf', 'Any', 'sync_engine_adapter', 'Any', 'account', 'Any', 'add_quit_handler', 'Callable[[Callable[..., None]], None]', 'metrics_reporter', 'Optional[SampleRecorderFactory]', 'return', 'None')):
        self._gandalf = gandalf
        self._sync_engine_adapter = sync_engine_adapter
        self._account = account
        self._add_quit_handler = add_quit_handler
        self._metrics_reporter = metrics_reporter
        self._lock = Lock()
        self._listener = None
        self._quit = False

    listener = (lambda self = None: self._listener)()
    
    def start_observing_rule(self = None):
        self._gandalf.add_on_changed_callback_any_account(self.match_rule)
        self._add_quit_handler(self._on_quit)
        self.match_rule()

    
    def match_rule(self = None):
        self._lock
        if self._quit:
            None(None, None)
            return None
    # WARNING: Decompyle incomplete

    
    def _on_quit(self = None, exit_code = None):
        self._lock
        self._quit = True
    # WARNING: Decompyle incomplete

    
    def _rule_allowed(self = None):
        return bool(self._gandalf.allows(_STORMCROW_RULE, account = self._account, treat_control_as_off = True))

    
    def _thin_client_or_none(self = None):
        if not self._sync_engine_adapter.is_ready(self._account):
            return None
        api = None._sync_engine_adapter.nucleus_api(self._account)
    # WARNING: Decompyle incomplete


