# Source Generated with Decompyle++
# File: paths.pyc (Python 3.11)

from __future__ import annotations
import unicodedata
from typing import Any, cast, NewType, Optional, Text
from unicodedata import normalize
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRLowerServerPath, MRUnknownCaseServerPath, RRCasedServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
NormalizedLocalPath = NewType('NormalizedLocalPath', LocalPath)

def normalize_local_path(lp = None):
    return NormalizedLocalPath(lp.to_nfc().db_lower())


class FSPath:
    __slots__ = ('_lp',)
    
    def __init__(self = None, converter = None, local_path = None, *, _normalize):
        if _normalize:
            self._lp = converter.normalize_within_dropbox(local_path)
            return None
        self._lp = None

    _from_local_path_without_normalizing = (lambda local_path = None: FSPath(cast(PathConverter, None), local_path, _normalize = False))()
    from_absolute_path_text = (lambda converter = None, path_text = None: FSPath(converter, converter.make_local_path(path_text)))()
    
    def to_text(self = None):
        return self._lp.to_unicode()

    
    def to_normalized_local_path(self = None):
        return normalize_local_path(self._lp)

    local_path = (lambda self: self._lp)()
    is_system_root = (lambda self = None: self._lp.is_root)()
    basename = (lambda self = None: self._lp.basename)()
    parent = (lambda self = None: FSPath._from_local_path_without_normalizing(self._lp.dirname) if not self._lp.is_root else None)()
    
    def join(self = None, converter = None, *components):
        pass
    # WARNING: Decompyle incomplete

    
    def is_ancestor_of(self = None, other = None):
        return self._lp.db_lower().is_parent_of(other._lp.db_lower())

    
    def is_equal_to_or_descendant_of(self = None, other = None):
        if not self._lp == other._lp:
            pass
        return other._lp.is_parent_of(self._lp)

    
    def __eq__(self = None, other = None):
