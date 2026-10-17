# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import glob
import math
import os
import struct
import time
import urllib
from ctypes import c_wchar_p
from enum import Enum
from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Text, Tuple
import ntsecuritycon
import psutil
import pywintypes
import win32api
import win32com.client as win32com
import win32con
import win32event
import win32evtlog
import win32file
import win32pipe
import win32process
import win32security
import win32ts
import winerror
from apex.metrics import Metric, MetricsReporter, Stats, Timer
from apex.util import process_architecture
from pynt.constants import FOLDERID_Documents, FOLDERID_Pictures, FOLDERID_SkyDriveDocuments, FOLDERID_SkyDrivePictures, KEY_ALL_ACCESS, KEY_CREATE_SUB_KEY, KEY_READ, KEY_WOW64_32KEY, KEY_WOW64_64KEY, REG_DWORD, REG_EXPAND_SZ, REG_SZ
from pynt.dlls.shell32 import shell32
from pynt.helpers.registry import create_registry_key, enum_registry_subkeys, hkey_to_str, key_to_str, registry_key, registry_key_with_error, safe_delete_regkey, safe_delete_regvalue, safe_read_registry_value, set_registry_value
from pynt.helpers.shell import shell_get_known_folder_path
from pywintypes import com_error
from six.moves import range
from six.moves.winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE
from win32api import RegCloseKey, RegOpenKeyEx
from win32com.shell import shellcon
import build_number
from build_number import assert_full_msix_no_registry_writes, BUILD_KEY, is_frozen, is_full_msix
from build_number.constants import WINDOWS_SHELL_EXT_VERSION
from build_number.features import feature_enabled
from dropbox.assertions import assert_
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.context_menu.wrapper import ContextMenuConfigWrapper
from dropbox.client.gandalf import Gandalf
from dropbox.client.installer.win_installer_sparse_msix import is_sparse_msix_registered, is_sparse_msix_required
from dropbox.client.message_queue import MessageQueueThread
from dropbox.client.multiaccount.role import Roles
from dropbox.client.shell.base import ShellControllerBase
from dropbox.client.shell.windows_mmf_file_reader import MemoryMappedFileReader
from dropbox.client.ui.icon_overlay import do_context_action, encode_menu, get_option_group, parse_verb, ShellExtensionInstallType
from dropbox.client.util.win import FIRST_SHELL_EXT_CLASS_GUID, get_install_dir, get_long_path, is_os_64bit, launch_new_dropbox, MIN_ICON_OVERLAY_KEY, register_module, SHELL_EXT_REG_KEY, unregister_module
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.dbexceptions import InterruptError
from dropbox.event import report, report_aggregate_event, sanitize_event_extra_dict
from dropbox.event_names import WIN_SHELL_EXTENSION_MONITOR_EVENT
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.fastwalk_bridge import fastwalk
from dropbox.fileutils import safe_remove
from dropbox.foundation.task_metrics import TaskTimingMetricReporter
from dropbox.functions import cached_property, convert_to_twos_complement, make_unicode
from dropbox.infinite.win.thumbnail_provider import WinThumbnailServer
from dropbox.install_type import get_dropbox_install_type, InstallType
from dropbox.preferences import DESKTOP_CUSTOMIZABLE_CONTEXT_MENU_STORMCROW_ENABLED
from dropbox.proto.nucleus.common_api_types_pb2 import LookupSyncIconReply
from dropbox.shared.local_path import LocalPath, WindowsPath
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockState
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.sync_root.interface import SyncRootManagerInterface
from dropbox.sync_root.types import SyncRootType
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
from dropbox.win32.internal import is_admin, RegQueryValueExW
from dropbox.win32.kernel32 import GetLastError
from dropbox.win32.version import WIN10, WIN11_VERSION_2109, WINDOWS_VERSION
if WINDOWS_VERSION.version_number() >= WIN10.version_number():
    import _bowbow
else:
    _bowbow = None
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
FIRST_SHELL_EXT_CLASS_REG_KEY = 'SOFTWARE\\Classes\\CLSID\\%s\\InProcServer32' % FIRST_SHELL_EXT_CLASS_GUID
SHELL_EXT_ICON_OVERLAY_REG_KEY = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellIconOverlayIdentifiers'

