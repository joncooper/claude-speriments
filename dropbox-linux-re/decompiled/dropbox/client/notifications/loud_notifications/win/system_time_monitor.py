# Source Generated with Decompyle++
# File: system_time_monitor.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Any, Callable, Optional
import win32con
import win32gui
from build_number import BUILD_KEY
from dropbox.callbacks import Handler
from dropbox.client.notifications.loud_notifications.interfaces import SystemTimeMonitor
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions_ex_5
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.trace import TRACE

class WindowsSystemTimeMonitor(SystemTimeMonitor):
    _WND_CLASS = BUILD_KEY + 'SystemTimeMonitorTrayHook'
    
    def __init__(self = None):
        self._time_change_handler = Handler(handle_exc = report_exception)
        self._hwnd_hook = None
        self._setup_hook_window()

    
    def add_time_changed_callback(self = None, callback = None):
        self._time_change_handler.add_handler(callback)

    
    def remove_time_changed_callback(self = None, callback = None):
        self._time_change_handler.remove_handler(callback)

    _setup_hook_window = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _on_time_change = (lambda self, hwnd_hook = None, msg = on_ui_thread, wparam = handle_exceptions_ex_5(return_value = 0, component = DesktopComponent.NATIVE_NOTIFICATIONS), lparam = ('return', 'int'): if msg == win32con.WM_TIMECHANGE:
TRACE('SystemTimeChangeMonitor reporting a time change event')self._time_change_handler.run_handlers()0)()

