# Source Generated with Decompyle++
# File: dummy_placeholder_fs_mixin.pyc (Python 3.11)

from contextlib import contextmanager
from typing import Any, ContextManager, Iterator, Optional
from datatypes.infinite_details import PlaceholderKind
from file_system.indexing_attributes import IndexingAttributes
from abstract_placeholder_fs_mixin import PlaceholderFileSystemMixinInterface
from constants import InfiniteFolderPolicy
from stub_folder_fs_mixin import StubFolderFileSystemMixinInterface
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import PlaceholderDetails
from dropbox.shared.stub_folder_details import StubFolderDetails

class DummyPlaceholderFileSystemMixin(StubFolderFileSystemMixinInterface, PlaceholderFileSystemMixinInterface):
    
    def create_infinite_placeholder(self = None, local_path = None, size = None, placeholder_details = ('local_path', 'LocalPath', 'size', 'int', 'placeholder_details', 'PlaceholderDetails', 'return', 'None')):
        raise NotImplementedError

    
    def is_infinite_placeholder(self = None, local_path = None):
        return False

    
    def read_infinite_placeholder(self = None, local_path = None):
        raise NotImplementedError

    open_placeholder_by_context = (lambda self = None, context = None, need_write_access = contextmanager: raise NotImplementedError)()
    
    def _open_placeholder_by_path(self = None, local_path = None):
        raise NotImplementedError

    
    def verify_placeholder_at_path(self = None, placeholder = None, local_path = None):
        raise NotImplementedError

    
    def placeholder_context_by_path(self = None, local_path = None):
        raise NotImplementedError

    
    def set_infinite_folder_policy(self = None, local_path = None, policy = None):
        raise NotImplementedError

    
    def get_infinite_folder_policy(self = None, local_path = None):
        raise NotImplementedError

    
    def is_infinite_stub_folder(self = None, local_path = None):
        raise NotImplementedError

    
    def set_stub_folder_by_path(self = None, local_path = None, stub_folder_details = None):
        raise NotImplementedError

    
    def unset_stub_folder_by_path(self = None, local_path = None):
        raise NotImplementedError

    
    def read_stub_folder_by_path(self = None, local_path = None):
        raise NotImplementedError

    
    def validate_placeholder_on_platform(self = None, account = None, local_path = None, st = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'st', 'IndexingAttributes', 'return', 'Optional[PlaceholderKind]')):
        raise NotImplementedError


