# Source Generated with Decompyle++
# File: log_break_dialog.pyc (Python 3.11)

import ctypes
from ctypes import wintypes
from typing import Callable, Text
import pywintypes
import win32api
import win32con
import win32gui
from build_number import BUILD_KEY
from dropbox.foundation.html_views.common.threading import assert_on_ui_thread
from dropbox.trace import TRACE
_FIELD_ID = 1001
_BUTTON_ID = 1002
_FIELD_X = 10
_FIELD_Y = 12
_FIELD_WIDTH = 240
_CONTROL_HEIGHT = 24
_PADDING = 8
_BUTTON_WIDTH = 80
_CLIENT_WIDTH = _FIELD_X + _FIELD_WIDTH + _PADDING + _BUTTON_WIDTH + _FIELD_X
_CLIENT_HEIGHT = _FIELD_Y * 2 + _CONTROL_HEIGHT

class LogBreakDialog(object):
    
    def __init__(self = None, on_insert = None):
        self._on_insert = on_insert
        self._counter = 0
        self._hwnd = 0
        self._field_hwnd = 0
        self._font = 0
        self._class_name = '%sLogBreak%d' % (BUILD_KEY, id(self))

    _dpi_scale = (lambda : try:
monitor = win32api.MonitorFromPoint(win32gui.GetCursorPos(), win32con.MONITOR_DEFAULTTONEAREST)dpi_x = ctypes.c_uint()dpi_y = ctypes.c_uint()hr = ctypes.windll.shcore.GetDpiForMonitor(monitor, 0, ctypes.byref(dpi_x), ctypes.byref(dpi_y))if hr == 0 and dpi_x.value:
dpi_x.value / 96except Exception:
TRACE('[log break] per-monitor DPI unavailable; falling back')hdc = win32gui.GetDC(0)try:
get_device_caps = ctypes.windll.gdi32.GetDeviceCapsget_device_caps.argtypes = [
wintypes.HDC,
ctypes.c_int]get_device_caps.restype = ctypes.c_intdpi = get_device_caps(hdc, win32con.LOGPIXELSX)win32gui.ReleaseDC(0, hdc)except:
win32gui.ReleaseDC(0, hdc)dpi / 96 if dpi else 1)()
    show = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _centered_position = (lambda win_w = None, win_h = None: monitor = win32api.MonitorFromPoint(win32gui.GetCursorPos(), win32con.MONITOR_DEFAULTTONEAREST)(left, top, right, bottom) = win32api.GetMonitorInfo(monitor)['Work']x = left + (right - left - win_w) // 2y = top + (bottom - top - win_h) // 2(x, y))()
    
    def _force_foreground(self = None):
        
        try:
            win32gui.SetForegroundWindow(self._hwnd)
            win32gui.SetActiveWindow(self._hwnd)
            win32gui.SetFocus(self._field_hwnd)
            return None
        except Exception:
            TRACE('[log break] failed to foreground window')
            return None


    
    def _reset_field(self = None):
        win32gui.SetWindowText(self._field_hwnd, 'break_%d' % self._counter)
        win32gui.SendMessage(self._field_hwnd, win32con.EM_SETSEL, 0, -1)

    
    def _on_command(self, hwnd = None, msg = None, wparam = None, lparam = ('hwnd', 'int', 'msg', 'int', 'wparam', 'int', 'lparam', 'int', 'return', 'int')):
        control_id = win32gui.LOWORD(wparam)
        if control_id == _BUTTON_ID:
            label = win32gui.GetWindowText(self._field_hwnd)
            if not label:
                label = 'break_%d' % self._counter
            self._on_insert(label)
            self._reset_field()
        return 0

    
    def _on_close(self, hwnd = None, msg = None, wparam = None, lparam = ('hwnd', 'int', 'msg', 'int', 'wparam', 'int', 'lparam', 'int', 'return', 'int')):
        win32gui.DestroyWindow(hwnd)
        return 0

    
    def _on_destroy(self, hwnd = None, msg = None, wparam = None, lparam = ('hwnd', 'int', 'msg', 'int', 'wparam', 'int', 'lparam', 'int', 'return', 'int')):
        
        try:
            win32gui.UnregisterClass(self._class_name, win32gui.GetModuleHandle(None))
        except pywintypes.error:
            TRACE('[log break] failed to unregister window class')

        if self._font:
            win32gui.DeleteObject(self._font)
            self._font = 0
        return 0


