# Source Generated with Decompyle++
# File: pending_details.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, cast, Optional, Tuple
from build_number.features import feature_enabled
from constants import DeletedFileStatus, SyncType
from file_cache.types import ExtraPendingDetails
from infinite_details import InfiniteDetails
from symlink_details import SymlinkDetails
from dropbox.attrs import Attributes
from dropbox.shared.server_path import MRFilenameCaseServerPath, ServerPath
from dropbox.shared.validated_record import BaseString, Field, ValidatedRecord

class PendingDetails(ValidatedRecord):
    server_path = Field.required(MRFilenameCaseServerPath)
    blocklist = Field.optional(bytes)
    parent_blocklist = Field.optional(bytes)
    attrs = Field.optional(Attributes)
    parent_attrs = Field.optional(Attributes)
    size = Field.required(int)
    dir = Field.required(bool)
    mtime = Field.required(int)
    ctime = Field.required(int)
    mount_request = cast(Optional[Tuple[(int, int)]], Field.optional(tuple))
    machineid_volumeid = Field.optional(int)
    machineid_inode = Field.optional(int)
    machineid_attr = Field.optional(BaseString)
    fileid = Field.optional(BaseString)
    parent_fileid = Field.optional(BaseString)
    fileid_rev = Field.optional(int)
    parent_fileid_rev = Field.optional(int)
    local_fileid_parent_fileid = Field.optional(BaseString)
    local_fileid_parent_fileid_rev = Field.optional(int)
    local_fileid_parent_fileid_type = Field.optional(int)
    sync_type = Field.required(SyncType)
    infinite_details = Field.optional(InfiniteDetails)
    folder_policy = Field.optional(SyncType)
    reassociate_flag = Field.required(bool)
    previous_entry_status = Field.optional(DeletedFileStatus)
    parent_machineid_volumeid = Field.optional(int)
    parent_machineid_inode = Field.optional(int)
    parent_machineid_attr = Field.optional(BaseString)
    symlink_details = Field.optional(SymlinkDetails)
    
    def validate(self = None):
        if self.reassociate_flag not in (0, 1):
            raise TypeError('Invalid value for reassociate_flag: %d' % self.reassociate_flag)
        if self.dir not in (0, 1):
            raise TypeError('Invalid value for dir: %d' % self.dir)
    # WARNING: Decompyle incomplete

    get_from_db_ent = (lambda file_cache = None, db_ent = None: sp = ServerPath(db_ent['parent_path'], lowered = True).join(db_ent['local_filename'])# WARNING: Decompyle incomplete
)()

