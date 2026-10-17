# Source Generated with Decompyle++
# File: route_extensions_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/rpc_core/route_extensions.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from dropbox.proto.rpc_core import common_pb2 as dropbox_dot_proto_dot_rpc__core_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-dropbox/proto/rpc_core/route_extensions.proto\x12\x08rpc_core\x1a google/protobuf/descriptor.proto\x1a#dropbox/proto/rpc_core/common.proto"\x88\x05\n\x12PublicMethodConfig\x12\r\n\x03get\x18\x01 \x01(\tH\x00\x12\r\n\x03put\x18\x02 \x01(\tH\x00\x12\x0e\n\x04post\x18\x03 \x01(\tH\x00\x12\x10\n\x06delete\x18\x04 \x01(\tH\x00\x12\x0f\n\x05patch\x18\x05 \x01(\tH\x00\x12\x11\n\x07options\x18\x06 \x01(\tH\x00\x12\x0c\n\x04i18n\x18\x07 \x01(\x08\x12\x13\n\x0bdescription\x18\x08 \x01(\t\x12\x0c\n\x04body\x18\t \x01(\t\x12$\n\x1cenable_deprecated_ajax_stubs\x18\n \x01(\x08\x12)\n!migrated_to_different_rpc_service\x18\x0b \x01(\x08\x12-\n\nrate_limit\x18\x0c \x01(\x0b2\x19.rpc_core.RateLimitConfig\x12-\n\raccess_config\x18\r \x01(\x0b2\x16.rpc_core.AccessConfig\x12@\n\x14active_user_selector\x18\x0e \x01(\x0b2".rpc_core.ActiveUserSelectorConfig\x129\n\x13additional_bindings\x18e \x03(\x0b2\x1c.rpc_core.PublicMethodConfig\x12"\n\x04cors\x18\x11 \x01(\x0b2\x14.rpc_core.CORSConfig\x12\x1c\n\x14include_empty_method\x18\x0f \x01(\x08\x12&\n\x05apiv1\x18\x10 \x01(\x0b2\x15.rpc_core.ApiV1ConfigH\x01\x12&\n\x05apiv2\x18\x13 \x01(\x0b2\x15.rpc_core.ApiV2ConfigH\x01B\t\n\x07patternB\x0e\n\x0cextra_configJ\x04\x08\x12\x10\x13"]\n\x0bApiV1Config\x12\x18\n\x10version_at_least\x18\x01 \x01(\x03\x12\x17\n\x0fversion_at_most\x18\x02 \x01(\x03\x12\x1b\n\x13omit_options_routes\x18\x03 \x01(\x08"8\n\x0bApiV2Config\x12)\n\x05route\x18\x01 \x01(\x0b2\x1a.rpc_core.ApiV2RouteConfig"0\n\x10ApiV2RouteConfig\x12\x1c\n\x14use_service_upstream\x18\x01 \x01(\x08"\x87\x01\n\nCORSConfig\x12\x19\n\x11allow_credentials\x18\x01 \x01(\x08\x12\x15\n\rallow_headers\x18\x02 \x01(\t\x12\x15\n\rallow_methods\x18\x03 \x01(\t\x12\x18\n\x10cors_allow_regex\x18\x04 \x01(\t\x12\x16\n\x0eexpose_headers\x18\x05 \x01(\tB6\n\x1acom.dropbox.proto.rpc_coreP\x01Z\x16dropbox/proto/rpc_coreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.rpc_core.route_extensions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.dropbox.proto.rpc_coreP\x01Z\x16dropbox/proto/rpc_core'
    _globals['_PUBLICMETHODCONFIG']._serialized_start = 131
    _globals['_PUBLICMETHODCONFIG']._serialized_end = 779
    _globals['_APIV1CONFIG']._serialized_start = 781
    _globals['_APIV1CONFIG']._serialized_end = 874
    _globals['_APIV2CONFIG']._serialized_start = 876
    _globals['_APIV2CONFIG']._serialized_end = 932
    _globals['_APIV2ROUTECONFIG']._serialized_start = 934
    _globals['_APIV2ROUTECONFIG']._serialized_end = 982
    _globals['_CORSCONFIG']._serialized_start = 985
    _globals['_CORSCONFIG']._serialized_end = 1120
    return None
