# Source Generated with Decompyle++
# File: select_desktop_surface_action_pb2.pyc (Python 3.11)

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 33, 6, '', 'dropbox/pap/events/desktop/select_desktop_surface_action.proto')
_sym_db = _symbol_database.Default()
from dropbox.proto.pap import options_pb2 as dropbox_dot_proto_dot_pap_dot_options__pb2
from dropbox.proto.pap import event_state_pb2 as dropbox_dot_proto_dot_pap_dot_event__state__pb2
from dropbox.pap.events.enums import desktop_surface_action_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_desktop__surface__action__pb2
from dropbox.pap.events.enums import tray_variant_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_tray__variant__pb2
from dropbox.pap.events.enums import account_menu_items_navigation_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_account__menu__items__navigation__pb2
from dropbox.pap.events.enums import navigation_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_navigation__pb2
from dropbox.pap.events.enums import file_category_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_file__category__pb2
from dropbox.pap.events.enums import file_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_file__type__pb2
from dropbox.pap.events.enums import selected_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_selected__pb2
from dropbox.pap.events.enums import preferences_menu_items_navigation_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_preferences__menu__items__navigation__pb2
from dropbox.pap.events.enums import sync_dashboard_variant_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_sync__dashboard__variant__pb2
from dropbox.pap.events.enums import slide_name_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_slide__name__pb2
from dropbox.pap.events.enums import language_code_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_language__code__pb2
from dropbox.pap.events.enums import theme_preference_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_theme__preference__pb2
from dropbox.pap.events.enums import desktop_surface_action_value_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_desktop__surface__action__value__pb2
from dropbox.pap.events.enums import account_role_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_account__role__pb2
from dropbox.pap.events.enums import notification_type_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_notification__type__pb2
from dropbox.pap.events.enums import desktop_surface_action_previous_value_pb2 as dropbox_dot_pap_dot_events_dot_enums_dot_desktop__surface__action__previous__value__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>dropbox/pap/events/desktop/select_desktop_surface_action.proto\x12\x12pap.events.desktop\x1a\x1fdropbox/proto/pap/options.proto\x1a#dropbox/proto/pap/event_state.proto\x1a5dropbox/pap/events/enums/desktop_surface_action.proto\x1a+dropbox/pap/events/enums/tray_variant.proto\x1a<dropbox/pap/events/enums/account_menu_items_navigation.proto\x1a)dropbox/pap/events/enums/navigation.proto\x1a,dropbox/pap/events/enums/file_category.proto\x1a(dropbox/pap/events/enums/file_type.proto\x1a\'dropbox/pap/events/enums/selected.proto\x1a@dropbox/pap/events/enums/preferences_menu_items_navigation.proto\x1a5dropbox/pap/events/enums/sync_dashboard_variant.proto\x1a)dropbox/pap/events/enums/slide_name.proto\x1a,dropbox/pap/events/enums/language_code.proto\x1a/dropbox/pap/events/enums/theme_preference.proto\x1a;dropbox/pap/events/enums/desktop_surface_action_value.proto\x1a+dropbox/pap/events/enums/account_role.proto\x1a0dropbox/pap/events/enums/notification_type.proto\x1aDdropbox/pap/events/enums/desktop_surface_action_previous_value.proto"\xcd\x0e\n\x1bSelect_DesktopSurfaceAction\x12\x16\n\x0eaction_surface\x18\x01 \x01(\t\x12P\n\x0bevent_class\x18\xcd\x08 \x01(\x0e2:.pap.events.desktop.Select_DesktopSurfaceAction.EventClass\x12%\n\x0bevent_state\x18\xce\x08 \x01(\x0e2\x0f.pap.EventState\x12R\n\x16desktop_surface_action\x18\x02 \x01(\x0e22.enums.desktop_surface_action.DesktopSurfaceAction\x125\n\x0ctray_variant\x18\x03 \x01(\x0e2\x1f.enums.tray_variant.TrayVariant\x12\x17\n\x0ftray_session_id\x18\x04 \x01(\x05\x12\x16\n\x0eaction_element\x18\x05 \x01(\t\x12f\n\x1daccount_menu_items_navigation\x18\x06 \x01(\x0e2?.enums.account_menu_items_navigation.AccountMenuItemsNavigation\x120\n\nnavigation\x18\x07 \x01(\x0e2\x1c.enums.navigation.Navigation\x128\n\rfile_category\x18\x08 \x01(\x0e2!.enums.file_category.FileCategory\x12,\n\tfile_type\x18\t \x01(\x0e2\x19.enums.file_type.FileType\x12\x16\n\x0efile_extension\x18\n \x01(\t\x12\x11\n\tis_shared\x18\x0b \x01(\x08\x12\x13\n\x0bfile_obj_id\x18\x0c \x01(\t\x12\x14\n\x0cis_encrypted\x18\r \x01(\x08\x12\x11\n\tupload_id\x18\x0e \x01(\t\x12\x11\n\tnum_files\x18\x0f \x01(\x05\x12\x13\n\x0bfilter_type\x18\x10 \x01(\t\x12\x13\n\x0bdate_filter\x18\x11 \x01(\t\x12\x19\n\x11file_type_filters\x18\x12 \x01(\t\x12\x19\n\x11target_object_key\x18\x13 \x01(\t\x12*\n\x08selected\x18\x14 \x01(\x0e2\x18.enums.selected.Selected\x12\x14\n\x0csnooze_event\x18\x15 \x01(\t\x12r\n!preferences_menu_items_navigation\x18\x16 \x01(\x0e2G.enums.preferences_menu_items_navigation.PreferencesMenuItemsNavigation\x12\x1f\n\x17tray_session_identifier\x18\x17 \x01(\t\x12\x1a\n\x12prompt_campaign_id\x18\x18 \x01(\x05\x12R\n\x16sync_dashboard_variant\x18\x19 \x01(\x0e22.enums.sync_dashboard_variant.SyncDashboardVariant\x12\x12\n\nsticky_key\x18\x1a \x01(\t\x12\x13\n\x0bentry_point\x18\x1b \x01(\t\x12/\n\nslide_name\x18\x1c \x01(\x0e2\x1b.enums.slide_name.SlideName\x12\x18\n\x10is_preference_on\x18\x1d \x01(\x08\x128\n\rlanguage_code\x18\x1e \x01(\x0e2!.enums.language_code.LanguageCode\x12A\n\x10theme_preference\x18\x1f \x01(\x0e2\'.enums.theme_preference.ThemePreference\x12c\n\x1cdesktop_surface_action_value\x18  \x01(\x0e2=.enums.desktop_surface_action_value.DesktopSurfaceActionValue\x125\n\x0caccount_role\x18! \x01(\x0e2\x1f.enums.account_role.AccountRole\x12D\n\x11notification_type\x18" \x01(\x0e2).enums.notification_type.NotificationType\x12\x10\n\x08position\x18# \x01(\t\x12\x19\n\x11dash_connector_id\x18$ \x01(\t\x12}\n%desktop_surface_action_previous_value\x18% \x01(\x0e2N.enums.desktop_surface_action_previous_value.DesktopSurfaceActionPreviousValue"\x19\n\nEventClass\x12\x0b\n\x07DESKTOP\x10\x00:"\xca>\x06select\xd2>\x16desktop_surface_actionB\x1cZ\x1adropbox/pap/events/desktopb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dropbox.pap.events.desktop.select_desktop_surface_action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z\x1adropbox/pap/events/desktop'
    _globals['_SELECT_DESKTOPSURFACEACTION']._loaded_options = None
    _globals['_SELECT_DESKTOPSURFACEACTION']._serialized_options = b'\xca>\x06select\xd2>\x16desktop_surface_action'
    _globals['_SELECT_DESKTOPSURFACEACTION']._serialized_start = 976
    _globals['_SELECT_DESKTOPSURFACEACTION']._serialized_end = 2845
    _globals['_SELECT_DESKTOPSURFACEACTION_EVENTCLASS']._serialized_start = 2784
    _globals['_SELECT_DESKTOPSURFACEACTION_EVENTCLASS']._serialized_end = 2809
    return None
