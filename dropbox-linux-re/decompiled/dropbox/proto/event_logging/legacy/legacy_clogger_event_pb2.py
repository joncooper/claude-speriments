# Source Generated with Decompyle++
# File: legacy_clogger_event_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/event_logging/legacy/legacy_clogger_event.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=dropbox/proto/event_logging/legacy/legacy_clogger_event.proto\x12\revent_logging\x1a\x1bgoogle/protobuf/empty.proto"\xf9\x01\n\tAvroValue\x12,\n\nnull_value\x18\x01 \x01(\x0b2\x16.google.protobuf.EmptyH\x00\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x04 \x01(\x01H\x00\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x00\x12-\n\nlist_value\x18\x06 \x01(\x0b2\x17.event_logging.AvroListH\x00\x12+\n\tmap_value\x18\x07 \x01(\x0b2\x16.event_logging.AvroMapH\x00B\x07\n\x05value"8\n\x08AvroList\x12,\n\nlist_value\x18\x01 \x03(\x0b2\x18.event_logging.AvroValue"\x8d\x01\n\x07AvroMap\x127\n\tmap_value\x18\x01 \x03(\x0b2$.event_logging.AvroMap.MapValueEntry\x1aI\n\rMapValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b2\x18.event_logging.AvroValue:\x028\x01"\xea\x02\n\x1aDesktopGenericCloggerEvent\x12\x10\n\x08category\x18\x01 \x01(\t\x12\x0f\n\x07host_id\x18\x02 \x01(\x03\x12\x10\n\x08build_id\x18\x03 \x01(\t\x12A\n\x04data\x18\x04 \x03(\x0b23.event_logging.DesktopGenericCloggerEvent.DataEntry\x12\x19\n\x11client_session_id\x18\x05 \x01(\t\x12 \n\x18sync_engine_build_number\x18\x06 \x01(\t\x12\x12\n\nmachine_id\x18\x08 \x01(\t\x12\x17\n\x0flinked_host_ids\x18\t \x03(\x03\x12\x1d\n\x15has_mti_team_accounts\x18\n \x01(\x08\x1aE\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b2\x18.event_logging.AvroValue:\x028\x01J\x04\x08\x07\x10\x08BN\n&com.dropbox.proto.event_logging.legacyP\x01Z"dropbox/proto/event_logging/legacyb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.event_logging.legacy.legacy_clogger_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.dropbox.proto.event_logging.legacyP\x01Z"dropbox/proto/event_logging/legacy'
    _globals['_AVROMAP_MAPVALUEENTRY']._loaded_options = None
    _globals['_AVROMAP_MAPVALUEENTRY']._serialized_options = b'8\x01'
    _globals['_DESKTOPGENERICCLOGGEREVENT_DATAENTRY']._loaded_options = None
    _globals['_DESKTOPGENERICCLOGGEREVENT_DATAENTRY']._serialized_options = b'8\x01'
    _globals['_AVROVALUE']._serialized_start = 110
    _globals['_AVROVALUE']._serialized_end = 359
    _globals['_AVROLIST']._serialized_start = 361
    _globals['_AVROLIST']._serialized_end = 417
    _globals['_AVROMAP']._serialized_start = 420
    _globals['_AVROMAP']._serialized_end = 561
    _globals['_AVROMAP_MAPVALUEENTRY']._serialized_start = 488
    _globals['_AVROMAP_MAPVALUEENTRY']._serialized_end = 561
    _globals['_DESKTOPGENERICCLOGGEREVENT']._serialized_start = 564
    _globals['_DESKTOPGENERICCLOGGEREVENT']._serialized_end = 926
    _globals['_DESKTOPGENERICCLOGGEREVENT_DATAENTRY']._serialized_start = 851
    _globals['_DESKTOPGENERICCLOGGEREVENT_DATAENTRY']._serialized_end = 920
    return None
