# Source Generated with Decompyle++
# File: internal.pyc (Python 3.11)

from __future__ import absolute_import
import ctypes
import os
import struct
import sys
import time
import winreg
from ctypes import c_int
from ctypes.wintypes import DWORD, HANDLE, HINSTANCE, HKEY, HWND, LONG, LPCWSTR, LPWSTR, UINT
from enum import IntEnum
from typing import Any, Callable, List, Optional, Text, Tuple
import mmapfile
import pywintypes
import win32api
import win32con
import win32event
import win32file
import win32security
import winerror
import winioctlcon
import winnt
from comtypes.client import CreateObject
from comtypes.persist import IPersistFile
from comtypes.shelllink import ShellLink
from pynt.constants import E_ACCESS_DENIED, E_BAD_PATHNAME, E_NOT_READY, E_PATH_NOT_FOUND
from pynt.helpers.registry import read_registry_value, registry_key
from win32com.shell import shell, shellcon
from win32file import INVALID_HANDLE_VALUE
from winffi.kernel32.api import FILE_ATTRIBUTE_DIRECTORY
from build_number import BUILD_KEY, is_frozen
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_assertion_error, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import convert_to_twos_complement
from dropbox.sync_engine_boundary.client_lib.windows_path_util import unescape_path
from dropbox.trace import TRACE, TraceSegment
from dropbox.win32.com_helper import uses_com
from dropbox.win32.kernel32 import FindFirstVolumeW, FindNextVolumeW, FindVolumeClose, GetLastError, GetVolumePathNamesForVolumeNameW, win_strerror

class RegKeyCouldntSetError(Exception):
    pass

ShellExecuteW = ctypes.windll.shell32.ShellExecuteW
ShellExecuteW.argtypes = [
    HWND,
    LPCWSTR,
    LPCWSTR,
    LPCWSTR,
    LPCWSTR,
    c_int]
ShellExecuteW.restype = HINSTANCE

def executable(opts = ((),)):
    return [
        sys.executable] + list(opts)

CTYPES_INVALID_HANDLE_VALUE = HANDLE(INVALID_HANDLE_VALUE).value
FILE_SYSTEM_FLAGS = (('FILE_CASE_PRESERVED_NAMES', 2), ('FILE_CASE_SENSITIVE_SEARCH', 1), ('FILE_FILE_COMPRESSION', 16), ('FILE_NAMED_STREAMS', 262144), ('FILE_PERSISTENT_ACLS', 8), ('FILE_READ_ONLY_VOLUME', 524288), ('FILE_SEQUENTIAL_WRITE_ONCE', 1048576), ('FILE_SUPPORTS_ENCRYPTION', 131072), ('FILE_SUPPORTS_EXTENDED_ATTRIBUTES', 8388608), ('FILE_SUPPORTS_HARD_LINKS', 4194304), ('FILE_SUPPORTS_OBJECT_IDS', 65536), ('FILE_SUPPORTS_OPEN_BY_FILE_ID', 16777216), ('FILE_SUPPORTS_REPARSE_POINTS', 128), ('FILE_SUPPORTS_SPARSE_FILES', 64), ('FILE_SUPPORTS_TRANSACTIONS', 2097152), ('FILE_SUPPORTS_USN_JOURNAL', 33554432), ('FILE_UNICODE_ON_DISK', 4), ('FILE_VOLUME_IS_COMPRESSED', 32768), ('FILE_VOLUME_QUOTAS', 32))

def masks(mask):
    pass
# WARNING: Decompyle incomplete


