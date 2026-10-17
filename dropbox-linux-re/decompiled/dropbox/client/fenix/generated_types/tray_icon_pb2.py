# Source Generated with Decompyle++
# File: tray_icon_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'tray_icon.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from  import shared_pb2 as shared__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftray_icon.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0cshared.proto"S\n\x15CanPromoteTrayIconReq\x12:\n\x07account\x18\x01 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount".\n\x17CanPromoteTrayIconReply\x12\x13\n\x0bcan_promote\x18\x01 \x01(\x08"1\n\x1aGetIsTrayIconPromotedReply\x12\x13\n\x0bis_promoted\x18\x01 \x01(\x082\xdf\x01\n\x0bTrayIconApi\x12n\n\x12CanPromoteTrayIcon\x12*.dropbox.meta_engine.CanPromoteTrayIconReq\x1a,.dropbox.meta_engine.CanPromoteTrayIconReply\x12`\n\x15GetIsTrayIconPromoted\x12\x16.google.protobuf.Empty\x1a/.dropbox.meta_engine.GetIsTrayIconPromotedReplyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tray_icon_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_CANPROMOTETRAYICONREQ']._serialized_start = 83
    _globals['_CANPROMOTETRAYICONREQ']._serialized_end = 166
    _globals['_CANPROMOTETRAYICONREPLY']._serialized_start = 168
    _globals['_CANPROMOTETRAYICONREPLY']._serialized_end = 214
    _globals['_GETISTRAYICONPROMOTEDREPLY']._serialized_start = 216
    _globals['_GETISTRAYICONPROMOTEDREPLY']._serialized_end = 265
    _globals['_TRAYICONAPI']._serialized_start = 268
    _globals['_TRAYICONAPI']._serialized_end = 491
    return None