class OverlayIconState(object):
    OVERLAY_UNKNOWN = -1
    OVERLAY_INVALID = 0
    OVERLAY_UPTODATE = 1
    OVERLAY_MODIFIED = 2
    OVERLAY_NOSYNC = 3
    OVERLAY_SELSYNC = 4
    OVERLAY_UPTODATE_LOCKED = 5
    OVERLAY_MODIFIED_LOCKED = 6
    OVERLAY_INFINITE = 7
    OVERLAY_INFINITE_LOCKED = 8
    OVERLAY_MIXEDSTATE = 9
    OVERLAY_MIXEDSTATE_LOCKED = 10
    OVERLAY_MAX = OVERLAY_MIXEDSTATE_LOCKED

MAX_ICON_OVERLAYS = 11
NUM_DROPBOX_ICON_OVERLAYS = OverlayIconState.OVERLAY_MAX

class ShellExtensionNamedPipe(object):
    DROPBOX_PIPE_NAME = f'''\\\\.\\pipe\\{BUILD_KEY}Pipe'''
    ERROR_PIPE_BUSY = 231
    PIPE_REJECT_REMOTE_CLIENTS = 8
    FILE_FLAG_FIRST_PIPE_INSTANCE = 524288
    MAGIC = 50627330
    
    def __init__(self, app):
        self._app = app
        TRACE('Creating %s for %r', type(self).__qualname__, self.DROPBOX_PIPE_NAME)
        self._mutex = None
        self._overlapped = pywintypes.OVERLAPPED()
        self._overlapped.hEvent = win32event.CreateEvent(None, 0, 0, None)
        session_id = win32ts.ProcessIdToSessionId(win32api.GetCurrentProcessId())
        self._pipe_name = '%s_%d' % (self.DROPBOX_PIPE_NAME, session_id)
        self._bind()

    pipe_exists = (lambda pipe_name: try:
h = win32file.CreateFile(pipe_name, win32con.GENERIC_READ, 0, None, win32con.OPEN_EXISTING, win32con.FILE_FLAG_OVERLAPPED, None)h.Close()Trueexcept pywintypes.error:
e = Noneif e.args[0] == ShellExtensionNamedPipe.ERROR_PIPE_BUSY:
e = Nonedel eTruee = Nonedel eFalsee = Nonedel eexcept Exception:
False)()
    
    def _bind(self):
        TRACE('Creating named pipe: %s', self._pipe_name)
        sa = self.get_named_pipe_security_attributes()
        pipe_mode = win32con.PIPE_TYPE_MESSAGE | self.PIPE_REJECT_REMOTE_CLIENTS
        open_mode = win32con.PIPE_ACCESS_DUPLEX | win32file.FILE_FLAG_OVERLAPPED | self.FILE_FLAG_FIRST_PIPE_INSTANCE
        
        try:
            self.hPipe = win32pipe.CreateNamedPipe(self._pipe_name, open_mode, pipe_mode, 1, 0, 0, 6000, sa)
        except Exception:
            TRACE('!! Failed to create pipe to Shell Extension!')
            report_exception(component = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER)
            raise 

        self.interrupt = False

    
    def break_block(self):
        self.interrupt = True
        win32event.SetEvent(self._overlapped.hEvent)

    
    def get_message(self):
        
        try:
            hr = win32pipe.ConnectNamedPipe(self.hPipe, self._overlapped)
        except pywintypes.error:
            details = None
            if details.args[0] not in (109, 232):
                report_exception(component = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER)
            win32pipe.DisconnectNamedPipe(self.hPipe)
            details = None
            del details
            continue
            details = None
            del details

        if hr == winerror.ERROR_PIPE_CONNECTED:
            win32event.SetEvent(self._overlapped.hEvent)
        timeout = win32event.INFINITE
        waitHandles = (self._overlapped.hEvent,)
        rc = win32event.WaitForMultipleObjects(waitHandles, 0, timeout)
        if self.interrupt:
            self.interrupt = False
            raise InterruptError()
    # WARNING: Decompyle incomplete

    _parse_shell_request = (lambda cls, s: pass# WARNING: Decompyle incomplete
)()
    
    def respond(self = None, context = staticmethod, ret = classmethod):
        
        try:
            win32file.WriteFile(self.hPipe, b''.join((struct.pack('L', self.MAGIC), Text(ret).encode('utf16')[2:])))
            return None
        except pywintypes.error:
            e = None
            if e.args[0] in (winerror.ERROR_BROKEN_PIPE, winerror.ERROR_NO_DATA):
                report_exception(severity = Severity.TRACE, component = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER)
            else:
                raise 
            e = None
            del e
            return None
            e = None
            del e


    
    def complete_request(self, context):
        win32pipe.DisconnectNamedPipe(self.hPipe)

    
    def get_named_pipe_security_attributes(self):
        
        try:
            ph = win32process.GetCurrentProcess()
            th = win32security.OpenProcessToken(ph, win32security.TOKEN_ALL_ACCESS)
            info = win32security.GetTokenInformation(th, win32security.TokenGroups)
            for sid, group_id in info:
                if group_id & win32security.SE_GROUP_LOGON_ID == win32security.SE_GROUP_LOGON_ID:
                    logon_sid = sid
                
                raise Exception('No Logon Sid Found!')
                dacl = win32security.ACL()
                dacl.AddAccessAllowedAce(dacl.GetAclRevision(), win32con.GENERIC_ALL, logon_sid)
                network_sid = win32security.SID()
                network_sid.Initialize(ntsecuritycon.SECURITY_NT_AUTHORITY, 1)
                network_sid.SetSubAuthority(0, ntsecuritycon.SECURITY_NETWORK_RID)
                dacl.AddAccessDeniedAce(dacl.GetAclRevision(), win32con.GENERIC_ALL, network_sid)
                sd = win32security.SECURITY_DESCRIPTOR()
                sd.SetSecurityDescriptorDacl(1, dacl, 0)
                sa = win32security.SECURITY_ATTRIBUTES()
                sa.SECURITY_DESCRIPTOR = sd
        except Exception:
            report_exception(component = DesktopComponent.SHELL_INTEGRATION_FILE_EXPLORER)
            sa = None

        return sa



