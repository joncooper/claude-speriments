# Source Generated with Decompyle++
# File: markup.pyc (Python 3.11)

import uuid
from enum import StrEnum
from typing import Any, Dict, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.features.notification_dialog.constants import NotificationDialogEntryPoint
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.event_hub import EventHubAccessor
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.html_views.electron.ipc import JSONDict
from dropbox.foundation.scheme_handler.util import get_mime_type_for_ext
from dropbox.functions import file_extension
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import ServerPath
from dropbox.trace import TRACE

class MarkupStrings(UIStrings):
    markup_dialog_title = UI("Markup tool can't open online-only files")
    markup_dialog_description = UI('To open this file in markup, open Finder, right-click the file, and select <strong>Make available offline<strong>.', windows = UI('To open this file in markup, open Explorer, right-click the file, and select <strong>Make available offline<strong>.'))
    markup_dialog_button_text = UI('Open file')
    screenshot_copy_image_clipboard_message = UI('An image was copied to your clipboard.')
    screenshot_copy_image_clipboard_caption = UI('Sharing Screenshot')
    screenshots_open_in_finder = UI('Show in Finder')
    screenshots_open_in_explorer = UI('Show in Explorer')


class MarkupSource(StrEnum):
    TRAY_CONTEXT_MENU = 'tray_context_menu'
    SCREENSHOT_CONTROLLER = 'screenshot_controller'


def report_markup_event(account = None, event_name = None, session_id = None, source = (None,), extra = ('account', 'AccountInterface', 'event_name', 'str', 'session_id', 'str', 'source', 'str', 'extra', 'Optional[Dict[str, Any]]', 'return', 'None')):
    new_event = NonUserLoggingEvent(event_name = event_name, feature_session_id = session_id, action_surface = source, source = str(source), component = DesktopComponent.SCREENSHOTS, extra_hive_dict_pii = extra)
    DesktopLogger.log_event(new_event, account)


def show_markup_mev(context, source = None, session_id = None, local_path = None, server_path = ('context', 'UserContext', 'source', 'MarkupSource', 'session_id', 'Optional[str]', 'local_path', 'str', 'server_path', 'Optional[str]', 'return', 'bool')):
    session_id = str(uuid.uuid4()) if not session_id else session_id
    extension = file_extension(local_path)
    mime_type = get_mime_type_for_ext(extension)
# WARNING: Decompyle incomplete


def show_markup_notification(account, source = None, session_id = None, local_path = None, server_path = ('account', 'AccountInterface', 'source', 'NotificationDialogEntryPoint', 'session_id', 'Text', 'local_path', 'LocalPath', 'server_path', 'ServerPath', 'return', 'None')):
    session_id = str(uuid.uuid4()) if not session_id else session_id
    local_path_str = Text(local_path)
    extension = file_extension(local_path_str)
    mime_type = get_mime_type_for_ext(extension)
# WARNING: Decompyle incomplete

