# Source Generated with Decompyle++
# File: reparse_point_placeholder.pyc (Python 3.11)

from __future__ import absolute_import, annotations, division, print_function
import contextlib
import sys
import uuid
from typing import Iterator, Text
import pywintypes
import win32file
import winerror
import winnt
from pynt.helpers.general import FormattedWindowsError
from six import reraise
from winffi.ntdll import CreateDisposition, CreateOption
from file_system import windows_fileapi as fileapi
from file_system.exceptions import create_is_a_directory_error
from file_system.util import convert_os_error
from file_system.windows_error import convert_pywin_error_fs_error_dec, windows_error_to_errno
from abstract_placeholder import AbstractPlaceholder, SimpleStat
from abstract_placeholder_fs_mixin import DuplicatePlaceholderOpenError
from reparse_point_utils import get_reparse_point_from_handle, read_file_system_id_from_handle, set_reparse_point_from_handle, set_sparse_file_from_handle, unset_reparse_point_from_handle, unset_sparse_file_from_handle
from dropbox.functions import int64_cast
from dropbox.infinite.exceptions import InfinitePlaceholderDecodeError, NotAnInfinitePlaceholderError
from dropbox.shared.local_path import WindowsPath
from dropbox.shared.placeholder_details import PlaceholderDetails
from dropbox.sync_engine_boundary.client_lib.windows_path_util import nt_escape_and_convert_to_unicode
from dropbox.sync_engine_boundary.file_system_exceptions import create_io_error
from dropbox.sync_engine_boundary.infinite.win.reparse_point_placeholder_context import ReparsePointPlaceholderContext
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from pywintypes import HANDLEType
ERROR_SHARING_VIOLATION = 32

class ReparsePointPlaceholder(AbstractPlaceholder):
    _open_placeholder = (lambda volume_guid = None, inode = staticmethod, need_write_access = convert_pywin_error_fs_error_dec: volume_path = '\\\\?\\Volume{%s}' % str(uuid.UUID(bytes_le = bytes(volume_guid))).upper()TRACE('Attempting to open %s:%r as a placeholder (Write Access)', volume_path, inode)flags = winnt.GENERIC_READ | winnt.FILE_READ_ATTRIBUTESsharing = win32file.FILE_SHARE_DELETE | win32file.FILE_SHARE_READif need_write_access:
flags |= winnt.GENERIC_WRITEelse:
sharing |= win32file.FILE_SHARE_WRITEtry:
volume_handle = fileapi.create_file(volume_path, 0, fileapi.FILE_SHARE_READ | fileapi.FILE_SHARE_WRITE | fileapi.FILE_SHARE_DELETE, fileapi.OPEN_EXISTING, 0)handle = fileapi.nt_create_file_from_file_id(inode, volume_handle, flags, 0, CreateDisposition.FILE_OPEN, CreateOption.FILE_OPEN_BY_FILE_ID | CreateOption.FILE_OPEN_REPARSE_POINT, sharing)handleexcept pywintypes.error:
error = Noneif error.winerror == winerror.ERROR_ACCESS_DENIED:
reraise(NotAnInfinitePlaceholderError, NotAnInfinitePlaceholderError(), sys.exc_info()[2])else:
raise error = Nonedel errorNoneerror = Nonedel error)()()
    
    def __init__(self = None, local_handle = None):
        self._local_handle = local_handle
        self._lock = Lock()

    open_from_context = (lambda context = None, need_write_access = staticmethod: pass# WARNING: Decompyle incomplete
)()()
    create = (lambda local_path = None, size = staticmethod, placeholder_details = convert_pywin_error_fs_error_dec: unicode_path = nt_escape_and_convert_to_unicode(local_path)TRACE('Attempting to set %r as a placeholder: %r', unicode_path, placeholder_details)handle = Nonetry:
handle = win32file.CreateFileW(unicode_path, win32file.GENERIC_WRITE, 0, None, win32file.OPEN_ALWAYS, win32file.FILE_ATTRIBUTE_NORMAL | win32file.FILE_FLAG_OPEN_REPARSE_POINT, None)fileinfo = fileapi.get_file_information_by_handle(handle.handle)fileapi.set_file_attributes_by_handle(handle.handle, fileinfo.file_attributes | winnt.FILE_ATTRIBUTE_OFFLINE, False)placeholder_data = placeholder_details.encode()set_reparse_point_from_handle(handle, placeholder_data)set_sparse_file_from_handle(handle, size)try:
passexcept pywintypes.error:
error = Noneif error.winerror == winerror.ERROR_ACCESS_DENIED:
exc = create_is_a_directory_error(unicode_path)reraise(type(exc), exc, sys.exc_info()[2])else:
raise try:
error = Nonedel errorerror = Nonedel errortry:
win32file.CloseHandle(handle)Noneexcept:
win32file.CloseHandle(handle))()()
    read = (lambda self = None: PlaceholderDetails.decode(self.read_raw()))()
    read_raw = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    prepare_for_write = (lambda self = None, size = None: try:
self.read()except InfinitePlaceholderDecodeError:
passfileapi.set_dont_modify_file_times(int(self._local_handle))self._lock.acquire()try:
win32file.SetFilePointer(self._local_handle, 0, win32file.FILE_BEGIN)win32file.SetEndOfFile(self._local_handle)win32file.SetFilePointer(self._local_handle, size, win32file.FILE_BEGIN)win32file.SetEndOfFile(self._local_handle)self._lock.release()except:
self._lock.release()unset_sparse_file_from_handle(self._local_handle))()
    write = (lambda self = None, data = None, offset = convert_pywin_error_fs_error_dec: reparse_data = get_reparse_point_from_handle(self._local_handle)# WARNING: Decompyle incomplete
)()
    read_data = (lambda self = None, offset = None, length = convert_pywin_error_fs_error_dec: reparse_data = get_reparse_point_from_handle(self._local_handle)# WARNING: Decompyle incomplete
)()
    unset = (lambda self = None: if unset_reparse_point_from_handle(self._local_handle):
fileinfo = fileapi.get_file_information_by_handle(self._local_handle.handle)fileapi.set_file_attributes_by_handle(self._local_handle.handle, fileinfo.file_attributes & ~(winnt.FILE_ATTRIBUTE_OFFLINE), False)unset_sparse_file_from_handle(self._local_handle)None)()
    reset = (lambda self = None, size = None: try:
self.read()except InfinitePlaceholderDecodeError:
passself._lock.acquire()try:
set_sparse_file_from_handle(self._local_handle, size)self._lock.release()Noneexcept:
self._lock.release())()
    
    def is_placeholder(self = None):
        
        try:
            self.read()
            return True
        except InfinitePlaceholderDecodeError:
            return True
            except NotAnInfinitePlaceholderError:
                return False


    file_system_id = (lambda self = None: read_file_system_id_from_handle(self._local_handle))()
    
    def resolve_path(self = None):
        return fileapi.get_final_path_name_by_handle(self._local_handle.handle, 0)

    set_file_mtime = (lambda self = None, mtime = None: fileapi.set_mtime_by_handle(self._local_handle.handle, mtime))()
    
    def simple_stat(self = None):
        convert_os_error()
        info = fileapi.get_file_information_by_handle(self._local_handle.handle)
        None(None, None)
        return 
        with None:
            if not None, SimpleStat(volumeid = int64_cast(info.volume_serial_number), inode = int64_cast(info.file_index), size = info.file_size, mtime = info.last_write_time):
                pass


