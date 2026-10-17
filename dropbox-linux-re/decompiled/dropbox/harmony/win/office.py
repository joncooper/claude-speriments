# Source Generated with Decompyle++
# File: office.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import ctypes
import os
import threading
import time
from dropbox.foundation.futures.basic import IncompleteFutureException
from dropbox.foundation.futures.thread import ThreadPoolExecutor
import psutil
from typing import Any, Callable, List, Optional, Set, Text, Tuple, TypeVar
import comtypes.client as comtypes
import pywintypes
import win32api
import win32con
import win32gui
import win32process
from comtypes import COMError
from comtypes.automation import IDispatch
from pynt.dlls.oleacc import oleacc
from pynt.headers.WinError import ERROR_INVALID_PARAMETER, ERROR_INVALID_WINDOW_HANDLE
from winffi.kernel32.api import get_process_name
from dropbox.client.util.win import get_long_path, kill_process_by_handle, launch_app
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import report
from dropbox.event_names import HARMONY_EVENT
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future, Future
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.functions import convert_to_twos_complement
from dropbox.gui import spawn_thread_with_name
from dropbox.harmony.models.types import ApplicationDetails, ApplicationVersion, WinApplicationVersion, WindowID
from dropbox.harmony.plugins.base import BasicCoordinatingPlugin, EditorStatusTracker, FileMapPlugin, PluginArgs
from dropbox.harmony.utility.exceptions import SEVERITY_BENIGN, SEVERITY_CRITICAL, StateNotAvailableError
from dropbox.harmony.win.com import COMWrapper, handle_rpc_errors, RPCError
from dropbox.harmony.win.com_thread import PluginCOMThread
from dropbox.harmony.win.plugin import WinPlugin
from dropbox.harmony.win.shell import MS_DLG_CLASS, NUIDialog
from dropbox.trace import TRACE
from dropbox.win32.version import OFFICE2007, OFFICE2010, OFFICE2013, OFFICE2016, OFFICE_VERSION_2502
OBJID_NATIVEOM = -16
_KNOWN_SAFE_TRACEABLE_PROCESSES = frozenset(('winword.exe', 'excel.exe', 'powerpnt.exe', 'explorer.exe', 'ctfmon.exe', 'textinputhost.exe'))
_PROCESS_NAME_EXECUTOR_LOCK = threading.Lock()
_PROCESS_NAME_EXECUTOR: 'Optional[ThreadPoolExecutor]' = None
_PROCESS_NAME_TIMEOUT_SECONDS: 'float' = 2
_PROCESS_NAME_DISABLED = False

def _get_process_name_executor():
    _PROCESS_NAME_EXECUTOR_LOCK
# WARNING: Decompyle incomplete


def _disable_process_name_lookup():
    global _PROCESS_NAME_DISABLED
    old = None
    _PROCESS_NAME_EXECUTOR_LOCK
    _PROCESS_NAME_DISABLED = True
# WARNING: Decompyle incomplete


def _get_process_name_impl(hwnd = None):
    if hwnd == 0:
        return 'unknown application (invalid hwnd)'
    (_, pid) = win32process.GetWindowThreadProcessId(hwnd)
    if pid <= 0:
        return 'unknown application (invalid pid)'
    process = psutil.Process(pid)
    exe_name = process.name().lower()
    if exe_name in _KNOWN_SAFE_TRACEABLE_PROCESSES:
        return exe_name


def _get_safe_process_name_for_trace(hwnd = None):
    pass
# WARNING: Decompyle incomplete


def _find_active_window_target(hwnd = None, target = None, attempt = None, should_raise = (False,)):
    pass
# WARNING: Decompyle incomplete


