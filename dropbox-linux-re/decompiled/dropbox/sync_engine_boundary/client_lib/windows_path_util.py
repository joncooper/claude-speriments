# Source Generated with Decompyle++
# File: windows_path_util.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Text, Union
from dropbox.assertions import assert_
from dropbox.shared.local_path import WindowsPath
WIN32_PATH_PREFIX = '\\\\?\\'
WIN32_SHARED_PATH_PREFIX = '\\\\?\\UNC\\'
WINNT_PATH_PREFIX = '\\??\\'
UNC_PATH_PREFIX = '\\\\'

def is_escaped_nt_path(path = None):
    return Text(path).startswith(WIN32_PATH_PREFIX)


def is_drive_path(path = None):
