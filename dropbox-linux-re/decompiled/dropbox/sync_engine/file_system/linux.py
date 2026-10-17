# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import fcntl
import os
import stat
import sys
from typing import Text
from infinite.linux.xattr_placeholder_fs_mixin import XattrPlaceholderFileSystemMixin
from posix import PosixFileSystem
from pythonos import PythonFile
from util import convert_os_error, convert_os_error_dec, FileSystemDirectory, mode_string_to_flags
from xattr_util import path_supports_xattrs, XAttrAttributesHandle
from dropbox import fsutil
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.infinite import infinite_platform_supported
from dropbox.linux_libc import POSIX_FADV_SEQUENTIAL, posix_fadvise
from dropbox.shared.local_path import LinuxPath
from dropbox.trace import TRACE
CURRENT_UMASK = os.umask(63)
os.umask(CURRENT_UMASK)

class LinuxFile(PythonFile):
    pass


class FileSystem(PosixFileSystem, PlaceholderMixin):
    pass
# WARNING: Decompyle incomplete

