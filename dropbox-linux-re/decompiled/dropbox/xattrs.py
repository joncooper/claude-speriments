# Source Generated with Decompyle++
# File: xattrs.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import fcntl
import os
from ctypes import c_char_p, create_string_buffer
from typing import Callable, Iterator, MutableMapping, Optional, Text, Type, TypeVar
from six.moves import range
from dropbox.misc import protect_closed
from dropbox.shared.error_util import convert_errno_to_ioerror
from dropbox.xattrs_posix import c_fgetxattr, ENOATTR_LIST, fgetxattr, flistxattr, fremovexattr, fsetxattr

def _fgetxattr_high(callable = None):
    for i in range(100):
        size = callable(None, 0)
        p = create_string_buffer(size)
        ret = callable(p, size)
        toret = p.raw
        if len(toret) == ret:
            
            return None, toret
        
        return None, None[:ret]
        except OSError:
            if e.errno == errno.ERANGE:
                None = None
                del e
                continue
            raise 
            e = None
            del e
        raise OSError(errno.ERANGE, os.strerror(errno.ERANGE))


def _fgetxattr_high_linux(fd = None, item = None):
    pass
# WARNING: Decompyle incomplete

T = TypeVar('T', bound = 'xattr')

def xattr():
    '''xattr'''
    
    def __init__(self = None, fd = None):
        self.fd = fd

    from_path = (lambda cls = None, path = None: try:
if not hasattr(os, 'O_NOATIME'):
raise OSError(errno.EPERM, 'this platform does no support O_NOATIME')fd = os.open(path, os.O_RDONLY | os.O_NOCTTY | os.O_NONBLOCK | os.O_NOATIME)except OSError:
e = Noneif e.errno == errno.EPERM:
fd = os.open(path, os.O_RDONLY | os.O_NOCTTY | os.O_NONBLOCK)else:
raise e = Nonedel eexcept:
e = Nonedel efcntl.fcntl(fd, fcntl.F_SETFL, fcntl.fcntl(fd, fcntl.F_GETFL) & ~(os.O_NONBLOCK))cls(fd))()
    fileno = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def dup(self = None):
        return type(self)(os.dup(self.fileno()))

    __getitem__ = (lambda self = None, item = None: pass# WARNING: Decompyle incomplete
)()
    __setitem__ = (lambda self = None, item = None, value = protect_closed: pass# WARNING: Decompyle incomplete
)()
    __delitem__ = (lambda self = None, item = None: try:
self.remove(item)Noneexcept OSError:
e = Noneif e.errno in ENOATTR_LIST:
raise KeyError(item)raise e = Nonedel e)()
    __len__ = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    __iter__ = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    remove = (lambda self = None, item = None: pass# WARNING: Decompyle incomplete
)()
    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    closed = (lambda self = None: self.fd is None)()
    
    def __del__(self = None):
        self.close()


xattr = <NODE:27>(xattr, 'xattr', MutableMapping[(str, bytes)])

def _fgetxattr_high_linux_str(fd = None, item = None):
    
    try:
        convert_errno_to_ioerror()
        
        try:
            None(None, None)
            return 
            with None:
                if not None, _fgetxattr_high_linux(fd, item):
                    
                    try:
                        
                        try:
                            return None
                        except IOError:
                            if e.errno in ENOATTR_LIST:
                                None = None
                                del e
                                return b''
                            e = None
                            del e





