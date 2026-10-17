# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import base64
import ctypes
import errno
import json
import os
import platform
import struct
import subprocess
import time
from ctypes.wintypes import DWORD, LPCWSTR, MAX_PATH, WCHAR
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Text, Tuple, TYPE_CHECKING, Union
if TYPE_CHECKING:
    from pywintypes import HANDLEType
import comtypes
import ntsecuritycon
import psutil
import pywintypes
import win32api
import win32clipboard
import win32con
import win32event
import win32file
import win32gui
import win32pipe
import win32process
import win32security
import winioctlcon
from apex.auto_updater import get_updater_id
from comtypes.client import CreateObject
from pynt.constants import E_FILE_NOT_FOUND, E_PATH_NOT_FOUND, FOLDERID_Desktop, FOLDERID_Documents, FOLDERID_Downloads, FOLDERID_LocalDocuments, FOLDERID_LocalDownloads, FOLDERID_LocalMusic, FOLDERID_LocalPictures, FOLDERID_LocalVideos, FOLDERID_Music, FOLDERID_Pictures, FOLDERID_SkyDrive, FOLDERID_SkyDriveDocuments, FOLDERID_SkyDrivePictures, FOLDERID_Videos, KEY_ALL_ACCESS, KEY_READ, KEY_WOW64_32KEY, KEY_WOW64_64KEY, REG_SZ, S_FALSE
from pynt.dlls.shell32 import shell32
from pynt.dlls.shlwapi import shlwapi
from pynt.headers.WinError import ERROR_ACCESS_DENIED, ERROR_INVALID_PARAMETER, ERROR_SIGNAL_REFUSED
from pynt.helpers.general import FormattedWindowsError, windows_error
from pynt.helpers.registry import enum_registry_subkeys_as_keys, registry_key, safe_delete_regvalue, safe_read_registry_value, set_registry_value
from pynt.helpers.shell import open_folder_and_select_items, shell_get_known_folder_path
from six.moves import range
from six.moves.winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE
from win32api import GetLongPathNameW, GetSystemDirectory
from win32com.shell import shell
from win32job import JobObjectBasicProcessIdList, QueryInformationJobObject
from winffi.dbghelp.api import MiniDumpNormal, MiniDumpWriteDump
from winffi.kernel32.api import FILE_ATTRIBUTE_HIDDEN, FILE_ATTRIBUTE_SYSTEM, GetCurrentProcess, GetFileAttributesW, GetFileSystemNameByHandleW, GetModuleFileName, SetFileAttributesW
from winffi.shell32.api import CSIDL_DESKTOP, CSIDL_MYMUSIC, CSIDL_MYPICTURES, CSIDL_MYVIDEO, CSIDL_PERSONAL, CSIDL_PROFILE, CSIDL_SENDTO, FO_COPY, FO_MOVE, FOF_ALLOWUNDO, FOF_NO_UI, SHFileOperation
from winshell.api import get_short_path_name
from build_number import BUILD_KEY, is_frozen, is_full_msix, is_store_managed, VERSION
from dropbox.client.constants.win import common_appdata_path, COMPAT_MODE_FLAG_LOCATION, DEFAULT_KILL_PROCESS_BY_NAME_TIMEOUT_MS, DROPBOX_UPDATER_CLIENT_STATE_KEY, KillProcessByNameResult, NAMED_PROCESS_EVENT_PREFIX, UNSUPPORTED_COMPAT_MODE_FLAGS, WinProcessInfo
from dropbox.client.flush_and_terminate.constants import FLUSH_AND_TERMINATE
from dropbox.client.ui.common.dialog_constants import IconType
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import is_short_path
from dropbox.foundation.reporting import report_app_framework_event, report_app_framework_event_restricted
from dropbox.foundation.runtime import Interpreter
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.fsutil import CreateHiddenSymlinkStatus
from dropbox.functions import convert_to_twos_complement, file_extension, lenient_decode, make_bytes, natural_sort_cmp, synchronized
from dropbox.gui import message_sender, spawn_thread_with_name
from dropbox.i18n import trans
from dropbox.install_type import get_dropbox_install_type, InstallType
from dropbox.trace import TRACE
from dropbox.win32.com_helper import uses_com
from dropbox.win32.internal import add_shortcut_to_user_location, create_shortcut, executable, get_user_folder_path, get_volumes, GetSystemWow64Directory, IO_REPARSE_TAG_MOUNT_POINT, is_admin, is_uac_enabled, remove_shortcut_from_user_location, ShellExecuteW, tcp_parameters
from dropbox.win32.kernel32 import is_os_64bit
from dropbox.win32.psapi import EnumProcesses
from dropbox.win32.version import WIN10, WINDOWS_VERSION, WINDOWS_VERSION_STRING
from dropbox.win32_util import find_media_type
MYPY = False
if MYPY:
    from dropbox.client.ui.common.dialogs import DialogController