def _get_rest_of_info(ub = None):
    
    try:
        info = win32api.GetVolumeInformation(ub.value)
        mm = list(masks(info[-2]))
    except Exception:
        e = None
        if (isinstance(e, pywintypes.error) or e.args) and e.args[0] != 21:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)
        info = None
        mm = None
        e = None
        del e
    except:
        e = None
        del e

    ldw = DWORD()
    ub2 = ctypes.create_string_buffer(ctypes.sizeof(ctypes.c_wchar) * win32con.MAX_PATH * 5)
    if not GetVolumePathNamesForVolumeNameW(ub, ctypes.cast(ub2, LPWSTR), win32con.MAX_PATH * 5, ctypes.byref(ldw)):
        
        try:
            win_errno = GetLastError()
            raise WindowsError(win_errno, win_strerror(win_errno))
        except Exception:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)

        aliases = []
    else:
        aliases = ub2.raw.decode('utf16')[:int(ldw.value)].split('\x00')[:-2]
    return (ub.value, info, aliases, mm)


def get_volumes():
    ub = ctypes.create_unicode_buffer(win32con.MAX_PATH)
    h_vol = FindFirstVolumeW(ub, win32con.MAX_PATH)
    if h_vol == CTYPES_INVALID_HANDLE_VALUE:
        win_errno = GetLastError()
        raise WindowsError(win_errno, win_strerror(win_errno))
    to_ret = []
    
    try:
        to_ret.append(_get_rest_of_info(ub))
        ret = FindNextVolumeW(h_vol, ub, win32con.MAX_PATH)
        if not ret:
            pass
        else:
            to_ret.append(_get_rest_of_info(ub))
        FindVolumeClose(h_vol)
        return to_ret
    except:
        FindVolumeClose(h_vol)



def GetEnvironmentVariableW(lpName):
    max_env_size = 32767
    lpBuffer = ctypes.create_unicode_buffer(max_env_size)
    ret = ctypes.windll.kernel32.GetEnvironmentVariableW(LPCWSTR(Text(lpName)), lpBuffer, DWORD(max_env_size))
    if ret:
        return lpBuffer.value


try:
    _GetSystemWow64DirectoryW = ctypes.windll.kernel32.GetSystemWow64DirectoryW
    _GetSystemWow64DirectoryW.argtypes = [
        LPWSTR,
        UINT]
    _GetSystemWow64DirectoryW.restype = UINT
except Exception:
    _GetSystemWow64DirectoryW = None


def GetSystemWow64Directory():
    pass
# WARNING: Decompyle incomplete

LPDWORD = ctypes.POINTER(DWORD)
_RegQueryValueExW = ctypes.windll.advapi32.RegQueryValueExW
_RegQueryValueExW.argtypes = [
    HKEY,
    LPCWSTR,
    LPDWORD,
    LPDWORD,
    ctypes.c_void_p,
    LPDWORD]
_RegQueryValueExW.restype = LONG

class RegQueryValueExWError(Exception):
    pass


def RegQueryValueExW(hkey, value_name):
    buf_size = DWORD(0)
    _RegQueryValueExW(hkey.handle, value_name, None, None, None, ctypes.byref(buf_size))
    buf = ctypes.create_unicode_buffer(buf_size.value)
    val_typ = DWORD()
    ret = _RegQueryValueExW(hkey.handle, value_name, None, ctypes.byref(val_typ), buf, ctypes.byref(buf_size))
    TRACE('_RegQueryValueExW(%r, %r, %r) -> %r, %r, %r, %r', hkey, value_name, None, val_typ.value, buf.value, buf_size.value, ret)
    if ret != 0:
        raise RegQueryValueExWError(ret)
    return (buf.value, val_typ.value)


def is_admin(check_membership_only = None):
    pass
# WARNING: Decompyle incomplete


def is_uac_enabled():
    
    try:
        hkey = win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System', 0, win32con.KEY_READ)
        
        try:
            (val, val_typ) = win32api.RegQueryValueEx(hkey, 'EnableLUA')
            
            try:
                win32api.RegCloseKey(hkey)
                return val != 0
                win32api.RegCloseKey(hkey)
                
                try:
                    pass
                except Exception:
                    return False






