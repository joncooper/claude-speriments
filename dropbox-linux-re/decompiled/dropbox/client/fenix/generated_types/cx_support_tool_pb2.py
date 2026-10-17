# Source Generated with Decompyle++
# File: cx_support_tool_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'cx_support_tool.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.nucleus import app_service_pb2 as dropbox_dot_proto_dot_nucleus_dot_app__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15cx_support_tool.proto\x12\x13dropbox.meta_engine\x1a\'dropbox/proto/nucleus/app_service.proto\x1a\x1bgoogle/protobuf/empty.proto"N\n\x19FetchEngineDebugInfoReply\x121\n\x15component_debug_infos\x18\x01 \x03(\x0b2\x12.nucleus.DebugInfo2r\n\x10CxSupportToolApi\x12^\n\x14FetchEngineDebugInfo\x12\x16.google.protobuf.Empty\x1a..dropbox.meta_engine.FetchEngineDebugInfoReplyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cx_support_tool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_FETCHENGINEDEBUGINFOREPLY']._serialized_start = 116
    _globals['_FETCHENGINEDEBUGINFOREPLY']._serialized_end = 194
    _globals['_CXSUPPORTTOOLAPI']._serialized_start = 196
    _globals['_CXSUPPORTTOOLAPI']._serialized_end = 310
    return None
