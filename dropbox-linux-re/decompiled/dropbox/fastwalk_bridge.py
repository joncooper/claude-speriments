# Source Generated with Decompyle++
# File: fastwalk_bridge.pyc (Python 3.11)

from __future__ import absolute_import
import functools
import os
from typing import Text
from dropbox.dirtraverse import _DirectoryEntryBase, Path
from dropbox.fastwalk import fastwalk as fastwalk_fs, fastwalk_strict as fastwalk_strict_fs, fastwalk_with_exception_handling as fastwalk_with_exception_handling_fs
from dropbox.platform import platform

class AugmentedDirent(_DirectoryEntryBase):
    
    def __init__(self, fs, path, dirent):
        self.fs = fs
        self.path = path
        self.dirent = dirent

    type = (lambda self = None: try:
self.dirent.typeexcept AttributeError:
)()
    name = (lambda self = None: self.dirent.name)()
    size = (lambda self: try:
self.dirent.sizeexcept AttributeError:
)()
    inode = (lambda self: if platform not in ('mac', 'linux'):
raise NotImplementedError('dirent.inode not supported on platform %r' % platform)self.dirent.inode)()
    win32_reparse_type = (lambda self: if platform != 'win':
raise NotImplementedError('dirent.win32_reparse_type not supported on platform %r' % platform)self.dirent.win32_reparse_type)()
    fullpath = (lambda self: Text(self.path.join(self.dirent.name)))()
    stat = (lambda self: try:
self._statexcept AttributeError:
self._stat = os.stat(self.fullpath))()
    lstat = (lambda self: try:
self._lstatexcept AttributeError:
self._lstat = os.lstat(self.fullpath))()


class MappedDirectory(object):
    
    def __init__(self, fn, inner):
        self.fn = fn
        self.inner = inner

    
    def __enter__(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __exit__(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def reset(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self):
        return self

    
    def readdir(self):
        ret = self.inner.readdir()
    # WARNING: Decompyle incomplete

    
    def __next__(self):
        return self.fn(next(self.inner))

    next = __next__


def fastwalk_bridge(fastwalk_func):
    pass
# WARNING: Decompyle incomplete

fastwalk = fastwalk_bridge(fastwalk_fs)
fastwalk_strict = fastwalk_bridge(fastwalk_strict_fs)
fastwalk_with_exception_handling = fastwalk_bridge(fastwalk_with_exception_handling_fs)
