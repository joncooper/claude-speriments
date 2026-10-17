# Source Generated with Decompyle++
# File: network_state_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/network_state.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dropbox/proto/nucleus/network_state.proto\x12\x07nucleus"\xc3\x01\n\x0cNetworkState\x12/\n\x08failures\x18\x01 \x03(\x0b2\x1d.nucleus.NetworkState.Failure\x1a\x81\x01\n\x07Failure\x12(\n\x07service\x18\x01 \x01(\x0e2\x17.nucleus.NetworkService\x121\n\x0cfailure_kind\x18\x02 \x01(\x0e2\x1b.nucleus.NetworkFailureKind\x12\x19\n\x11failure_timestamp\x18\x03 \x01(\x04*g\n\x0eNetworkService\x12\x13\n\x0fUNKNOWN_SERVICE\x10\x00\x12\x10\n\x0cBLOCK_SERVER\x10\x01\x12\x11\n\rSYNC_FRONTEND\x10\x02\x12\x0f\n\x0bBOLT_SERVER\x10\x03\x12\n\n\x06API_V2\x10\x04*\xd2\x02\n\x12NetworkFailureKind\x12\x18\n\x14UNKNOWN_FAILURE_KIND\x10\x00\x12\x16\n\x12OTHER_FAILURE_KIND\x10\x01\x12\x0e\n\nCONNECTION\x10\x02\x12\x1e\n\x1aCLIENT_INITIATED_RECONNECT\x10\x03\x12\x0b\n\x07DROPBOX\x10\x04\x12\x15\n\x11DEPRECATED_CLIENT\x10\x05\x12\x19\n\x15NETWORK_CONFIGURATION\x10\x06\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x07\x12\x13\n\x0fUNAUTHENTICATED\x10\x08\x12\r\n\tTRANSIENT\x10\t\x12\x15\n\x11DEADLINE_EXCEEDED\x10\n\x12\x15\n\x11DENIED_PERMISSION\x10\x0b\x12\x13\n\x0fSYSTEM_RESOURCE\x10\x0c\x12\x1c\n\x18TRANSPORT_LAYER_SECURITY\x10\rB\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.network_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_NETWORKSERVICE']._serialized_start = 252
    _globals['_NETWORKSERVICE']._serialized_end = 355
    _globals['_NETWORKFAILUREKIND']._serialized_start = 358
    _globals['_NETWORKFAILUREKIND']._serialized_end = 696
    _globals['_NETWORKSTATE']._serialized_start = 55
    _globals['_NETWORKSTATE']._serialized_end = 250
    _globals['_NETWORKSTATE_FAILURE']._serialized_start = 121
    _globals['_NETWORKSTATE_FAILURE']._serialized_end = 250
    return None
