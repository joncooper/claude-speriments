# Source Generated with Decompyle++
# File: sync_engine_api_base.pyc (Python 3.11)

from typing import Dict, Callable, Optional
from dropbox.client.fenix.event_hub import EventHub
from dropbox.client.fenix.meta_engine_api import MetaEngineBaseClass
from dropbox.client.fenix.meta_engine_apis.base import serialize_protobuf_response, wrap_typed_handler
from abc import abstractmethod
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.client.fenix.generated_types.sync_engine_pb2 import GetHiddenStateReply, GetSyncPhaseReply, LookupByLocalPathBatchReply, LookupByLocalPathBatchReq, LookupRemotePropertiesByFileIdBatchReply, LookupRemotePropertiesByFileIdBatchReq, PauseSyncEngineReply, ResumeSyncEngineReply, ResumeSyncEngineReq, TPRTReply, TPRTReq, UpdatePriorityHintReply
from dropbox.proto.nucleus.common_api_types_pb2 import DeleteRemoteSyncedIgnoredDirectoryFilesReply, DeleteRemoteSyncedIgnoredDirectoryFilesReq, DeleteRemoteSyncedIgnoredFileReply, DeleteRemoteSyncedIgnoredFileReq, GetHomeFolderPathReply, GetRemoteMountPointsInfoReply, GetRemoteMountPointsInfoReq, GetRemoteSyncedIgnoredFilesReply, GetRemoteSyncedIgnoredFilesReq, LocalLocationProperties, LookupByFileIdReq, LookupByLocalPathReply, LookupByLocalPathReq, LookupSyncIconReply, LookupSyncIconReq, RemoteLocationProperties, UpdateHiddenStateReq, UpdateHydrationPolicyReq, UpdatePriorityHintReq
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveEvent, ReactiveRequest
from dropbox.proto.nucleus.sync_engine_status_pb2 import SyncEngineStatus
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class _SyncEngineBaseClass(MetaEngineBaseClass):
    pass
# WARNING: Decompyle incomplete


class _FSSEngineBaseClass(MetaEngineBaseClass):
    pass
# WARNING: Decompyle incomplete

