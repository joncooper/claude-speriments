# Source Generated with Decompyle++
# File: mount.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import errno
import os
from abc import abstractmethod
from typing import Any, Callable, Text
from six import iteritems
from abstract_file_system import AbstractFileSystem
from exceptions import FileSystemError
from dropbox.fsutil import fsutil
from dropbox.shared.local_path import AbstractPosixPath, LocalPath

class _MountPath(AbstractPosixPath):
    SEPARATOR = '/'


class AbstractMountFS(AbstractFileSystem):
    root_path = (lambda self = None: pass)()


class MountFS(AbstractMountFS):
    
    def __init__(self, fs):
        self.fs = fs
        self.mounts = { }

    
    def initialize_volumeid_map(self, sync_engine):
        pass

    
    def set_placeholder_config(self, config):
        pass

    
    def supported_attributes(self, path = (None,)):
        return set()

    
    def make_path(self, *n, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def root_path(self, *n, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def _under_any_mount(self, path):
        pass
    # WARNING: Decompyle incomplete

    
    def _fs_rel(self, path, with_mp = (False,)):
        for k, fs in iteritems(self.mounts):
            if k == path or k.is_parent_of(path):
                newp = fsutil.reparent_path(k, fs.root_path(), path)
                if with_mp:
                    
                    return None, (fs, newp, k)
                
                return None, (None, newp)
            if with_mp:
                return (self.fs, path, None)
            return (None.fs, path)

    
    def mount_at(self, fs, path):
        if not fsutil.is_directory(self.fs, path):
            raise Exception('No directory to mount at!')
        if self._under_any_mount(path):
            raise Exception('Nested mounting is not supported!')
        if path in self.mounts:
            raise Exception('Something is already mounted at this path: %r' % path)
        self.mounts[path] = fs

    
    def rename(self, src, dst, use_shell_fallback = (False,)):
        if src in self.mounts or dst in self.mounts:
            raise FileSystemError(errno.EBUSY, os.strerror(errno.EBUSY))
        (fs1, path1) = self._fs_rel(src)
        (fs2, path2) = self._fs_rel(dst)
        if fs1 is fs2:
            print(fs1, path1, src)
            print(fs2, path2, dst)
            return fs1.rename(path1, path2)
        raise FileSystemError(errno.EXDEV, os.strerror(errno.ENOENT))

    
    def posix_symlink(self, symdata, path):
        (fs, path) = self._fs_rel(path)
        return fs.posix_symlink(symdata, path)

    
    def _create_wrapped_method(name = None, check = None):
        pass
    # WARNING: Decompyle incomplete

    mkdir = _create_wrapped_method('mkdir')
    set_file_mtime = _create_wrapped_method('set_file_mtime')
    set_read_only = _create_wrapped_method('set_read_only')
    open_attributes = _create_wrapped_method('open_attributes')
    rmdir = _create_wrapped_method('rmdir', check = True)
    opendir = _create_wrapped_method('opendir')
    open = _create_wrapped_method('open')
    remove = _create_wrapped_method('remove')
    posix_readlink = _create_wrapped_method('posix_readlink')
    posix_chmod = _create_wrapped_method('posix_chmod')
    is_case_insensitive_directory = _create_wrapped_method('is_case_insensitive_directory')
    sync_path = _create_wrapped_method('sync_path')
    is_infinite_placeholder = _create_wrapped_method('is_infinite_placeholder')
    read_infinite_placeholder = _create_wrapped_method('read_infinite_placeholder')
    create_infinite_placeholder = _create_wrapped_method('create_infinite_placeholder')
    
    def indexing_attributes(self, path, *n, **kw):
        (fs, path, mp) = self._fs_rel(path, with_mp = True)
    # WARNING: Decompyle incomplete

    
    def realpath(self, path):
        (fs, path, mp) = self._fs_rel(path, with_mp = True)
        rp = fs.realpath(path)
    # WARNING: Decompyle incomplete

    
    def supports_extension(self, ext):
        return ext == 'posix'

    
    def get_disk_space_info(self, path):
        return (0x100000000000, 0xA00000000000)