def get_hive_name(hive = None):
    if hive in (win32con.HKEY_CURRENT_USER, winreg.HKEY_CURRENT_USER):
        return 'HKEY_CURRENT_USER'
    if None in (win32con.HKEY_LOCAL_MACHINE, winreg.HKEY_LOCAL_MACHINE):
        return 'HKEY_LOCAL_MACHINE'
    return str(hive)


class RegistryWowFlag(IntEnum):
    NONE = 0
    KEY_WOW64_64KEY = win32con.KEY_WOW64_64KEY
    KEY_WOW64_32KEY = win32con.KEY_WOW64_32KEY


def get_registry(value_name = None, default_value = None, hive = None, wow_flag = (win32con.HKEY_CURRENT_USER, RegistryWowFlag.NONE, None), key = ('value_name', 'Text', 'default_value', 'Optional[Text]', 'hive', 'int', 'wow_flag', 'RegistryWowFlag', 'key', 'Optional[Text]', 'return', 'Optional[Text]')):
    if not key:
        pass
    dropbox_key = 'SOFTWARE\\%s' % BUILD_KEY
    
    try:
        hkcu_dropbox = win32api.RegOpenKeyEx(hive, dropbox_key, 0, win32con.KEY_READ | wow_flag.value)
    except Exception:
        TRACE("Couldn't open %s %s key", get_hive_name(hive), dropbox_key)
        return 

    
    try:
        (value, _) = RegQueryValueExW(hkcu_dropbox, value_name)
        
        try:
            pass
        except Exception:
            TRACE("Couldn't read value %s %s %s", get_hive_name(hive), dropbox_key, value_name)
            value = default_value
            
            try:
                pass
            try:
                win32api.RegCloseKey(hkcu_dropbox)
            except:
                win32api.RegCloseKey(hkcu_dropbox)

            TRACE('Read value %s for key %s %s %s', value, get_hive_name(hive), dropbox_key, value_name)
            return value




def set_registry(value_name = None, value = None, hive = None):
    dropbox_key = 'SOFTWARE\\%s' % BUILD_KEY
    
    try:
        hkcu_dropbox = win32api.RegOpenKeyEx(hive, dropbox_key, 0, win32con.KEY_ALL_ACCESS)
    except Exception:
        report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)
        return None

    
    try:
        win32api.RegSetValueEx(hkcu_dropbox, value_name, 0, win32con.REG_SZ, value)
        
        try:
            pass
        except Exception:
            e = None
            raise RegKeyCouldntSetError(value_name + ':' + value), e
            except Exception:
                report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)
            except:
                
                try:
                    e = None
                    del e
                e = None
                del e
                try:
                    win32api.RegCloseKey(hkcu_dropbox)
                    return None
                except:
                    win32api.RegCloseKey(hkcu_dropbox)




CSIDL_FLAG_CREATE = 32768
relevant_env_vars = {
    shellcon.CSIDL_PROFILE: ('%USERPROFILE%', '%userprofile%'),
    shellcon.CSIDL_APPDATA: ('%APPDATA%', '%appdata%'),
    shellcon.CSIDL_WINDOWS: ('%SYSTEMROOT%', '%windir%') }
default_csidl_locs = {
    shellcon.CSIDL_PROGRAM_FILES: 'C:\\Program Files',
    shellcon.CSIDL_SYSTEM: 'C:\\Windows\\System32',
    shellcon.CSIDL_WINDOWS: 'C:\\Windows' }

