# Source Generated with Decompyle++
# File: account_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/apex/account.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n dropbox/proto/apex/account.proto\x12\tstormcrow"-\n\x08DeviceId\x12\x0f\n\x07host_id\x18\x01 \x01(\x04\x12\x10\n\x08host_key\x18\x02 \x01(\t"V\n\x07Account\x12&\n\tdevice_id\x18\x01 \x01(\x0b2\x13.stormcrow.DeviceId\x12\x0f\n\x07user_id\x18\x02 \x01(\x04\x12\x12\n\naccount_id\x18\x03 \x01(\tB\x11\xa2\x02\x0eDropboxAccountb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.apex.account_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\x0eDropboxAccount'
    _globals['_DEVICEID']._serialized_start = 47
    _globals['_DEVICEID']._serialized_end = 92
    _globals['_ACCOUNT']._serialized_start = 94
    _globals['_ACCOUNT']._serialized_end = 180
    return None
