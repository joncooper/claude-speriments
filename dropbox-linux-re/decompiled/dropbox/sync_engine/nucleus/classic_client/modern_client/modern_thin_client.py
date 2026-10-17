# Source Generated with Decompyle++
# File: modern_thin_client.pyc (Python 3.11)

from __future__ import annotations
import threading
from concurrent.futures import Future as PythonFuture
from typing import Callable, Dict, Generic, List, Optional, Text, TypeVar
from cffi_transport.exceptions import ServiceNotAvailableException
from google.protobuf.empty_pb2 import Empty
from google.protobuf.service import RpcController
from thin_client.base import NucleusThinClient
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.thread import ThreadPoolExecutor
from dropbox.foundation.transitional.wrapper_future import create_and_wrap_future
from dropbox.model.types import NsId
from dropbox.proto.engine_wait_tracker.engine_waits_pb2 import GetActiveEngineWaitsReply
from dropbox.proto.nucleus.app_service_pb2 import AllowUserAccessReply, AllowUserAccessReq, BindIntoDropboxReply, BindIntoDropboxReq, BugReporterStatsReply, CancelRecallReq, CheckBlockExistsForPeerReply, CheckBlockExistsForPeerReq, CheckFPEligibilityReply, ContainerActionReply, ContainerStateReply, ContainerStateReq, CreateBreadcrumbsReply, CreateBreadcrumbsReq, CreateEphemeralTempDirReply, DematerializeContainerReq, DenyUserAccessReply, DenyUserAccessReq, DirtyPathsReply, DirtyPathsReq, DiskUsageReply, EchoMessage, EnumerateRemoteDirReply, EnumerateRemoteDirReq, EstimateFPMigrationDurationReply, FetchByteRangeReply, FetchByteRangeReq, FetchUnsyncableFileIdsResponse, FileProviderDumpReq, FPCutoverGoNoGoReq, GetAccountReply, GetBlockForPeerReply, GetBlockForPeerReq, GetConflictedPathReply, GetConflictedPathReq, GetCurrentComputerBackupSyncProgressReply, GetCurrentComputerBackupSyncProgressReq, GetCurrentDeviceAnchorSyncProgressReply, GetCurrentDeviceAnchorSyncProgressReq, GetDebugInfoReply, GetFilesystemInfoReply, GetFilesystemInfoReq, GetOSFolderPathReply, GetOSFolderPathReq, GetRemoteFeatureConfigsReply, GetSyncEngineStatusReply, HydratePlaceholderReply, HydratePlaceholderReq, ListContainersReply, ListDirByFileTypeReply, ListDirByFileTypeReq, ListDirLocalReply, ListDirLocalReq, LookupByFileIdBatchReply, LookupByFileIdBatchReq, LookupByFileIdReply, LookupFileIdByMRServerPathReq, LookupFileIdByRRServerPathReq, LookupFileIdReply, LookupLockStatusByFileIdReply, LookupLockStatusByFileIdReq, LookupMountPointUnderFileIdReply, LookupMountPointUnderFileIdReq, LookupNamespacesReply, LookupPropsByLocalPathReply, LookupPropsByLocalPathReq, LookupRemoteEntryReply, LookupRemoteEntryReq, MaterializeContainerReq, MergeIntoDropboxReply, MergeIntoDropboxReq, NotifyShadowDomainCreatedReq, PrepareForFPMigrationReply, RecordUpcomingFolderDeleteReply, RecordUpcomingFolderDeleteReq, RegisterCameraUploadsTagReq, RemoveBreadcrumbsReply, RemoveBreadcrumbsReq, RenameIntoDropboxRequest, RetrySyncReply, RetrySyncRequest, SendFileEventReply, SendFileEventReq, ServerComponentToLocalReply, ServerComponentToLocalReq, SetPathIgnoredStateReply, SetPathIgnoredStateReq, StartFPCutoverDryRunReply, StartFPCutoverDryRunReq, StartFPCutoverReply, StartFPCutoverReq, SubscribeForBackupSyncProgressReply, SubscribeForBackupSyncProgressReq, SuppressFSWsReply, SuppressFSWsReq, UnbindFromDropboxReply, UnbindFromDropboxReq, UnmergeFromDropboxReply, UnmergeFromDropboxReq, UnpackFPPackageReply, UnpackFPPackageReq, UpdateConfigReply, UpdateConfigReq, UpdateFeatureConfigReply, UpdateFeatureConfigRequest, UpdateInfiniteOperatingModeReq, UpdateP2PKeysReply, UpdateP2PKeysReq
from dropbox.proto.nucleus.common_api_types_pb2 import DeleteRemoteSyncedIgnoredDirectoryFilesReply, DeleteRemoteSyncedIgnoredDirectoryFilesReq, DeleteRemoteSyncedIgnoredFileReply, DeleteRemoteSyncedIgnoredFileReq, GetHiddenStateReply, GetHomeFolderPathReply, GetRemoteMountPointsInfoReply, GetRemoteMountPointsInfoReq, GetRemoteSyncedIgnoredFilesReply, GetRemoteSyncedIgnoredFilesReq, LocalLocationProperties, LookupByFileIdReq, LookupByLocalPathReply, LookupByLocalPathReq, LookupSyncIconReply, LookupSyncIconReq, RemoteLocationProperties, UpdateHiddenStateReply, UpdateHiddenStateReq, UpdateHydrationPolicyReq, UpdatePriorityHintReq
from dropbox.proto.nucleus.device_anchor_pb2 import BreakBackupByFileIdReply, BreakBackupByFileIdReq, BreakBackupByTargetPathReply, BreakBackupByTargetPathReq, CreateDeviceAnchorReply, CreateDeviceAnchorReq, DeleteDeviceAnchorReply, DeleteDeviceAnchorReq, GetDbxIgnoreContentsReply, GetDbxIgnoreContentsReq, GetDeviceAnchorMetadataByPathReply, GetDeviceAnchorMetadataByPathReq, ListDeviceAnchorsReply, ListDeviceAnchorsReq, PauseDeviceAnchorReply, PauseDeviceAnchorReq, ResolveDeviceAnchorReply, ResolveDeviceAnchorReq, ResumeDeviceAnchorReply, ResumeDeviceAnchorReq, SetDbxIgnoreContentsReply, SetDbxIgnoreContentsReq, ValidateAnchorTargetReply, ValidateAnchorTargetReq
from dropbox.proto.nucleus.published_event_pb2 import GetPublishedEventsReq, PublishedEvent
from dropbox.proto.nucleus.reactive_api_pb2 import ReactiveEvent, ReactiveRequest
from dropbox.proto.nucleus.sync_engine_pb2 import FPContextMenuPreferences
from dropbox.proto.nucleus.sync_failures_pb2 import GetSyncFailuresSummaryReply, GetSyncFailuresSummaryReq
from dropbox.proto.nucleus.types_pb2 import FileId as FileIdProto
_T = TypeVar('_T')
_U = TypeVar('_U')

