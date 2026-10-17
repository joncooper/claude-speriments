# Source Generated with Decompyle++
# File: feature_configs_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/feature_configs.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dropbox/proto/nucleus/feature_configs.proto\x12\x07nucleus\x1a#dropbox/proto/rust/extensions.proto"8\n\x0fStormcrowConfig\x12\x14\n\x0cfeature_name\x18\x01 \x01(\t\x12\x0f\n\x07variant\x18\x02 \x01(\t"U\n\x13ServerFeatureConfig\x12-\n\tstormcrow\x18\x01 \x01(\x0b2\x18.nucleus.StormcrowConfigH\x00B\x0f\n\x07feature\x12\x04\x88\xb5\x18\x00"T\n\x14ServerFeatureConfigs\x12<\n\x16server_feature_configs\x18\x02 \x03(\x0b2\x1c.nucleus.ServerFeatureConfigB\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.feature_configs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_SERVERFEATURECONFIG'].oneofs_by_name['feature']._loaded_options = None
    _globals['_SERVERFEATURECONFIG'].oneofs_by_name['feature']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_STORMCROWCONFIG']._serialized_start = 93
    _globals['_STORMCROWCONFIG']._serialized_end = 149
    _globals['_SERVERFEATURECONFIG']._serialized_start = 151
    _globals['_SERVERFEATURECONFIG']._serialized_end = 236
    _globals['_SERVERFEATURECONFIGS']._serialized_start = 238
    _globals['_SERVERFEATURECONFIGS']._serialized_end = 322
    return None
