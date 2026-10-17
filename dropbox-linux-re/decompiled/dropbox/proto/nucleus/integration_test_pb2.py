# Source Generated with Decompyle++
# File: integration_test_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/integration_test.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
from dropbox.proto.sync_frontend import context_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_context__pb2
from dropbox.proto.sync_frontend.debug import rpc_pb2 as dropbox_dot_proto_dot_sync__frontend_dot_debug_dot_rpc__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,dropbox/proto/nucleus/integration_test.proto\x12\x07nucleus\x1a#dropbox/proto/rust/extensions.proto\x1a)dropbox/proto/sync_frontend/context.proto\x1a+dropbox/proto/sync_frontend/debug/rpc.proto"\xf4\x02\n\x19DevboxIntegrationTestArgs\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x10\n\x08build_no\x18\x03 \x01(\t\x12\x1c\n\x14sync_engine_build_no\x18\x04 \x01(\t\x12:\n\x08new_host\x18\x05 \x01(\x0b2&.sync_frontend_dbg.RegisterHostRequestH\x00\x12@\n\rexisting_host\x18\x06 \x01(\x0b2\'.sync_frontend_dbg.RegisterHostResponseH\x00\x12\x16\n\x0eenable_tracing\x18\x07 \x01(\x08\x12B\n\x13metaserver_run_type\x18\x08 \x01(\x0e2%.sync_frontend.RequestContext.RunType\x12\x1a\n\x12enable_apiv2_oauth\x18\t \x01(\x08B\x15\n\rregister_host\x12\x04\x88\xb5\x18\x00B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.integration_test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_DEVBOXINTEGRATIONTESTARGS'].oneofs_by_name['register_host']._loaded_options = None
    _globals['_DEVBOXINTEGRATIONTESTARGS'].oneofs_by_name['register_host']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_DEVBOXINTEGRATIONTESTARGS']._serialized_start = 183
    _globals['_DEVBOXINTEGRATIONTESTARGS']._serialized_end = 555
    return None
