# Source Generated with Decompyle++
# File: abstract_file_system.pyc (Python 3.11)

from __future__ import absolute_import
from contextlib import contextmanager
from typing import Any, BinaryIO, Optional, Text, Tuple, Union
import build_number
from fileid_utils import deserialize_fileid_and_rev, PERSISTED_FILEID_PRESERVED_NAME
from infinite.dummy_placeholder_fs_mixin import DummyPlaceholderFileSystemMixin
from abstract_attributes_handle import AbstractAttributesHandle
from dropbox.misc import LineReaderMixin
from dropbox.shared.local_path import LocalPath
from dropbox.shared.util import Closeable

class AbstractDirectory(Closeable):
    
    def readdir(self):
        raise NotImplementedError()

    
    def reset(self):
        raise NotImplementedError()

    
    def close(self):
        raise NotImplementedError()

    
    def __iter__(self):
        return self

    
    def __next__(self):
        return self.next()

    
    def next(self):
        toret = self.readdir()
    # WARNING: Decompyle incomplete



class AbstractFile(LineReaderMixin, Closeable):
    
    def close(self):
        raise NotImplementedError()

    closed = (lambda self: raise NotImplementedError())()
    
    def flush(self):
        raise NotImplementedError()

    
    def read(self, size = (None,)):
        raise NotImplementedError()

    
    def seek(self, offset, whence = (0,)):
        raise NotImplementedError()

    
    def sync(self):
        raise NotImplementedError()

    
    def tell(self):
        raise NotImplementedError()

    
    def truncate(self):
        raise NotImplementedError()

    
    def write(self, data):
        raise NotImplementedError()



class AbstractFileSystem(Closeable, DummyPlaceholderFileSystemMixin):
    version_array = (lambda cls = None: build_number.dropbox_version.version_tuple)()
    
    def indexing_attributes(self, path, resolve_link = (True,)):
        raise NotImplementedError()

    
    def make_path(self = None, string_path = None):
        raise NotImplementedError()

    
    def mkdir(self = None, path = None):
        raise NotImplementedError()

    
    def is_case_insensitive_directory(self = None, path = None):
        raise NotImplementedError()

    
    def open(self = None, path = None, mode = None, **kw):
        raise NotImplementedError()

    
    def open_attributes(self = None, path = None, **kw):
        raise NotImplementedError()

    
    def readlink(self = None, path = None):
        raise NotImplementedError()

    
    def opendir(self, path, **kw):
        raise NotImplementedError()

    
    def is_absolute_path(self = None, path = None):
        raise NotImplementedError()

    
    def realpath(self = None, path = None):
        raise NotImplementedError()

    
    def remove(self = None, path = None):
        raise NotImplementedError()

    
    def rename(self = None, src = None, dst = None, use_shell_fallback = (False,)):
        raise NotImplementedError()

    
    def rmdir(self = None, path = None):
        raise NotImplementedError()

    
    def is_normal_file(self = None, path = None):
        raise NotImplementedError()

    
    def is_symbolic_link(self = None, path = None):
        raise NotImplementedError()

    
    def resolve_symbolic_links(self = None, path = None):
        raise NotImplementedError()

    
    def remove_symbolic_link(self = None, path = None):
        raise NotImplementedError()

    
    def set_file_mtime(self = None, path = None, modification_time = None):
        raise NotImplementedError()

    
    def set_read_only(self = None, local_path = None, read_only = None):
        raise NotImplementedError()

    
    def get_disk_space_info(self = None, path = None):
        raise NotImplementedError()

    
    def supported_attributes(self = None, path = None):
        raise NotImplementedError()

    
    def supports_extension(self, ext_name):
        raise NotImplementedError()

    
    def is_read_only(self = None, local_path = None):
        raise NotImplementedError()

    
    def exclusive_delete_access(self, path):
        raise NotImplementedError()

    
    def sync_path(self = None, path = None):
        raise NotImplementedError()

    access_protection_info = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def get_protection_details(self, path, st = (None,)):
        pass

    
    def exchangedata(self = None, src = None, dest = contextmanager, temp_prefix = ('',)):
        raise NotImplementedError()

    
    def find_path_by_machineid(self = None, machineid_volumeid = None, machineid_inode = None):
        raise NotImplementedError()

    
    def get_symbolic_link_target(self = None, path = None):
        raise NotImplementedError()

    
    def get_fileid_and_rev_from_xattr(self = None, local_path = None):
        attrs_handle = self.open_attributes(local_path)
        persisted_fileid = attrs_handle.open_preserved('r', name = PERSISTED_FILEID_PRESERVED_NAME).read()
        None(None, None)
        return 
        with None:
            if not None, deserialize_fileid_and_rev(persisted_fileid):
                pass