def get_user_folder_path(flag = None, fallback_to_default = None):
    to_ret = ''
    TRACE('getting user folder path: %r', flag)
    
    try:
        to_ret = shell.SHGetFolderPath(0, flag | CSIDL_FLAG_CREATE, None, 0)
    except pywintypes.com_error:
        ex = None
        e_code = convert_to_twos_complement(ex.args[0])
        if e_code in (E_ACCESS_DENIED, E_BAD_PATHNAME, E_NOT_READY, E_PATH_NOT_FOUND):
            TRACE('!! getting user com_error: %r', ex)
        else:
            report_exception(component = DesktopComponent.UNKNOWN)
        ex = None
        del ex
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)

    if not to_ret:
        
        try:
            env_choices = relevant_env_vars[flag]
            TRACE('!! Failed to get user path; trying environment environment')
            for env in env_choices:
                maybe = GetEnvironmentVariableW(env)
                if maybe:
                    to_ret = maybe
                
                except Exception:
                    report_exception(component = DesktopComponent.UNKNOWN)
                    continue
        except KeyError:
            pass

        if to_ret and fallback_to_default:
            
            try:
                to_ret = default_csidl_locs[flag]
            except KeyError:
                pass

            if not to_ret:
                TRACE('!! Failed to get user path')
    return to_ret

create_shortcut = (lambda name, target = None, description = None, arguments = uses_com('create_shortcut'), icon_location = (None, None, None, None), working_directory = ('name', 'Any', 'target', 'Any', 'description', 'Optional[Any]', 'arguments', 'Optional[Any]', 'icon_location', 'Optional[Any]', 'working_directory', 'Optional[Any]', 'return', 'None'): TRACE('Creating shortcut %r', name)TRACE('  target=%r', target)TRACE('  arguments=%r', arguments)TRACE('  working_directory=%r', working_directory)TRACE('  icon_location=%r', icon_location)TRACE('  description=%r', description)shortcut = CreateObject(ShellLink)shortcut.SetPath(target)if working_directory:
shortcut.SetWorkingDirectory(working_directory)if description:
shortcut.SetDescription(description)if arguments:
shortcut.SetArguments(arguments)if icon_location:
try:
(i_fn, i_offset) = icon_locationTRACE("setting %r's shortcut icon to %r, %r", name, i_fn, i_offset)shortcut.SetIconLocation(i_fn, i_offset)except Exception:
report_exception(component = DesktopComponent.UNKNOWN)pf = shortcut.QueryInterface(IPersistFile)pf.Save(name, True)None)()

def remove_shortcut_from_user_location(location = None, dropbox_name = None):
    
    try:
        folder = get_user_folder_path(location)
        item_path = os.path.join(folder, '%s.lnk' % dropbox_name)
        if not os.path.exists(item_path):
            TRACE('Shortcut not removed (already gone): %s', item_path)
            return False
        if not is_frozen() and os.environ.get('DROPBOX_DEBUG_SHORTCUTS'):
            TRACE('Shortcut not removed (not a frozen build, set DROPBOX_DEBUG_SHORTCUTS=1 to enable): %s', item_path)
            return False
        TRACE('Removing shortcut: %s', item_path)
        os.remove(item_path)
        return True
    except Exception:
        report_exception(component = DesktopComponent.UNKNOWN)
        return False



def add_shortcut_to_user_location(location = None, dropbox_name = None, dest = None, arguments = (None, None), working_directory = ('location', 'Any', 'dropbox_name', 'str', 'dest', 'str', 'arguments', 'Optional[str]', 'working_directory', 'Optional[str]', 'return', 'None')):
    folder = get_user_folder_path(location)
    if not folder:
        TRACE("Couldn't add shortcut at %r with args: %r (get_user_folder_path returned %r)", location, arguments, folder)
        return None
    item_path = None.path.join(folder, '%s.lnk' % dropbox_name)
    if os.path.exists(item_path):
        TRACE('Shortcut not added (already exists): %s', item_path)
        return None
    if not is_frozen() and os.environ.get('DROPBOX_DEBUG_SHORTCUTS'):
        TRACE('Shortcut not added (not a frozen build, set DROPBOX_DEBUG_SHORTCUTS=1 to enable): %s', item_path)
        return None
    TRACE('Adding shortcut: %s', item_path)
    create_shortcut(item_path, dest, '%s - Sync your files online and across computers' % BUILD_KEY, arguments = arguments, working_directory = working_directory)


