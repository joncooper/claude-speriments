# Source Generated with Decompyle++
# File: xattr_placeholder.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import contextlib
import errno
import os
import sys
from typing import BinaryIO, cast, Iterator, Text
from lib.linuxffi.sys.api import fstatvfs
from lib.posixffi.libc.api import set_file_mtime
from file_system.util import convert_os_error, convert_os_error_dec
from abstract_placeholder import AbstractPlaceholder, SimpleStat
from dropbox.functions import int64_cast
from dropbox.infinite import infinite_platform_supported
from dropbox.infinite.exceptions import NotAnInfinitePlaceholderError
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import PlaceholderDetails
from dropbox.sync_engine_boundary.infinite.linux.xattr_placeholder_context import XattrPlaceholderContext
from dropbox.threading import Lock
if infinite_platform_supported():
    from lib.linuxinfinite.common import DROPBOX_PLACEHOLDER_ATTR, posix_fallocate
    from lib.linuxinfinite.xattr import fgetxattr, fhasxattr, fremovexattr, fsetxattr
MYPY = False

class XattrPlaceholder(AbstractPlaceholder):
    
    def __init__(self = None, file_obj = None, context = None):
        self._file_obj = file_obj
        self.context = context
        self._lock = Lock()

    open_from_context = (lambda context = None, need_write_access = staticmethod: pass# WARNING: Decompyle incomplete
)()()
    create = (lambda local_path = None, size = staticmethod, placeholder_details = convert_os_error_dec: unicode_path = local_path.to_unicode()fd = None# WARNING: Decompyle incomplete
)()()
    
    def read(self = None):
        contents = fgetxattr(self._file_obj.fileno(), DROPBOX_PLACEHOLDER_ATTR)
        return PlaceholderDetails.decode(contents)

    prepare_for_write = (lambda self = None, size = None: self._lock.acquire()try:
posix_fallocate(self._file_obj.fileno(), 0, size)self._file_obj.seek(0)self._lock.release()except:
self._lock.release()self._file_obj.flush())()
    
    def write(self = None, data = None, offset = None):
        self._lock.acquire()
        
        try:
            self._file_obj.seek(offset)
            self._file_obj.write(data)
            self._lock.release()
        except:
            self._lock.release()

        self._file_obj.flush()

    read_data = (lambda self = None, offset = None, length = convert_os_error_dec: self._lock.acquire()try:
self._file_obj.seek(offset)self._lock.release()self._file_obj.read(length)except:
self._lock.release())()
    
    def unset(self = None):
        convert_os_error()
        fremovexattr(self._file_obj.fileno(), DROPBOX_PLACEHOLDER_ATTR)

    
    def reset(self = None, size = None):
        self._file_obj.truncate(0)
        self._file_obj.truncate(size)

    
    def is_placeholder(self = None):
        return fhasxattr(self._file_obj.fileno(), DROPBOX_PLACEHOLDER_ATTR)

    
    def file_system_id(self = None):
        st = os.fstat(self._file_obj.fileno())
        return '<%d, %d>' % (st.st_dev, st.st_ino)

    
    def resolve_path(self = None):
        raise NotImplementedError

    
    def set_file_mtime(self = None, mtime = None):
        set_file_mtime(self._file_obj.fileno(), mtime)

    
    def simple_stat(self = None):
        st = os.fstat(self._file_obj.fileno())
        st_vfs = fstatvfs(self._file_obj.fileno())
        return SimpleStat(volumeid = st_vfs.f_fsid & 0xFFFFFFFF, inode = int64_cast(st.st_ino), mtime = int(st.st_mtime), size = st.st_size)