SHORTCUT_ICON_OFFSET = 0
ASSOCSTR_FRIENDLYAPPNAME = 4
DIR_WRITE_PERMISSIONS = [
    'DELETE',
    'WRITE_DAC',
    'WRITE_OWNER',
    'FILE_ADD_FILE',
    'FILE_ADD_SUBDIRECTORY',
    'FILE_WRITE_EA',
    'FILE_DELETE_CHILD',
    'FILE_WRITE_ATTRIBUTES']
FILE_WRITE_PERMISSIONS = [
    'DELETE',
    'WRITE_DAC',
    'WRITE_OWNER',
    'FILE_WRITE_DATA',
    'FILE_APPEND_DATA',
    'FILE_WRITE_EA',
    'FILE_DELETE_CHILD',
    'FILE_WRITE_ATTRIBUTES']
TRUSTED_INSTALLER_SID = 'S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464'
ONEDRIVE_ACCOUNTS_KEY = 'SOFTWARE\\Microsoft\\OneDrive\\Accounts'

def get_fs_type(path = None):
    temp_handle = win32file.CreateFileW(path, 0, win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE | win32file.FILE_SHARE_DELETE, None, win32file.OPEN_EXISTING, win32file.FILE_FLAG_BACKUP_SEMANTICS, None)
    
    try:
        win32api.CloseHandle(temp_handle)
        return (GetFileSystemNameByHandleW(temp_handle), None)
    except:
        win32api.CloseHandle(temp_handle)



def get_volume_info(path = None):
    raise NotImplementedError('get_volume_info is not implemented on windows')


def get_sid_string():
    token = win32security.OpenProcessToken(win32api.GetCurrentProcess(), win32security.TOKEN_QUERY)
    (sid, _) = win32security.GetTokenInformation(token, win32security.TokenUser)
    return win32security.ConvertSidToStringSid(sid)


def register_module(module_path = None, is_64bit = None, flags = None):
    if not is_64bit and is_os_64bit():
        return None
    system_path = GetSystemDirectory() if not None else GetSystemWow64Directory()
    command_path = os.path.join(system_path, 'regsvr32.exe')
    TRACE('Registering module %r', module_path)
# WARNING: Decompyle incomplete


def unregister_module(module_path = None, is_64bit = None, flags = None):
    if not is_64bit and is_os_64bit():
        return None
    system_path = GetSystemDirectory() if not None else GetSystemWow64Directory()
    command_path = os.path.join(system_path, 'regsvr32.exe')
    TRACE('Unregistering module %r', module_path)
# WARNING: Decompyle incomplete


def get_executable():
    return GetModuleFileName(None)


def get_executable_dir():
    return os.path.dirname(get_executable())


def get_contents_root():
    install_dir = get_install_dir()
    return os.path.join(install_dir, VERSION)


def get_repo_root_unfrozen():
    pass
# WARNING: Decompyle incomplete


def get_install_dir():
    exe = get_executable()
    if is_frozen() and 'python' in os.path.basename(exe):
        repo_root = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')
        return os.path.abspath(os.path.join(repo_root, 'build', 'Debug'))
    return get_executable_dir()


_ = lambda x: x
FOLDER_INFOTIP = _('A secure home for all your photos, documents, and videos.')
del _
MEGABYTE = 1048576
PIPE_REJECT_REMOTE_CLIENTS = 8
FILE_FLAG_FIRST_PIPE_INSTANCE = 524288
DRIVE_SEPARATOR = ':'
ERROR_PIPE_BUSY = 231

