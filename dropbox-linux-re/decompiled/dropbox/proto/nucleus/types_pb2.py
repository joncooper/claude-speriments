# Source Generated with Decompyle++
# File: types_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/types.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!dropbox/proto/nucleus/types.proto\x12\x07nucleus\x1a\x1bgoogle/protobuf/empty.proto\x1a#dropbox/proto/rust/extensions.proto"\xa8\x01\n\x04Path\x12 \n\x18root_relative_components\x18\x01 \x03(\t\x121\n\x13valid_platform_path\x18\x02 \x01(\x0b2\x12.nucleus.LocalPathH\x00\x127\n\x15invalid_platform_path\x18\x03 \x01(\x0b2\x16.google.protobuf.EmptyH\x00B\x12\n\nlocal_path\x12\x04\x88\xb5\x18\x00"\x1c\n\x0cRRServerPath\x12\x0c\n\x04path\x18\x01 \x01(\t""\n\tLocalPath\x12\x15\n\rabsolute_path\x18\x01 \x01(\t"\x14\n\x06FileId\x12\n\n\x02id\x18\x01 \x01(\t"G\n\x04File\x12?\n\tblocklist\x18\x01 \x03(\x0cB,\xa2\xb5\x18(::obfuscation::WithObfuscation<[u8; 32]>"\x0b\n\tDirectory"\t\n\x07Symlink"\r\n\x0bPlaceholder"\n\n\x08CloudDoc"\xa0\x02\n\nSyncObject\x12\x1d\n\x04file\x18\x01 \x01(\x0b2\r.nucleus.FileH\x00\x12!\n\x03dir\x18\x02 \x01(\x0b2\x12.nucleus.DirectoryH\x00\x12#\n\x07symlink\x18\x03 \x01(\x0b2\x10.nucleus.SymlinkH\x00\x12+\n\x0bplaceholder\x18\x06 \x01(\x0b2\x14.nucleus.PlaceholderH\x00\x12&\n\tcloud_doc\x18\x07 \x01(\x0b2\x11.nucleus.CloudDocH\x00\x12!\n\x04path\x18\x04 \x01(\x0b2\r.nucleus.PathB\x04\xc0\xb5\x18\x00\x12%\n\x06fileid\x18\x05 \x01(\x0b2\x0f.nucleus.FileIdB\x04\xc0\xb5\x18\x00B\x0c\n\x04type\x12\x04\x88\xb5\x18\x00"<\n\x0fRevisionDetails\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x18\n\x10server_timestamp\x18\x02 \x01(\x03",\n\x07LocalId\x12\x0f\n\x07version\x18\x01 \x01(\x06\x12\x10\n\x08sequence\x18\x02 \x01(\x04*K\n\x0cSyncPriority\x12\x10\n\x0cUNKNOWN_PRIO\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\r\n\tDBXIGNORE\x10\x03\x1a\x04\x90\xb5\x18\x01*q\n\x08FileType\x12\x15\n\x11UNKNOWN_FILE_TYPE\x10\x00\x12\x08\n\x04FILE\x10\x01\x12\r\n\tDIRECTORY\x10\x02\x12\x0f\n\x0bPLACEHOLDER\x10\x03\x12\x0b\n\x07SYMLINK\x10\x04\x12\x11\n\rDEVICE_ANCHOR\x10\x05\x1a\x04\x90\xb5\x18\x01*@\n\x0fHydrationPolicy\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05LOCAL\x10\x01\x12\x0f\n\x0bONLINE_ONLY\x10\x02\x1a\x04\x90\xb5\x18\x01B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_SYNCPRIORITY']._loaded_options = None
    _globals['_SYNCPRIORITY']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_FILETYPE']._loaded_options = None
    _globals['_FILETYPE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_HYDRATIONPOLICY']._loaded_options = None
    _globals['_HYDRATIONPOLICY']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_PATH'].oneofs_by_name['local_path']._loaded_options = None
    _globals['_PATH'].oneofs_by_name['local_path']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_FILE'].fields_by_name['blocklist']._loaded_options = None
    _globals['_FILE'].fields_by_name['blocklist']._serialized_options = b'\xa2\xb5\x18(::obfuscation::WithObfuscation<[u8; 32]>'
    _globals['_SYNCOBJECT'].oneofs_by_name['type']._loaded_options = None
    _globals['_SYNCOBJECT'].oneofs_by_name['type']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_SYNCOBJECT'].fields_by_name['path']._loaded_options = None
    _globals['_SYNCOBJECT'].fields_by_name['path']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCOBJECT'].fields_by_name['fileid']._loaded_options = None
    _globals['_SYNCOBJECT'].fields_by_name['fileid']._serialized_options = b'\xc0\xb5\x18\x00'
    _globals['_SYNCPRIORITY']._serialized_start = 894
    _globals['_SYNCPRIORITY']._serialized_end = 969
    _globals['_FILETYPE']._serialized_start = 971
    _globals['_FILETYPE']._serialized_end = 1084
    _globals['_HYDRATIONPOLICY']._serialized_start = 1086
    _globals['_HYDRATIONPOLICY']._serialized_end = 1150
    _globals['_PATH']._serialized_start = 113
    _globals['_PATH']._serialized_end = 281
    _globals['_RRSERVERPATH']._serialized_start = 283
    _globals['_RRSERVERPATH']._serialized_end = 311
    _globals['_LOCALPATH']._serialized_start = 313
    _globals['_LOCALPATH']._serialized_end = 347
    _globals['_FILEID']._serialized_start = 349
    _globals['_FILEID']._serialized_end = 369
    _globals['_FILE']._serialized_start = 371
    _globals['_FILE']._serialized_end = 442
    _globals['_DIRECTORY']._serialized_start = 444
    _globals['_DIRECTORY']._serialized_end = 455
    _globals['_SYMLINK']._serialized_start = 457
    _globals['_SYMLINK']._serialized_end = 466
    _globals['_PLACEHOLDER']._serialized_start = 468
    _globals['_PLACEHOLDER']._serialized_end = 481
    _globals['_CLOUDDOC']._serialized_start = 483
    _globals['_CLOUDDOC']._serialized_end = 493
    _globals['_SYNCOBJECT']._serialized_start = 496
    _globals['_SYNCOBJECT']._serialized_end = 784
    _globals['_REVISIONDETAILS']._serialized_start = 786
    _globals['_REVISIONDETAILS']._serialized_end = 846
    _globals['_LOCALID']._serialized_start = 848
    _globals['_LOCALID']._serialized_end = 892
    return None
