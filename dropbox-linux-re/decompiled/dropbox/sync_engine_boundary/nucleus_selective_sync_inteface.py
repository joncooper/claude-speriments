# Source Generated with Decompyle++
# File: nucleus_selective_sync_inteface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Set
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId

class NucleusSelectiveSyncInterface(ABC):
    get_fileid_hidden_set = (lambda self = None: raise NotImplementedError())()
    change_fileid_hidden_set = (lambda self = None, new_fileid_hidden_set = None, infinitize_unignores = abstractmethod: raise NotImplementedError())()
    hidden_set_add = (lambda self = None, fileids = None: raise NotImplementedError())()
    hidden_set_remove = (lambda self = None, fileids = None, infinitize_unignores = abstractmethod: raise NotImplementedError())()

