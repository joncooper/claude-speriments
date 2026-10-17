# Source Generated with Decompyle++
# File: client_auth.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import common

class CreateHostForUserArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateHostForUserArg_validator = bv.Struct(CreateHostForUserArg)

class CreateHostForUserError(bb.Union):
    pass
# WARNING: Decompyle incomplete

CreateHostForUserError_validator = bv.Union(CreateHostForUserError)

class CreateHostForUserResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CreateHostForUserResult_validator = bv.Struct(CreateHostForUserResult)

class DeviceLimitExceededPaywallError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DeviceLimitExceededPaywallError_validator = bv.Struct(DeviceLimitExceededPaywallError)

class LinkUserToHostArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkUserToHostArg_validator = bv.Struct(LinkUserToHostArg)

class LinkUserToHostError(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkUserToHostError_validator = bv.Union(LinkUserToHostError)

class LinkUserToHostResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkUserToHostResult_validator = bv.Struct(LinkUserToHostResult)

class PostSetupFlags(bb.Union):
    pass
# WARNING: Decompyle incomplete

PostSetupFlags_validator = bv.Union(PostSetupFlags)
CreateHostForUserArg.hostname.validator = bv.String()
CreateHostForUserArg.hostname.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.buildno.validator = bv.String()
CreateHostForUserArg.buildno.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.uname.validator = bv.String()
CreateHostForUserArg.uname.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.host_characteristics.validator = bv.String()
CreateHostForUserArg.host_characteristics.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.machine_id.validator = bv.String()
CreateHostForUserArg.machine_id.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.buildid.validator = bv.String()
CreateHostForUserArg.buildid.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.glibc_version.validator = bv.String()
CreateHostForUserArg.glibc_version.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.client_info.validator = bv.String()
CreateHostForUserArg.client_info.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.tag.validator = bv.String()
CreateHostForUserArg.tag.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg.linked_user_id.validator = bv.Int64()
CreateHostForUserArg.linked_user_id.validator._redact = bv.BlotRedactor(None)
CreateHostForUserArg._all_field_names_ = set([
    'hostname',
    'buildno',
    'uname',
    'host_characteristics',
    'machine_id',
    'buildid',
    'glibc_version',
    'client_info',
    'tag',
    'linked_user_id'])
CreateHostForUserArg._all_fields_ = [
    ('hostname', CreateHostForUserArg.hostname.validator),
    ('buildno', CreateHostForUserArg.buildno.validator),
    ('uname', CreateHostForUserArg.uname.validator),
    ('host_characteristics', CreateHostForUserArg.host_characteristics.validator),
    ('machine_id', CreateHostForUserArg.machine_id.validator),
    ('buildid', CreateHostForUserArg.buildid.validator),
    ('glibc_version', CreateHostForUserArg.glibc_version.validator),
    ('client_info', CreateHostForUserArg.client_info.validator),
    ('tag', CreateHostForUserArg.tag.validator),
    ('linked_user_id', CreateHostForUserArg.linked_user_id.validator)]
CreateHostForUserError._device_limit_exceeded_validator = bv.String()
CreateHostForUserError._device_limit_exceeded_validator._redact = bv.BlotRedactor(None)
CreateHostForUserError._host_platform_deprecated_validator = bv.String()
CreateHostForUserError._host_platform_deprecated_validator._redact = bv.BlotRedactor(None)
CreateHostForUserError._host_invalid_display_name_validator = bv.String()
CreateHostForUserError._host_invalid_display_name_validator._redact = bv.BlotRedactor(None)
CreateHostForUserError._device_limit_exceeded_paywall_validator = DeviceLimitExceededPaywallError_validator
CreateHostForUserError._host_validation_invalid_validator = bv.Void()
CreateHostForUserError._host_platform_os_deprecated_validator = bv.String()
CreateHostForUserError._host_platform_os_deprecated_validator._redact = bv.BlotRedactor(None)
CreateHostForUserError._host_platform_client_deprecated_validator = bv.String()
CreateHostForUserError._host_platform_client_deprecated_validator._redact = bv.BlotRedactor(None)
CreateHostForUserError._no_desktop_access_validator = bv.String()
CreateHostForUserError._no_desktop_access_validator._redact = bv.BlotRedactor(None)
CreateHostForUserError._other_validator = bv.Void()
CreateHostForUserError._tagmap = {
    'device_limit_exceeded': CreateHostForUserError._device_limit_exceeded_validator,
    'host_platform_deprecated': CreateHostForUserError._host_platform_deprecated_validator,
    'host_invalid_display_name': CreateHostForUserError._host_invalid_display_name_validator,
    'device_limit_exceeded_paywall': CreateHostForUserError._device_limit_exceeded_paywall_validator,
    'host_validation_invalid': CreateHostForUserError._host_validation_invalid_validator,
    'host_platform_os_deprecated': CreateHostForUserError._host_platform_os_deprecated_validator,
    'host_platform_client_deprecated': CreateHostForUserError._host_platform_client_deprecated_validator,
    'no_desktop_access': CreateHostForUserError._no_desktop_access_validator,
    'other': CreateHostForUserError._other_validator }
CreateHostForUserError.host_validation_invalid = CreateHostForUserError('host_validation_invalid')
CreateHostForUserError.other = CreateHostForUserError('other')
CreateHostForUserResult.host_int.validator = bv.Int64()
CreateHostForUserResult.host_int.validator._redact = bv.BlotRedactor(None)
CreateHostForUserResult.host_secret.validator = bv.String()
CreateHostForUserResult.host_secret.validator._redact = bv.BlotRedactor(None)
CreateHostForUserResult.deal_code.validator = bv.String()
CreateHostForUserResult.deal_code.validator._redact = bv.BlotRedactor(None)
CreateHostForUserResult.is_fedramp_user.validator = bv.Boolean()
CreateHostForUserResult.is_fedramp_user.validator._redact = bv.BlotRedactor(None)
CreateHostForUserResult.infinite_exposed.validator = bv.Boolean()
CreateHostForUserResult.infinite_exposed.validator._redact = bv.BlotRedactor(None)
CreateHostForUserResult.infinite_sync_policy.validator = bv.String()
CreateHostForUserResult.infinite_sync_policy.validator._redact = bv.BlotRedactor(None)
CreateHostForUserResult.post_link_setup_flags.validator = bv.Nullable(bv.List(PostSetupFlags_validator))
CreateHostForUserResult._all_field_names_ = set([
    'host_int',
    'host_secret',
    'deal_code',
    'is_fedramp_user',
    'infinite_exposed',
    'infinite_sync_policy',
    'post_link_setup_flags'])
CreateHostForUserResult._all_fields_ = [
    ('host_int', CreateHostForUserResult.host_int.validator),
    ('host_secret', CreateHostForUserResult.host_secret.validator),
    ('deal_code', CreateHostForUserResult.deal_code.validator),
    ('is_fedramp_user', CreateHostForUserResult.is_fedramp_user.validator),
    ('infinite_exposed', CreateHostForUserResult.infinite_exposed.validator),
    ('infinite_sync_policy', CreateHostForUserResult.infinite_sync_policy.validator),
    ('post_link_setup_flags', CreateHostForUserResult.post_link_setup_flags.validator)]
DeviceLimitExceededPaywallError.current_host.validator = bv.Int64()
DeviceLimitExceededPaywallError.current_host.validator._redact = bv.BlotRedactor(None)
DeviceLimitExceededPaywallError.device_limit_nonce.validator = bv.String()
DeviceLimitExceededPaywallError.device_limit_nonce.validator._redact = bv.BlotRedactor(None)
DeviceLimitExceededPaywallError.sku_content.validator = bv.Nullable(common.SerializedSkuContent_validator)
DeviceLimitExceededPaywallError.user_dbx_id.validator = bv.Int64()
DeviceLimitExceededPaywallError.user_dbx_id.validator._redact = bv.BlotRedactor(None)
DeviceLimitExceededPaywallError.user_root_ns_id.validator = bv.Int64()
DeviceLimitExceededPaywallError.user_root_ns_id.validator._redact = bv.BlotRedactor(None)
DeviceLimitExceededPaywallError.status.validator = bv.String()
DeviceLimitExceededPaywallError.status.validator._redact = bv.BlotRedactor(None)
DeviceLimitExceededPaywallError._all_field_names_ = set([
    'current_host',
    'device_limit_nonce',
    'sku_content',
    'user_dbx_id',
    'user_root_ns_id',
    'status'])
DeviceLimitExceededPaywallError._all_fields_ = [
    ('current_host', DeviceLimitExceededPaywallError.current_host.validator),
    ('device_limit_nonce', DeviceLimitExceededPaywallError.device_limit_nonce.validator),
    ('sku_content', DeviceLimitExceededPaywallError.sku_content.validator),
    ('user_dbx_id', DeviceLimitExceededPaywallError.user_dbx_id.validator),
    ('user_root_ns_id', DeviceLimitExceededPaywallError.user_root_ns_id.validator),
    ('status', DeviceLimitExceededPaywallError.status.validator)]
LinkUserToHostArg.host_nonce.validator = bv.String()
LinkUserToHostArg.host_nonce.validator._redact = bv.BlotRedactor(None)
LinkUserToHostArg.client_info.validator = bv.String()
LinkUserToHostArg.client_info.validator._redact = bv.BlotRedactor(None)
LinkUserToHostArg.tag.validator = bv.String()
LinkUserToHostArg.tag.validator._redact = bv.BlotRedactor(None)
LinkUserToHostArg.linked_user_id.validator = bv.Int64()
LinkUserToHostArg.linked_user_id.validator._redact = bv.BlotRedactor(None)
LinkUserToHostArg._all_field_names_ = set([
    'host_nonce',
    'client_info',
    'tag',
    'linked_user_id'])
LinkUserToHostArg._all_fields_ = [
    ('host_nonce', LinkUserToHostArg.host_nonce.validator),
    ('client_info', LinkUserToHostArg.client_info.validator),
    ('tag', LinkUserToHostArg.tag.validator),
    ('linked_user_id', LinkUserToHostArg.linked_user_id.validator)]
LinkUserToHostError._device_limit_exceeded_validator = bv.String()
LinkUserToHostError._device_limit_exceeded_validator._redact = bv.BlotRedactor(None)
LinkUserToHostError._host_invalid_nonce_validator = bv.Void()
LinkUserToHostError._host_platform_deprecated_validator = bv.String()
LinkUserToHostError._host_platform_deprecated_validator._redact = bv.BlotRedactor(None)
LinkUserToHostError._host_invalid_display_name_validator = bv.String()
LinkUserToHostError._host_invalid_display_name_validator._redact = bv.BlotRedactor(None)
LinkUserToHostError._device_limit_exceeded_paywall_validator = DeviceLimitExceededPaywallError_validator
LinkUserToHostError._host_validation_invalid_validator = bv.Void()
LinkUserToHostError._host_platform_os_deprecated_validator = bv.String()
LinkUserToHostError._host_platform_os_deprecated_validator._redact = bv.BlotRedactor(None)
LinkUserToHostError._host_platform_client_deprecated_validator = bv.String()
LinkUserToHostError._host_platform_client_deprecated_validator._redact = bv.BlotRedactor(None)
LinkUserToHostError._no_desktop_access_validator = bv.String()
LinkUserToHostError._no_desktop_access_validator._redact = bv.BlotRedactor(None)
LinkUserToHostError._other_validator = bv.Void()
LinkUserToHostError._tagmap = {
    'device_limit_exceeded': LinkUserToHostError._device_limit_exceeded_validator,
    'host_invalid_nonce': LinkUserToHostError._host_invalid_nonce_validator,
    'host_platform_deprecated': LinkUserToHostError._host_platform_deprecated_validator,
    'host_invalid_display_name': LinkUserToHostError._host_invalid_display_name_validator,
    'device_limit_exceeded_paywall': LinkUserToHostError._device_limit_exceeded_paywall_validator,
    'host_validation_invalid': LinkUserToHostError._host_validation_invalid_validator,
    'host_platform_os_deprecated': LinkUserToHostError._host_platform_os_deprecated_validator,
    'host_platform_client_deprecated': LinkUserToHostError._host_platform_client_deprecated_validator,
    'no_desktop_access': LinkUserToHostError._no_desktop_access_validator,
    'other': LinkUserToHostError._other_validator }
LinkUserToHostError.host_invalid_nonce = LinkUserToHostError('host_invalid_nonce')
LinkUserToHostError.host_validation_invalid = LinkUserToHostError('host_validation_invalid')
LinkUserToHostError.other = LinkUserToHostError('other')
LinkUserToHostResult.deal_code.validator = bv.String()
LinkUserToHostResult.deal_code.validator._redact = bv.BlotRedactor(None)
LinkUserToHostResult.is_fedramp_user.validator = bv.Boolean()
LinkUserToHostResult.is_fedramp_user.validator._redact = bv.BlotRedactor(None)
LinkUserToHostResult.infinite_exposed.validator = bv.Boolean()
LinkUserToHostResult.infinite_exposed.validator._redact = bv.BlotRedactor(None)
LinkUserToHostResult.infinite_sync_policy.validator = bv.String()
LinkUserToHostResult.infinite_sync_policy.validator._redact = bv.BlotRedactor(None)
LinkUserToHostResult.post_link_setup_flags.validator = bv.Nullable(bv.List(PostSetupFlags_validator))
LinkUserToHostResult._all_field_names_ = set([
    'deal_code',
    'is_fedramp_user',
    'infinite_exposed',
    'infinite_sync_policy',
    'post_link_setup_flags'])
LinkUserToHostResult._all_fields_ = [
    ('deal_code', LinkUserToHostResult.deal_code.validator),
    ('is_fedramp_user', LinkUserToHostResult.is_fedramp_user.validator),
    ('infinite_exposed', LinkUserToHostResult.infinite_exposed.validator),
    ('infinite_sync_policy', LinkUserToHostResult.infinite_sync_policy.validator),
    ('post_link_setup_flags', LinkUserToHostResult.post_link_setup_flags.validator)]
PostSetupFlags._require_scale_mitigation_validator = bv.Void()
PostSetupFlags._show_move_dropbox_validator = bv.Void()
PostSetupFlags._other_validator = bv.Void()
PostSetupFlags._tagmap = {
    'require_scale_mitigation': PostSetupFlags._require_scale_mitigation_validator,
    'show_move_dropbox': PostSetupFlags._show_move_dropbox_validator,
    'other': PostSetupFlags._other_validator }
PostSetupFlags.require_scale_mitigation = PostSetupFlags('require_scale_mitigation')
PostSetupFlags.show_move_dropbox = PostSetupFlags('show_move_dropbox')
PostSetupFlags.other = PostSetupFlags('other')
CreateHostForUserArg.uname.default = ''
CreateHostForUserArg.host_characteristics.default = ''
CreateHostForUserArg.glibc_version.default = ''
CreateHostForUserArg.client_info.default = ''
CreateHostForUserArg.tag.default = ''
CreateHostForUserArg.linked_user_id.default = 0
CreateHostForUserResult.host_int.default = 0
CreateHostForUserResult.host_secret.default = ''
CreateHostForUserResult.deal_code.default = ''
CreateHostForUserResult.is_fedramp_user.default = False
CreateHostForUserResult.infinite_exposed.default = False
CreateHostForUserResult.infinite_sync_policy.default = ''
DeviceLimitExceededPaywallError.current_host.default = 0
DeviceLimitExceededPaywallError.device_limit_nonce.default = ''
DeviceLimitExceededPaywallError.user_dbx_id.default = 0
DeviceLimitExceededPaywallError.user_root_ns_id.default = 0
DeviceLimitExceededPaywallError.status.default = ''
LinkUserToHostArg.client_info.default = ''
LinkUserToHostArg.tag.default = ''
LinkUserToHostArg.linked_user_id.default = 0
LinkUserToHostResult.deal_code.default = ''
LinkUserToHostResult.is_fedramp_user.default = False
LinkUserToHostResult.infinite_exposed.default = False
LinkUserToHostResult.infinite_sync_policy.default = ''
# WARNING: Decompyle incomplete
