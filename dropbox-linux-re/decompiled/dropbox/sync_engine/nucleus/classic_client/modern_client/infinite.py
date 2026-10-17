# Source Generated with Decompyle++
# File: infinite.pyc (Python 3.11)

from typing import Callable, Iterable, List
from google.protobuf.service import RpcController
from base import NucleusModernClientBase
from nucleus_decorators import boundary_api
from dropbox.exception.reporting import report_assertion_error
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.infinite import infinite_exposed
from dropbox.infinite.pager import CancelPageRequest, PageFileRequest, PageResponse
from dropbox.metrics.function_usage import logged_method
from dropbox.model.types import FileId
from dropbox.proto.nucleus.app_service_pb2 import CancelRecallReq, HydratePlaceholderReply, HydratePlaceholderReq, UpdateInfiniteOperatingModeReq
from dropbox.proto.nucleus.common_api_types_pb2 import UpdateHydrationPolicyReq
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto, HydrationPolicy
from dropbox.sync_engine_boundary.infinite.constants import InfiniteOperatingMode
from dropbox.sync_engine_boundary.infinite.infinite_interface import NucleusInfiniteInterface
from dropbox.trace import TRACE

class NucleusInfiniteClient(NucleusModernClientBase, NucleusInfiniteInterface):
    _infinite_transition_state = (lambda self = None, fileids = None, recursive = boundary_api, state = ('fileids', 'Iterable[FileId]', 'recursive', 'bool', 'state', 'HydrationPolicy.V', 'return', 'Future[None]'): strategy = UpdateHydrationPolicyReq.RECURSIVE if recursive else UpdateHydrationPolicyReq.SELF_ONLYNone(UpdateHydrationPolicyReq, (lambda .0: [ FileIdProto(id = fileid) for fileid in .0 ])(fileids = fileids(), desired_policy = state, strategy = strategy), None).discard_result()
)()
    infinite_evict_batch = (lambda self = None, fileids = None, recursive = boundary_api: self._infinite_transition_state(fileids, recursive, HydrationPolicy.ONLINE_ONLY))()
    infinite_recall_batch = (lambda self = None, fileids = None, recursive = boundary_api: self._infinite_transition_state(fileids, recursive, HydrationPolicy.LOCAL))()
    update_infinite_operating_mode = (lambda self = None, operating_mode = None: if operating_mode == InfiniteOperatingMode.INFINITE_FULLY_ENABLED:
mode = UpdateInfiniteOperatingModeReq.INFINITE_FULLY_ENABLEDelif operating_mode == InfiniteOperatingMode.INFINITE_FULLY_DISABLED:
mode = UpdateInfiniteOperatingModeReq.INFINITE_FULLY_DISABLEDelif operating_mode in (InfiniteOperatingMode.IGNORE_FOLDER_POLICY, InfiniteOperatingMode.DEFAULT):
mode = UpdateInfiniteOperatingModeReq.INFINITE_SOFT_DISABLEDelif operating_mode == InfiniteOperatingMode.IGNORE_FOLDER_POLICY_AND_RECALL_PLACEHOLDERS:
mode = UpdateInfiniteOperatingModeReq.INFINITE_SOFT_DISABLEDelse:
report_assertion_error('Unhandled InfiniteOperatingMode: %s', operating_mode)ResolvedFuture(False)None.modern_thin_client.UpdateInfiniteOperatingMode(RpcController(), UpdateInfiniteOperatingModeReq(mode = mode), None).on_result((lambda _: True))
)()
    set_infinite_page_response_callback = (lambda self = None, callback = None: self.infinite_page_response_callback = callback)()
    infinite_cancel_batch = (lambda self = None, cancel_ids = None: if not infinite_exposed(self._gandalf, self._account):
TRACE('NUCLEUS: Infinite recall cancellation is not supported in this configuration')ResolvedFuture(None)None.modern_thin_client.CancelRecall(RpcController(), CancelRecallReq(paging_request_ids = cancel_ids), None).discard_result())()
    infinite_ensure_recalled = (lambda self = None, fileid = None: 
def _done(reply = None):
if reply.response == HydratePlaceholderReply.HydrateResponse.CANCEL:
raise Exception('Unable to recall placeholder')self.modern_thin_client.HydratePlaceholder(RpcController(), HydratePlaceholderReq(fileid = HydratePlaceholderReq.FileIdTransferKey(fileid = FileIdProto(id = fileid))), None).on_result(_done))()
    infinite_cancel_page_request = (lambda self = None, request = None: TRACE('NUCLEUS: infinite_cancel_page_request %r', request.request_id)if not infinite_exposed(self._gandalf, self._account):
TRACE('NUCLEUS: Infinite recall cancellation is not supported in this configuration')ResolvedFuture(None)# WARNING: Decompyle incomplete
)()

