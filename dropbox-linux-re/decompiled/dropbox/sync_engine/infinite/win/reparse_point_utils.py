# Source Generated with Decompyle++
# File: reparse_point_utils.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from ctypes import c_ubyte, c_ulong, c_ulonglong, c_ushort, sizeof, Structure
from typing import Optional, Text
import pywintypes
import win32file
import winerror
import winioctlcon
from pynt.constants import ERROR_ONLY_IF_CONNECTED
from file_system import windows_fileapi as fileapi
from dropbox.exception.reporting import report_bad_assumption
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from pywintypes import HANDLEType
REPARSE_TAG = 68
REPARSE_GUID_STR = b'\x16\x0f\xbb\xc5\xe9hVD\xb6\xb9_^\xe5\xf8\x99e'
# WARNING: Decompyle incomplete
