# Source Generated with Decompyle++
# File: throttler_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/throttler/throttler.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'dropbox/proto/throttler/throttler.proto\x12\tthrottler\x1a#dropbox/proto/rust/extensions.proto\x1a\x1bgoogle/protobuf/empty.proto"#\n\x14FlatThrottleSettings\x12\x0b\n\x03bps\x18\x01 \x01(\x04"\xb8\x01\n\x0cThrottleMode\x12-\n\x0bunthrottled\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x120\n\x0eauto_throttled\x18\x02 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x129\n\x0eflat_throttled\x18\x03 \x01(\x0b2\x1f.throttler.FlatThrottleSettingsH\x00B\x0c\n\x04mode\x12\x04\x88\xb5\x18\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.throttler.throttler_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_THROTTLEMODE'].oneofs_by_name['mode']._loaded_options = None
    _globals['_THROTTLEMODE'].oneofs_by_name['mode']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_FLATTHROTTLESETTINGS']._serialized_start = 120
    _globals['_FLATTHROTTLESETTINGS']._serialized_end = 155
    _globals['_THROTTLEMODE']._serialized_start = 158
    _globals['_THROTTLEMODE']._serialized_end = 342
    return None
