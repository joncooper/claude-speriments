# Source Generated with Decompyle++
# File: fs_api_service_tprt_client.pyc (Python 3.11)

from concurrent.futures import futures
import typing
import tprt
from google.protobuf.service import RpcController
from dropbox.proto.fs_api import fs_api_service_pb2 as dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2
from dropbox.proto.nucleus import app_service_pb2 as dropbox__dot__proto__dot__nucleus__dot__app_service_pb2
from dropbox.proto.nucleus import device_anchor_pb2 as dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2
from dropbox.proto.nucleus import feature_configs_pb2 as dropbox__dot__proto__dot__nucleus__dot__feature_configs_pb2
from dropbox.proto.nucleus import published_event_pb2 as dropbox__dot__proto__dot__nucleus__dot__published_event_pb2
from dropbox.proto.nucleus import sync_engine_pb2 as dropbox__dot__proto__dot__nucleus__dot__sync_engine_pb2
from dropbox.proto.nucleus import types_pb2 as dropbox__dot__proto__dot__nucleus__dot__types_pb2
from dropbox.proto.rust import extensions_pb2 as dropbox__dot__proto__dot__rust__dot__extensions_pb2
from dropbox.proto.sync import xattr_pb2 as dropbox__dot__proto__dot__sync__dot__xattr_pb2
from google.protobuf import empty_pb2 as google__dot__protobuf__dot__empty_pb2

class FsApiClient:
    
    def __init__(self = None, raw_client = None):
        self._raw_client = raw_client

    
    def Example(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.ExampleReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.ExampleReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.ExampleReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetOSFolderPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetOSFolderPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetOSFolderPathReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetOSFolderPathReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CreateBreadcrumbs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateBreadcrumbsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateBreadcrumbsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateBreadcrumbsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def RemoveBreadcrumbs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RemoveBreadcrumbsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RemoveBreadcrumbsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RemoveBreadcrumbsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def DenyUserAccess(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DenyUserAccessReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DenyUserAccessReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DenyUserAccessReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def AllowUserAccess(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AllowUserAccessReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AllowUserAccessReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AllowUserAccessReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def BindIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.BindIntoDropboxReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.BindIntoDropboxReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.BindIntoDropboxReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UnbindFromDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnbindFromDropboxReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnbindFromDropboxReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnbindFromDropboxReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UnmergeFromDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnmergeFromDropboxReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnmergeFromDropboxReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnmergeFromDropboxReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def MergeIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.MergeIntoDropboxReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.MergeIntoDropboxReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.MergeIntoDropboxReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CreateEphemeralTempDir(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateEphemeralTempDirReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateEphemeralTempDirReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def RenameIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.RenameIntoDropboxRequest', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetPublishedEvents(self = None, rpc_controller = None, request = None, done_unused = (None,)):
        req_buf = request.SerializeToString()
        tprt_queue = self._raw_client.streaming('/fs_api.FsApi/GetPublishedEvents', req_buf)
        return StreamingQueue(tprt_queue, dropbox__dot__proto__dot__nucleus__dot__published_event_pb2.PublishedEvent)

    
    def DeleteDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.DeleteDeviceAnchorReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.DeleteDeviceAnchorReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.DeleteDeviceAnchorReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CreateTempVolume(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.CreateTempVolumeReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.CreateTempVolumeReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.CreateTempVolumeReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def DropTempVolume(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.DropTempVolumeReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.DropTempVolumeReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__fs_api__dot__fs_api_service_pb2.DropTempVolumeReply]')):
        pass
    # WARNING: Decompyle incomplete



def _parse_and_complete(bytes_future, typed_future, output_type):
    pass
# WARNING: Decompyle incomplete


def _parse_response(future, output_type):
    pass
# WARNING: Decompyle incomplete


def _parse_stream_response(output, output_type):
    response = output_type()
    response.ParseFromString(output)
    return response


class StreamingQueue:
    
    def __init__(self, tprt_queue, message_type):
        self.tprt_queue = tprt_queue
        self.message_type = message_type

    
    def get(self):
        item = self.tprt_queue.get()
    # WARNING: Decompyle incomplete

    
    def stop(self):
        self.tprt_queue.stop()

    
    def size(self):
        return self.tprt_queue.qsize()

    
    def connection_reset(self):
        self.tprt_queue.connection_reset()


