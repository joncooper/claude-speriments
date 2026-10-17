# Source Generated with Decompyle++
# File: root_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/sync/root.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ddropbox/proto/sync/root.proto\x12\x04sync*M\n\nRootLayout\x12\x10\n\x0cUNKNOWN_ROOT\x10\x00\x12\x11\n\rPERSONAL_ROOT\x10\x01\x12\x0c\n\x08TSD_ROOT\x10\x02\x12\x0c\n\x08TMR_ROOT\x10\x03B.\n\x16com.dropbox.proto.syncP\x01Z\x12dropbox/proto/syncb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.sync.root_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.dropbox.proto.syncP\x01Z\x12dropbox/proto/sync'
    _globals['_ROOTLAYOUT']._serialized_start = 39
    _globals['_ROOTLAYOUT']._serialized_end = 116
    return None
