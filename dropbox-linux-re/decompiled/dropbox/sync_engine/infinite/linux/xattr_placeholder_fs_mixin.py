# Source Generated with Decompyle++
# File: xattr_placeholder_fs_mixin.pyc (Python 3.11)

import errno
import os
from contextlib import contextmanager
from typing import ContextManager, Iterator, Optional
from datatypes.infinite_details import PlaceholderKind
from file_system.indexing_attributes import IndexingAttributes
from file_system.util import convert_os_error
from abstract_placeholder_fs_mixin import PlaceholderFileSystemMixinInterface
from download.common import PlaceholderMovedError
from xattr_placeholder import XattrPlaceholder
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.infinite import infinite_platform_supported
from dropbox.infinite.exceptions import NotAnInfinitePlaceholderError
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import NucleusPlaceholderDetails, PlaceholderDetails
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError
from dropbox.sync_engine_boundary.infinite.linux.xattr_placeholder_context import XattrPlaceholderContext
if infinite_platform_supported():
    from lib.linuxinfinite.common import DROPBOX_PLACEHOLDER_ATTR
    from lib.linuxinfinite.xattr import fgetxattr, fhasxattr

def XattrPlaceholderFileSystemMixin():
    '''XattrPlaceholderFileSystemMixin'''
    
    def create_infinite_placeholder(self = None, local_path = None, size = None, placeholder_details = ('local_path', 'LocalPath', 'size', 'int', 'placeholder_details', 'PlaceholderDetails', 'return', 'None')):
        XattrPlaceholder.create(local_path, size, placeholder_details)

    
    def is_infinite_placeholder(self = None, local_path = None):
        
        try:
            convert_os_error()
            fd = os.open(local_path.to_unicode(), os.O_RDONLY)
            os.close(fd)
            
            try:
                None(None, None)
                return 
                os.close(fd)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                None, fhasxattr(fd, DROPBOX_PLACEHOLDER_ATTR)
                                return None
                            except FileNotFoundError:
                                return False





    
    def _read_placeholder_data(self = None, local_path = None):
        convert_os_error()
        fd = os.open(local_path.to_unicode(), os.O_RDONLY)
        os.close(fd)
        None(None, None)
        return 
        except OSError:
            if e.errno == errno.ENODATA or e.errno == 93:
                raise NotAnInfinitePlaceholderError
            raise e
            None = None
            del e
        os.close(fd)
        with None:
            if not None:
                pass

    
    def read_infinite_placeholder(self = None, local_path = None):
        return PlaceholderDetails.decode(self._read_placeholder_data(local_path))

    
    def read_nucleus_infinite_placeholder(self = None, local_path = None):
        return NucleusPlaceholderDetails.decode(self._read_placeholder_data(local_path))

    open_placeholder_by_context = (lambda self = None, context = None, need_write_access = contextmanager: pass# WARNING: Decompyle incomplete
)()
    
    def _open_placeholder_by_path(self = None, local_path = None):
        return self.open_placeholder_by_context(self.placeholder_context_by_path(local_path))

    
    def verify_placeholder_at_path(self = None, placeholder = None, local_path = None):
        other_placeholder = self._open_placeholder_by_path(local_path)
        if placeholder.file_system_id() != other_placeholder.file_system_id():
            raise PlaceholderMovedError
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def placeholder_context_by_path(self = None, local_path = None):
        return XattrPlaceholderContext(path = local_path.to_unicode())

    
    def validate_placeholder_on_platform(self = None, account = None, local_path = None, st = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'st', 'IndexingAttributes', 'return', 'Optional[PlaceholderKind]')):
        pass


XattrPlaceholderFileSystemMixin = <NODE:27>(XattrPlaceholderFileSystemMixin, 'XattrPlaceholderFileSystemMixin', PlaceholderFileSystemMixinInterface[(XattrPlaceholderContext, XattrPlaceholder)])
