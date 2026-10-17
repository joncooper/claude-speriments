# Source Generated with Decompyle++
# File: cursors_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync_frontend/cursors.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dropbox/proto/sync_frontend/cursors.proto\x12\rsync_frontend"M\n\x19SignedConsistentCutCursor\x12\x1d\n\x15consistent_cut_cursor\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c"F\n\x16SignedLinearizedCursor\x12\x19\n\x11linearized_cursor\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0cB\x1dZ\x1bdropbox/proto/sync_frontendb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync_frontend.cursors_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1bdropbox/proto/sync_frontend'
    _globals['_SIGNEDCONSISTENTCUTCURSOR']._serialized_start = 60
    _globals['_SIGNEDCONSISTENTCUTCURSOR']._serialized_end = 137
    _globals['_SIGNEDLINEARIZEDCURSOR']._serialized_start = 139
    _globals['_SIGNEDLINEARIZEDCURSOR']._serialized_end = 209
    return None
