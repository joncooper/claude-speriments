# Source Generated with Decompyle++
# File: published_event_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/published_event.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.nucleus import reactive_api_pb2 as dropbox_dot_proto_dot_nucleus_dot_reactive__api__pb2
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
from dropbox.proto.nucleus import device_anchor_pb2 as dropbox_dot_proto_dot_nucleus_dot_device__anchor__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync import remote_ops_pb2 as dropbox_dot_proto_dot_sync_dot_remote__ops__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dropbox/proto/nucleus/published_event.proto\x12\x07nucleus\x1a(dropbox/proto/nucleus/reactive_api.proto\x1a!dropbox/proto/nucleus/types.proto\x1a)dropbox/proto/nucleus/device_anchor.proto\x1a#dropbox/proto/rust/extensions.proto\x1a#dropbox/proto/sync/remote_ops.proto\x1a\x1bgoogle/protobuf/empty.proto"\xc6\r\n\x0ePublishedEvent\x12*\n\x08reactive\x18\x11 \x01(\x0b2\x16.nucleus.ReactiveEventH\x00\x121\n\x0cfile_changed\x18\x02 \x01(\x0b2\x19.nucleus.FileChangedEventH\x00\x12Z\n migration_from_classic_completed\x18\t \x01(\x0e2..nucleus.PublishedEvent.MigrationCompletedInfoH\x00\x121\n\x0frequest_restart\x18\x0e \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12.\n\rmount_changed\x18\x13 \x01(\x0b2\x15.nucleus.MountChangedH\x00\x126\n\x12office_move_to_dfc\x18\x15 \x01(\x0b2\x18.nucleus.OfficeMoveToDFCH\x00\x12N\n\x1bconflict_resolution_attempt\x18\x16 \x01(\x0b2\'.nucleus.ConflictResolutionAttemptEventH\x00\x12M\n+cdm_relocation_ack_commits_patch_trees_done\x18\x19 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12C\n\x18infinite_recall_progress\x18\x1a \x01(\x0b2\x1f.nucleus.InfiniteRecallProgressH\x00\x12?\n\x16applied_hidden_default\x18\x1b \x01(\x0b2\x1d.nucleus.AppliedHiddenDefaultH\x00\x12N\n\x1edelete_suppressed_dir_restored\x18\x1c \x01(\x0b2$.nucleus.DeleteSuppressRestoredEventH\x00\x12N\n\x1ecdm_relocation_request_restart\x18\x1d \x01(\x0b2$.nucleus.CDMRelocationRequestRestartH\x00\x12J\n\x1clink_container_changed_event\x18\x1e \x01(\x0b2".nucleus.LinkContainerChangedEventH\x00\x12F\n\x1adevice_anchor_unbind_event\x18\x1f \x01(\x0b2 .nucleus.DeviceAnchorUnbindEventH\x00\x12G\n\x18one_way_sync_remediation\x18" \x01(\x0b2#.nucleus.OneWaySyncRemediationEventH\x00\x12O\n\x1cfile_provider_dump_requested\x18# \x01(\x0b2\'.nucleus.FileProviderDumpRequestedEventH\x00\x125\n\x0esilly_labrador\x18$ \x01(\x0b2\x1b.nucleus.SillyLabradorEventH\x00\x12?\n\x1dfile_provider_permissions_fix\x18% \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12?\n\x16encryption_error_event\x18& \x01(\x0b2\x1d.nucleus.EncryptionErrorEventH\x00\x12>\n\x13client_key_enrolled\x18\' \x01(\x0b2\x1f.nucleus.ClientKeyEnrolledEventH\x00\x12<\n\x1await_for_client_enrollment\x18( \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12G\n\x18new_team_key_fingerprint\x18) \x01(\x0b2#.nucleus.NewTeamKeyFingerprintEventH\x00\x12H\n\x1bfp_shadow_cutover_completed\x18* \x01(\x0b2!.nucleus.FPShadowCutoverCompletedH\x00\x12&\n\x1eevent_created_timestamp_micros\x18  \x01(\x04\x12*\n"sent_from_nucleus_timestamp_micros\x18! \x01(\x04"2\n\x16MigrationCompletedInfo\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07TIMEOUT\x10\x01B\r\n\x05event\x12\x04\x88\xb5\x18\x00J\x04\x08\n\x10\x0bJ\x04\x08\x0f\x10\x10"\x17\n\x15GetPublishedEventsReq"B\n\x19LinkContainerChangedEvent\x12%\n\x06fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00"\x82\x01\n\x1bCDMRelocationRequestRestart\x12?\n\x0caccount_role\x18\x01 \x01(\x0e2).nucleus.CDMRelocationRequestRestart.Role""\n\x04Role\x12\x0c\n\x08PERSONAL\x10\x00\x12\x0c\n\x08BUSINESS\x10\x01"g\n\x16InfiniteRecallProgress\x12!\n\x04path\x18\x01 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x12\x16\n\x0eelapsed_millis\x18\x02 \x01(\x04\x12\x12\n\nrequest_id\x18\x03 \x01(\x04"5\n\x10FileChangedEvent\x12!\n\x05paths\x18\x01 \x03(\x0b2\x12.nucleus.LocalPath"\xb2\x01\n\x0cMountChanged\x12\x0e\n\x06fileid\x18\x01 \x01(\t\x12\'\n\nlocal_path\x18\x02 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x12\r\n\x05ns_id\x18\x03 \x01(\x04\x12\x0e\n\x06is_add\x18\x04 \x01(\x08\x122\n\nproperties\x18\x05 \x01(\x0b2\x18.sync.TargetNSPropertiesB\x04\xc0\xb5\x18\x00\x12\x16\n\x0eis_online_only\x18\x06 \x01(\x08";\n\x0fOfficeMoveToDFC\x12\x12\n\nlocal_path\x18\x01 \x01(\t\x12\x14\n\x0cdeleted_path\x18\x02 \x01(\t"\xc8\x03\n\x1eConflictResolutionAttemptEvent\x12-\n\x0esrc_dir_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12)\n\x0csrc_dir_path\x18\x07 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x12\x14\n\x0csrc_filename\x18\x02 \x01(\t\x12.\n\x0fdest_dir_fileid\x18\x03 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12)\n\x0cdst_dir_path\x18\x08 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x12\x15\n\rdest_filename\x18\x04 \x01(\t\x12K\n\rconflict_type\x18\x05 \x01(\x0e24.nucleus.ConflictResolutionAttemptEvent.ConflictType\x12\x13\n\x0bis_resolved\x18\x06 \x01(\x08"b\n\x0cConflictType\x12\x0f\n\x0bPERMISSIONS\x10\x00\x12\x0b\n\x07CONTENT\x10\x01\x12\x18\n\x14SERVER_REJECTED_MOVE\x10\x02\x12\t\n\x05OTHER\x10\x03\x12\x0f\n\x0bLOCKED_FILE\x10\x04"8\n\x14AppliedHiddenDefault\x12 \n\x07fileids\x18\x01 \x03(\x0b2\x0f.nucleus.FileId"\x8b\x05\n\x1bDeleteSuppressRestoredEvent\x12%\n\x06fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x12;\n\x03add\x18\x02 \x01(\x0b2,.nucleus.DeleteSuppressRestoredEvent.FromAddH\x00\x12=\n\x04move\x18\x03 \x01(\x0b2-.nucleus.DeleteSuppressRestoredEvent.FromMoveH\x00\x12N\n\rcanceled_move\x18\x04 \x01(\x0b25.nucleus.DeleteSuppressRestoredEvent.FromCanceledMoveH\x00\x12C\n\x06unsync\x18\x05 \x01(\x0b21.nucleus.DeleteSuppressRestoredEvent.NodeUnsyncedH\x00\x1a,\n\x07FromAdd\x12!\n\x04path\x18\x01 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x1aX\n\x08FromMove\x12%\n\x08dst_path\x18\x01 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x12%\n\x08src_path\x18\x02 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x1ai\n\x10FromCanceledMove\x12%\n\x08dst_path\x18\x01 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x12.\n\x0csrc_abs_path\x18\x02 \x01(\x0b2\x12.nucleus.LocalPathB\x04\xc0\xb5\x18\x00\x1a1\n\x0cNodeUnsynced\x12!\n\x04path\x18\x01 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00B\x0e\n\x06action\x12\x04\x88\xb5\x18\x00"\xa4\x05\n\x17DeviceAnchorUnbindEvent\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x127\n\x06reason\x18\x02 \x01(\x0e2\'.nucleus.DeviceAnchorUnbindEvent.Reason\x12\x11\n\tvolume_id\x18\x03 \x01(\t\x124\n\x0btarget_type\x18\x04 \x01(\x0e2\x1f.nucleus.DeviceAnchorTargetType"\xd1\x03\n\x06Reason\x12\x13\n\x0fRECONSTRUCT_ADD\x10\x00\x12\x16\n\x12RECONSTRUCT_DELETE\x10\x01\x12\x18\n\x14RECONSTRUCT_MOVE_OUT\x10\x02\x12\x17\n\x13RECONSTRUCT_MOVE_IN\x10\x03\x12\x14\n\x10RECONSTRUCT_EDIT\x10\x04\x12\x14\n\x10RECONSTRUCT_HIDE\x10\x05\x12\x16\n\x12RECONSTRUCT_RECALL\x10\x06\x12\x16\n\x12REMAKE_PLACEHOLDER\x10\x07\x12\x1f\n\x1bLOCAL_ADD_BAD_DEVICE_ANCHOR\x10\x08\x12 \n\x1cLOCAL_EDIT_BAD_DEVICE_ANCHOR\x10\t\x12\x14\n\x10REQUESTED_BY_APP\x10\n\x12\x11\n\rREMOTE_CHANGE\x10\x0b\x12\x0b\n\x07IGNORED\x10\x0c\x12\x1b\n\x17FILE_PROVIDER_MIGRATION\x10\r\x12\x1e\n\x1aSEAMLESS_FISSION_MIGRATION\x10\x0e\x12\x1a\n\x16CBOA_ABANDONED_ANCHORS\x10\x0f\x12\'\n#CBOA_ONE_WAY_SYNC_CONFLICTED_ANCHOR\x10\x10\x12\x10\n\x0cREASON_COUNT\x10\x11"c\n\x1aOneWaySyncRemediationEvent\x12\x17\n\x0fanchor_filename\x18\x01 \x01(\t\x12,\n\ranchor_fileid\x18\x02 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00"\xbd\x04\n\x1eFileProviderDumpRequestedEvent\x12\n\n\x02id\x18\x01 \x01(\x04\x12T\n\x11dump_daemon_state\x18\x02 \x01(\x0b27.nucleus.FileProviderDumpRequestedEvent.DumpDaemonStateH\x00\x12R\n\x10dump_daemon_logs\x18\x03 \x01(\x0b26.nucleus.FileProviderDumpRequestedEvent.DumpDaemonLogsH\x00\x12L\n\rdump_fs_state\x18\x04 \x01(\x0b23.nucleus.FileProviderDumpRequestedEvent.DumpFsStateH\x00\x12J\n\x0cdump_md_util\x18\x06 \x01(\x0b22.nucleus.FileProviderDumpRequestedEvent.DumpMdUtilH\x00\x12\x0b\n\x03why\x18\x05 \x01(\t\x1a\x1f\n\x0fDumpDaemonState\x12\x0c\n\x04full\x18\x01 \x01(\x08\x1a<\n\x0eDumpDaemonLogs\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08end_date\x18\x03 \x01(\tJ\x04\x08\x01\x10\x02\x1a \n\x0bDumpFsState\x12\x11\n\tfull_path\x18\x01 \x01(\t\x1a-\n\nDumpMdUtil\x12\x0e\n\x06dev_id\x18\x01 \x01(\x04\x12\x0f\n\x07file_id\x18\x02 \x01(\x04B\x0e\n\x06method\x12\x04\x88\xb5\x18\x00"\x7f\n\x12SillyLabradorEvent\x123\n\x14device_anchor_fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00\x124\n\x0btarget_type\x18\x02 \x01(\x0e2\x1f.nucleus.DeviceAnchorTargetType"\x98\x01\n\x14EncryptionErrorEvent\x124\n\x06source\x18\x01 \x01(\x0e2$.nucleus.EncryptionErrorEvent.Source"J\n\x06Source\x12\x1d\n\x19UNKNOWN_ENCRYPTION_SCHEME\x10\x00\x12!\n\x1dTEAM_KEY_FINGERPRINT_MISMATCH\x10\x01"(\n\x16ClientKeyEnrolledEvent\x12\x0e\n\x06key_id\x18\x01 \x01(\t"1\n\x1aNewTeamKeyFingerprintEvent\x12\x13\n\x0bfingerprint\x18\x01 \x01(\x0c"\xa9\x01\n\x18FPShadowCutoverCompleted\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12"\n\x15unmigrated_files_path\x18\x02 \x01(\tH\x00\x88\x01\x01\x12#\n\x16unmigrated_files_count\x18\x03 \x01(\x04H\x01\x88\x01\x01B\x18\n\x16_unmigrated_files_pathB\x19\n\x17_unmigrated_files_countB\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.published_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_PUBLISHEDEVENT'].oneofs_by_name['event']._loaded_options = None
    _globals['_PUBLISHEDEVENT'].oneofs_by_name['event']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_LINKCONTAINERCHANGEDEVENT'].fields_by_name['fileid']._loaded_options = None
    _globals['_LINKCONTAINERCHANGEDEVENT'].fields_by_name['fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_INFINITERECALLPROGRESS'].fields_by_name['path']._loaded_options = None
    _globals['_INFINITERECALLPROGRESS'].fields_by_name['path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_MOUNTCHANGED'].fields_by_name['local_path']._loaded_options = None
    _globals['_MOUNTCHANGED'].fields_by_name['local_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_MOUNTCHANGED'].fields_by_name['properties']._loaded_options = None
    _globals['_MOUNTCHANGED'].fields_by_name['properties']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT'].fields_by_name['src_dir_fileid']._loaded_options = None
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT'].fields_by_name['src_dir_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT'].fields_by_name['src_dir_path']._loaded_options = None
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT'].fields_by_name['src_dir_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT'].fields_by_name['dest_dir_fileid']._loaded_options = None
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT'].fields_by_name['dest_dir_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT'].fields_by_name['dst_dir_path']._loaded_options = None
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT'].fields_by_name['dst_dir_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMADD'].fields_by_name['path']._loaded_options = None
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMADD'].fields_by_name['path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMMOVE'].fields_by_name['dst_path']._loaded_options = None
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMMOVE'].fields_by_name['dst_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMMOVE'].fields_by_name['src_path']._loaded_options = None
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMMOVE'].fields_by_name['src_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMCANCELEDMOVE'].fields_by_name['dst_path']._loaded_options = None
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMCANCELEDMOVE'].fields_by_name['dst_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMCANCELEDMOVE'].fields_by_name['src_abs_path']._loaded_options = None
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMCANCELEDMOVE'].fields_by_name['src_abs_path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DELETESUPPRESSRESTOREDEVENT_NODEUNSYNCED'].fields_by_name['path']._loaded_options = None
    _globals['_DELETESUPPRESSRESTOREDEVENT_NODEUNSYNCED'].fields_by_name['path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DELETESUPPRESSRESTOREDEVENT'].oneofs_by_name['action']._loaded_options = None
    _globals['_DELETESUPPRESSRESTOREDEVENT'].oneofs_by_name['action']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_DELETESUPPRESSRESTOREDEVENT'].fields_by_name['fileid']._loaded_options = None
    _globals['_DELETESUPPRESSRESTOREDEVENT'].fields_by_name['fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DEVICEANCHORUNBINDEVENT'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_DEVICEANCHORUNBINDEVENT'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_ONEWAYSYNCREMEDIATIONEVENT'].fields_by_name['anchor_fileid']._loaded_options = None
    _globals['_ONEWAYSYNCREMEDIATIONEVENT'].fields_by_name['anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT'].oneofs_by_name['method']._loaded_options = None
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT'].oneofs_by_name['method']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_SILLYLABRADOREVENT'].fields_by_name['device_anchor_fileid']._loaded_options = None
    _globals['_SILLYLABRADOREVENT'].fields_by_name['device_anchor_fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_PUBLISHEDEVENT']._serialized_start = 280
    _globals['_PUBLISHEDEVENT']._serialized_end = 2014
    _globals['_PUBLISHEDEVENT_MIGRATIONCOMPLETEDINFO']._serialized_start = 1937
    _globals['_PUBLISHEDEVENT_MIGRATIONCOMPLETEDINFO']._serialized_end = 1987
    _globals['_GETPUBLISHEDEVENTSREQ']._serialized_start = 2016
    _globals['_GETPUBLISHEDEVENTSREQ']._serialized_end = 2039
    _globals['_LINKCONTAINERCHANGEDEVENT']._serialized_start = 2041
    _globals['_LINKCONTAINERCHANGEDEVENT']._serialized_end = 2107
    _globals['_CDMRELOCATIONREQUESTRESTART']._serialized_start = 2110
    _globals['_CDMRELOCATIONREQUESTRESTART']._serialized_end = 2240
    _globals['_CDMRELOCATIONREQUESTRESTART_ROLE']._serialized_start = 2206
    _globals['_CDMRELOCATIONREQUESTRESTART_ROLE']._serialized_end = 2240
    _globals['_INFINITERECALLPROGRESS']._serialized_start = 2242
    _globals['_INFINITERECALLPROGRESS']._serialized_end = 2345
    _globals['_FILECHANGEDEVENT']._serialized_start = 2347
    _globals['_FILECHANGEDEVENT']._serialized_end = 2400
    _globals['_MOUNTCHANGED']._serialized_start = 2403
    _globals['_MOUNTCHANGED']._serialized_end = 2581
    _globals['_OFFICEMOVETODFC']._serialized_start = 2583
    _globals['_OFFICEMOVETODFC']._serialized_end = 2642
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT']._serialized_start = 2645
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT']._serialized_end = 3101
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT_CONFLICTTYPE']._serialized_start = 3003
    _globals['_CONFLICTRESOLUTIONATTEMPTEVENT_CONFLICTTYPE']._serialized_end = 3101
    _globals['_APPLIEDHIDDENDEFAULT']._serialized_start = 3103
    _globals['_APPLIEDHIDDENDEFAULT']._serialized_end = 3159
    _globals['_DELETESUPPRESSRESTOREDEVENT']._serialized_start = 3162
    _globals['_DELETESUPPRESSRESTOREDEVENT']._serialized_end = 3813
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMADD']._serialized_start = 3505
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMADD']._serialized_end = 3549
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMMOVE']._serialized_start = 3551
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMMOVE']._serialized_end = 3639
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMCANCELEDMOVE']._serialized_start = 3641
    _globals['_DELETESUPPRESSRESTOREDEVENT_FROMCANCELEDMOVE']._serialized_end = 3746
    _globals['_DELETESUPPRESSRESTOREDEVENT_NODEUNSYNCED']._serialized_start = 3748
    _globals['_DELETESUPPRESSRESTOREDEVENT_NODEUNSYNCED']._serialized_end = 3797
    _globals['_DEVICEANCHORUNBINDEVENT']._serialized_start = 3816
    _globals['_DEVICEANCHORUNBINDEVENT']._serialized_end = 4492
    _globals['_DEVICEANCHORUNBINDEVENT_REASON']._serialized_start = 4027
    _globals['_DEVICEANCHORUNBINDEVENT_REASON']._serialized_end = 4492
    _globals['_ONEWAYSYNCREMEDIATIONEVENT']._serialized_start = 4494
    _globals['_ONEWAYSYNCREMEDIATIONEVENT']._serialized_end = 4593
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT']._serialized_start = 4596
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT']._serialized_end = 5169
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT_DUMPDAEMONSTATE']._serialized_start = 4979
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT_DUMPDAEMONSTATE']._serialized_end = 5010
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT_DUMPDAEMONLOGS']._serialized_start = 5012
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT_DUMPDAEMONLOGS']._serialized_end = 5072
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT_DUMPFSSTATE']._serialized_start = 5074
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT_DUMPFSSTATE']._serialized_end = 5106
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT_DUMPMDUTIL']._serialized_start = 5108
    _globals['_FILEPROVIDERDUMPREQUESTEDEVENT_DUMPMDUTIL']._serialized_end = 5153
    _globals['_SILLYLABRADOREVENT']._serialized_start = 5171
    _globals['_SILLYLABRADOREVENT']._serialized_end = 5298
    _globals['_ENCRYPTIONERROREVENT']._serialized_start = 5301
    _globals['_ENCRYPTIONERROREVENT']._serialized_end = 5453
    _globals['_ENCRYPTIONERROREVENT_SOURCE']._serialized_start = 5379
    _globals['_ENCRYPTIONERROREVENT_SOURCE']._serialized_end = 5453
    _globals['_CLIENTKEYENROLLEDEVENT']._serialized_start = 5455
    _globals['_CLIENTKEYENROLLEDEVENT']._serialized_end = 5495
    _globals['_NEWTEAMKEYFINGERPRINTEVENT']._serialized_start = 5497
    _globals['_NEWTEAMKEYFINGERPRINTEVENT']._serialized_end = 5546
    _globals['_FPSHADOWCUTOVERCOMPLETED']._serialized_start = 5549
    _globals['_FPSHADOWCUTOVERCOMPLETED']._serialized_end = 5718
    return None
