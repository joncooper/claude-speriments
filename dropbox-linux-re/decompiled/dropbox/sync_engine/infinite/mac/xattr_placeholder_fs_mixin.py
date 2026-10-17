# Source Generated with Decompyle++
# File: xattr_placeholder_fs_mixin.pyc (Python 3.11)

import os
import stat
from contextlib import contextmanager
from typing import ContextManager, Iterator, Optional, Text
from datatypes.infinite_details import PlaceholderKind
from file_system.indexing_attributes import IndexingAttributes
from file_system.util import convert_os_error
from abstract_placeholder_fs_mixin import PlaceholderFileSystemMixinInterface
from download.common import PlaceholderMovedError
from xattr_placeholder import XattrPlaceholder
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import make_decorated_exception_name
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.infinite import infinite_platform_supported
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.exceptions import NotAnInfinitePlaceholderError
from dropbox.infinite.util import report_infinite_event
from dropbox.shared.local_path import LocalPath
from dropbox.shared.placeholder_details import NucleusPlaceholderDetails, PlaceholderDetails
from dropbox.sync_engine_boundary.file_system_exceptions import AttrNotFoundError, FileNotFoundError, NotADirectoryError
from dropbox.sync_engine_boundary.infinite.mac.xattr_placeholder_context import XattrPlaceholderContext
from dropbox.sync_event.report import truncated_hash
if infinite_platform_supported():
    from macinfinite.common import DROPBOX_PLACEHOLDER_ATTR
    from macinfinite.xattr import fgetxattr, hasxattr

def XattrPlaceholderFileSystemMixin():
    '''XattrPlaceholderFileSystemMixin'''
    
    def create_infinite_placeholder(self = None, local_path = None, size = None, placeholder_details = ('local_path', 'LocalPath', 'size', 'int', 'placeholder_details', 'PlaceholderDetails', 'return', 'None')):
        MacOSXFileSystem = MacOSXFileSystem
        import file_system.macosx
    # WARNING: Decompyle incomplete

    
    def is_infinite_placeholder(self = None, local_path = None):
        
        try:
            convert_os_error()
            
            try:
                None(None, None)
                return 
                with None:
                    if not None, hasxattr(Text(local_path), DROPBOX_PLACEHOLDER_ATTR):
                        
                        try:
                            
                            try:
                                return None
                            except (FileNotFoundError, NotADirectoryError):
                                return False





    _read_placeholder_attr_at_path = (lambda path = None: try:
convert_os_error()fd = os.open(path, os.O_RDONLY)st = os.fstat(fd)if stat.S_ISDIR(st.st_mode):
raise NotAnInfinitePlaceholderErroros.close(fd)try:
None(None, None)os.close(fd)with None:
if not None:
try:
try:
None, bytes(fgetxattr(fd, DROPBOX_PLACEHOLDER_ATTR))Noneexcept AttrNotFoundError:
raise NotAnInfinitePlaceholderError)()
    
    def read_infinite_placeholder(self = None, local_path = None):
        return PlaceholderDetails.decode(self._read_placeholder_attr_at_path(local_path.to_unicode()))

    
    def read_nucleus_infinite_placeholder(self = None, local_path = None):
        return NucleusPlaceholderDetails.decode(self._read_placeholder_attr_at_path(local_path.to_unicode()))

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
        convert_os_error()
        st = os.stat(local_path.to_unicode())
        None(None, None)

    
    def validate_placeholder_on_platform(self = None, account = None, local_path = None, st = ('account', 'AccountInterface', 'local_path', 'LocalPath', 'st', 'IndexingAttributes', 'return', 'Optional[PlaceholderKind]')):
        path_str = local_path.to_unicode()
        path_hash = truncated_hash(path_str)
        size_on_disk = getattr(st, 'size_on_disk', None)
        size = getattr(st, 'size', -1)
        
        try:
            return XattrPlaceholder.get_placeholder_kind(path_str)
        except AttrNotFoundError:
            report_infinite_event(InfiniteEventType.INFINITE_HASHED_MISSING_COMPRESSION_XATTR, account = account, size_on_disk = size_on_disk, size = size, path_hash = path_hash)
        except Exception:
            e = None
            report_exception(severity = Severity.WARN, component = DesktopComponent.INFINITE)
            report_infinite_event(InfiniteEventType.INFINITE_ERRONEOUS_PLACEHOLDER_KIND, account = account, exception_name = make_decorated_exception_name(e))
            e = None
            del e
        except:
            e = None
            del e

        return PlaceholderKind.ERRONEOUS


XattrPlaceholderFileSystemMixin = <NODE:27>(XattrPlaceholderFileSystemMixin, 'XattrPlaceholderFileSystemMixin', PlaceholderFileSystemMixinInterface[(XattrPlaceholderContext, XattrPlaceholder)])
