# Source Generated with Decompyle++
# File: accumulator.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from collections import OrderedDict
from typing import List, Optional, OrderedDict as OrderedDictType, Tuple
from dropbox.client.ui.sync_engine_ui.utils import get_time
from dropbox.model.types import FileId, UserId
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import SyncEventType

class SyncOperationBucketingAccumulator:
    MAX_DELAY_TIME = 600
    
    def __init__(self = None):
        self._user_id_to_files = OrderedDict()

    
    def is_empty(self = None):
        return len(self._user_id_to_files) == 0

    
    def put(self, user_id = None, last_fileid = None, last_local_path = None, operation = ('user_id', 'UserId', 'last_fileid', 'FileId', 'last_local_path', 'LocalPath', 'operation', 'SyncEventType', 'return', 'None')):
        if user_id not in self._user_id_to_files:
            self._user_id_to_files[user_id] = SyncOperationFileTracker()
        self._user_id_to_files[user_id].put(operation, last_fileid, last_local_path)
        self._user_id_to_files.move_to_end(user_id)

    
    def merge(self = None, other = None):
        for user_id, file_tracker in other._user_id_to_files.items():
            if user_id in self._user_id_to_files:
                self._user_id_to_files[user_id].merge(file_tracker)
                continue
            self._user_id_to_files[user_id] = file_tracker
            return None

    
    def pop_users(self = None, users = None):
        result = []
        for user_id in list(self._user_id_to_files.keys()):
            if user_id in users:
                result.append((user_id, self._user_id_to_files[user_id]))
                del self._user_id_to_files[user_id]
            return result

    
    def pop_users_before(self = None, time = None):
        result = []
        for user_id in list(self._user_id_to_files.keys()):
            file_tracker = self._user_id_to_files[user_id]
            if get_time() > file_tracker.first_event_time + self.MAX_DELAY_TIME or file_tracker.last_event_time < time:
                result.append((user_id, file_tracker))
                del self._user_id_to_files[user_id]
            return result

    
    def get_file_trackers(self = None):
        return list(self._user_id_to_files.values())

    
    def contains_any_users(self = None, uids = None):
        for uid in uids:
            if uid in self._user_id_to_files:
                return True
            return False

    
    def clear(self = None):
        self._user_id_to_files.clear()



class SyncOperationFileTracker:
    __slots__ = ('num_files_added', 'num_files_deleted', 'num_files_updated', 'last_fileid_changed', 'last_local_path_changed', 'first_event_time', 'last_event_time')
    
    def __init__(self = None):
        self.clear()

    
    def clear(self = None):
        self.num_files_added = 0
        self.num_files_deleted = 0
        self.num_files_updated = 0
        self.last_fileid_changed = None
        self.last_local_path_changed = None
        self.first_event_time = 0
        self.last_event_time = 0

    
    def get_total_changes(self = None):
        return self.num_files_added + self.num_files_deleted + self.num_files_updated

    
    def has_multiple_operations(self = None):
        return bool(self.num_files_added) + bool(self.num_files_deleted) + bool(self.num_files_updated) > 1

    
    def update_event_time(self = None):
        curr_time = get_time()
        if not self.first_event_time:
            self.first_event_time = curr_time
        self.last_event_time = curr_time

    
    def update_num_files(self = None, operation = None, count = None):
        if operation == SyncEventType.ADD:
            return None
        if None == SyncEventType.DELETE:
            return None
        if None == SyncEventType.EDIT:
            return None

    
    def put(self = None, operation = None, fileid = None, path = ('operation', 'SyncEventType', 'fileid', 'FileId', 'path', 'LocalPath', 'return', 'None')):
        self.update_event_time()
        self.update_num_files(operation, 1)
        self.last_fileid_changed = fileid
        self.last_local_path_changed = path

    
    def merge(self = None, other = None):
        if other.first_event_time < self.first_event_time:
            other.first_event_time = self, self.num_files_updated += other.num_files_updated, .num_files_updated
        if other.last_event_time > self.last_event_time:
            self.last_fileid_changed = other.last_fileid_changed
            self.last_local_path_changed = other.last_local_path_changed
            self.last_event_time = other.last_event_time
            return None
        return self, self.num_files_deleted += other.num_files_deleted, .num_files_deleted


