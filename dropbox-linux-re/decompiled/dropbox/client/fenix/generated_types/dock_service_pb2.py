# Source Generated with Decompyle++
# File: dock_service_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dock_service.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12dock_service.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto"\x13\n\x11CloseWindowsEvent2\xfb\x01\n\x0eDockServiceApi\x12F\n\x14IncrementWindowCount\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12F\n\x14DecrementWindowCount\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12Y\n\x15GetCloseWindowsEvents\x12\x16.google.protobuf.Empty\x1a&.dropbox.meta_engine.CloseWindowsEvent0\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dock_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CLOSEWINDOWSEVENT']._serialized_start = 72
    _globals['_CLOSEWINDOWSEVENT']._serialized_end = 91
    _globals['_DOCKSERVICEAPI']._serialized_start = 94
    _globals['_DOCKSERVICEAPI']._serialized_end = 345
    return None
