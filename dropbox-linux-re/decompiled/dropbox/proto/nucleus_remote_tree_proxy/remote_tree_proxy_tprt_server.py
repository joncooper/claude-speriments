# Source Generated with Decompyle++
# File: remote_tree_proxy_tprt_server.pyc (Python 3.11)

import abc
from concurrent.futures import futures
import typing
import tprt
from google.protobuf.service import RpcController
from dropbox.proto.nucleus_remote_tree_proxy import remote_tree_proxy_pb2 as dropbox__dot__proto__dot__nucleus_remote_tree_proxy__dot__remote_tree_proxy_pb2

def RemoteTreeProxyService():
    '''RemoteTreeProxyService'''
    FetchByteRange = (lambda self = None, rpc_controller = None, Request = abc.abstractmethod, done_unused = (None,): pass)()
    EnumerateRemoteDir = (lambda self = None, rpc_controller = None, Request = abc.abstractmethod, done_unused = (None,): pass)()
    LookupRemoteEntry = (lambda self = None, rpc_controller = None, Request = abc.abstractmethod, done_unused = (None,): pass)()

RemoteTreeProxyService = <NODE:27>(RemoteTreeProxyService, 'RemoteTreeProxyService', metaclass = abc.ABCMeta)

class RemoteTreeProxyServer:
    
    def __init__(self = None, raw_server = None, service = None):
        self._raw_server = raw_server
        self._service = service
        self._handlers = {
            '/nucleus_remote_tree_proxy.RemoteTreeProxy/FetchByteRange': (self._service.FetchByteRange, dropbox__dot__proto__dot__nucleus_remote_tree_proxy__dot__remote_tree_proxy_pb2.FetchByteRangeReq),
            '/nucleus_remote_tree_proxy.RemoteTreeProxy/EnumerateRemoteDir': (self._service.EnumerateRemoteDir, dropbox__dot__proto__dot__nucleus_remote_tree_proxy__dot__remote_tree_proxy_pb2.EnumerateRemoteDirReq),
            '/nucleus_remote_tree_proxy.RemoteTreeProxy/LookupRemoteEntry': (self._service.LookupRemoteEntry, dropbox__dot__proto__dot__nucleus_remote_tree_proxy__dot__remote_tree_proxy_pb2.LookupRemoteEntryReq) }
        raw_server.register_unary(self._server_unary_handler)

    
    def _server_unary_handler(self = None, path = None, buf = None):
        pass
    # WARNING: Decompyle incomplete



def _parse_and_complete(typed_future, bytes_future):
    pass
# WARNING: Decompyle incomplete