def _output_dbdebug_string(encoded_trace = None):
    trace = encoded_trace.decode('ascii')
    mm = mmapfile.mmapfile(None, 'DBNSIS_BUFFER', 4096, 0, 4096)
    buffer_event = win32event.OpenEvent(win32con.SYNCHRONIZE, 0, 'DBNSIS_BUFFER_READY')
    data_event = win32event.OpenEvent(win32con.EVENT_MODIFY_STATE, 0, 'DBNSIS_DATA_READY')
    win32event.WaitForSingleObject(buffer_event, 10000)
    mm.seek(0)
    frag = struct.pack('L', win32api.GetCurrentProcessId()) + trace.rstrip()[:2000].encode('utf16')[2:] + b'\x00\x00'
    mm.write(frag)
    mm.flush()
    win32event.SetEvent(data_event)

_tracer: 'Optional[Callable[[TraceSegment], None]]' = None

def check_nsis_tracing():
    pass
# WARNING: Decompyle incomplete


def reset_nsis_tracing():
    time.sleep(0.5)
    remove_high_trace_handler = remove_high_trace_handler
    import dropbox.client.high_trace
# WARNING: Decompyle incomplete


def tcp_parameters():
    to_ret = []
    subkey = 'SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters'
    hkey = registry_key(win32con.HKEY_LOCAL_MACHINE, subkey)
    if hkey:
        for _t in ('Tcp1323Opts', 'GlobalMaxTcpWindowSize', 'TcpWindowSize', 'EnablePMTUDiscovery'):
            v = read_registry_value(hkey, _t)
            to_ret.append((_t, v))
            except KeyError:
                continue
            except Exception:
                report_exception(component = DesktopComponent.UNKNOWN)
                continue
            None(None, None)
        with None:
            if not None:
                pass
    return to_ret

IO_REPARSE_TAG_MOUNT_POINT = 0xA0000003
IO_REPARSE_TAG_SYMLINK = 0xA000000C

def is_junction_point(path = None):
    
    try:
        reparse_buffer = get_reparse_buffer(path, False, strip_prefix = True)
    except pywintypes.error:
        reparse_buffer = None

# WARNING: Decompyle incomplete


class NotASymlinkError(Exception):
    pass


def get_symlink_target(path = None):
    reparse_buffer = get_reparse_buffer(path, True, strip_prefix = False)
# WARNING: Decompyle incomplete


def get_reparse_buffer(path = None, allow_directories = None, strip_prefix = None):
    
    try:
        if strip_prefix:
            path = path.lstrip('\\??\\')
            path = path.lstrip('\\\\?\\')
        handle = win32file.CreateFileW(path, winnt.FILE_READ_ATTRIBUTES, 0, None, win32con.OPEN_EXISTING, win32file.FILE_FLAG_BACKUP_SEMANTICS | win32file.FILE_FLAG_OPEN_REPARSE_POINT, None)
        file_info = win32file.GetFileInformationByHandle(handle)
        if allow_directories and file_info[0] & FILE_ATTRIBUTE_DIRECTORY == 0:
            return None
    except pywintypes.error:
        raise 
        except Exception:
            return None
        buffer_size = 128
        ioctl_buffer = None
        
        try:
            ioctl_buffer = win32file.DeviceIoControl(handle, winioctlcon.FSCTL_GET_REPARSE_POINT, None, buffer_size, None)
        except pywintypes.error:
            e = None
            if buffer_size > 16384:
                e = None
                del e
                return None
            if None.winerror in (winerror.ERROR_MORE_DATA, winerror.ERROR_INSUFFICIENT_BUFFER):
                buffer_size = buffer_size * 2
            else:
                e = None
                del e
                return None
            e = None
            del e
        except:
            e = None
            del e

        continue
        return ioctl_buffer



def is_kb2533623_installed():
    return hasattr(ctypes.windll.kernel32, 'AddDllDirectory')

