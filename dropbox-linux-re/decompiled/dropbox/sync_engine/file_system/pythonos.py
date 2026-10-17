# Source Generated with Decompyle++
# File: pythonos.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import os
import sys
import time
from typing import Callable, Text
from abstract_file_system import AbstractFile, AbstractFileSystem
from util import convert_errno_to_ioerror, convert_os_error_dec, mode_map
from dropbox.fileutils import is_case_insensitive_path
from dropbox.shared.local_path import LocalPath

class PythonFile(AbstractFile):
    
    def __init__(self, f):
        self.inner = f

    closed = (lambda self: self.inner.closed)()
    
    def close(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def flush(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def read(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def seek(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def tell(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def truncate(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def write(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def sync(self):
        self.flush()
        convert_errno_to_ioerror()
        os.fsync(self.inner.fileno())
        None(None, None)
        return None
        with None:
            if not None:
                pass



class FileSystem(AbstractFileSystem):
    FILE_CLASS = PythonFile
    
    def __init__(self = None, make_path = None):
        self._make_path = make_path

    
    def make_path(self = None, string_path = None):
        return self._make_path(string_path)

    
    def is_case_insensitive_directory(self = None, path = None):
        return is_case_insensitive_path(Text(path))

    mkdir = (lambda self, path: os.mkdir(Text(path)))()
    rmdir = (lambda self, path: os.rmdir(Text(path)))()
    open = (lambda self, path, mode = ('r',): if mode not in mode_map:
raise ValueError(f'''Opening file {path!r} with an invalid mode ({mode!r})''')self.FILE_CLASS(open(Text(path), mode = mode + 'b')))()
    
    def supported_attributes(self, path = (None,)):
        return ()

    
    def supports_extension(self, ext):
