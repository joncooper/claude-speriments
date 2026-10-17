# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import errno
import itertools
import os
import sys
from typing import Callable, cast, Iterator, List, Optional, Text
from dirtraverse_high_sierra_native import ffi, lib
from six.moves import range
from dropbox.dirtraverse.common import _DirectoryAbstract, _DirectoryEntryBase, DirectoryModifiedError, Path
from dropbox.dirtraverse.mac import _DirectoryEntry, DirectoryMacNotSupported
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_BLOCK_DEVICE, FILE_TYPE_POSIX_CHARACTER_DEVICE, FILE_TYPE_POSIX_FIFO, FILE_TYPE_POSIX_SOCKET, FILE_TYPE_POSIX_SYMLINK, FILE_TYPE_REGULAR
from dropbox.trace import TRACE
ATTR_BIT_MAP_COUNT = lib.ATTR_BIT_MAP_COUNT
ATTR_CMN_RETURNED_ATTRS = lib.ATTR_CMN_RETURNED_ATTRS
ATTR_CMN_CHGTIME = lib.ATTR_CMN_CHGTIME
ATTR_CMN_MODTIME = lib.ATTR_CMN_MODTIME
ATTR_CMN_NAME = lib.ATTR_CMN_NAME
ATTR_CMN_OBJTYPE = lib.ATTR_CMN_OBJTYPE
ATTR_CMN_FILEID = lib.ATTR_CMN_FILEID
ATTR_FILE_DATALENGTH = lib.ATTR_FILE_DATALENGTH
NAME_MAX = lib.NAME_MAX
_NATIVE_TO_LOGICAL = {
    lib.VFIFO: FILE_TYPE_POSIX_FIFO,
    lib.VSOCK: FILE_TYPE_POSIX_SOCKET,
    lib.VLNK: FILE_TYPE_POSIX_SYMLINK,
    lib.VCHR: FILE_TYPE_POSIX_CHARACTER_DEVICE,
    lib.VBLK: FILE_TYPE_POSIX_BLOCK_DEVICE,
    lib.VDIR: FILE_TYPE_DIRECTORY,
    lib.VREG: FILE_TYPE_REGULAR }

class AttributeMismatchError(Exception):
    pass
# WARNING: Decompyle incomplete


class ShortAttributeRead(Exception):
    pass


class _DirectoryMacHighSierra(_DirectoryAbstract):
    _ENTRIES_PER_CALL = 50
    _ATTR_CMN_NAME_SIZE = NAME_MAX * 3 + 1
    _MAX_BUF_SIZE = 1048576
    
    def __init__(self = None, path = None, no_atime = None):
        self._fd = os.open(cast(str, path), os.O_RDONLY | os.O_DIRECTORY)
        self.path = path
        self._is_unicode = isinstance(path, Text)
        self._attr_list = ffi.new('struct attrlist *')
        attr_list = ffi.new('struct attrlist *')
        attr_list.bitmapcount = ATTR_BIT_MAP_COUNT
        attr_list.commonattr = ATTR_CMN_NAME | ATTR_CMN_RETURNED_ATTRS | ATTR_CMN_OBJTYPE | ATTR_CMN_MODTIME | ATTR_CMN_CHGTIME | ATTR_CMN_FILEID
        attr_list.volattr = 0
        attr_list.dirattr = 0
        attr_list.fileattr = ATTR_FILE_DATALENGTH
        attr_list.forkattr = 0
        self._entry_size = ffi.sizeof('struct attrbuf_hdr') + ffi.sizeof('struct attrreference') + ffi.sizeof('fsobj_type_t') + ffi.sizeof('struct timespec') + ffi.sizeof('struct timespec') + ffi.sizeof('uint64_t') + ffi.sizeof('off_t') + self._ATTR_CMN_NAME_SIZE
        buf_size = self._entry_size * self._ENTRIES_PER_CALL
        self._raw_buf = ffi.new('uint8_t[]', buf_size)
        raw_buf = ffi.new('uint8_t[]', buf_size)
        allocated_size = ffi.sizeof(raw_buf)
        if allocated_size != buf_size:
            raise MemoryError('Requested %d bytes, only received %d' % (buf_size, allocated_size))
        self._options = 0
        self._finished = False
        self._errored = False
        self._init_state()

    
    def _init_state(self = None):
        gen = self._underlying_generator()
        
        try:
            primed_entry = next(gen)
            gen = itertools.chain([
                primed_entry], gen)
        except StopIteration:
            pass

        self._next = gen.__next__

    
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
    
    def _call_getattrlistbulk(self = None):
        num_entries = None
        num_entries = lib.getattrlistbulk(self._fd, self._attr_list, ffi.cast('void *', self._raw_buf), ffi.sizeof(self._raw_buf), self._options)
        if num_entries >= 0:
            pass
    # WARNING: Decompyle incomplete

    
    def _underlying_generator(self = None):
        pass
    # WARNING: Decompyle incomplete


