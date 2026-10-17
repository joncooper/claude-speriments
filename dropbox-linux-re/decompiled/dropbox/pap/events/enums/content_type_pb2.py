# Source Generated with Decompyle++
# File: content_type_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/enums/content_type.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dropbox/pap/events/enums/content_type.proto\x12\x12enums.content_type*\x9c\x01\n\x0bContentType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04FILE\x10\x01\x12\n\n\x06FOLDER\x10\x02\x12\t\n\x05MIXED\x10\x03\x12\x0b\n\x07PROJECT\x10\x04\x12\t\n\x05ASSET\x10\x05\x12\x11\n\rDASH_DOCUMENT\x10\x06\x12\x13\n\x0fREQUEST_TO_JOIN\x10\x07\x12\x0f\n\x0bTEAM_INVITE\x10\x08\x12\x0e\n\nONBOARDING\x10\tB\x1aZ\x18dropbox/pap/events/enumsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.enums.content_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18dropbox/pap/events/enums'
    _globals['_CONTENTTYPE']._serialized_start = 68
    _globals['_CONTENTTYPE']._serialized_end = 224
    return None
