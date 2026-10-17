# Source Generated with Decompyle++
# File: backend.pyc (Python 3.11)

from __future__ import annotations
import functools
import os
from abc import ABC, abstractmethod
from concurrent.futures import Future, TimeoutError as FuturesTimeout
from enum import IntEnum
from typing import Callable, Concatenate, Iterable, Iterator, NamedTuple, Optional, ParamSpec, Protocol, Tuple, Type, TypeVar, Union
import tprt
from cffi_transport.exceptions import ServiceNotAvailableException
from google.protobuf.service import RpcController
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exceptions import NucleusPanicException
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.proto.nucleus import app_service_pb2 as engine_pb
from dropbox.proto.nucleus.app_service_pb2 import EnumerateRemoteDirReq, FetchByteRangeReq, LookupRemoteEntryReq
from dropbox.proto.nucleus.types_pb2 import FileId
from dropbox.sync_engine_boundary.exceptions import SyncEngineStoppedError

class RemoteReadErrorCode(IntEnum):
    UNKNOWN = engine_pb.REMOTE_READ_ERROR_UNKNOWN
    NOT_READY = engine_pb.REMOTE_READ_ERROR_NOT_READY
    NOT_FOUND = engine_pb.REMOTE_READ_ERROR_NOT_FOUND
    STALE_REVISION = engine_pb.REMOTE_READ_ERROR_STALE_REVISION
    INACCESSIBLE = engine_pb.REMOTE_READ_ERROR_INACCESSIBLE
    TRANSIENT = engine_pb.REMOTE_READ_ERROR_TRANSIENT
    REJECTED = engine_pb.REMOTE_READ_ERROR_REJECTED


class RemoteEntryType(IntEnum):
    UNKNOWN = engine_pb.REMOTE_ENTRY_UNKNOWN
    FILE = engine_pb.REMOTE_ENTRY_FILE
    DIRECTORY = engine_pb.REMOTE_ENTRY_DIRECTORY
    SYMLINK = engine_pb.REMOTE_ENTRY_SYMLINK
    MOUNT = engine_pb.REMOTE_ENTRY_MOUNT
    CLOUDDOC = engine_pb.REMOTE_ENTRY_CLOUDDOC


class RemoteEntryAttribute(IntEnum):
    UNKNOWN = engine_pb.REMOTE_ENTRY_ATTRIBUTE_UNKNOWN
    ENCRYPTED = engine_pb.REMOTE_ENTRY_ATTRIBUTE_ENCRYPTED
    HIDDEN = engine_pb.REMOTE_ENTRY_ATTRIBUTE_HIDDEN

_MirrorT = TypeVar('_MirrorT', bound = IntEnum)

def _mirrored(mirror = None, ordinal = None):
    
    try:
        return mirror(ordinal)
    except ValueError:
        return 


_ENGINE_UNAVAILABLE_ERRORS: 'Tuple[Type[BaseException], ...]' = (SyncEngineStoppedError, ServiceNotAvailableException, NucleusPanicException)
_ENGINE_TRANSPORT_ERRORS: 'Tuple[Type[BaseException], ...]' = (tprt.TransportError,)
_NO_ENGINE_CLIENT_ERRORS: 'Tuple[Type[BaseException], ...]' = _ENGINE_UNAVAILABLE_ERRORS + _ENGINE_TRANSPORT_ERRORS

class RemoteEntry(NamedTuple):
    attributes: 'Tuple[RemoteEntryAttribute, ...]' = 'RemoteEntry'


class ServedRange(NamedTuple):
    data: 'bytes' = 'ServedRange'


class RemoteReadFailure(NamedTuple):
    code: 'RemoteReadErrorCode' = 'RemoteReadFailure'
    stale_revision_new_content_hash: 'bytes' = b''
    stale_revision_new_size: 'int' = 0

