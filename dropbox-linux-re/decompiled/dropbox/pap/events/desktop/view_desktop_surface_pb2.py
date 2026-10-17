# Source Generated with Decompyle++
# File: view_desktop_surface_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/desktop/view_desktop_surface.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.pap.events.enums import tray_trigger_reason_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_tray__trigger__reason__pb2
from dropbox.pap.events.enums import file_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_file__type__pb2
from dropbox.pap.events.enums import file_category_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_file__category__pb2
from dropbox.pap.events.enums import content_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_content__type__pb2
from dropbox.pap.events.enums import tray_variant_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_tray__variant__pb2
from dropbox.pap.events.enums import desktop_nudge_location_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_desktop__nudge__location__pb2
from dropbox.pap.events.enums import desktop_sync_info_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_desktop__sync__info__pb2
from dropbox.pap.events.enums import sync_dashboard_variant_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_sync__dashboard__variant__pb2
from dropbox.pap.events.enums import view_source_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_view__source__pb2
from dropbox.pap.events.enums import slide_name_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_slide__name__pb2
from dropbox.pap.events.enums import tooltip_name_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_tooltip__name__pb2
from dropbox.pap.events.enums import notification_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_notification__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5dropbox/pap/events/desktop/view_desktop_surface.proto\x12\x12pap.events.desktop\x1a\x1fdropbox/proto/pap/options.proto\x1a2dropbox/pap/events/enums/tray_trigger_reason.proto\x1a(dropbox/pap/events/enums/file_type.proto\x1a,dropbox/pap/events/enums/file_category.proto\x1a+dropbox/pap/events/enums/content_type.proto\x1a+dropbox/pap/events/enums/tray_variant.proto\x1a5dropbox/pap/events/enums/desktop_nudge_location.proto\x1a0dropbox/pap/events/enums/desktop_sync_info.proto\x1a5dropbox/pap/events/enums/sync_dashboard_variant.proto\x1a*dropbox/pap/events/enums/view_source.proto\x1a)dropbox/pap/events/enums/slide_name.proto\x1a+dropbox/pap/events/enums/tooltip_name.proto\x1a0dropbox/pap/events/enums/notification_type.proto"\xf9\n\n\x13View_DesktopSurface\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12H\n\x0bevent_class\x18\xcd\x08 \x01(\x0e22.pap.events.desktop.View_DesktopSurface.EventClass\x12I\n\x13tray_trigger_reason\x18\x02 \x01(\x0e2,.enums.tray_trigger_reason.TrayTriggerReason\x12\x16\n\x0efile_extension\x18\x03 \x01(\t\x12,\n\tfile_type\x18\x04 \x01(\x0e2\x19.enums.file_type.FileType\x12\x11\n\tupload_id\x18\x05 \x01(\t\x12\x13\n\x0bfile_obj_id\x18\x06 \x01(\t\x128\n\rfile_category\x18\x07 \x01(\x0e2!.enums.file_category.FileCategory\x12\x15\n\roptions_shown\x18\x08 \x01(\t\x125\n\x0ccontent_type\x18\t \x01(\x0e2\x1f.enums.content_type.ContentType\x12\x14\n\x0cis_encrypted\x18\n \x01(\x08\x125\n\x0ctray_variant\x18\x0b \x01(\x0e2\x1f.enums.tray_variant.TrayVariant\x12\x17\n\x0ftray_session_id\x18\x0c \x01(\x05\x12\x16\n\x0eaction_element\x18\r \x01(\t\x12\x11\n\tnum_files\x18\x0e \x01(\x05\x12\x1f\n\x17tray_session_identifier\x18\x0f \x01(\t\x12R\n\x16desktop_nudge_location\x18\x10 \x01(\x0e22.enums.desktop_nudge_location.DesktopNudgeLocation\x12\x1a\n\x12desktop_nudge_step\x18\x11 \x01(\x05\x12\x11\n\tsync_info\x18\x12 \x01(\t\x12C\n\x11desktop_sync_info\x18\x13 \x01(\x0e2(.enums.desktop_sync_info.DesktopSyncInfo\x12\x1a\n\x12prompt_campaign_id\x18\x14 \x01(\x05\x12R\n\x16sync_dashboard_variant\x18\x15 \x01(\x0e22.enums.sync_dashboard_variant.SyncDashboardVariant\x12\x12\n\nsticky_key\x18\x16 \x01(\t\x122\n\x0bview_source\x18\x17 \x01(\x0e2\x1d.enums.view_source.ViewSource\x12\x17\n\x0fnum_sync_issues\x18\x18 \x01(\x03\x12!\n\x19hard_drive_capacity_bytes\x18\x19 \x01(\x03\x12\x1d\n\x15hard_drive_free_bytes\x18\x1a \x01(\x03\x12\x1e\n\x16hard_drive_usage_bytes\x18\x1b \x01(\x03\x12/\n\nslide_name\x18\x1c \x01(\x0e2\x1b.enums.slide_name.SlideName\x125\n\x0ctooltip_name\x18\x1d \x01(\x0e2\x1f.enums.tooltip_name.TooltipName\x12D\n\x11notification_type\x18\x1e \x01(\x0e2).enums.notification_type.NotificationType\x12\x1b\n\x13has_unsaved_changes\x18\x1f \x01(\x08\x12\x11\n\tis_pinned\x18  \x01(\x08"\x19\n\nEventClass\x12\x0b\n\x07DESKTOP\x10\x00:\x19\xca>\x04view\xd2>\x0fdesktop_surfaceB\x1cZ\x1adropbox/pap/events/desktopb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.desktop.view_desktop_surface_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1adropbox/pap/events/desktop'
    _globals['_VIEW_DESKTOPSURFACE']._loaded_options = None
    _globals['_VIEW_DESKTOPSURFACE']._serialized_options = b'\xca>\x04view\xd2>\x0fdesktop_surface'
    _globals['_VIEW_DESKTOPSURFACE']._serialized_start = 683
    _globals['_VIEW_DESKTOPSURFACE']._serialized_end = 2084
    _globals['_VIEW_DESKTOPSURFACE_EVENTCLASS']._serialized_start = 2032
    _globals['_VIEW_DESKTOPSURFACE_EVENTCLASS']._serialized_end = 2057
    return None