class ShellExtensionRequestType(Enum):
    MSG_INIT = 0
    MSG_FILE_STATUS = 1
    MSG_CONTEXT_OPTIONS = 3
    MSG_CONTEXT_ACTION = 4
    MSG_REPORT_FOLDER_DELETE = 10
    MSG_REQUEST_THUMBNAIL = 14
    MSG_MIGRATION = 255
    MSG_RETIRED_RESERVED = 2
    MSG_RETIRED_REQUEST_CHAIN = 5
    MSG_RETIRED_TOOLBAR_OPTIONS = 6
    MSG_RETIRED_TOOLBAR_ACTION = 7
    MSG_RETIRED_TRACE = 8
    MSG_RETIRED_VERSION = 9
    MSG_RETIRED_PID = 11
    MSG_RETIRED_REQUEST_FOLDER_MOVE = 12
    MSG_RETIRED_REQUEST_MOVEDENIAL_ACTION = 13
    MSG_RETIRED_REPORT_LOG_EVENT = 15
    
    def is_retired(self = None):
        return self in {
            ShellExtensionRequestType.MSG_RETIRED_RESERVED,
            ShellExtensionRequestType.MSG_RETIRED_REQUEST_CHAIN,
            ShellExtensionRequestType.MSG_RETIRED_TOOLBAR_OPTIONS,
            ShellExtensionRequestType.MSG_RETIRED_TOOLBAR_ACTION,
            ShellExtensionRequestType.MSG_RETIRED_TRACE,
            ShellExtensionRequestType.MSG_RETIRED_VERSION,
            ShellExtensionRequestType.MSG_RETIRED_PID,
            ShellExtensionRequestType.MSG_RETIRED_REQUEST_FOLDER_MOVE,
            ShellExtensionRequestType.MSG_RETIRED_REQUEST_MOVEDENIAL_ACTION,
            ShellExtensionRequestType.MSG_RETIRED_REPORT_LOG_EVENT}


WIN_SHELL_EXTENSION_MESSAGE_THREAD_NAME = 'WIN_SHELL_EXTENSION_MESSAGE_THREAD'
WIN_SHELL_EXTENSION_TELEMETRY_THREAD = 'WIN_SHELL_EXTENSION_TELEMETRY_THREAD'
SHELL_EXTENSION_AMP_NAMESPACE = 'desktop_shell_extension'
WIN_SHELL_EXTENSION_EXECUTION_METRICS_EVENT = 'shell-extension-execution-metrics'

class Windows10FileOutsideContextMenuFixer:
    should_show = True
    
    def __init__(self = None, sync_root_manager = None, filesystem = None):
        self.sync_root_manager = sync_root_manager
        self.filesystem = filesystem

    
    def _get_sync_root_paths(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _is_path_file_outside_of_sync_root(self = None, path = None):
        pass
    # WARNING: Decompyle incomplete

    
    def start_suppressing_menu_if_necessary(self = None, process_name = None, path = None):
        if self.should_show or WINDOWS_VERSION.version_number() >= WIN11_VERSION_2109:
            return False
        if None == 'dllhost.exe' and self._is_path_file_outside_of_sync_root(path):
            self.should_show = False
            return True

    
    def should_suppress_menu(self = None, process_name = None, path = None):
