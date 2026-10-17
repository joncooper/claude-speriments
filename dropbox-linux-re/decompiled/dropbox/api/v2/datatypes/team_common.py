# Source Generated with Decompyle++
# File: team_common.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import common

class GroupManagementType(bb.Union):
    pass
# WARNING: Decompyle incomplete

GroupManagementType_validator = bv.Union(GroupManagementType)

class GroupSummary(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GroupSummary_validator = bv.Struct(GroupSummary)

class GroupType(bb.Union):
    pass
# WARNING: Decompyle incomplete

GroupType_validator = bv.Union(GroupType)

class MemberSpaceLimitType(bb.Union):
    pass
# WARNING: Decompyle incomplete

MemberSpaceLimitType_validator = bv.Union(MemberSpaceLimitType)

class TeamReportEngineError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TeamReportEngineError_validator = bv.Union(TeamReportEngineError)

class TimeRange(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TimeRange_validator = bv.Struct(TimeRange)
GroupExternalId_validator = bv.String()
GroupExternalId_validator._redact = bv.BlotRedactor(None)
GroupId_validator = bv.String()
GroupId_validator._redact = bv.BlotRedactor(None)
MemberExternalId_validator = bv.String(max_length = 64)
MemberExternalId_validator._redact = bv.BlotRedactor(None)
ResellerId_validator = bv.String()
ResellerId_validator._redact = bv.BlotRedactor(None)
TeamId_validator = bv.String()
TeamId_validator._redact = bv.BlotRedactor(None)
TeamMemberId_validator = bv.String()
TeamMemberId_validator._redact = bv.BlotRedactor(None)
GroupManagementType._user_managed_validator = bv.Void()
GroupManagementType._company_managed_validator = bv.Void()
GroupManagementType._system_managed_validator = bv.Void()
GroupManagementType._other_validator = bv.Void()
GroupManagementType._tagmap = {
    'user_managed': GroupManagementType._user_managed_validator,
    'company_managed': GroupManagementType._company_managed_validator,
    'system_managed': GroupManagementType._system_managed_validator,
    'other': GroupManagementType._other_validator }
GroupManagementType.user_managed = GroupManagementType('user_managed')
GroupManagementType.company_managed = GroupManagementType('company_managed')
GroupManagementType.system_managed = GroupManagementType('system_managed')
GroupManagementType.other = GroupManagementType('other')
GroupSummary.group_name.validator = bv.String()
GroupSummary.group_name.validator._redact = bv.BlotRedactor(None)
GroupSummary.group_id.validator = GroupId_validator
GroupSummary.group_external_id.validator = bv.Nullable(GroupExternalId_validator)
GroupSummary.member_count.validator = bv.Nullable(bv.UInt32())
GroupSummary.group_management_type.validator = GroupManagementType_validator
GroupSummary._all_field_names_ = set([
    'group_name',
    'group_id',
    'group_external_id',
    'member_count',
    'group_management_type'])
GroupSummary._all_fields_ = [
    ('group_name', GroupSummary.group_name.validator),
    ('group_id', GroupSummary.group_id.validator),
    ('group_external_id', GroupSummary.group_external_id.validator),
    ('member_count', GroupSummary.member_count.validator),
    ('group_management_type', GroupSummary.group_management_type.validator)]
GroupType._team_validator = bv.Void()
GroupType._user_managed_validator = bv.Void()
GroupType._other_validator = bv.Void()
GroupType._tagmap = {
    'team': GroupType._team_validator,
    'user_managed': GroupType._user_managed_validator,
    'other': GroupType._other_validator }
GroupType.team = GroupType('team')
GroupType.user_managed = GroupType('user_managed')
GroupType.other = GroupType('other')
MemberSpaceLimitType._off_validator = bv.Void()
MemberSpaceLimitType._alert_only_validator = bv.Void()
MemberSpaceLimitType._stop_sync_validator = bv.Void()
MemberSpaceLimitType._other_validator = bv.Void()
MemberSpaceLimitType._tagmap = {
    'off': MemberSpaceLimitType._off_validator,
    'alert_only': MemberSpaceLimitType._alert_only_validator,
    'stop_sync': MemberSpaceLimitType._stop_sync_validator,
    'other': MemberSpaceLimitType._other_validator }
MemberSpaceLimitType.off = MemberSpaceLimitType('off')
MemberSpaceLimitType.alert_only = MemberSpaceLimitType('alert_only')
MemberSpaceLimitType.stop_sync = MemberSpaceLimitType('stop_sync')
MemberSpaceLimitType.other = MemberSpaceLimitType('other')
TeamReportEngineError._generic_error_validator = bv.Void()
TeamReportEngineError._rate_limit_validator = bv.Void()
TeamReportEngineError._other_validator = bv.Void()
TeamReportEngineError._tagmap = {
    'generic_error': TeamReportEngineError._generic_error_validator,
    'rate_limit': TeamReportEngineError._rate_limit_validator,
    'other': TeamReportEngineError._other_validator }
TeamReportEngineError.generic_error = TeamReportEngineError('generic_error')
TeamReportEngineError.rate_limit = TeamReportEngineError('rate_limit')
TeamReportEngineError.other = TeamReportEngineError('other')
TimeRange.start_time.validator = bv.Nullable(common.DropboxTimestamp_validator)
TimeRange.end_time.validator = bv.Nullable(common.DropboxTimestamp_validator)
TimeRange._all_field_names_ = set([
    'start_time',
    'end_time'])
TimeRange._all_fields_ = [
    ('start_time', TimeRange.start_time.validator),
    ('end_time', TimeRange.end_time.validator)]
ROUTES = { }
