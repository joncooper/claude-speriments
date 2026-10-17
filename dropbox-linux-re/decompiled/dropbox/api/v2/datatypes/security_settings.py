# Source Generated with Decompyle++
# File: security_settings.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import public_id

class AllHostsAndDevicesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AllHostsAndDevicesArg_validator = bv.Struct(AllHostsAndDevicesArg)

class AllHostsAndDevicesResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AllHostsAndDevicesResult_validator = bv.Struct(AllHostsAndDevicesResult)

class AppInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AppInfo_validator = bv.Struct(AppInfo)

class AuthHistoryEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AuthHistoryEntry_validator = bv.Struct(AuthHistoryEntry)

class AuthHistoryError(bb.Union):
    pass
# WARNING: Decompyle incomplete

AuthHistoryError_validator = bv.Union(AuthHistoryError)

class GetAuthHistoryArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetAuthHistoryArg_validator = bv.Struct(GetAuthHistoryArg)

class GetAuthHistoryResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetAuthHistoryResult_validator = bv.Struct(GetAuthHistoryResult)

class GetLinkedHostsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetLinkedHostsArg_validator = bv.Struct(GetLinkedHostsArg)

class GetLinkedMobileDevicesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetLinkedMobileDevicesArg_validator = bv.Struct(GetLinkedMobileDevicesArg)

class HostInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

HostInfo_validator = bv.Struct(HostInfo)

class LinkedDevicesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkedDevicesArg_validator = bv.Struct(LinkedDevicesArg)

class LinkedDevicesResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkedDevicesResult_validator = bv.Struct(LinkedDevicesResult)

class LogoutUserSessionArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LogoutUserSessionArg_validator = bv.Struct(LogoutUserSessionArg)

class MobileDeviceInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MobileDeviceInfo_validator = bv.Struct(MobileDeviceInfo)

class RenameAuthDeviceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RenameAuthDeviceArg_validator = bv.Struct(RenameAuthDeviceArg)

class RenameAuthDeviceError(bb.Union):
    pass
# WARNING: Decompyle incomplete

RenameAuthDeviceError_validator = bv.Union(RenameAuthDeviceError)

class SendVerifyEmailArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SendVerifyEmailArg_validator = bv.Struct(SendVerifyEmailArg)

class SendVerifyEmailError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SendVerifyEmailError_validator = bv.Union(SendVerifyEmailError)

class SendVerifyEmailReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

SendVerifyEmailReason_validator = bv.Union(SendVerifyEmailReason)

class SendVerifyEmailType(bb.Union):
    pass
# WARNING: Decompyle incomplete

SendVerifyEmailType_validator = bv.Union(SendVerifyEmailType)

class SendVerifyPendingEmailArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SendVerifyPendingEmailArg_validator = bv.Struct(SendVerifyPendingEmailArg)

class SendVerifyPendingEmailError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SendVerifyPendingEmailError_validator = bv.Union(SendVerifyPendingEmailError)

class TwofactorInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TwofactorInfo_validator = bv.Struct(TwofactorInfo)

class UninstallAppActionArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UninstallAppActionArg_validator = bv.Struct(UninstallAppActionArg)

class UninstallAppArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UninstallAppArg_validator = bv.Struct(UninstallAppArg)

class UninstallAppError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UninstallAppError_validator = bv.Union(UninstallAppError)

class UnlinkDevicesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnlinkDevicesArg_validator = bv.Struct(UnlinkDevicesArg)

class UnlinkDevicesCallSource(bb.Union):
    pass
# WARNING: Decompyle incomplete

UnlinkDevicesCallSource_validator = bv.Union(UnlinkDevicesCallSource)

class UnlinkDevicesError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UnlinkDevicesError_validator = bv.Union(UnlinkDevicesError)

class UnlinkHostArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnlinkHostArg_validator = bv.Struct(UnlinkHostArg)

class UnlinkHostError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UnlinkHostError_validator = bv.Union(UnlinkHostError)

class UnlinkMobileDeviceArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UnlinkMobileDeviceArg_validator = bv.Struct(UnlinkMobileDeviceArg)

class VerifyEmailCodeArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

