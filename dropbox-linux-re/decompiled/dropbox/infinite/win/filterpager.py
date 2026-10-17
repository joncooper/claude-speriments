# Source Generated with Decompyle++
# File: filterpager.pyc (Python 3.11)

import ctypes
import string
from typing import cast, Dict, Optional, Text
import pywintypes
import win32api
import win32event
import winerror
from pynt.constants import S_OK
from pynt.headers.WinBase import OVERLAPPED
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.exception.reporting import report_bad_assumption
from dropbox.fileutils import is_short_path
from dropbox.infinite.blacklist import InfiniteRecallBlacklist
from dropbox.infinite.pager import InfiniteRequest, PageFileRequest, Pager, PagerCommunicationError, PageResponse, PagerNotLoadedError
from dropbox.infinite.win.driver_manager import DriverManager
from dropbox.infinite.win.util import trace_recent_service_info
from dropbox.sync_engine_boundary.infinite.win.reparse_point_placeholder_context import ReparsePointPlaceholderContext
from dropbox.trace import TRACE
STATUS_SUCCESS = 0
STATUS_UNSUCCESSFUL = 0xC0000001
STATUS_IO_REPARSE_TAG_NOT_HANDLED = 0xC0000279
STATUS_PORT_DISCONNECTED = 0xC0000037
MAX_PATH = 260

def _format_frn(FileRefNum = None):
    first_qword = (lambda .0: pass# WARNING: Decompyle incomplete
)(FileRefNum[15:7:-1]())
    second_qword = (lambda .0: pass# WARNING: Decompyle incomplete
)(FileRefNum[7::-1]())
    return f'''{first_qword!s}:{second_qword!s}'''


class RequestMessage(ctypes.Structure):
    BYTE_ARRAY_TYPE = ctypes.c_ubyte * 16
    _fields_ = [
        ('ReplyLength', ctypes.c_ulong),
        ('MessageId', ctypes.c_ulonglong),
        ('PID', ctypes.c_ulong),
        ('VolumeId', BYTE_ARRAY_TYPE),
        ('FileRefNum', BYTE_ARRAY_TYPE),
        ('Index', ctypes.c_ulonglong),
        ('Path', ctypes.c_ubyte * ctypes.sizeof(ctypes.c_wchar) * 512),
        ('ProcessName', ctypes.c_ubyte * ctypes.sizeof(ctypes.c_wchar) * 512)]


class RequestMessage_v3(ctypes.Structure):
    BYTE_ARRAY_TYPE = ctypes.c_ubyte * 16
    _fields_ = [
        ('ReplyLength', ctypes.c_ulong),
        ('MessageId', ctypes.c_ulonglong),
        ('PID', ctypes.c_ulong),
        ('VolumeId', BYTE_ARRAY_TYPE),
        ('FileRefNum', BYTE_ARRAY_TYPE),
        ('Path', ctypes.c_ubyte * ctypes.sizeof(ctypes.c_wchar) * 512),
        ('ProcessName', ctypes.c_ubyte * ctypes.sizeof(ctypes.c_wchar) * 512)]


class ResponseMessage(ctypes.Structure):
    _fields_ = [
        ('Decision', ctypes.c_ulong),
        ('VolumeId', ctypes.c_ubyte * 16),
        ('FileRefNum', ctypes.c_ubyte * 16),
        ('Index', ctypes.c_ulonglong)]


class FilterPager(Pager):
    pass
# WARNING: Decompyle incomplete

