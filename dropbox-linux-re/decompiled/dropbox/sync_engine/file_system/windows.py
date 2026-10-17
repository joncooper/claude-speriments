# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import
import ctypes
import errno
import os
import sys
import time
from contextlib import contextmanager
from ctypes import c_ulong, c_ushort, sizeof, Structure
from typing import Any, Callable, Optional, Text, Tuple, Union
import ntsecuritycon
import pywintypes
import win32api
import win32con
import win32file
import win32security
import winerror
import winioctlcon
import winnt
from mypy_extensions import NamedArg
from pynt.constants import ERROR_ACCESS_DENIED, ERROR_CANT_ACCESS_FILE, ERROR_FILE_NOT_FOUND, ERROR_ONLY_IF_CONNECTED, ERROR_SHARING_VIOLATION, ERROR_SYMLINK_NOT_SUPPORTED, ERROR_UNABLE_TO_MOVE_REPLACEMENT, ERROR_UNABLE_TO_MOVE_REPLACEMENT_2, ERROR_UNABLE_TO_REMOVE_REPLACED
from six.moves import range
from winffi.kernel32.api import GetFileAttributesW, SetFileAttributesW
from infinite.win.reparse_point_placeholder_fs_mixin import ReparsePointPlaceholderFileSystemMixin
from infinite.win.reparse_point_stub_folder_fs_mixin import ReparsePointStubFolderFileSystemMixinInterface
from  import windows_fileapi as fileapi
from abstract_file_system import AbstractFile
from ads_util import XAttrAttributesHandleWin
from constants import FILE_TYPE_DIRECTORY, FILE_TYPE_REGULAR, FILE_TYPE_WIN32_REPARSE_POINT
from exceptions import create_file_not_found_error, create_file_system_error, create_fs_invalid_argument_error, FileNotFoundError, FileSystemError, PermissionDeniedError
from indexing_attributes import IndexingAttributes
from pythonos import FileSystem as PythonFileSystem
from util import convert_os_error, convert_os_error_dec, FileSystemDirectory
from windows_error import convert_pywin_error_fs_error, convert_pywin_error_fs_error_dec, convert_pywin_error_ioerror_dec
from dropbox import fsutil
from dropbox.client.util.win import rename_file
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.functions import classproperty, int64_cast
from dropbox.infinite import infinite_platform_supported, infinite_stubfolders_enabled
from dropbox.misc import protect_closed
from dropbox.shared.local_path import WindowsPath
from dropbox.shared.util import const
from dropbox.sync_engine_boundary.client_lib.windows_path_util import is_escaped_nt_path, nt_escape_and_convert_to_unicode, nt_escape_unicode_path, nt_unescape_path, unescape_path
from dropbox.sync_engine_boundary.file_system_exceptions import ExclusiveAccessException, FSInvalidArgumentError
from dropbox.sync_event.report import report_sync_event, SyncEventName
from dropbox.trace import TRACE
from dropbox.win32.internal import get_symlink_target, NotASymlinkError
mode_flag_map = {
    'r': (win32con.GENERIC_READ, win32con.FILE_SHARE_READ | win32con.FILE_SHARE_DELETE | win32con.FILE_SHARE_WRITE, win32con.OPEN_EXISTING),
    'r+': (win32con.GENERIC_READ | win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, win32con.OPEN_EXISTING),
    'w': (win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, win32con.CREATE_ALWAYS),
    'w+': (win32con.GENERIC_READ | win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, win32con.CREATE_ALWAYS),
    'a': (win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, win32con.OPEN_ALWAYS),
    'a+': (win32con.GENERIC_READ | win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, win32con.OPEN_ALWAYS),
    'wp': (win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, win32con.OPEN_ALWAYS),
    'we': (win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, win32con.OPEN_EXISTING) }

def get_real_file_path(suspected_symlink):
    handle = fileapi.create_file(suspected_symlink, fileapi.GENERIC_READ, 0, fileapi.OPEN_EXISTING, 0)
    
    try:
        fileapi.close_handle(handle)
        return fileapi.get_final_path_name_by_handle(handle, 0)[4:]
    except:
        fileapi.close_handle(handle)



def is_drive_letter(char):
    d = ord(char)
    if  <= 65, d:
        pass
    elif not None, 65, d <= 90:
        pass
    return None if  <= 97, d else None, 65, d <= 90, 97, d <= 122


def is_root_without_slash(path):
