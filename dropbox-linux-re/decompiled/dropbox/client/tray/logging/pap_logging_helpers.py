# Source Generated with Decompyle++
# File: pap_logging_helpers.pyc (Python 3.11)

from typing import Any, Dict, Optional, Union
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventState as DesktopEventState
from dropbox.client.features.desktop_logging.logging_event import PAPLoggingEvent
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import sanitize_event_extra_dict
from dropbox.pap.events.desktop.select_desktop_surface_action_pb2 import Select_DesktopSurfaceAction
from dropbox.pap.events.desktop.view_desktop_surface_pb2 import View_DesktopSurface
from dropbox.pap.events.enums.account_menu_items_navigation_pb2 import AccountMenuItemsNavigation
from dropbox.pap.events.enums.content_action_pb2 import ContentAction
from dropbox.pap.events.enums.desktop_surface_action_pb2 import DesktopSurfaceAction
from dropbox.pap.events.enums.preferences_menu_items_navigation_pb2 import PreferencesMenuItemsNavigation
from dropbox.pap.events.enums.tray_trigger_reason_pb2 import TrayTriggerReason as PAPTrayTriggerReason
from dropbox.pap.events.enums.tray_variant_pb2 import TrayVariant
from dropbox.pap.events.enums.view_source_pb2 import ViewSource
from dropbox.pap.events.navigation.select_content_action_pb2 import Select_ContentAction
from dropbox.proto.pap.event_state_pb2 import EventState
SOURCE_TRAY = 'tray'
ACCOUNT_MENU_ITEMS = 'account_menu_items'
SOURCE_PREFERENCES = 'preferences'

def convert_to_content_action(action = None):
    if action == 'share':
        return ContentAction.SHARE
    if None == 'copy_link':
        return ContentAction.COPY_LINK
    if None == 'copy_url':
        return ContentAction.COPY_URL
    if None == 'open_notifications':
        return ContentAction.OPEN_NOTIFICATIONS
    if None == 'open_resource':
        return ContentAction.OPEN_FILE
    if None in frozenset({'preview_file_locally', 'preview_file_locally_rich_tool_tip_shown', 'preview_file_locally_rich_tool_tip_try_it', 'preview_file_locally_rich_tool_tip_not_now'}):
        return ContentAction.OPEN_PREVIEW
    if None == 'preview_file_on_web':
        return ContentAction.PREVIEW_FILE
    return None.UNKNOWN


def convert_to_event_state_enum(event_state = None):
    if event_state == 'canceled':
        return EventState.CANCELED
    if None == 'failed':
        return EventState.FAILED
    if None == 'rejected':
        return EventState.REJECTED
    if None == 'start':
        return EventState.START
    if None == 'success':
        return EventState.SUCCESS


def get_select_tray_assistant_action_pap_event(action = None, session_id = None, is_encrypted = None, file_extension = (False, None, None), hive_extra = ('action', 'str', 'session_id', 'str', 'is_encrypted', 'Optional[bool]', 'file_extension', 'Optional[str]', 'hive_extra', 'Optional[Dict[str, Any]]', 'return', 'PAPLoggingEvent')):
    extra_hive_dict_nopii = { }
# WARNING: Decompyle incomplete


def convert_tray_trigger_reason_to_enum(tray_trigger_reason = None):
    if tray_trigger_reason == TrayTriggerReason.TRAY_ICON_CLICK:
        return PAPTrayTriggerReason.TRAY_ICON_CLICK
    if None == TrayTriggerReason.TRAY_RUN_ICON_CLICK:
        return PAPTrayTriggerReason.TRAY_RUN_ICON_CLICK
    if None == TrayTriggerReason.TRAY_MENU:
        return PAPTrayTriggerReason.TRAY_MENU
    if None == TrayTriggerReason.NOTIFICATIONS:
        return PAPTrayTriggerReason.NOTIFICATIONS
    if None == TrayTriggerReason.LEGACY_UI_LAUNCHER:
        return PAPTrayTriggerReason.LEGACY_UI_LAUNCHER
    if None == TrayTriggerReason.LEGACY_VIEW_MANAGER:
        return PAPTrayTriggerReason.LEGACY_VIEW_MANAGER
    if None == TrayTriggerReason.LEGACY_NOTIFICATIONS:
        return PAPTrayTriggerReason.LEGACY_NOTIFICATIONS
    if None == TrayTriggerReason.LEGACY_POPUP_ALT_MENU:
        return PAPTrayTriggerReason.LEGACY_POPUP_ALT_MENU
    if None == TrayTriggerReason.TRAY_DEBUG:
        return PAPTrayTriggerReason.TRAY_DEBUG


