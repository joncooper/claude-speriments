# Source Generated with Decompyle++
# File: status_label_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/enums/status_label.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+dropbox/pap/events/enums/status_label.proto\x12\x12enums.status_label*\x9d\x05\n\x0bStatusLabel\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tIMPORTING\x10\x01\x12\x12\n\x0eLOW_DISK_SPACE\x10\x02\x12\x16\n\x12CANT_WATCH_DROPBOX\x10\x03\x12\x1a\n\x16CANT_UNMOUNT_NAMESPACE\x10\x04\x12\x16\n\x12CANT_MOUNT_DROPBOX\x10\x05\x12\x16\n\x12NO_ROOT_PERMISSION\x10\x06\x12\n\n\x06PAUSED\x10\x07\x12\x0e\n\nCONNECTING\x10\x08\x12\x14\n\x10WAITING_FOR_LINK\x10\t\x12\x07\n\x03NIL\x10\n\x12\x0c\n\x08UPDATING\x10\x0b\x12\r\n\tMIGRATING\x10\x0c\x12\x19\n\x15MIGRATING_SYNC_ENGINE\x10\r\x12\n\n\x06MOVING\x10\x0e\x12\x0b\n\x07PAUSING\x10\x0f\x12\x15\n\x11CONNECTING_ENGINE\x10\x10\x12\x0c\n\x08STARTING\x10\x11\x12\x10\n\x0cINITIALIZING\x10\x12\x12(\n$ENCRYPTED_FOLDER_ENROLLMENT_BLOCKING\x10\x13\x12,\n(ENCRYPTED_FOLDER_ENROLLMENT_NON_BLOCKING\x10\x14\x12\x0e\n\nREINDEXING\x10\x15\x12\x0b\n\x07SELSYNC\x10\x16\x12\x0f\n\x0bREARRANGING\x10\x17\x12\x17\n\x13SYNCING_WITH_ERRORS\x10\x18\x12\t\n\x05ERROR\x10\x19\x12\x0b\n\x07SYNCING\x10\x1a\x12\x0b\n\x07LISTING\x10\x1b\x12\x0f\n\x0bHASH_STATUS\x10\x1c\x12\x10\n\x0cHASH_FAILURE\x10\x1d\x12\x13\n\x0fDOWNLOAD_STATUS\x10\x1e\x12\x14\n\x10DOWNLOAD_FAILURE\x10\x1f\x12\x11\n\rUPLOAD_STATUS\x10 \x12\x12\n\x0eUPLOAD_FAILURE\x10!B\x1aZ\x18dropbox/pap/events/enumsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.enums.status_label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18dropbox/pap/events/enums'
    _globals['_STATUSLABEL']._serialized_start = 68
    _globals['_STATUSLABEL']._serialized_end = 737
    return None
