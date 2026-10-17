# Source Generated with Decompyle++
# File: abstract_placeholder_fs_mixin.pyc (Python 3.11)

from abc import abstractmethod
from contextlib import contextmanager
from typing import ContextManager, Generic, Iterator, NamedTuple, Optional, TypeVar
from build_number.features import feature_enabled
from datatypes.infinite_details import PlaceholderKind
from file_system.indexing_attributes import IndexingAttributes
from abstract_placeholder import AbstractPlaceholder
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.exception.reporting import report_bad_assumption
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.util import report_infinite_event
from dropbox.platform import IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import NucleusPlaceholderDetails, PlaceholderDetails
from dropbox.sync_engine_boundary.infinite.placeholder_context import PlaceholderContext
from dropbox.sync_event.report import truncated_hash
PlaceholderContextT = TypeVar('PlaceholderContextT', bound = PlaceholderContext)
PlaceholderT = TypeVar('PlaceholderT', bound = AbstractPlaceholder)

class DuplicatePlaceholderOpenError(Exception):
    pass

PlaceholderConfig = NamedTuple('PlaceholderConfig', [
    ('mac_support_sparse_files', bool)])
DEFAULT_MACOS_PLACEHOLDER_CONFIG = PlaceholderConfig(False)

def PlaceholderFileSystemMixinInterface():
    '''PlaceholderFileSystemMixinInterface'''
    create_infinite_placeholder = (lambda self = None, local_path = None, size = abstractmethod, placeholder_details = ('local_path', 'LocalPath', 'size', 'int', 'placeholder_details', 'PlaceholderDetails', 'return', 'None'): pass)()
    is_infinite_placeholder = (lambda self = None, local_path = None: pass)()
    read_infinite_placeholder = (lambda self = None, local_path = None: pass)()
    
    def read_nucleus_infinite_placeholder(self = None, local_path = None):
        pass

    open_placeholder_by_context = (lambda self = None, context = None, need_write_access = contextmanager: pass)()
    _open_placeholder_by_path = (lambda self = None, local_path = None: pass)()
    verify_placeholder_at_path = (lambda self = None, placeholder = None, local_path = abstractmethod: pass)()
    placeholder_context_by_path = (lambda self = None, local_path = None: pass)()
    
    def validate_placeholder(self = None, account = None, local_path = None, st = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'st', 'IndexingAttributes', 'return', 'Optional[PlaceholderKind]')):
        pass
    # WARNING: Decompyle incomplete

    validate_placeholder_on_platform = (lambda self = None, account = None, local_path = abstractmethod, st = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'st', 'IndexingAttributes', 'return', 'Optional[PlaceholderKind]'): pass)()
    
    def supports_mac_sparse_files(self = None):
        return False


PlaceholderFileSystemMixinInterface = <NODE:27>(PlaceholderFileSystemMixinInterface, 'PlaceholderFileSystemMixinInterface', Generic[(PlaceholderContextT, PlaceholderT)])
