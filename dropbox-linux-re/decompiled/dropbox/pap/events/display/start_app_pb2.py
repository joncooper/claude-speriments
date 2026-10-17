# Source Generated with Decompyle++
# File: start_app_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/display/start_app.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.proto.pap import event_state_pb2 as dropbox_dot_proto_dot_pap_dot_event__state__pb2
from dropbox.pap.events.enums import app_start_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_app__start__type__pb2
from dropbox.pap.events.enums import app_start_failure_reason_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_app__start__failure__reason__pb2
from dropbox.pap.events.enums import status_label_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_status__label__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*dropbox/pap/events/display/start_app.proto\x12\x12pap.events.display\x1a\x1fdropbox/proto/pap/options.proto\x1a#dropbox/proto/pap/event_state.proto\x1a-dropbox/pap/events/enums/app_start_type.proto\x1a7dropbox/pap/events/enums/app_start_failure_reason.proto\x1a+dropbox/pap/events/enums/status_label.proto"\xa5\x03\n\tStart_App\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12>\n\x0bevent_class\x18\xcd\x08 \x01(\x0e2(.pap.events.display.Start_App.EventClass\x12%\n\x0bevent_state\x18\xce\x08 \x01(\x0e2\x0f.pap.EventState\x12:\n\x0eapp_start_type\x18\x02 \x01(\x0e2".enums.app_start_type.AppStartType\x12"\n\x1aactivity_launch_class_name\x18\x03 \x01(\t\x12W\n\x18app_start_failure_reason\x18\x04 \x01(\x0e25.enums.app_start_failure_reason.AppStartFailureReason\x125\n\x0cstatus_label\x18\x05 \x01(\x0e2\x1f.enums.status_label.StatusLabel"\x19\n\nEventClass\x12\x0b\n\x07DISPLAY\x10\x00:\x0e\xca>\x05start\xd2>\x03appB\x1cZ\x1adropbox/pap/events/displayb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.display.start_app_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1adropbox/pap/events/display'
    _globals['_START_APP']._loaded_options = None
    _globals['_START_APP']._serialized_options = b'\xca>\x05start\xd2>\x03app'
    _globals['_START_APP']._serialized_start = 286
    _globals['_START_APP']._serialized_end = 707
    _globals['_START_APP_EVENTCLASS']._serialized_start = 666
    _globals['_START_APP_EVENTCLASS']._serialized_end = 691
    return None
