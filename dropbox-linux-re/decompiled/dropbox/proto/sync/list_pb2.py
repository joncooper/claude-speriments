# Source Generated with Decompyle++
# File: list_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync/list.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.godbx import extensions_pb2 as dropbox_dot_proto_dot_godbx_dot_extensions__pb2
from dropbox.proto.edgestore_gid import gid_pb2 as dropbox_dot_proto_dot_edgestore__gid_dot_gid__pb2
from dropbox.proto.iam_types import user_prefs_pb2 as dropbox_dot_proto_dot_iam__types_dot_user__prefs__pb2
from dropbox.proto.mypy import mypy_pb2 as dropbox_dot_proto_dot_mypy_dot_mypy__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync import cursor_pb2 as dropbox_dot_proto_dot_sync_dot_cursor__pb2
from dropbox.proto.sync import remote_ops_pb2 as dropbox_dot_proto_dot_sync_dot_remote__ops__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ddropbox/proto/sync/list.proto\x12\x04sync\x1a$dropbox/proto/godbx/extensions.proto\x1a%dropbox/proto/edgestore_gid/gid.proto\x1a(dropbox/proto/iam_types/user_prefs.proto\x1a\x1ddropbox/proto/mypy/mypy.proto\x1a#dropbox/proto/rust/extensions.proto\x1a\x1fdropbox/proto/sync/cursor.proto\x1a#dropbox/proto/sync/remote_ops.proto"f\n\x0eLinearizedPage\x12 \n\x03ops\x18\x03 \x03(\x0b2\x13.sync.ListOperation\x12,\n\x06cursor\x18\x02 \x01(\x0b2\x16.sync.LinearizedCursorB\x04\xc0\xb5\x18\x00J\x04\x08\x01\x10\x02"g\n\x0eSyncPermission\x12C\n\x04NSID\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12\x10\n\x08writable\x18\x02 \x01(\x08"\xee\x01\n\x0eExtraSyncState\x12`\n\x14admin_hidden_fileids\x18\x01 \x03(\x0cBB\xa2\xb5\x18\x1a::sync_types::RemoteFileId\xc2\xb9\x8e\x01\x1fdropbox/id/file.FileObjGidBytes\x12;\n\x13hidden_stub_fileids\x18\x02 \x03(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x12=\n\x13tss_push_directives\x18\x03 \x03(\x0b2 .sync.NamespaceTssPushDirectives"\x81\x01\n\x1aNamespaceTssPushDirectives\x127\n\x06ns_gid\x18\x01 \x01(\x0b2\x12.edgestore_gid.GidB\x13\x9a\xed \x0fNamespaceEntity\x12*\n\ndirectives\x18\x02 \x03(\x0b2\x16.sync.TssPushDirective"\x98\x01\n\x10TssPushDirective\x12R\n\x06fileid\x18\x01 \x01(\x0cBB\xa2\xb5\x18\x1a::sync_types::RemoteFileId\xc2\xb9\x8e\x01\x1fdropbox/id/file.FileObjGidBytes\x120\n\x0eintended_state\x18\x02 \x01(\x0e2\x18.sync.TssPushTargetState"e\n\x10HiddenPathHashes\x12\r\n\x05ns_id\x18\x01 \x01(\x04\x12\x1a\n\x12hidden_path_hashes\x18\x02 \x03(\x04\x12&\n\x1eguaranteed_parent_before_child\x18\x03 \x01(\x08"\x85\x02\n\x12EnterConsistentCut\x12(\n\nnamespaces\x18\x01 \x03(\x0b2\x14.sync.SyncPermission\x12/\n\x06cursor\x18\x02 \x01(\x0b2\x19.sync.ConsistentCutCursorB\x04\xc0\xb5\x18\x00\x12(\n\x0cnsproperties\x18\x03 \x03(\x0b2\x12.sync.NSProperties\x12.\n\x10extra_sync_state\x18\x04 \x01(\x0b2\x14.sync.ExtraSyncState\x12:\n\x1ainitial_hidden_path_hashes\x18\x05 \x03(\x0b2\x16.sync.HiddenPathHashes"\xf6\x01\n\x15ConsistentCutListPage\x12 \n\x03ops\x18\x05 \x03(\x0b2\x13.sync.ListOperation\x124\n\x13transplant_segments\x18\x02 \x03(\x0b2\x17.sync.TransplantSegment\x12<\n\x17continue_consistent_cut\x18\x03 \x01(\x0b2\x19.sync.ConsistentCutCursorH\x00\x127\n\x15finish_consistent_cut\x18\x04 \x01(\x0b2\x16.sync.LinearizedCursorH\x00B\x08\n\x06cursorJ\x04\x08\x01\x10\x02"\x97\x01\n\x12AbortConsistentCut\x12/\n\x06reason\x18\x01 \x01(\x0e2\x1f.sync.AbortConsistentCut.Reason\x12\x11\n\tErrorType\x18\x02 \x01(\t"=\n\x06Reason\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x1a\n\x16CURSOR_BEFORE_MIN_SJID\x10\x01\x12\n\n\x06PURGED\x10\x02"f\n\x11TransplantSegment\x12C\n\x04NSID\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12\x0c\n\x04data\x18\x02 \x01(\x0c*S\n\x14NamespaceViewVersion\x12%\n!GzippedRevisionsWithXAttrsInOneof\x10\x00\x12\x14\n\x10GzippedRevisions\x10\x01*|\n\x12TssPushTargetState\x12!\n\x1dTSS_PUSH_TARGET_STATE_UNKNOWN\x10\x00\x12 \n\x1cTSS_PUSH_TARGET_STATE_HIDDEN\x10\x01\x12!\n\x1dTSS_PUSH_TARGET_STATE_VISIBLE\x10\x02B.\n\x16com.dropbox.proto.syncP\x01Z\x12dropbox/proto/syncb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync.list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.dropbox.proto.syncP\x01Z\x12dropbox/proto/sync'
    _globals['_LINEARIZEDPAGE'].fields_by_name['cursor']._loaded_options = None
    _globals['_LINEARIZEDPAGE'].fields_by_name['cursor']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCPERMISSION'].fields_by_name['NSID']._loaded_options = None
    _globals['_SYNCPERMISSION'].fields_by_name['NSID']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_EXTRASYNCSTATE'].fields_by_name['admin_hidden_fileids']._loaded_options = None
    _globals['_EXTRASYNCSTATE'].fields_by_name['admin_hidden_fileids']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId\xc2\xb9\x8e\x01\x1fdropbox/id/file.FileObjGidBytes'
    _globals['_EXTRASYNCSTATE'].fields_by_name['hidden_stub_fileids']._loaded_options = None
    _globals['_EXTRASYNCSTATE'].fields_by_name['hidden_stub_fileids']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_NAMESPACETSSPUSHDIRECTIVES'].fields_by_name['ns_gid']._loaded_options = None
    _globals['_NAMESPACETSSPUSHDIRECTIVES'].fields_by_name['ns_gid']._serialized_options = b'\x9a\xed \x0fNamespaceEntity'
    _globals['_TSSPUSHDIRECTIVE'].fields_by_name['fileid']._loaded_options = None
    _globals['_TSSPUSHDIRECTIVE'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId\xc2\xb9\x8e\x01\x1fdropbox/id/file.FileObjGidBytes'
    _globals['_ENTERCONSISTENTCUT'].fields_by_name['cursor']._loaded_options = None
    _globals['_ENTERCONSISTENTCUT'].fields_by_name['cursor']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_TRANSPLANTSEGMENT'].fields_by_name['NSID']._loaded_options = None
    _globals['_TRANSPLANTSEGMENT'].fields_by_name['NSID']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_NAMESPACEVIEWVERSION']._serialized_start = 1907
    _globals['_NAMESPACEVIEWVERSION']._serialized_end = 1990
    _globals['_TSSPUSHTARGETSTATE']._serialized_start = 1992
    _globals['_TSSPUSHTARGETSTATE']._serialized_end = 2116
    _globals['_LINEARIZEDPAGE']._serialized_start = 296
    _globals['_LINEARIZEDPAGE']._serialized_end = 398
    _globals['_SYNCPERMISSION']._serialized_start = 400
    _globals['_SYNCPERMISSION']._serialized_end = 503
    _globals['_EXTRASYNCSTATE']._serialized_start = 506
    _globals['_EXTRASYNCSTATE']._serialized_end = 744
    _globals['_NAMESPACETSSPUSHDIRECTIVES']._serialized_start = 747
    _globals['_NAMESPACETSSPUSHDIRECTIVES']._serialized_end = 876
    _globals['_TSSPUSHDIRECTIVE']._serialized_start = 879
    _globals['_TSSPUSHDIRECTIVE']._serialized_end = 1031
    _globals['_HIDDENPATHHASHES']._serialized_start = 1033
    _globals['_HIDDENPATHHASHES']._serialized_end = 1134
    _globals['_ENTERCONSISTENTCUT']._serialized_start = 1137
    _globals['_ENTERCONSISTENTCUT']._serialized_end = 1398
    _globals['_CONSISTENTCUTLISTPAGE']._serialized_start = 1401
    _globals['_CONSISTENTCUTLISTPAGE']._serialized_end = 1647
    _globals['_ABORTCONSISTENTCUT']._serialized_start = 1650
    _globals['_ABORTCONSISTENTCUT']._serialized_end = 1801
    _globals['_ABORTCONSISTENTCUT_REASON']._serialized_start = 1740
    _globals['_ABORTCONSISTENTCUT_REASON']._serialized_end = 1801
    _globals['_TRANSPLANTSEGMENT']._serialized_start = 1803
    _globals['_TRANSPLANTSEGMENT']._serialized_end = 1905
    return None
