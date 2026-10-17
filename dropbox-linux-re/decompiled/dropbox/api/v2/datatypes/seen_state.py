# Source Generated with Decompyle++
# File: seen_state.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account_id
from dropbox.api.v2.datatypes import files
from dropbox.api.v2.datatypes import team_common

class BeaconInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BeaconInfo_validator = bv.Struct(BeaconInfo)

class BeaconInfoList(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BeaconInfoList_validator = bv.Struct(BeaconInfoList)

class FileInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FileInfo_validator = bv.Struct(FileInfo)

class GetSeenStateInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSeenStateInfoArg_validator = bv.Struct(GetSeenStateInfoArg)

class GetSeenStateInfoContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSeenStateInfoContinueArg_validator = bv.Struct(GetSeenStateInfoContinueArg)

class GroupAccessDetails(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GroupAccessDetails_validator = bv.Struct(GroupAccessDetails)

class LogFileViewArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LogFileViewArg_validator = bv.Struct(LogFileViewArg)

class PlatformType(bb.Union):
    pass
# WARNING: Decompyle incomplete

PlatformType_validator = bv.Union(PlatformType)

class SeenEvent(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SeenEvent_validator = bv.Struct(SeenEvent)

class SeenStateCursor(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SeenStateCursor_validator = bv.Struct(SeenStateCursor)

class SeenStateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SeenStateError_validator = bv.Union(SeenStateError)

class SeenStateInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SeenStateInfo_validator = bv.Struct(SeenStateInfo)

class SeenStateInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SeenStateInfoResult_validator = bv.Struct(SeenStateInfoResult)

class SeenStateLastSeen(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SeenStateLastSeen_validator = bv.Struct(SeenStateLastSeen)

class SeenStateUser(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SeenStateUser_validator = bv.Struct(SeenStateUser)

class SeenStateUserArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SeenStateUserArg_validator = bv.Struct(SeenStateUserArg)

class SharedLinkDetails(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharedLinkDetails_validator = bv.Struct(SharedLinkDetails)

class SharingAccessType(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharingAccessType_validator = bv.Union(SharingAccessType)

class ViewInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ViewInfo_validator = bv.Struct(ViewInfo)
BeaconInfo.context.validator = bv.String()
BeaconInfo.identifier.validator = bv.String()
BeaconInfo.beacon_user_id.validator = bv.String()
BeaconInfo.shared_link_url.validator = bv.Nullable(bv.String())
BeaconInfo.shared_link_url.validator._redact = bv.HashRedactor(None)
BeaconInfo._all_field_names_ = set([
    'context',
    'identifier',
    'beacon_user_id',
    'shared_link_url'])
BeaconInfo._all_fields_ = [
    ('context', BeaconInfo.context.validator),
    ('identifier', BeaconInfo.identifier.validator),
    ('beacon_user_id', BeaconInfo.beacon_user_id.validator),
    ('shared_link_url', BeaconInfo.shared_link_url.validator)]
BeaconInfoList.beacon_infos.validator = bv.List(BeaconInfo_validator, min_items = 1)
BeaconInfoList._all_field_names_ = set([
    'beacon_infos'])
BeaconInfoList._all_fields_ = [
    ('beacon_infos', BeaconInfoList.beacon_infos.validator)]
FileInfo.ns_id.validator = bv.Nullable(bv.UInt64())
FileInfo.file_identifier.validator = bv.Nullable(files.PathOrId_validator)
FileInfo.url.validator = bv.Nullable(bv.String())
FileInfo.url.validator._redact = bv.HashRedactor(None)
FileInfo.shared_link_details.validator = bv.Nullable(SharedLinkDetails_validator)
FileInfo._all_field_names_ = set([
    'ns_id',
    'file_identifier',
    'url',
    'shared_link_details'])
FileInfo._all_fields_ = [
    ('ns_id', FileInfo.ns_id.validator),
    ('file_identifier', FileInfo.file_identifier.validator),
    ('url', FileInfo.url.validator),
    ('shared_link_details', FileInfo.shared_link_details.validator)]
GetSeenStateInfoArg.file_infos.validator = bv.List(FileInfo_validator)
GetSeenStateInfoArg.limit.validator = bv.UInt32()
GetSeenStateInfoArg._all_field_names_ = set([
    'file_infos',
    'limit'])
GetSeenStateInfoArg._all_fields_ = [
    ('file_infos', GetSeenStateInfoArg.file_infos.validator),
    ('limit', GetSeenStateInfoArg.limit.validator)]
GetSeenStateInfoContinueArg.file_infos.validator = bv.List(FileInfo_validator)
GetSeenStateInfoContinueArg.cursor.validator = bv.Bytes()
GetSeenStateInfoContinueArg.limit.validator = bv.UInt32()
GetSeenStateInfoContinueArg._all_field_names_ = set([
    'file_infos',
    'cursor',
    'limit'])
GetSeenStateInfoContinueArg._all_fields_ = [
    ('file_infos', GetSeenStateInfoContinueArg.file_infos.validator),
    ('cursor', GetSeenStateInfoContinueArg.cursor.validator),
    ('limit', GetSeenStateInfoContinueArg.limit.validator)]
GroupAccessDetails.group_ids.validator = bv.List(team_common.GroupId_validator)
GroupAccessDetails.group_access_only.validator = bv.Boolean()
GroupAccessDetails._all_field_names_ = set([
    'group_ids',
    'group_access_only'])
GroupAccessDetails._all_fields_ = [
    ('group_ids', GroupAccessDetails.group_ids.validator),
    ('group_access_only', GroupAccessDetails.group_access_only.validator)]
LogFileViewArg.file_views.validator = bv.List(ViewInfo_validator)
LogFileViewArg.client_time.validator = bv.Nullable(bv.UInt64())
LogFileViewArg._all_field_names_ = set([
    'file_views',
    'client_time'])
LogFileViewArg._all_fields_ = [
    ('file_views', LogFileViewArg.file_views.validator),
    ('client_time', LogFileViewArg.client_time.validator)]
PlatformType._web_validator = bv.Void()
PlatformType._desktop_validator = bv.Void()
PlatformType._mobile_ios_validator = bv.Void()
PlatformType._mobile_android_validator = bv.Void()
PlatformType._api_validator = bv.Void()
PlatformType._unknown_validator = bv.Void()
PlatformType._mobile_validator = bv.Void()
PlatformType._other_validator = bv.Void()
PlatformType._tagmap = {
    'web': PlatformType._web_validator,
    'desktop': PlatformType._desktop_validator,
    'mobile_ios': PlatformType._mobile_ios_validator,
    'mobile_android': PlatformType._mobile_android_validator,
    'api': PlatformType._api_validator,
    'unknown': PlatformType._unknown_validator,
    'mobile': PlatformType._mobile_validator,
    'other': PlatformType._other_validator }
PlatformType.web = PlatformType('web')
PlatformType.desktop = PlatformType('desktop')
PlatformType.mobile_ios = PlatformType('mobile_ios')
PlatformType.mobile_android = PlatformType('mobile_android')
PlatformType.api = PlatformType('api')
PlatformType.unknown = PlatformType('unknown')
PlatformType.mobile = PlatformType('mobile')
PlatformType.other = PlatformType('other')
SeenEvent.ts.validator = bv.UInt64()
SeenEvent.platform_type.validator = PlatformType_validator
SeenEvent._all_field_names_ = set([
    'ts',
    'platform_type'])
SeenEvent._all_fields_ = [
    ('ts', SeenEvent.ts.validator),
    ('platform_type', SeenEvent.platform_type.validator)]
SeenStateCursor.cursor_state.validator = bv.Nullable(bv.Bytes())
SeenStateCursor.has_next.validator = bv.Nullable(bv.Boolean())
SeenStateCursor._all_field_names_ = set([
    'cursor_state',
    'has_next'])
SeenStateCursor._all_fields_ = [
    ('cursor_state', SeenStateCursor.cursor_state.validator),
    ('has_next', SeenStateCursor.has_next.validator)]
SeenStateError._no_file_validator = bv.Void()
SeenStateError._deleted_validator = bv.Void()
SeenStateError._no_permission_validator = bv.Void()
SeenStateError._inconsistent_params_validator = bv.Void()
SeenStateError._invalid_cursor_validator = bv.Void()
SeenStateError._invalid_caller_validator = bv.Void()
SeenStateError._other_validator = bv.Void()
SeenStateError._tagmap = {
    'no_file': SeenStateError._no_file_validator,
    'deleted': SeenStateError._deleted_validator,
    'no_permission': SeenStateError._no_permission_validator,
    'inconsistent_params': SeenStateError._inconsistent_params_validator,
    'invalid_cursor': SeenStateError._invalid_cursor_validator,
    'invalid_caller': SeenStateError._invalid_caller_validator,
    'other': SeenStateError._other_validator }
SeenStateError.no_file = SeenStateError('no_file')
SeenStateError.deleted = SeenStateError('deleted')
SeenStateError.no_permission = SeenStateError('no_permission')
SeenStateError.inconsistent_params = SeenStateError('inconsistent_params')
SeenStateError.invalid_cursor = SeenStateError('invalid_cursor')
SeenStateError.invalid_caller = SeenStateError('invalid_caller')
SeenStateError.other = SeenStateError('other')
SeenStateInfo.seen_states.validator = bv.List(SeenStateLastSeen_validator)
SeenStateInfo._all_field_names_ = set([
    'seen_states'])
SeenStateInfo._all_fields_ = [
    ('seen_states', SeenStateInfo.seen_states.validator)]
SeenStateInfoResult.file_info.validator = FileInfo_validator
SeenStateInfoResult.seen_state_info.validator = SeenStateInfo_validator
SeenStateInfoResult.seen_state_error.validator = bv.Nullable(SeenStateError_validator)
SeenStateInfoResult.seen_state_cursor.validator = bv.Nullable(SeenStateCursor_validator)
SeenStateInfoResult._all_field_names_ = set([
    'file_info',
    'seen_state_info',
    'seen_state_error',
    'seen_state_cursor'])
SeenStateInfoResult._all_fields_ = [
    ('file_info', SeenStateInfoResult.file_info.validator),
    ('seen_state_info', SeenStateInfoResult.seen_state_info.validator),
    ('seen_state_error', SeenStateInfoResult.seen_state_error.validator),
    ('seen_state_cursor', SeenStateInfoResult.seen_state_cursor.validator)]
SeenStateLastSeen.when_last_seen.validator = bv.Nullable(bv.UInt64())
SeenStateLastSeen.seen_state_user.validator = SeenStateUser_validator
SeenStateLastSeen.seen_events.validator = bv.List(SeenEvent_validator)
SeenStateLastSeen.platform_type.validator = PlatformType_validator
SeenStateLastSeen._all_field_names_ = set([
    'when_last_seen',
    'seen_state_user',
    'seen_events',
    'platform_type'])
SeenStateLastSeen._all_fields_ = [
    ('when_last_seen', SeenStateLastSeen.when_last_seen.validator),
    ('seen_state_user', SeenStateLastSeen.seen_state_user.validator),
    ('seen_events', SeenStateLastSeen.seen_events.validator),
    ('platform_type', SeenStateLastSeen.platform_type.validator)]
SeenStateUser.user_id.validator = bv.String()
SeenStateUser.user_id.validator._redact = bv.BlotRedactor(None)
SeenStateUser.display_name.validator = bv.String()
SeenStateUser.display_name.validator._redact = bv.BlotRedactor(None)
SeenStateUser.email.validator = bv.Nullable(bv.String())
SeenStateUser.email.validator._redact = bv.BlotRedactor(None)
SeenStateUser.photo_circle_url.validator = bv.Nullable(bv.String())
SeenStateUser.photo_circle_url.validator._redact = bv.HashRedactor(None)
SeenStateUser.sharing_access_type.validator = bv.Nullable(SharingAccessType_validator)
SeenStateUser.in_owners_team.validator = bv.Boolean()
SeenStateUser.same_team.validator = bv.Boolean()
SeenStateUser._all_field_names_ = set([
    'user_id',
    'display_name',
    'email',
    'photo_circle_url',
    'sharing_access_type',
    'in_owners_team',
    'same_team'])
SeenStateUser._all_fields_ = [
    ('user_id', SeenStateUser.user_id.validator),
    ('display_name', SeenStateUser.display_name.validator),
    ('email', SeenStateUser.email.validator),
    ('photo_circle_url', SeenStateUser.photo_circle_url.validator),
    ('sharing_access_type', SeenStateUser.sharing_access_type.validator),
    ('in_owners_team', SeenStateUser.in_owners_team.validator),
    ('same_team', SeenStateUser.same_team.validator)]
SeenStateUserArg.user_ids.validator = bv.List(bv.String())
SeenStateUserArg.user_ids.validator._redact = bv.BlotRedactor(None)
SeenStateUserArg.file_info.validator = FileInfo_validator
SeenStateUserArg._all_field_names_ = set([
    'user_ids',
    'file_info'])
SeenStateUserArg._all_fields_ = [
    ('user_ids', SeenStateUserArg.user_ids.validator),
    ('file_info', SeenStateUserArg.file_info.validator)]
SharedLinkDetails.url.validator = bv.String()
SharedLinkDetails.url.validator._redact = bv.HashRedactor(None)
SharedLinkDetails.path.validator = bv.Nullable(files.Path_validator)
SharedLinkDetails._all_field_names_ = set([
    'url',
    'path'])
SharedLinkDetails._all_fields_ = [
    ('url', SharedLinkDetails.url.validator),
    ('path', SharedLinkDetails.path.validator)]
SharingAccessType._edit_member_access_validator = GroupAccessDetails_validator
SharingAccessType._view_member_access_validator = GroupAccessDetails_validator
SharingAccessType._edit_link_access_validator = bv.Void()
SharingAccessType._view_link_access_validator = bv.Void()
SharingAccessType._link_only_validator = bv.Void()
SharingAccessType._other_validator = bv.Void()
SharingAccessType._tagmap = {
    'edit_member_access': SharingAccessType._edit_member_access_validator,
    'view_member_access': SharingAccessType._view_member_access_validator,
    'edit_link_access': SharingAccessType._edit_link_access_validator,
    'view_link_access': SharingAccessType._view_link_access_validator,
    'link_only': SharingAccessType._link_only_validator,
    'other': SharingAccessType._other_validator }
SharingAccessType.edit_link_access = SharingAccessType('edit_link_access')
SharingAccessType.view_link_access = SharingAccessType('view_link_access')
SharingAccessType.link_only = SharingAccessType('link_only')
SharingAccessType.other = SharingAccessType('other')
ViewInfo.file_info.validator = FileInfo_validator
ViewInfo.platform_type.validator = PlatformType_validator
ViewInfo.sec_time.validator = bv.Nullable(bv.UInt64())
ViewInfo.origin.validator = bv.UInt32()
ViewInfo.action.validator = bv.Nullable(bv.UInt32())
ViewInfo._all_field_names_ = set([
    'file_info',
    'platform_type',
    'sec_time',
    'origin',
    'action'])
ViewInfo._all_fields_ = [
    ('file_info', ViewInfo.file_info.validator),
    ('platform_type', ViewInfo.platform_type.validator),
    ('sec_time', ViewInfo.sec_time.validator),
    ('origin', ViewInfo.origin.validator),
    ('action', ViewInfo.action.validator)]
GetSeenStateInfoArg.limit.default = 103
ViewInfo.origin.default = 0
# WARNING: Decompyle incomplete