VerifyEmailCodeArg_validator = bv.Struct(VerifyEmailCodeArg)

class VerifyEmailCodeError(bb.Union):
    pass
# WARNING: Decompyle incomplete

VerifyEmailCodeError_validator = bv.Union(VerifyEmailCodeError)

class WebSessionInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

WebSessionInfo_validator = bv.Struct(WebSessionInfo)
AuthDeviceId_validator = bv.String()
AuthDeviceId_validator._redact = bv.BlotRedactor(None)
MobileDeviceId_validator = bv.String()
MobileDeviceId_validator._redact = bv.BlotRedactor(None)
WebSessionId_validator = bv.String()
WebSessionId_validator._redact = bv.BlotRedactor(None)
AllHostsAndDevicesArg.device_id.validator = bv.Nullable(MobileDeviceId_validator)
AllHostsAndDevicesArg._all_field_names_ = set([
    'device_id'])
AllHostsAndDevicesArg._all_fields_ = [
    ('device_id', AllHostsAndDevicesArg.device_id.validator)]
AllHostsAndDevicesResult.desktop_hosts.validator = bv.Nullable(bv.List(HostInfo_validator))
AllHostsAndDevicesResult.mobile_devices.validator = bv.Nullable(bv.List(MobileDeviceInfo_validator))
AllHostsAndDevicesResult._all_field_names_ = set([
    'desktop_hosts',
    'mobile_devices'])
AllHostsAndDevicesResult._all_fields_ = [
    ('desktop_hosts', AllHostsAndDevicesResult.desktop_hosts.validator),
    ('mobile_devices', AllHostsAndDevicesResult.mobile_devices.validator)]
AppInfo.app_folder.validator = bv.String()
AppInfo.app_folder.validator._redact = bv.BlotRedactor(None)
AppInfo.app_name.validator = bv.String()
AppInfo.app_name.validator._redact = bv.BlotRedactor(None)
AppInfo.id.validator = bv.UInt64()
AppInfo.id.validator._redact = bv.BlotRedactor(None)
AppInfo.publisher.validator = bv.String()
AppInfo.publisher.validator._redact = bv.BlotRedactor(None)
AppInfo.publisher_url.validator = bv.String()
AppInfo.publisher_url.validator._redact = bv.BlotRedactor(None)
AppInfo.icon_url.validator = bv.String()
AppInfo.icon_url.validator._redact = bv.BlotRedactor(None)
AppInfo.access_type_desc.validator = bv.String()
AppInfo.access_type_desc.validator._redact = bv.BlotRedactor(None)
AppInfo.scope_messages.validator = bv.Nullable(bv.List(bv.String()))
AppInfo.scope_messages.validator._redact = bv.BlotRedactor(None)
AppInfo.app_status.validator = bv.UInt64()
AppInfo.app_status.validator._redact = bv.BlotRedactor(None)
AppInfo.last_activity.validator = bv.String()
AppInfo.last_activity.validator._redact = bv.BlotRedactor(None)
AppInfo.last_activity_raw.validator = bv.UInt64()
AppInfo.last_activity_raw.validator._redact = bv.BlotRedactor(None)
AppInfo._all_field_names_ = set([
    'app_folder',
    'app_name',
    'id',
    'publisher',
    'publisher_url',
    'icon_url',
    'access_type_desc',
    'scope_messages',
    'app_status',
    'last_activity',
    'last_activity_raw'])
AppInfo._all_fields_ = [
    ('app_folder', AppInfo.app_folder.validator),
    ('app_name', AppInfo.app_name.validator),
    ('id', AppInfo.id.validator),
    ('publisher', AppInfo.publisher.validator),
    ('publisher_url', AppInfo.publisher_url.validator),
    ('icon_url', AppInfo.icon_url.validator),
    ('access_type_desc', AppInfo.access_type_desc.validator),
    ('scope_messages', AppInfo.scope_messages.validator),
    ('app_status', AppInfo.app_status.validator),
    ('last_activity', AppInfo.last_activity.validator),
    ('last_activity_raw', AppInfo.last_activity_raw.validator)]
