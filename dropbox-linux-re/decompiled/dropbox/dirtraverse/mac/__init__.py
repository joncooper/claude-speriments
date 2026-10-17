# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional
from build_number.features import feature_enabled
from dropbox.dirtraverse.common import _DirectoryAbstract, _DirectoryEntryBase, Path
from dropbox.dirtraverse.posix import Directory as DirectoryPosix
from dropbox.mac.version import HIGH_SIERRA, MAC_VERSION, SIERRA
from dropbox.repr_utils import easy_repr

class DirectoryMacNotSupported(Exception):
    pass


class _DirectoryEntry(_DirectoryEntryBase):
    
    def __init__(self, name, type_, size = None, mtime = None, inode = None, ctime = ('name', 'Path', 'type_', 'Optional[str]', 'size', 'Optional[int]', 'mtime', 'float', 'inode', 'int', 'ctime', 'float', 'return', 'None')):
        self.name = name
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return easy_repr(self, 'name', 'type', 'size', 'mtime', 'inode', 'ctime')



def Directory(path = None, no_atime = None):
    
    try:
        if MAC_VERSION >= HIGH_SIERRA:
            _DirectoryMacHighSierra = _DirectoryMacHighSierra
            import high_sierra
            return _DirectoryMacHighSierra(path, no_atime = no_atime)
        if None == SIERRA and feature_enabled('getattrlistbulk-sierra'):
            _DirectoryMacHighSierra = _DirectoryMacHighSierra
            import high_sierra
            return _DirectoryMacHighSierra(path, no_atime = no_atime)
        _DirectoryMacLegacy = _DirectoryMacLegacy
        import legacy
        return _DirectoryMacLegacy(path, no_atime = no_atime)
    except DirectoryMacNotSupported:
        return 


