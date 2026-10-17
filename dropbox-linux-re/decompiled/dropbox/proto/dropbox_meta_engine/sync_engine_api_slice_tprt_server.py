# Source Generated with Decompyle++
# File: sync_engine_api_slice_tprt_server.pyc (Python 3.11)

import abc
from concurrent.futures import futures
import typing
import tprt
from google.protobuf.service import RpcController
from dropbox.proto.nucleus import app_service_pb2 as dropbox__dot__proto__dot__nucleus__dot__app_service_pb2
from dropbox.proto.nucleus import common_api_types_pb2 as dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2
from dropbox.proto.nucleus import sync_engine_status_pb2 as dropbox__dot__proto__dot__nucleus__dot__sync_engine_status_pb2
from google.protobuf import empty_pb2 as google__dot__protobuf__dot__empty_pb2

def SyncEngineApiService():
    '''SyncEngineApiService'''
    GetSyncEngineStatus = (lambda self = None, rpc_controller = None, Request = abc.abstractmethod, done_unused = (None,): pass)()
    LookupByLocalPath = (lambda self = None, rpc_controller = None, Request = abc.abstractmethod, done_unused = (None,): pass)()
    LookupByFileId = (lambda self = None, rpc_controller = None, Request = abc.abstractmethod, done_unused = (None,): pass)()
    UpdateHydrationPolicy = (lambda self = None, rpc_controller = None, Request = abc.abstractmethod, done_unused = (None,): pass)()

SyncEngineApiService = <NODE:27>(SyncEngineApiService, 'SyncEngineApiService', metaclass = abc.ABCMeta)

class SyncEngineApiServer:
    
    def __init__(self = None, raw_server = None, service = None):
        self._raw_server = raw_server
        self._service = service
        self._handlers = {
            '/dropbox_meta_engine.SyncEngineApi/GetSyncEngineStatus': (self._service.GetSyncEngineStatus, google__dot__protobuf__dot__empty_pb2.Empty),
            '/dropbox_meta_engine.SyncEngineApi/LookupByLocalPath': (self._service.LookupByLocalPath, dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupByLocalPathReq),
            '/dropbox_meta_engine.SyncEngineApi/LookupByFileId': (self._service.LookupByFileId, dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupByFileIdReq),
            '/dropbox_meta_engine.SyncEngineApi/UpdateHydrationPolicy': (self._service.UpdateHydrationPolicy, dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.UpdateHydrationPolicyReq) }
        raw_server.register_unary(self._server_unary_handler)

    
    def _server_unary_handler(self = None, path = None, buf = None):
        pass
    # WARNING: Decompyle incomplete



def _parse_and_complete(typed_future, bytes_future):
    pass
# WARNING: Decompyle incomplete

