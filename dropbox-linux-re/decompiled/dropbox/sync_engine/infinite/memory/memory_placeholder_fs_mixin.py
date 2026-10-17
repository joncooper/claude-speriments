# Source Generated with Decompyle++
# File: memory_placeholder_fs_mixin.pyc (Python 3.11)

from contextlib import contextmanager
from typing import ContextManager, Iterator, Optional
from datatypes.infinite_details import PlaceholderKind
from file_system.indexing_attributes import IndexingAttributes
from file_system.util import convert_os_error_dec
from abstract_placeholder_fs_mixin import PlaceholderFileSystemMixinInterface
from download.common import PlaceholderMovedError
from memory_placeholder import MemoryPlaceholder, MemoryPlaceholderContext
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import NucleusPlaceholderDetails, PlaceholderDetails
from dropbox.sync_engine_boundary.file_system_exceptions import FileNotFoundError

def MemoryPlaceholderFileSystemMixin():
    '''MemoryPlaceholderFileSystemMixin'''
    
    def create_infinite_placeholder(self = None, local_path = None, size = None, placeholder_details = ('local_path', 'LocalPath', 'size', 'int', 'placeholder_details', 'PlaceholderDetails', 'return', 'None')):
        f = self.open(local_path, 'a')
        f.seek(0)
        f.truncate()
        None(None, None)

    
    def is_infinite_placeholder(self = None, local_path = None):
        
        try:
            md = self._getmd(local_path)
        except FileNotFoundError:
            return False

        return getattr(md, 'infinite_details', None) is not None

    read_infinite_placeholder = (lambda self = None, local_path = None: placeholder = self._open_placeholder_by_path(local_path)None(None, None)with None:
if not None, placeholder.read():
pass)()
    
    def read_nucleus_infinite_placeholder(self = None, local_path = None):
        raise NotImplementedError('Reading Nucleus placeholders not yet supported on the memory platform.')

    open_placeholder_by_context = (lambda self = None, context = None, need_write_access = contextmanager: pass# WARNING: Decompyle incomplete
)()
    
    def verify_placeholder_at_path(self = None, placeholder = None, local_path = None):
        other_placeholder = self._open_placeholder_by_path(local_path)
        if placeholder.file_system_id() != other_placeholder.file_system_id():
            raise PlaceholderMovedError
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _open_placeholder_by_path(self = None, local_path = None):
        MemoryFS = MemoryFS
        import file_system.memory
    # WARNING: Decompyle incomplete

    
    def placeholder_context_by_path(self = None, local_path = None):
        MemoryFS = MemoryFS
        import file_system.memory
    # WARNING: Decompyle incomplete

    
    def validate_placeholder_on_platform(self = None, account = None, local_path = None, st = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'st', 'IndexingAttributes', 'return', 'Optional[PlaceholderKind]')):
        pass


MemoryPlaceholderFileSystemMixin = <NODE:27>(MemoryPlaceholderFileSystemMixin, 'MemoryPlaceholderFileSystemMixin', PlaceholderFileSystemMixinInterface[(MemoryPlaceholderContext, MemoryPlaceholder)])
