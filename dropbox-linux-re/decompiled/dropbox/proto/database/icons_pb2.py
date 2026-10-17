# Source Generated with Decompyle++
# File: icons_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/database/icons.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"dropbox/proto/database/icons.proto\x12\x08database\x1a#dropbox/proto/rust/extensions.proto"A\n\x07DBXIcon\x12(\n\ticon_type\x18\x01 \x01(\x0e2\x15.database.DBXIconType\x12\x0c\n\x04path\x18\x02 \x01(\t*\xfc\x03\n\x0bDBXIconType\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07DROPBOX\x10\x01\x12\x12\n\x0eCAMERA_UPLOADS\x10\x02\x12\n\n\x06SHARED\x10\x03\x12\x14\n\x10SHARED_READ_ONLY\x10\x04\x12\x19\n\x15SHARED_VIEW_NAME_ONLY\x10\x05\x12\x0f\n\x0bTEAM_FOLDER\x10\x06\x12\x19\n\x15TEAM_FOLDER_READ_ONLY\x10\x07\x12\x16\n\x12TEAM_MEMBER_FOLDER\x10\x08\x12\x0b\n\x07SANDBOX\x10\t\x12\x15\n\x11DEVICE_FOLDER_MAC\x10\n\x12\x15\n\x11DEVICE_FOLDER_WIN\x10\x0b\x12\x19\n\x15DEVICE_FOLDER_GENERIC\x10\x0c\x12\x19\n\x15DEVICE_FOLDER_DESKTOP\x10\r\x12\x1b\n\x17DEVICE_FOLDER_DOCUMENTS\x10\x0e\x12\x1b\n\x17DEVICE_FOLDER_DOWNLOADS\x10\x0f\x12\x1a\n\x16DEVICE_FOLDER_PICTURES\x10\x10\x12\x17\n\x13DEVICE_FOLDER_MUSIC\x10\x13\x12\x18\n\x14DEVICE_FOLDER_VIDEOS\x10\x14\x12\t\n\x05VAULT\x10\x11\x12\x18\n\x14FAMILY_SHARED_FOLDER\x10\x12\x12\x19\n\x15ENCRYPTED_TEAM_FOLDER\x10\x15\x1a\x04\x90\xb5\x18\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.database.icons_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_DBXICONTYPE']._loaded_options = None
    _globals['_DBXICONTYPE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_DBXICONTYPE']._serialized_start = 153
    _globals['_DBXICONTYPE']._serialized_end = 661
    _globals['_DBXICON']._serialized_start = 85
    _globals['_DBXICON']._serialized_end = 150
    return None
