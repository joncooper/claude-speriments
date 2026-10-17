# Source Generated with Decompyle++
# File: linux_libc.pyc (Python 3.11)

from __future__ import absolute_import
import ctypes.util as ctypes
import os
import sys
from ctypes import c_char_p, c_int, c_long, c_uint32, c_void_p, CFUNCTYPE, POINTER
import six
from build_number import BUILD_KEY
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_bytes
_libc = ctypes.cdll.LoadLibrary('libc.so.6')
MAX_TRACE_LENGTH = 65536
sig_handler_t = CFUNCTYPE(c_int, c_int)
backtrace = _libc.backtrace
backtrace.restype = c_int
backtrace.argtypes = [
    c_void_p,
    c_int]
backtrace_symbols = _libc.backtrace_symbols
backtrace_symbols.restype = POINTER(c_char_p)
backtrace_symbols.argtypes = [
    c_void_p,
    c_int]
signal = _libc.signal
signal.restype = sig_handler_t
signal.argtypes = [
    c_int,
    sig_handler_t]
LOG_PID = 1
LOG_USER = 8
LOG_DAEMON = 24
openlog = _libc.openlog
openlog.argtypes = [
    c_char_p,
    c_int,
    c_int]
LOG_EMERG = 0
LOG_ALERT = 1
LOG_CRIT = 2
LOG_ERR = 3
LOG_WARNING = 4
LOG_NOTICE = 5
LOG_INFO = 6
LOG_DEBUG = 7
libc_syslog = _libc.syslog
libc_syslog.argtypes = [
    c_int,
    c_char_p,
    c_void_p]

def errcheck(ret, func, args):
    if ret < 0:
        e = ctypes.get_errno()
        raise OSError(e, os.strerror(e))
    return ret

func_dict = { }
# WARNING: Decompyle incomplete
