# Source Generated with Decompyle++
# File: ads_util.pyc (Python 3.11)

from __future__ import absolute_import
import errno
from contextlib import contextmanager
from typing import Text
import win32api
import win32file
import winerror
import winnt
from pynt.helpers.general import FormattedWindowsError
from winffi.ntdll import CreateDisposition, CreateOption
from abstract_attributes_handle import AbstractAttributesHandle, DEFAULT_PRESERVED_ATTRS_NAME
from exceptions import create_io_error, PermissionDeniedError
from util import convert_errno_to_ioerror
from windows_error import windows_error_to_errno
from windows_fileapi import get_file_attributes_by_handle, nt_create_file_from_path, set_dont_modify_file_times, set_file_attributes_by_handle
from dropbox.exception.reporting import report_bad_assumption
from dropbox.infinite import infinite_stubfolders_enabled
from dropbox.misc import protect_closed
from dropbox.shared.local_path import WindowsPath
from dropbox.sync_engine_boundary.client_lib.windows_path_util import nt_escape_and_convert_to_unicode
MYPY = False
if MYPY:
    import ctypes.wintypes as ctypes
    from typing import Iterator, Optional, Union
    import pywintypes
    from util import FileSystemDirectory
    from windows import FileSystem, WindowsFileBase

def _dropbox_attr_stream(name = None):
    return 'com.dropbox.%s' % name

_clear_temporary_fs_attr_readonly = (lambda localpath = None, handle = None, open_reparse_point = contextmanager: pass# WARNING: Decompyle incomplete
)()

class XAttrAttributesHandleWin(AbstractAttributesHandle):
    
    def __init__(self = None, fs = None, path = None, open_dir_handle = (False, False), open_reparse_point = ('fs', 'FileSystem', 'path', 'WindowsPath', 'open_dir_handle', 'bool', 'open_reparse_point', 'bool', 'return', 'None')):
        self.fs = fs
        self.path = path
        self._closed = False
        attrs = win32api.GetFileAttributes(nt_escape_and_convert_to_unicode(path))
        self.fh = None
        self.do_relative_open = False
        self.open_reparse_point = open_reparse_point
        if attrs & win32file.FILE_ATTRIBUTE_DIRECTORY:
            if open_dir_handle:
                self.fh = fs.opendir(path)
                return None
            return None
        create_options = None
        if open_reparse_point:
            create_options |= CreateOption.FILE_OPEN_REPARSE_POINT
        self.fh = nt_create_file_from_path(path, None, winnt.FILE_READ_ATTRIBUTES, 0, CreateDisposition.FILE_OPEN, create_options, winnt.FILE_SHARE_DELETE | winnt.FILE_SHARE_READ | winnt.FILE_SHARE_WRITE)
        self.do_relative_open = True

    closed = (lambda self: self._closed)()
    
    def close(self):
        self._closed = True
        if self.fh:
            self.fh.close()
            return None

    open = (lambda self, plat: raise create_io_error(errno.ENOENT, filename = plat))()
    
    def _preserved_fname(self = None, name = property):
        return WindowsPath(f'''{Text(self.path)!s}:{_dropbox_attr_stream(name)!s}''')

    open_preserved = (lambda self = None, mode = None, name = protect_closed: pass# WARNING: Decompyle incomplete
)()
    readplat = (lambda self: pass)()
    remove_preserved = (lambda self = None, name = protect_closed: try:
convert_errno_to_ioerror()if self.do_relative_open:
access = winnt.SYNCHRONIZE | winnt.DELETE | winnt.FILE_READ_ATTRIBUTESsharing = winnt.FILE_SHARE_DELETE | winnt.FILE_SHARE_READ | winnt.FILE_SHARE_WRITEdisposition = CreateDisposition.FILE_OPENcreate_options = CreateOption.FILE_DELETE_ON_CLOSE | CreateOption.FILE_OPEN_REPARSE_POINT | CreateOption.FILE_NON_DIRECTORY_FILE | CreateOption.FILE_OPEN_FOR_BACKUP_INTENTdelete_ads_handle = nt_create_file_from_path(':' + _dropbox_attr_stream(name), self.fh.handle, access, winnt.FILE_ATTRIBUTE_NORMAL, disposition, create_options, sharing)win32file.CloseHandle(delete_ads_handle)else:
self.fs.remove(self._preserved_fname(name))try:
None(None, None)Nonewith None:
if not None:
try:
try:
Noneexcept IOError:
e = Noneif e.errno == errno.EINVAL:
raise create_io_error(errno.ENOENT, 'Preserved attributes not found', self._preserved_fname(name))raise e = Nonedel e)()
    reset = (lambda self: pass)()

