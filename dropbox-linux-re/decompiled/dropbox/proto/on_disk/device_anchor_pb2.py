# Source Generated with Decompyle++
# File: device_anchor_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/on_disk/device_anchor.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dropbox/proto/on_disk/device_anchor.proto\x12\x07on_disk\x1a#dropbox/proto/rust/extensions.proto"\x1f\n\x0bPausedState\x12\n\n\x02ts\x18\x01 \x01(\x04:\x04\xb0\xb5\x18\x01"\x17\n\x0fReindexingState:\x04\xb0\xb5\x18\x01"(\n\x0eDeviceCapacity\x12\x10\n\x08capacity\x18\x01 \x01(\x04:\x04\xb0\xb5\x18\x01"S\n\x19DeviceIdVerificationAttrs\x120\n\x0fdevice_capacity\x18\x01 \x01(\x0b2\x17.on_disk.DeviceCapacity:\x04\xb0\xb5\x18\x01"\xa8\x02\n\x0eTargetMetadata\x12\x13\n\tdevice_id\x18\x01 \x01(\tH\x00\x12\x0f\n\x05inode\x18\x02 \x01(\x04H\x00\x12\x14\n\nlocal_path\x18\x03 \x01(\tH\x00\x12\x1c\n\x12backup_folder_path\x18\x07 \x01(\tH\x00\x12&\n\x06paused\x18\x04 \x01(\x0b2\x14.on_disk.PausedStateH\x01\x12.\n\nreindexing\x18\x06 \x01(\x0b2\x18.on_disk.ReindexingStateH\x01\x12E\n\x19device_verification_attrs\x18\x05 \x01(\x0b2".on_disk.DeviceIdVerificationAttrs:\x04\xb0\xb5\x18\x01B\x0e\n\x06target\x12\x04\x88\xb5\x18\x00B\x07\n\x05stateb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.on_disk.device_anchor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_PAUSEDSTATE']._loaded_options = None
    _globals['_PAUSEDSTATE']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_REINDEXINGSTATE']._loaded_options = None
    _globals['_REINDEXINGSTATE']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_DEVICECAPACITY']._loaded_options = None
    _globals['_DEVICECAPACITY']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_DEVICEIDVERIFICATIONATTRS']._loaded_options = None
    _globals['_DEVICEIDVERIFICATIONATTRS']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_TARGETMETADATA'].oneofs_by_name['target']._loaded_options = None
    _globals['_TARGETMETADATA'].oneofs_by_name['target']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_TARGETMETADATA']._loaded_options = None
    _globals['_TARGETMETADATA']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_PAUSEDSTATE']._serialized_start = 91
    _globals['_PAUSEDSTATE']._serialized_end = 122
    _globals['_REINDEXINGSTATE']._serialized_start = 124
    _globals['_REINDEXINGSTATE']._serialized_end = 147
    _globals['_DEVICECAPACITY']._serialized_start = 149
    _globals['_DEVICECAPACITY']._serialized_end = 189
    _globals['_DEVICEIDVERIFICATIONATTRS']._serialized_start = 191
    _globals['_DEVICEIDVERIFICATIONATTRS']._serialized_end = 274
    _globals['_TARGETMETADATA']._serialized_start = 277
    _globals['_TARGETMETADATA']._serialized_end = 573
    return None
