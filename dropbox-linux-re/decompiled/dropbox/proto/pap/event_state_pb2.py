# Source Generated with Decompyle++
# File: event_state_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/pap/event_state.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.api_proxy.api_v2 import api_v2_pb2 as dropbox_dot_proto_dot_api__proxy_dot_api__v2_dot_api__v2__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#dropbox/proto/pap/event_state.proto\x12\x03pap\x1a+dropbox/proto/api_proxy/api_v2/api_v2.proto*e\n\nEventState\x12\x17\n\x13UNKNOWN_EVENT_STATE\x10\x00\x12\t\n\x05START\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x12\n\n\x06FAILED\x10\x03\x12\x0c\n\x08CANCELED\x10\x04\x12\x0c\n\x08REJECTED\x10\x05B,Z\x11dropbox/proto/pap\x80\xa7\x1d\x01\x8a\xa7\x1d\x11pap_event_loggingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.pap.event_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x11dropbox/proto/pap\x80\xa7\x1d\x01\x8a\xa7\x1d\x11pap_event_logging'
    _globals['_EVENTSTATE']._serialized_start = 89
    _globals['_EVENTSTATE']._serialized_end = 190
    return None