AuthHistoryEntry.timestamp.validator = bv.UInt64()
AuthHistoryEntry.timestamp.validator._redact = bv.BlotRedactor(None)
AuthHistoryEntry.event_type.validator = bv.String()
AuthHistoryEntry.event_type.validator._redact = bv.BlotRedactor(None)
AuthHistoryEntry.ip.validator = bv.String()
AuthHistoryEntry.ip.validator._redact = bv.BlotRedactor(None)
AuthHistoryEntry.location.validator = bv.String()
AuthHistoryEntry.location.validator._redact = bv.BlotRedactor(None)
AuthHistoryEntry.client_info.validator = bv.Nullable(bv.String())
AuthHistoryEntry.result.validator = bv.Nullable(bv.String())
AuthHistoryEntry._all_field_names_ = set([
    'timestamp',
    'event_type',
    'ip',
    'location',
    'client_info',
    'result'])
AuthHistoryEntry._all_fields_ = [
    ('timestamp', AuthHistoryEntry.timestamp.validator),
    ('event_type', AuthHistoryEntry.event_type.validator),
    ('ip', AuthHistoryEntry.ip.validator),
    ('location', AuthHistoryEntry.location.validator),
    ('client_info', AuthHistoryEntry.client_info.validator),
    ('result', AuthHistoryEntry.result.validator)]
AuthHistoryError._unhandled_event_validator = bv.Void()
AuthHistoryError._other_validator = bv.Void()
AuthHistoryError._tagmap = {
    'unhandled_event': AuthHistoryError._unhandled_event_validator,
    'other': AuthHistoryError._other_validator }
AuthHistoryError.unhandled_event = AuthHistoryError('unhandled_event')
AuthHistoryError.other = AuthHistoryError('other')
GetAuthHistoryArg.cursor.validator = bv.Nullable(bv.String())
GetAuthHistoryArg._all_field_names_ = set([
    'cursor'])
GetAuthHistoryArg._all_fields_ = [
    ('cursor', GetAuthHistoryArg.cursor.validator)]
GetAuthHistoryResult.auth_history.validator = bv.List(AuthHistoryEntry_validator)
GetAuthHistoryResult._all_field_names_ = set([
    'auth_history'])
GetAuthHistoryResult._all_fields_ = [
    ('auth_history', GetAuthHistoryResult.auth_history.validator)]
GetLinkedHostsArg.include_pending.validator = bv.Nullable(bv.Boolean())
GetLinkedHostsArg._all_field_names_ = set([
    'include_pending'])
GetLinkedHostsArg._all_fields_ = [
    ('include_pending', GetLinkedHostsArg.include_pending.validator)]
GetLinkedMobileDevicesArg.check_pending.validator = bv.Nullable(bv.Boolean())
GetLinkedMobileDevicesArg._all_field_names_ = set([
    'check_pending'])
GetLinkedMobileDevicesArg._all_fields_ = [
    ('check_pending', GetLinkedMobileDevicesArg.check_pending.validator)]
HostInfo.display_name.validator = bv.String()
HostInfo.display_name.validator._redact = bv.BlotRedactor(None)
HostInfo.id.validator = bv.UInt64()
HostInfo.id.validator._redact = bv.BlotRedactor(None)
HostInfo.version.validator = bv.String()
HostInfo.version.validator._redact = bv.BlotRedactor(None)
HostInfo.last_activity.validator = bv.String()
HostInfo.last_activity.validator._redact = bv.BlotRedactor(None)
HostInfo.last_activity_raw.validator = bv.UInt64()
HostInfo.last_activity_raw.validator._redact = bv.BlotRedactor(None)
HostInfo.last_ip.validator = bv.String()
HostInfo.last_ip.validator._redact = bv.BlotRedactor(None)
HostInfo.location.validator = bv.String()
HostInfo.location.validator._redact = bv.BlotRedactor(None)
HostInfo.platform.validator = bv.String()
HostInfo.platform.validator._redact = bv.BlotRedactor(None)
HostInfo.can_delete.validator = bv.Boolean()
HostInfo.can_delete.validator._redact = bv.BlotRedactor(None)
HostInfo.delete_support_type.validator = bv.UInt64()
HostInfo.delete_support_type.validator._redact = bv.BlotRedactor(None)
HostInfo.icon.validator = bv.String()
HostInfo.icon.validator._redact = bv.BlotRedactor(None)
HostInfo.is_linked.validator = bv.Boolean()
HostInfo.is_linked.validator._redact = bv.BlotRedactor(None)
HostInfo.unlink_state.validator = bv.Nullable(bv.UInt64())
HostInfo.is_pending.validator = bv.Boolean()
HostInfo.is_pending.validator._redact = bv.BlotRedactor(None)
HostInfo.device_id.validator = bv.Nullable(bv.String())
HostInfo._all_field_names_ = set([
    'display_name',
    'id',
    'version',
    'last_activity',
    'last_activity_raw',
    'last_ip',
    'location',
    'platform',
    'can_delete',
    'delete_support_type',
    'icon',
    'is_linked',
    'unlink_state',
    'is_pending',
    'device_id'])
