# Source Generated with Decompyle++
# File: shell.pyc (Python 3.11)

from __future__ import absolute_import
import os
from typing import Any, Optional
import pywintypes
import win32api
import win32con
import win32gui
import win32process
from pynt.constants import WM_DWMCOMPOSITIONCHANGED
from pynt.dlls.user32 import user32
from pynt.headers.WinError import ERROR_ACCESS_DENIED, ERROR_GEN_FAILURE, ERROR_INVALID_PARAMETER, ERROR_INVALID_WINDOW_HANDLE
from pynt.helpers.general import FormattedWindowsError
from pynt.types import WINEVENTPROC
from winffi.kernel32.api import get_process_name
from build_number import BUILD_KEY
from dropbox.callbacks import Handler
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions_ex_5
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import lrudict
from dropbox.gui import event_handler
from dropbox.harmony.model import HarmonyWindow
from dropbox.harmony.models.types import ApplicationDetails, ApplicationID, WindowDetails, WindowFile, WindowID
from dropbox.harmony.plugins.office_coauthoring import application_supports_coauthoring
from dropbox.harmony.utility.exceptions import SEVERITY_BENIGN, StateNotAvailableError
from dropbox.harmony.utility.threading import HarmonyThread
from dropbox.harmony.utility.threading_decorators import assert_on_harmony_thread, on_harmony_thread
from dropbox.harmony.win.office_coauthoring import office_license_supports_coauthoring
from dropbox.harmony.window_tracking.shell_interface import HarmonyShellInterface
from dropbox.trace import TRACE
from dropbox.win32.version import get_app_major_version, get_app_version
SHELL_TRAY_CLASS = 'Shell_TrayWnd'
MS_SPLASH_CLASS = 'MsoSplash'
MS_TOOLTIPS_CLASS = 'tooltips_class32'
MS_DLG_CLASS = '#32770'
NUIDialog = 'NUIDialog'
WM_D_PING = win32con.WM_USER + 16

class WindowsShellTracker(HarmonyShellInterface):
    _WINDOW_CAPACITY = 50
    _APPLICATION_CAPACITY = 50
    _WND_CLASS = BUILD_KEY + 'ShellHook'
    _GLOBAL_EVENTS = [
        (user32.EVENT_SYSTEM_FOREGROUND, None),
        (user32.EVENT_SYSTEM_MINIMIZESTART, user32.EVENT_SYSTEM_MINIMIZEEND)]
    _PROCESS_EVENTS = [
        (user32.EVENT_SYSTEM_MOVESIZESTART, user32.EVENT_SYSTEM_MOVESIZEEND),
        (user32.EVENT_SYSTEM_CAPTUREEND, None)]
    class_atom: 'Optional[int]' = None
    
    def __init__(self):
        self._tracked = None
        self._tracked_title = None
        self._tracked_maximized = False
        self._pid = os.getpid()
        self._app_versions = { }
        self._ignored_windows = set()
        self._hooks = { }
        self._win_callback = None
        self._hwnd_foreground = None
        self._hwnd_hook = None
        self._watched = lrudict(cache_size = self._WINDOW_CAPACITY)
        self._processes = lrudict(cache_size = self._APPLICATION_CAPACITY)
        self._window_focused_handler = Handler(handle_exc = report_exception)
        self.add_window_focused_callback = self._window_focused_handler.add_handler
        self.remove_window_focused_callback = self._window_focused_handler.remove_handler
        self._window_moved_handler = Handler(handle_exc = report_exception)
        self.add_window_moved_callback = self._window_moved_handler.add_handler
        self.remove_window_moved_callback = self._window_moved_handler.remove_handler
        self._windows_hidden_handler = Handler(handle_exc = report_exception)
        self.add_windows_hidden_callback = self._windows_hidden_handler.add_handler
        self.remove_windows_hidden_callback = self._windows_hidden_handler.remove_handler
        self._windows_destroyed_handler = Handler(handle_exc = report_exception)
        self.add_windows_destroyed_callback = self._windows_destroyed_handler.add_handler
        self.remove_windows_destroyed_callback = self._windows_destroyed_handler.remove_handler
        self._window_ping_handler = Handler(handle_exc = report_exception)
        self.add_window_ping_callback = self._window_ping_handler.add_handler
        self.remove_window_ping_callback = self._window_ping_handler.remove_handler
        self._transparency_support_changed_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_transparency_support_changed_callback = self._transparency_support_changed_callbacks.add_handler
        self.remove_transparency_support_changed_callback = self._transparency_support_changed_callbacks.remove_handler

    set_ignored_window = (lambda self = None, hwnd = None: self._ignored_windows.add(hwnd))()
    enable = (lambda self = None: if not self._win_callback:
decorated_cb = event_handler(self._on_win_event_callback, HarmonyThread.HARMONY_THREAD_NAME)self._win_callback = WINEVENTPROC(decorated_cb)self._setup_winevent_hook(self._GLOBAL_EVENTS, 0)self._setup_hook_window())()
    
    def _setup_winevent_hook(self, events, pid):
