# Source Generated with Decompyle++
# File: tprt_control_endpoint.pyc (Python 3.11)

from __future__ import absolute_import
import os
from concurrent import futures
from typing import Any, cast, Optional
import tprt
from dropbox.client.constants import AppDataPaths
from dropbox.client.fenix.type_converter import convert_sync_status_to_protobuf
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.proto.dropbox_meta_engine.sync_engine_api_slice_tprt_server import SyncEngineApiServer, SyncEngineApiService
from dropbox.proto.nucleus import sync_engine_status_pb2
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.foundation.context.user import UserContext
_SOCKET_NAME = 'sync_engine_api_socket'

def _bridge_to_concurrent_future(foundation_future = None):
    pass
# WARNING: Decompyle incomplete


class _SyncEngineApiServiceImpl(SyncEngineApiService):
    
    def __init__(self = None, app = None, primary_account_id = None):
        self._app = app
        self._primary_account_id = primary_account_id

    
    def _get_user_context(self = None, primary_account_id = None):
        machine_context = self._app.app_model.machine_context
        account_models = machine_context.account_manager.account_models
        for account, account_model in account_models.items():
            if account.account_id == primary_account_id:
                
                return None, account_model.user_context
            return None

    
    def GetSyncEngineStatus(self = None, rpc_controller = None, Request = None, done_unused = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupByLocalPath(self = None, rpc_controller = None, Request = None, done_unused = (None,)):
        return self._forward_to_modern_client('LookupByLocalPath', Request)

    
    def UpdateHydrationPolicy(self = None, rpc_controller = None, Request = None, done_unused = (None,)):
        return self._forward_to_modern_client('UpdateHydrationPolicy', Request)

    
    def LookupByFileId(self = None, rpc_controller = None, Request = None, done_unused = (None,)):
        return self._forward_to_modern_client('LookupByFileId', Request)

    
    def _forward_to_modern_client(self = None, method_name = None, request = None):
        RpcController = RpcController
        import google.protobuf.service
        user_context = self._get_user_context(self._primary_account_id)
    # WARNING: Decompyle incomplete



class TprtControlEndpoint:
    
    def __init__(self = None, app = None, primary_account_id = None):
        self.app = app
        self._primary_account_id = primary_account_id
        self._server = None
        self._api_server = None

    
    def start(self = None):
        if not self._primary_account_id:
            TRACE('!! TprtControlEndpoint: no primary account_id; not starting dropboxctl control endpoint')
            return None
        socket_path = None.path.join(AppDataPaths.dropbox_appdata_path, _SOCKET_NAME)
        self._server = tprt.uds_transport_server(socket_path)
        service = _SyncEngineApiServiceImpl(self.app, self._primary_account_id)
        self._api_server = SyncEngineApiServer(self._server, service)
        self._server.serve()
        TRACE('TprtControlEndpoint: started SyncEngineApi listener on %s', socket_path)


