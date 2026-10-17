# Source Generated with Decompyle++
# File: app_service_tprt_client.pyc (Python 3.11)

from concurrent.futures import futures
import typing
import tprt
from google.protobuf.service import RpcController
from dropbox.proto.bolt import bolt_pb2 as dropbox__dot__proto__dot__bolt__dot__bolt_pb2
from dropbox.proto.engine_wait_tracker import engine_waits_pb2 as dropbox__dot__proto__dot__engine_wait_tracker__dot__engine_waits_pb2
from dropbox.proto.namespace import namespace_entity_pb2 as dropbox__dot__proto__dot__namespace__dot__namespace_entity_pb2
from dropbox.proto.nucleus import app_service_pb2 as dropbox__dot__proto__dot__nucleus__dot__app_service_pb2
from dropbox.proto.nucleus import common_api_types_pb2 as dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2
from dropbox.proto.nucleus import device_anchor_pb2 as dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2
from dropbox.proto.nucleus import feature_configs_pb2 as dropbox__dot__proto__dot__nucleus__dot__feature_configs_pb2
from dropbox.proto.nucleus import file_event_pb2 as dropbox__dot__proto__dot__nucleus__dot__file_event_pb2
from dropbox.proto.nucleus import fsw_generated_pb2 as dropbox__dot__proto__dot__nucleus__dot__fsw_generated_pb2
from dropbox.proto.nucleus import fsw_pb2 as dropbox__dot__proto__dot__nucleus__dot__fsw_pb2
from dropbox.proto.nucleus import link_container_pb2 as dropbox__dot__proto__dot__nucleus__dot__link_container_pb2
from dropbox.proto.nucleus import published_event_pb2 as dropbox__dot__proto__dot__nucleus__dot__published_event_pb2
from dropbox.proto.nucleus import reactive_api_pb2 as dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2
from dropbox.proto.nucleus import sync_engine_pb2 as dropbox__dot__proto__dot__nucleus__dot__sync_engine_pb2
from dropbox.proto.nucleus import sync_engine_status_pb2 as dropbox__dot__proto__dot__nucleus__dot__sync_engine_status_pb2
from dropbox.proto.nucleus import sync_failures_pb2 as dropbox__dot__proto__dot__nucleus__dot__sync_failures_pb2
from dropbox.proto.nucleus import types_pb2 as dropbox__dot__proto__dot__nucleus__dot__types_pb2
from dropbox.proto.per_node_metadata import attributes_pb2 as dropbox__dot__proto__dot__per_node_metadata__dot__attributes_pb2
from dropbox.proto.per_node_metadata import link_node_pb2 as dropbox__dot__proto__dot__per_node_metadata__dot__link_node_pb2
from dropbox.proto.rust import extensions_pb2 as dropbox__dot__proto__dot__rust__dot__extensions_pb2
from dropbox.proto.sync import remote_ops_pb2 as dropbox__dot__proto__dot__sync__dot__remote_ops_pb2
from dropbox.proto.sync import xattr_pb2 as dropbox__dot__proto__dot__sync__dot__xattr_pb2
from google.protobuf import empty_pb2 as google__dot__protobuf__dot__empty_pb2

