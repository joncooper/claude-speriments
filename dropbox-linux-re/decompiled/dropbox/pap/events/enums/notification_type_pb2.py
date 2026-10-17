# Source Generated with Decompyle++
# File: notification_type_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/enums/notification_type.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0dropbox/pap/events/enums/notification_type.proto\x12\x17enums.notification_type*\x8d\x02\n\x10NotificationType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bFILE_SHARED\x10\x01\x12\x11\n\rFOLDER_SHARED\x10\x02\x12\x16\n\x12FILE_PAPER_COMMENT\x10\x03\x12\x16\n\x12FILE_FOLDER_VIEWED\x10\x04\x12\x1e\n\x1aFILE_FOLDER_ACCESS_REQUEST\x10\x05\x12\n\n\x06VIEWER\x10\x06\x12\x10\n\x0cCOORDINATION\x10\x07\x12\x1a\n\x16VIEWER_UNSAVED_CHANGES\x10\x08\x12\x12\n\x0eMULTIPLE_EDITS\x10\t\x12\x10\n\x0cMULTI_VIEWER\x10\n\x12\x18\n\x14COORDINATION_PENDING\x10\x0bB\x1aZ\x18dropbox/pap/events/enumsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.enums.notification_type_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18dropbox/pap/events/enums'
    _globals['_NOTIFICATIONTYPE']._serialized_start = 78
    _globals['_NOTIFICATIONTYPE']._serialized_end = 347
    return None
