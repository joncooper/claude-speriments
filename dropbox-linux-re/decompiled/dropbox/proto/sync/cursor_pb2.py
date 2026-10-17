# Source Generated with Decompyle++
# File: cursor_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync/cursor.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.edgestore_gid import gid_pb2 as dropbox_dot_proto_dot_edgestore__gid_dot_gid__pb2
from dropbox.proto.gatekeeper import data_pb2 as dropbox_dot_proto_dot_gatekeeper_dot_data__pb2
from dropbox.proto.godbx import extensions_pb2 as dropbox_dot_proto_dot_godbx_dot_extensions__pb2
from dropbox.proto.iam_types import user_prefs_pb2 as dropbox_dot_proto_dot_iam__types_dot_user__prefs__pb2
from dropbox.proto.mypy import mypy_pb2 as dropbox_dot_proto_dot_mypy_dot_mypy__pb2
from dropbox.proto.sync import remote_ops_pb2 as dropbox_dot_proto_dot_sync_dot_remote__ops__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fdropbox/proto/sync/cursor.proto\x12\x04sync\x1a#dropbox/proto/rust/extensions.proto\x1a%dropbox/proto/edgestore_gid/gid.proto\x1a#dropbox/proto/gatekeeper/data.proto\x1a$dropbox/proto/godbx/extensions.proto\x1a(dropbox/proto/iam_types/user_prefs.proto\x1a\x1ddropbox/proto/mypy/mypy.proto\x1a#dropbox/proto/sync/remote_ops.proto"\xe3\x02\n\x08XOpState\x12\x0e\n\x06xop_id\x18\x01 \x01(\x0c\x12H\n\tsrc_ns_id\x18\x02 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12.\n\x04move\x18\x03 \x01(\x0b2\x1e.sync.RemoteMoveOperationProtoH\x00\x128\n\tpartition\x18\x06 \x01(\x0b2#.sync.RemotePartitionOperationProtoH\x00\x12#\n\x05state\x18\x04 \x01(\x0e2\x14.sync.XOpState.State\x12\x0f\n\x07host_id\x18\x05 \x01(\x04"W\n\x05State\x12\t\n\x05START\x10\x00\x12\x0b\n\x07EMITTED\x10\x01\x12\x1a\n\x16UNMOUNT_SRC_DEPRECATED\x10\x02\x12\x1a\n\x16UNMOUNT_DST_DEPRECATED\x10\x03B\x04\n\x02op"O\n\x0eSnapshotCursor\x12\x13\n\x0bsnapshot_id\x18\x02 \x01(\x0c\x12\x10\n\x08page_idx\x18\x03 \x01(\r\x12\x16\n\x0eoffset_in_page\x18\x04 \x01(\r"\x88\x01\n\x0cNSProperties\x12D\n\x05ns_id\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x122\n\nproperties\x18\x02 \x01(\x0b2\x18.sync.TargetNSPropertiesB\x04\xc0\xb5\x18\x00"Y\n\tTSSCursor\x127\n\x06ns_gid\x18\x01 \x01(\x0b2\x12.edgestore_gid.GidB\x13\x9a\xed \x0fNamespaceEntity\x12\x13\n\x0brevision_id\x18\x02 \x01(\x04"Y\n\x14ExtraSyncStateCursor\x12$\n\x0btss_cursors\x18\x01 \x03(\x0b2\x0f.sync.TSSCursor\x12\x1b\n\x13hidden_stub_fileids\x18\x02 \x03(\x0c"\xc0\x03\n\x08NSCursor\x12C\n\x04NSID\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12A\n\x04SJID\x18\x02 \x01(\x04B3\x82\xa6\x1d\x18dropbox/model/types.SJId\xc2\xb9\x8e\x01\x12dropbox/id.Journal\x126\n\x14child_ns_permissions\x18\x05 \x03(\x0b2\x18.gatekeeper.NSPermission\x12/\n\x13child_ns_properties\x18\x06 \x03(\x0b2\x12.sync.NSProperties\x12\x0e\n\x06hidden\x18\x07 \x01(\x08\x12\x14\n\x0chidden_paths\x18\x08 \x03(\t\x12<\n\x18sel_sync_stubs_v2_status\x18\t \x01(\x0e2\x1a.sync.SelSyncStubsV2Status\x12_\n+sel_sync_stubs_v2_hidden_by_ancestor_status\x18\n \x01(\x0e2*.sync.SelSyncStubsV2HiddenByAncestorStatus"\xc6\x08\n\x15ConsistentCutNSCursor\x126\n\x08strategy\x18\x01 \x01(\x0e2$.sync.ConsistentCutNSCursor.Strategy\x12C\n\x04NSID\x18\x02 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12C\n\x04SJID\x18\x03 \x01(\x04B3\x82\xa6\x1d\x18dropbox/model/types.SJId\xc2\xb9\x8e\x01\x12dropbox/id.JournalH\x00\x12/\n\x0fsnapshot_cursor\x18\x04 \x01(\x0b2\x14.sync.SnapshotCursorH\x00\x126\n\x14child_ns_permissions\x18\x05 \x03(\x0b2\x18.gatekeeper.NSPermission\x12\x1a\n\x12hidden_path_hashes\x18\x07 \x03(\x04\x12C\n\x0fsnapshot_status\x18\x08 \x01(\x0e2*.sync.ConsistentCutNSCursor.SnapshotStatus\x12G\n\x11transplant_reason\x18\t \x01(\x0e2,.sync.ConsistentCutNSCursor.TransplantReason"C\n\x08Strategy\x12\x0e\n\nUNASSIGNED\x10\x00\x12\x17\n\x13DIFFERENTIAL_UPDATE\x10\x01\x12\x0e\n\nTRANSPLANT\x10\x02"\x92\x01\n\x0eSnapshotStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05FOUND\x10\x01\x12\x16\n\x12NOT_FOUND_SMALL_NS\x10\x02\x12\x14\n\x10NOT_FOUND_BIG_NS\x10\x03\x12\x1a\n\x16NOT_FOUND_UNKNOWN_SIZE\x10\x04\x12\x0b\n\x07TOO_NEW\x10\x05\x12\x11\n\rFOUND_BUT_OLD\x10\x06"\xed\x02\n\x10TransplantReason\x12\x12\n\x0eUNKNOWN_REASON\x10\x00\x12\x1a\n\x16IS_DIFFERENTIAL_UPDATE\x10\x01\x12\x16\n\x12NOT_IN_PREV_CURSOR\x10\x02\x12\x18\n\x14HIDDEN_PATHS_CHANGED\x10\x03\x12\x1a\n\x16CURSOR_BEFORE_MIN_SJID\x10\x04\x12#\n\x1fDELTA_OVER_TRANSPLANT_THRESHOLD\x10\x05\x12\x14\n\x10PROTOCOL_VERSION\x10\x06\x12\x15\n\x11PREVIOUSLY_HIDDEN\x10\x07\x12\x1d\n\x19TRAVERSE_PERMISSIONS_ONLY\x10\x08\x12$\n READ_MOUNT_NAME_PERMISSIONS_ONLY\x10\t\x12\x10\n\x0cNEWLY_HIDDEN\x10\n\x12\x1a\n\x16CHILD_NAMESPACE_PURGED\x10\x0b\x12\x16\n\x12START_AT_SJID_ZERO\x10\x0cB\x08\n\x06cursorJ\x04\x08\x06\x10\x07"\x9b\x02\n\x12PerformanceMetrics\x12\x13\n\x0bduration_ms\x18\x01 \x01(\x03\x12\x11\n\tnum_pages\x18\x02 \x01(\x05\x12\x1a\n\x12start_time_unix_ms\x18\x03 \x01(\x03\x12\x1c\n\x14num_transplant_pages\x18\x04 \x01(\x05\x12 \n\x18num_differential_updates\x18\x05 \x01(\x05\x12\x1d\n\x15approx_uploaded_bytes\x18\x06 \x01(\x03\x12\x1f\n\x17approx_downloaded_bytes\x18\x07 \x01(\x03\x12"\n\x1amax_num_hidden_path_hashes\x18\x08 \x01(\x05\x12\x1d\n\x15max_cursor_size_bytes\x18\t \x01(\x03"6\n\rFeatureGating\x12%\n\x1dpebble_snapshot_read_eligible\x18\x01 \x01(\x08"\x9a\x02\n\x13ConsistentCutCursor\x12*\n\x05state\x18\x02 \x03(\x0b2\x1b.sync.ConsistentCutNSCursor\x122\n\x0cstart_cursor\x18\x04 \x01(\x0b2\x16.sync.LinearizedCursorB\x04\xc0\xb5\x18\x00\x123\n\rtarget_cursor\x18\x06 \x01(\x0b2\x16.sync.LinearizedCursorB\x04\xc0\xb5\x18\x00\x125\n\x13performance_metrics\x18\x07 \x01(\x0b2\x18.sync.PerformanceMetrics\x12%\n\x08features\x18\x08 \x01(\x0b2\x13.sync.FeatureGatingJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x04J\x04\x08\x05\x10\x06"\xda\x03\n\x10LinearizedCursor\x12\x1d\n\x05state\x18\x01 \x03(\x0b2\x0e.sync.NSCursor\x12!\n\txop_state\x18\x02 \x03(\x0b2\x0e.sync.XOpState\x122\n\x12root_ns_permission\x18\x03 \x01(\x0e2\x16.sync.RootNSPermission\x12\x19\n\x11root_filter_paths\x18\t \x03(\t\x12Q\n\x12root_filter_ns_ids\x18\n \x03(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12I\n\nroot_ns_id\x18\x04 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12\x18\n\x10protocol_version\x18\x06 \x01(\r\x124\n\x12root_ns_properties\x18\x07 \x01(\x0b2\x18.sync.TargetNSProperties\x12A\n\x17extra_sync_state_cursor\x18\x08 \x01(\x0b2\x1a.sync.ExtraSyncStateCursorB\x04\xc0\xb5\x18\x00J\x04\x08\x05\x10\x06*\x87\x02\n\x14SelSyncStubsV2Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x18\n\x14ENABLED_NEW_SNAPSHOT\x10\x05\x12\x17\n\x13ENABLED_NO_SNAPSHOT\x10\x06\x12 \n\x1cPOSSIBLE_CHILD_BEFORE_PARENT\x10\n\x12+\n\'GUARANTEED_PARENT_BEFORE_CHILD_SNAPSHOT\x10\x0b\x12.\n*GUARANTEED_PARENT_BEFORE_CHILD_NO_SNAPSHOT\x10\x0c"\x04\x08\x02\x10\x02"\x04\x08\x03\x10\x03"\x04\x08\x04\x10\x04"\x04\x08\x07\x10\x07"\x04\x08\x08\x10\x08"\x04\x08\t\x10\t*\xcc\x01\n$SelSyncStubsV2HiddenByAncestorStatus\x12%\n!UNKNOWN_HIDDEN_BY_ANCESTOR_STATUS\x10\x00\x12\x1a\n\x16NOT_HIDDEN_BY_ANCESTOR\x10\x01\x120\n,HIDDEN_BY_SELSYNC_STUBS_V2_DISABLED_ANCESTOR\x10\x02\x12/\n+HIDDEN_BY_SELSYNC_STUBS_V2_ENABLED_ANCESTOR\x10\x03*>\n\x10RootNSPermission\x12\x0c\n\x08READ_ALL\x10\x00\x12\x0e\n\nREAD_WRITE\x10\x01\x12\x0c\n\x08TRAVERSE\x10\x02B4\n\x16com.dropbox.proto.syncP\x01Z\x12dropbox/proto/sync\xa2\x02\x03DBXb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync.cursor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.dropbox.proto.syncP\x01Z\x12dropbox/proto/sync\xa2\x02\x03DBX'
    _globals['_XOPSTATE'].fields_by_name['src_ns_id']._loaded_options = None
    _globals['_XOPSTATE'].fields_by_name['src_ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_NSPROPERTIES'].fields_by_name['ns_id']._loaded_options = None
    _globals['_NSPROPERTIES'].fields_by_name['ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_NSPROPERTIES'].fields_by_name['properties']._loaded_options = None
    _globals['_NSPROPERTIES'].fields_by_name['properties']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_TSSCURSOR'].fields_by_name['ns_gid']._loaded_options = None
    _globals['_TSSCURSOR'].fields_by_name['ns_gid']._serialized_options = b'\x9a\xed \x0fNamespaceEntity'
    _globals['_NSCURSOR'].fields_by_name['NSID']._loaded_options = None
    _globals['_NSCURSOR'].fields_by_name['NSID']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_NSCURSOR'].fields_by_name['SJID']._loaded_options = None
    _globals['_NSCURSOR'].fields_by_name['SJID']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.SJId\xc2\xb9\x8e\x01\x12dropbox/id.Journal'
    _globals['_CONSISTENTCUTNSCURSOR'].fields_by_name['NSID']._loaded_options = None
    _globals['_CONSISTENTCUTNSCURSOR'].fields_by_name['NSID']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_CONSISTENTCUTNSCURSOR'].fields_by_name['SJID']._loaded_options = None
    _globals['_CONSISTENTCUTNSCURSOR'].fields_by_name['SJID']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.SJId\xc2\xb9\x8e\x01\x12dropbox/id.Journal'
    _globals['_CONSISTENTCUTCURSOR'].fields_by_name['start_cursor']._loaded_options = None
    _globals['_CONSISTENTCUTCURSOR'].fields_by_name['start_cursor']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CONSISTENTCUTCURSOR'].fields_by_name['target_cursor']._loaded_options = None
    _globals['_CONSISTENTCUTCURSOR'].fields_by_name['target_cursor']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_LINEARIZEDCURSOR'].fields_by_name['root_filter_ns_ids']._loaded_options = None
    _globals['_LINEARIZEDCURSOR'].fields_by_name['root_filter_ns_ids']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_LINEARIZEDCURSOR'].fields_by_name['root_ns_id']._loaded_options = None
    _globals['_LINEARIZEDCURSOR'].fields_by_name['root_ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_LINEARIZEDCURSOR'].fields_by_name['extra_sync_state_cursor']._loaded_options = None
    _globals['_LINEARIZEDCURSOR'].fields_by_name['extra_sync_state_cursor']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SELSYNCSTUBSV2STATUS']._serialized_start = 3715
    _globals['_SELSYNCSTUBSV2STATUS']._serialized_end = 3978
    _globals['_SELSYNCSTUBSV2HIDDENBYANCESTORSTATUS']._serialized_start = 3981
    _globals['_SELSYNCSTUBSV2HIDDENBYANCESTORSTATUS']._serialized_end = 4185
    _globals['_ROOTNSPERMISSION']._serialized_start = 4187
    _globals['_ROOTNSPERMISSION']._serialized_end = 4249
    _globals['_XOPSTATE']._serialized_start = 303
    _globals['_XOPSTATE']._serialized_end = 658
    _globals['_XOPSTATE_STATE']._serialized_start = 565
    _globals['_XOPSTATE_STATE']._serialized_end = 652
    _globals['_SNAPSHOTCURSOR']._serialized_start = 660
    _globals['_SNAPSHOTCURSOR']._serialized_end = 739
    _globals['_NSPROPERTIES']._serialized_start = 742
    _globals['_NSPROPERTIES']._serialized_end = 878
    _globals['_TSSCURSOR']._serialized_start = 880
    _globals['_TSSCURSOR']._serialized_end = 969
    _globals['_EXTRASYNCSTATECURSOR']._serialized_start = 971
    _globals['_EXTRASYNCSTATECURSOR']._serialized_end = 1060
    _globals['_NSCURSOR']._serialized_start = 1063
    _globals['_NSCURSOR']._serialized_end = 1511
    _globals['_CONSISTENTCUTNSCURSOR']._serialized_start = 1514
    _globals['_CONSISTENTCUTNSCURSOR']._serialized_end = 2608
    _globals['_CONSISTENTCUTNSCURSOR_STRATEGY']._serialized_start = 2008
    _globals['_CONSISTENTCUTNSCURSOR_STRATEGY']._serialized_end = 2075
    _globals['_CONSISTENTCUTNSCURSOR_SNAPSHOTSTATUS']._serialized_start = 2078
    _globals['_CONSISTENTCUTNSCURSOR_SNAPSHOTSTATUS']._serialized_end = 2224
    _globals['_CONSISTENTCUTNSCURSOR_TRANSPLANTREASON']._serialized_start = 2227
    _globals['_CONSISTENTCUTNSCURSOR_TRANSPLANTREASON']._serialized_end = 2592
    _globals['_PERFORMANCEMETRICS']._serialized_start = 2611
    _globals['_PERFORMANCEMETRICS']._serialized_end = 2894
    _globals['_FEATUREGATING']._serialized_start = 2896
    _globals['_FEATUREGATING']._serialized_end = 2950
    _globals['_CONSISTENTCUTCURSOR']._serialized_start = 2953
    _globals['_CONSISTENTCUTCURSOR']._serialized_end = 3235
    _globals['_LINEARIZEDCURSOR']._serialized_start = 3238
    _globals['_LINEARIZEDCURSOR']._serialized_end = 3712
    return None
