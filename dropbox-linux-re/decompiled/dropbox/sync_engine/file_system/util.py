# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import functools
import os
from typing import Any, Callable, Optional
from abstract_file_system import AbstractDirectory, AbstractFile
from constants import SEEK_CUR, SEEK_END, SEEK_SET
from exceptions import create_file_system_error
from indexing_attributes import IndexingAttributes
from dropbox.dirtraverse import Directory
from dropbox.misc import protect_closed
from dropbox.platform import IS_WINDOWS
from dropbox.shared.error_util import convert_errno_to_ioerror, convert_error
from dropbox.shared.util import RuntimeMixin
if IS_WINDOWS:
    from pynt.headers.WinError import ERROR_FILE_NOT_FOUND, ERROR_FILENAME_EXCED_RANGE, ERROR_PATH_NOT_FOUND
    from pywintypes import error as PyWinError
else:
    ERROR_FILENAME_EXCED_RANGE = None
    ERROR_FILE_NOT_FOUND = None
    ERROR_PATH_NOT_FOUND = None
    PyWinError = None

def convert_os_error():
    
    def handle_exc(e):
        err = None
        filename = None
    # WARNING: Decompyle incomplete

    return convert_error(handle_exc)


def convert_os_error_dec(f = None):
    pass
# WARNING: Decompyle incomplete


class FileSystemDirectory(AbstractDirectory):
    __init__ = (lambda self, path: pass# WARNING: Decompyle incomplete
)()
    
    def readdir(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def reset(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete



class IterableBasedDirectory(AbstractDirectory):
    
    def __init__(self, get_entries):
        self.get_entries = get_entries
        self.reset()

    
    def reset(self):
        self.curiter = iter(self.get_entries())

    
    def close(self):
        pass

    
    def readdir(self):
        
        try:
            return next(self.curiter)
        except StopIteration:
            return None



CAN_READ = {
    'r': True,
    'r+': True,
    'w': False,
    'w+': True,
    'a': False,
    'a+': True }
CAN_WRITE = {
    'r': False,
    'r+': True,
    'w': True,
    'w+': True,
    'a': True,
    'a+': True }
mode_map = {
    'r': os.O_RDONLY,
    'r+': os.O_RDWR,
    'w': os.O_WRONLY | os.O_TRUNC | os.O_CREAT,
    'w+': os.O_RDWR | os.O_TRUNC | os.O_CREAT,
    'a': os.O_WRONLY | os.O_APPEND | os.O_CREAT,
    'a+': os.O_RDWR | os.O_APPEND | os.O_CREAT }

def mode_string_to_flags(mode):
    return mode_map[mode]


class FunctionBasedFile(AbstractFile):
    
    def __init__(self, name = None, mode = None, read_function = None, write_function = ('name', 'str', 'mode', 'str', 'read_function', 'Callable[[], bytes]', 'write_function', 'Callable[[bytes], None]', 'return', 'None')):
        self._name = name
        self.mode = mode
        self.read_all = read_function
        self.write_all = write_function
        self._closed = False
        if 'w' in mode:
            self.eof_offset = 0
        else:
            all_data = self.read_all()
            self.eof_offset = len(all_data) if all_data else 0
        self.file_pointer_offset = 0

    
    def close(self = None):
        self._closed = True

    closed = (lambda self = None: self._closed)()
    name = (lambda self = None: self._name)()
    flush = (lambda self = None: pass)()
    read = (lambda self = None, size = None: all_data = self.read_all()# WARNING: Decompyle incomplete
)()
    seek = (lambda self = None, offset = None, whence = protect_closed: if whence == SEEK_CUR:
Noneif None == SEEK_END:
self.eof_offset + offset = NoneNoneif None == SEEK_SET:
self.file_pointer_offset = offsetNoneraise IOError(errno.EINVAL, os.strerror(errno.EINVAL)))()
    sync = (lambda self = None: pass)()
    tell = (lambda self = None: self.file_pointer_offset)()
    truncate = (lambda self = None: all_data = self.read_all()all_data = all_data[:self.file_pointer_offset]all_data = all_data + b'\x00' * (self.file_pointer_offset - len(all_data))self.write_all(all_data))()
    write = (lambda self = None, data = None: all_data = self.read_all()new_offset = self.file_pointer_offset + len(data)if new_offset >= self.eof_offset:
new_data = all_data[:self.file_pointer_offset] + dataself.eof_offset = new_offsetelse:
new_data = all_data[:self.file_pointer_offset] + data + all_data[new_offset:]self.write_all(new_data)self.file_pointer_offset = new_offset)()


class WrappedFileSystem(RuntimeMixin):
    fs = (lambda self: self.inner)()

