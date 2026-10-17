# Source Generated with Decompyle++
# File: dialogs.pyc (Python 3.11)

from typing import Callable, List, Optional, Text, Union
from apex.metrics import Metric
from build_number import is_electron_application, IS_MAC, IS_WINDOWS
from build_number.platform import IS_LINUX
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes, IconType
from dropbox.client.ui.common.uikit import Closeable, FrameworkProps, on_ui_thread, on_ui_thread_blocking, report_ui_framework_event_restricted
from dropbox.client.ui.linux.dialogs import GtkDialogController
from dropbox.client.util import safe_print
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.electron_dialogs import ElectronDialogController
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility
if IS_MAC:
    from dropbox.client.ui.cocoa.dialogs import modern_alert_dialog, show_alert_dialog
elif IS_WINDOWS:
    from dropbox.client.ui.win32.dialogs import TaskDialogController

class DummyNativeDialogController:
    show_blocking_alert_dialog = (lambda self, caption, message, buttons, checkbox_text, default_button_id, callback = None, icon = None, allows_closing = on_ui_thread_blocking(), steal_focus = (None, 0, None, IconType.WARN, False, False, None), help_link = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'checkbox_text', 'Optional[Text]', 'default_button_id', 'int', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'icon', 'IconType', 'allows_closing', 'bool', 'steal_focus', 'bool', 'help_link', 'Optional[Text]', 'return', 'Future[Optional[int]]'): safe_print(f'''\n[ALERT: {caption}]\n{message}\n''')if callback:
callback(None, None)ResolvedFuture(None))()
    show_non_blocking_alert_dialog = (lambda self, caption, message, buttons, left_buttons, checkbox_text, default_button_id, callback = None, icon = None, keep_open = on_ui_thread(), allows_closing = (None, None, 0, None, IconType.WARN, False, False, False), steal_focus = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'left_buttons', 'Optional[List[Text]]', 'checkbox_text', 'Optional[Text]', 'default_button_id', 'int', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'icon', 'IconType', 'keep_open', 'bool', 'allows_closing', 'bool', 'steal_focus', 'bool', 'return', 'Closeable'): safe_print(f'''\n[ALERT: {caption}]\n{message}\n''')if callback:
callback(None, None)Closeable((lambda : pass))
)()


class NativeDialogController:
    
    def __init__(self = None):
        if IS_MAC:
            self._macos_blocking_alert_dialog = show_alert_dialog
            self._macos_nonblocking_alert_dialog = modern_alert_dialog
            return None
        if None:
            self._tdc = TaskDialogController()
            return None
        if None:
            self._gtk = GtkDialogController()
            return None

    show_blocking_alert_dialog = (lambda self, caption, message, buttons, checkbox_text, default_button_id, callback = None, icon = None, allows_closing = on_ui_thread_blocking(), steal_focus = (None, 0, None, IconType.WARN, False, False, None), help_link = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'checkbox_text', 'Optional[Text]', 'default_button_id', 'int', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'icon', 'IconType', 'allows_closing', 'bool', 'steal_focus', 'bool', 'help_link', 'Optional[Text]', 'return', 'Future[Optional[int]]'): if IS_MAC:
show_warning_icon = icon in (IconType.ERROR, IconType.WARN)button_id = self._macos_blocking_alert_dialog(caption = caption, message = message, buttons = buttons, default = default_button_id, image_name = None, show_on_top = True, help_link = help_link, show_warning_icon = show_warning_icon, detailed_text = None)ResolvedFuture(button_id)if None:
self._tdc.show_blocking_alert_dialog(caption = caption, message = message, buttons = buttons, default_button_id = default_button_id, checkbox_text = checkbox_text, callback = callback, icon = icon, allows_closing = allows_closing, steal_focus = steal_focus)None._gtk.show_blocking_alert_dialog(caption = caption, message = message, buttons = buttons))()
    show_non_blocking_alert_dialog = (lambda self, caption, message, buttons, left_buttons, checkbox_text, default_button_id, callback = None, icon = None, keep_open = on_ui_thread(), allows_closing = (None, None, 0, None, IconType.WARN, False, False, False), steal_focus = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'left_buttons', 'Optional[List[Text]]', 'checkbox_text', 'Optional[Text]', 'default_button_id', 'int', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'icon', 'IconType', 'keep_open', 'bool', 'allows_closing', 'bool', 'steal_focus', 'bool', 'return', 'Closeable'): if IS_MAC:
show_warning_icon = icon in (IconType.ERROR, IconType.WARN)self._macos_nonblocking_alert_dialog(caption = caption, message = message, buttons = buttons, detailed_text = None, default = default_button_id, checkbox_text = checkbox_text, callback = callback, keep_open = keep_open, left_buttons = left_buttons, no_warning = not show_warning_icon)if None:
self._tdc.show_non_blocking_alert_dialog(caption = caption, message = message, buttons = buttons, default_button_id = default_button_id, checkbox_text = checkbox_text, callback = callback, keep_open = keep_open, left_buttons = left_buttons, icon = icon, allows_closing = allows_closing, steal_focus = steal_focus)None._gtk.show_non_blocking_alert_dialog(caption = caption, message = message, buttons = buttons, left_buttons = left_buttons, callback = callback))()


class BaseDialogController:
    
    def __init__(self = None, app = None):
        self._app = app
        self._apex_context = app._apex_context
        self._native_dialog_controller = NativeDialogController()

    
    def electron_dialogs_enabled(self = None):
        return is_electron_application()

    native_dialog_controller = (lambda self = None: self._native_dialog_controller)()
    
    def get_electron_dialog_controller(self = None):
        raise NotImplementedError()

    
    def report_dialog_metrics(self = None, event = None, framework = None, source = ('event', 'DialogEventTypes', 'framework', 'DialogFrameworkTypes', 'source', 'DialogSourceTypes', 'return', 'None')):
        if self._apex_context.metrics_reporter:
            dialog_counter = self._apex_context.metrics_reporter.create_counter(Metric('desktop_ui_framework', f'''dialogs/{framework.value}'''), {
                'event': event.value,
                'source': source.value })
            dialog_counter.increment()
            dialog_counter.record()
        if IS_LINUX:
            report_ui_framework_event_restricted('show_alert_dialog_reported', FrameworkProps.LINUX, event = event.value, source = source.value)
            return None



class DummyDialogController(BaseDialogController):
    pass
# WARNING: Decompyle incomplete


class DialogController(BaseDialogController):
    pass
# WARNING: Decompyle incomplete

