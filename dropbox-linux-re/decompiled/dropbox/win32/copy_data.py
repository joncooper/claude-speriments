# Source Generated with Decompyle++
# File: copy_data.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import ctypes
from typing import Any, Callable, Optional, Text, Tuple
import win32con
import win32gui
import winerror
from build_number import BUILD_KEY
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions_ex_4
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.trace import TRACE
CopyDataId = Tuple[(int, int, int)]

class COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ('dwData', ctypes.c_void_p),
        ('cbData', ctypes.wintypes.DWORD),
        ('lpData', ctypes.c_wchar_p)]


def find_copy_data_window(name = None):
    hwnd = win32gui.FindWindow(BUILD_KEY + name, None)
    if not hwnd:
        TRACE('Failed to find COPYDATA window %s', BUILD_KEY + name)
        return False


def send_copy_data_message(name = None, message = None):
    hwnd = win32gui.FindWindow(BUILD_KEY + name, None)
    if not hwnd:
        TRACE('Failed to create COPYDATA window %s', BUILD_KEY + name)
        return False
    TRACE('Sending COPYDATA message %s', message)
    cds = COPYDATASTRUCT()
    cds.dwData = 0
    cds.cbData = ctypes.sizeof(ctypes.create_unicode_buffer(message))
    cds.lpData = ctypes.c_wchar_p(message)
    ctypes.windll.user32.SendMessageW(hwnd, win32con.WM_COPYDATA, 0, ctypes.byref(cds))
    return True

create_copy_data_window = (lambda name = None, callback = None: pass# WARNING: Decompyle incomplete
)()
create_unique_copy_data_window = (lambda name = None, callback = None: class_name = BUILD_KEY + nametry:
if win32gui.FindWindow(class_name, None):
TRACE('!! Window of class %r already exists', class_name)Noneexcept win32gui.error:
e = Noneif e.winerror != winerror.ERROR_FILE_NOT_FOUND:
raise e = Nonedel eexcept:
e = Nonedel ecreate_copy_data_window(name, callback))()
destroy_copy_data_window = (lambda copy_data_id = None: (hwnd, class_atom, hinst) = copy_data_idwin32gui.DestroyWindow(hwnd)win32gui.UnregisterClass(class_atom, hinst))()
