# Source Generated with Decompyle++
# File: file_event_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/nucleus/file_event.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.rust import extensions_pb2 as dropbox_dot_proto_dot_rust_dot_extensions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&dropbox/proto/nucleus/file_event.proto\x12\x07nucleus\x1a#dropbox/proto/rust/extensions.proto"9\n\nWatchEvent\x12+\n\nevent_type\x18\x01 \x01(\x0e2\x17.nucleus.WatchEventType"_\n\tPathEvent\x12*\n\nevent_type\x18\x01 \x01(\x0e2\x16.nucleus.PathEventType\x12&\n\x06cookie\x18\x02 \x01(\x0b2\x16.nucleus.InotifyCookie"\x1e\n\rInotifyCookie\x12\r\n\x05value\x18\x01 \x01(\r"{\n\tFileEvent\x12"\n\x04path\x18\x01 \x01(\x0b2\x12.nucleus.PathEventH\x00\x12$\n\x05watch\x18\x02 \x01(\x0b2\x13.nucleus.WatchEventH\x00\x12\x15\n\rabsolute_path\x18\x03 \x01(\tB\r\n\x05event\x12\x04\x88\xb5\x18\x00*\xac\x01\n\rPathEventType\x12%\n!UNKNOWN_UNHANDLED_PATH_EVENT_TYPE\x10\x00\x12\x1b\n\x17UNKNOWN_PATH_EVENT_TYPE\x10\x01\x12\r\n\tATTR_ONLY\x10\x02\x12\n\n\x06CREATE\x10\x03\x12\n\n\x06DELETE\x10\x04\x12\r\n\tRENAME_TO\x10\x05\x12\x0f\n\x0bRENAME_FROM\x10\x06\x12\n\n\x06RENAME\x10\x07\x1a\x04\x90\xb5\x18\x01*v\n\x0eWatchEventType\x12&\n"UNKNOWN_UNHANDLED_WATCH_EVENT_TYPE\x10\x00\x12\x12\n\x0eDROPPED_EVENTS\x10\x01\x12\x11\n\rWATCH_REMOVED\x10\x02\x12\x0f\n\x0bWATCH_ERROR\x10\x03\x1a\x04\x90\xb5\x18\x01B\x0c\xa2\x02\tNucleusSEb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.nucleus.file_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\xa2\x02\tNucleusSE'
    _globals['_PATHEVENTTYPE']._loaded_options = None
    _globals['_PATHEVENTTYPE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_WATCHEVENTTYPE']._loaded_options = None
    _globals['_WATCHEVENTTYPE']._serialized_options = b'\x90\xb5\x18\x01'
    _globals['_FILEEVENT'].oneofs_by_name['event']._loaded_options = None
    _globals['_FILEEVENT'].oneofs_by_name['event']._serialized_options = b'\x88\xb5\x18\x00'
    _globals['_PATHEVENTTYPE']._serialized_start = 402
    _globals['_PATHEVENTTYPE']._serialized_end = 574
    _globals['_WATCHEVENTTYPE']._serialized_start = 576
    _globals['_WATCHEVENTTYPE']._serialized_end = 694
    _globals['_WATCHEVENT']._serialized_start = 88
    _globals['_WATCHEVENT']._serialized_end = 145
    _globals['_PATHEVENT']._serialized_start = 147
    _globals['_PATHEVENT']._serialized_end = 242
    _globals['_INOTIFYCOOKIE']._serialized_start = 244
    _globals['_INOTIFYCOOKIE']._serialized_end = 274
    _globals['_FILEEVENT']._serialized_start = 276
    _globals['_FILEEVENT']._serialized_end = 399
    return None
