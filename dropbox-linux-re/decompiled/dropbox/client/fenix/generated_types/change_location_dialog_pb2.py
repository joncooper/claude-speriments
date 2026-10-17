# Source Generated with Decompyle++
# File: change_location_dialog_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'change_location_dialog.proto')
_sym_db = _symbol_database.Default()
from  import shared_pb2 as shared__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cchange_location_dialog.proto\x12\x13dropbox.meta_engine\x1a\x0cshared.proto"v\n\x1bOpenChangeLocationDialogReq\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount\x12\x1b\n\x13dropbox_folder_path\x18\x02 \x01(\t"H\n\x1dOpenChangeLocationDialogReply\x12\x1d\n\x13dropbox_folder_path\x18\x01 \x01(\tH\x00B\x08\n\x06result2\x9c\x01\n\x17ChangeLocationDialogApi\x12\x80\x01\n\x18OpenChangeLocationDialog\x120.dropbox.meta_engine.OpenChangeLocationDialogReq\x1a2.dropbox.meta_engine.OpenChangeLocationDialogReplyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'change_location_dialog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_OPENCHANGELOCATIONDIALOGREQ']._serialized_start = 67
    _globals['_OPENCHANGELOCATIONDIALOGREQ']._serialized_end = 185
    _globals['_OPENCHANGELOCATIONDIALOGREPLY']._serialized_start = 187
    _globals['_OPENCHANGELOCATIONDIALOGREPLY']._serialized_end = 259
    _globals['_CHANGELOCATIONDIALOGAPI']._serialized_start = 262
    _globals['_CHANGELOCATIONDIALOGAPI']._serialized_end = 418
    return None
