# Source Generated with Decompyle++
# File: log_desktop_tray_menu_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/desktop/log_desktop_tray_menu.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.proto.pap import event_state_pb2 as dropbox_dot_proto_dot_pap_dot_event__state__pb2
from dropbox.pap.events.enums import status_label_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_status__label__pb2
from dropbox.pap.events.enums import next_status_label_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_next__status__label__pb2
from dropbox.pap.events.enums import previous_status_label_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_previous__status__label__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6dropbox/pap/events/desktop/log_desktop_tray_menu.proto\x12\x12pap.events.desktop\x1a\x1fdropbox/proto/pap/options.proto\x1a#dropbox/proto/pap/event_state.proto\x1a+dropbox/pap/events/enums/status_label.proto\x1a0dropbox/pap/events/enums/next_status_label.proto\x1a4dropbox/pap/events/enums/previous_status_label.proto"\xa2\x03\n\x13Log_DesktopTrayMenu\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12H\n\x0bevent_class\x18\xcd\x08 \x01(\x0e22.pap.events.desktop.Log_DesktopTrayMenu.EventClass\x12%\n\x0bevent_state\x18\xce\x08 \x01(\x0e2\x0f.pap.EventState\x125\n\x0cstatus_label\x18\x02 \x01(\x0e2\x1f.enums.status_label.StatusLabel\x12C\n\x11next_status_label\x18\x03 \x01(\x0e2(.enums.next_status_label.NextStatusLabel\x12O\n\x15previous_status_label\x18\x04 \x01(\x0e20.enums.previous_status_label.PreviousStatusLabel"\x19\n\nEventClass\x12\x0b\n\x07DESKTOP\x10\x00:\x1a\xca>\x03log\xd2>\x11desktop_tray_menuB\x1cZ\x1adropbox/pap/events/desktopb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.desktop.log_desktop_tray_menu_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1adropbox/pap/events/desktop'
    _globals['_LOG_DESKTOPTRAYMENU']._loaded_options = None
    _globals['_LOG_DESKTOPTRAYMENU']._serialized_options = b'\xca>\x03log\xd2>\x11desktop_tray_menu'
    _globals['_LOG_DESKTOPTRAYMENU']._serialized_start = 298
    _globals['_LOG_DESKTOPTRAYMENU']._serialized_end = 716
    _globals['_LOG_DESKTOPTRAYMENU_EVENTCLASS']._serialized_start = 663
    _globals['_LOG_DESKTOPTRAYMENU_EVENTCLASS']._serialized_end = 688
    return None
