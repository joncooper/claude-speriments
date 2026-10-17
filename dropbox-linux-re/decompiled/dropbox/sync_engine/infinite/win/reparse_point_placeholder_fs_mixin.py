# Source Generated with Decompyle++
# File: reparse_point_placeholder_fs_mixin.pyc (Python 3.11)

from __future__ import annotations
import sys
from contextlib import contextmanager
from typing import cast, ContextManager, Iterator, Optional, TYPE_CHECKING
import pywintypes
import win32file
import winerror
import winnt
if TYPE_CHECKING:
    from pywintypes import HANDLEType
from six import reraise
from datatypes.infinite_details import PlaceholderKind
from file_system import windows_fileapi as fileapi
from file_system.indexing_attributes import IndexingAttributes
from file_system.windows_error import convert_pywin_error_fs_error_dec
from abstract_placeholder_fs_mixin import PlaceholderFileSystemMixinInterface
from download.common import PlaceholderMovedError
from reparse_point_placeholder import ReparsePointPlaceholder
from reparse_point_utils import read_file_system_id_from_handle
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.infinite.exceptions import NotAnInfinitePlaceholderError
from dropbox.shared.local_path import LocalPath, WindowsPath
from dropbox.shared.placeholder_details import NucleusPlaceholderDetails, PlaceholderDetails
from dropbox.sync_engine_boundary.client_lib.windows_path_util import nt_escape_and_convert_to_unicode
from dropbox.sync_engine_boundary.file_system_exceptions import create_file_not_found_error, FileNotFoundError, FSInvalidArgumentError
from dropbox.sync_engine_boundary.infinite.win.reparse_point_placeholder_context import ReparsePointPlaceholderContext

def ReparsePointPlaceholderFileSystemMixin():
    '''ReparsePointPlaceholderFileSystemMixin'''
    _open_placeholder_for_read = (lambda local_path = None: unicode_path = nt_escape_and_convert_to_unicode(cast(WindowsPath, local_path))try:
win32file.CreateFileW(unicode_path, winnt.FILE_READ_ATTRIBUTES, win32file.FILE_SHARE_DELETE | win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE, None, win32file.OPEN_EXISTING, win32file.FILE_FLAG_OPEN_REPARSE_POINT, None)except pywintypes.error:
error = Noneif error.winerror == winerror.ERROR_ACCESS_DENIED:
reraise(NotAnInfinitePlaceholderError, NotAnInfinitePlaceholderError(), sys.exc_info()[2])elif error.winerror == winerror.ERROR_FILE_NOT_FOUND:
reraise(FileNotFoundError, create_file_not_found_error(filename = local_path.to_unicode()), sys.exc_info()[2])else:
raise error = Nonedel errorNoneerror = Nonedel errorNoneerror = Nonedel error)()()
    
    def create_infinite_placeholder(self = None, local_path = None, size = None, placeholder_details = ('local_path', 'LocalPath', 'size', 'int', 'placeholder_details', 'PlaceholderDetails', 'return', 'None')):
        ReparsePointPlaceholder.create(cast(WindowsPath, local_path), size, placeholder_details)

    
    def is_infinite_placeholder(self = None, local_path = None):
        local_handle = None
    # WARNING: Decompyle incomplete

    
    def _read_placeholder_reparse_point_at_path(self = None, local_path = None):
        local_handle = None
    # WARNING: Decompyle incomplete

    
    def read_infinite_placeholder(self = None, local_path = None):
        return PlaceholderDetails.decode(self._read_placeholder_reparse_point_at_path(local_path))

    
    def read_nucleus_infinite_placeholder(self = None, local_path = None):
        return NucleusPlaceholderDetails.decode(self._read_placeholder_reparse_point_at_path(local_path))

    open_placeholder_by_context = (lambda self = None, context = None, need_write_access = contextmanager: pass# WARNING: Decompyle incomplete
)()
    
    def _open_placeholder_by_path(self = None, local_path = None):
        return ReparsePointPlaceholder.open_from_context(self.placeholder_context_by_path(local_path))

    
    def verify_placeholder_at_path(self = None, placeholder = None, local_path = None):
        local_handle = None
    # WARNING: Decompyle incomplete

    
    def placeholder_context_by_path(self = None, local_path = None):
        local_handle = None
    # WARNING: Decompyle incomplete

    
    def validate_placeholder_on_platform(self = None, account = None, local_path = None, st = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'st', 'IndexingAttributes', 'return', 'Optional[PlaceholderKind]')):
        pass


ReparsePointPlaceholderFileSystemMixin = <NODE:27>(ReparsePointPlaceholderFileSystemMixin, 'ReparsePointPlaceholderFileSystemMixin', PlaceholderFileSystemMixinInterface[(ReparsePointPlaceholderContext, ReparsePointPlaceholder)])
