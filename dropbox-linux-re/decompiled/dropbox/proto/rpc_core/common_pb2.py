# Source Generated with Decompyle++
# File: common_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/rpc_core/common.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#dropbox/proto/rpc_core/common.proto\x12\x08rpc_core"x\n\x0fRateLimitConfig\x12\r\n\x05quota\x18\x01 \x01(\r\x12\x18\n\x10limit_duration_s\x18\x02 \x01(\r\x12+\n\nlimit_type\x18\x03 \x01(\x0e2\x17.rpc_core.RateLimitType\x12\x0f\n\x07dry_run\x18\x04 \x01(\x08"g\n\x0cAccessConfig\x12\x1c\n\x14additional_hostnames\x18\x01 \x03(\t\x12\x11\n\thostnames\x18\x02 \x03(\t\x12\x15\n\rsupports_grpc\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\r"\x8b\x01\n\x18ActiveUserSelectorConfig\x12\x12\n\nrpc_method\x18\x01 \x01(\t\x12\x13\n\x0brpc_service\x18\x02 \x01(\t\x12\x12\n\ntimeout_ms\x18\x03 \x01(\r\x12\x1b\n\x13buffer_request_body\x18\x04 \x01(\x08\x12\x15\n\rfallback_only\x18\x05 \x01(\x08*M\n\rRateLimitType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08ROUTE_IP\x10\x01\x12\x0e\n\nROUTE_PATH\x10\x02\x12\x11\n\rROUTE_PATH_IP\x10\x03B6\n\x1acom.dropbox.proto.rpc_coreP\x01Z\x16dropbox/proto/rpc_coreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.rpc_core.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.dropbox.proto.rpc_coreP\x01Z\x16dropbox/proto/rpc_core'
    _globals['_RATELIMITTYPE']._serialized_start = 418
    _globals['_RATELIMITTYPE']._serialized_end = 495
    _globals['_RATELIMITCONFIG']._serialized_start = 49
    _globals['_RATELIMITCONFIG']._serialized_end = 169
    _globals['_ACCESSCONFIG']._serialized_start = 171
    _globals['_ACCESSCONFIG']._serialized_end = 274
    _globals['_ACTIVEUSERSELECTORCONFIG']._serialized_start = 277
    _globals['_ACTIVEUSERSELECTORCONFIG']._serialized_end = 416
    return None
