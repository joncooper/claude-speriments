# Source Generated with Decompyle++
# File: sync_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/isotope_server/sync.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'dropbox/proto/isotope_server/sync.proto\x12\x0eisotope_server\x1a#dropbox/proto/rust/extensions.proto")\n\x15IsotopeRootIdentifier\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\xc0\xb5\x18\x00"\xca\x01\n\x15IsotopeClientLocation\x12P\n\x10user_device_path\x18\x01 \x01(\x0b24.isotope_server.IsotopeClientLocation.UserDevicePathH\x00\x1aO\n\x0eUserDevicePath\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x13\n\x0bclient_path\x18\x03 \x01(\t:\x04\xb0\xb5\x18\x01:\x04\xb0\xb5\x18\x01B\x08\n\x06target*7\n\x0fIsotopeSyncMode\x12\x0b\n\x07INVALID\x10\x00\x12\x17\n\x13BACKUP_TWO_WAY_SYNC\x10\x01B\x1eZ\x1cdropbox/proto/isotope_serverb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.isotope_server.sync_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1cdropbox/proto/isotope_server'
    _globals['_ISOTOPEROOTIDENTIFIER'].fields_by_name['id']._loaded_options = None
    _globals['_ISOTOPEROOTIDENTIFIER'].fields_by_name['id']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_ISOTOPECLIENTLOCATION_USERDEVICEPATH']._loaded_options = None
    _globals['_ISOTOPECLIENTLOCATION_USERDEVICEPATH']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_ISOTOPECLIENTLOCATION']._loaded_options = None
    _globals['_ISOTOPECLIENTLOCATION']._serialized_options = b'\xb0\xb5\x18\x01'
    _globals['_ISOTOPESYNCMODE']._serialized_start = 344
    _globals['_ISOTOPESYNCMODE']._serialized_end = 399
    _globals['_ISOTOPEROOTIDENTIFIER']._serialized_start = 96
    _globals['_ISOTOPEROOTIDENTIFIER']._serialized_end = 137
    _globals['_ISOTOPECLIENTLOCATION']._serialized_start = 140
    _globals['_ISOTOPECLIENTLOCATION']._serialized_end = 342
    _globals['_ISOTOPECLIENTLOCATION_USERDEVICEPATH']._serialized_start = 247
    _globals['_ISOTOPECLIENTLOCATION_USERDEVICEPATH']._serialized_end = 326
    return None
