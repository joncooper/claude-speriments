# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum, IntEnum, unique
from typing import List, Optional, Text
from dropbox.client.features.sync_error.contants import PERMISSION_DENIED_RESOLVER, PERMISSION_DENIED_RESOLVER_FOR_CBOS
MYPY = False
if MYPY:
    from dropbox.foundation.context.user import UserContext
    from dropbox.shared.local_path import LocalPath
    from dropbox.shared.server_path import MRCasedServerPath
SYNC_ERROR_LOG_PREFIX = '[Sync Errors]'
SYNC_ERROR_LOG_INTERVAL = 3600
SYNC_ERROR_LOG_INTERVAL_STORMCROW = 'desktop-sync-error-log-interval'
SYNC_ERROR_LOG_EVENT_NAME = 'sync_error_counts'
SyncErrorType = <NODE:12>()

class SyncStuckEvents(Enum):
    STUCK_ERROR_SEEN = 'stuck_error_seen'
    ERROR_SEEN = 'error_seen'
    OPEN_PROGRAMS = 'open_programs'
    VIEW_FILE_CLICK = 'view_file_click'
    LEARN_MORE_CLICK = 'learn_more_click'


class ResolveDetailsReturn(Enum):
    CANCELLED = 'cancelled'
    DONE = 'done'
    ERROR = 'error'
    PERMISSIONS_PENDING = 'permissions_pending'


class SyncErrorDetail:
    
    def __init__(self, error_id, local_path, file_id, server_path, fs_path, error_type, direction = None, is_directory = None, is_in_cbos = None, open_program_names = (False,), is_in_backup_instance = ('error_id', 'Text', 'local_path', 'LocalPath', 'file_id', 'Optional[bytes]', 'server_path', 'Optional[MRCasedServerPath]', 'fs_path', 'Text', 'error_type', 'SyncErrorType', 'direction', 'int', 'is_directory', 'bool', 'is_in_cbos', 'bool', 'open_program_names', 'Optional[List[str]]', 'is_in_backup_instance', 'bool', 'return', 'None')):
        self.error_id = error_id
        self.local_path = local_path
        self.file_id = file_id
        self.server_path = server_path
        self.fs_path = fs_path
        self.error_type = error_type
        self.direction = direction
        self.is_directory = is_directory
        self.is_in_cbos = is_in_cbos
        self.open_program_names = open_program_names
        self.is_in_backup_instance = is_in_backup_instance

    
    def __repr__(self = None):
        return 'error_id=[{}] local_path=[{}] server_path=[{}] fs_path=[{}] file_id=[{}error_type=[{}] direction=[{}] is_directory=[{}] open_program_names=[{}]'.format(self.error_id, self.local_path, self.server_path, self.fs_path, self.file_id, self.error_type, self.direction, self.is_directory, self.open_program_names)



def show_permissions_denied_resolver_flow(err = None, context = None):
    if err.is_in_backup_instance:
        return False
    if not None.is_in_cbos and context.stormcrow.allows(PERMISSION_DENIED_RESOLVER_FOR_CBOS):
        return False
    if None.error_type == SyncErrorType.PERMISSION_DENIED and context.stormcrow.allows(PERMISSION_DENIED_RESOLVER):
        return True

