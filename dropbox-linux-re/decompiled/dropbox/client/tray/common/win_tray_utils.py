# Source Generated with Decompyle++
# File: win_tray_utils.pyc (Python 3.11)

from __future__ import absolute_import, division
import ctypes
import sys
from typing import Optional
import win32gui
from build_number import BUILD_KEY
from comtypes.GUID import GUID
from pynt.constants import NIF_GUID
from pynt.dlls.shell32 import shell32
from pynt.helpers.general import win_error_check
from pynt.types import NOTIFYICONDATA
from dropbox.win32.GUID import generate_name_based_guid

class Win32TrayIconHelper:
    CLASS_NAME = BUILD_KEY + 'TrayIcon'
    BUBBLE_TIMEOUT = 10000
    _notify_icon_guid: 'Optional[GUID]' = None
    _notify_icon_data_size: 'Optional[int]' = None
    get_tray_icon_guid = (lambda cls = None: is_official = bool(getattr(sys, 'dropbox_windows_official', False))if not is_official:
None# WARNING: Decompyle incomplete
)()
    make_empty_notify_icon_data = (lambda cls = None, guid = None: pass# WARNING: Decompyle incomplete
)()
    clear_guid_icon = (lambda cls = None, guid = None: data = cls.make_empty_notify_icon_data(guid)ret = shell32.Shell_NotifyIconW(win32gui.NIM_DELETE, ctypes.byref(data))if not ret:
win_error_check()None)()