def get_select_tray_assistant_pap_event(session_id = None, tray_trigger_reason = None, hive_extra = None, tray_session_identifier = (None, None, None), tray_variant = ('session_id', 'Optional[str]', 'tray_trigger_reason', 'Optional[TrayTriggerReason]', 'hive_extra', 'Optional[Dict[str, Any]]', 'tray_session_identifier', 'Optional[str]', 'tray_variant', 'Optional[TrayVariant.V]', 'return', 'PAPLoggingEvent')):
    extra_hive_dict_nopii = { }
# WARNING: Decompyle incomplete


def convert_to_account_menu_items_navigation_enum(account_menu_items_navigation = None):
    if account_menu_items_navigation == 'open_dropbox_folder':
        return AccountMenuItemsNavigation.OPEN_DROPBOX_FOLDER
    if None == 'launch_dropbox_website':
        return AccountMenuItemsNavigation.LAUNCH_DROPBOX_WEBSITE
    if None == 'help':
        return AccountMenuItemsNavigation.HELP
    if None == 'report_bug':
        return AccountMenuItemsNavigation.REPORT_BUG
    if None == 'admin_console':
        return AccountMenuItemsNavigation.ADMIN_CONSOLE
    if None == 'open_recent_file':
        return AccountMenuItemsNavigation.OPEN_RECENT_FILE
    return None.UNKNOWN


def get_account_menu_pap_event_low_ui(session_id = None, action_surface = None, action_element = None, account_menu_items_navigation = (None, None), hive_extra = ('session_id', 'Optional[str]', 'action_surface', 'str', 'action_element', 'str', 'account_menu_items_navigation', 'Optional[str]', 'hive_extra', 'Optional[Dict[str, Any]]', 'return', 'PAPLoggingEvent')):
    extra_hive_dict_nopii = { }
# WARNING: Decompyle incomplete


def get_select_desktop_surface_pap_event_low_ui(session_id, action_element = None, snooze_event = None, hive_extra = None, target_object_key = (None, None, None, None), entry_point = ('session_id', 'Optional[str]', 'action_element', 'str', 'snooze_event', 'Optional[str]', 'hive_extra', 'Optional[Dict[str, Any]]', 'target_object_key', 'Optional[str]', 'entry_point', 'Optional[str]', 'return', 'PAPLoggingEvent')):
    extra_hive_dict_nopii = { }
# WARNING: Decompyle incomplete


def get_preferences_menu_pap_event_low_ui(session_id = None, action_surface = None, action_element = None, preferences_menu_items_navigation = (None, None), hive_extra = ('session_id', 'Optional[str]', 'action_surface', 'str', 'action_element', 'str', 'preferences_menu_items_navigation', 'Optional[str]', 'hive_extra', 'Optional[Dict[str, Any]]', 'return', 'PAPLoggingEvent')):
    extra_hive_dict_nopii = { }
# WARNING: Decompyle incomplete


def convert_to_preferences_menu_items_navigation_enum(preferences_menu_item_navigation = None):
    if preferences_menu_item_navigation == 'start_dbx_at_startup':
        return PreferencesMenuItemsNavigation.START_DBX_AT_STARTUP
    if None == 'language':
        return PreferencesMenuItemsNavigation.LANGUAGE
    if None == 'unlink':
        return PreferencesMenuItemsNavigation.UNLINK
    if None == 'network':
        return PreferencesMenuItemsNavigation.NETWORK
    if None == 'notifications':
        return PreferencesMenuItemsNavigation.NOTIFICATIONS
    if None == 'selsync':
        return PreferencesMenuItemsNavigation.SELSYNC
    if None == 'move_dbx_folder':
        return PreferencesMenuItemsNavigation.MOVE_DBX_FOLDER
    if None == 'sync_defaults':
        return PreferencesMenuItemsNavigation.SYNC_DEFAULTS
    if None == 'screenshots':
        return PreferencesMenuItemsNavigation.SCREENSHOTS
    if None == 'camera_uploads':
        return PreferencesMenuItemsNavigation.CAMERA_UPLOADS
    if None == 'disable_backup':
        return PreferencesMenuItemsNavigation.DISABLE_BACKUP
    if None == 'delete_external_drive_backup':
        return PreferencesMenuItemsNavigation.DELETE_EXTERNAL_DRIVE_BACKUP
    return None.UNKNOWN


def _to_desktop_event_state(event_state = None):
    if event_state == 'start':
        return DesktopEventState.START
    if None == 'success':
        return DesktopEventState.SUCCESS
    if None == 'failed':
        return DesktopEventState.FAILED
    if None == 'canceled':
        return DesktopEventState.CANCELED
    if None == 'rejected':
        return DesktopEventState.REJECTED


