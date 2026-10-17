# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

from __future__ import absolute_import
import json
from enum import IntEnum
from typing import Any, Dict, NamedTuple, Optional, Text
from six import iteritems
from build_number.features import feature_enabled
from constants import DeletedFileStatus, SyncType
from datatypes.symlink_details import SymlinkDetails
from dropbox.attrs import Attributes
from dropbox.exception.exception_decorators import handle_exceptions_ex_2
from dropbox.functions import EitherStr, make_bytes, make_unicode
from dropbox.shared.server_path import MRLowerServerPath
from dropbox.shared.validated_record import BaseString, Field, ValidatedRecord

class PendingParentDetails(ValidatedRecord):
    sjid = Field.required(int)
    blocklist = Field.required(bytes)
    attrs = Field.required(Attributes)
    size = Field.required(int)
    dir = Field.required(bool)
    mtime = Field.optional(int)
    ctime = Field.optional(int)
    timestamp = Field.optional(int)
    user_id = Field.optional(int)
    host_id = Field.optional(int)
    directory_not_empty_recommit = Field.optional(bool, default = False)
    sync_type = Field.required(SyncType)
    folder_policy = Field.optional(SyncType)
    fileid = Field.optional(BaseString)
    fileid_rev = Field.optional(int)
    machineid_volumeid = Field.optional(int)
    machineid_inode = Field.optional(int)
    machineid_attr = Field.optional(BaseString)
    transition_type = Field.optional(DeletedFileStatus)
    
    def validate(self = None):
        if self.sjid < 0:
            raise TypeError('Bad sjid on pending parent details: %r', self.sjid)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(iteritems(self.attrs.attr_dict)()):
            raise TypeError(f'''Empty parent attr dict! {self.attrs.attr_dict!r}''')

    
    def to_dict(self = None):
        result = dict(self)
        result['attrs'] = result['attrs'].marshal()
        result['sync_type'] = int(result['sync_type'])
        if result.get('folder_policy'):
            result['folder_policy'] = int(result['folder_policy'])
        if feature_enabled('previous-entry-status-field-v3') and result.get('transition_type'):
            result['transition_type'] = int(result['transition_type'])
        for field_name, field_type in iteritems(self._SCHEMA):
            if field_type.is_optional and result[field_name] == field_type.default:
                result.pop(field_name)
            return result

    from_dict = (lambda cls = None, fields_dict = None: fields_dict['attrs'] = Attributes.unmarshal(fields_dict['attrs'])# WARNING: Decompyle incomplete
)()


class ExtraPendingDetails(ValidatedRecord):
    parent = Field.optional(PendingParentDetails)
    mount_request = Field.optional(int)
    upcoming_sync_type = Field.optional(SyncType)
    upcoming_folder_policy = Field.optional(SyncType)
    symlink_details = Field.optional(SymlinkDetails)
    
    def validate(self = None):
        pass
    # WARNING: Decompyle incomplete

    unmarshal = (lambda cls = None, buf = None: d = json.loads(make_unicode(buf))parent_dict = d.get('parent')parent = None# WARNING: Decompyle incomplete
)()
    __conform__ = (lambda self = None, protocol = None: self.marshal())()
    
    def to_dict(self = None):
        result = { }
    # WARNING: Decompyle incomplete

    
    def marshal(self = None):
        kw = self.to_dict()
    # WARNING: Decompyle incomplete

    
    def copy_with_parent(self = None, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class ConflictType(IntEnum):
    CONFLICTED = 1
    PERMISSION_CONFLICTED = 2
    PLACEHOLDER_SOURCE_CONFLICTED = 3
    NO_ACCESS_CONFLICTED = 4

NSMetadata = NamedTuple('NSMetadata', [
    ('permissions', int),
    ('properties', Optional[int]),
    ('team_id', Optional[int]),
    ('owner_id_hash', Optional[Text])])
MountRequest = NamedTuple('MountRequest', [
    ('mount_point_sp', MRLowerServerPath),
    ('target_ns', int),
    ('ns_metadata', NSMetadata)])
UnmountRequest = NamedTuple('UnmountRequest', [
    ('mount_point_sp', MRLowerServerPath),
    ('target_ns', int),
    ('destructive', bool),
    ('from_local', bool)])
