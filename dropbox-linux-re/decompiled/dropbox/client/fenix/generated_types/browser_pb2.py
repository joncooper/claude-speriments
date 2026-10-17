# Source Generated with Decompyle++
# File: browser_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'browser.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from  import shared_pb2 as shared__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbrowser.proto\x12\x13dropbox.meta_engine\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0cshared.proto"^\n\x13LoginAndRedirectReq\x12\x0b\n\x03url\x18\x01 \x01(\t\x12:\n\x07account\x18\x02 \x01(\x0b2).dropbox.meta_engine.AuthenticatedAccount"L\n\x13OpenUrlInBrowserReq\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x14\n\x0cquery_pieces\x18\x02 \x03(\t\x12\x12\n\naccount_id\x18\x03 \x01(\t2\xb8\x01\n\nBrowserApi\x12T\n\x10LoginAndRedirect\x12(.dropbox.meta_engine.LoginAndRedirectReq\x1a\x16.google.protobuf.Empty\x12T\n\x10OpenUrlInBrowser\x12(.dropbox.meta_engine.OpenUrlInBrowserReq\x1a\x16.google.protobuf.Emptyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'browser_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_LOGINANDREDIRECTREQ']._serialized_start = 81
    _globals['_LOGINANDREDIRECTREQ']._serialized_end = 175
    _globals['_OPENURLINBROWSERREQ']._serialized_start = 177
    _globals['_OPENURLINBROWSERREQ']._serialized_end = 253
    _globals['_BROWSERAPI']._serialized_start = 256
    _globals['_BROWSERAPI']._serialized_end = 440
    return None