def _walk(hwnd = None, path = None, should_raise = None):
    TRACE('Searching for active window via window hierarchy walk')
    for index, class_name in enumerate(path):
        if not hwnd:
            return None
        hwnd = win32gui.FindWindowEx(hwnd, 0, class_name, None)
    except pywintypes.error:
        e = None
        if e.args[0] != ERROR_INVALID_WINDOW_HANDLE:
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.HARMONY)
        if should_raise:
            raise RPCError(message = 'Could not get window', error = e, code = e.args[0])
        e = None
        del e
        return None
        e = None
        del e
    if hwnd:
        preview_window = win32gui.FindWindowEx(hwnd, 0, 'OPH Previewer Parent Window', None)
        if preview_window:
            TRACE('!! Application in protected mode %r %r', hex(hwnd), hex(preview_window))
            if should_raise:
                raise RPCError(message = 'Application in protected mode')
            return None
        except pywintypes.error:
            e = None
            if e.args[0] != ERROR_INVALID_WINDOW_HANDLE:
                report_exception(severity = Severity.CRITICAL, component = DesktopComponent.HARMONY)
            if should_raise:
                raise RPCError(message = 'Error finding previewer window', error = e, code = e.args[0])
            e = None
            del e
            return None
            e = None
            del e
    TRACE('!! Unable to get hwnd for class: %s', class_name)
    if index != len(path) - 1:
        if should_raise:
            raise StateNotAvailableError('Application window not ready', stage = 'window-not-ready')
        return None
    return hwnd

_F = TypeVar('_F', bound = Callable)

def handle_office_rpc_errors(should_raise = None, return_value = None):
    
    def invalid_pointer_handler(exception = None, plugin = None, *args, **kwargs):
        TRACE('!! COM object for active document is no longer valid')
        plugin._cleanup_remote()

    return handle_rpc_errors(should_raise = should_raise, return_value = return_value, invalid_pointer_handler = invalid_pointer_handler)


class _CleanupMonitor:
    pass
# WARNING: Decompyle incomplete


def monitor_and_cleanup(cleanup_monitor = None):
    
    try:
        cleanup_monitor.monitor()
        return None
    except Exception:
        TRACE('!! Error cleaning up the plugin')
        report_exception(severity = Severity.WARN, component = DesktopComponent.HARMONY)
        return None



def office_version_2502_or_greater(version = None):
    
    try:
        office_2502_build_nums = map(int, OFFICE_VERSION_2502.split('.'))
        version_build_nums = map(int, version.split('.'))
        for office_2502_build_num, version_build_num in zip(office_2502_build_nums, version_build_nums):
            if version_build_num > office_2502_build_num:
                return True
            if None < office_2502_build_num:
                return False
            return True
            TRACE('!! Error trying to compare Microsoft Office version to 2502!')
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.HARMONY)
            return False



def microsoft_office_version_16_or_greater(version = None):
    if not isinstance(version, WinApplicationVersion):
        return False
    return None <= version


class OfficePlugin(FileMapPlugin, EditorStatusTracker, BasicCoordinatingPlugin, WinPlugin):
    pass
# WARNING: Decompyle incomplete


class WordPlugin(OfficePlugin):
    APPLICATION_IDENTIFIER = 'Word.Application'
    STORMCROW_RULE = 'desktop-harmony-enable-word'
    _WORD_CLASS_TREE = [
        '_WwF',
        '_WwB',
        '_WwG']
    _WORD_CLASS_TREE_VERSION_2502 = [
        '_WwB',
        '_WwG']
    _WORD_WINDOW_CLASS_TARGET = '_WwG'
    supports_version = (lambda version = None: if not isinstance(version, WinApplicationVersion):
FalseNone <= version)()
    
    def _get_class_tree(self = None):
        if office_version_2502_or_greater(self._long_version):
            return self._WORD_CLASS_TREE_VERSION_2502
        return None._WORD_CLASS_TREE

    
    def _get_target_window_class(self = None):
        return self._WORD_WINDOW_CLASS_TARGET

    
    def _get_object_collection(self = None):
        return self._remote.Application.Documents if self._remote else None

    
    def _get_active_object(self = None):
        return self._remote.Document if self._remote else None

    
    def _close_without_save(self = None, document = None):
        document.Close(0)



class PowerPointPlugin(OfficePlugin):
    pass
# WARNING: Decompyle incomplete


class ExcelPlugin(OfficePlugin):
    pass
# WARNING: Decompyle incomplete