HostInfo._all_fields_ = [
    ('display_name', HostInfo.display_name.validator),
    ('id', HostInfo.id.validator),
    ('version', HostInfo.version.validator),
    ('last_activity', HostInfo.last_activity.validator),
    ('last_activity_raw', HostInfo.last_activity_raw.validator),
    ('last_ip', HostInfo.last_ip.validator),
    ('location', HostInfo.location.validator),
    ('platform', HostInfo.platform.validator),
    ('can_delete', HostInfo.can_delete.validator),
    ('delete_support_type', HostInfo.delete_support_type.validator),
    ('icon', HostInfo.icon.validator),
    ('is_linked', HostInfo.is_linked.validator),
    ('unlink_state', HostInfo.unlink_state.validator),
    ('is_pending', HostInfo.is_pending.validator),
    ('device_id', HostInfo.device_id.validator)]
LinkedDevicesArg.device_id.validator = bv.Nullable(MobileDeviceId_validator)
LinkedDevicesArg.include_pending.validator = bv.Nullable(bv.Boolean())
LinkedDevicesArg._all_field_names_ = set([
    'device_id',
    'include_pending'])
LinkedDevicesArg._all_fields_ = [
    ('device_id', LinkedDevicesArg.device_id.validator),
    ('include_pending', LinkedDevicesArg.include_pending.validator)]
LinkedDevicesResult.desktop_hosts.validator = bv.Nullable(bv.List(HostInfo_validator))
LinkedDevicesResult.mobile_devices.validator = bv.Nullable(bv.List(MobileDeviceInfo_validator))
LinkedDevicesResult._all_field_names_ = set([
    'desktop_hosts',
    'mobile_devices'])
LinkedDevicesResult._all_fields_ = [
    ('desktop_hosts', LinkedDevicesResult.desktop_hosts.validator),
    ('mobile_devices', LinkedDevicesResult.mobile_devices.validator)]
LogoutUserSessionArg.remote_login_id.validator = WebSessionId_validator
LogoutUserSessionArg._all_field_names_ = set([
    'remote_login_id'])
LogoutUserSessionArg._all_fields_ = [
    ('remote_login_id', LogoutUserSessionArg.remote_login_id.validator)]
MobileDeviceInfo.app_id.validator = bv.UInt64()
MobileDeviceInfo.app_id.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.category.validator = bv.String()
MobileDeviceInfo.category.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.version.validator = bv.String()
MobileDeviceInfo.version.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.device_id.validator = MobileDeviceId_validator
MobileDeviceInfo.display_name.validator = bv.String()
MobileDeviceInfo.display_name.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.last_activity.validator = bv.String()
MobileDeviceInfo.last_activity.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.last_activity_raw.validator = bv.UInt64()
MobileDeviceInfo.last_activity_raw.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.last_ip.validator = bv.String()
MobileDeviceInfo.last_ip.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.location.validator = bv.String()
MobileDeviceInfo.location.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.icon.validator = bv.String()
MobileDeviceInfo.icon.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.is_emm_enabled.validator = bv.Boolean()
MobileDeviceInfo.is_emm_enabled.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo.is_pending.validator = bv.Nullable(bv.Boolean())
MobileDeviceInfo.is_current.validator = bv.Nullable(bv.Boolean())
MobileDeviceInfo.is_password_app.validator = bv.Boolean()
MobileDeviceInfo.is_password_app.validator._redact = bv.BlotRedactor(None)
MobileDeviceInfo._all_field_names_ = set([
    'app_id',
    'category',
    'version',
    'device_id',
    'display_name',
    'last_activity',
    'last_activity_raw',
    'last_ip',
    'location',
    'icon',
    'is_emm_enabled',
    'is_pending',
    'is_current',
    'is_password_app'])
