# Source Generated with Decompyle++
# File: selective_sync_by_path_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import ABC, abstractmethod
from typing import Dict, FrozenSet, Iterable, Optional
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.shared.server_path import RRCasedServerPath
FileIdRRServerPaths = Dict[(FileId, Optional[RRCasedServerPath])]

class SelectiveSyncByPathInterface(ABC):
    add_paths = (lambda self = None, paths = None: raise NotImplementedError())()
    remove_paths = (lambda self = None, paths = None, infinitize_unignores = abstractmethod: raise NotImplementedError())()
    clear_user_hidden_paths = (lambda self = None, infinitize_unignores = None: raise NotImplementedError())()
    get_set = (lambda self = None: raise NotImplementedError())()
    get_paths = (lambda self = None: raise NotImplementedError())()
    replace = (lambda self = None, new_set = None, infinitize_unignores = abstractmethod: raise NotImplementedError())()
    is_path_hidden = (lambda self = None, path = None: raise NotImplementedError())()

