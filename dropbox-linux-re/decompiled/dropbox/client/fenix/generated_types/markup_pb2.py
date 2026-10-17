# Source Generated with Decompyle++
# File: markup_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'markup.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cmarkup.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto"J\n\x0bCopyLinkReq\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x12\n\nlocal_path\x18\x02 \x01(\t\x12\x13\n\x0bserver_path\x18\x03 \x01(\t"-\n\x17CopyImageToClipboardReq\x12\x12\n\nlocal_path\x18\x01 \x01(\t"<\n\x12OpenErrorDialogReq\x12\x12\n\nlocal_path\x18\x01 \x01(\t\x12\x12\n\naccount_id\x18\x02 \x01(\t"0\n\x1dSetMacScreenshotThumbnailsReq\x12\x0f\n\x07enabled\x18\x01 \x01(\x082\xed\x02\n\tMarkupApi\x12D\n\x08CopyLink\x12 .dropbox.meta_engine.CopyLinkReq\x1a\x16.google.protobuf.Empty\x12\\\n\x14CopyImageToClipboard\x12,.dropbox.meta_engine.CopyImageToClipboardReq\x1a\x16.google.protobuf.Empty\x12R\n\x0fOpenErrorDialog\x12\'.dropbox.meta_engine.OpenErrorDialogReq\x1a\x16.google.protobuf.Empty\x12h\n\x1aSetMacScreenshotThumbnails\x122.dropbox.meta_engine.SetMacScreenshotThumbnailsReq\x1a\x16.google.protobuf.Emptyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'markup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_COPYLINKREQ']._serialized_start = 66
    _globals['_COPYLINKREQ']._serialized_end = 140
    _globals['_COPYIMAGETOCLIPBOARDREQ']._serialized_start = 142
    _globals['_COPYIMAGETOCLIPBOARDREQ']._serialized_end = 187
    _globals['_OPENERRORDIALOGREQ']._serialized_start = 189
    _globals['_OPENERRORDIALOGREQ']._serialized_end = 249
    _globals['_SETMACSCREENSHOTTHUMBNAILSREQ']._serialized_start = 251
    _globals['_SETMACSCREENSHOTTHUMBNAILSREQ']._serialized_end = 299
    _globals['_MARKUPAPI']._serialized_start = 302
    _globals['_MARKUPAPI']._serialized_end = 667
    return None
