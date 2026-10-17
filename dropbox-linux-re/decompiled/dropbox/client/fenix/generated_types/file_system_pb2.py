# Source Generated with Decompyle++
# File: file_system_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'file_system.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11file_system.proto\x12\x13dropbox.meta_engine"!\n\x11FileSystemPathReq\x12\x0c\n\x04path\x18\x01 \x01(\t"8\n\rDiskSpaceInfo\x12\x12\n\nfree_space\x18\x01 \x01(\x04\x12\x13\n\x0btotal_space\x18\x02 \x01(\x04"\x1c\n\nBoolResult\x12\x0e\n\x06result\x18\x01 \x01(\x082\xf3\x02\n\rFileSystemApi\x12^\n\x10GetDiskSpaceInfo\x12&.dropbox.meta_engine.FileSystemPathReq\x1a".dropbox.meta_engine.DiskSpaceInfo\x12T\n\tCanAccess\x12&.dropbox.meta_engine.FileSystemPathReq\x1a\x1f.dropbox.meta_engine.BoolResult\x12T\n\tIsSymlink\x12&.dropbox.meta_engine.FileSystemPathReq\x1a\x1f.dropbox.meta_engine.BoolResult\x12V\n\x0bIsDirectory\x12&.dropbox.meta_engine.FileSystemPathReq\x1a\x1f.dropbox.meta_engine.BoolResultb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_system_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_FILESYSTEMPATHREQ']._serialized_start = 42
    _globals['_FILESYSTEMPATHREQ']._serialized_end = 75
    _globals['_DISKSPACEINFO']._serialized_start = 77
    _globals['_DISKSPACEINFO']._serialized_end = 133
    _globals['_BOOLRESULT']._serialized_start = 135
    _globals['_BOOLRESULT']._serialized_end = 163
    _globals['_FILESYSTEMAPI']._serialized_start = 166
    _globals['_FILESYSTEMAPI']._serialized_end = 537
    return None
