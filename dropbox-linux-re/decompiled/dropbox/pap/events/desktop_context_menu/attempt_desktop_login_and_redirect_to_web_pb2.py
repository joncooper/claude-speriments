# Source Generated with Decompyle++
# File: attempt_desktop_login_and_redirect_to_web_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/desktop_context_menu/attempt_desktop_login_and_redirect_to_web.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nWdropbox/pap/events/desktop_context_menu/attempt_desktop_login_and_redirect_to_web.proto\x12\x1fpap.events.desktop_context_menu\x1a\x1fdropbox/proto/pap/options.proto"\xda\x02\n$Attempt_DesktopLoginAndRedirectToWeb\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12f\n\x0bevent_class\x18\xcd\x08 \x01(\x0e2P.pap.events.desktop_context_menu.Attempt_DesktopLoginAndRedirectToWeb.EventClass\x12\x1d\n\x15onboarding_session_id\x18\x02 \x01(\t\x12\x1c\n\x14installer_session_id\x18\x03 \x01(\t\x12\x1d\n\x15is_apex_flush_enabled\x18\x04 \x01(\x08"&\n\nEventClass\x12\x18\n\x14DESKTOP_CONTEXT_MENU\x10\x00:.\xca>\x07attempt\xd2>!desktop_login_and_redirect_to_webB)Z\'dropbox/pap/events/desktop_context_menub\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.desktop_context_menu.attempt_desktop_login_and_redirect_to_web_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"Z'dropbox/pap/events/desktop_context_menu"
    _globals['_ATTEMPT_DESKTOPLOGINANDREDIRECTTOWEB']._loaded_options = None
    _globals['_ATTEMPT_DESKTOPLOGINANDREDIRECTTOWEB']._serialized_options = b'\xca>\x07attempt\xd2>!desktop_login_and_redirect_to_web'
    _globals['_ATTEMPT_DESKTOPLOGINANDREDIRECTTOWEB']._serialized_start = 158
    _globals['_ATTEMPT_DESKTOPLOGINANDREDIRECTTOWEB']._serialized_end = 504
    _globals['_ATTEMPT_DESKTOPLOGINANDREDIRECTTOWEB_EVENTCLASS']._serialized_start = 418
    _globals['_ATTEMPT_DESKTOPLOGINANDREDIRECTTOWEB_EVENTCLASS']._serialized_end = 456
    return None
