# Source Generated with Decompyle++
# File: synced_callback_details.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from constants import SyncPolicy
from dropbox.attrs import Attributes
from dropbox.shared.server_path import ServerPath
from dropbox.shared.validated_record import BaseString, Field, ValidatedRecord

class SyncedCallbackDetails(ValidatedRecord):
    server_path = Field.required(ServerPath)
    ctime = Field.optional(int)
    user_id = Field.optional(int)
    host_id = Field.optional(int)
    fileid = Field.optional(BaseString)
    blocklist = Field.required(bytes)
    attrs = Field.required(Attributes)
    size = Field.required(int)
    dir = Field.required(bool)
    sync_policy = Field.required(SyncPolicy)
    timestamp = Field.optional(int)
    is_edit = Field.required(bool)
    is_delete = Field.required(bool)
    is_sync_policy_change = Field.required(bool)
    is_local_change = Field.required(bool)
    is_cloud_content = Field.required(bool)

