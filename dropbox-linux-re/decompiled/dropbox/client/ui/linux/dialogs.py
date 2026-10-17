# Source Generated with Decompyle++
# File: dialogs.pyc (Python 3.11)

from typing import Callable, List, Optional
from dropbox.client.ui.common.uikit import Closeable, FrameworkProps, on_ui_thread_future, on_ui_thread_returns_none, report_ui_framework_event, report_ui_framework_event_restricted, should_create_headless_ui_kit
from dropbox.client.ui.linux.gtk_lib_app_indicator_loader import get_gtk_libappindicator_loader, GtkLibAppIndicatorLoader
from dropbox.client.util import safe_print
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.gui import assert_message_queue
from dropbox.trace import TRACE

class GtkDialogController:
    
    def __init__(self = None):
        self._gtk_lib = None
        self._initialize_gtk().ground(DesktopComponent.UI_KIT)

    _initialize_gtk = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def fallback_print_console(self = None, caption = None, message = None):
        safe_print(f'''\n[ALERT: {caption}]\n{message}\n''')
        report_ui_framework_event_restricted('show_alert_fallback', FrameworkProps.LINUX, message = message, detailed_text = str(message))

    show_blocking_alert_dialog = (lambda self = None, caption = None, message = assert_message_queue, buttons = ('caption', 'str', 'message', 'str', 'buttons', 'List[str]', 'return', 'Future[Optional[int]]'): pass# WARNING: Decompyle incomplete
)()
    _show_dialog_future = (lambda self = None, caption = None, message = on_ui_thread_returns_none(), buttons = (None,), callback = ('caption', 'str', 'message', 'str', 'buttons', 'List[str]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    show_non_blocking_alert_dialog = (lambda self, caption = None, message = None, buttons = assert_message_queue, left_buttons = (None, None), callback = ('caption', 'str', 'message', 'str', 'buttons', 'List[str]', 'left_buttons', 'Optional[List[str]]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'return', 'Closeable'): combined_buttons = buttonsif left_buttons:
combined_buttons.extend(left_buttons)self._show_dialog_future(caption = caption, message = message, buttons = combined_buttons, callback = callback)report_ui_framework_event_restricted('show_non_blocking_alert_dialog', FrameworkProps.LINUX, message = message)Closeable((lambda : pass))
)()

