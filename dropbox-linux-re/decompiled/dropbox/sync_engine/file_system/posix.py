# Source Generated with Decompyle++
# File: posix.pyc (Python 3.11)

from __future__ import absolute_import
import os
from typing import Optional, Text
from posix_indexing_attributes_mixin import PosixIndexingAttributesMixin
from pythonos import FileSystem
from util import convert_os_error_dec
from dropbox import fsutil
from dropbox.shared.local_path import LocalPath
from dropbox.symlink_util import is_decodable
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_POSIX_SYMLINK

class PosixFileSystem(FileSystem, PosixIndexingAttributesMixin):
    pass
# WARNING: Decompyle incomplete

