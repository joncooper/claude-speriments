# Source Generated with Decompyle++
# File: xattr_util.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
from typing import Optional, Text
from abstract_attributes_handle import AbstractAttributesHandle, AbstractPlatformHandle, DEFAULT_PRESERVED_ATTRS_NAME
from exceptions import create_io_error
from util import convert_errno_to_ioerror, convert_os_error
from xattr_file import XAttrFile
from dropbox.functions import make_bytes
from dropbox.misc import protect_closed
from dropbox.shared.local_path import LocalPath
from dropbox.xattrs import xattr

class _PlatformHandle(AbstractPlatformHandle):
    
    def __init__(self = None, xattr = None, plat = None):
        convert_errno_to_ioerror()
        self.xattr = xattr.dup()
        None(None, None)

    name = (lambda self = None: self.platform)()
    reset = (lambda self = None: self.curiter = iter(self.xattr))()
    open = (lambda self = None, key = None, mode = protect_closed: convert_errno_to_ioerror()fd = os.dup(self.xattr.fileno())None(None, None)with None:
if not None, XAttrFile(fd, make_bytes(key), mode):
pass)()
    close = (lambda self = None: self.xattr.close())()
    closed = (lambda self = None: self.xattr.closed)()
    readattr = (lambda self = None: try:
next(self.curiter)except StopIteration:
None)()


class XAttrAttributesHandle(AbstractAttributesHandle):
    
    def __init__(self = None, path = None, plat = None, preserved_prefix = ('path', 'LocalPath', 'plat', 'str', 'preserved_prefix', 'str', 'return', 'None')):
        convert_os_error()
        self._xattr = xattr.from_path(Text(path))
        None(None, None)

    
    def _preserved_name(self = None, name = None):
        return f'''{self._preserved_prefix!s}.{name!s}'''

    
    def _default_preserved_name(self = None):
        return self._preserved_name(DEFAULT_PRESERVED_ATTRS_NAME)

    closed = (lambda self = None: self._xattr.closed)()
    reset = (lambda self = None: self.curiter = iter(self._supported_plats))()
    readplat = (lambda self = None: try:
next(self.curiter)except StopIteration:
None)()
    open = (lambda self = None, plat = None: if plat != self._supported_plats[0]:
raise create_io_error(errno.ENOENT, filename = plat)_PlatformHandle(self._xattr, plat))()
    open_preserved = (lambda self = None, mode = None, name = protect_closed: try:
convert_errno_to_ioerror()fd = os.dup(self._xattr.fileno())try:
None(None, None)with None:
if not None, XAttrFile(fd, make_bytes(self._preserved_name(name)), mode):
try:
try:
Noneexcept IOError:
if e.errno == errno.ENOTSUP:
raise IOError(errno.ENOENT, 'Preserved attributes not found')raise None = Nonedel e)()
    remove = (lambda self = None, plat = None, key = protect_closed: if plat != self._supported_plats[0]:
raise create_io_error(errno.ENOENT, filename = plat)convert_errno_to_ioerror()self._xattr.remove(key)None(None, None)Nonewith None:
if not None:
pass)()
    remove_preserved = (lambda self = None, name = None: try:
convert_errno_to_ioerror()del self._xattr[self._preserved_name(name)]try:
None(None, None)Nonewith None:
if not None:
try:
try:
Noneexcept KeyError:
Noneexcept IOError:
e = Noneif e.errno == errno.ENOTSUP:
passelse:
raise e = Nonedel eNonee = Nonedel e)()
    
    def close(self = None):
        self._xattr.close()



def path_supports_xattrs(path = None, test = None):
    x = xattr.from_path(Text(path))
    
    try:
        x[test]
    except KeyError:
        pass
    except OSError:
        e = None
        if e.errno == errno.ENOTSUP:
            e = None
            del e
            return False
        e = None
        del e

    return True

