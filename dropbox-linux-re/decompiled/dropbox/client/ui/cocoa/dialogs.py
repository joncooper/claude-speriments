# Source Generated with Decompyle++
# File: dialogs.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Any, Callable, List, Optional, Set, Text, Tuple
from AppKit import NSAlert, NSAlertFirstButtonReturn, NSApp, NSCriticalAlertStyle, NSImage, NSObject, NSURL, NSWarningAlertStyle, NSWindow, NSWorkspace
from objc import YES
from build_number import BUILD_KEY
from dropbox.client.ui.cocoa.alert_dialog.alert_dialog import CocoaAlertDialog
from dropbox.client.ui.cocoa.constants import ESCAPE_KEY
from dropbox.client.ui.common.dialog_constants import ALERT_DIALOG_FAILED_TO_DISPLAY
from dropbox.client.ui.common.icon_overlay import IconOverlayStrings
from dropbox.client.ui.common.uikit import Closeable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import assert_message_queue
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
_MOVE_TO_DROPBOX_WARNING: 'Optional[CocoaAlertDialog]' = None
_MODERN_ALERT_DIALOGS: 'Set[CocoaAlertDialog]' = set()

class EFAlert(NSAlert):
    alertWithHelpLink_ = (lambda cls, help_link: alert = EFAlert.alloc().init()# WARNING: Decompyle incomplete
)()
    
    def alertShowHelp_(self, alert):
        help_link = alert.helpAnchor()
    # WARNING: Decompyle incomplete


show_alert_dialog = (lambda caption, message, buttons, default, image_name = None, show_on_top = None, help_link = assert_message_queue, show_warning_icon = (0, None, False, None, False, None), detailed_text = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'default', 'Optional[int]', 'image_name', 'Optional[str]', 'show_on_top', 'Optional[bool]', 'help_link', 'Optional[Text]', 'show_warning_icon', 'Optional[bool]', 'detailed_text', 'Optional[Text]', 'return', 'Optional[int]'): try:
icon = NSImage.imageNamed_(image_name) if image_name else Nonealert = _create_alert(caption = caption, message = message, buttons = buttons, icon = icon, default = default, help_link = help_link, show_warning_icon = show_warning_icon)if show_on_top:
try:
NSApp().activateIgnoringOtherApps_(True)try:
passexcept Exception:
e = NoneTRACE('[dialogs] Failed to activate app: %s', e)try:
e = Nonedel ee = Nonedel etry:
alert_ret = alert.runModal()alert_ret - NSAlertFirstButtonReturnexcept Exception:
e = NoneTRACE('Failed to show Cocoa dialog: %s', e)report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UI_KIT)del eNoneNone = del e)()
modern_alert_dialog = (lambda caption, message, buttons, detailed_text, default, checkbox_text, callback = None, keep_open = None, left_buttons = assert_message_queue, force_min_width = (None, 0, None, None, False, None, False, False), no_warning = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'detailed_text', 'Optional[Text]', 'default', 'int', 'checkbox_text', 'Optional[Text]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'keep_open', 'bool', 'left_buttons', 'Optional[List[Text]]', 'force_min_width', 'bool', 'no_warning', 'bool', 'return', 'Closeable'): pass# WARNING: Decompyle incomplete
)()
show_indeterminate_progress_alert = (lambda caption = None, message = None, no_warning = assert_message_queue: pass# WARNING: Decompyle incomplete
)()
show_office_addin_prompt = (lambda caption, message, buttons, accept_cb, decline_cb = None, close_cb = None, default = assert_message_queue, image_name = (0, None, True), show_on_top = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'accept_cb', 'Callable[[], Any]', 'decline_cb', 'Callable[[], Any]', 'close_cb', 'Callable[[], Any]', 'default', 'int', 'image_name', 'Optional[str]', 'show_on_top', 'bool', 'return', 'None'): button_clicked = show_alert_dialog(caption, message, buttons, default = default, image_name = image_name, show_on_top = show_on_top)# WARNING: Decompyle incomplete
)()
_current_accessibility_alert: 'Optional[EFAlert]' = None

def show_move_to_dropbox_warning():
    global _MOVE_TO_DROPBOX_WARNING
    
    def _learn_more_callback(button_clicked = None, _ = None, dialog = None):
        global _MOVE_TO_DROPBOX_WARNING
        if button_clicked == 1:
            dropbox_url_info.launch_full_url('https://www.dropbox.com/help/9269')
            return None
        None.close()
        _MOVE_TO_DROPBOX_WARNING = None

    if _MOVE_TO_DROPBOX_WARNING and _MOVE_TO_DROPBOX_WARNING.isShowing():
        _MOVE_TO_DROPBOX_WARNING.activate()
        return None
    _MOVE_TO_DROPBOX_WARNING = CocoaAlertDialog(caption = IconOverlayStrings.icloud_heading, message = IconOverlayStrings.icloud_message, left_button_list = [], right_button_list = [
        (IconOverlayStrings.learn_more_button, None),
        (IconOverlayStrings.ok_button, ESCAPE_KEY)], checkbox_text = None, callback = _learn_more_callback)


def show_alert_sheet(caption, message, buttons, window, delegate = None, selector = None, icon = None, width = (None, None, 0), context_info = ('caption', 'Optional[Text]', 'message', 'Optional[Text]', 'buttons', 'Optional[List[Text]]', 'window', 'NSWindow', 'delegate', 'str', 'selector', 'NSObject', 'icon', 'Optional[NSImage]', 'width', 'Optional[int]', 'context_info', 'int', 'return', 'EFAlert')):
    alert = _create_alert(caption = caption, message = message, buttons = buttons, icon = icon)
    alert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_(window, delegate, selector, context_info)
    return alert


def _create_alert(caption, message, buttons, icon, width, default, help_link, show_warning_icon, check_box = (None, None, None, None, None, 0, None, False, None)):
    alert = EFAlert.alertWithHelpLink_(help_link)
    style = NSCriticalAlertStyle if show_warning_icon else NSWarningAlertStyle
    alert.setAlertStyle_(style)
    if caption:
        alert.setMessageText_(caption)
    if message:
        alert.setInformativeText_(message)
    alert.window().setTitle_(BUILD_KEY)
# WARNING: Decompyle incomplete

