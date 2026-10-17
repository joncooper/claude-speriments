# Source Generated with Decompyle++
# File: folder_type_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/enums/folder_type.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*dropbox/pap/events/enums/folder_type.proto\x12\x11enums.folder_type*\xa2\x01\n\nFolderType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04ROOT\x10\x01\x12\n\n\x06FOLDER\x10\x02\x12\x11\n\rSHARED_FOLDER\x10\x03\x12\x16\n\x12TEAM_SHARED_FOLDER\x10\x04\x12\x16\n\x12TEAM_MEMBER_FOLDER\x10\x05\x12\t\n\x05VAULT\x10\x06\x12\n\n\x06FAMILY\x10\x07\x12\x17\n\x13PRIVATE_TEAM_FOLDER\x10\x08B\x1aZ\x18dropbox/pap/events/enumsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.enums.folder_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18dropbox/pap/events/enums'
    _globals['_FOLDERTYPE']._serialized_start = 66
    _globals['_FOLDERTYPE']._serialized_end = 228
    return None
