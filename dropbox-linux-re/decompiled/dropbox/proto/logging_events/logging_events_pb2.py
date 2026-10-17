# Source Generated with Decompyle++
# File: logging_events_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/logging_events/logging_events.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1dropbox/proto/logging_events/logging_events.proto\x12\x0elogging_events"\x91\x02\n\x08LogEvent\x12\x12\n\nevent_type\x18\x02 \x01(\t\x123\n\x08severity\x18\x03 \x01(\x0e2!.logging_events.LogEvent.Severity\x12C\n\x11additional_fields\x18\x04 \x03(\x0b2(.logging_events.LogEvent.AdditionalField\x12\r\n\x05table\x18\x06 \x01(\t\x1a-\n\x0fAdditionalField\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"9\n\x08Severity\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.logging_events.logging_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_LOGEVENT']._serialized_start = 70
    _globals['_LOGEVENT']._serialized_end = 343
    _globals['_LOGEVENT_ADDITIONALFIELD']._serialized_start = 239
    _globals['_LOGEVENT_ADDITIONALFIELD']._serialized_end = 284
    _globals['_LOGEVENT_SEVERITY']._serialized_start = 286
    _globals['_LOGEVENT_SEVERITY']._serialized_end = 343
    return None
