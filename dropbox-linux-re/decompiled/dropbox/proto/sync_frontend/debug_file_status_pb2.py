# Source Generated with Decompyle++
# File: debug_file_status_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync_frontend/debug_file_status.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync import remote_ops_pb2 as dropbox_dot_proto_dot_sync_dot_remote__ops__pb2
from dropbox.proto.sync import xattr_pb2 as dropbox_dot_proto_dot_sync_dot_xattr__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3dropbox/proto/sync_frontend/debug_file_status.proto\x12\rsync_frontend\x1a#dropbox/proto/rust/extensions.proto\x1a#dropbox/proto/sync/remote_ops.proto\x1a\x1edropbox/proto/sync/xattr.proto\x1a\x1bgoogle/protobuf/empty.proto"\x18\n\x06FileId\x12\x0e\n\x06fileId\x18\x01 \x01(\t"\'\n\x04File\x12\x1f\n\x0bremote_data\x18\x01 \x01(\x0b2\n.sync.File"Z\n\x0bFileContent\x12\x1f\n\tblocklist\x18\x01 \x03(\x0cB\x0c\xa2\xb5\x18\x08[u8; 32]\x12*\n\x06xattrs\x18\x02 \x03(\x0b2\x1a.sync.RawExtendedAttribute"\x87\x01\n\x0bPlaceholder\x12\x0c\n\x04size\x18\x01 \x01(\x04\x12,\n\rtarget_fileid\x18\x02 \x01(\x0b2\x15.sync_frontend.FileId\x12+\n\x07content\x18\x03 \x01(\x0b2\x1a.sync_frontend.FileContent\x12\x0f\n\x07version\x18\x04 \x01(\x05"\xf5\x01\n\tDirectory\x12$\n\x0bremote_data\x18\x01 \x01(\x0b2\x0f.sync.Directory\x12)\n\x07unknown\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12\x13\n\ticon_type\x18\x03 \x01(\tH\x00\x12<\n\x0fadd_destination\x18\x04 \x01(\x0e2#.sync_frontend.OnDiskAddDestination\x126\n\x14target_ns_properties\x18\x05 \x01(\x0b2\x18.sync.TargetNSPropertiesB\x0c\n\x04icon\x12\x04\x88\xb5\x18\x01"-\n\x07Symlink\x12"\n\x0bremote_data\x18\x01 \x01(\x0b2\r.sync.Symlink"\xe8\x01\n\x07Ignored\x12+\n\tdirectory\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12\x0e\n\x04file\x18\x02 \x01(\x04H\x00\x12)\n\x07symlink\x18\x03 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x121\n\x0bplaceholder\x18\x04 \x01(\x0b2\x1a.sync_frontend.PlaceholderH\x00\x12/\n\rdevice_anchor\x18\x05 \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x11\n\tfile_type\x12\x04\x88\xb5\x18\x00"i\n\x0fNodePermissions\x121\n\x04mode\x18\x01 \x01(\x0e2#.sync_frontend.NodePermissions.Mode"#\n\x04Mode\x12\x0c\n\x08ReadOnly\x10\x00\x12\r\n\tReadWrite\x10\x01"\xcc\x04\n\x0eFileStatusNode\x129\n\x0bpermissions\x18\x04 \x01(\x0b2\x1e.sync_frontend.NodePermissionsB\x04\xc0\xb5\x18\x00\x12*\n\x06xattrs\x18\t \x03(\x0b2\x1a.sync.RawExtendedAttribute\x12#\n\x04file\x18\x05 \x01(\x0b2\x13.sync_frontend.FileH\x00\x12\'\n\x03dir\x18\x06 \x01(\x0b2\x18.sync_frontend.DirectoryH\x00\x12)\n\x05mount\x18\x07 \x01(\x0b2\x18.sync_frontend.DirectoryH\x00\x12)\n\x07symlink\x18\x08 \x01(\x0b2\x16.sync_frontend.SymlinkH\x00\x12)\n\x07ignored\x18\n \x01(\x0b2\x16.sync_frontend.IgnoredH\x00\x121\n\x0bplaceholder\x18\x0b \x01(\x0b2\x1a.sync_frontend.PlaceholderH\x00\x12(\n\x05times\x18\x0c \x01(\x0b2\x19.sync_frontend.Timestamps\x12\r\n\x05inode\x18\r \x01(\x04\x12\x11\n\tnode_type\x18\x0e \x01(\t\x12\r\n\x05mtime\x18\x0f \x01(\x03\x12/\n\x10revision_details\x18\x10 \x01(\x0b2\x15.sync.RevisionDetails\x128\n\x10hydration_policy\x18\x11 \x01(\x0b2\x1e.sync_frontend.HydrationPolicyB\x0b\n\tfile_type"`\n\x0fHydrationPolicy\x12\x1b\n\x11local_with_reason\x18\x01 \x01(\tH\x00\x12!\n\x17online_only_with_reason\x18\x02 \x01(\tH\x00B\r\n\x05state\x12\x04\x88\xb5\x18\x00"9\n\nTimestamps\x12\r\n\x05mtime\x18\x01 \x01(\x03\x12\r\n\x05ctime\x18\x02 \x01(\x03\x12\r\n\x05extra\x18\x03 \x01(\r"-\n\x04Path\x12%\n\x06fileId\x18\x01 \x03(\x0b2\x15.sync_frontend.FileId*7\n\x14OnDiskAddDestination\x12\x10\n\x0cUNRESTRICTED\x10\x00\x12\r\n\tHOME_ONLY\x10\x01B\x1dZ\x1bdropbox/proto/sync_frontendb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync_frontend.debug_file_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1bdropbox/proto/sync_frontend'
    _globals['_FILECONTENT'].fields_by_name['blocklist']._loaded_options = None
    _globals['_FILECONTENT'].fields_by_name['blocklist']._serialized_options = b'\xa2\xb5\x18\x08[u8; 32]'
    _globals['_DIRECTORY'].oneofs_by_name['icon']._loaded_options = None
    _globals['_DIRECTORY'].oneofs_by_name['icon']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_IGNORED'].oneofs_by_name['file_type']._loaded_options = None
    _globals['_IGNORED'].oneofs_by_name['file_type']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_FILESTATUSNODE'].fields_by_name['permissions']._loaded_options = None
    _globals['_FILESTATUSNODE'].fields_by_name['permissions']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_HYDRATIONPOLICY'].oneofs_by_name['state']._loaded_options = None
    _globals['_HYDRATIONPOLICY'].oneofs_by_name['state']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_ONDISKADDDESTINATION']._serialized_start = 1934
    _globals['_ONDISKADDDESTINATION']._serialized_end = 1989
    _globals['_FILEID']._serialized_start = 205
    _globals['_FILEID']._serialized_end = 229
    _globals['_FILE']._serialized_start = 231
    _globals['_FILE']._serialized_end = 270
    _globals['_FILECONTENT']._serialized_start = 272
    _globals['_FILECONTENT']._serialized_end = 362
    _globals['_PLACEHOLDER']._serialized_start = 365
    _globals['_PLACEHOLDER']._serialized_end = 500
    _globals['_DIRECTORY']._serialized_start = 503
    _globals['_DIRECTORY']._serialized_end = 748
    _globals['_SYMLINK']._serialized_start = 750
    _globals['_SYMLINK']._serialized_end = 795
    _globals['_IGNORED']._serialized_start = 798
    _globals['_IGNORED']._serialized_end = 1030
    _globals['_NODEPERMISSIONS']._serialized_start = 1032
    _globals['_NODEPERMISSIONS']._serialized_end = 1137
    _globals['_NODEPERMISSIONS_MODE']._serialized_start = 1102
    _globals['_NODEPERMISSIONS_MODE']._serialized_end = 1137
    _globals['_FILESTATUSNODE']._serialized_start = 1140
    _globals['_FILESTATUSNODE']._serialized_end = 1728
    _globals['_HYDRATIONPOLICY']._serialized_start = 1730
    _globals['_HYDRATIONPOLICY']._serialized_end = 1826
    _globals['_TIMESTAMPS']._serialized_start = 1828
    _globals['_TIMESTAMPS']._serialized_end = 1885
    _globals['_PATH']._serialized_start = 1887
    _globals['_PATH']._serialized_end = 1932
    return None