def _PinnedResult():
    '''_PinnedResult'''
    pass
# WARNING: Decompyle incomplete

_PinnedResult = <NODE:27>(_PinnedResult, '_PinnedResult', Future[_T])

def ModernThinClientResult():
    '''ModernThinClientResult'''
    
    def __init__(self = None, base_future = None, boundary_thread_pool = None):
        self._thread_pool = boundary_thread_pool
        self._base_future = base_future

    
    def on_result(self = None, handler = None):
        pass
    # WARNING: Decompyle incomplete

    
    def discard_result(self = None):
        return self._base_future.discard_value()

    
    def wait_for_result(self = None):
        self._base_future.block()
        return self._base_future.result()


ModernThinClientResult = <NODE:27>(ModernThinClientResult, 'ModernThinClientResult', Generic[_T])
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_Result = TypeVar('_Result')

class ModernThinClient:
    
    def __init__(self = None, base_client = None, boundary_thread_pool = None):
        self._base_client = base_client
        self._boundary_thread_pool = boundary_thread_pool

    
    def __wrap_thin_client_call(self = None, tc_func = None):
        pass
    # WARNING: Decompyle incomplete

    
    def thin_lookup_by_fileid(self = None, fileid = None):
        return self._base_client.thin_lookup_by_fileid(fileid)

    
    def thin_lookup_remote_properties_by_fileid(self = None, fileid = None):
        return self._base_client.thin_lookup_remote_properties_by_fileid(fileid)

    
    def thin_lookup_local_properties_by_fileid(self = None, fileid = None):
        return self._base_client.thin_lookup_local_properties_by_fileid(fileid)

    
    def get_queue_stats(self = None):
        return self._base_client.get_queue_stats()

    
    def stop(self = None, stop_reason = None):
        return self._base_client.stop(stop_reason)

    
    def root_ns(self = None):
        return self._base_client.root_ns()

    
    def GetSyncProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetSyncProgress)(rpc_controller, request, done)

    
    def LookupByFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupByFileIdReq', 'done', 'Optional[Callable[[LookupByFileIdReply], None]]', 'return', 'ModernThinClientResult[LookupByFileIdReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupByFileId)(rpc_controller, request, done)

    
    def LookupByFileIdBatch(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupByFileIdBatchReq', 'done', 'Optional[Callable[[LookupByFileIdBatchReply], None]]', 'return', 'ModernThinClientResult[LookupByFileIdBatchReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupByFileIdBatch)(rpc_controller, request, done)

    
    def LookupSyncIcon(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupSyncIconReq', 'done', 'Optional[Callable[[LookupSyncIconReply], None]]', 'return', 'ModernThinClientResult[LookupSyncIconReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupSyncIcon)(rpc_controller, request, done)

    
    def LookupRemoteEntry(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupRemoteEntryReq', 'done', 'Optional[Callable[[LookupRemoteEntryReply], None]]', 'return', 'ModernThinClientResult[LookupRemoteEntryReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupRemoteEntry)(rpc_controller, request, done)

    
    def EnumerateRemoteDir(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'EnumerateRemoteDirReq', 'done', 'Optional[Callable[[EnumerateRemoteDirReply], None]]', 'return', 'ModernThinClientResult[EnumerateRemoteDirReply]')):
        return self.__wrap_thin_client_call(self._base_client.EnumerateRemoteDir)(rpc_controller, request, done)

    
    def FetchByteRange(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'FetchByteRangeReq', 'done', 'Optional[Callable[[FetchByteRangeReply], None]]', 'return', 'ModernThinClientResult[FetchByteRangeReply]')):
        return self.__wrap_thin_client_call(self._base_client.FetchByteRange)(rpc_controller, request, done)

    
    def HydratePlaceholder(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'HydratePlaceholderReq', 'done', 'Optional[Callable[[HydratePlaceholderReply], None]]', 'return', 'ModernThinClientResult[HydratePlaceholderReply]')):
        return self.__wrap_thin_client_call(self._base_client.HydratePlaceholder)(rpc_controller, request, done)

    
    def CancelRecall(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'CancelRecallReq', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.CancelRecall)(rpc_controller, request, done)

    
    def UpdateFeatureConfig(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UpdateFeatureConfigRequest', 'done', 'Optional[Callable[[UpdateFeatureConfigReply], None]]', 'return', 'ModernThinClientResult[UpdateFeatureConfigReply]')):
        return self.__wrap_thin_client_call(self._base_client.UpdateFeatureConfig)(rpc_controller, request, done)

    
    def UnmergeFromDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UnmergeFromDropboxReq', 'done', 'Optional[Callable[[UnmergeFromDropboxReply], None]]', 'return', 'ModernThinClientResult[UnmergeFromDropboxReply]')):
        return self.__wrap_thin_client_call(self._base_client.UnmergeFromDropbox)(rpc_controller, request, done)

    
    def GetSyncEngineStatus(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[GetSyncEngineStatusReply], None]]', 'return', 'ModernThinClientResult[GetSyncEngineStatusReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetSyncEngineStatus)(rpc_controller, request, done)

    
    def GetHomeFolderPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[GetHomeFolderPathReply], None]]', 'return', 'ModernThinClientResult[GetHomeFolderPathReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetHomeFolderPath)(rpc_controller, request, done)

    
    def UpdateConfig(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UpdateConfigReq', 'done', 'Optional[Callable[[UpdateConfigReply], None]]', 'return', 'ModernThinClientResult[UpdateConfigReply]')):
        return self.__wrap_thin_client_call(self._base_client.UpdateConfig)(rpc_controller, request, done)

    
    def UpdateP2PKeys(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UpdateP2PKeysReq', 'done', 'Optional[Callable[[UpdateP2PKeysReply], None]]', 'return', 'ModernThinClientResult[UpdateP2PKeysReply]')):
        return self.__wrap_thin_client_call(self._base_client.UpdateP2PKeys)(rpc_controller, request, done)

    
    def Stop(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.Stop)(rpc_controller, request, done)

    
    def Pause(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.Pause)(rpc_controller, request, done)

    
    def Unpause(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.Unpause)(rpc_controller, request, done)

    
    def PrepareForFPMigration(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[PrepareForFPMigrationReply], None]]', 'return', 'ModernThinClientResult[PrepareForFPMigrationReply]')):
        return self.__wrap_thin_client_call(self._base_client.PrepareForFPMigration)(rpc_controller, request, done)

    
    def NotifyShadowDomainCreated(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'NotifyShadowDomainCreatedReq', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.NotifyShadowDomainCreated)(rpc_controller, request, done)

    
    def NotifyShadowDomainDeleted(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.NotifyShadowDomainDeleted)(rpc_controller, request, done)

    
    def StartFPCutover(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'StartFPCutoverReq', 'done', 'Optional[Callable[[StartFPCutoverReply], None]]', 'return', 'ModernThinClientResult[StartFPCutoverReply]')):
        return self.__wrap_thin_client_call(self._base_client.StartFPCutover)(rpc_controller, request, done)

    
    def StartFPCutoverDryRun(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'StartFPCutoverDryRunReq', 'done', 'Optional[Callable[[StartFPCutoverDryRunReply], None]]', 'return', 'ModernThinClientResult[StartFPCutoverDryRunReply]')):
        return self.__wrap_thin_client_call(self._base_client.StartFPCutoverDryRun)(rpc_controller, request, done)

    
    def FPCutoverGoNoGo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'FPCutoverGoNoGoReq', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.FPCutoverGoNoGo)(rpc_controller, request, done)

    
    def CheckFPEligibility(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[CheckFPEligibilityReply], None]]', 'return', 'ModernThinClientResult[CheckFPEligibilityReply]')):
        return self.__wrap_thin_client_call(self._base_client.CheckFPEligibility)(rpc_controller, request, done)

    
    def EstimateFPMigrationDuration(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[EstimateFPMigrationDurationReply], None]]', 'return', 'ModernThinClientResult[EstimateFPMigrationDurationReply]')):
        return self.__wrap_thin_client_call(self._base_client.EstimateFPMigrationDuration)(rpc_controller, request, done)

    
    def GetAccount(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[GetAccountReply], None]]', 'return', 'ModernThinClientResult[GetAccountReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetAccount)(rpc_controller, request, done)

    
    def UpdateHiddenState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UpdateHiddenStateReq', 'done', 'Optional[Callable[[UpdateHiddenStateReply], None]]', 'return', 'ModernThinClientResult[UpdateHiddenStateReply]')):
        return self.__wrap_thin_client_call(self._base_client.UpdateHiddenState)(rpc_controller, request, done)

    
    def GetHiddenState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[GetHiddenStateReply], None]]', 'return', 'ModernThinClientResult[GetHiddenStateReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetHiddenState)(rpc_controller, request, done)

    
    def GetRemoteFeatureConfigs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[GetRemoteFeatureConfigsReply], None]]', 'return', 'ModernThinClientResult[GetRemoteFeatureConfigsReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetRemoteFeatureConfigs)(rpc_controller, request, done)

    
    def LookupByLocalPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupByLocalPathReq', 'done', 'Optional[Callable[[LookupByLocalPathReply], None]]', 'return', 'ModernThinClientResult[LookupByLocalPathReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupByLocalPath)(rpc_controller, request, done)

    
    def LookupFileIdByRRServerPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupFileIdByRRServerPathReq', 'done', 'Optional[Callable[[LookupFileIdReply], None]]', 'return', 'ModernThinClientResult[LookupFileIdReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupFileIdByRRServerPath)(rpc_controller, request, done)

    
    def LookupFileIdByMRServerPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupFileIdByMRServerPathReq', 'done', 'Optional[Callable[[LookupFileIdReply], None]]', 'return', 'ModernThinClientResult[LookupFileIdReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupFileIdByMRServerPath)(rpc_controller, request, done)

    
    def LookupLockStatusByFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupLockStatusByFileIdReq', 'done', 'Optional[Callable[[LookupLockStatusByFileIdReply], None]]', 'return', 'ModernThinClientResult[LookupLockStatusByFileIdReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupLockStatusByFileId)(rpc_controller, request, done)

    
    def ListDirLocal(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ListDirLocalReq', 'done', 'Optional[Callable[[ListDirLocalReply], None]]', 'return', 'ModernThinClientResult[ListDirLocalReply]')):
        return self.__wrap_thin_client_call(self._base_client.ListDirLocal)(rpc_controller, request, done)

    
    def BugReporterStats(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[BugReporterStatsReply], None]]', 'return', 'ModernThinClientResult[BugReporterStatsReply]')):
        return self.__wrap_thin_client_call(self._base_client.BugReporterStats)(rpc_controller, request, done)

    
    def RegisterCameraUploadsTag(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'RegisterCameraUploadsTagReq', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.RegisterCameraUploadsTag)(rpc_controller, request, done)

    
    def GetConflictedPathForRemoteApplication(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetConflictedPathReq', 'done', 'Optional[Callable[[GetConflictedPathReply], None]]', 'return', 'ModernThinClientResult[GetConflictedPathReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetConflictedPathForRemoteApplication)(rpc_controller, request, done)

    
    def RenameIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'RenameIntoDropboxRequest', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.RenameIntoDropbox)(rpc_controller, request, done)

    
    def CreateEphemeralTempDir(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[CreateEphemeralTempDirReply], None]]', 'return', 'ModernThinClientResult[CreateEphemeralTempDirReply]')):
        return self.__wrap_thin_client_call(self._base_client.CreateEphemeralTempDir)(rpc_controller, request, done)

    
    def LookupMountPointUnderFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupMountPointUnderFileIdReq', 'done', 'Optional[Callable[[LookupMountPointUnderFileIdReply], None]]', 'return', 'ModernThinClientResult[LookupMountPointUnderFileIdReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupMountPointUnderFileId)(rpc_controller, request, done)

    
    def LookupNamespaces(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[LookupNamespacesReply], None]]', 'return', 'ModernThinClientResult[LookupNamespacesReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupNamespaces)(rpc_controller, request, done)

    
    def UpdatePriorityHint(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UpdatePriorityHintReq', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.UpdatePriorityHint)(rpc_controller, request, done)

    
    def GetSyncQueueSnapshot(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetSyncQueueSnapshot)(rpc_controller, request, done)

    
    def GetAndSubscribeToSyncProgressForFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetAndSubscribeToSyncProgressForFileId)(rpc_controller, request, done)

    
    def UnsubscribeToSyncProgressForFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.UnsubscribeToSyncProgressForFileId)(rpc_controller, request, done)

    
    def GetMergeProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetMergeProgress)(rpc_controller, request, done)

    
    def GetSyncCompletedSummary(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetSyncCompletedSummary)(rpc_controller, request, done)

    
    def GetDiskUsage(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[DiskUsageReply], None]]', 'return', 'ModernThinClientResult[DiskUsageReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetDiskUsage)(rpc_controller, request, done)

    
    def GetFilesystemInfo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetFilesystemInfoReq', 'done', 'Optional[Callable[[GetFilesystemInfoReply], None]]', 'return', 'ModernThinClientResult[GetFilesystemInfoReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetFilesystemInfo)(rpc_controller, request, done)

    
    def PingSfe(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.PingSfe)(rpc_controller, request, done)

    
    def UpdateHydrationPolicy(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UpdateHydrationPolicyReq', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.UpdateHydrationPolicy)(rpc_controller, request, done)

    
    def UpdateInfiniteOperatingMode(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UpdateInfiniteOperatingModeReq', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.UpdateInfiniteOperatingMode)(rpc_controller, request, done)

    
    def ServerComponentToLocal(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ServerComponentToLocalReq', 'done', 'Optional[Callable[[ServerComponentToLocalReply], None]]', 'return', 'ModernThinClientResult[ServerComponentToLocalReply]')):
        return self.__wrap_thin_client_call(self._base_client.ServerComponentToLocal)(rpc_controller, request, done)

    
    def GetOSFolderPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetOSFolderPathReq', 'done', 'Optional[Callable[[GetOSFolderPathReply], None]]', 'return', 'ModernThinClientResult[GetOSFolderPathReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetOSFolderPath)(rpc_controller, request, done)

    
    def DenyUserAccess(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DenyUserAccessReq', 'done', 'Optional[Callable[[DenyUserAccessReply], None]]', 'return', 'ModernThinClientResult[DenyUserAccessReply]')):
        return self.__wrap_thin_client_call(self._base_client.DenyUserAccess)(rpc_controller, request, done)

    
    def AllowUserAccess(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'AllowUserAccessReq', 'done', 'Optional[Callable[[AllowUserAccessReply], None]]', 'return', 'ModernThinClientResult[AllowUserAccessReply]')):
        return self.__wrap_thin_client_call(self._base_client.AllowUserAccess)(rpc_controller, request, done)

    
    def MergeIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'MergeIntoDropboxReq', 'done', 'Optional[Callable[[MergeIntoDropboxReply], None]]', 'return', 'ModernThinClientResult[MergeIntoDropboxReply]')):
        return self.__wrap_thin_client_call(self._base_client.MergeIntoDropbox)(rpc_controller, request, done)

    
    def ContainerState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ContainerStateReq', 'done', 'Optional[Callable[[ContainerStateReply], None]]', 'return', 'ModernThinClientResult[ContainerStateReply]')):
        return self.__wrap_thin_client_call(self._base_client.ContainerState)(rpc_controller, request, done)

    
    def ListContainers(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[ListContainersReply], None]]', 'return', 'ModernThinClientResult[ListContainersReply]')):
        return self.__wrap_thin_client_call(self._base_client.ListContainers)(rpc_controller, request, done)

    
    def SetPathIgnoredState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'SetPathIgnoredStateReq', 'done', 'Optional[Callable[[SetPathIgnoredStateReply], None]]', 'return', 'ModernThinClientResult[SetPathIgnoredStateReply]')):
        return self.__wrap_thin_client_call(self._base_client.SetPathIgnoredState)(rpc_controller, request, done)

    
    def ListDirByFileType(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ListDirByFileTypeReq', 'done', 'Optional[Callable[[ListDirByFileTypeReply], None]]', 'return', 'ModernThinClientResult[ListDirByFileTypeReply]')):
        return self.__wrap_thin_client_call(self._base_client.ListDirByFileType)(rpc_controller, request, done)

    
    def RecordUpcomingFolderDelete(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'RecordUpcomingFolderDeleteReq', 'done', 'Optional[Callable[[RecordUpcomingFolderDeleteReply], None]]', 'return', 'ModernThinClientResult[RecordUpcomingFolderDeleteReply]')):
        return self.__wrap_thin_client_call(self._base_client.RecordUpcomingFolderDelete)(rpc_controller, request, done)

    
    def CheckConsistency(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.CheckConsistency)(rpc_controller, request, done)

    
    def CheckConsistencyDbxIgnore(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.CheckConsistencyDbxIgnore)(rpc_controller, request, done)

    
    def GetSyncOperationCompletedSummary(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetSyncOperationCompletedSummary)(rpc_controller, request, done)

    
    def GetBlockForPeer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetBlockForPeerReq', 'done', 'Optional[Callable[[GetBlockForPeerReply], None]]', 'return', 'ModernThinClientResult[GetBlockForPeerReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetBlockForPeer)(rpc_controller, request, done)

    
    def CheckBlockExistsForPeer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'CheckBlockExistsForPeerReq', 'done', 'Optional[Callable[[CheckBlockExistsForPeerReply], None]]', 'return', 'ModernThinClientResult[CheckBlockExistsForPeerReply]')):
        return self.__wrap_thin_client_call(self._base_client.CheckBlockExistsForPeer)(rpc_controller, request, done)

    
    def MaterializeContainer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'MaterializeContainerReq', 'done', 'Optional[Callable[[ContainerActionReply], None]]', 'return', 'ModernThinClientResult[ContainerActionReply]')):
        return self.__wrap_thin_client_call(self._base_client.MaterializeContainer)(rpc_controller, request, done)

    
    def DematerializeContainer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DematerializeContainerReq', 'done', 'Optional[Callable[[ContainerActionReply], None]]', 'return', 'ModernThinClientResult[ContainerActionReply]')):
        return self.__wrap_thin_client_call(self._base_client.DematerializeContainer)(rpc_controller, request, done)

    
    def BindIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'BindIntoDropboxReq', 'done', 'Optional[Callable[[BindIntoDropboxReply], None]]', 'return', 'ModernThinClientResult[BindIntoDropboxReply]')):
        return self.__wrap_thin_client_call(self._base_client.BindIntoDropbox)(rpc_controller, request, done)

    
    def UnbindFromDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UnbindFromDropboxReq', 'done', 'Optional[Callable[[UnbindFromDropboxReply], None]]', 'return', 'ModernThinClientResult[UnbindFromDropboxReply]')):
        return self.__wrap_thin_client_call(self._base_client.UnbindFromDropbox)(rpc_controller, request, done)

    
    def CreateBreadcrumbs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'CreateBreadcrumbsReq', 'done', 'Optional[Callable[[CreateBreadcrumbsReply], None]]', 'return', 'ModernThinClientResult[CreateBreadcrumbsReply]')):
        return self.__wrap_thin_client_call(self._base_client.CreateBreadcrumbs)(rpc_controller, request, done)

    
    def RemoveBreadcrumbs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'RemoveBreadcrumbsReq', 'done', 'Optional[Callable[[RemoveBreadcrumbsReply], None]]', 'return', 'ModernThinClientResult[RemoveBreadcrumbsReply]')):
        return self.__wrap_thin_client_call(self._base_client.RemoveBreadcrumbs)(rpc_controller, request, done)

    
    def EarlyRetrySync(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'RetrySyncRequest', 'done', 'Optional[Callable[[RetrySyncReply], None]]', 'return', 'ModernThinClientResult[RetrySyncReply]')):
        return self.__wrap_thin_client_call(self._base_client.EarlyRetrySync)(rpc_controller, request, done)

    
    def GetSyncFailuresSummary(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetSyncFailuresSummaryReq', 'done', 'Optional[Callable[[GetSyncFailuresSummaryReply], None]]', 'return', 'ModernThinClientResult[GetSyncFailuresSummaryReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetSyncFailuresSummary)(rpc_controller, request, done)

    
    def SendFileEvent(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'SendFileEventReq', 'done', 'Optional[Callable[[SendFileEventReply], None]]', 'return', 'ModernThinClientResult[SendFileEventReply]')):
        return self.__wrap_thin_client_call(self._base_client.SendFileEvent)(rpc_controller, request, done)

    
    def TriggerList(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.TriggerList)(rpc_controller, request, done)

    
    def ValidateAnchorTarget(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ValidateAnchorTargetReq', 'done', 'Optional[Callable[[ValidateAnchorTargetReply], None]]', 'return', 'ModernThinClientResult[ValidateAnchorTargetReply]')):
        return self.__wrap_thin_client_call(self._base_client.ValidateAnchorTarget)(rpc_controller, request, done)

    
    def CreateDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'CreateDeviceAnchorReq', 'done', 'Optional[Callable[[CreateDeviceAnchorReply], None]]', 'return', 'ModernThinClientResult[CreateDeviceAnchorReply]')):
        return self.__wrap_thin_client_call(self._base_client.CreateDeviceAnchor)(rpc_controller, request, done)

    
    def ResolveDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ResolveDeviceAnchorReq', 'done', 'Optional[Callable[[ResolveDeviceAnchorReply], None]]', 'return', 'ModernThinClientResult[ResolveDeviceAnchorReply]')):
        return self.__wrap_thin_client_call(self._base_client.ResolveDeviceAnchor)(rpc_controller, request, done)

    
    def ResumeDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ResumeDeviceAnchorReq', 'done', 'Optional[Callable[[ResumeDeviceAnchorReply], None]]', 'return', 'ModernThinClientResult[ResumeDeviceAnchorReply]')):
        return self.__wrap_thin_client_call(self._base_client.ResumeDeviceAnchor)(rpc_controller, request, done)

    
    def PauseDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'PauseDeviceAnchorReq', 'done', 'Optional[Callable[[PauseDeviceAnchorReply], None]]', 'return', 'ModernThinClientResult[PauseDeviceAnchorReply]')):
        return self.__wrap_thin_client_call(self._base_client.PauseDeviceAnchor)(rpc_controller, request, done)

    
    def DeleteDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DeleteDeviceAnchorReq', 'done', 'Optional[Callable[[DeleteDeviceAnchorReply], None]]', 'return', 'ModernThinClientResult[DeleteDeviceAnchorReply]')):
        return self.__wrap_thin_client_call(self._base_client.DeleteDeviceAnchor)(rpc_controller, request, done)

    
    def ListDeviceAnchors(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ListDeviceAnchorsReq', 'done', 'Optional[Callable[[ListDeviceAnchorsReply], None]]', 'return', 'ModernThinClientResult[ListDeviceAnchorsReply]')):
        return self.__wrap_thin_client_call(self._base_client.ListDeviceAnchors)(rpc_controller, request, done)

    
    def BreakBackupByTargetPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'BreakBackupByTargetPathReq', 'done', 'Optional[Callable[[BreakBackupByTargetPathReply], None]]', 'return', 'ModernThinClientResult[BreakBackupByTargetPathReply]')):
        return self.__wrap_thin_client_call(self._base_client.BreakBackupByTargetPath)(rpc_controller, request, done)

    
    def BreakBackupByFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'BreakBackupByFileIdReq', 'done', 'Optional[Callable[[BreakBackupByFileIdReply], None]]', 'return', 'ModernThinClientResult[BreakBackupByFileIdReply]')):
        return self.__wrap_thin_client_call(self._base_client.BreakBackupByFileId)(rpc_controller, request, done)

    
    def GetDbxIgnoreContents(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetDbxIgnoreContentsReq', 'done', 'Optional[Callable[[GetDbxIgnoreContentsReply], None]]', 'return', 'ModernThinClientResult[GetDbxIgnoreContentsReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetDbxIgnoreContents)(rpc_controller, request, done)

    
    def SetDbxIgnoreContents(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'SetDbxIgnoreContentsReq', 'done', 'Optional[Callable[[SetDbxIgnoreContentsReply], None]]', 'return', 'ModernThinClientResult[SetDbxIgnoreContentsReply]')):
        return self.__wrap_thin_client_call(self._base_client.SetDbxIgnoreContents)(rpc_controller, request, done)

    
    def InduceNucleusPanic(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.InduceNucleusPanic)(rpc_controller, request, done)

    
    def InduceNucleusOom(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.InduceNucleusOom)(rpc_controller, request, done)

    
    def Echo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'EchoMessage', 'done', 'Optional[Callable[[EchoMessage], None]]', 'return', 'ModernThinClientResult[EchoMessage]')):
        return self.__wrap_thin_client_call(self._base_client.Echo)(rpc_controller, request, done)

    
    def KeepAlive(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.KeepAlive)(rpc_controller, request, done)

    
    def EchoStream(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'EchoMessage', 'done', 'Optional[Callable[[EchoMessage], None]]', 'return', 'ModernThinClientResult[EchoMessage]')):
        return self.__wrap_thin_client_call(self._base_client.EchoStream)(rpc_controller, request, done)

    
    def InduceRemoteInconsistencies(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.InduceRemoteInconsistencies)(rpc_controller, request, done)

    
    def LookupPropsByLocalPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'LookupPropsByLocalPathReq', 'done', 'Optional[Callable[[LookupPropsByLocalPathReply], None]]', 'return', 'ModernThinClientResult[LookupPropsByLocalPathReply]')):
        return self.__wrap_thin_client_call(self._base_client.LookupPropsByLocalPath)(rpc_controller, request, done)

    
    def GetPublishedEvents(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetPublishedEventsReq', 'done', 'Optional[Callable[[PublishedEvent], None]]', 'return', 'ModernThinClientResult[PublishedEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetPublishedEvents)(rpc_controller, request, done)

    
    def GetHiddenSetChanged(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetHiddenSetChanged)(rpc_controller, request, done)

    
    def GetSyncOpFailedSummary(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetSyncOpFailedSummary)(rpc_controller, request, done)

    
    def GetRemoteMountPointsInfo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetRemoteMountPointsInfoReq', 'done', 'Optional[Callable[[GetRemoteMountPointsInfoReply], None]]', 'return', 'ModernThinClientResult[GetRemoteMountPointsInfoReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetRemoteMountPointsInfo)(rpc_controller, request, done)

    
    def DirtyPaths(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DirtyPathsReq', 'done', 'Optional[Callable[[DirtyPathsReply], None]]', 'return', 'ModernThinClientResult[DirtyPathsReply]')):
        return self.__wrap_thin_client_call(self._base_client.DirtyPaths)(rpc_controller, request, done)

    
    def SuppressFSWs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'SuppressFSWsReq', 'done', 'Optional[Callable[[SuppressFSWsReply], None]]', 'return', 'ModernThinClientResult[SuppressFSWsReply]')):
        return self.__wrap_thin_client_call(self._base_client.SuppressFSWs)(rpc_controller, request, done)

    
    def SubscribeForBackupSyncProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'SubscribeForBackupSyncProgressReq', 'done', 'Optional[Callable[[SubscribeForBackupSyncProgressReply], None]]', 'return', 'ModernThinClientResult[SubscribeForBackupSyncProgressReply]')):
        return self.__wrap_thin_client_call(self._base_client.SubscribeForBackupSyncProgress)(rpc_controller, request, done)

    
    def GetCurrentDeviceAnchorSyncProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetCurrentDeviceAnchorSyncProgressReq', 'done', 'Optional[Callable[[GetCurrentDeviceAnchorSyncProgressReply], None]]', 'return', 'ModernThinClientResult[GetCurrentDeviceAnchorSyncProgressReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetCurrentDeviceAnchorSyncProgress)(rpc_controller, request, done)

    
    def GetCurrentComputerBackupSyncProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetCurrentComputerBackupSyncProgressReq', 'done', 'Optional[Callable[[GetCurrentComputerBackupSyncProgressReply], None]]', 'return', 'ModernThinClientResult[GetCurrentComputerBackupSyncProgressReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetCurrentComputerBackupSyncProgress)(rpc_controller, request, done)

    
    def GetDeviceAnchorMetadataByPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetDeviceAnchorMetadataByPathReq', 'done', 'Optional[Callable[[GetDeviceAnchorMetadataByPathReply], None]]', 'return', 'ModernThinClientResult[GetDeviceAnchorMetadataByPathReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetDeviceAnchorMetadataByPath)(rpc_controller, request, done)

    
    def ReportFileProviderDump(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'FileProviderDumpReq', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.ReportFileProviderDump)(rpc_controller, request, done)

    
    def ReconnectNetwork(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.ReconnectNetwork)(rpc_controller, request, done)

    
    def ForceHardeningMigrationForAllPlaceholders(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.ForceHardeningMigrationForAllPlaceholders)(rpc_controller, request, done)

    
    def GetNetworkState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'ReactiveRequest', 'done', 'Optional[Callable[[ReactiveEvent], None]]', 'return', 'ModernThinClientResult[ReactiveEvent]')):
        return self.__wrap_thin_client_call(self._base_client.GetNetworkState)(rpc_controller, request, done)

    
    def GetActiveEngineWaits(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[GetActiveEngineWaitsReply], None]]', 'return', 'ModernThinClientResult[GetActiveEngineWaitsReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetActiveEngineWaits)(rpc_controller, request, done)

    
    def GetDebugInfo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[GetDebugInfoReply], None]]', 'return', 'ModernThinClientResult[GetDebugInfoReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetDebugInfo)(rpc_controller, request, done)

    
    def UnpackFPPackage(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'UnpackFPPackageReq', 'done', 'Optional[Callable[[UnpackFPPackageReply], None]]', 'return', 'ModernThinClientResult[UnpackFPPackageReply]')):
        return self.__wrap_thin_client_call(self._base_client.UnpackFPPackage)(rpc_controller, request, done)

    
    def SetCustomizableContextMenuPreferences(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'FPContextMenuPreferences', 'done', 'Optional[Callable[[Empty], None]]', 'return', 'ModernThinClientResult[Empty]')):
        return self.__wrap_thin_client_call(self._base_client.SetCustomizableContextMenuPreferences)(rpc_controller, request, done)

    
    def FetchUnsyncableFileIds(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'Empty', 'done', 'Optional[Callable[[FetchUnsyncableFileIdsResponse], None]]', 'return', 'ModernThinClientResult[FetchUnsyncableFileIdsResponse]')):
        return self.__wrap_thin_client_call(self._base_client.FetchUnsyncableFileIds)(rpc_controller, request, done)

    
    def DeleteRemoteSyncedIgnoredFile(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DeleteRemoteSyncedIgnoredFileReq', 'done', 'Optional[Callable[[DeleteRemoteSyncedIgnoredFileReply], None]]', 'return', 'ModernThinClientResult[DeleteRemoteSyncedIgnoredFileReply]')):
        return self.__wrap_thin_client_call(self._base_client.DeleteRemoteSyncedIgnoredFile)(rpc_controller, request, done)

    
    def GetRemoteSyncedIgnoredFiles(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'GetRemoteSyncedIgnoredFilesReq', 'done', 'Optional[Callable[[GetRemoteSyncedIgnoredFilesReply], None]]', 'return', 'ModernThinClientResult[GetRemoteSyncedIgnoredFilesReply]')):
        return self.__wrap_thin_client_call(self._base_client.GetRemoteSyncedIgnoredFiles)(rpc_controller, request, done)

    
    def DeleteRemoteSyncedIgnoredDirectoryFiles(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'DeleteRemoteSyncedIgnoredDirectoryFilesReq', 'done', 'Optional[Callable[[DeleteRemoteSyncedIgnoredDirectoryFilesReply], None]]', 'return', 'ModernThinClientResult[DeleteRemoteSyncedIgnoredDirectoryFilesReply]')):
        return self.__wrap_thin_client_call(self._base_client.DeleteRemoteSyncedIgnoredDirectoryFiles)(rpc_controller, request, done)


