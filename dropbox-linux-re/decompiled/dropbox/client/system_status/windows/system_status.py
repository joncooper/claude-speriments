# Source Generated with Decompyle++
# File: system_status.pyc (Python 3.11)

from __future__ import absolute_import
import time
from typing import Any, Callable, Optional
import win32con
import win32gui
from build_number import BUILD_KEY
from dropbox.callbacks import Handler
from dropbox.client.system_status.system_status_monitor_interface import SystemStatusMonitorTestingInterface
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions_ex_5
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime import AutorestartRequestManager
from dropbox.trace import TRACE

class WindowsSystemStatusMonitor(SystemStatusMonitorTestingInterface):
    _WND_CLASS = BUILD_KEY + 'SystemStatusMonitorShellHook'
    
    def __init__(self = None):
        self._suspend_handler = Handler(handle_exc = report_exception)
        self._resume_handler = Handler(handle_exc = report_exception)
        self._shutdown_handler = Handler(handle_exc = report_exception)
        self._shutdown_requested = False
        self._sleep_start_time = None
        self._sleep_end_time = None
        self._hwnd_hook = None
        self._setup_hook_window()

    
    def add_suspend_callback(self = None, callback = None):
        self._suspend_handler.add_handler(callback)

    
    def remove_suspend_callback(self = None, callback = None):
        self._suspend_handler.remove_handler(callback)

    
    def trigger_suspend_callbacks(self = None):
        self._suspend_handler.run_handlers()

    
    def add_resume_callback(self = None, callback = None):
        self._resume_handler.add_handler(callback)

    
    def remove_resume_callback(self = None, callback = None):
        self._resume_handler.remove_handler(callback)

    
    def trigger_resume_callbacks(self = None):
        self._resume_handler.run_handlers()

    
    def add_shutdown_callback(self = None, callback = None):
        self._shutdown_handler.add_handler(callback)

    
    def remove_shutdown_callback(self = None, callback = None):
        self._shutdown_handler.remove_handler(callback)

    
    def trigger_shutdown_callbacks(self = None):
        if self._shutdown_requested:
            return None
        TRACE('WindowsSystemStatusMonitor: Triggering shutdown callbacks')
        self._shutdown_requested = True
        self._shutdown_handler.run_handlers()

    sleep_start_time = (lambda self = None: self._sleep_start_time)()
    sleep_start_time = (lambda self = None, value = None: self._sleep_start_time = valueself._sleep_end_time = None)()
    sleep_end_time = (lambda self = None: self._sleep_end_time)()
    sleep_end_time = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()
    _setup_hook_window = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _on_power_broadcast = (lambda self, hwnd_hook = None, msg = on_ui_thread, wparam = handle_exceptions_ex_5(return_value = 0, component = DesktopComponent.UNKNOWN), lparam = ('return', 'int'): if wparam == win32con.PBT_APMSUSPEND:
TRACE('[WindowsSystemStatusMonitor] host entering sleep...')self.sleep_start_time = time.time()self._suspend_handler.run_handlers()elif wparam == win32con.PBT_APMRESUMEAUTOMATIC:
TRACE('[WindowsSystemStatusMonitor] ...host woke up.')self.sleep_end_time = time.time()self._resume_handler.run_handlers()win32con.TRUE)()
    _on_end_session = (lambda self, hwnd_hook = None, msg = None, wparam = handle_exceptions_ex_5(return_value = 0, component = DesktopComponent.UNKNOWN), lparam = ('return', 'int'): TRACE('[WindowsSystemStatusMonitor] Received WM_ENDSESSION with wparam=%r, lparam=%r', wparam, lparam)AutorestartRequestManager.instance().undo_mark_no_autorestart("Received WM_ENDSESSION -- It's unlikely we crashed")if bool(wparam):
self.trigger_shutdown_callbacks()win32con.TRUE)()
    _on_query_end_session = (lambda self, hwnd_hook = None, msg = None, wparam = handle_exceptions_ex_5(return_value = 0, component = DesktopComponent.UNKNOWN), lparam = ('return', 'int'): AutorestartRequestManager.instance().mark_no_autorestart('User initiated session end')win32con.TRUE)()

