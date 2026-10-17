# Source Generated with Decompyle++
# File: posix.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
import sys
from typing import Optional, Text
from lib.posixffi.libc.api import closedir, fdopendir, ffi as ffi_libc, opendir, readdir_r, rewinddir
from common import _DirectoryAbstract, _DirectoryEntryBase, Path
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.repr_utils import easy_repr
from dropbox.stat_helper import stat_result_to_type
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_BLOCK_DEVICE, FILE_TYPE_POSIX_CHARACTER_DEVICE, FILE_TYPE_POSIX_FIFO, FILE_TYPE_POSIX_SOCKET, FILE_TYPE_POSIX_SYMLINK, FILE_TYPE_REGULAR, FILE_TYPE_UNKNOWN
_is_linux = sys.platform.startswith('linux')

class _DirectoryEntry(_DirectoryEntryBase):
    __slots__ = ('inode', 'name', 'type')
    
    def __init__(self = None, name = None, inode = None, _type = (None,)):
        self.name = name
        self.inode = inode
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return easy_repr(self, 'name', 'inode', 'type')


_native_to_logical = {
    1: FILE_TYPE_POSIX_FIFO,
    2: FILE_TYPE_POSIX_CHARACTER_DEVICE,
    4: FILE_TYPE_DIRECTORY,
    6: FILE_TYPE_POSIX_BLOCK_DEVICE,
    8: FILE_TYPE_REGULAR,
    10: FILE_TYPE_POSIX_SYMLINK,
    12: FILE_TYPE_POSIX_SOCKET }

class Directory(_DirectoryAbstract):
    __slots__ = ('dirp', '_entry_holder', '_result_holder', 'arg_is_unicode', 'path')
    
    def __init__(self = None, path = None, no_atime = None):
