# Source Generated with Decompyle++
# File: selsync.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Dict, FrozenSet, Iterable, List, Mapping, Optional, Set, Text
from six import iteritems
from transitional_utils.futures import parasitic_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.model.types import FileId
from dropbox.shared.server_path import RRCasedServerPath, RRLowerServerPath
from dropbox.sync_engine_boundary.selsync import FileIdSet, SelectiveSyncInterface, SelectiveSyncSet
from dropbox.sync_engine_boundary.types.remote_props import FolderPolicyStatus, RemoteLocationProperties
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from sync_engine import NucleusClassicClient

class NucleusSelectiveSyncManager(SelectiveSyncInterface):
    
    def __init__(self = None, sync_engine = None):
        self._sync_engine = sync_engine

    
    def add_paths(self = None, paths = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_fileid_futures(self = None, paths = None):
        fileids_fut = []
        for path in paths:
            fileids_fut.append(self._sync_engine.rr_server_to_fileid(RRCasedServerPath(path)))
            return Future.all_list(fileids_fut)

    
    def remove_paths(self = None, paths = None, infinitize_unignores = None):
        pass
    # WARNING: Decompyle incomplete

    
    def clear_user_hidden_paths(self = None, infinitize_unignores = None):
        self._sync_engine.change_fileid_hidden_set(set(), infinitize_unignores = infinitize_unignores)

    
    def _get_fileid_path_dict(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_paths(self = None):
        paths = []
        for _, path in self._get_fileid_path_dict().items():
            if path:
                paths.append(RRCasedServerPath(path))
            return frozenset(paths)

    
    def get_set(self = None):
        fileids_and_paths = self._get_fileid_path_dict()
        return frozenset(fileids_and_paths)(fileids = (lambda .0: pass# WARNING: Decompyle incomplete
), known_paths = iteritems(fileids_and_paths)())

    
    def replace(self = None, new_set = None, infinitize_unignores = None, lite = (False, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def is_path_hidden(self = None, path = None):
        pass
    # WARNING: Decompyle incomplete


