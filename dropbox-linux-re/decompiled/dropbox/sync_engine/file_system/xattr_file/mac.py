# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
from ctypes import create_string_buffer
from typing import Optional
from abstract_file_system import AbstractFile
from constants import RESOURCE_FORK_XATTR
from util import CAN_READ, convert_errno_to_ioerror
from linux import XAttrFileLinux
from dropbox.xattrs import _fgetxattr_high
from dropbox.xattrs_posix import c_fgetxattr, ENOATTR_LIST

class XAttrFileMac(AbstractFile):
    
    def __init__(self = None, fd = None, item = None, mode = ('fd', 'int', 'item', 'bytes', 'mode', 'str', 'return', 'None')):
        self.fd = fd
        self.item = item
        self.can_read = CAN_READ[mode]
        self.linux_xattr = XAttrFileLinux(fd, item, mode)

    name = (lambda self = None: self.linux_xattr.name)()
    closed = (lambda self = None: self.linux_xattr.closed)()
    
    def write(self = None, data = None):
        self.linux_xattr.write(data)

    
    def seek(self = None, where = None, whence = None):
        self.linux_xattr.seek(where, whence)

    
    def tell(self = None):
        return self.linux_xattr.tell()

    
    def close(self = None):
        self.linux_xattr.close()

    
    def read(self = None, amt = None):
        pass
    # WARNING: Decompyle incomplete


