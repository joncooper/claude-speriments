# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
from typing import Optional
from abstract_file_system import AbstractFile
from constants import RESOURCE_FORK_XATTR
from util import CAN_READ, CAN_WRITE, convert_errno_to_ioerror
from dropbox.misc import protect_closed
from dropbox.xattrs import _fgetxattr_high_linux, _fgetxattr_high_linux_str
from dropbox.xattrs_posix import ENOATTR_LIST, fremovexattr, fsetxattr
ENOATTR = 93

class XAttrFileLinux(AbstractFile):
    
    def __init__(self = None, fd = None, item = None, mode = ('fd', 'int', 'item', 'bytes', 'mode', 'str', 'return', 'None')):
        
        try:
            if mode[-1] == 'b':
                mode = mode[:-1]
            self.fd = None
            self.can_read = CAN_READ[mode]
            self.can_write = CAN_WRITE[mode]
            self.item = item
            self.offset = 0
            if mode[0] == 'a':
                raise NotImplementedError()
            if mode[0] == 'r':
                
                try:
                    _fgetxattr_high_linux(fd, item)
                    
                    try:
                        pass
                    except OSError:
                        e = None
                        if e.errno in ENOATTR_LIST:
                            raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), item)
                        raise 
                        e = None
                        del e

                    
                    try:
                        if mode[0] == 'w' and self.item == RESOURCE_FORK_XATTR.encode('utf-8'):
                            
                            try:
                                fremovexattr(fd, self.item)
                                
                                try:
                                    pass
                                except OSError:
                                    e = None
                                    if e.errno != ENOATTR:
                                        raise 
                                    
                                    try:
                                        e = None
                                        del e
                                    e = None
                                    del e
                                    try:
                                        pass
                                    except Exception:
                                        os.close(fd)
                                        raise 

                                    self.fd = fd
                                    return None






    read = (lambda self = None, amt = None: if not self.can_read:
raise IOError(errno.EBADF, os.strerror(errno.EBADF))# WARNING: Decompyle incomplete
)()
    tell = (lambda self = None: self.offset)()
    write = (lambda self = None, data = None: pass# WARNING: Decompyle incomplete
)()
    seek = (lambda self = None, where = None, whence = protect_closed: if whence == os.SEEK_END:
self.read()Noneif None == os.SEEK_SET:
where = NoneNoneraise NotImplementedError())()
    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    name = (lambda self = None: self.item)()
    closed = (lambda self = None: self.fd is None)()
    
    def __del__(self = None):
        self.close()


