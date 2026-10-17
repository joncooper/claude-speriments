# Source Generated with Decompyle++
# File: posix_indexing_attributes_mixin.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import fcntl
import os
import stat
from os import open as _open
from typing import Text
from exceptions import create_infinite_kext_io_error
from indexing_attributes import IndexingAttributes
from util import convert_os_error_dec
from dropbox.exception.reporting import report_bad_assumption
from dropbox.functions import int64_cast
from dropbox.platform import IS_LINUX
from dropbox.stat_helper import stat_result_to_type
from dropbox.trace import TRACE
if IS_LINUX:
    from lib.linuxffi.sys.api import fstatvfs, statvfs
PLACEHOLDER_PROTECTED_BY_KEXT_ERRNO = 219

class RaceDetected(Exception):
    pass


class MachineGuidUnavailable(Exception):
    pass


def bitwise_or(flags):
    ret = 0
    for flag in flags:
        ret |= flag
        return ret


def st_equal(st1, st2):
    pass
# WARNING: Decompyle incomplete


class PosixIndexingAttributesMixin(object):
    indexing_attributes = (lambda self, path, resolve_link = (True,): resolve_link_or_callback = resolve_linkdel resolve_linkfd = None# WARNING: Decompyle incomplete
)()
    
    def indexing_attributes_from_fd(self, fd, symlink_stat, symlink_statvfs, symlink_target, path = (None, None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __volumeid_from_stat_result(self, st, st_vfs):
        if self.USE_STATVFS:
            return st_vfs.f_fsid & 0xFFFFFFFF
        return None.st_dev & 0xFFFFFFFF

    
    def __indexing_attributes_from_stat_result(self, st, st_vfs, **kwargs):
        _mode = st.st_mode
        _type = stat_result_to_type(st)
        kw = { }
        kw['mtime'] = st.st_mtime
        kw['size'] = st.st_size
        kw['size_on_disk'] = st.st_blocks * 512
        kw['ctime'] = st.st_ctime
        kw['volumeid'] = self.__volumeid_from_stat_result(st, st_vfs)
        kw['inode'] = int64_cast(st.st_ino)
        kw['machineid_attr'] = None
        kw['type'] = _type
        kw['posix_mode'] = _mode
        kw['posix_uid'] = st.st_uid
        kw['posix_gid'] = st.st_gid
        kw['posix_nlink'] = st.st_nlink
        kw['is_read_only'] = self.stat_is_read_only(st = st)
        kw['has_stable_inodes'] = True
        kw.update(kwargs)
    # WARNING: Decompyle incomplete

    
    def __stat_symlink_and_open_path(self, path, resolve_link_or_callback):
        symlink_stat = None
        symlink_statvfs = None
        symlink_target = None
        if callable(resolve_link_or_callback):
            resolving_link = None
        else:
            resolving_link = bool(resolve_link_or_callback)
        flags = set((os.O_RDONLY, os.O_NOCTTY, os.O_NOFOLLOW, os.O_NONBLOCK))
        if self.HAS_O_NOATIME:
            flags.add(os.O_NOATIME)
        fd = None
    # WARNING: Decompyle incomplete

    
    def __indexing_attributes_without_fd(self, path, resolving_link, symlink_stat, symlink_statvfs, symlink_target):
        pass
    # WARNING: Decompyle incomplete

    is_read_only = (lambda self, local_path: self.stat_is_read_only(os.lstat(Text(local_path))))()

