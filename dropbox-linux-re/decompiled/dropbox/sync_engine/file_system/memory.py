# Source Generated with Decompyle++
# File: memory.pyc (Python 3.11)

from __future__ import absolute_import
import collections
import contextlib
import errno
import functools
import os
import pprint
import time
from io import BytesIO
from typing import Any, BinaryIO, Dict, Optional, Set, Text, Tuple, Union
from six import iteritems
from infinite.memory.memory_placeholder_fs_mixin import MemoryPlaceholderFileSystemMixin
from infinite.memory.memory_stub_folder_fs_mixin import MemoryStubFolderFileSystemMixin
from abstract_attributes_handle import AbstractAttributesHandle, AbstractPlatformHandle, DEFAULT_PRESERVED_ATTRS_NAME
from abstract_file_system import AbstractFile, AbstractFileSystem
from constants import FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_SYMLINK, FILE_TYPE_REGULAR
from exceptions import AttrsModifiedError, create_directory_not_empty_error, create_file_exists_error, create_file_not_found_error, create_file_system_error, create_fs_invalid_argument_error, create_is_a_directory_error, create_not_a_directory_error, FileNotFoundError
from indexing_attributes import IndexingAttributes
from mount import AbstractMountFS
from util import IterableBasedDirectory
from dropbox.dirtraverse.common import DirectoryModifiedError
from dropbox.misc import protect_closed
from dropbox.shared.local_path import AbstractPosixPath, LocalPath
from dropbox.shared.util import db_lower
from dropbox.sync_engine_boundary.infinite.memory import MemoryFileOpenHandler
from dropbox.threading import Lock
_PRESERVED_PREFIX = '____preserved____'

def _preserved_key(name = None):
    return f'''{_PRESERVED_PREFIX!s}{name!s}'''


def _default_preserved_key():
    return _preserved_key(DEFAULT_PRESERVED_ATTRS_NAME)


def _wrap_memory_file_methods(fn):
    pass
# WARNING: Decompyle incomplete

_IndexingAttributes = IndexingAttributes

class _MemoryFile(AbstractFile):
    
    def __init__(self, name, mode = None, metadata = None, stringio = None, stringlock = ('name', 'Union[LocalPath, Text, str]', 'mode', 'str', 'metadata', 'Any', 'stringio', 'BinaryIO', 'stringlock', 'Any', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    flush = (lambda self: pass# WARNING: Decompyle incomplete
)()
    read = (lambda self: pass# WARNING: Decompyle incomplete
)()
    tell = (lambda self: pass# WARNING: Decompyle incomplete
)()
    truncate = (lambda self: pass# WARNING: Decompyle incomplete
)()
    write = (lambda self: pass# WARNING: Decompyle incomplete
)()
    closed = (lambda self: self.stringio is None)()
    name = (lambda self: self._name)()
    _preserve_offset = (lambda self: pass# WARNING: Decompyle incomplete
)()
    seek = (lambda self, offset, whence = (os.SEEK_SET,): if whence not in (os.SEEK_SET, os.SEEK_CUR, os.SEEK_END):
raise IOError(errno.EINVAL, os.strerror(errno.EINVAL))self.offset, self.whence = offset, whence)()
    
    def close(self):
        self.stringio = None

    sync = (lambda self: pass)()
    
    def __enter__(self = contextlib.contextmanager):
        return self

    
    def __exit__(self = _wrap_memory_file_methods, *n, **kw):
        self.close()



class _PlatHandle(AbstractPlatformHandle):
    
    def __init__(self, fs, platform, plat_dict, stringlock):
        self.fs = fs
        self.stringlock = stringlock
        self.plat_dict = plat_dict
        self.platform = platform
        self.reset()

    closed = (lambda self: self.plat_dict is None)()
    readattr = (lambda self: try:
self._next()except RuntimeError:
raise AttrsModifiedError()except StopIteration:
None)()
    reset = (lambda self: plat_dict_it = iter(self.plat_dict)self._next = plat_dict_it.__next__)()
    open = (lambda self = protect_closed, key = protect_closed, mode = protect_closed: self.stringlocksio = self.plat_dict[key])()
    
    def close(self):
        self.plat_dict = None



class _AttributesHandle(AbstractAttributesHandle):
    
    def __init__(self, fs, attrs_dict, stringlock, support_preserved_attrs):
        self.fs = fs
        self.attrs_dict = attrs_dict
        self.stringlock = stringlock
        self.support_preserved_attrs = support_preserved_attrs
        self.reset()

    closed = (lambda self: self.attrs_dict is None)()
    reset = (lambda self: attrs_dict_it = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.attrs_dict())
        self._next = attrs_dict_it.__next__
)()
    readplat = (lambda self: try:
self._next()except StopIteration:
None)()
    open = (lambda self, plat: if plat.startswith(_PRESERVED_PREFIX):
raise create_file_not_found_error(filename = plat)try:
plat_dict = self.attrs_dict[plat]except KeyError:
raise create_file_not_found_error(filename = plat)_PlatHandle(self.fs, plat, plat_dict, self.stringlock))()
    open_preserved = (lambda self = protect_closed, mode = protect_closed, name = protect_closed: key = _preserved_key(name)self.stringlocksio = self.attrs_dict[key])()
    remove = (lambda self, plat, key: self.stringlockplat_dict = self.attrs_dict[plat]del plat_dict[key])()
    remove_preserved = (lambda self, name = (DEFAULT_PRESERVED_ATTRS_NAME,): self.stringlockself.attrs_dict.pop(_preserved_key(name), None)None(None, None)Nonewith None:
if not None:
pass)()
    
    def close(self):
        self.attrs_dict = None



class _MemoryPath(AbstractPosixPath):
    SEPARATOR = '/'


class MemoryFS(AbstractFileSystem, AbstractMountFS, MemoryStubFolderFileSystemMixin, MemoryPlaceholderFileSystemMixin):
    pass
# WARNING: Decompyle incomplete

