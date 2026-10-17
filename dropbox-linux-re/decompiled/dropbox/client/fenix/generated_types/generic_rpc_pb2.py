# Source Generated with Decompyle++
# File: generic_rpc_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'generic_rpc.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from  import shared_pb2 as shared__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11generic_rpc.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0cshared.proto"\xd9\x01\n\x11GenericRpcRequest\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12\x11\n\targs_json\x18\x03 \x01(\t\x126\n\x0cmessage_type\x18\x04 \x01(\x0e2 .dropbox.meta_engine.MessageType\x12:\n\x07account\x18\x05 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount\x12\x12\n\nmessage_id\x18\x06 \x01(\t"N\n\x12GenericRpcResponse\x12\x17\n\rresponse_json\x18\x01 \x01(\tH\x00\x12\x17\n\rerror_message\x18\x03 \x01(\tH\x00B\x06\n\x04body*B\n\x0bMessageType\x12\n\n\x06SIGNAL\x10\x00\x12\x0e\n\nINVOCATION\x10\x01\x12\x17\n\x13INVOCATION_RESPONSE\x10\x022\xc3\x01\n\rGenericRpcApi\x12^\n\x0bExecuteCall\x12&.dropbox.meta_engine.GenericRpcRequest\x1a\'.dropbox.meta_engine.GenericRpcResponse\x12R\n\x0eGetEventStream\x12\x16.google.protobuf.Empty\x1a&.dropbox.meta_engine.GenericRpcRequest0\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generic_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_MESSAGETYPE']._serialized_start = 385
    _globals['_MESSAGETYPE']._serialized_end = 451
    _globals['_GENERICRPCREQUEST']._serialized_start = 86
    _globals['_GENERICRPCREQUEST']._serialized_end = 303
    _globals['_GENERICRPCRESPONSE']._serialized_start = 305
    _globals['_GENERICRPCRESPONSE']._serialized_end = 383
    _globals['_GENERICRPCAPI']._serialized_start = 454
    _globals['_GENERICRPCAPI']._serialized_end = 649
    return None
