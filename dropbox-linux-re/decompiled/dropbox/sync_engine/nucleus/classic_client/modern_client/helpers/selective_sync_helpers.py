# Source Generated with Decompyle++
# File: selective_sync_helpers.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import FrozenSet, Iterable, List, Mapping, Optional, Set
from transitional_utils.futures import parasitic_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.model.types import FileId
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.sync_engine_boundary.selective_sync_by_path_interface import FileIdRRServerPaths, SelectiveSyncByPathInterface
from dropbox.sync_engine_boundary.types.remote_props import FolderPolicyStatus, RemoteLocationProperties
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from modern_client import NucleusModernClient

class ModernSelectiveSyncManager(SelectiveSyncByPathInterface):
    
    def __init__(self = None, sync_engine = None):
        self._sync_engine = sync_engine

    
    def _get_fileid_path_dict(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_fileid_futures(self = None, paths = None):
        pass
    # WARNING: Decompyle incomplete

    
    def add_paths(self = None, paths = None):
        pass
    # WARNING: Decompyle incomplete

    
    def remove_paths(self = None, paths = None, infinitize_unignores = None):
        pass
    # WARNING: Decompyle incomplete

    
    def clear_user_hidden_paths(self = None, infinitize_unignores = None):
        self._sync_engine.change_fileid_hidden_set(set(), infinitize_unignores = infinitize_unignores)

    
    def get_set(self = None):
        return self._get_fileid_path_dict()

    
    def get_paths(self = None):
        complete = (lambda result = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(result.values()())
)()
        return self._get_fileid_path_dict().then(complete)

    
    def replace(self = None, new_fileids = None, infinitize_unignores = None):
        return self._sync_engine.change_fileid_hidden_set(new_fileids, infinitize_unignores)

    
    def is_path_hidden(self = None, path = None):
        pass
    # WARNING: Decompyle incomplete


