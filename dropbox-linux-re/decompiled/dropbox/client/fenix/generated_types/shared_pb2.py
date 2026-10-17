# Source Generated with Decompyle++
# File: shared_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'shared.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.nucleus import types_pb2 as dropbox_dot_proto_dot_nucleus_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cshared.proto\x12\x13dropbox.meta_engine\x1a!dropbox/proto/nucleus/types.proto"H\n\x0eFileIdPathPair\x12\x1f\n\x06fileid\x18\x01 \x01(\x0b2\x0f.nucleus.FileId\x12\x15\n\rrelative_path\x18\x02 \x01(\t"*\n\x0cAnchorFolder\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t"\xd9\x03\n\x14AuthenticatedAccount\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\x04\x12\r\n\x05email\x18\x03 \x01(\t\x12\x16\n\x0eemail_verified\x18\x04 \x01(\x08\x12\x14\n\x0cdisplay_name\x18\x05 \x01(\t\x12\x12\n\nfirst_name\x18\x06 \x01(\t\x12.\n\x04role\x18\x07 \x01(\x0e2 .dropbox.meta_engine.AccountRole\x12\x0f\n\x07team_id\x18\x08 \x01(\x04\x12\x11\n\tteam_name\x18\t \x01(\t\x12\x10\n\x08host_int\x18\n \x01(\x04\x12\x13\n\x0bhost_secret\x18\x0b \x01(\t\x12\x13\n\x0bclient_uuid\x18\x0c \x01(\t\x12\x10\n\x08ui_flags\x18\r \x01(\t\x12\x19\n\x11subscription_type\x18\x0e \x01(\t\x12\x12\n\nroot_ns_id\x18\x0f \x01(\x04\x12\x16\n\x0eroot_ns_fileid\x18\x10 \x01(\t\x12\x12\n\nhome_ns_id\x18\x11 \x01(\x04\x12\x16\n\x0ehome_ns_fileid\x18\x12 \x01(\t\x12\x17\n\x0froot_mount_path\x18\x13 \x01(\t\x12!\n\x19disable_multiaccount_link\x18\x14 \x01(\x08*;\n\x0bAccountRole\x12\x10\n\x0cUNKNOWN_ROLE\x10\x00\x12\x0c\n\x08PERSONAL\x10\x01\x12\x0c\n\x08BUSINESS\x10\x02b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'shared_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_ACCOUNTROLE']._serialized_start = 666
    _globals['_ACCOUNTROLE']._serialized_end = 725
    _globals['_FILEIDPATHPAIR']._serialized_start = 72
    _globals['_FILEIDPATHPAIR']._serialized_end = 144
    _globals['_ANCHORFOLDER']._serialized_start = 146
    _globals['_ANCHORFOLDER']._serialized_end = 188
    _globals['_AUTHENTICATEDACCOUNT']._serialized_start = 191
    _globals['_AUTHENTICATEDACCOUNT']._serialized_end = 664
    return None