def raise_application():
    pass


def copy_text_to_clipboard_external(text):
    win32clipboard.OpenClipboard()
    
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()
        return None
    except:
        win32clipboard.CloseClipboard()



def get_text_from_clipboard_external():
    win32clipboard.OpenClipboard()
    
    try:
        win32clipboard.CloseClipboard()
        return win32clipboard.GetClipboardData(win32con.CF_TEXT)
    except:
        win32clipboard.CloseClipboard()



def launch_new_dropbox(opts = None, wait = None, timeout = None):
    TRACE('Launching second Dropbox process with args %r', opts)
    return _launch_new_dropbox(opts, wait, timeout)


def restart_unwatched(opts = None):
    opts = [
        '/restart',
        str(win32process.GetCurrentProcessId())] + list(opts)
    _launch_new_dropbox(opts)
    Interpreter._signal_and_exit(ExitCode.SUCCESS)


def _launch_new_dropbox(opts = None, wait = None, timeout = None):
    cmd = executable(list(opts))
    if not is_frozen():
        maybe_detach_debugger = maybe_detach_debugger
        import dropbox.client.debugger
        maybe_detach_debugger()
    if wait:
        
        try:
            TRACE('Waiting for second Dropbox process to finish.')
            p = subprocess.Popen(cmd)
            p.communicate(timeout = timeout)
            return p
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
        except:
            fn = cmd[0]
            args = ' '.join(cmd[1:])
            
            try:
                ShellExecuteW(0, 'open', fn, args, None, win32con.SW_SHOW)
                
                try:
                    pass
                except Exception:
                    report_exception(component = DesktopComponent.UNKNOWN)
                    win32api.ShellExecute(0, 'open', fn.encode('mbcs'), args.encode('mbcs'), None, win32con.SW_SHOW)
                    
                    try:
                        pass
                    try:
                        pass
                    except Exception:
                        report_exception(component = DesktopComponent.UNKNOWN)

                    return None





def path_filter(local_path, server_path, active_details = (None,)):
    return True


def hard_exit_unwatched(exit_code = None):
    Interpreter._signal_and_exit(exit_code)

get_drives = get_volumes
_StrCmpLogicalW: 'Optional[Any]' = None

def get_named_process_event(event_name, pid, access):
    name = '%s_%s_%d' % (NAMED_PROCESS_EVENT_PREFIX, event_name, pid)
    return win32event.OpenEvent(access, 0, name)


def natural_basename_sort_cmp(bn1, bn2):
    pass
# WARNING: Decompyle incomplete


def compatibility_mode_check(dialog_controller = None):
    pass
# WARNING: Decompyle incomplete


def _sorted_procs_ancillary_procs_last(procs = None):
    non_ancillary_procs = []
    ancillary_procs = []
    for proc in procs:
        pid = proc.pid
        psutil_process = psutil.Process(pid)
        cmdline = psutil_process.cmdline()
        TRACE('_sorted_procs_ancillary_procs_last: pid=%s cmdline=%r', pid, cmdline)
        command_bytes = make_bytes(cmdline[1]) if cmdline and len(cmdline) > 1 else None
        is_exit_monitor = make_bytes('-type:exit-monitor') == command_bytes
        is_crashpad = make_bytes('-type:crashpad-handler') == command_bytes
        if is_exit_monitor or is_crashpad:
            ancillary_procs.append(proc)
        else:
            non_ancillary_procs.append(proc)
        except psutil.Error:
            non_ancillary_procs.append(proc)
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
            TRACE('Could not get cmdline for process: %r', proc)
            continue
        return non_ancillary_procs + ancillary_procs


def kill_other_instances():
    (success, _) = kill_process_by_name('%s.exe' % BUILD_KEY, send_signal = False, force_kill = True, timeout = 20000)
    return success