MobileDeviceInfo._all_fields_ = [
    ('app_id', MobileDeviceInfo.app_id.validator),
    ('category', MobileDeviceInfo.category.validator),
    ('version', MobileDeviceInfo.version.validator),
    ('device_id', MobileDeviceInfo.device_id.validator),
    ('display_name', MobileDeviceInfo.display_name.validator),
    ('last_activity', MobileDeviceInfo.last_activity.validator),
    ('last_activity_raw', MobileDeviceInfo.last_activity_raw.validator),
    ('last_ip', MobileDeviceInfo.last_ip.validator),
    ('location', MobileDeviceInfo.location.validator),
    ('icon', MobileDeviceInfo.icon.validator),
    ('is_emm_enabled', MobileDeviceInfo.is_emm_enabled.validator),
    ('is_pending', MobileDeviceInfo.is_pending.validator),
    ('is_current', MobileDeviceInfo.is_current.validator),
    ('is_password_app', MobileDeviceInfo.is_password_app.validator)]
RenameAuthDeviceArg.device_gid.validator = AuthDeviceId_validator
RenameAuthDeviceArg.nickname.validator = bv.String(max_length = 100)
RenameAuthDeviceArg.nickname.validator._redact = bv.BlotRedactor(None)
RenameAuthDeviceArg._all_field_names_ = set([
    'device_gid',
    'nickname'])
RenameAuthDeviceArg._all_fields_ = [
    ('device_gid', RenameAuthDeviceArg.device_gid.validator),
    ('nickname', RenameAuthDeviceArg.nickname.validator)]
RenameAuthDeviceError._no_such_device_validator = bv.Void()
RenameAuthDeviceError._other_validator = bv.Void()
RenameAuthDeviceError._tagmap = {
    'no_such_device': RenameAuthDeviceError._no_such_device_validator,
    'other': RenameAuthDeviceError._other_validator }
RenameAuthDeviceError.no_such_device = RenameAuthDeviceError('no_such_device')
RenameAuthDeviceError.other = RenameAuthDeviceError('other')
SendVerifyEmailArg.verification_reason.validator = SendVerifyEmailReason_validator
SendVerifyEmailArg.type.validator = SendVerifyEmailType_validator
SendVerifyEmailArg._all_field_names_ = set([
    'verification_reason',
    'type'])
SendVerifyEmailArg._all_fields_ = [
    ('verification_reason', SendVerifyEmailArg.verification_reason.validator),
    ('type', SendVerifyEmailArg.type.validator)]
SendVerifyEmailError._invalid_type_validator = bv.Void()
SendVerifyEmailError._invalid_reason_validator = bv.Void()
SendVerifyEmailError._other_validator = bv.Void()
SendVerifyEmailError._tagmap = {
    'invalid_type': SendVerifyEmailError._invalid_type_validator,
    'invalid_reason': SendVerifyEmailError._invalid_reason_validator,
    'other': SendVerifyEmailError._other_validator }
SendVerifyEmailError.invalid_type = SendVerifyEmailError('invalid_type')
SendVerifyEmailError.invalid_reason = SendVerifyEmailError('invalid_reason')
SendVerifyEmailError.other = SendVerifyEmailError('other')
SendVerifyEmailReason._security_checkup_validator = bv.Void()
SendVerifyEmailReason._paper_user_validator = bv.Void()
SendVerifyEmailReason._dash_unverified_email_validator = bv.Void()
SendVerifyEmailReason._other_validator = bv.Void()
SendVerifyEmailReason._tagmap = {
    'security_checkup': SendVerifyEmailReason._security_checkup_validator,
    'paper_user': SendVerifyEmailReason._paper_user_validator,
    'dash_unverified_email': SendVerifyEmailReason._dash_unverified_email_validator,
    'other': SendVerifyEmailReason._other_validator }
