# Source Generated with Decompyle++
# File: click_tray_menu_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/tray/click_tray_menu.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-dropbox/pap/events/tray/click_tray_menu.proto\x12\x0fpap.events.tray\x1a\x1fdropbox/proto/pap/options.proto"\xc5\x01\n\x0eClick_TrayMenu\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12@\n\x0bevent_class\x18\xcd\x08 \x01(\x0e2*.pap.events.tray.Click_TrayMenu.EventClass\x12\x14\n\x0csnooze_event\x18\x02 \x01(\t\x12\x15\n\rtime_interval\x18\x03 \x01(\t"\x16\n\nEventClass\x12\x08\n\x04TRAY\x10\x00:\x14\xca>\x05click\xd2>\ttray_menuB\x19Z\x17dropbox/pap/events/trayb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.tray.click_tray_menu_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x17dropbox/pap/events/tray'
    _globals['_CLICK_TRAYMENU']._loaded_options = None
    _globals['_CLICK_TRAYMENU']._serialized_options = b'\xca>\x05click\xd2>\ttray_menu'
    _globals['_CLICK_TRAYMENU']._serialized_start = 100
    _globals['_CLICK_TRAYMENU']._serialized_end = 297
    _globals['_CLICK_TRAYMENU_EVENTCLASS']._serialized_start = 253
    _globals['_CLICK_TRAYMENU_EVENTCLASS']._serialized_end = 275
    return None