def kill_process_by_name(target = None, other_users = None, send_signal = None, force_kill = (False, False, True, DEFAULT_KILL_PROCESS_BY_NAME_TIMEOUT_MS), timeout = ('target', 'str', 'other_users', 'bool', 'send_signal', 'bool', 'force_kill', 'bool', 'timeout', 'int', 'return', 'KillProcessByNameResult')):
    success = True
    kill_count = 0
    target = target.lower()
    if other_users:
        enable_debug_privileges()
    
    def get_processname(h = None):
        p = ctypes.create_unicode_buffer(2048)
        ret = ctypes.windll.psapi.GetProcessImageFileNameW(int(h), ctypes.byref(p), 2048)
    # WARNING: Decompyle incomplete

    mypid = win32process.GetCurrentProcessId()
    procs_to_kill = []
    
    try:
        job_processes = QueryInformationJobObject(None, JobObjectBasicProcessIdList)
    except pywintypes.error:
        job_processes = ()
        report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UNKNOWN)

    
    try:
        for pid in EnumProcesses():
            if pid == mypid or pid in job_processes:
                
                try:
                    continue
                    h = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, 0, pid)
                except pywintypes.error:
                    e = None
                    if e.args[0] in (5, 87):
                        e = None
                        del e
                        
                        try:
                            continue
                            raise 
                            e = None
                            del e
                            processname = get_processname(h)
                            if processname.lower().endswith('\\' + target):
                                TRACE('Adding process %r (pid %s) to list of processes to be killed', processname, pid)
                                h_kill = win32api.OpenProcess(win32con.PROCESS_TERMINATE | win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ | win32con.SYNCHRONIZE, 0, pid)
                            else:
                                except pywintypes.error:
                                    e = None
                                    if e.args[0] in (5, 87):
                                        e = None
                                        del e
                                        win32api.CloseHandle(h)
                                        
                                        try:
                                            continue
                                            raise 
                                            e = None
                                            del e
                                            procs_to_kill.append(WinProcessInfo(handle = h_kill, name = processname, pid = pid))
                                            win32api.CloseHandle(h)
                                        try:
                                            continue
                                            except Exception:
                                                TRACE('While examining %d:', pid)
                                                report_exception(component = DesktopComponent.UNKNOWN)
                                                
                                                try:
                                                    continue
                                                    
                                                    try:
                                                        procs_to_kill = _sorted_procs_ancillary_procs_last(procs_to_kill)
                                                        if send_signal:
                                                            procs_to_wait_on = []
                                                            for proc_info in procs_to_kill:
                                                                (_, processname, pid) = proc_info
                                                                TRACE('Sending FLUSH_AND_TERMINATE signal to process %r (pid %s)', processname, pid)
                                                                h_event = get_named_process_event(FLUSH_AND_TERMINATE, pid, win32event.EVENT_MODIFY_STATE)
                                                                win32event.PulseEvent(h_event)
                                                                kill_count += 1
                                                                procs_to_wait_on.append(proc_info)
                                                                report(data_name = 'win-startup', event_name = 'sent_flush_and_terminate', sent_to_process_name = os.path.basename(processname), sent_to_pid = pid)
                                                                
                                                                try:
                                                                    continue
                                                                    except pywintypes.error:
                                                                        e = None
                                                                        if e.args[0] == 2:
                                                                            TRACE('Event not found while signaling %d:', pid)
                                                                            procs_to_wait_on.append(proc_info)
                                                                            
                                                                            try:
                                                                                e = None
                                                                                del e
                                                                                continue
                                                                                if e.args[0] == 5:
                                                                                    TRACE('Access denied while signaling %d:', pid)
                                                                                    
                                                                                    try:
                                                                                        e = None
                                                                                        del e
                                                                                        continue
                                                                                        report_exception(component = DesktopComponent.UNKNOWN)
                                                                                        
                                                                                        try:
                                                                                            e = None
                                                                                            del e
                                                                                            continue
                                                                                            e = None
                                                                                            del e
                                                                                            
                                                                                            try:
                                                                                                if procs_to_wait_on:
                                                                                                    handles = procs_to_wait_on()
                                                                                                    win32event.WaitForMultipleObjects(handles, 1, timeout)
                                                                                                for handle, name, pid in procs_to_kill:
                                                                                                    if win32process.GetExitCodeProcess(handle) == win32con.STILL_ACTIVE:
                                                                                                        report(data_name = 'win-startup', event_name = 'flush_and_terminate_timeout', sent_to_process_name = os.path.basename(name), sent_to_pid = pid)
                                                                                                        if force_kill:
                                                                                                            TRACE('Process %d is active. Terminating forcefully.', pid)
                                                                                                            kill_process_by_handle(handle, timeout)
                                                                                                            report(data_name = 'win-startup', event_name = 'force_terminate_success', sent_to_process_name = os.path.basename(name), sent_to_pid = pid)
                                                                                                            
                                                                                                            try:
                                                                                                                continue
                                                                                                                except Exception:
                                                                                                                    success = False
                                                                                                                    kill_count -= 1
                                                                                                                    report(data_name = 'win-startup', event_name = 'force_terminate_failure', sent_to_process_name = os.path.basename(name), sent_to_pid = pid)
                                                                                                                    report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
                                                                                                                    
                                                                                                                    try:
                                                                                                                        continue
                                                                                                                        
                                                                                                                        try:
                                                                                                                            TRACE('Failed to kill process %r.', name)
                                                                                                                            success = False
                                                                                                                            kill_count -= 1
                                                                                                                            continue
                                                                                                                            for h_kill, _, _ in procs_to_kill:
                                                                                                                                if h_kill:
                                                                                                                                    win32api.CloseHandle(h_kill)
                                                                                                                        except:
                                                                                                                            for h_kill, _, _ in procs_to_kill:
                                                                                                                                if h_kill:
                                                                                                                                    win32api.CloseHandle(h_kill)
                                                                                                                                return KillProcessByNameResult(success = success, kill_count = kill_count)
















