# Source Generated with Decompyle++
# File: routing_config_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/rpc_core/routing_config.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from dropbox.proto.rpc_core import common_pb2 as dropbox_dot_proto_dot_rpc__core_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dropbox/proto/rpc_core/routing_config.proto\x12\x08rpc_core\x1a google/protobuf/descriptor.proto\x1a#dropbox/proto/rpc_core/common.proto"\xb9\x05\n\x1aPublicRoutingConfiguration\x12\x11\n\thostnames\x18\x01 \x03(\t\x12\x1c\n\x14additional_hostnames\x18\x12 \x03(\t\x12\x12\n\x08upstream\x18\x02 \x01(\tH\x00\x12-\n\x0ckiev_backend\x18\x03 \x01(\x0b2\x15.rpc_core.KievBackendH\x00\x121\n\x0etiered_backend\x18\x04 \x01(\x0b2\x17.rpc_core.TieredBackendH\x00\x12/\n\ratlas_backend\x18\x11 \x01(\x0e2\x16.rpc_core.AtlasBackendH\x00\x12\x17\n\rtitan_backend\x18\x10 \x01(\tH\x00\x127\n\x11robinhood_backend\x18\x07 \x01(\x0b2\x1a.rpc_core.RobinhoodBackendH\x00\x12\x13\n\x0bdescription\x18\x08 \x01(\t\x12-\n\nrate_limit\x18\t \x01(\x0b2\x19.rpc_core.RateLimitConfig\x12\x0f\n\x07timeout\x18\n \x01(\r\x121\n\x0fextra_upstreams\x18\x13 \x03(\x0b2\x18.rpc_core.ExtraUpstreams\x12\x17\n\x0fno_grpc_support\x18\x0b \x01(\x08\x12\x1b\n\x13courier_permissions\x18\x0c \x03(\t\x12"\n\x1askip_automatic_permissions\x18\r \x01(\x08\x12,\n\rtraffic_tiers\x18\x0f \x03(\x0e2\x15.rpc_core.TrafficTier\x12\x16\n\x0chttp_service\x18\x14 \x01(\x08H\x01\x12\x17\n\rapiv2_service\x18\x15 \x01(\x08H\x01B\x0e\n\x0cbackend_typeB\x0e\n\x0cextra_configJ\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x0e\x10\x0f"\xf6\x03\n\rTieredBackend\x12\x17\n\rlive_upstream\x18\x01 \x01(\tH\x00\x124\n\x12live_atlas_backend\x18\x10 \x01(\x0e2\x16.rpc_core.AtlasBackendH\x00\x12\x1c\n\x12live_titan_backend\x18\x0c \x01(\tH\x00\x12<\n\x16live_robinhood_backend\x18\x04 \x01(\x0b2\x1a.rpc_core.RobinhoodBackendH\x00\x12\x18\n\x0ebatch_upstream\x18\x05 \x01(\tH\x01\x125\n\x13batch_atlas_backend\x18\x11 \x01(\x0e2\x16.rpc_core.AtlasBackendH\x01\x12\x1d\n\x13batch_titan_backend\x18\x0f \x01(\tH\x01\x12=\n\x17batch_robinhood_backend\x18\x08 \x01(\x0b2\x1a.rpc_core.RobinhoodBackendH\x01\x120\n\x11http_traffic_tier\x18\t \x01(\x0e2\x15.rpc_core.TrafficTierB\x13\n\x11live_backend_typeB\x14\n\x12batch_backend_typeJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0cJ\x04\x08\r\x10\x0eJ\x04\x08\x0e\x10\x0f"\xc4\x04\n\x0bKievBackend\x12\x11\n\tkiev_rule\x18\x01 \x01(\t\x12\x17\n\x0fstage_kiev_rule\x18\x02 \x01(\t\x12\x1a\n\x10enabled_upstream\x18\x03 \x01(\tH\x00\x12B\n\x15enabled_atlas_backend\x18\x0b \x01(\x0b2!.rpc_core.AtlasBackendWithServiceH\x00\x12B\n\x15enabled_titan_backend\x18\x05 \x01(\x0b2!.rpc_core.TitanBackendWithServiceH\x00\x12?\n\x19enabled_robinhood_backend\x18\x06 \x01(\x0b2\x1a.rpc_core.RobinhoodBackendH\x00\x12\x1b\n\x11disabled_upstream\x18\x07 \x01(\tH\x01\x12C\n\x16disabled_atlas_backend\x18\x0c \x01(\x0b2!.rpc_core.AtlasBackendWithServiceH\x01\x12C\n\x16disabled_titan_backend\x18\t \x01(\x0b2!.rpc_core.TitanBackendWithServiceH\x01\x12@\n\x1adisabled_robinhood_backend\x18\n \x01(\x0b2\x1a.rpc_core.RobinhoodBackendH\x01B\x16\n\x14enabled_backend_typeB\x17\n\x15disabled_backend_typeJ\x04\x08\x04\x10\x05J\x04\x08\x08\x10\t"\x8b\x01\n\x17AtlasBackendWithService\x12,\n\x0catlasservlet\x18\x03 \x01(\x0e2\x16.rpc_core.AtlasBackend\x12+\n\x0ctraffic_tier\x18\x04 \x01(\x0e2\x15.rpc_core.TrafficTier\x12\x0f\n\x07service\x18\x02 \x01(\tJ\x04\x08\x01\x10\x02";\n\x17TitanBackendWithService\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t"\x8a\x02\n\x10RobinhoodBackend\x12\x17\n\x0fserver_identity\x18\x01 \x01(\t\x12\x1a\n\x10robinhood_target\x18\x02 \x01(\tH\x00\x12\x15\n\x0bserver_name\x18\x03 \x01(\tH\x00\x125\n\x08protocol\x18\x04 \x01(\x0e2#.rpc_core.RobinhoodBackend.Protocol\x12#\n\x1bqueue_config_per_host_limit\x18\x05 \x01(\x05\x12\x14\n\x0csusanin_cell\x18\x06 \x01(\t")\n\x08Protocol\x12\x08\n\x04GRPC\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTP2\x10\x02B\r\n\x0btarget_type"\x8a\x01\n\x0eExtraUpstreams\x12\x10\n\x08upstream\x18\x01 \x01(\t\x121\n\x07headers\x18\x02 \x03(\x0b2 .rpc_core.ExtraUpstreams.Headers\x1a3\n\x07Headers\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12exact_string_match\x18\x02 \x01(\t*B\n\x0bTrafficTier\x12\x08\n\x04LIVE\x10\x00\x12\t\n\x05BATCH\x10\x01\x12\x10\n\x0cEXPERIMENTAL\x10\x02\x12\x0c\n\x08TESTONLY\x10\x03*Z\n\x0cAtlasBackend\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07ASYNCIO\x10\x01\x12\x11\n\rMULTITHREADED\x10\x02\x12\x18\n\x14LEGACY_MULTITHREADED\x10\x03\x12\x06\n\x02GO\x10\x04B6\n\x1acom.dropbox.proto.rpc_coreP\x01Z\x16dropbox/proto/rpc_coreb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.rpc_core.routing_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.dropbox.proto.rpc_coreP\x01Z\x16dropbox/proto/rpc_core'
    _globals['_TRAFFICTIER']._serialized_start = 2529
    _globals['_TRAFFICTIER']._serialized_end = 2595
    _globals['_ATLASBACKEND']._serialized_start = 2597
    _globals['_ATLASBACKEND']._serialized_end = 2687
    _globals['_PUBLICROUTINGCONFIGURATION']._serialized_start = 129
    _globals['_PUBLICROUTINGCONFIGURATION']._serialized_end = 826
    _globals['_TIEREDBACKEND']._serialized_start = 829
    _globals['_TIEREDBACKEND']._serialized_end = 1331
    _globals['_KIEVBACKEND']._serialized_start = 1334
    _globals['_KIEVBACKEND']._serialized_end = 1914
    _globals['_ATLASBACKENDWITHSERVICE']._serialized_start = 1917
    _globals['_ATLASBACKENDWITHSERVICE']._serialized_end = 2056
    _globals['_TITANBACKENDWITHSERVICE']._serialized_start = 2058
    _globals['_TITANBACKENDWITHSERVICE']._serialized_end = 2117
    _globals['_ROBINHOODBACKEND']._serialized_start = 2120
    _globals['_ROBINHOODBACKEND']._serialized_end = 2386
    _globals['_ROBINHOODBACKEND_PROTOCOL']._serialized_start = 2330
    _globals['_ROBINHOODBACKEND_PROTOCOL']._serialized_end = 2371
    _globals['_EXTRAUPSTREAMS']._serialized_start = 2389
    _globals['_EXTRAUPSTREAMS']._serialized_end = 2527
    _globals['_EXTRAUPSTREAMS_HEADERS']._serialized_start = 2476
    _globals['_EXTRAUPSTREAMS_HEADERS']._serialized_end = 2527
    return None