SendVerifyEmailReason.security_checkup = SendVerifyEmailReason('security_checkup')
SendVerifyEmailReason.paper_user = SendVerifyEmailReason('paper_user')
SendVerifyEmailReason.dash_unverified_email = SendVerifyEmailReason('dash_unverified_email')
SendVerifyEmailReason.other = SendVerifyEmailReason('other')
SendVerifyEmailType._link_validator = bv.Void()
SendVerifyEmailType._code_validator = bv.Void()
SendVerifyEmailType._other_validator = bv.Void()
SendVerifyEmailType._tagmap = {
    'link': SendVerifyEmailType._link_validator,
    'code': SendVerifyEmailType._code_validator,
    'other': SendVerifyEmailType._other_validator }
SendVerifyEmailType.link = SendVerifyEmailType('link')
SendVerifyEmailType.code = SendVerifyEmailType('code')
SendVerifyEmailType.other = SendVerifyEmailType('other')
SendVerifyPendingEmailArg.unverified_new_email.validator = bv.String()
SendVerifyPendingEmailArg.unverified_new_email.validator._redact = bv.BlotRedactor(None)
SendVerifyPendingEmailArg._all_field_names_ = set([
    'unverified_new_email'])
SendVerifyPendingEmailArg._all_fields_ = [
    ('unverified_new_email', SendVerifyPendingEmailArg.unverified_new_email.validator)]
SendVerifyPendingEmailError._incorrect_email_validator = bv.Void()
SendVerifyPendingEmailError._other_validator = bv.Void()
SendVerifyPendingEmailError._tagmap = {
    'incorrect_email': SendVerifyPendingEmailError._incorrect_email_validator,
    'other': SendVerifyPendingEmailError._other_validator }
SendVerifyPendingEmailError.incorrect_email = SendVerifyPendingEmailError('incorrect_email')
SendVerifyPendingEmailError.other = SendVerifyPendingEmailError('other')
TwofactorInfo.user_can_disable.validator = bv.Boolean()
TwofactorInfo.user_can_disable.validator._redact = bv.BlotRedactor(None)
TwofactorInfo.status.validator = bv.String()
TwofactorInfo.status.validator._redact = bv.BlotRedactor(None)
TwofactorInfo.primary.validator = bv.String()
TwofactorInfo.primary.validator._redact = bv.BlotRedactor(None)
TwofactorInfo.primary_phone.validator = bv.Nullable(bv.String())
TwofactorInfo.backup.validator = bv.Nullable(bv.String())
TwofactorInfo.num_security_keys.validator = bv.UInt64()
TwofactorInfo.num_security_keys.validator._redact = bv.BlotRedactor(None)
TwofactorInfo._all_field_names_ = set([
    'user_can_disable',
    'status',
    'primary',
    'primary_phone',
    'backup',
    'num_security_keys'])
TwofactorInfo._all_fields_ = [
    ('user_can_disable', TwofactorInfo.user_can_disable.validator),
    ('status', TwofactorInfo.status.validator),
    ('primary', TwofactorInfo.primary.validator),
    ('primary_phone', TwofactorInfo.primary_phone.validator),
    ('backup', TwofactorInfo.backup.validator),
    ('num_security_keys', TwofactorInfo.num_security_keys.validator)]
UninstallAppActionArg.action_id.validator = bv.String()
UninstallAppActionArg.action_id.validator._redact = bv.BlotRedactor(None)
UninstallAppActionArg._all_field_names_ = set([
    'action_id'])
UninstallAppActionArg._all_fields_ = [
    ('action_id', UninstallAppActionArg.action_id.validator)]
UninstallAppArg.app_id.validator = bv.UInt64()
UninstallAppArg.app_id.validator._redact = bv.BlotRedactor(None)
UninstallAppArg.keep_sandbox_files.validator = bv.Boolean()
UninstallAppArg.keep_sandbox_files.validator._redact = bv.BlotRedactor(None)
UninstallAppArg._all_field_names_ = set([
    'app_id',
    'keep_sandbox_files'])
UninstallAppArg._all_fields_ = [
    ('app_id', UninstallAppArg.app_id.validator),
    ('keep_sandbox_files', UninstallAppArg.keep_sandbox_files.validator)]
