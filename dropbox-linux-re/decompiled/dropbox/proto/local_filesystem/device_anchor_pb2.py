# Source Generated with Decompyle++
# File: device_anchor_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/local_filesystem/device_anchor.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2dropbox/proto/local_filesystem/device_anchor.proto\x12\x10local_filesystem\x1a#dropbox/proto/rust/extensions.proto"4\n\x17DeviceAnchorTargetFlags\x12\x19\n\x04bits\x18\x01 \x01(\x0cB\x0b\xa2\xb5\x18\x07[u8; 1]"\xba\x01\n\x13DeviceAnchorDetails\x12F\n\rtarget_fileid\x18\x01 \x01(\x0cB/\xa2\xb5\x18+::std::option::Option<::sync_types::FileId>\x12\x14\n\x0ctarget_inode\x18\x02 \x01(\x04\x12E\n\x0ctarget_flags\x18\x03 \x01(\x0b2).local_filesystem.DeviceAnchorTargetFlagsB\x04\xc0\xb5\x18\x00"\x9f\x01\n\x12DeviceAnchorStatus\x12@\n\x08inactive\x18\x01 \x01(\x0e2,.local_filesystem.DeviceAnchorInactiveReasonH\x00\x127\n\x06active\x18\x02 \x01(\x0b2%.local_filesystem.DeviceAnchorDetailsH\x00B\x0e\n\x06status\x12\x04\x88\xb5\x18\x00*[\n\x1aDeviceAnchorInactiveReason\x12\x0f\n\x0bUnreachable\x10\x00\x12\n\n\x06Paused\x10\x01\x12\n\n\x06Broken\x10\x02\x12\x0e\n\nReindexing\x10\x03\x1a\x04\xc0\xb5\x18\x01B\x16\xa2\x02\x13LocalFSDeviceAnchorb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.local_filesystem.device_anchor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\x13LocalFSDeviceAnchor'
    _globals['_DEVICEANCHORINACTIVEREASON']._loaded_options = None
    _globals['_DEVICEANCHORINACTIVEREASON']._serialized_options = b'\xc0\xb5\x18\x01'
    _globals['_DEVICEANCHORTARGETFLAGS'].fields_by_name['bits']._loaded_options = None
    _globals['_DEVICEANCHORTARGETFLAGS'].fields_by_name['bits']._serialized_options = b'\xa2\xb5\x18\x07[u8; 1]'
    _globals['_DEVICEANCHORDETAILS'].fields_by_name['target_fileid']._loaded_options = None
    _globals['_DEVICEANCHORDETAILS'].fields_by_name['target_fileid']._serialized_options = b'\xa2\xb5\x18+::std::option::Option<::sync_types::FileId>'
    _globals['_DEVICEANCHORDETAILS'].fields_by_name['target_flags']._loaded_options = None
    _globals['_DEVICEANCHORDETAILS'].fields_by_name['target_flags']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DEVICEANCHORSTATUS'].oneofs_by_name['status']._loaded_options = None
    _globals['_DEVICEANCHORSTATUS'].oneofs_by_name['status']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_DEVICEANCHORINACTIVEREASON']._serialized_start = 514
    _globals['_DEVICEANCHORINACTIVEREASON']._serialized_end = 605
    _globals['_DEVICEANCHORTARGETFLAGS']._serialized_start = 109
    _globals['_DEVICEANCHORTARGETFLAGS']._serialized_end = 161
    _globals['_DEVICEANCHORDETAILS']._serialized_start = 164
    _globals['_DEVICEANCHORDETAILS']._serialized_end = 350
    _globals['_DEVICEANCHORSTATUS']._serialized_start = 353
    _globals['_DEVICEANCHORSTATUS']._serialized_end = 512
    return None
