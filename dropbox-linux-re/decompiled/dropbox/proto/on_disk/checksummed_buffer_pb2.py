# Source Generated with Decompyle++
# File: checksummed_buffer_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/on_disk/checksummed_buffer.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.dropbox/proto/on_disk/checksummed_buffer.proto\x12\x07on_disk"2\n\x11ChecksummedBuffer\x12\x0e\n\x06buffer\x18\x01 \x01(\x0c\x12\r\n\x05crc32\x18\x02 \x01(\rb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.on_disk.checksummed_buffer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CHECKSUMMEDBUFFER']._serialized_start = 59
    _globals['_CHECKSUMMEDBUFFER']._serialized_end = 109
    return None