UninstallAppError._invalid_app_validator = bv.Void()
UninstallAppError._team_linked_app_validator = bv.Void()
UninstallAppError._app_cannot_be_uninstalled_validator = bv.Void()
UninstallAppError._other_validator = bv.Void()
UninstallAppError._tagmap = {
    'invalid_app': UninstallAppError._invalid_app_validator,
    'team_linked_app': UninstallAppError._team_linked_app_validator,
    'app_cannot_be_uninstalled': UninstallAppError._app_cannot_be_uninstalled_validator,
    'other': UninstallAppError._other_validator }
UninstallAppError.invalid_app = UninstallAppError('invalid_app')
UninstallAppError.team_linked_app = UninstallAppError('team_linked_app')
UninstallAppError.app_cannot_be_uninstalled = UninstallAppError('app_cannot_be_uninstalled')
UninstallAppError.other = UninstallAppError('other')
UnlinkDevicesArg.mobile_devices.validator = bv.Nullable(bv.List(UnlinkMobileDeviceArg_validator))
UnlinkDevicesArg.desktop_hosts.validator = bv.Nullable(bv.List(UnlinkHostArg_validator))
UnlinkDevicesArg.call_source.validator = bv.Nullable(UnlinkDevicesCallSource_validator)
UnlinkDevicesArg._all_field_names_ = set([
    'mobile_devices',
    'desktop_hosts',
    'call_source'])
UnlinkDevicesArg._all_fields_ = [
    ('mobile_devices', UnlinkDevicesArg.mobile_devices.validator),
    ('desktop_hosts', UnlinkDevicesArg.desktop_hosts.validator),
    ('call_source', UnlinkDevicesArg.call_source.validator)]
UnlinkDevicesCallSource._device_limits_m1_nudge_modal_validator = bv.Void()
UnlinkDevicesCallSource._other_validator = bv.Void()
UnlinkDevicesCallSource._tagmap = {
    'device_limits_m1_nudge_modal': UnlinkDevicesCallSource._device_limits_m1_nudge_modal_validator,
    'other': UnlinkDevicesCallSource._other_validator }
UnlinkDevicesCallSource.device_limits_m1_nudge_modal = UnlinkDevicesCallSource('device_limits_m1_nudge_modal')
UnlinkDevicesCallSource.other = UnlinkDevicesCallSource('other')
UnlinkDevicesError._invalid_app_validator = bv.Void()
UnlinkDevicesError._invalid_device_validator = bv.Void()
UnlinkDevicesError._already_unlinked_validator = bv.Void()
UnlinkDevicesError._other_validator = bv.Void()
UnlinkDevicesError._tagmap = {
    'invalid_app': UnlinkDevicesError._invalid_app_validator,
    'invalid_device': UnlinkDevicesError._invalid_device_validator,
    'already_unlinked': UnlinkDevicesError._already_unlinked_validator,
    'other': UnlinkDevicesError._other_validator }
UnlinkDevicesError.invalid_app = UnlinkDevicesError('invalid_app')
UnlinkDevicesError.invalid_device = UnlinkDevicesError('invalid_device')
UnlinkDevicesError.already_unlinked = UnlinkDevicesError('already_unlinked')
UnlinkDevicesError.other = UnlinkDevicesError('other')
UnlinkHostArg.host_id.validator = bv.UInt64()
UnlinkHostArg.host_id.validator._redact = bv.BlotRedactor(None)
UnlinkHostArg.delete_data.validator = bv.Nullable(bv.Boolean())
UnlinkHostArg._all_field_names_ = set([
    'host_id',
    'delete_data'])
UnlinkHostArg._all_fields_ = [
    ('host_id', UnlinkHostArg.host_id.validator),
    ('delete_data', UnlinkHostArg.delete_data.validator)]
UnlinkHostError._invalid_host_id_for_user_validator = bv.Void()
UnlinkHostError._already_unlinked_validator = bv.Void()
UnlinkHostError._other_validator = bv.Void()
UnlinkHostError._tagmap = {
    'invalid_host_id_for_user': UnlinkHostError._invalid_host_id_for_user_validator,
    'already_unlinked': UnlinkHostError._already_unlinked_validator,
    'other': UnlinkHostError._other_validator }
