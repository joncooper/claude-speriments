# Source Generated with Decompyle++
# File: mixin.pyc (Python 3.11)

from typing import Any, Callable, Dict, List, Optional, Text
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes, IconType
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.uikit import Closeable
from dropbox.foundation.futures import Future
from dropbox.threadutils import SafeValue
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.multiaccount.selector import MultiAccountSelector

class LowUIMixin:
    dialog_controller: 'DialogController' = 'LowUIMixin'
    
    def __init__(self = None, app = None):
        self._app = app

    
    def show_electron_blocking_dialog(self, caption, message, buttons, checkbox_text, callback, keep_open = None, left_buttons = None, no_warning = None, allows_closing = (None, None, False, None, False, False, DialogSourceTypes.OTHER), dialog_source_type = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'checkbox_text', 'Optional[Text]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'keep_open', 'bool', 'left_buttons', 'Optional[List[Text]]', 'no_warning', 'bool', 'allows_closing', 'bool', 'dialog_source_type', 'DialogSourceTypes', 'return', 'Future[Optional[int]]')):
        pass

    
    def show_electron_non_blocking_dialog(self, caption, message, buttons, checkbox_text, callback, keep_open = None, left_buttons = None, no_warning = None, allows_closing = (None, None, False, None, False, False, DialogSourceTypes.OTHER), dialog_source_type = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'checkbox_text', 'Optional[Text]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'keep_open', 'bool', 'left_buttons', 'Optional[List[Text]]', 'no_warning', 'bool', 'allows_closing', 'bool', 'dialog_source_type', 'DialogSourceTypes', 'return', 'SafeValue[Closeable]')):
        pass

    
    def show_native_non_blocking_dialog(self, caption, message, buttons, left_buttons, checkbox_text, default_button_id, callback, icon = None, keep_open = None, allows_closing = None, steal_focus = (None, None, 0, None, IconType.WARN, False, False, False, DialogSourceTypes.OTHER), dialog_source_type = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'left_buttons', 'Optional[List[Text]]', 'checkbox_text', 'Optional[Text]', 'default_button_id', 'int', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'icon', 'IconType', 'keep_open', 'bool', 'allows_closing', 'bool', 'steal_focus', 'bool', 'dialog_source_type', 'DialogSourceTypes', 'return', 'SafeValue[Closeable]')):
        pass
    # WARNING: Decompyle incomplete

    
    def show_native_blocking_dialog(self, caption, message, buttons, checkbox_text, default_button_id, callback, icon = None, allows_closing = None, steal_focus = None, help_link = (None, 0, None, IconType.WARN, False, False, None, DialogSourceTypes.OTHER), dialog_source_type = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'checkbox_text', 'Optional[Text]', 'default_button_id', 'int', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'icon', 'IconType', 'allows_closing', 'bool', 'steal_focus', 'bool', 'help_link', 'Optional[Text]', 'dialog_source_type', 'DialogSourceTypes', 'return', 'Future[Optional[int]]')):
        pass
    # WARNING: Decompyle incomplete

    
    def show_screenshots_dialog(self, always_cb, never_cb = None, close_cb = None, is_linked = None, mbox_selector = (False, None, None), confirm_choice_text = ('always_cb', 'Callable[[Optional[int]], None]', 'never_cb', 'Callable[[], None]', 'close_cb', 'Callable[[], None]', 'is_linked', 'bool', 'mbox_selector', 'Optional[MultiAccountSelector]', 'confirm_choice_text', 'Optional[Dict[str, Text]]', 'return', 'None')):
        pass

    
    def show_screenshots_selsync_dialog(self = None, turn_off_selsync_cb = None, turn_off_screenshots_cb = None, close_cb = ('turn_off_selsync_cb', 'Callable[[], None]', 'turn_off_screenshots_cb', 'Callable[[], None]', 'close_cb', 'Callable[[], None]', 'return', 'None')):
        pass

    
    def show_office_addin_prompt(self = None, accept_cb = None, decline_cb = None, close_cb = ('accept_cb', 'Callable[[], Any]', 'decline_cb', 'Callable[[], Any]', 'close_cb', 'Callable[[], Any]', 'return', 'None')):
        pass


