# Source Generated with Decompyle++
# File: macosx.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import fcntl
import os
import stat
import sys
from contextlib import contextmanager
from typing import Optional, Text
from Foundation import NSAutoreleasePool, NSString
from macffi.System import fsgetpath
from six import iteritems
from infinite.abstract_placeholder_fs_mixin import DEFAULT_MACOS_PLACEHOLDER_CONFIG, PlaceholderConfig
from infinite.mac.xattr_placeholder_fs_mixin import XattrPlaceholderFileSystemMixin
from infinite.mac.xattr_stub_folder_fs_mixin import XattrStubFolderFileSystemMixinInterface
from exceptions import FileNotFoundError, FileSystemError, PermissionDeniedError
from hfsplus_compare import hfsplus_casefold
from mac.volumeid_to_persistent_volumeid_map import VolumeIdToPersistentVolumeIdMap
from posix import PosixFileSystem
from pythonos import PythonFile
from util import convert_errno_to_ioerror, convert_os_error_dec, FileSystemDirectory
from xattr_util import path_supports_xattrs, XAttrAttributesHandle
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.fileutils import convert_mac_on_disk_path_to_nfd
from dropbox.infinite import infinite_platform_supported
from dropbox.mac.version import HIGH_SIERRA, MAC_VERSION
from dropbox.shared.local_path import LocalPath, MacOSXPath
from dropbox.sync_engine_boundary.file_system_exceptions import ExclusiveAccessException
from dropbox.trace import TRACE
if infinite_platform_supported():
    from macinfinite.common import installed_dropbox_kext_version_string

class MacOSXFile(PythonFile):
    
    def sync(self = None):
        self.flush()
        convert_errno_to_ioerror()
        fcntl.fcntl(self.inner.fileno(), fcntl.F_FULLFSYNC)
        None(None, None)
        return None
        with None:
            if not None:
                pass



class MacOSXFileSystem(PosixFileSystem, StubFolderMixin, PlaceholderMixin):
    pass
# WARNING: Decompyle incomplete

