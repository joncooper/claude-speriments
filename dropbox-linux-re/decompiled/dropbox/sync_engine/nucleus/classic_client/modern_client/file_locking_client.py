# Source Generated with Decompyle++
# File: file_locking_client.pyc (Python 3.11)

from google.protobuf.service import RpcController
from base import NucleusModernClientBase
from nucleus_decorators import boundary_api
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.proto.nucleus.app_service_pb2 import LookupLockStatusByFileIdReply, LookupLockStatusByFileIdReq
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto
from dropbox.sync_engine_boundary.file_locking.file_locking_sync_interface import SyncEngineFileLockingInterface
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockStatus

class NucleusFileLockingClient(NucleusModernClientBase, SyncEngineFileLockingInterface):
    lookup_lock_state = (lambda self = None, fileid = None: 
def convert_status(reply = None):
status_proto = reply.lock_status# WARNING: Decompyle incomplete
self.modern_thin_client.LookupLockStatusByFileId(RpcController(), LookupLockStatusByFileIdReq(fileid = FileIdProto(id = fileid)), None).on_result(convert_status))()

