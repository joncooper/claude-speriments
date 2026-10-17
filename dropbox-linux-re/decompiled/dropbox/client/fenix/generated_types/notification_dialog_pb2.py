# Source Generated with Decompyle++
# File: notification_dialog_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'notification_dialog.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19notification_dialog.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto"#\n\rDeleteFileReq\x12\x12\n\nlocal_path\x18\x01 \x01(\t2a\n\x15NotificationDialogApi\x12H\n\nDeleteFile\x12".dropbox.meta_engine.DeleteFileReq\x1a\x16.google.protobuf.Emptyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notification_dialog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DELETEFILEREQ']._serialized_start = 79
    _globals['_DELETEFILEREQ']._serialized_end = 114
    _globals['_NOTIFICATIONDIALOGAPI']._serialized_start = 116
    _globals['_NOTIFICATIONDIALOGAPI']._serialized_end = 213
    return None
