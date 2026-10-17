# Source Generated with Decompyle++
# File: dialogs.pyc (Python 3.11)

import ctypes
import dataclasses
import uuid
from ctypes.wintypes import LPCWSTR
from enum import IntEnum
from typing import Callable, List, Optional, Text
import psutil
import win32con
import win32gui
import win32process
from build_number import BUILD_KEY
from winffi.progresstaskdialog import WinffiProgressTaskDialog
from winffi.taskdialog import IconType as TaskDialogIconType, WinffiTaskDialog
from dropbox.client.ui.common.dialog_constants import IconType as CommonIconType
from dropbox.client.ui.common.uikit import Closeable, on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures.basic import EasyFuture
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info

class TaskDialogNotifications(IntEnum):
    CREATED = 0
    NAVIGATED = 1
    BUTTON_CLICKED = 2
    HYPERLINK_CLICKED = 3
    TIMER = 4
    DESTROYED = 5
    RADIO_BUTTON_CLICKED = 6
    DIALOG_CONSTRUCTED = 7
    VERIFICATION_CLICKED = 8
    HELP = 9
    EXPANDO_BUTTON_CLICKED = 10


class TaskDialogElements(IntEnum):
    TDE_CONTENT = 0
    TDE_EXPANDED_INFORMATION = 1
    TDE_FOOTER = 2
    TDE_MAIN_INSTRUCTION = 3


class TaskDialogCommonButtonFlags(IntEnum):
    OK = 1
    YES = 2
    NO = 4
    CANCEL = 8
    RETRY = 16
    CLOSE = 32
    X_BUTTON = 2
    BUTTON_ID_OFFSET = 10


class TaskDialogMessageOffsets(IntEnum):
    TDM_NAVIGATE_PAGE = 101
    TDM_CLICK_BUTTON = 102
    TDM_SET_MARQUEE_PROGRESS_BAR = 103
    TDM_SET_PROGRESS_BAR_STATE = 104
    TDM_SET_PROGRESS_BAR_RANGE = 105
    TDM_SET_PROGRESS_BAR_POS = 106
    TDM_SET_PROGRESS_BAR_MARQUEE = 107
    TDM_SET_ELEMENT_TEXT = 108
    TDM_CLICK_RADIO_BUTTON = 110
    TDM_ENABLE_BUTTON = 111
    TDM_ENABLE_RADIO_BUTTON = 112
    TDM_CLICK_VERIFICATION = 113
    TDM_UPDATE_ELEMENT_TEXT = 114
    TDM_SET_BUTTON_ELEVATION_REQUIRED_STATE = 115
    TDM_UPDATE_ICON = 116


class CallbackResponse(IntEnum):
    CLOSE_DIALOG = 0
    KEEP_OPEN = 1


def get_unique_dialog_id():
    return str(uuid.uuid4())

DialogProperties = <NODE:12>()
DialogContents = <NODE:12>()
DialogStatus = <NODE:12>()

def replace_html_tags(text = dataclasses.dataclass):
    return text.replace('<br/>', '\n').replace('<br />', '\n').replace('<br>', '\n').replace('<b>', '"').replace('</b>', '"')


def convert_icon_type(common_icon_type = None):
    if common_icon_type == CommonIconType.ERROR:
        return TaskDialogIconType.ERROR_ICON
    if None == CommonIconType.WARN:
        return TaskDialogIconType.WARNING_ICON
    if None == CommonIconType.SHIELD:
        return TaskDialogIconType.SHIELD_ICON
    return None.INFO_ICON


