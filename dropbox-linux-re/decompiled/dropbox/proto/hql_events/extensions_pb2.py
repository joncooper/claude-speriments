# Source Generated with Decompyle++
# File: extensions_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/proto/hql_events/extensions.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from dropbox.proto.hql_events import taxonomy_pb2 as dropbox_dot_proto_dot_hql__events_dot_taxonomy__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)dropbox/proto/hql_events/extensions.proto\x12\nhql_events\x1a google/protobuf/descriptor.proto\x1a\'dropbox/proto/hql_events/taxonomy.proto"\x8f\x04\n\x10HQLEventIdentity\x12K\n\x0faction_event_id\x18\x01 \x01(\x0b20.hql_events.HQLEventIdentity.ActionEventIdentityH\x00\x12\x14\n\nevent_name\x18\x02 \x01(\tH\x00\x12<\n\x0bevent_class\x18\x03 \x01(\x0b2\'.hql_events.HQLEventIdentity.EventClass\x12>\n\x0clegacy_event\x18\x04 \x01(\x0b2(.hql_events.HQLEventIdentity.LegacyEvent\x1aX\n\x13ActionEventIdentity\x12\x0e\n\x06object\x18\x01 \x01(\t\x121\n\x06action\x18\x02 \x01(\x0e2!.hql_events.TaxonomyAction.Action\x1a\x87\x01\n\nEventClass\x127\n\nclass_name\x18\x01 \x01(\x0e2#.hql_events.TaxonomyClass.ClassName\x12@\n\rsubclass_name\x18\x02 \x01(\x0e2).hql_events.TaxonomySubclass.SubclassName\x1a*\n\x0bLegacyEvent\x12\r\n\x05table\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tB\n\n\x08identity"\xcf\x01\n\x0bHQLMetadata\x12>\n\x0bapp_surface\x18\x01 \x01(\x0e2).hql_events.TaxonomyAppSurface.AppSurface\x12G\n\x0eaction_surface\x18\x02 \x01(\x0e2/.hql_events.TaxonomyActionSurface.ActionSurface\x127\n\x11identity_override\x18\x03 \x01(\x0b2\x1c.hql_events.HQLEventIdentity:W\n\x0eevent_identity\x12\x1f.google.protobuf.MessageOptions\x18\xc3\xad\x01 \x01(\x0b2\x1c.hql_events.HQLEventIdentity:<\n\x11event_description\x12\x1f.google.protobuf.MessageOptions\x18\xc1\xad\x01 \x01(\t:7\n\x0cevent_is_pii\x12\x1f.google.protobuf.MessageOptions\x18\xbe\xad\x01 \x01(\x08:G\n\x1cidentity_provided_at_runtime\x12\x1f.google.protobuf.MessageOptions\x18\xc4\xad\x01 \x01(\x08:9\n\x0enested_message\x12\x1f.google.protobuf.MessageOptions\x18\xc5\xad\x01 \x01(\x08:,\n\x03pii\x12\x1d.google.protobuf.FieldOptions\x18\x90\xb2\x01 \x01(\x08B:\n\x1ccom.dropbox.proto.hql_eventsP\x01Z\x18dropbox/proto/hql_eventsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.proto.hql_events.extensions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.dropbox.proto.hql_eventsP\x01Z\x18dropbox/proto/hql_events'
    _globals['_HQLEVENTIDENTITY']._serialized_start = 133
    _globals['_HQLEVENTIDENTITY']._serialized_end = 660
    _globals['_HQLEVENTIDENTITY_ACTIONEVENTIDENTITY']._serialized_start = 378
    _globals['_HQLEVENTIDENTITY_ACTIONEVENTIDENTITY']._serialized_end = 466
    _globals['_HQLEVENTIDENTITY_EVENTCLASS']._serialized_start = 469
    _globals['_HQLEVENTIDENTITY_EVENTCLASS']._serialized_end = 604
    _globals['_HQLEVENTIDENTITY_LEGACYEVENT']._serialized_start = 606
    _globals['_HQLEVENTIDENTITY_LEGACYEVENT']._serialized_end = 648
    _globals['_HQLMETADATA']._serialized_start = 663
    _globals['_HQLMETADATA']._serialized_end = 870
    return None
