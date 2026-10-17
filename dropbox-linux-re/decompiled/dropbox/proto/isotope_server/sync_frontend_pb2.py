# Source Generated with Decompyle++
# File: sync_frontend_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/isotope_server/sync_frontend.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.isotope_server import sync_pb2 as dropbox_dot_proto_dot_isotope__server_dot_sync__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0dropbox/proto/isotope_server/sync_frontend.proto\x12\x0eisotope_server\x1a\'dropbox/proto/isotope_server/sync.proto"\xa1\x01\n\x15IsotopeRequestContext\x12>\n\x0fisotope_root_id\x18\x01 \x01(\x0b2%.isotope_server.IsotopeRootIdentifier\x12H\n\x11validation_fields\x18\x02 \x01(\x0b2-.isotope_server.IsotopeClientValidationFields"\x9b\x01\n\x1dIsotopeClientValidationFields\x12F\n\x17isotope_client_location\x18\x01 \x01(\x0b2%.isotope_server.IsotopeClientLocation\x122\n\tsync_mode\x18\x02 \x01(\x0e2\x1f.isotope_server.IsotopeSyncModeB\x1eZ\x1cdropbox/proto/isotope_serverb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.isotope_server.sync_frontend_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1cdropbox/proto/isotope_server'
    _globals['_ISOTOPEREQUESTCONTEXT']._serialized_start = 110
    _globals['_ISOTOPEREQUESTCONTEXT']._serialized_end = 271
    _globals['_ISOTOPECLIENTVALIDATIONFIELDS']._serialized_start = 274
    _globals['_ISOTOPECLIENTVALIDATIONFIELDS']._serialized_end = 429
    return None