class TaskDialog:
    
    def __init__(self, caption, message, buttons, future_to_resolve, default_button_id, checkbox_text, callback, keep_open, always_on_top = None, allows_closing = None, left_buttons = None, icon = (None, 0, None, None, False, True, False, None, CommonIconType.WARN, False), steal_focus = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'future_to_resolve', 'Optional[EasyFuture[Optional[int]]]', 'default_button_id', 'int', 'checkbox_text', 'Optional[Text]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'keep_open', 'bool', 'always_on_top', 'bool', 'allows_closing', 'bool', 'left_buttons', 'Optional[List[Text]]', 'icon', 'CommonIconType', 'steal_focus', 'bool', 'return', 'None')):
        self.properties = DialogProperties(always_on_top = always_on_top, allows_closing = allows_closing, keep_open = keep_open, has_checkbox = bool(checkbox_text), steal_focus = steal_focus, callback = callback, future_to_resolve = future_to_resolve)
        self.contents = DialogContents(caption = caption, message = message, buttons = buttons, default_button_id = default_button_id, checkbox_text = checkbox_text, left_buttons = left_buttons, icon = convert_icon_type(icon))
        self.status = DialogStatus()
        self.dialog_uuid = get_unique_dialog_id()
        self._td_thread = None

    run_callback_on_ui_thread = (lambda self = None, func = None, button_id = on_ui_thread_returns_none(), checkbox_id = ('func', 'Callable[[Optional[int], Optional[bool]], None]', 'button_id', 'Optional[int]', 'checkbox_id', 'Optional[bool]', 'return', 'None'): func(button_id, checkbox_id))()
    
    def winffi_callback_helper(self = None):
        if self.status.destroyed:
            TRACE('TaskDialog %s: Cleaned up', self.dialog_uuid)
            return None
        if not None.status.requested_callback or self.status.requested_destroyed:
            TRACE('TaskDialog %s: Running callbacks/futures', self.dialog_uuid)
            if self.properties.callback:
                self.run_callback_on_ui_thread(self.properties.callback, self.status.button_selected, self.status.checkbox_selected)
            if self.properties.future_to_resolve:
                self.properties.future_to_resolve.set_result(self.status.button_selected)
                return None
            return None
        return None

    
    def winffi_callback(self, hwnd = None, msg = None, wparam = None, lparam = ('hwnd', 'int', 'msg', 'int', 'wparam', 'int', 'lparam', 'int')):
        ret_value = CallbackResponse.CLOSE_DIALOG
        run_helper = False
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def show_taskdialog(self = None):
        pass
    # WARNING: Decompyle incomplete



class TaskDialogController:
    
    def show_blocking_alert_dialog(self, caption, message, buttons, default_button_id, checkbox_text, callback, keep_open, always_on_top = None, allows_closing = None, left_buttons = None, icon = (0, None, None, False, True, False, None, CommonIconType.WARN, False), steal_focus = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'default_button_id', 'int', 'checkbox_text', 'Optional[Text]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'keep_open', 'bool', 'always_on_top', 'bool', 'allows_closing', 'bool', 'left_buttons', 'Optional[List[Text]]', 'icon', 'CommonIconType', 'steal_focus', 'bool', 'return', 'EasyFuture[Optional[int]]')):
        id_future = EasyFuture('win32_dialog_future')
        dialog = TaskDialog(caption = caption, message = message, buttons = buttons, future_to_resolve = id_future, default_button_id = default_button_id, checkbox_text = checkbox_text, callback = callback, keep_open = keep_open, always_on_top = always_on_top, allows_closing = allows_closing, left_buttons = left_buttons, icon = icon, steal_focus = steal_focus)
        dialog.show_taskdialog()
        return id_future

    
    def show_non_blocking_alert_dialog(self, caption, message, buttons, default_button_id, checkbox_text, callback, keep_open, always_on_top = None, allows_closing = None, left_buttons = None, icon = (0, None, None, False, True, False, None, CommonIconType.WARN, False), steal_focus = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'default_button_id', 'int', 'checkbox_text', 'Optional[Text]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'keep_open', 'bool', 'always_on_top', 'bool', 'allows_closing', 'bool', 'left_buttons', 'Optional[List[Text]]', 'icon', 'CommonIconType', 'steal_focus', 'bool', 'return', 'Closeable')):
        dialog = TaskDialog(caption = caption, message = message, buttons = buttons, future_to_resolve = None, default_button_id = default_button_id, checkbox_text = checkbox_text, callback = callback, keep_open = keep_open, always_on_top = always_on_top, allows_closing = allows_closing, left_buttons = left_buttons, icon = icon, steal_focus = steal_focus)
        dialog.show_taskdialog()
        return Closeable(dialog.close)

    
    def show_taskdialog(self, caption, message, buttons, future_to_resolve, default_button_id, checkbox_text, callback, keep_open, always_on_top = None, allows_closing = None, left_buttons = None, icon = (None, 0, None, None, False, True, False, None, CommonIconType.WARN, False), steal_focus = ('caption', 'Text', 'message', 'Text', 'buttons', 'List[Text]', 'future_to_resolve', 'Optional[EasyFuture[Optional[int]]]', 'default_button_id', 'int', 'checkbox_text', 'Optional[Text]', 'callback', 'Optional[Callable[[Optional[int], Optional[bool]], None]]', 'keep_open', 'bool', 'always_on_top', 'bool', 'allows_closing', 'bool', 'left_buttons', 'Optional[List[Text]]', 'icon', 'CommonIconType', 'steal_focus', 'bool', 'return', 'None')):
        dialog = TaskDialog(caption = caption, message = message, buttons = buttons, future_to_resolve = future_to_resolve, default_button_id = default_button_id, checkbox_text = checkbox_text, callback = callback, keep_open = keep_open, always_on_top = always_on_top, allows_closing = allows_closing, left_buttons = left_buttons, icon = icon, steal_focus = steal_focus)
        dialog.show_taskdialog()



class ProgressTaskDialog:
    
    def __init__(self, caption, message = None, marquee = None, always_on_top = None, cancel_enabled = ('', True, True, False, None), cancel_callback = ('caption', 'Text', 'message', 'Text', 'marquee', 'bool', 'always_on_top', 'bool', 'cancel_enabled', 'bool', 'cancel_callback', 'Optional[Callable[[], None]]')):
        self.dialog_uuid = get_unique_dialog_id()
        self._config_caption = caption
        self._config_message = message
        self._config_marquee = marquee
        self._config_always_on_top = always_on_top
        self._config_cancel_enabled = cancel_enabled
        self._config_cancel_callback = cancel_callback
        self._td_thread = None
        self._status_hwnd = None
        self._status_requested_destroyed = False
        self._status_destroyed = False

    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def winffi_callback(self, hwnd = None, msg = None, wparam = None, lparam = ('hwnd', 'int', 'msg', 'int', 'wparam', 'int', 'lparam', 'int')):
        if msg == TaskDialogNotifications.DIALOG_CONSTRUCTED:
            TRACE('ProgressTaskDialog %s: Constructed', self.dialog_uuid)
            self._status_hwnd = hwnd
            win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_SMALL, win32con.NULL)
            win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_BIG, win32con.NULL)
            if self._config_always_on_top:
                win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
            hmenu = win32gui.GetSystemMenu(hwnd, False)
            win32gui.EnableMenuItem(hmenu, win32con.SC_CLOSE, win32con.MF_DISABLED)
            if not self._config_cancel_enabled:
                win32gui.SendMessage(self._status_hwnd, win32con.WM_USER + TaskDialogMessageOffsets.TDM_ENABLE_BUTTON, 2, 0)
            elif msg == TaskDialogNotifications.CREATED:
                TRACE('ProgressTaskDialog %s: Created', self.dialog_uuid)
                if self._config_marquee:
                    win32gui.SendMessage(self._status_hwnd, win32con.WM_USER + TaskDialogMessageOffsets.TDM_SET_PROGRESS_BAR_MARQUEE, True, 0)
                elif msg == TaskDialogNotifications.BUTTON_CLICKED:
                    TRACE('ProgressTaskDialog %s: Button %s clicked', self.dialog_uuid, wparam)
                    if not self._config_cancel_callback and self._status_requested_destroyed:
                        TRACE('ProgressTaskDialog %s: Running callback...', self.dialog_uuid)
                        self._config_cancel_callback()
                    elif msg == TaskDialogNotifications.DESTROYED:
                        TRACE('ProgressTaskDialog %s: Dialog destroyed', self.dialog_uuid)
                        self._status_destroyed = True
        return CallbackResponse.CLOSE_DIALOG

    
    def update_progress(self = None, value = None, range = None):
        if self._config_marquee or self._status_destroyed:
            return None
        new_value = None * 100 / range
        win32gui.SendMessage(self._status_hwnd, win32con.WM_USER + TaskDialogMessageOffsets.TDM_SET_PROGRESS_BAR_POS, new_value, 0)

    
    def update_message(self = None, new_text = None):
        if self._status_destroyed:
            return None
        win32gui.SendMessage(self._status_hwnd, win32con.WM_USER + TaskDialogMessageOffsets.TDM_SET_ELEMENT_TEXT, TaskDialogElements.TDE_CONTENT, new_text)

    
    def show(self = None):
        pass
    # WARNING: Decompyle incomplete


