# Source Generated with Decompyle++
# File: updated_details.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Union
from constants import SyncType
from file_cache.types import ConflictType, PendingParentDetails
from dropbox.assertions import assert_
from dropbox.attrs import Attributes
from dropbox.shared.server_path import MRFilenameCaseServerPath, ServerPath
from dropbox.shared.validated_record import BaseString, Field, ValidatedRecord
from dropbox.sqlite3_helpers import FileCacheEntry as sqlite_FileCacheEntry
MYPY = False
if MYPY:
    from file_cache_entry import FileCacheEntry, MutableFileCacheEntry

class UpdatedDetails(ValidatedRecord):
    server_path = Field.required(MRFilenameCaseServerPath)
    sjid = Field.required(int)
    blocklist = Field.required(bytes)
    attrs = Field.required(Attributes)
    size = Field.required(int)
    dir = Field.required(bool)
    mtime = Field.required(int)
    sync_type = Field.required(SyncType)
    folder_policy = Field.optional(SyncType)
    force_reconstruct = Field.optional(bool)
    conflict_type = Field.optional(ConflictType)
    timestamp = Field.optional(int)
    user_id = Field.optional(int)
    host_id = Field.optional(int)
    fileid = Field.optional(BaseString)
    fileid_rev = Field.optional(int)
    local_blocklist = Field.optional(bytes)
    local_attrs = Field.optional(Attributes)
    
    def validate(self = None):
        if (self.local_blocklist is None) != (self.local_attrs is None):
            raise TypeError('UpdatedDetails requires either both or neither of local_blocklist and local_attrs defined.')

    get_from_db_ent = (lambda db_ent = None: pass# WARNING: Decompyle incomplete
)()
    deleted_details = (lambda server_path = None, sjid = None: UpdatedDetails(server_path = server_path, sjid = sjid, size = -1, blocklist = b'', mtime = -1, dir = 0, attrs = Attributes(), sync_type = SyncType.NORMAL))()
    create_from_synced_db_ent = (lambda db_ent = None: pass# WARNING: Decompyle incomplete
)()
    create_from_synced_parent = (lambda server_path = None, parent = None: UpdatedDetails(server_path = server_path, sjid = parent.sjid, blocklist = parent.blocklist, attrs = parent.attrs.copy(data_plats = frozenset()), size = parent.size, dir = parent.dir, mtime = parent.mtime, sync_type = parent.sync_type, timestamp = parent.timestamp, user_id = parent.user_id, host_id = parent.host_id, fileid = parent.fileid, fileid_rev = parent.fileid_rev, folder_policy = parent.folder_policy))()