def kill_process_by_handle(h = None, timeout = None):
    
    try:
        win32process.TerminateProcess(int(h), ERROR_SIGNAL_REFUSED)
        if timeout > 0:
            win32event.WaitForSingleObject(h, timeout)
            return None
        return None
    except pywintypes.error:
        e = None
        if e.args[0] != ERROR_INVALID_PARAMETER:
            raise 
        e = None
        del e
        return None
        e = None
        del e


enable_debug_privileges = (lambda : htoken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), ntsecuritycon.TOKEN_ADJUST_PRIVILEGES | ntsecuritycon.TOKEN_QUERY)id = win32security.LookupPrivilegeValue(None, ntsecuritycon.SE_DEBUG_NAME)newPrivileges = [
(id, ntsecuritycon.SE_PRIVILEGE_ENABLED)]win32security.AdjustTokenPrivileges(htoken, 0, newPrivileges))()

def show_folder(full_path = None):
    launch_folder(full_path)


def launch_folder(full_path = None, force_foreground = None, cleanup = None):
    pass
# WARNING: Decompyle incomplete


def launch_app(full_path):
    
    try:
        os.startfile(full_path)
        return None
    except WindowsError:
        e = None
        raise IOError(e.winerror, e.strerror)
        e = None
        del e



def executable_for_file(full_path = None):
    pbuf = ctypes.create_unicode_buffer(MAX_PATH)
    ret = shell32.FindExecutableW(full_path, None, pbuf)
    if ret <= 32:
        return None
    return None.path.basename(pbuf.value).lower()


def assoc_query_string_for_file(full_path = None, assoc_string_id = None):
    file_ext = file_extension(full_path, False)
    outsize = DWORD(0)
    
    try:
        shlwapi.AssocQueryStringW(0, assoc_string_id, LPCWSTR(file_ext), None, None, ctypes.byref(outsize))
    except WindowsError:
        e = None
        if e.winerror != S_FALSE:
            e = None
            del e
            return None
        e = None
        del e
    except:
        e = None
        del e

    outval = ctypes.create_unicode_buffer(outsize.value)
    
    try:
        shlwapi.AssocQueryStringW(0, assoc_string_id, LPCWSTR(file_ext), None, outval, ctypes.byref(outsize))
    except WindowsError:
        e = None
        e = None
        del e
        return None
        e = None
        del e

    return outval.value


def app_for_file(full_path = None):
    return executable_for_file(full_path)


def app_display_name_for_file(full_path = None):
    return assoc_query_string_for_file(full_path, ASSOCSTR_FRIENDLYAPPNAME)


def is_dir(full_path):
    return os.path.isdir(full_path)


def get_long_path(path = None):
