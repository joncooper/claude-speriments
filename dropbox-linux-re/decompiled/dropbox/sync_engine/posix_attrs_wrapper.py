# Source Generated with Decompyle++
# File: posix_attrs_wrapper.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import itertools
import os
import stat
import sys
from typing import Any, List, Optional, Union
from file_system.abstract_attributes_handle import AbstractAttributesHandle, AbstractPlatformHandle
from file_system.abstract_file_system import AbstractFile
from file_system.constants import SEEK_CUR, SEEK_END, SEEK_SET
from file_system.util import WrappedFileSystem
from dropbox import fsutil
from dropbox.misc import protect_closed
from dropbox.shared.local_path import LocalPath
from dropbox.trace import WARNING
MYPY = False
FileSystem = Any
_POSIX_ATTR_PLAT = 'posix'
_EXECUTABLE_ATTR_KEY = 'executable'

def posix_file_is_executable(fs = None, path = None):