class NucleusAPIClient:
    
    def __init__(self = None, raw_client = None):
        self._raw_client = raw_client

    
    def LookupByFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupByFileIdReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupByFileIdReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupByFileIdReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupByFileIdBatch(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupByFileIdBatchReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupByFileIdBatchReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupByFileIdBatchReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupSyncIcon(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupSyncIconReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupSyncIconReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupSyncIconReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def HydratePlaceholder(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.HydratePlaceholderReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.HydratePlaceholderReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.HydratePlaceholderReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CancelRecall(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CancelRecallReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetSyncProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetSyncEngineStatus(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetSyncEngineStatusReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetSyncEngineStatusReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UpdateFeatureConfig(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateFeatureConfigRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateFeatureConfigReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateFeatureConfigReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UnmergeFromDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnmergeFromDropboxReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnmergeFromDropboxReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnmergeFromDropboxReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupPropsByLocalPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupPropsByLocalPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupPropsByLocalPathReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupPropsByLocalPathReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SuppressFSWs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SuppressFSWsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SuppressFSWsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SuppressFSWsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetSyncFailuresSummary(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__sync_failures_pb2.GetSyncFailuresSummaryReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__sync_failures_pb2.GetSyncFailuresSummaryReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__sync_failures_pb2.GetSyncFailuresSummaryReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ReportFileProviderDump(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.FileProviderDumpReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ForceHardeningMigrationForAllPlaceholders(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetDebugInfo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetDebugInfoReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetDebugInfoReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SetCustomizableContextMenuPreferences(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__sync_engine_pb2.FPContextMenuPreferences', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def DeleteRemoteSyncedIgnoredFile(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.DeleteRemoteSyncedIgnoredFileReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.DeleteRemoteSyncedIgnoredFileReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.DeleteRemoteSyncedIgnoredFileReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetRemoteSyncedIgnoredFiles(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetRemoteSyncedIgnoredFilesReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetRemoteSyncedIgnoredFilesReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetRemoteSyncedIgnoredFilesReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def DeleteRemoteSyncedIgnoredDirectoryFiles(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.DeleteRemoteSyncedIgnoredDirectoryFilesReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.DeleteRemoteSyncedIgnoredDirectoryFilesReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.DeleteRemoteSyncedIgnoredDirectoryFilesReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def FetchByteRange(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.FetchByteRangeReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.FetchByteRangeReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.FetchByteRangeReply]')):
        pass
    # WARNING: Decompyle incomplete



class NucleusPhaseAgnosticAPIClient:
    
    def __init__(self = None, raw_client = None):
        self._raw_client = raw_client

    
    def UpdateConfig(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateConfigReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateConfigReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateConfigReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UpdateP2PKeys(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateP2PKeysReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateP2PKeysReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateP2PKeysReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def Stop(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def Pause(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def Unpause(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def PrepareForFPMigration(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.PrepareForFPMigrationReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.PrepareForFPMigrationReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def NotifyShadowDomainCreated(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.NotifyShadowDomainCreatedReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def NotifyShadowDomainDeleted(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def StartFPCutover(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.StartFPCutoverReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.StartFPCutoverReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.StartFPCutoverReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def StartFPCutoverDryRun(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.StartFPCutoverDryRunReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.StartFPCutoverDryRunReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.StartFPCutoverDryRunReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def FPCutoverGoNoGo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.FPCutoverGoNoGoReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CheckFPEligibility(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CheckFPEligibilityReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CheckFPEligibilityReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def EstimateFPMigrationDuration(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EstimateFPMigrationDurationReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EstimateFPMigrationDurationReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetAccount(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetAccountReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetAccountReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UpdateHiddenState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.UpdateHiddenStateReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.UpdateHiddenStateReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.UpdateHiddenStateReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetHiddenState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetHiddenStateReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetHiddenStateReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetRemoteFeatureConfigs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetRemoteFeatureConfigsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetRemoteFeatureConfigsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupByLocalPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupByLocalPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupByLocalPathReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.LookupByLocalPathReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetHomeFolderPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetHomeFolderPathReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetHomeFolderPathReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupFileIdByRRServerPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupFileIdByRRServerPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupFileIdReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupFileIdReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupFileIdByMRServerPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupFileIdByMRServerPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupFileIdReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupFileIdReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupLockStatusByFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupLockStatusByFileIdReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupLockStatusByFileIdReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupLockStatusByFileIdReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ListDirLocal(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ListDirLocalReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ListDirLocalReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ListDirLocalReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def BugReporterStats(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.BugReporterStatsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.BugReporterStatsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def RegisterCameraUploadsTag(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RegisterCameraUploadsTagReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetConflictedPathForRemoteApplication(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetConflictedPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetConflictedPathReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetConflictedPathReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def RenameIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RenameIntoDropboxRequest', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CreateEphemeralTempDir(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateEphemeralTempDirReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateEphemeralTempDirReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetRemoteMountPointsInfo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetRemoteMountPointsInfoReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetRemoteMountPointsInfoReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.GetRemoteMountPointsInfoReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupMountPointUnderFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupMountPointUnderFileIdReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupMountPointUnderFileIdReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupMountPointUnderFileIdReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupNamespaces(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupNamespacesReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupNamespacesReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UpdatePriorityHint(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.UpdatePriorityHintReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetSyncQueueSnapshot(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetAndSubscribeToSyncProgressForFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UnsubscribeToSyncProgressForFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetMergeProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetSyncCompletedSummary(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetHiddenSetChanged(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetSyncOpFailedSummary(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetDiskUsage(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DiskUsageReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DiskUsageReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetFilesystemInfo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetFilesystemInfoReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetFilesystemInfoReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetFilesystemInfoReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def PingSfe(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UpdateHydrationPolicy(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__common_api_types_pb2.UpdateHydrationPolicyReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UpdateInfiniteOperatingMode(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UpdateInfiniteOperatingModeReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ServerComponentToLocal(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ServerComponentToLocalReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ServerComponentToLocalReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ServerComponentToLocalReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetOSFolderPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetOSFolderPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetOSFolderPathReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetOSFolderPathReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def DenyUserAccess(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DenyUserAccessReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DenyUserAccessReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DenyUserAccessReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def AllowUserAccess(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AllowUserAccessReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AllowUserAccessReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AllowUserAccessReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def MergeIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.MergeIntoDropboxReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.MergeIntoDropboxReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.MergeIntoDropboxReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ContainerState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ContainerStateReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ContainerStateReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ContainerStateReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ListContainers(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ListContainersReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ListContainersReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SetPathIgnoredState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SetPathIgnoredStateReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SetPathIgnoredStateReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SetPathIgnoredStateReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ListDirByFileType(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ListDirByFileTypeReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ListDirByFileTypeReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ListDirByFileTypeReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def RecordUpcomingFolderDelete(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RecordUpcomingFolderDeleteReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RecordUpcomingFolderDeleteReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RecordUpcomingFolderDeleteReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CheckConsistency(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CheckConsistencyDbxIgnore(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetSyncOperationCompletedSummary(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetBlockForPeer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetBlockForPeerReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetBlockForPeerReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetBlockForPeerReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CheckBlockExistsForPeer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CheckBlockExistsForPeerReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CheckBlockExistsForPeerReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CheckBlockExistsForPeerReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def MaterializeContainer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.MaterializeContainerReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ContainerActionReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ContainerActionReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def DematerializeContainer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DematerializeContainerReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ContainerActionReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ContainerActionReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def BindIntoDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.BindIntoDropboxReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.BindIntoDropboxReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.BindIntoDropboxReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UnbindFromDropbox(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnbindFromDropboxReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnbindFromDropboxReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnbindFromDropboxReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CreateBreadcrumbs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateBreadcrumbsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateBreadcrumbsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateBreadcrumbsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def RemoveBreadcrumbs(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RemoveBreadcrumbsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RemoveBreadcrumbsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RemoveBreadcrumbsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def EarlyRetrySync(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RetrySyncRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RetrySyncReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.RetrySyncReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SendFileEvent(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SendFileEventReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SendFileEventReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SendFileEventReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def TriggerList(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ValidateAnchorTarget(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ValidateAnchorTargetReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ValidateAnchorTargetReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ValidateAnchorTargetReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CreateDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.CreateDeviceAnchorReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.CreateDeviceAnchorReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.CreateDeviceAnchorReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ResolveDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ResolveDeviceAnchorReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ResolveDeviceAnchorReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ResolveDeviceAnchorReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def BreakBackupByTargetPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.BreakBackupByTargetPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.BreakBackupByTargetPathReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.BreakBackupByTargetPathReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def BreakBackupByFileId(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.BreakBackupByFileIdReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.BreakBackupByFileIdReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.BreakBackupByFileIdReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ResumeDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ResumeDeviceAnchorReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ResumeDeviceAnchorReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ResumeDeviceAnchorReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def PauseDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.PauseDeviceAnchorReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.PauseDeviceAnchorReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.PauseDeviceAnchorReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def DeleteDeviceAnchor(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.DeleteDeviceAnchorReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.DeleteDeviceAnchorReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.DeleteDeviceAnchorReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ListDeviceAnchors(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ListDeviceAnchorsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ListDeviceAnchorsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.ListDeviceAnchorsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetDbxIgnoreContents(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.GetDbxIgnoreContentsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.GetDbxIgnoreContentsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.GetDbxIgnoreContentsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SetDbxIgnoreContents(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.SetDbxIgnoreContentsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.SetDbxIgnoreContentsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.SetDbxIgnoreContentsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetDeviceAnchorMetadataByPath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.GetDeviceAnchorMetadataByPathReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.GetDeviceAnchorMetadataByPathReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__device_anchor_pb2.GetDeviceAnchorMetadataByPathReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetPublishedEvents(self = None, rpc_controller = None, request = None, done_unused = (None,)):
        req_buf = request.SerializeToString()
        tprt_queue = self._raw_client.streaming('/nucleus.NucleusPhaseAgnosticAPI/GetPublishedEvents', req_buf)
        return StreamingQueue(tprt_queue, dropbox__dot__proto__dot__nucleus__dot__published_event_pb2.PublishedEvent)

    
    def DirtyPaths(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DirtyPathsReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DirtyPathsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.DirtyPathsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ReconnectNetwork(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SubscribeForBackupSyncProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SubscribeForBackupSyncProgressReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SubscribeForBackupSyncProgressReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SubscribeForBackupSyncProgressReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetCurrentDeviceAnchorSyncProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetCurrentDeviceAnchorSyncProgressReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetCurrentDeviceAnchorSyncProgressReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetCurrentDeviceAnchorSyncProgressReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetCurrentComputerBackupSyncProgress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetCurrentComputerBackupSyncProgressReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetCurrentComputerBackupSyncProgressReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetCurrentComputerBackupSyncProgressReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetNetworkState(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveRequest', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__reactive_api_pb2.ReactiveEvent]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetActiveEngineWaits(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__engine_wait_tracker__dot__engine_waits_pb2.GetActiveEngineWaitsReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__engine_wait_tracker__dot__engine_waits_pb2.GetActiveEngineWaitsReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UnpackFPPackage(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnpackFPPackageReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnpackFPPackageReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.UnpackFPPackageReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def InduceNucleusPanic(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def InduceNucleusOom(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def Echo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EchoMessage', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EchoMessage], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EchoMessage]')):
        pass
    # WARNING: Decompyle incomplete

    
    def EchoStream(self = None, rpc_controller = None, request = None, done_unused = (None,)):
        req_buf = request.SerializeToString()
        tprt_queue = self._raw_client.streaming('/nucleus.NucleusPhaseAgnosticAPI/EchoStream', req_buf)
        return StreamingQueue(tprt_queue, dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EchoMessage)

    
    def KeepAlive(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def InduceRemoteInconsistencies(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def FetchUnsyncableFileIds(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.FetchUnsyncableFileIdsResponse], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.FetchUnsyncableFileIdsResponse]')):
        pass
    # WARNING: Decompyle incomplete

    
    def EnumerateRemoteDir(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EnumerateRemoteDirReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EnumerateRemoteDirReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EnumerateRemoteDirReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def LookupRemoteEntry(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupRemoteEntryReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupRemoteEntryReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.LookupRemoteEntryReply]')):
        pass
    # WARNING: Decompyle incomplete



class ReverseNucleusAPIClient:
    
    def __init__(self = None, raw_client = None):
        self._raw_client = raw_client

    
    def Echo(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EchoMessage', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EchoMessage], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.EchoMessage]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SubscribeToBolt(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__bolt__dot__bolt_pb2.SubscribeToBoltReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__bolt__dot__bolt_pb2.SubscribeToBoltReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__bolt__dot__bolt_pb2.SubscribeToBoltReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def PublishEvent(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__published_event_pb2.PublishedEvent', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ShowFSWDialog(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__fsw_generated_pb2.ShowFSWDialogReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__fsw_pb2.FSWDialogDecision], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__fsw_pb2.FSWDialogDecision]')):
        pass
    # WARNING: Decompyle incomplete

    
    def IsFswRuleSuppressed(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.IsFswRuleSuppressedReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.IsFswRuleSuppressedReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.IsFswRuleSuppressedReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def FswRuleSuppress(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.FswRuleSuppressReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def IsAnyPathMonitoredByAnySyncEngine(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AnyPathMonitoredReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AnyPathMonitoredReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.AnyPathMonitoredReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def GetBlockFromPeer(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetBlockFromPeerReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetBlockFromPeerReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.GetBlockFromPeerReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def RequestWholeDropboxPermissionsFix(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete



class DebugEngineNetworkClient:
    
    def __init__(self = None, raw_client = None):
        self._raw_client = raw_client

    
    def CreateDirectory(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateDirReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateResp], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateResp]')):
        pass
    # WARNING: Decompyle incomplete

    
    def CreateFile(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateFileReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateResp], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.CreateResp]')):
        pass
    # WARNING: Decompyle incomplete

    
    def PurgePath(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.PurgePathReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def ConvertToMount(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ConvertToMountReq', 'done', 'typing.Optional[typing.Callable[[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ConvertToMountReply], None]]', 'return', 'futures.Future[dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.ConvertToMountReply]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SetMountReadOnly(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SetMountReadOnlyReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SetNamespaceProperties(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SetNamespacePropertiesReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def FreezeNetwork(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def UnfreezeNetwork(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'google__dot__protobuf__dot__empty_pb2.Empty', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
        pass
    # WARNING: Decompyle incomplete

    
    def SetDeviceFolder(self = None, rpc_controller = None, request = None, done = ('rpc_controller', 'RpcController', 'request', 'dropbox__dot__proto__dot__nucleus__dot__app_service_pb2.SetDeviceFolderReq', 'done', 'typing.Optional[typing.Callable[[google__dot__protobuf__dot__empty_pb2.Empty], None]]', 'return', 'futures.Future[google__dot__protobuf__dot__empty_pb2.Empty]')):
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


