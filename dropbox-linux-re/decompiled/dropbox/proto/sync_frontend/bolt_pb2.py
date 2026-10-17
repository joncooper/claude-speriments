# Source Generated with Decompyle++
# File: bolt_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync_frontend/bolt.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&dropbox/proto/sync_frontend/bolt.proto\x12\rsync_frontend\x1a#dropbox/proto/rust/extensions.proto".\n\tChannelId\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x12\x11\n\tunique_id\x18\x02 \x01(\t"g\n\x10BoltChannelToken\x122\n\nchannel_id\x18\x01 \x01(\x0b2\x18.sync_frontend.ChannelIdB\x04\xc0\xb5\x18\x00\x12\x10\n\x08revision\x18\x02 \x01(\x04\x12\r\n\x05token\x18\x03 \x01(\tB\x1dZ\x1bdropbox/proto/sync_frontendb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync_frontend.bolt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1bdropbox/proto/sync_frontend'
    _globals['_BOLTCHANNELTOKEN'].fields_by_name['channel_id']._loaded_options = None
    _globals['_BOLTCHANNELTOKEN'].fields_by_name['channel_id']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_CHANNELID']._serialized_start = 94
    _globals['_CHANNELID']._serialized_end = 140
    _globals['_BOLTCHANNELTOKEN']._serialized_start = 142
    _globals['_BOLTCHANNELTOKEN']._serialized_end = 245
    return None
