# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import errno
import os
import sys
from typing import Callable, cast, Iterator, Optional, Text
from dirtraverse_mac_legacy_native import ffi, lib
from six.moves import range
from dropbox.dirtraverse.common import _DirectoryAbstract, _DirectoryEntryBase, DirectoryModifiedError, Path
from dropbox.dirtraverse.mac import _DirectoryEntry, DirectoryMacNotSupported
from dropbox.dirtraverse.posix import Directory as DirectoryPosix
from dropbox.repr_utils import easy_repr
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_BLOCK_DEVICE, FILE_TYPE_POSIX_CHARACTER_DEVICE, FILE_TYPE_POSIX_FIFO, FILE_TYPE_POSIX_SOCKET, FILE_TYPE_POSIX_SYMLINK, FILE_TYPE_REGULAR
ATTR_BIT_MAP_COUNT = lib.ATTR_BIT_MAP_COUNT
ATTR_CMN_CHGTIME = lib.ATTR_CMN_CHGTIME
ATTR_CMN_MODTIME = lib.ATTR_CMN_MODTIME
ATTR_CMN_NAME = lib.ATTR_CMN_NAME
ATTR_CMN_OBJID = lib.ATTR_CMN_OBJID
ATTR_CMN_OBJTYPE = lib.ATTR_CMN_OBJTYPE
ATTR_FILE_DATALENGTH = lib.ATTR_FILE_DATALENGTH
_NATIVE_TO_LOGICAL = {
    lib.VFIFO: FILE_TYPE_POSIX_FIFO,
    lib.VSOCK: FILE_TYPE_POSIX_SOCKET,
    lib.VLNK: FILE_TYPE_POSIX_SYMLINK,
    lib.VCHR: FILE_TYPE_POSIX_CHARACTER_DEVICE,
    lib.VBLK: FILE_TYPE_POSIX_BLOCK_DEVICE,
    lib.VDIR: FILE_TYPE_DIRECTORY,
    lib.VREG: FILE_TYPE_REGULAR }

class _DirectoryMacLegacy(_DirectoryAbstract):
    _ENTRIES_PER_CALL = 50
    _AVERAGE_FILE_NAME_SIZE = 256
    
    def __init__(self = None, path = None, no_atime = None):
        self._fd = os.open(cast(str, path), os.O_RDONLY | os.O_DIRECTORY)
        self.path = path
        self._is_unicode = isinstance(path, Text)
        self._attr_list = ffi.new('struct attrlist *')
        attr_list = ffi.new('struct attrlist *')
        attr_list.bitmapcount = ATTR_BIT_MAP_COUNT
        attr_list.commonattr = ATTR_CMN_NAME | ATTR_CMN_OBJTYPE | ATTR_CMN_OBJID | ATTR_CMN_MODTIME | ATTR_CMN_CHGTIME
        attr_list.volattr = 0
        attr_list.dirattr = 0
        attr_list.fileattr = ATTR_FILE_DATALENGTH
        attr_list.forkattr = 0
        buf_size = _DirectoryMacLegacy._ENTRIES_PER_CALL * (ffi.sizeof('struct _attrbuf') + _DirectoryMacLegacy._AVERAGE_FILE_NAME_SIZE)
        self._raw_buf = ffi.new('uint8_t[]', buf_size)
        raw_buf = ffi.new('uint8_t[]', buf_size)
        self._raw_buf_size = ffi.sizeof(raw_buf)
        self._base_ptr = ffi.new('uint32_t *')
        self._state_ptr = ffi.new('uint32_t *')
        self._count_ptr = ffi.new('uint32_t *')
        self._options = 0
        self._state_valid = False
        self._err = -1
        self._init_state()

    
    def _init_state(self = None):
        self._state_valid = False
        self._get_entries()
        self._next = self._underlying_generator().__next__

    
    def reset(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def readdir(self = None):
        
        try:
            return self.__next__()
        except StopIteration:
            return None


    
    def __next__(self = None):
        return self._next()

    next = __next__
    
    def _get_entries(self = None):
        old_state = self._state_ptr[0]
        self._count_ptr[0] = _DirectoryMacLegacy._ENTRIES_PER_CALL
        self._err = lib.getdirentriesattr(self._fd, self._attr_list, ffi.cast('void *', self._raw_buf), self._raw_buf_size, self._count_ptr, self._base_ptr, self._state_ptr, self._options)
        err = lib.getdirentriesattr(self._fd, self._attr_list, ffi.cast('void *', self._raw_buf), self._raw_buf_size, self._count_ptr, self._base_ptr, self._state_ptr, self._options)
        if err < 0:
            _errno = ffi.errno
            if _errno == errno.ENOTSUP:
                raise DirectoryMacNotSupported()
            raise OSError(_errno, os.strerror(_errno))
        if self._state_valid and old_state != self._state_ptr[0]:
            
            def _raise():
                raise DirectoryModifiedError()

            self._next = _raise
            _raise()
        self._state_valid = True

    
    def _underlying_generator(self = None):
        pass
    # WARNING: Decompyle incomplete


