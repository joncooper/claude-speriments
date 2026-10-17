# Source Generated with Decompyle++
# File: copy_capture_shared_link_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/share/copy_capture_shared_link.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.proto.pap import event_state_pb2 as dropbox_dot_proto_dot_pap_dot_event__state__pb2
from dropbox.pap.events.enums import shared_link_origin_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_shared__link__origin__pb2
from dropbox.pap.events.enums import share_link_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_share__link__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7dropbox/pap/events/share/copy_capture_shared_link.proto\x12\x10pap.events.share\x1a\x1fdropbox/proto/pap/options.proto\x1a#dropbox/proto/pap/event_state.proto\x1a1dropbox/pap/events/enums/shared_link_origin.proto\x1a.dropbox/pap/events/enums/share_link_type.proto"\xcf\x03\n\x16Copy_CaptureSharedLink\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12I\n\x0bevent_class\x18\xcd\x08 \x01(\x0e23.pap.events.share.Copy_CaptureSharedLink.EventClass\x12%\n\x0bevent_state\x18\xce\x08 \x01(\x0e2\x0f.pap.EventState\x12\x1d\n\x15is_capture_over_quota\x18\x02 \x01(\x08\x12F\n\x12shared_link_origin\x18\x03 \x01(\x0e2*.enums.shared_link_origin.SharedLinkOrigin\x12\x17\n\x0fshared_link_url\x18\x04 \x01(\t\x12=\n\x0fshare_link_type\x18\x05 \x01(\x0e2$.enums.share_link_type.ShareLinkType\x12\x0e\n\x06timing\x18\x06 \x01(\t\x12\x14\n\x0cerror_reason\x18\x07 \x01(\t\x12\x0e\n\x06is_dir\x18\x08 \x01(\x08"\x17\n\nEventClass\x12\t\n\x05SHARE\x10\x00:\x1d\xca>\x04copy\xd2>\x13capture_shared_linkB\x1aZ\x18dropbox/pap/events/shareb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.share.copy_capture_shared_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x18dropbox/pap/events/share'
    _globals['_COPY_CAPTURESHAREDLINK']._loaded_options = None
    _globals['_COPY_CAPTURESHAREDLINK']._serialized_options = b'\xca>\x04copy\xd2>\x13capture_shared_link'
    _globals['_COPY_CAPTURESHAREDLINK']._serialized_start = 247
    _globals['_COPY_CAPTURESHAREDLINK']._serialized_end = 710
    _globals['_COPY_CAPTURESHAREDLINK_EVENTCLASS']._serialized_start = 656
    _globals['_COPY_CAPTURESHAREDLINK_EVENTCLASS']._serialized_end = 679
    return None
