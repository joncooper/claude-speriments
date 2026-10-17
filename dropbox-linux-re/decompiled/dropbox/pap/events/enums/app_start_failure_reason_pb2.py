# Source Generated with Decompyle++
# File: app_start_failure_reason_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/enums/app_start_failure_reason.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7dropbox/pap/events/enums/app_start_failure_reason.proto\x12\x1eenums.app_start_failure_reason*\xcd\x03\n\x15AppStartFailureReason\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tAPP_STUCK\x10\x01\x12\x0f\n\x0bAPP_CRASHED\x10\x02\x12/\n+APP_CRASHING_REPEATEDLY_DUE_TO_MOVE_FAILURE\x10\x03\x125\n1APP_CRASHING_REPEATEDLY_DUE_TO_FAILED_CHECK_MERGE\x10\x04\x12\x1c\n\x18BOOT_FAILED_STARTUP_HIGH\x10\x05\x12 \n\x1cBOOT_FAILED_TO_LOAD_ACCOUNTS\x10\x06\x12\x1d\n\x19BOOT_FAILED_TO_SETUP_ROOT\x10\x07\x12\x1c\n\x18BOOT_FAILED_TO_START_APP\x10\x08\x12 \n\x1cBOOT_FAILED_TO_REGISTER_HOST\x10\t\x12)\n%BOOT_FAILED_TO_HANDLE_REGISTERED_HOST\x10\n\x125\n1BOOT_FAILED_TO_CREATE_KEY_STORE_AND_UNLINK_COOKIE\x10\x0b\x12\x1e\n\x1aAPP_STARTUP_FAILED_UNKNOWN\x10\x0cB\x1aZ\x18dropbox/pap/events/enumsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.enums.app_start_failure_reason_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18dropbox/pap/events/enums'
    _globals['_APPSTARTFAILUREREASON']._serialized_start = 92
    _globals['_APPSTARTFAILUREREASON']._serialized_end = 553
    return None