FetchByteRangeResult = Union[(ServedRange, RemoteReadFailure)]
EnumerateResult = Union[(Iterable[RemoteEntry], RemoteReadFailure)]
LookupResult = Union[(RemoteEntry, RemoteReadFailure)]

class RemoteTreeProxyBackend(ABC):
    fetch_byte_range = (lambda self, fileid, content_hash = None, offset = None, length = abstractmethod, alignment = ('fileid', 'str', 'content_hash', 'bytes', 'offset', 'int', 'length', 'int', 'alignment', 'int', 'return', 'FetchByteRangeResult'): raise NotImplementedError)()
    enumerate_remote_dir = (lambda self = None, dbx_rr_path = None: raise NotImplementedError)()
    lookup_remote_entry = (lambda self = None, dbx_rr_path = None: raise NotImplementedError)()

_ReadArgsT = ParamSpec('_ReadArgsT')
_ReplyT = TypeVar('_ReplyT')

class _EngineThinClient(Protocol):
    
    def FetchByteRange(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'FetchByteRangeReq', 'done', 'Optional[Callable[[engine_pb.FetchByteRangeReply], None]]', 'return', 'Future[engine_pb.FetchByteRangeReply]')):
        pass

    
    def EnumerateRemoteDir(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'EnumerateRemoteDirReq', 'done', 'Optional[Callable[[engine_pb.EnumerateRemoteDirReply], None]]', 'return', 'Future[engine_pb.EnumerateRemoteDirReply]')):
        pass

    
    def LookupRemoteEntry(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupRemoteEntryReq', 'done', 'Optional[Callable[[engine_pb.LookupRemoteEntryReply], None]]', 'return', 'Future[engine_pb.LookupRemoteEntryReply]')):
        pass



class _EngineNotReady(Exception):
    pass


def _return_not_ready_without_an_engine(read = None):
    pass
# WARNING: Decompyle incomplete


class EngineRemoteTreeProxyBackend(RemoteTreeProxyBackend):
    _ENGINE_RPC_TIMEOUT_S = 5
    
    def __init__(self = None, thin_client_provider = None):
        self._thin_client_provider = thin_client_provider

    
    def _engine_client(self = None):
        
        try:
            client = self._thin_client_provider()
        except _NO_ENGINE_CLIENT_ERRORS:
            raise _EngineNotReady, None

    # WARNING: Decompyle incomplete

    
    def _call(self = None, send = None):
        
        try:
            return send().result(timeout = self._ENGINE_RPC_TIMEOUT_S)
        except FuturesTimeout:
            return 
            except AttributeError:
                report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_ENGINE)
                return 
            except _ENGINE_UNAVAILABLE_ERRORS:
                return 
            except _ENGINE_TRANSPORT_ERRORS:
                return 


    _pread_exact = (lambda fd = None, count = None, pos = staticmethod: chunks = []got = 0# WARNING: Decompyle incomplete
)()
    
    def _to_remote_entry(self = None, e = None):
        return e.fileid.id(filename = _mirrored(RemoteEntryType, int(e.type)), fileid = bytes(e.content_hash), type = int(e.size), content_hash = int(e.mtime), size = None, mtime = tuple, attributes = (lambda .0: pass# WARNING: Decompyle incomplete
)(e.attributes()))

    fetch_byte_range = (lambda self, fileid, content_hash = None, offset = None, length = _return_not_ready_without_an_engine, alignment = ('fileid', 'str', 'content_hash', 'bytes', 'offset', 'int', 'length', 'int', 'alignment', 'int', 'return', 'FetchByteRangeResult'): pass# WARNING: Decompyle incomplete
)()
    enumerate_remote_dir = (lambda self = None, dbx_rr_path = None: pass# WARNING: Decompyle incomplete
)()
    
    def _to_remote_entries(self = None, pb_entries = None):
        pass
    # WARNING: Decompyle incomplete

    lookup_remote_entry = (lambda self = None, dbx_rr_path = None: pass# WARNING: Decompyle incomplete
)()

