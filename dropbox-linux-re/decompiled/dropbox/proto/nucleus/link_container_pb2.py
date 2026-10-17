# Source Generated with Decompyle++
# File: link_container_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/link_container.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*dropbox/proto/nucleus/link_container.proto\x12\x07nucleus*_\n\x12LinkContainerState\x12\x10\n\x0cInconsistent\x10\x00\x12\x10\n\x0cMaterialized\x10\x01\x12\x12\n\x0eDematerialized\x10\x02\x12\x11\n\rTransitioning\x10\x03b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.link_container_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_LINKCONTAINERSTATE']._serialized_start = 55
    _globals['_LINKCONTAINERSTATE']._serialized_end = 150
    return None
