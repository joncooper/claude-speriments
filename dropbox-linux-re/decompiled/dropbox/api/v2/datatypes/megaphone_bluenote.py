# Source Generated with Decompyle++
# File: megaphone_bluenote.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account_id

class ActOnNotificationRequest(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ActOnNotificationRequest_validator = bv.Struct(ActOnNotificationRequest)

class BluenoteError(bb.Union):
    pass
# WARNING: Decompyle incomplete

BluenoteError_validator = bv.Union(BluenoteError)

class NotificationRequest(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NotificationRequest_validator = bv.Struct(NotificationRequest)

class NotificationResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NotificationResponse_validator = bv.Struct(NotificationResponse)
ActOnNotificationRequest.user_id.validator = bv.UInt64()
ActOnNotificationRequest.user_id.validator._redact = bv.BlotRedactor(None)
ActOnNotificationRequest.target_object_key.validator = bv.String()
ActOnNotificationRequest.target_object_key.validator._redact = bv.BlotRedactor(None)
ActOnNotificationRequest.megaphone_parent_event_id.validator = bv.String()
ActOnNotificationRequest.megaphone_parent_event_id.validator._redact = bv.BlotRedactor(None)
ActOnNotificationRequest._all_field_names_ = set([
    'user_id',
    'target_object_key',
    'megaphone_parent_event_id'])
ActOnNotificationRequest._all_fields_ = [
    ('user_id', ActOnNotificationRequest.user_id.validator),
    ('target_object_key', ActOnNotificationRequest.target_object_key.validator),
    ('megaphone_parent_event_id', ActOnNotificationRequest.megaphone_parent_event_id.validator)]
BluenoteError._some_err_validator = bv.String()
BluenoteError._some_err_validator._redact = bv.BlotRedactor(None)
BluenoteError._other_validator = bv.Void()
BluenoteError._tagmap = {
    'some_err': BluenoteError._some_err_validator,
    'other': BluenoteError._other_validator }
BluenoteError.other = BluenoteError('other')
NotificationRequest.user_id.validator = bv.UInt64()
NotificationRequest.user_id.validator._redact = bv.BlotRedactor(None)
NotificationRequest.campaign_id.validator = bv.UInt64()
NotificationRequest.campaign_id.validator._redact = bv.BlotRedactor(None)
NotificationRequest.substitution_dict.validator = bv.Nullable(bv.Map(bv.String(), bv.String()))
NotificationRequest.fallback_en.validator = bv.Boolean()
NotificationRequest.fallback_en.validator._redact = bv.BlotRedactor(None)
NotificationRequest.is_preview.validator = bv.Boolean()
NotificationRequest.is_preview.validator._redact = bv.BlotRedactor(None)
NotificationRequest.megaphone_parent_event_id.validator = bv.String()
NotificationRequest.megaphone_parent_event_id.validator._redact = bv.BlotRedactor(None)
NotificationRequest.force_resend.validator = bv.Boolean()
NotificationRequest.force_resend.validator._redact = bv.BlotRedactor(None)
NotificationRequest.parent_correlation_id.validator = bv.String()
NotificationRequest.parent_correlation_id.validator._redact = bv.BlotRedactor(None)
NotificationRequest.version_id.validator = bv.UInt64()
NotificationRequest.version_id.validator._redact = bv.BlotRedactor(None)
NotificationRequest.deprecated_target_host_id.validator = bv.UInt64()
NotificationRequest.deprecated_target_host_id.validator._redact = bv.BlotRedactor(None)
NotificationRequest.target_device_id.validator = bv.String()
NotificationRequest.target_device_id.validator._redact = bv.BlotRedactor(None)
NotificationRequest.trigger_id.validator = bv.String()
NotificationRequest.trigger_id.validator._redact = bv.BlotRedactor(None)
NotificationRequest._all_field_names_ = set([
    'user_id',
    'campaign_id',
    'substitution_dict',
    'fallback_en',
    'is_preview',
    'megaphone_parent_event_id',
    'force_resend',
    'parent_correlation_id',
    'version_id',
    'deprecated_target_host_id',
    'target_device_id',
    'trigger_id'])
NotificationRequest._all_fields_ = [
    ('user_id', NotificationRequest.user_id.validator),
    ('campaign_id', NotificationRequest.campaign_id.validator),
    ('substitution_dict', NotificationRequest.substitution_dict.validator),
    ('fallback_en', NotificationRequest.fallback_en.validator),
    ('is_preview', NotificationRequest.is_preview.validator),
    ('megaphone_parent_event_id', NotificationRequest.megaphone_parent_event_id.validator),
    ('force_resend', NotificationRequest.force_resend.validator),
    ('parent_correlation_id', NotificationRequest.parent_correlation_id.validator),
    ('version_id', NotificationRequest.version_id.validator),
    ('deprecated_target_host_id', NotificationRequest.deprecated_target_host_id.validator),
    ('target_device_id', NotificationRequest.target_device_id.validator),
    ('trigger_id', NotificationRequest.trigger_id.validator)]
NotificationResponse.user_id.validator = bv.UInt64()
NotificationResponse.user_id.validator._redact = bv.BlotRedactor(None)
NotificationResponse.status.validator = bv.String()
NotificationResponse.status.validator._redact = bv.BlotRedactor(None)
NotificationResponse.message_id.validator = bv.String()
NotificationResponse.message_id.validator._redact = bv.BlotRedactor(None)
NotificationResponse._all_field_names_ = set([
    'user_id',
    'status',
    'message_id'])
NotificationResponse._all_fields_ = [
    ('user_id', NotificationResponse.user_id.validator),
    ('status', NotificationResponse.status.validator),
    ('message_id', NotificationResponse.message_id.validator)]
ActOnNotificationRequest.user_id.default = 0
ActOnNotificationRequest.target_object_key.default = ''
ActOnNotificationRequest.megaphone_parent_event_id.default = ''
NotificationRequest.user_id.default = 0
NotificationRequest.campaign_id.default = 0
NotificationRequest.fallback_en.default = False
NotificationRequest.is_preview.default = False
NotificationRequest.megaphone_parent_event_id.default = ''
NotificationRequest.force_resend.default = False
NotificationRequest.parent_correlation_id.default = ''
NotificationRequest.version_id.default = 0
NotificationRequest.deprecated_target_host_id.default = 0
NotificationRequest.target_device_id.default = ''
NotificationRequest.trigger_id.default = ''
NotificationResponse.user_id.default = 0
NotificationResponse.status.default = ''
NotificationResponse.message_id.default = ''
# WARNING: Decompyle incomplete
