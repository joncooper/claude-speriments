# Source Generated with Decompyle++
# File: sync_engine_api.pyc (Python 3.11)

from typing import Any, cast, Dict, List, Tuple
from google.protobuf.empty_pb2 import Empty as EmptyPb
from google.protobuf.service import RpcController
from build_number.features import feature_enabled
from base import named_partial
from dropbox.client.authentication.account import Account
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.generated_types.shared_pb2 import FileIdPathPair
from dropbox.client.fenix.generated_types.sync_engine_pb2 import FileIdRemotePropertiesPair, GetHiddenStateReply, GetSyncPhaseReply, LookupByLocalPathBatchReply, LookupByLocalPathBatchReq, LookupRemotePropertiesByFileIdBatchReply, LookupRemotePropertiesByFileIdBatchReq, PathLocationPropertiesPair, PauseSyncEngineReply, ResumeSyncEngineReply, ResumeSyncEngineReq, UpdatePriorityHintReply
from dropbox.client.fenix.meta_engine_apis.generated_base_classes.sync_engine_api_base import _SyncEngineBaseClass
from dropbox.client.fenix.type_converter import convert_sync_phase_to_protobuf, convert_sync_status_to_protobuf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.raii2 import destroying
from dropbox.model.types import FileId
from dropbox.proto.nucleus.app_service_pb2 import LookupByFileIdBatchReply, LookupByFileIdBatchReq, LookupByFileIdReply
from dropbox.proto.nucleus.common_api_types_pb2 import DeleteRemoteSyncedIgnoredDirectoryFilesReply, DeleteRemoteSyncedIgnoredDirectoryFilesReq, DeleteRemoteSyncedIgnoredFileReply, DeleteRemoteSyncedIgnoredFileReq, GetHomeFolderPathReply, GetRemoteMountPointsInfoReply, GetRemoteMountPointsInfoReq, GetRemoteSyncedIgnoredFilesReply, GetRemoteSyncedIgnoredFilesReq, LocalLocationProperties, LookupByFileIdReq, LookupByLocalPathReply, LookupByLocalPathReq, LookupSyncIconReply, LookupSyncIconReq, RemoteLocationProperties, UpdateHiddenStateReq, UpdateHydrationPolicyReq, UpdatePriorityHintReq
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveEvent, ReactiveRequest
from dropbox.proto.nucleus.sync_engine_status_pb2 import SyncEngineStatus as SyncEngineStatusProto
from dropbox.proto.nucleus.types_pb2 import FileId as ProtoFileId
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.selective_sync_by_path_interface import FileIdRRServerPaths
from dropbox.sync_engine_boundary.types.sync_engine_status import SyncEngineStatus
from dropbox.sync_engine_boundary.types.sync_progress import SyncProgress
from dropbox.sync_engine_boundary.types.sync_queue import SyncPriority
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.foundation.account_manager import AccountModel

class SyncEngineAPI(_SyncEngineBaseClass):
    pass
# WARNING: Decompyle incomplete

