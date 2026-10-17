# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

from __future__ import absolute_import, division
import ctypes
import os
from ctypes.wintypes import HANDLE
from typing import Optional, Text
from winerror import ERROR_ACCESS_DENIED, ERROR_FILE_NOT_FOUND, ERROR_NO_MORE_FILES, ERROR_PATH_NOT_FOUND
from winffi.kernel32.api import FILE_ATTRIBUTE_DIRECTORY, FILE_ATTRIBUTE_REPARSE_POINT, GetFileAttributesW, INVALID_HANDLE_VALUE
from common import _DirectoryAbstract, _DirectoryEntryBase, Path
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.functions import is_four_byte_unicode
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_REGULAR
from dropbox.trace import TRACE
from dropbox.win32.kernel32 import FILETIME, FIND_FIRST_EX_LARGE_FETCH, FindClose, FindExInfoBasic, FindExSearchNameMatch, FindFirstFileExW, FindNextFileW, GetLastError, WIN32_FIND_DATAW
WIN32_REPARSE_TAG_DFS = 'dfs'
WIN32_REPARSE_TAG_DFSR = 'dfsr'
WIN32_REPARSE_TAG_HSM = 'hsm'
WIN32_REPARSE_TAG_MOUNT_POINT = 'mount-point'
WIN32_REPARSE_TAG_RESERVED_ONE = 'reserved-one'
WIN32_REPARSE_TAG_RESERVED_RANGE = 'reserved-range'
WIN32_REPARSE_TAG_RESERVED_ZERO = 'reserved-zero'
WIN32_REPARSE_TAG_SIS = 'sis'
WIN32_REPARSE_TAG_SYMLINK = 'symlink'
WIN32_REPARSE_TAGS = (WIN32_REPARSE_TAG_DFS, WIN32_REPARSE_TAG_DFSR, WIN32_REPARSE_TAG_HSM, WIN32_REPARSE_TAG_MOUNT_POINT, WIN32_REPARSE_TAG_RESERVED_ONE, WIN32_REPARSE_TAG_RESERVED_RANGE, WIN32_REPARSE_TAG_RESERVED_ZERO, WIN32_REPARSE_TAG_SIS, WIN32_REPARSE_TAG_SYMLINK)

def win32_reparse_tag_to_human_readable(reparse_tag = None):
    return reparse_tag.replace('-', ' ')

GET_TAG = {
    0x8000000A: WIN32_REPARSE_TAG_DFS,
    0x80000012: WIN32_REPARSE_TAG_DFSR,
    0xC0000004: WIN32_REPARSE_TAG_HSM,
    0xA0000003: WIN32_REPARSE_TAG_MOUNT_POINT,
    1: WIN32_REPARSE_TAG_RESERVED_ONE,
    1: WIN32_REPARSE_TAG_RESERVED_RANGE,
    0: WIN32_REPARSE_TAG_RESERVED_ZERO,
    0x80000007: WIN32_REPARSE_TAG_SIS,
    0xA000000C: WIN32_REPARSE_TAG_SYMLINK }
CTYPES_INVALID_HANDLE_VALUE = HANDLE(INVALID_HANDLE_VALUE).value

class _DirectoryEntry(_DirectoryEntryBase):
    __slots__ = [
        'name',
        'size',
        'mtime',
        'ctime',
        'win32_reparse_type',
        'win32_file_attributes']
    
    def __init__(self, file_name, size = None, mtime = None, win32_reparse_type = None, win32_file_attributes = ('file_name', 'Path', 'size', 'int', 'mtime', 'float', 'win32_reparse_type', 'Optional[str]', 'win32_file_attributes', 'int', 'return', 'None')):
        self.name = file_name
        self.size = size
        self.mtime = mtime
        self.ctime = mtime
        self.win32_reparse_type = win32_reparse_type
        self.win32_file_attributes = win32_file_attributes

    type = (lambda self = None: FILE_TYPE_DIRECTORY if self.win32_file_attributes & FILE_ATTRIBUTE_DIRECTORY else FILE_TYPE_REGULAR)()
    
    def __repr__(self = None):
        return f'''_DirectoryEntry({self.name!r}, {self.size!r}, {self.mtime!r}, {self.win32_reparse_type!r}, {self.win32_file_attributes!r})'''



class Directory(_DirectoryAbstract):
    
    def __repr__(self = None):
        return easy_repr(self, 'path', 'search_handle', 'file_data', 'first_file')

    
    def __init__(self = None, path = None, no_atime = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _make_long_paths_safe(self = None, path = None):
        if path.startswith('\\\\?\\'):
            return path
        return None + path

    
    def close(self = None):
        if self.search_handle:
            if not FindClose(self.search_handle):
                raise Exception(f'''FindClose() --> {GetLastError()!r}''')
            self.search_handle = None
            return None

    
    def reset(self = None):
        self.close()
        self.__init__(self.path)

    
    def debug_trace_path_info(self = None):
        
        try:
            exists = os.path.exists(self._max_length_safe_path)
            TRACE('!! exists=%r', exists)
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            TRACE("!! couldn't check exists for %r", self._max_length_safe_path)

        
        try:
            contents = os.listdir(self._max_length_safe_path)
            TRACE('!! contents=%r', contents)
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            TRACE("!! couldn't check contents for %r", self._max_length_safe_path)

        
        try:
            the_stat = os.stat(self._max_length_safe_path)
            TRACE('!! the_stat=%r', the_stat)
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            TRACE("!! couldn't check the_stat for %r", self._max_length_safe_path)

        
        try:
            attrib = GetFileAttributesW(self._max_length_safe_path)
            TRACE('!! attrib=%r', attrib)
            return None
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)
            TRACE("!! couldn't check attrib for %r", self._max_length_safe_path)
            return None


    
    def one_entry(self = None):
        if not FindNextFileW(self.search_handle, ctypes.byref(self.file_data)):
            err = GetLastError()
            if err != ERROR_NO_MORE_FILES:
                self.debug_trace_path_info()
                raise Exception('FindNextFileW(%r, %r) --> %d' % (self.search_handle, self.file_data, err))
            self.first_file = None
            return False

    
    def file_time_to_unix_time(self = None, file_time = None):
        win_time = file_time.dwHighDateTime << 32 | file_time.dwLowDateTime
        return (win_time - 0x19DB1DED53E8000) / 1e+07

    
    def readdir(self = None):
        pass
    # WARNING: Decompyle incomplete


