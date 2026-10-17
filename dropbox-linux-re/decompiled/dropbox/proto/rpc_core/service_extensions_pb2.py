# Source Generated with Decompyle++
# File: service_extensions_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/rpc_core/service_extensions.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from dropbox.proto.rpc_core import route_extensions_pb2 as dropbox_dot_proto_dot_rpc__core_dot_route__extensions__pb2
from dropbox.proto.rpc_core import routing_config_pb2 as dropbox_dot_proto_dot_rpc__core_dot_routing__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/dropbox/proto/rpc_core/service_extensions.proto\x12\x08rpc_core\x1a google/protobuf/descriptor.proto\x1a-dropbox/proto/rpc_core/route_extensions.proto\x1a+dropbox/proto/rpc_core/routing_config.proto"L\n\x0eServiceOptions\x12\x1d\n\x15default_error_package\x18\x01 \x01(\t\x12\x1b\n\x13extra_error_package\x18\x02 \x03(\t:^\n6services_allow_no_deadline_promise_it_is_3rdparty_file\x12\x1c.google.protobuf.FileOptions\x18\xd9\x86\x03 \x01(\x08:1\n\trpc_error\x12\x1c.google.protobuf.EnumOptions\x18\xd6\x86\x03 \x01(\x08:6\n\tgrpc_code\x12!.google.protobuf.EnumValueOptions\x18\xd7\x86\x03 \x01(\t:B\n\x17dbx_legacy_service_name\x12\x1f.google.protobuf.ServiceOptions\x18\xd0\x86\x03 \x01(\t:F\n\x1bservice_default_deadline_ms\x12\x1f.google.protobuf.ServiceOptions\x18\xd2\x86\x03 \x01(\x05:B\n\x17service_max_deadline_ms\x12\x1f.google.protobuf.ServiceOptions\x18\xdc\x86\x03 \x01(\x05:B\n\x17service_min_deadline_ms\x12\x1f.google.protobuf.ServiceOptions\x18\xde\x86\x03 \x01(\x05:X\n\x13dbx_service_options\x12\x1f.google.protobuf.ServiceOptions\x18\xda\x86\x03 \x01(\x0b2\x18.rpc_core.ServiceOptions:F\n\x1bdbx_py_server_use_iterators\x12\x1f.google.protobuf.ServiceOptions\x18\xe0\x86\x03 \x01(\x08:?\n\x14method_py_snake_case\x12\x1f.google.protobuf.ServiceOptions\x18\xe1\x86\x03 \x01(\x08:f\n\x15service_configuration\x12\x1f.google.protobuf.ServiceOptions\x18\xe2\x86\x03 \x01(\x0b2$.rpc_core.PublicRoutingConfiguration:@\n\x15alt_rpc_service_names\x12\x1f.google.protobuf.ServiceOptions\x18\xe3\x86\x03 \x03(\t:@\n\x16dbx_legacy_method_name\x12\x1e.google.protobuf.MethodOptions\x18\xd1\x86\x03 \x01(\t:D\n\x1amethod_default_deadline_ms\x12\x1e.google.protobuf.MethodOptions\x18\xd3\x86\x03 \x01(\x05:@\n\x16method_max_deadline_ms\x12\x1e.google.protobuf.MethodOptions\x18\xdd\x86\x03 \x01(\x05:@\n\x16method_min_deadline_ms\x12\x1e.google.protobuf.MethodOptions\x18\xdf\x86\x03 \x01(\x05:K\n!dbx_py_return_raw_response_string\x12\x1e.google.protobuf.MethodOptions\x18\xd4\x86\x03 \x01(\x08:<\n\x12method_no_deadline\x12\x1e.google.protobuf.MethodOptions\x18\xd5\x86\x03 \x01(\x08:\x89\x01\n_dbx_unary_unary_slow_start_may_deadlock_never_use_it_unless_explicitly_allowed_by_services_team\x12\x1e.google.protobuf.MethodOptions\x18\xd8\x86\x03 \x01(\x08:\x83\x01\nYdbx_unary_unary_slow_start_server_never_use_it_unless_explicitly_allowed_by_services_team\x12\x1e.google.protobuf.MethodOptions\x18\xdb\x86\x03 \x01(\x08:\\\n\x14method_configuration\x12\x1e.google.protobuf.MethodOptions\x18\xe4\x86\x03 \x01(\x0b2\x1c.rpc_core.PublicMethodConfigB6\n\x1acom.dropbox.proto.rpc_coreP\x01Z\x16dropbox/proto/rpc_coreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.rpc_core.service_extensions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.dropbox.proto.rpc_coreP\x01Z\x16dropbox/proto/rpc_core'
    _globals['_SERVICEOPTIONS']._serialized_start = 187
    _globals['_SERVICEOPTIONS']._serialized_end = 263
    return None
