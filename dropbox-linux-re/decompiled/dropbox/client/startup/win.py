# Source Generated with Decompyle++
# File: win.pyc (Python 3.11)

import ctypes
import os.path as os
import pprint
import re
import sys
import time
from typing import Any, Optional
import pynt
import pywintypes
import win32api
import win32con
import win32event
import win32evtlog
import win32profile
import winerror
from pynt.constants import HKEY_CURRENT_USER
from pynt.dlls import advapi32, kernel32, shell32
from pynt.helpers.registry import create_registry_key, read_registry_value, registry_key
from six import iteritems
from win32com.shell import shellcon
from build_number import BUILD_KEY, is_full_msix
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.constants import AppDataPaths
from dropbox.client.util import hard_exit
from dropbox.client.util.win import get_dropbox_update_versioned_path, get_update_manager_client_state_value, get_user_sid_string, kill_process_by_name
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import check_perms
from dropbox.foundation.reporting import report_app_framework_event, report_app_framework_event_restricted
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.infinite import infinite_pager_enabled
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.util import report_infinite_event
from dropbox.install_type import get_dropbox_install_type, InstallType
from dropbox.network.win import generate_adapter_info
from dropbox.trace import TRACE
from dropbox.win32.internal import add_shortcut_to_user_location, check_nsis_tracing, get_volumes, is_admin, is_kb2533623_installed, is_uac_enabled, remove_shortcut_from_user_location, reset_nsis_tracing, tcp_parameters, win_strerror
from dropbox.win32.kernel32 import GetLastError
from dropbox.win32.psapi import GetProcessMemoryInfo, PROCESS_MEMORY_COUNTERS
from dropbox.win32.version import WIN7, WINDOWS_VERSION
from dropbox.win32_util import path_is_remote
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
BUGCHECK_EVENT_ID = 1001

def install_early_in_boot(client_session_id = None):
    pass


def notify_windows_system_crash(local_config, gandalf):
    send_kernel_panics = send_kernel_panics
    import dropbox.client.high_trace
    send_kernel_panics()
    
    try:
        if local_config:
            last_timestamp = local_config.config_dict.get('last_windows_crash_log_sent', 0)
            if last_timestamp != 0:
                crash_info = get_windows_last_crash_info(last_timestamp)
                if crash_info:
                    report_infinite_event(InfiniteEventType.INFINITE_WIN_BUGCHECK_EVENT, bugcheck_info = crash_info, driver_enabled = infinite_pager_enabled(gandalf))
                    TRACE('!! Windows Kernel Crash, %r', (crash_info,))
            local_config.config_dict['last_windows_crash_log_sent'] = int(time.time())
            return None
        return None
    except Exception:
        report_exception(component = DesktopComponent.INITIALIZATION)
        return None



def get_rss():
    
    try:
        c = PROCESS_MEMORY_COUNTERS()
        if not GetProcessMemoryInfo(win32api.GetCurrentProcess(), ctypes.byref(c), ctypes.sizeof(c)):
            win_errno = GetLastError()
            raise WindowsError(win_errno, win_strerror(win_errno))
        return c.WorkingSetSize
    except Exception:
        report_exception(component = DesktopComponent.INITIALIZATION)

    return -1


def restart_explorer():
    TRACE('Killing Windows Explorer.')
    kill_process_by_name('explorer.exe')

_mutex: 'Optional[Any]' = None

def limit_to_one_instance(app, appdata_path):
