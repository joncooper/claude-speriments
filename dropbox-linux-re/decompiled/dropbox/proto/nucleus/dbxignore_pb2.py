# Source Generated with Decompyle++
# File: dbxignore_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/dbxignore.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%dropbox/proto/nucleus/dbxignore.proto\x12\x07nucleus\x1a#dropbox/proto/rust/extensions.proto"=\n\x11DBXIgnoreContents\x12(\n\x08contents\x18\x01 \x03(\x0b2\x16.nucleus.DBXIgnoreLine"\xf0\x02\n\rDBXIgnoreLine\x121\n\x07comment\x18\x01 \x01(\x0b2\x1e.nucleus.DBXIgnoreLine.CommentH\x00\x12+\n\x04glob\x18\x02 \x01(\x0b2\x1b.nucleus.DBXIgnoreLine.GlobH\x00\x12A\n\x10glob_and_comment\x18\x03 \x01(\x0b2%.nucleus.DBXIgnoreLine.GlobAndCommentH\x00\x1a\x1a\n\x07Comment\x12\x0f\n\x07comment\x18\x01 \x01(\t\x1a\x14\n\x04Glob\x12\x0c\n\x04glob\x18\x01 \x01(\t\x1ax\n\x0eGlobAndComment\x12/\n\x04glob\x18\x01 \x01(\x0b2\x1b.nucleus.DBXIgnoreLine.GlobB\x04\xc0\xb5\x18\x00\x125\n\x07comment\x18\x02 \x01(\x0b2\x1e.nucleus.DBXIgnoreLine.CommentB\x04\xc0\xb5\x18\x00B\x10\n\x08contents\x12\x04\x88\xb5\x18\x00"\x84\x01\n\x1bDBXIgnoreContentsAndVersion\x123\n\tdbxignore\x18\x01 \x01(\x0b2\x1a.nucleus.DBXIgnoreContentsB\x04\xc0\xb5\x18\x00\x120\n\x07version\x18\x02 \x01(\x0e2\x19.nucleus.DBXIgnoreVersionB\x04\xc0\xb5\x18\x00*G\n\x10DBXIgnoreVersion\x12\r\n\tV_UNKNOWN\x10\x00\x12\x06\n\x02V1\x10\x01\x12\x06\n\x02V2\x10\x02\x12\x06\n\x02V3\x10\x03\x12\x06\n\x02V4\x10\x04\x1a\x04\x90\xb5\x18\x01B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.dbxignore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_DBXIGNOREVERSION']._loaded_options = None
    _globals['_DBXIGNOREVERSION']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_DBXIGNORELINE_GLOBANDCOMMENT'].fields_by_name['glob']._loaded_options = None
    _globals['_DBXIGNORELINE_GLOBANDCOMMENT'].fields_by_name['glob']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DBXIGNORELINE_GLOBANDCOMMENT'].fields_by_name['comment']._loaded_options = None
    _globals['_DBXIGNORELINE_GLOBANDCOMMENT'].fields_by_name['comment']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DBXIGNORELINE'].oneofs_by_name['contents']._loaded_options = None
    _globals['_DBXIGNORELINE'].oneofs_by_name['contents']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_DBXIGNORECONTENTSANDVERSION'].fields_by_name['dbxignore']._loaded_options = None
    _globals['_DBXIGNORECONTENTSANDVERSION'].fields_by_name['dbxignore']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DBXIGNORECONTENTSANDVERSION'].fields_by_name['version']._loaded_options = None
    _globals['_DBXIGNORECONTENTSANDVERSION'].fields_by_name['version']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_DBXIGNOREVERSION']._serialized_start = 656
    _globals['_DBXIGNOREVERSION']._serialized_end = 727
    _globals['_DBXIGNORECONTENTS']._serialized_start = 87
    _globals['_DBXIGNORECONTENTS']._serialized_end = 148
    _globals['_DBXIGNORELINE']._serialized_start = 151
    _globals['_DBXIGNORELINE']._serialized_end = 519
    _globals['_DBXIGNORELINE_COMMENT']._serialized_start = 331
    _globals['_DBXIGNORELINE_COMMENT']._serialized_end = 357
    _globals['_DBXIGNORELINE_GLOB']._serialized_start = 359
    _globals['_DBXIGNORELINE_GLOB']._serialized_end = 379
    _globals['_DBXIGNORELINE_GLOBANDCOMMENT']._serialized_start = 381
    _globals['_DBXIGNORELINE_GLOBANDCOMMENT']._serialized_end = 501
    _globals['_DBXIGNORECONTENTSANDVERSION']._serialized_start = 522
    _globals['_DBXIGNORECONTENTSANDVERSION']._serialized_end = 654
    return None
