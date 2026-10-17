# Source Generated with Decompyle++
# File: selective_sync_client.pyc (Python 3.11)

from typing import Callable, Set
from google.protobuf.empty_pb2 import Empty as EmptyPb
from google.protobuf.service import RpcController
from transitional_utils.futures import parasitic_future
from base import NucleusModernClientBase
from nucleus_decorators import boundary_api
from dropbox.foundation.futures import Future
from dropbox.infinite import infinite_exposed
from dropbox.model.types import FileId
from dropbox.proto.nucleus.common_api_types_pb2 import GetHiddenStateReply, UpdateHiddenStateReply, UpdateHiddenStateReq
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto
from dropbox.sync_engine_boundary.device_anchor_interface import DeviceAnchorParentError
from dropbox.sync_engine_boundary.nucleus_selective_sync_inteface import NucleusSelectiveSyncInterface
from dropbox.trace import TRACE

class NucleusSelectiveSyncClient(NucleusModernClientBase, NucleusSelectiveSyncInterface):
    
    def _change_fileid_hidden_set(self = None, new_fileid_hidden_set = None, infinitize_unignores = None):
        
        def convert_reply(resp = None):
            if resp.update_hidden_state_error == UpdateHiddenStateReply.DEVICE_ANCHOR_PARENT:
                raise DeviceAnchorParentError

        if infinite_exposed(self._gandalf, self._account) and infinitize_unignores:
            TRACE('NUCLEUS: Infinite is not supported in this configuration')
            infinitize_unignores = False
        return None(UpdateHiddenStateReq, (lambda .0: [ FileIdProto(id = fileid) for fileid in .0 ])(fileids = new_fileid_hidden_set(), infinitize_unignores = infinitize_unignores), None).on_result(convert_reply)

    
    def _update_hidden_set(self = None, fileids = None, update_fn = None, infinitize_unignores = (False,)):
        pass
    # WARNING: Decompyle incomplete

    change_fileid_hidden_set = (lambda self = None, new_fileid_hidden_set = None, infinitize_unignores = boundary_api: TRACE('NUCLEUS: change_fileid_hidden_set fileids=%r, infinitize_unignores=%r', new_fileid_hidden_set, infinitize_unignores)self._change_fileid_hidden_set(new_fileid_hidden_set, infinitize_unignores))()
    hidden_set_add = (lambda self = None, fileids = None: TRACE('NUCLEUS: hidden_set_add fileids=%r', fileids)self._update_hidden_set(fileids, set.add))()
    hidden_set_remove = (lambda self = None, fileids = None, infinitize_unignores = boundary_api: TRACE('NUCLEUS: hidden_set_remove fileids=%r', fileids)self._update_hidden_set(fileids, set.discard, infinitize_unignores))()
    get_fileid_hidden_set = (lambda self = None: TRACE('NUCLEUS:  get_fileid_hidden_set')
def convert_reply(resp = None):
resp.fileids()self.modern_thin_client.GetHiddenState(RpcController(), EmptyPb(), None).on_result(convert_reply))()

