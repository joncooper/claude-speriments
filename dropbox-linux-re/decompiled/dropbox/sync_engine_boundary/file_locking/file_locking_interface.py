# Source Generated with Decompyle++
# File: file_locking_interface.pyc (Python 3.11)

from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.file_locking.file_locking_boundary_cache import FileLockingBoundaryCache
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockResponse, FileLockStatus
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface

class FileLockingInterface:
    
    def __init__(self = None, nucleus_interface = None):
        self._file_locking = FileLockingBoundaryCache(nucleus_interface)

    
    def get_file_lock_status(self = None, fileid = None):
        return self._file_locking.get_lock_status(fileid)

    
    def override_file_lock_status(self = None, fileid = None, se_state = None):
        return self._file_locking.override_file_lock_status(fileid, se_state)

    
    def lock_file(self = None, fileid = None, conn = None):
        return self._file_locking.lock(fileid, conn)

    
    def unlock_file(self = None, fileid = None, conn = None):
        return self._file_locking.unlock(fileid, conn)

    
    def request_unlock_file(self = None, fileid = None, conn = None):
        return self._file_locking.request_unlock(fileid, conn)


