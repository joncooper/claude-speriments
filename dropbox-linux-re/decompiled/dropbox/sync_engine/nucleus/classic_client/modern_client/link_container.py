# Source Generated with Decompyle++
# File: link_container.pyc (Python 3.11)

from typing import Callable, Dict, Optional
from google.protobuf.empty_pb2 import Empty as EmptyPb
from google.protobuf.service import RpcController
from base import NucleusModernClientBase
from nucleus_decorators import boundary_api
from dropbox.foundation.futures import Future
from dropbox.metrics.function_usage import logged_method
from dropbox.model.types import FileId
from dropbox.proto.nucleus.app_service_pb2 import ContainerActionReply, ContainerActionResult, ContainerStateReq, DematerializeContainerReq, MaterializeContainerReq
from dropbox.proto.nucleus.link_container_pb2 import LinkContainerState
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto
from dropbox.proto.per_node_metadata.link_node_pb2 import LinkNodeEntity
from dropbox.sync_engine_boundary.link_container_interface import SyncEngineLinkContainerInterface
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, LinkContainerError
from dropbox.trace import TRACE

class NucleusLinkContainerClient(NucleusModernClientBase, SyncEngineLinkContainerInterface):
    container_state = (lambda self = None, fileid = None: self.modern_thin_client.ContainerState(RpcController(), ContainerStateReq(fileid = FileIdProto(id = fileid)), None).on_result((lambda resp: resp.state if resp.HasField('state') else None))
)()
    dematerialize_container = (lambda self = None, fileid = None: self.modern_thin_client.DematerializeContainer(RpcController(), DematerializeContainerReq(fileid = FileIdProto(id = fileid)), None).on_result(self._handle_container_result))()
    list_containers = (lambda self = None: self.modern_thin_client.ListContainers(RpcController(), EmptyPb(), None).on_result((lambda resp: resp.containers()))
)()
    materialize_container = (lambda self = None, fileid = None: self.modern_thin_client.MaterializeContainer(RpcController(), MaterializeContainerReq(fileid = FileIdProto(id = fileid)), None).on_result(self._handle_container_result))()
    
    def _handle_container_result(self = None, proto = None):
        result = proto.result
        if result == ContainerActionResult.CONTAINER_ACTION_SUCCESS:
            return None
        raise LinkContainerError(result)

    on_link_container_changed = (lambda self = None, callback = None: TRACE('NUCLEUS: Subscribe published event on_link_container_changed')self.callback_processor.on_link_container_changed(callback))()
    remove_on_link_container_changed = (lambda self = None, token = None: TRACE('NUCLEUS: remove_on_link_container_changed')self.callback_processor.remove_on_link_container_changed(token))()

