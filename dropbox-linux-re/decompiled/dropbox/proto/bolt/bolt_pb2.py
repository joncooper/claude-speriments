# Source Generated with Decompyle++
# File: bolt_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/bolt/bolt.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.sync_frontend import bolt_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_bolt__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ddropbox/proto/bolt/bolt.proto\x12\x04bolt\x1a&dropbox/proto/sync_frontend/bolt.proto"E\n\x12SubscribeToBoltReq\x12/\n\x06tokens\x18\x01 \x03(\x0b2\x1f.sync_frontend.BoltChannelToken"s\n\x14SubscribeToBoltReply\x120\n\x07updated\x18\x01 \x03(\x0b2\x1f.sync_frontend.BoltChannelToken\x12)\n\x07invalid\x18\x02 \x03(\x0b2\x18.sync_frontend.ChannelIdB\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.bolt.bolt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_SUBSCRIBETOBOLTREQ']._serialized_start = 79
    _globals['_SUBSCRIBETOBOLTREQ']._serialized_end = 148
    _globals['_SUBSCRIBETOBOLTREPLY']._serialized_start = 150
    _globals['_SUBSCRIBETOBOLTREPLY']._serialized_end = 265
    return None
