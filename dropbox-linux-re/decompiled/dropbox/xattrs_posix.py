# Source Generated with Decompyle++
# File: xattrs_posix.pyc (Python 3.11)

from __future__ import absolute_import
import ctypes.util as ctypes
import errno
import os
import sys
from ctypes import c_char_p, c_int, c_size_t, c_ssize_t, c_uint32, c_void_p, CFUNCTYPE, create_string_buffer
from typing import Any, Dict, List, Optional, Text
from six import iteritems
from six.moves import range
from dropbox.exception.reporting import report_bad_assumption
from dropbox.functions import EitherStr, make_bytes, make_unicode
from dropbox.platform import IS_LINUX, IS_MAC
from dropbox.trace import TRACE

def _fs_to_unicode(name = None):
    return make_unicode(name, sys.getfilesystemencoding(), 'surrogateescape')


def _unicode_to_fs(name = None):
    return make_bytes(name, sys.getfilesystemencoding(), 'surrogateescape')

if IS_LINUX:
    _libc = ctypes.cdll.LoadLibrary('libc.so.6')
elif IS_MAC:
    _libc = ctypes.cdll.LoadLibrary('/usr/lib/libSystem.dylib')
else:
    _libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

def _errcheck(ret = None, func = None, args = None):
    if ret < 0:
        e = ctypes.get_errno()
        raise OSError(e, os.strerror(e))
    return ret

if sys.platform.startswith('linux'):
    c_calls = {
        'fgetxattr': (c_ssize_t, [
            c_int,
            c_char_p,
            c_void_p,
            c_size_t]),
        'fsetxattr': (c_int, [
            c_int,
            c_char_p,
            c_void_p,
            c_size_t,
            c_int]),
        'flistxattr': (c_ssize_t, [
            c_int,
            c_char_p,
            c_size_t]),
        'fremovexattr': (c_int, [
            c_int,
            c_char_p]) }
    errno.ENOATTR = errno.ENODATA
    ENOATTR_LIST = {
        errno.ENOATTR}
    XATTR_CREATE = 1
    XATTR_REPLACE = 2
elif sys.platform.startswith('darwin'):
    c_calls = {
        'fgetxattr': (c_ssize_t, [
            c_int,
            c_char_p,
            c_void_p,
            c_size_t,
            c_uint32,
            c_int]),
        'fsetxattr': (c_int, [
            c_int,
            c_char_p,
            c_void_p,
            c_size_t,
            c_uint32,
            c_int]),
        'flistxattr': (c_ssize_t, [
            c_int,
            c_char_p,
            c_size_t,
            c_int]),
        'fremovexattr': (c_int, [
            c_int,
            c_char_p,
            c_int]) }
    errno.ENOATTR = 93
    ENOATTR_LIST = {
        errno.ENOATTR,
        errno.EINVAL,
        errno.EPERM}
    XATTR_CREATE = 2
    XATTR_REPLACE = 4
else:
    MYPY = False
    if MYPY:
        c_calls = { }
        ENOATTR_LIST = { }
        XATTR_CREATE = 0
        XATTR_REPLACE = 0
    raise Exception('Xattrs not supported on this platform!')
XATTR_SHOWCOMPRESSION = 32
_func_types: 'Dict[str, CFUNCTYPE]' = { }
# WARNING: Decompyle incomplete