def log_select_desktop_surface_action_tray_low_ui(account, session_id, action_element, account_menu_items_navigation, snooze_event, preferences_menu_items_navigation = None, hive_extra = None, target_object_key = None, entry_point = (None, None, None, None, None, None, None), event_state = ('account', 'Optional[AccountInterface]', 'session_id', 'Optional[str]', 'action_element', 'str', 'account_menu_items_navigation', 'Optional[str]', 'snooze_event', 'Optional[str]', 'preferences_menu_items_navigation', 'Optional[str]', 'hive_extra', 'Optional[Dict[str, Any]]', 'target_object_key', 'Optional[str]', 'entry_point', 'Optional[str]', 'event_state', 'Optional[str]', 'return', 'None')):
    event = None
    if action_element == ACCOUNT_MENU_ITEMS:
        event = get_account_menu_pap_event_low_ui(session_id = session_id, action_surface = SOURCE_TRAY, action_element = action_element, account_menu_items_navigation = account_menu_items_navigation, hive_extra = hive_extra)
# WARNING: Decompyle incomplete


def get_view_desktop_surface_pap_event_low_ui(session_id = None, tray_trigger_reason = None, hive_extra = None):
    extra_hive_dict_nopii = { }
# WARNING: Decompyle incomplete


def log_view_desktop_surface_tray_assistant_low_ui(account = None, session_id = None, tray_trigger_reason = None, hive_extra = (None,)):
    event = get_view_desktop_surface_pap_event_low_ui(session_id = session_id, tray_trigger_reason = tray_trigger_reason, hive_extra = hive_extra)
    DesktopLogger.log_event(event = event, account = account)


def convert_view_source_to_enum(view_source = None):
    if view_source == 'tray':
        return ViewSource.TRAY
    if None == 'keyboard':
        return ViewSource.KEYBOARD
    if None == 'dock_icon':
        return ViewSource.DOCK_ICON
    if None == 'desktop_shortcut':
        return ViewSource.DESKTOP_SHORTCUT
    return None.UNKNOWN


def convert_tray_variant_to_enum(tray_variant = None):
    if tray_variant == 'bridge':
        return TrayVariant.BRIDGE
    if None == 'mev':
        return TrayVariant.MEV
    if None == 'low_ui':
        return TrayVariant.LOW_UI
    return None.UNKNOWN


def log_view_desktop_surface_launcher(account = None, session_id = None, view_source = None, hive_extra = (None,)):
    extra_hive_dict_nopii = { }
# WARNING: Decompyle incomplete


def log_select_tray_assistant(account, session_id = None, tray_trigger_reason = None, hive_extra = None, tray_session_identifier = (None, None, None), tray_variant = ('account', 'Optional[AccountInterface]', 'session_id', 'Optional[str]', 'tray_trigger_reason', 'Optional[TrayTriggerReason]', 'hive_extra', 'Optional[Dict[str, Any]]', 'tray_session_identifier', 'Optional[str]', 'tray_variant', 'Optional[TrayVariant.V]', 'return', 'None')):
    event = get_select_tray_assistant_pap_event(session_id = session_id, tray_trigger_reason = tray_trigger_reason, hive_extra = hive_extra, tray_session_identifier = tray_session_identifier, tray_variant = tray_variant)
    DesktopLogger.log_event(event = event, account = account)


def log_select_desktop_surface_action_dash_launcher(account, session_id = None, action_surface = None, desktop_surface_action = None, tray_session_identifier = (None, None), hive_extra = ('account', 'Optional[AccountInterface]', 'session_id', 'str', 'action_surface', 'str', 'desktop_surface_action', 'DesktopSurfaceAction.V', 'tray_session_identifier', 'Optional[str]', 'hive_extra', 'Optional[Dict[str, Any]]', 'return', 'None')):
    extra_hive_dict_nopii = { }
# WARNING: Decompyle incomplete


def log_tray_sticky_action(account = None, desktop_surface_action = None, session_id = None, sticky_key = (None, None, TrayVariant.MEV), tray_variant = ('account', 'Optional[AccountInterface]', 'desktop_surface_action', 'DesktopSurfaceAction.V', 'session_id', 'Optional[str]', 'sticky_key', 'Optional[str]', 'tray_variant', 'Union[TrayVariant.V, None]', 'return', 'None')):
    pap_event_kwargs = {
        'action_surface': SOURCE_TRAY,
        'action_element': 'sticky_notification',
        'desktop_surface_action': desktop_surface_action,
        'sticky_key': sticky_key }
# WARNING: Decompyle incomplete


def log_tray_sticky_view(account = None, session_id = None, sticky_key = None, tray_variant = (None, None, TrayVariant.MEV)):
    pap_event_kwargs = {
        'action_surface': SOURCE_TRAY,
        'sticky_key': sticky_key }
# WARNING: Decompyle incomplete


def log_finder_view_from_dock_icon(account = None):
    event = PAPLoggingEvent(pap_event = View_DesktopSurface(action_surface = 'file_system', view_source = convert_view_source_to_enum('dock_icon')), component = DesktopComponent.DESKTOP_APP, source = 'dock_icon')
    DesktopLogger.log_event(event = event, account = account)

