# Source Generated with Decompyle++
# File: fs_api_thin_client.pyc (Python 3.11)

from __future__ import annotations
from concurrent.futures import Future as PythonFuture
from typing import Callable, Generic, Optional, TypeVar
from google.protobuf.empty_pb2 import Empty
from google.protobuf.service import RpcController
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.thread import ThreadPoolExecutor
from dropbox.foundation.transitional.wrapper_future import create_and_wrap_future
from dropbox.fs_api.fs_api_adapter import FsApiAdapter
from dropbox.proto.fs_api.fs_api_service_pb2 import CreateTempVolumeReply, CreateTempVolumeReq, DropTempVolumeReply, DropTempVolumeReq, RenameIntoDropboxRequest
from dropbox.proto.fs_api.fs_api_service_tprt_client import StreamingQueue
from dropbox.proto.nucleus.app_service_pb2 import AllowUserAccessReply, AllowUserAccessReq, BindIntoDropboxReply, BindIntoDropboxReq, CreateBreadcrumbsReply, CreateBreadcrumbsReq, CreateEphemeralTempDirReply, DenyUserAccessReply, DenyUserAccessReq, GetOSFolderPathReply, GetOSFolderPathReq, MergeIntoDropboxReply, MergeIntoDropboxReq, RemoveBreadcrumbsReply, RemoveBreadcrumbsReq, UnbindFromDropboxReply, UnbindFromDropboxReq, UnmergeFromDropboxReply, UnmergeFromDropboxReq
from dropbox.proto.nucleus.device_anchor_pb2 import DeleteDeviceAnchorReply, DeleteDeviceAnchorReq
from dropbox.proto.nucleus.published_event_pb2 import GetPublishedEventsReq, PublishedEvent
_T = TypeVar('_T')
_U = TypeVar('_U')

def FsApiThinClientResult():
    '''FsApiThinClientResult'''
    
    def __init__(self = None, base_future = None, boundary_thread_pool = None):
        self._thread_pool = boundary_thread_pool
        self._base_future = base_future

    
    def on_result(self = None, handler = None):
        pass
    # WARNING: Decompyle incomplete

    
    def discard_result(self = None):
        return self._base_future.discard_value()

    
    def deprecated_wait_for_result(self = None):
        self._base_future.block()
        return self._base_future.result()


FsApiThinClientResult = <NODE:27>(FsApiThinClientResult, 'FsApiThinClientResult', Generic[_T])
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_Result = TypeVar('_Result')

class FsApiThinClient:
    
    def __init__(self = None, fs_api_adapter = None, boundary_thread_pool = None):
        self._fs_api_adapter = fs_api_adapter
        self._boundary_thread_pool = boundary_thread_pool

    
    def __wrap_thin_client_call(self = None, tc_func = None):
        pass
    # WARNING: Decompyle incomplete

    
    def stop(self = None):
        self._fs_api_adapter.stop()

    
    def GetOSFolderPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetOSFolderPathReq', 'done', 'Optional[Callable[[GetOSFolderPathReply], None]]', 'return', 'FsApiThinClientResult[GetOSFolderPathReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.GetOSFolderPath)(rpc_controller, request, done)

    
    def CreateBreadcrumbs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'CreateBreadcrumbsReq', 'done', 'Optional[Callable[[CreateBreadcrumbsReply], None]]', 'return', 'FsApiThinClientResult[CreateBreadcrumbsReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.CreateBreadcrumbs)(rpc_controller, request, done)

    
    def CreateTempVolume(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'CreateTempVolumeReq', 'done', 'Optional[Callable[[CreateTempVolumeReply], None]]', 'return', 'FsApiThinClientResult[CreateTempVolumeReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.CreateTempVolume)(rpc_controller, request, done)

    
    def DropTempVolume(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DropTempVolumeReq', 'done', 'Optional[Callable[[DropTempVolumeReply], None]]', 'return', 'FsApiThinClientResult[DropTempVolumeReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.DropTempVolume)(rpc_controller, request, done)

    
    def RemoveBreadcrumbs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'RemoveBreadcrumbsReq', 'done', 'Optional[Callable[[RemoveBreadcrumbsReply], None]]', 'return', 'FsApiThinClientResult[RemoveBreadcrumbsReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.RemoveBreadcrumbs)(rpc_controller, request, done)

    
    def AllowUserAccess(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'AllowUserAccessReq', 'done', 'Optional[Callable[[AllowUserAccessReply], None]]', 'return', 'FsApiThinClientResult[AllowUserAccessReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.AllowUserAccess)(rpc_controller, request, done)

    
    def DenyUserAccess(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DenyUserAccessReq', 'done', 'Optional[Callable[[DenyUserAccessReply], None]]', 'return', 'FsApiThinClientResult[DenyUserAccessReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.DenyUserAccess)(rpc_controller, request, done)

    
    def BindIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'BindIntoDropboxReq', 'done', 'Optional[Callable[[BindIntoDropboxReply], None]]', 'return', 'FsApiThinClientResult[BindIntoDropboxReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.BindIntoDropbox)(rpc_controller, request, done)

    
    def GetPublishedEvents(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetPublishedEventsReq', 'done', 'Optional[Callable[[PublishedEvent], None]]', 'return', 'StreamingQueue')):
        return self._fs_api_adapter.GetPublishedEvents(rpc_controller, request, done)

    
    def UnbindFromDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UnbindFromDropboxReq', 'done', 'Optional[Callable[[UnbindFromDropboxReply], None]]', 'return', 'FsApiThinClientResult[UnbindFromDropboxReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.UnbindFromDropbox)(rpc_controller, request, done)

    
    def UnmergeFromDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UnmergeFromDropboxReq', 'done', 'Optional[Callable[[UnmergeFromDropboxReply], None]]', 'return', 'FsApiThinClientResult[UnmergeFromDropboxReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.UnmergeFromDropbox)(rpc_controller, request, done)

    
    def MergeIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'MergeIntoDropboxReq', 'done', 'Optional[Callable[[MergeIntoDropboxReply], None]]', 'return', 'FsApiThinClientResult[MergeIntoDropboxReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.MergeIntoDropbox)(rpc_controller, request, done)

    
    def CreateEphemeralTempDir(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[CreateEphemeralTempDirReply], None]]', 'return', 'FsApiThinClientResult[CreateEphemeralTempDirReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.CreateEphemeralTempDir)(rpc_controller, request, done)

    
    def RenameIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'RenameIntoDropboxRequest', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'FsApiThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.RenameIntoDropbox)(rpc_controller, request, done)

    
    def DeleteDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DeleteDeviceAnchorReq', 'done', 'Optional[Callable[[DeleteDeviceAnchorReply], None]]', 'return', 'FsApiThinClientResult[DeleteDeviceAnchorReply]')):
        return self.__wrap_thin_client_call(self._fs_api_adapter.DeleteDeviceAnchor)(rpc_controller, request, done)


