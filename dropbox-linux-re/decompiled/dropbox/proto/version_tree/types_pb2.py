# Source Generated with Decompyle++
# File: types_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/version_tree/types.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.api_proxy.api_v2 import api_v2_pb2 as dropbox_dot_proto_dot_api__proxy_dot_api__v2_dot_api__v2__pb2
from dropbox.proto.godbx import extensions_pb2 as dropbox_dot_proto_dot_godbx_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&dropbox/proto/version_tree/types.proto\x12\x0cversion_tree\x1a+dropbox/proto/api_proxy/api_v2/api_v2.proto\x1a$dropbox/proto/godbx/extensions.proto"!\n\x03Hlc\x12\x13\n\x0bunix_micros\x18\x01 \x01(\x06:\x05\xc8\xb9\x8e\x01\x01"\x19\n\x03Oid\x12\x0b\n\x03val\x18\x01 \x01(\x06:\x05\xc8\xb9\x8e\x01\x01"\x19\n\x03Sid\x12\x0b\n\x03val\x18\x01 \x01(\x06:\x05\xc8\xb9\x8e\x01\x01BR\n\x1ecom.dropbox.proto.version_treeP\x01Z\x1adropbox/proto/version_tree\x80\xa7\x1d\x01\x8a\xa7\x1d\x0cversion_treeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.version_tree.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.dropbox.proto.version_treeP\x01Z\x1adropbox/proto/version_tree\x80\xa7\x1d\x01\x8a\xa7\x1d\x0cversion_tree'
    _globals['_HLC']._loaded_options = None
    _globals['_HLC']._serialized_options = b'\xc8\xb9\x8e\x01\x01'
    _globals['_OID']._loaded_options = None
    _globals['_OID']._serialized_options = b'\xc8\xb9\x8e\x01\x01'
    _globals['_SID']._loaded_options = None
    _globals['_SID']._serialized_options = b'\xc8\xb9\x8e\x01\x01'
    _globals['_HLC']._serialized_start = 139
    _globals['_HLC']._serialized_end = 172
    _globals['_OID']._serialized_start = 174
    _globals['_OID']._serialized_end = 199
    _globals['_SID']._serialized_start = 201
    _globals['_SID']._serialized_end = 226
    return None
