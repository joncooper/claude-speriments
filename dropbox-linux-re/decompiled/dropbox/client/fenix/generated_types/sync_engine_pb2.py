# Source Generated with Decompyle++
# File: sync_engine_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'sync_engine.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dropbox.proto.nucleus import common_api_types_pb2 as dropbox_dot_proto_dot_nucleus_dot_common__api__types__pb2
from dropbox.proto.nucleus import reactive_api_pb2 as dropbox_dot_proto_dot_nucleus_dot_reactive__api__pb2
from dropbox.proto.nucleus import sync_engine_status_pb2 as dropbox_dot_proto_dot_nucleus_dot_sync__engine__status__pb2
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
from  import shared_pb2 as shared__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11sync_engine.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto\x1a,dropbox/proto/nucleus/common_api_types.proto\x1a(dropbox/proto/nucleus/reactive_api.proto\x1a.dropbox/proto/nucleus/sync_engine_status.proto\x1a!dropbox/proto/nucleus/types.proto\x1a\x0cshared.proto"&\n\x14PauseSyncEngineReply\x12\x0e\n\x06result\x18\x01 \x01(\x08";\n\x13ResumeSyncEngineReq\x12$\n\x1cuse_retray_snooze_sync_timer\x18\x01 \x01(\x08"\'\n\x15ResumeSyncEngineReply\x12\x0e\n\x06result\x18\x01 \x01(\x08"+\n\x07TPRTReq\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t"=\n\tTPRTReply\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t")\n\x17UpdatePriorityHintReply\x12\x0e\n\x06result\x18\x01 \x01(\x08"r\n\x1aPathLocationPropertiesPair\x12\x15\n\rabsolute_path\x18\x01 \x01(\t\x12=\n\x14lookup_by_path_reply\x18\x02 \x01(\x0b2\x1f.nucleus.LookupByLocalPathReply"3\n\x19LookupByLocalPathBatchReq\x12\x16\n\x0eabsolute_paths\x18\x01 \x03(\t"k\n\x1bLookupByLocalPathBatchReply\x12L\n\x13location_prop_pairs\x18\x01 \x03(\x0b2/.dropbox.meta_engine.PathLocationPropertiesPair":\n&LookupRemotePropertiesByFileIdBatchReq\x12\x10\n\x08file_ids\x18\x01 \x03(\t"\x83\x01\n\x1aFileIdRemotePropertiesPair\x12 \n\x07file_id\x18\x01 \x01(\x0b2\x0f.nucleus.FileId\x12C\n\x18remote_location_property\x18\x02 \x01(\x0b2!.nucleus.RemoteLocationProperties"\x7f\n(LookupRemotePropertiesByFileIdBatchReply\x12S\n\x1aremote_location_properties\x18\x01 \x03(\x0b2/.dropbox.meta_engine.FileIdRemotePropertiesPair"S\n\x13GetHiddenStateReply\x12<\n\x0ffile_id_to_path\x18\x01 \x03(\x0b2#.dropbox.meta_engine.FileIdPathPair"(\n\x16UpdateHiddenStateReply\x12\x0e\n\x06result\x18\x01 \x01(\x08"\xfc\x02\n\x11GetSyncPhaseReply\x12*\n\x08starting\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12*\n\x08indexing\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12/\n\rreassociating\x18\x03 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12(\n\x06paused\x18\x04 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12)\n\x07syncing\x18\x05 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12(\n\x06synced\x18\x06 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12+\n\tmigrating\x18\x07 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12)\n\x07listing\x18\t \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x07\n\x05phase2\xcc\x0f\n\rSyncEngineApi\x12H\n\x13GetSyncEngineStatus\x12\x16.google.protobuf.Empty\x1a\x19.nucleus.SyncEngineStatus\x12H\n\x12GetPublishedEvents\x12\x18.nucleus.ReactiveRequest\x1a\x16.nucleus.ReactiveEvent0\x01\x12T\n\x0fPauseSyncEngine\x12\x16.google.protobuf.Empty\x1a).dropbox.meta_engine.PauseSyncEngineReply\x12h\n\x10ResumeSyncEngine\x12(.dropbox.meta_engine.ResumeSyncEngineReq\x1a*.dropbox.meta_engine.ResumeSyncEngineReply\x12d\n\x14GetRemoteMountPoints\x12$.nucleus.GetRemoteMountPointsInfoReq\x1a&.nucleus.GetRemoteMountPointsInfoReply\x12d\n\x12UpdatePriorityHint\x12\x1e.nucleus.UpdatePriorityHintReq\x1a,.dropbox.meta_engine.UpdatePriorityHintReply"\x00\x12S\n\x11LookupByLocalPath\x12\x1d.nucleus.LookupByLocalPathReq\x1a\x1f.nucleus.LookupByLocalPathReply\x12z\n\x16LookupByLocalPathBatch\x12..dropbox.meta_engine.LookupByLocalPathBatchReq\x1a0.dropbox.meta_engine.LookupByLocalPathBatchReply\x12]\n\x1dLookupLocalPropertiesByFileId\x12\x1a.nucleus.LookupByFileIdReq\x1a .nucleus.LocalLocationProperties\x12_\n\x1eLookupRemotePropertiesByFileId\x12\x1a.nucleus.LookupByFileIdReq\x1a!.nucleus.RemoteLocationProperties\x12L\n\x11GetHomeFolderPath\x12\x16.google.protobuf.Empty\x1a\x1f.nucleus.GetHomeFolderPathReply\x12\xa1\x01\n#LookupRemotePropertiesByFileIdBatch\x12;.dropbox.meta_engine.LookupRemotePropertiesByFileIdBatchReq\x1a=.dropbox.meta_engine.LookupRemotePropertiesByFileIdBatchReply\x12T\n\x15UpdateHydrationPolicy\x12!.nucleus.UpdateHydrationPolicyReq\x1a\x16.google.protobuf.Empty"\x00\x12L\n\x11UpdateHiddenState\x12\x1d.nucleus.UpdateHiddenStateReq\x1a\x16.google.protobuf.Empty"\x00\x12T\n\x0eGetHiddenState\x12\x16.google.protobuf.Empty\x1a(.dropbox.meta_engine.GetHiddenStateReply"\x00\x12J\n\x0eLookupSyncIcon\x12\x1a.nucleus.LookupSyncIconReq\x1a\x1c.nucleus.LookupSyncIconReply\x12N\n\x0cGetSyncPhase\x12\x16.google.protobuf.Empty\x1a&.dropbox.meta_engine.GetSyncPhaseReply\x12w\n\x1dDeleteRemoteSyncedIgnoredFile\x12).nucleus.DeleteRemoteSyncedIgnoredFileReq\x1a+.nucleus.DeleteRemoteSyncedIgnoredFileReply\x12q\n\x1bGetRemoteSyncedIgnoredFiles\x12\'.nucleus.GetRemoteSyncedIgnoredFilesReq\x1a).nucleus.GetRemoteSyncedIgnoredFilesReply\x12\x95\x01\n\'DeleteRemoteSyncedIgnoredDirectoryFiles\x123.nucleus.DeleteRemoteSyncedIgnoredDirectoryFilesReq\x1a5.nucleus.DeleteRemoteSyncedIgnoredDirectoryFilesReply2^\n\x0cFSSEngineApi\x12N\n\x0eTPRTExampleAPI\x12\x1c.dropbox.meta_engine.TPRTReq\x1a\x1e.dropbox.meta_engine.TPRTReplyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sync_engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_PAUSESYNCENGINEREPLY']._serialized_start = 256
    _globals['_PAUSESYNCENGINEREPLY']._serialized_end = 294
    _globals['_RESUMESYNCENGINEREQ']._serialized_start = 296
    _globals['_RESUMESYNCENGINEREQ']._serialized_end = 355
    _globals['_RESUMESYNCENGINEREPLY']._serialized_start = 357
    _globals['_RESUMESYNCENGINEREPLY']._serialized_end = 396
    _globals['_TPRTREQ']._serialized_start = 398
    _globals['_TPRTREQ']._serialized_end = 441
    _globals['_TPRTREPLY']._serialized_start = 443
    _globals['_TPRTREPLY']._serialized_end = 504
    _globals['_UPDATEPRIORITYHINTREPLY']._serialized_start = 506
    _globals['_UPDATEPRIORITYHINTREPLY']._serialized_end = 547
    _globals['_PATHLOCATIONPROPERTIESPAIR']._serialized_start = 549
    _globals['_PATHLOCATIONPROPERTIESPAIR']._serialized_end = 663
    _globals['_LOOKUPBYLOCALPATHBATCHREQ']._serialized_start = 665
    _globals['_LOOKUPBYLOCALPATHBATCHREQ']._serialized_end = 716
    _globals['_LOOKUPBYLOCALPATHBATCHREPLY']._serialized_start = 718
    _globals['_LOOKUPBYLOCALPATHBATCHREPLY']._serialized_end = 825
    _globals['_LOOKUPREMOTEPROPERTIESBYFILEIDBATCHREQ']._serialized_start = 827
    _globals['_LOOKUPREMOTEPROPERTIESBYFILEIDBATCHREQ']._serialized_end = 885
    _globals['_FILEIDREMOTEPROPERTIESPAIR']._serialized_start = 888
    _globals['_FILEIDREMOTEPROPERTIESPAIR']._serialized_end = 1019
    _globals['_LOOKUPREMOTEPROPERTIESBYFILEIDBATCHREPLY']._serialized_start = 1021
    _globals['_LOOKUPREMOTEPROPERTIESBYFILEIDBATCHREPLY']._serialized_end = 1148
    _globals['_GETHIDDENSTATEREPLY']._serialized_start = 1150
    _globals['_GETHIDDENSTATEREPLY']._serialized_end = 1233
    _globals['_UPDATEHIDDENSTATEREPLY']._serialized_start = 1235
    _globals['_UPDATEHIDDENSTATEREPLY']._serialized_end = 1275
    _globals['_GETSYNCPHASEREPLY']._serialized_start = 1278
    _globals['_GETSYNCPHASEREPLY']._serialized_end = 1658
    _globals['_SYNCENGINEAPI']._serialized_start = 1661
    _globals['_SYNCENGINEAPI']._serialized_end = 3657
    _globals['_FSSENGINEAPI']._serialized_start = 3659
    _globals['_FSSENGINEAPI']._serialized_end = 3753
    return None
