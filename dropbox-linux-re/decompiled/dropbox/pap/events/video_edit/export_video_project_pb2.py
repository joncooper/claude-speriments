# Source Generated with Decompyle++
# File: export_video_project_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/video_edit/export_video_project.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.proto.pap import event_state_pb2 as dropbox_dot_proto_dot_pap_dot_event__state__pb2
from dropbox.pap.events.enums import export_funnel_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_export__funnel__pb2
from dropbox.pap.events.enums import file_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_file__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8dropbox/pap/events/video_edit/export_video_project.proto\x12\x15pap.events.video_edit\x1a\x1fdropbox/proto/pap/options.proto\x1a#dropbox/proto/pap/event_state.proto\x1a,dropbox/pap/events/enums/export_funnel.proto\x1a(dropbox/pap/events/enums/file_type.proto"\xb3\x05\n\x13Export_VideoProject\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12K\n\x0bevent_class\x18\xcd\x08 \x01(\x0e25.pap.events.video_edit.Export_VideoProject.EventClass\x12%\n\x0bevent_state\x18\xce\x08 \x01(\x0e2\x0f.pap.EventState\x12\x16\n\x0eaction_element\x18\x02 \x01(\t\x128\n\rexport_funnel\x18\x03 \x01(\x0e2!.enums.export_funnel.ExportFunnel\x12\x18\n\x10video_project_id\x18\x04 \x01(\t\x12\x18\n\x10video_session_id\x18\x05 \x01(\t\x12\x1a\n\x12content_identifier\x18\x06 \x01(\t\x12\x16\n\x0efile_extension\x18\x07 \x01(\t\x12,\n\tfile_type\x18\x08 \x01(\x0e2\x19.enums.file_type.FileType\x12\x11\n\tfile_size\x18\t \x01(\x03\x12\x16\n\x0evideo_duration\x18\n \x01(\x05\x12\x18\n\x10video_frame_rate\x18\x0b \x01(\x01\x12\x12\n\nfile_codec\x18\x0c \x01(\t\x12\r\n\x05width\x18\r \x01(\x05\x12\x0e\n\x06height\x18\x0e \x01(\x05\x12\x14\n\x0caspect_ratio\x18\x0f \x01(\x01\x12\x10\n\x08duration\x18\x10 \x01(\x01\x12\x15\n\rmedia_bitrate\x18\x11 \x01(\x01\x12\x1c\n\x14num_of_text_overlays\x18\x12 \x01(\x01\x12\x1a\n\x12riviera_request_id\x18\x13 \x01(\t"\x1c\n\nEventClass\x12\x0e\n\nVIDEO_EDIT\x10\x00:\x19\xca>\x06export\xd2>\rvideo_projectB\x1fZ\x1ddropbox/pap/events/video_editb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.video_edit.export_video_project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1ddropbox/pap/events/video_edit'
    _globals['_EXPORT_VIDEOPROJECT']._loaded_options = None
    _globals['_EXPORT_VIDEOPROJECT']._serialized_options = b'\xca>\x06export\xd2>\rvideo_project'
    _globals['_EXPORT_VIDEOPROJECT']._serialized_start = 242
    _globals['_EXPORT_VIDEOPROJECT']._serialized_end = 933
    _globals['_EXPORT_VIDEOPROJECT_EVENTCLASS']._serialized_start = 878
    _globals['_EXPORT_VIDEOPROJECT_EVENTCLASS']._serialized_end = 906
    return None