UnlinkHostError.invalid_host_id_for_user = UnlinkHostError('invalid_host_id_for_user')
UnlinkHostError.already_unlinked = UnlinkHostError('already_unlinked')
UnlinkHostError.other = UnlinkHostError('other')
UnlinkMobileDeviceArg.device_id.validator = MobileDeviceId_validator
UnlinkMobileDeviceArg.app_id.validator = bv.UInt64()
UnlinkMobileDeviceArg.app_id.validator._redact = bv.BlotRedactor(None)
UnlinkMobileDeviceArg._all_field_names_ = set([
    'device_id',
    'app_id'])
UnlinkMobileDeviceArg._all_fields_ = [
    ('device_id', UnlinkMobileDeviceArg.device_id.validator),
    ('app_id', UnlinkMobileDeviceArg.app_id.validator)]
VerifyEmailCodeArg.verification_code.validator = bv.String()
VerifyEmailCodeArg.verification_code.validator._redact = bv.BlotRedactor(None)
VerifyEmailCodeArg._all_field_names_ = set([
    'verification_code'])
VerifyEmailCodeArg._all_fields_ = [
    ('verification_code', VerifyEmailCodeArg.verification_code.validator)]
VerifyEmailCodeError._verification_code_invalid_validator = bv.Void()
VerifyEmailCodeError._attempt_rate_exceeded_validator = bv.Void()
VerifyEmailCodeError._experiment_disabled_validator = bv.Void()
VerifyEmailCodeError._other_validator = bv.Void()
VerifyEmailCodeError._tagmap = {
    'verification_code_invalid': VerifyEmailCodeError._verification_code_invalid_validator,
    'attempt_rate_exceeded': VerifyEmailCodeError._attempt_rate_exceeded_validator,
    'experiment_disabled': VerifyEmailCodeError._experiment_disabled_validator,
    'other': VerifyEmailCodeError._other_validator }
VerifyEmailCodeError.verification_code_invalid = VerifyEmailCodeError('verification_code_invalid')
VerifyEmailCodeError.attempt_rate_exceeded = VerifyEmailCodeError('attempt_rate_exceeded')
VerifyEmailCodeError.experiment_disabled = VerifyEmailCodeError('experiment_disabled')
VerifyEmailCodeError.other = VerifyEmailCodeError('other')
WebSessionInfo.browser_name.validator = bv.String()
WebSessionInfo.browser_name.validator._redact = bv.BlotRedactor(None)
WebSessionInfo.os_name.validator = bv.String()
WebSessionInfo.os_name.validator._redact = bv.BlotRedactor(None)
WebSessionInfo.last_activity.validator = bv.String()
WebSessionInfo.last_activity.validator._redact = bv.BlotRedactor(None)
WebSessionInfo.location.validator = bv.String()
WebSessionInfo.location.validator._redact = bv.BlotRedactor(None)
WebSessionInfo.login_id.validator = WebSessionId_validator
WebSessionInfo.is_current.validator = bv.Boolean()
WebSessionInfo.is_current.validator._redact = bv.BlotRedactor(None)
WebSessionInfo.icon.validator = bv.String()
WebSessionInfo.icon.validator._redact = bv.BlotRedactor(None)
WebSessionInfo._all_field_names_ = set([
    'browser_name',
    'os_name',
    'last_activity',
    'location',
    'login_id',
    'is_current',
    'icon'])
WebSessionInfo._all_fields_ = [
    ('browser_name', WebSessionInfo.browser_name.validator),
    ('os_name', WebSessionInfo.os_name.validator),
    ('last_activity', WebSessionInfo.last_activity.validator),
    ('location', WebSessionInfo.location.validator),
    ('login_id', WebSessionInfo.login_id.validator),
    ('is_current', WebSessionInfo.is_current.validator),
    ('icon', WebSessionInfo.icon.validator)]
SendVerifyEmailArg.verification_reason.default = SendVerifyEmailReason.security_checkup
SendVerifyEmailArg.type.default = SendVerifyEmailType.link
# WARNING: Decompyle incomplete
