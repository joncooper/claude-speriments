# Source Generated with Decompyle++
# File: remote_ops_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync/remote_ops.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.cypress import item_pb2 as dropbox_dot_proto_dot_cypress_dot_item__pb2
from dropbox.proto.godbx import extensions_pb2 as dropbox_dot_proto_dot_godbx_dot_extensions__pb2
from dropbox.proto.mypy import mypy_pb2 as dropbox_dot_proto_dot_mypy_dot_mypy__pb2
from dropbox.proto.namespace import namespace_entity_pb2 as dropbox_dot_proto_dot_namespace_dot_namespace__entity__pb2
from dropbox.proto.per_node_metadata import attributes_pb2 as dropbox_dot_proto_dot_per__node__metadata_dot_attributes__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync import xattr_pb2 as dropbox_dot_proto_dot_sync_dot_xattr__pb2
from dropbox.proto.version_tree import types_pb2 as dropbox_dot_proto_dot_version__tree_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#dropbox/proto/sync/remote_ops.proto\x12\x04sync\x1a dropbox/proto/cypress/item.proto\x1a$dropbox/proto/godbx/extensions.proto\x1a\x1ddropbox/proto/mypy/mypy.proto\x1a.dropbox/proto/namespace/namespace_entity.proto\x1a0dropbox/proto/per_node_metadata/attributes.proto\x1a#dropbox/proto/rust/extensions.proto\x1a\x1edropbox/proto/sync/xattr.proto\x1a&dropbox/proto/version_tree/types.proto"\x86\x03\n\x17ClientDerivedProperties\x12 \n\x18can_mount_shared_folders\x18\x01 \x01(\x08\x12\x1d\n\x15is_team_shared_folder\x18\x03 \x01(\x08\x12\x16\n\x0ein_team_folder\x18\x04 \x01(\x08\x12\x17\n\x0fis_confidential\x18\x05 \x01(\x08\x12!\n\x19only_owner_can_update_acl\x18\x06 \x01(\x08\x12\x1f\n\x17forbid_non_team_sharing\x18\x07 \x01(\x08\x12%\n\x1dis_user_on_same_team_as_owner\x18\x08 \x01(\x08\x12C\n\x07team_id\x18\t \x01(\x03B2\x82\xa6\x1d\x1adropbox/model/types.TeamId\xc2\xb9\x8e\x01\x0fdropbox/id.Team\x12\x10\n\x08is_owner\x18\n \x01(\x08\x12\x14\n\x0cis_no_access\x18\x0b \x01(\x08\x12\x1b\n\x13is_encrypted_folder\x18\x0c \x01(\x08J\x04\x08\x02\x10\x03"h\n\x04File\x12\x1f\n\tblocklist\x18\x01 \x03(\x0cB\x0c\xa2\xb5\x18\x08[u8; 32]\x12\x0c\n\x04size\x18\x02 \x01(\x04\x121\n\x03pnm\x18\x03 \x01(\x0b2\x1e.per_node_metadata.FilePNMListB\x04\xc0\xb5\x18\x00"\r\n\x0bPlaceholder"C\n\tDirectory\x126\n\x03pnm\x18\x01 \x01(\x0b2#.per_node_metadata.DirectoryPNMListB\x04\xc0\xb5\x18\x00"j\n\x07Symlink\x12)\n\x06target\x18\x01 \x01(\x0b2\x13.sync.SymlinkTargetB\x04\xc0\xb5\x18\x00\x124\n\x03pnm\x18\x02 \x01(\x0b2!.per_node_metadata.SymlinkPNMListB\x04\xc0\xb5\x18\x00"\x83\x01\n\x12TargetNSProperties\x12/\n\x07ns_type\x18\x01 \x01(\x0e2\x1e.namespace.NamespaceTypeValues\x12<\n\x15ns_derived_properties\x18\x02 \x01(\x0b2\x1d.sync.ClientDerivedProperties"\xd1\x01\n\x05Mount\x12(\n\tdirectory\x18\x05 \x01(\x0b2\x0f.sync.DirectoryB\x04\xc0\xb5\x18\x00\x12H\n\ttarget_ns\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12\x10\n\x08writable\x18\x02 \x01(\x08\x12<\n\x14target_ns_properties\x18\x04 \x01(\x0b2\x18.sync.TargetNSPropertiesB\x04\xc0\xb5\x18\x00J\x04\x08\x03\x10\x04"\x1f\n\rSymlinkTarget\x12\x0e\n\x06target\x18\x01 \x01(\x0c"2\n\x0cUpdateFileId\x12\x0e\n\x06fileid\x18\x01 \x01(\x0c\x12\x12\n\nnew_fileid\x18\x02 \x01(\x0c"\xfe\x01\n\x06Object\x12\x1a\n\x04file\x18\x01 \x01(\x0b2\n.sync.FileH\x00\x12\x1e\n\x03dir\x18\x02 \x01(\x0b2\x0f.sync.DirectoryH\x00\x12 \n\x07symlink\x18\x03 \x01(\x0b2\r.sync.SymlinkH\x00\x12\x1c\n\x05mount\x18\x04 \x01(\x0b2\x0b.sync.MountH\x00\x12*\n\x06xattrs\x18\x05 \x03(\x0b2\x1a.sync.RawExtendedAttribute\x12\r\n\x05mtime\x18\x06 \x01(\x03\x12*\n\titem_data\x18\x07 \x03(\x0b2\x17.cypress.ItemDataRecordB\x11\n\tfile_type\x12\x04\x88\xb5\x18\x00"p\n\x0fRevisionDetails\x12C\n\x07user_id\x18\x01 \x01(\x03B2\x82\xa6\x1d\x1adropbox/model/types.UserId\xc2\xb9\x8e\x01\x0fdropbox/id.User\x12\x18\n\x10server_timestamp\x18\x02 \x01(\x03"\xf3\x01\n\x17RemoteAddOperationProto\x12\x10\n\x08filename\x18\x03 \x01(\t\x12\x1f\n\x03obj\x18\x05 \x01(\x0b2\x0c.sync.ObjectB\x04\xc0\xb5\x18\x00\x12(\n\x06fileid\x18\x06 \x01(\x0cB\x18\xa2\xb5\x18\x14::sync_types::FileId\x12\x12\n\ndir_fileid\x18\x07 \x01(\x0c\x12/\n\x10revision_details\x18\x08 \x01(\x0b2\x15.sync.RevisionDetails\x12\x1e\n\x03oid\x18\n \x01(\x0b2\x11.version_tree.OidJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05J\x04\x08\t\x10\n"\xce\x01\n\x18RemoteEditOperationProto\x12\x1f\n\x03obj\x18\x03 \x01(\x0b2\x0c.sync.ObjectB\x04\xc0\xb5\x18\x00\x12.\n\x06fileid\x18\x04 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x12/\n\x10revision_details\x18\x05 \x01(\x0b2\x15.sync.RevisionDetails\x12\x1e\n\x03oid\x18\x07 \x01(\x0b2\x11.version_tree.OidJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x06\x10\x07"\xee\x01\n\x18RemoteMoveOperationProto\x12\x14\n\x0cdst_filename\x18\x03 \x01(\t\x12H\n\tdst_ns_id\x18\x04 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12.\n\x06fileid\x18\x05 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x126\n\x0edst_dir_fileid\x18\x06 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileIdJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03"\xa4\x01\n\x1aRemoteDeleteOperationProto\x12\x19\n\x03obj\x18\x02 \x01(\x0b2\x0c.sync.Object\x12.\n\x06fileid\x18\x03 \x01(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileId\x12/\n\x10revision_details\x18\x04 \x01(\x0b2\x15.sync.RevisionDetailsJ\x04\x08\x01\x10\x02J\x04\x08\x05\x10\x06"\x1f\n\x1dRemotePartitionOperationProto"?\n\x13CommitEditExtraInfo\x12(\n\x0cexisting_obj\x18\x01 \x01(\x0b2\x0c.sync.ObjectB\x04\xc0\xb5\x18\x00"A\n\x15CommitDeleteExtraInfo\x12(\n\x0cexisting_obj\x18\x01 \x01(\x0b2\x0c.sync.ObjectB\x04\xc0\xb5\x18\x00"?\n\x13CommitMoveExtraInfo\x12(\n\x0cexisting_obj\x18\x01 \x01(\x0b2\x0c.sync.ObjectB\x04\xc0\xb5\x18\x00"\x9a\x04\n\x0fCommitOperation\x12C\n\x04NSID\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12,\n\x03add\x18\x02 \x01(\x0b2\x1d.sync.RemoteAddOperationProtoH\x00\x12.\n\x04edit\x18\x03 \x01(\x0b2\x1e.sync.RemoteEditOperationProtoH\x00\x12.\n\x04move\x18\x04 \x01(\x0b2\x1e.sync.RemoteMoveOperationProtoH\x00\x122\n\x06delete\x18\x05 \x01(\x0b2 .sync.RemoteDeleteOperationProtoH\x00\x124\n\x0fedit_extra_info\x18\x06 \x01(\x0b2\x19.sync.CommitEditExtraInfoH\x01\x128\n\x11delete_extra_info\x18\x07 \x01(\x0b2\x1b.sync.CommitDeleteExtraInfoH\x01\x124\n\x0fmove_extra_info\x18\x08 \x01(\x0b2\x19.sync.CommitMoveExtraInfoH\x01\x12@\n\x18blockcopy_source_fileids\x18\t \x03(\x0cB\x1e\xa2\xb5\x18\x1a::sync_types::RemoteFileIdB\n\n\x02op\x12\x04\x88\xb5\x18\x00B\x0c\n\nextra_info"\xa3\x03\n\rListOperation\x12C\n\x04NSID\x18\x01 \x01(\x04B5\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace\x12B\n\x06hostID\x18\x02 \x01(\x04B2\x82\xa6\x1d\x1adropbox/model/types.HostId\xc2\xb9\x8e\x01\x0fdropbox/id.Host\x12/\n\x06add_op\x18\x03 \x01(\x0b2\x1d.sync.RemoteAddOperationProtoH\x00\x121\n\x07edit_op\x18\x04 \x01(\x0b2\x1e.sync.RemoteEditOperationProtoH\x00\x121\n\x07move_op\x18\x05 \x01(\x0b2\x1e.sync.RemoteMoveOperationProtoH\x00\x125\n\tdelete_op\x18\x06 \x01(\x0b2 .sync.RemoteDeleteOperationProtoH\x00\x12/\n\x11update_file_id_op\x18\x07 \x01(\x0b2\x12.sync.UpdateFileIdH\x00B\n\n\x02op\x12\x04\x88\xb5\x18\x00B4\n\x16com.dropbox.proto.syncP\x01Z\x12dropbox/proto/sync\xa2\x02\x03DBXb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync.remote_ops_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.dropbox.proto.syncP\x01Z\x12dropbox/proto/sync\xa2\x02\x03DBX'
    _globals['_CLIENTDERIVEDPROPERTIES'].fields_by_name['team_id']._loaded_options = None
    _globals['_CLIENTDERIVEDPROPERTIES'].fields_by_name['team_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.TeamId\xc2\xb9\x8e\x01\x0fdropbox/id.Team'
    _globals['_FILE'].fields_by_name['blocklist']._loaded_options = None
    _globals['_FILE'].fields_by_name['blocklist']._serialized_options = b'\xa2\xb5\x18\x08[u8; 32]'
    _globals['_FILE'].fields_by_name['pnm']._loaded_options = None
    _globals['_FILE'].fields_by_name['pnm']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DIRECTORY'].fields_by_name['pnm']._loaded_options = None
    _globals['_DIRECTORY'].fields_by_name['pnm']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYMLINK'].fields_by_name['target']._loaded_options = None
    _globals['_SYMLINK'].fields_by_name['target']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYMLINK'].fields_by_name['pnm']._loaded_options = None
    _globals['_SYMLINK'].fields_by_name['pnm']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_MOUNT'].fields_by_name['directory']._loaded_options = None
    _globals['_MOUNT'].fields_by_name['directory']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_MOUNT'].fields_by_name['target_ns']._loaded_options = None
    _globals['_MOUNT'].fields_by_name['target_ns']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_MOUNT'].fields_by_name['target_ns_properties']._loaded_options = None
    _globals['_MOUNT'].fields_by_name['target_ns_properties']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_OBJECT'].oneofs_by_name['file_type']._loaded_options = None
    _globals['_OBJECT'].oneofs_by_name['file_type']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_REVISIONDETAILS'].fields_by_name['user_id']._loaded_options = None
    _globals['_REVISIONDETAILS'].fields_by_name['user_id']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.UserId\xc2\xb9\x8e\x01\x0fdropbox/id.User'
    _globals['_REMOTEADDOPERATIONPROTO'].fields_by_name['obj']._loaded_options = None
    _globals['_REMOTEADDOPERATIONPROTO'].fields_by_name['obj']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_REMOTEADDOPERATIONPROTO'].fields_by_name['fileid']._loaded_options = None
    _globals['_REMOTEADDOPERATIONPROTO'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x14::sync_types::FileId'
    _globals['_REMOTEEDITOPERATIONPROTO'].fields_by_name['obj']._loaded_options = None
    _globals['_REMOTEEDITOPERATIONPROTO'].fields_by_name['obj']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_REMOTEEDITOPERATIONPROTO'].fields_by_name['fileid']._loaded_options = None
    _globals['_REMOTEEDITOPERATIONPROTO'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_REMOTEMOVEOPERATIONPROTO'].fields_by_name['dst_ns_id']._loaded_options = None
    _globals['_REMOTEMOVEOPERATIONPROTO'].fields_by_name['dst_ns_id']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_REMOTEMOVEOPERATIONPROTO'].fields_by_name['fileid']._loaded_options = None
    _globals['_REMOTEMOVEOPERATIONPROTO'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_REMOTEMOVEOPERATIONPROTO'].fields_by_name['dst_dir_fileid']._loaded_options = None
    _globals['_REMOTEMOVEOPERATIONPROTO'].fields_by_name['dst_dir_fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_REMOTEDELETEOPERATIONPROTO'].fields_by_name['fileid']._loaded_options = None
    _globals['_REMOTEDELETEOPERATIONPROTO'].fields_by_name['fileid']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_COMMITEDITEXTRAINFO'].fields_by_name['existing_obj']._loaded_options = None
    _globals['_COMMITEDITEXTRAINFO'].fields_by_name['existing_obj']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_COMMITDELETEEXTRAINFO'].fields_by_name['existing_obj']._loaded_options = None
    _globals['_COMMITDELETEEXTRAINFO'].fields_by_name['existing_obj']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_COMMITMOVEEXTRAINFO'].fields_by_name['existing_obj']._loaded_options = None
    _globals['_COMMITMOVEEXTRAINFO'].fields_by_name['existing_obj']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_COMMITOPERATION'].oneofs_by_name['op']._loaded_options = None
    _globals['_COMMITOPERATION'].oneofs_by_name['op']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_COMMITOPERATION'].fields_by_name['NSID']._loaded_options = None
    _globals['_COMMITOPERATION'].fields_by_name['NSID']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_COMMITOPERATION'].fields_by_name['blockcopy_source_fileids']._loaded_options = None
    _globals['_COMMITOPERATION'].fields_by_name['blockcopy_source_fileids']._serialized_options = b'\xa2\xb5\x18\x1a::sync_types::RemoteFileId'
    _globals['_LISTOPERATION'].oneofs_by_name['op']._loaded_options = None
    _globals['_LISTOPERATION'].oneofs_by_name['op']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_LISTOPERATION'].fields_by_name['NSID']._loaded_options = None
    _globals['_LISTOPERATION'].fields_by_name['NSID']._serialized_options = b'\x82\xa6\x1d\x18dropbox/model/types.NsId\xc2\xb9\x8e\x01\x14dropbox/id.Namespace'
    _globals['_LISTOPERATION'].fields_by_name['hostID']._loaded_options = None
    _globals['_LISTOPERATION'].fields_by_name['hostID']._serialized_options = b'\x82\xa6\x1d\x1adropbox/model/types.HostId\xc2\xb9\x8e\x01\x0fdropbox/id.Host'
    _globals['_CLIENTDERIVEDPROPERTIES']._serialized_start = 356
    _globals['_CLIENTDERIVEDPROPERTIES']._serialized_end = 746
    _globals['_FILE']._serialized_start = 748
    _globals['_FILE']._serialized_end = 852
    _globals['_PLACEHOLDER']._serialized_start = 854
    _globals['_PLACEHOLDER']._serialized_end = 867
    _globals['_DIRECTORY']._serialized_start = 869
    _globals['_DIRECTORY']._serialized_end = 936
    _globals['_SYMLINK']._serialized_start = 938
    _globals['_SYMLINK']._serialized_end = 1044
    _globals['_TARGETNSPROPERTIES']._serialized_start = 1047
    _globals['_TARGETNSPROPERTIES']._serialized_end = 1178
    _globals['_MOUNT']._serialized_start = 1181
    _globals['_MOUNT']._serialized_end = 1390
    _globals['_SYMLINKTARGET']._serialized_start = 1392
    _globals['_SYMLINKTARGET']._serialized_end = 1423
    _globals['_UPDATEFILEID']._serialized_start = 1425
    _globals['_UPDATEFILEID']._serialized_end = 1475
    _globals['_OBJECT']._serialized_start = 1478
    _globals['_OBJECT']._serialized_end = 1732
    _globals['_REVISIONDETAILS']._serialized_start = 1734
    _globals['_REVISIONDETAILS']._serialized_end = 1846
    _globals['_REMOTEADDOPERATIONPROTO']._serialized_start = 1849
    _globals['_REMOTEADDOPERATIONPROTO']._serialized_end = 2092
    _globals['_REMOTEEDITOPERATIONPROTO']._serialized_start = 2095
    _globals['_REMOTEEDITOPERATIONPROTO']._serialized_end = 2301
    _globals['_REMOTEMOVEOPERATIONPROTO']._serialized_start = 2304
    _globals['_REMOTEMOVEOPERATIONPROTO']._serialized_end = 2542
    _globals['_REMOTEDELETEOPERATIONPROTO']._serialized_start = 2545
    _globals['_REMOTEDELETEOPERATIONPROTO']._serialized_end = 2709
    _globals['_REMOTEPARTITIONOPERATIONPROTO']._serialized_start = 2711
    _globals['_REMOTEPARTITIONOPERATIONPROTO']._serialized_end = 2742
    _globals['_COMMITEDITEXTRAINFO']._serialized_start = 2744
    _globals['_COMMITEDITEXTRAINFO']._serialized_end = 2807
    _globals['_COMMITDELETEEXTRAINFO']._serialized_start = 2809
    _globals['_COMMITDELETEEXTRAINFO']._serialized_end = 2874
    _globals['_COMMITMOVEEXTRAINFO']._serialized_start = 2876
    _globals['_COMMITMOVEEXTRAINFO']._serialized_end = 2939
    _globals['_COMMITOPERATION']._serialized_start = 2942
    _globals['_COMMITOPERATION']._serialized_end = 3480
    _globals['_LISTOPERATION']._serialized_start = 3483
    _globals['_LISTOPERATION']._serialized_end = 3902
    return None
