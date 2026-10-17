# Source Generated with Decompyle++
# File: team_selective_sync.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class ListTeamSelectiveSyncSettingsArgs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListTeamSelectiveSyncSettingsArgs_validator = bv.Struct(ListTeamSelectiveSyncSettingsArgs)

class ListTeamSelectiveSyncSettingsEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListTeamSelectiveSyncSettingsEntry_validator = bv.Struct(ListTeamSelectiveSyncSettingsEntry)

class ListTeamSelectiveSyncSettingsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ListTeamSelectiveSyncSettingsError_validator = bv.Union(ListTeamSelectiveSyncSettingsError)

class ListTeamSelectiveSyncSettingsResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListTeamSelectiveSyncSettingsResponse_validator = bv.Struct(ListTeamSelectiveSyncSettingsResponse)
ListTeamSelectiveSyncSettingsArgs.path.validator = bv.String()
ListTeamSelectiveSyncSettingsArgs.path.validator._redact = bv.BlotRedactor(None)
ListTeamSelectiveSyncSettingsArgs._all_field_names_ = set([
    'path'])
ListTeamSelectiveSyncSettingsArgs._all_fields_ = [
    ('path', ListTeamSelectiveSyncSettingsArgs.path.validator)]
ListTeamSelectiveSyncSettingsEntry.path.validator = bv.String()
ListTeamSelectiveSyncSettingsEntry.path.validator._redact = bv.BlotRedactor(None)
ListTeamSelectiveSyncSettingsEntry.target_root_fileid.validator = bv.String()
ListTeamSelectiveSyncSettingsEntry.target_root_fileid.validator._redact = bv.BlotRedactor(None)
ListTeamSelectiveSyncSettingsEntry.fileid.validator = bv.String()
ListTeamSelectiveSyncSettingsEntry.fileid.validator._redact = bv.BlotRedactor(None)
ListTeamSelectiveSyncSettingsEntry._all_field_names_ = set([
    'path',
    'target_root_fileid',
    'fileid'])
ListTeamSelectiveSyncSettingsEntry._all_fields_ = [
    ('path', ListTeamSelectiveSyncSettingsEntry.path.validator),
    ('target_root_fileid', ListTeamSelectiveSyncSettingsEntry.target_root_fileid.validator),
    ('fileid', ListTeamSelectiveSyncSettingsEntry.fileid.validator)]
ListTeamSelectiveSyncSettingsError._invalid_path_validator = bv.Void()
ListTeamSelectiveSyncSettingsError._unauthorized_ns_validator = bv.Void()
ListTeamSelectiveSyncSettingsError._other_validator = bv.Void()
ListTeamSelectiveSyncSettingsError._tagmap = {
    'invalid_path': ListTeamSelectiveSyncSettingsError._invalid_path_validator,
    'unauthorized_ns': ListTeamSelectiveSyncSettingsError._unauthorized_ns_validator,
    'other': ListTeamSelectiveSyncSettingsError._other_validator }
ListTeamSelectiveSyncSettingsError.invalid_path = ListTeamSelectiveSyncSettingsError('invalid_path')
ListTeamSelectiveSyncSettingsError.unauthorized_ns = ListTeamSelectiveSyncSettingsError('unauthorized_ns')
ListTeamSelectiveSyncSettingsError.other = ListTeamSelectiveSyncSettingsError('other')
ListTeamSelectiveSyncSettingsResponse.folders.validator = bv.Nullable(bv.List(ListTeamSelectiveSyncSettingsEntry_validator))
ListTeamSelectiveSyncSettingsResponse._all_field_names_ = set([
    'folders'])
ListTeamSelectiveSyncSettingsResponse._all_fields_ = [
    ('folders', ListTeamSelectiveSyncSettingsResponse.folders.validator)]
ListTeamSelectiveSyncSettingsArgs.path.default = ''
ListTeamSelectiveSyncSettingsEntry.path.default = ''
ListTeamSelectiveSyncSettingsEntry.target_root_fileid.default = ''
ListTeamSelectiveSyncSettingsEntry.fileid.default = ''
# WARNING: Decompyle incomplete
