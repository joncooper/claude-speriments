# Source Generated with Decompyle++
# File: reparse_point_stub_folder_fs_mixin.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import sys
from typing import cast
import pywintypes
import win32file
import winerror
import winnt
from six import reraise
from file_system import windows_fileapi as fileapi
from file_system.windows_error import convert_pywin_error_fs_error_dec
from stub_folder_fs_mixin import StubFolderFileSystemMixinInterface
from reparse_point_utils import get_reparse_point_from_handle, set_reparse_point_from_handle, unset_reparse_point_from_handle
from dropbox.infinite.exceptions import NotAStubFolderError
from dropbox.shared.local_path import LocalPath, WindowsPath
from dropbox.shared.stub_folder_details import StubFolderDetails
from dropbox.sync_engine_boundary.client_lib.windows_path_util import nt_escape_and_convert_to_unicode
from dropbox.sync_engine_boundary.file_system_exceptions import create_file_not_found_error, create_not_a_directory_error, FileNotFoundError, PermissionDeniedError
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from pywintypes import HANDLEType

class ReparsePointStubFolderFileSystemMixinInterface(StubFolderFileSystemMixinInterface):
    
    def is_infinite_stub_folder(self = None, local_path = None):
        local_handle = None
    # WARNING: Decompyle incomplete

    set_stub_folder_by_path = (lambda self = None, local_path = None, stub_folder_details = convert_pywin_error_fs_error_dec: local_handle = None# WARNING: Decompyle incomplete
)()
    
    def unset_stub_folder_by_path(self = None, local_path = None):
        local_handle = None
    # WARNING: Decompyle incomplete

    read_stub_folder_by_path = (lambda self = None, local_path = None: handle = self._get_handle_for_stub_folder_at_path(local_path)data = get_reparse_point_from_handle(handle)# WARNING: Decompyle incomplete
)()
    _get_handle_for_stub_folder_at_path = (lambda local_path = None: unicode_path = nt_escape_and_convert_to_unicode(cast(WindowsPath, local_path))TRACE('Attempting to open %r as a stub folder (Read/Write Access)', unicode_path)try:
win32file.CreateFileW(unicode_path, winnt.FILE_READ_ATTRIBUTES | win32file.GENERIC_WRITE, win32file.FILE_SHARE_DELETE | win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE, None, win32file.OPEN_EXISTING, win32file.FILE_FLAG_OPEN_REPARSE_POINT | win32file.FILE_FLAG_BACKUP_SEMANTICS, None)except pywintypes.error:
error = Noneif error.winerror == winerror.ERROR_FILE_NOT_FOUND:
reraise(FileNotFoundError, create_file_not_found_error(filename = local_path.to_unicode()), sys.exc_info()[2])else:
raise error = Nonedel errorNoneerror = Nonedel error)()()

