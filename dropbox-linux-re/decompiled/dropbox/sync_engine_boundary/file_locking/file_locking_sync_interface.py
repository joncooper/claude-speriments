# Source Generated with Decompyle++
# File: file_locking_sync_interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from dropbox.foundation.futures import Future
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockStatus

class SyncEngineFileLockingInterface(ABC):
    lookup_lock_state = (lambda self = None, fileid = None: raise NotImplementedError())()

