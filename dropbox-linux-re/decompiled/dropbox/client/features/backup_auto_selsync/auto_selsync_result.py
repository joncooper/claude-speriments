# Source Generated with Decompyle++
# File: auto_selsync_result.pyc (Python 3.11)

from enum import auto, Enum
from typing import Optional, Set
from dropbox.model.types import FileId
from dropbox.repr_utils import easy_repr

class BackupAutoSelSyncResultCode(Enum):
    FEATURE_NOT_ENABLED = auto()
    NO_BACKUP_INSTANCE_FOUND = auto()
    NO_MOUNT_PATH_FOUND = auto()
    MOUNT_PATH_DOES_NOT_EXIST_LOCALLY = auto()
    NO_FILE_FOUND_TO_SELSYNC = auto()
    FAILED_TO_SELSYNC = auto()
    SUCCESS = auto()
    NO_TOP_LEVEL_FILE_OBJECTS_FOUND = auto()
    ALREADY_RUNNING = auto()
    
    def __repr__(self = None):
        return str(self)



class BackupAutoSelSyncResult:
    
    def __init__(self = None, auto_selsync_result_code = None, file_ids = None):
        self._auto_selsync_result_code = auto_selsync_result_code
        self._file_ids = file_ids

    
    def success(self = None):
        return self._auto_selsync_result_code == BackupAutoSelSyncResultCode.SUCCESS

    
    def __eq__(self = None, rhs = None):
