# Source Generated with Decompyle++
# File: windows_fileapi.pyc (Python 3.11)

from __future__ import absolute_import, division
import time
import uuid
from ctypes import addressof, byref, c_ulong, create_unicode_buffer, memmove, POINTER, sizeof, string_at, Structure, windll
from ctypes.wintypes import FILETIME, HANDLE
from typing import Optional, Text, Union
import pywintypes
import win32api
import win32con
import winnt
from pynt.constants import ERROR_FILE_NOT_FOUND, ERROR_INVALID_FUNCTION, ERROR_INVALID_PARAMETER
from pynt.dlls.kernel32 import kernel32
from pynt.headers.windows import BY_HANDLE_FILE_INFORMATION, BYTE, DWORD, FILE_ATTRIBUTE_DIRECTORY, FILE_ATTRIBUTE_HIDDEN, FILE_ATTRIBUTE_NORMAL, FILE_ATTRIBUTE_NOT_CONTENT_INDEXED, FILE_ATTRIBUTE_REPARSE_POINT, FILE_ATTRIBUTE_SYSTEM, FILE_BASIC_INFORMATION, FILE_FLAG_BACKUP_SEMANTICS, FILE_FLAG_NO_BUFFERING, FILE_FLAG_OPEN_REPARSE_POINT, FILE_FLAG_WRITE_THROUGH, FILE_OBJECTID_BUFFER, FILE_RENAME_INFORMATION, FILE_SHARE_DELETE, FILE_SHARE_READ, FILE_SHARE_WRITE, FILE_STANDARD_INFO, FileBasicInformation, FileRenameInformation, FSCTL_CREATE_OR_GET_OBJECT_ID, FSCTL_GET_OBJECT_ID, GENERIC_READ, GENERIC_WRITE, INVALID_HANDLE_VALUE, IO_STATUS_BLOCK, MAX_PATH, MOVEFILE_REPLACE_EXISTING, OPEN_EXISTING, READ_CONTROL, REPLACEFILE_WRITE_THROUGH, VOLUME_NAME_NT, WRITE_DAC, WRITE_OWNER
from pynt.helpers.general import FormattedWindowsError, windows_error
from pynt.types import PSECURITY_DESCRIPTOR
from winffi.ntdll import CreateDisposition, CreateOption, nt_create_file_from_file_id as _nt_create_file_from_file_id, nt_create_file_from_path as _nt_create_file_from_path
from util import convert_os_error_dec
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import UnsupportedPlatformError
from dropbox.shared.local_path import WindowsPath
from dropbox.shared.util import Closeable
from dropbox.sync_engine_boundary.client_lib.windows_path_util import local_path_to_nt_prefix_unicode
from dropbox.win32.internal import get_volumes
CLOUD_REPARSE_TAGS = [
    0x9000001A,
    0x9000101A,
    0x9000201A,
    0x9000301A,
    0x9000401A,
    0x9000501A,
    0x9000601A,
    0x9000701A,
    0x9000801A,
    0x9000901A,
    0x9000A01A,
    0x9000B01A,
    0x9000C01A,
    0x9000D01A,
    0x9000E01A,
    0x9000F01A]
FileAttributeTagInfo = 9

class FILE_ATTRIBUTE_TAG_INFO(Structure):
    _fields_ = [
        ('FileAttributes', c_ulong),
        ('ReparseTag', c_ulong)]


def _python_to_c(ctype, str_):
    fit = min(len(str_), sizeof(ctype))
    memmove(addressof(ctype), str(str_), fit)


def _raise_error_from_status(status):
    err_str = win32api.FormatMessage(win32con.FORMAT_MESSAGE_FROM_HMODULE | win32con.FORMAT_MESSAGE_FROM_SYSTEM, windll.ntdll._handle, status, 0, None)
    win32_err = windll.ntdll.RtlNtStatusToDosError(status)
    raise FormattedWindowsError(win32_err, '[NTSTATUS %08X] %s' % (status, err_str))


class ObjectID(object):
    
    def __init__(self, bytes_):
        pass
    # WARNING: Decompyle incomplete

    generate_random = (lambda cls: cls(uuid.uuid4().bytes))()
    
    def to_hex(self):
        return str(self).encode('hex')

    
    def __eq__(self, other):
        return str(self) == str(other)

    
    def __ne__(self, other):
        return not (self == other)

    
    def __str__(self):
        return self._bytes

    
    def __repr__(self):
        return f'''ObjectID({str(self)!r})'''



class FileObjectID(object):
    
    def __init__(self, object_id, birth_volume_id, birth_object_id, domain_id):
        self.object_id = object_id
        self.birth_volume_id = birth_volume_id
        self.birth_object_id = birth_object_id
        self.domain_id = domain_id

    generate_random = (lambda cls: cls(ObjectID.generate_random(), ObjectID.generate_random(), ObjectID.generate_random(), ObjectID.generate_random()))()
    
    def __eq__(self, other):
