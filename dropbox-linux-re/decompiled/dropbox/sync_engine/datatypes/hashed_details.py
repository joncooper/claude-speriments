# Source Generated with Decompyle++
# File: hashed_details.pyc (Python 3.11)

from __future__ import absolute_import
import json
from typing import Any, Text
from build_number import is_test
from build_number.features import feature_enabled
from constants import DeletedFileStatus, SyncType
from infinite_details import InfiniteDetails
from symlink_details import SymlinkDetails
from dropbox.attrs import Attributes
from dropbox.exception.exception_decorators import handle_exceptions_ex_1
from dropbox.functions import EitherStr, make_bytes, make_unicode
from dropbox.shared.server_path import ServerPath
from dropbox.shared.validated_record import BaseString, Field, ValidatedRecord
from dropbox.trace import TRACE

class HashedDetailsWithoutPath(ValidatedRecord):
    blocklist = Field.optional(bytes)
    attrs = Field.optional(Attributes)
    size = Field.required(int)
    dir = Field.required(bool)
    mtime = Field.required(int)
    ctime = Field.required(int)
    sync_type = Field.required(SyncType)
    infinite_details = Field.optional(InfiniteDetails)
    folder_policy = Field.optional(SyncType)
    is_opened_stubfolder = Field.optional(bool, default = False)
    protected = Field.optional(bool, default = False)
    previous_entry_status = Field.optional(DeletedFileStatus)
    machineid_volumeid = Field.optional(int)
    machineid_inode = Field.optional(int)
    machineid_attr = Field.optional(BaseString)
    reassociate_flag = Field.optional(bool, default = False)
    symlink_details = Field.optional(SymlinkDetails)
    deleted_details = (lambda : HashedDetailsWithoutPath(blocklist = b'', attrs = Attributes(), size = -1, dir = 0, mtime = -1, ctime = -1, sync_type = SyncType.NORMAL, reassociate_flag = 0))()
    
    def validate(self = None):
        pass
    # WARNING: Decompyle incomplete



class HashedDetails(HashedDetailsWithoutPath):
    pass
# WARNING: Decompyle incomplete

