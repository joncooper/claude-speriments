# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import cash_catalog_constants_stone

class DropboxDuration(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DropboxDuration_validator = bv.Struct(DropboxDuration)

class InvalidPathRootError(bb.Struct):
    pass
# WARNING: Decompyle incomplete

InvalidPathRootError_validator = bv.Struct(InvalidPathRootError)

class PathRoot(bb.Union):
    pass
# WARNING: Decompyle incomplete

PathRoot_validator = bv.Union(PathRoot)

class PathRootError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PathRootError_validator = bv.Union(PathRootError)

class PlanChangeToken(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PlanChangeToken_validator = bv.Struct(PlanChangeToken)

class RootInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RootInfo_validator = bv.StructTree(RootInfo)

class SerializedPhoneInputData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SerializedPhoneInputData_validator = bv.Struct(SerializedPhoneInputData)

class SerializedSkuContent(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SerializedSkuContent_validator = bv.Struct(SerializedSkuContent)

class SerializedSkuContentV2(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SerializedSkuContentV2_validator = bv.Struct(SerializedSkuContentV2)

class SerializedSubStateContent(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SerializedSubStateContent_validator = bv.Struct(SerializedSubStateContent)

class TeamRootInfo(RootInfo):
    pass
# WARNING: Decompyle incomplete

TeamRootInfo_validator = bv.Struct(TeamRootInfo)

class UrlByProtocol(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UrlByProtocol_validator = bv.Struct(UrlByProtocol)

class UserRootInfo(RootInfo):
    pass
# WARNING: Decompyle incomplete

UserRootInfo_validator = bv.Struct(UserRootInfo)
Date_validator = bv.Timestamp('%Y-%m-%d')
DisplayName_validator = bv.String(pattern = '[^/:?*<>"|]*')
DisplayName_validator._redact = bv.BlotRedactor(None)
DisplayNameLegacy_validator = bv.String()
DisplayNameLegacy_validator._redact = bv.BlotRedactor(None)
DropboxTimestamp_validator = bv.Timestamp('%Y-%m-%dT%H:%M:%SZ')
EmailAddress_validator = bv.String(max_length = 255, pattern = "^['#&A-Za-z0-9._%+-]+@[A-Za-z0-9-][A-Za-z0-9.-]*\\.[A-Za-z]{2,15}$")
EmailAddress_validator._redact = bv.HashRedactor('^()(?:[^@]+)(@[^@]{1,2})(?:[^@]*)(\\.[^@\\.]+)$')
LanguageCode_validator = bv.String(min_length = 2)
NamePart_validator = bv.String(min_length = 1, max_length = 50, pattern = '[^/:?*<>"|]*')
NamePart_validator._redact = bv.BlotRedactor(None)
NamespaceId_validator = bv.String(pattern = '[-_0-9a-zA-Z:]+')
OptionalNamePart_validator = bv.String(max_length = 50, pattern = '[^/:?*<>"|]*')
OptionalNamePart_validator._redact = bv.BlotRedactor(None)
SessionId_validator = bv.String()
SharedFolderId_validator = NamespaceId_validator
DropboxDuration.seconds.validator = bv.Int64()
DropboxDuration.nanos.validator = bv.Int32()
DropboxDuration._all_field_names_ = set([
    'seconds',
    'nanos'])
DropboxDuration._all_fields_ = [
    ('seconds', DropboxDuration.seconds.validator),
    ('nanos', DropboxDuration.nanos.validator)]
InvalidPathRootError.path_root.validator = bv.Nullable(bv.String())
InvalidPathRootError._all_field_names_ = set([
    'path_root'])
InvalidPathRootError._all_fields_ = [
    ('path_root', InvalidPathRootError.path_root.validator)]
PathRoot._home_validator = bv.Void()
PathRoot._root_validator = NamespaceId_validator
PathRoot._namespace_id_validator = NamespaceId_validator
PathRoot._other_validator = bv.Void()
PathRoot._tagmap = {
    'home': PathRoot._home_validator,
    'root': PathRoot._root_validator,
    'namespace_id': PathRoot._namespace_id_validator,
    'other': PathRoot._other_validator }
PathRoot.home = PathRoot('home')
PathRoot.other = PathRoot('other')
PathRootError._invalid_root_validator = RootInfo_validator
PathRootError._no_permission_validator = bv.Void()
PathRootError._invalid_validator = InvalidPathRootError_validator
PathRootError._other_validator = bv.Void()
PathRootError._tagmap = {
    'invalid_root': PathRootError._invalid_root_validator,
    'no_permission': PathRootError._no_permission_validator,
    'invalid': PathRootError._invalid_validator,
    'other': PathRootError._other_validator }
PathRootError.no_permission = PathRootError('no_permission')
PathRootError.other = PathRootError('other')
PlanChangeToken.plan_sku_code.validator = bv.String()
PlanChangeToken.pricing_token.validator = bv.String()
PlanChangeToken._all_field_names_ = set([
    'plan_sku_code',
    'pricing_token'])
PlanChangeToken._all_fields_ = [
    ('plan_sku_code', PlanChangeToken.plan_sku_code.validator),
    ('pricing_token', PlanChangeToken.pricing_token.validator)]
RootInfo.root_namespace_id.validator = NamespaceId_validator
RootInfo.home_namespace_id.validator = NamespaceId_validator
RootInfo._field_names_ = set([
    'root_namespace_id',
    'home_namespace_id'])
RootInfo._all_field_names_ = RootInfo._field_names_
RootInfo._fields_ = [
    ('root_namespace_id', RootInfo.root_namespace_id.validator),
    ('home_namespace_id', RootInfo.home_namespace_id.validator)]
RootInfo._all_fields_ = RootInfo._fields_
RootInfo._tag_to_subtype_ = {
    ('team',): TeamRootInfo_validator,
    ('user',): UserRootInfo_validator }
RootInfo._pytype_to_tag_and_subtype_ = {
    UserRootInfo: (('user',), UserRootInfo_validator),
    TeamRootInfo: (('team',), TeamRootInfo_validator) }
RootInfo._is_catch_all_ = True
SerializedPhoneInputData.country_list.validator = bv.List(bv.List(bv.String()))
SerializedPhoneInputData.phone_code_map.validator = bv.Map(bv.String(), bv.String())
SerializedPhoneInputData._all_field_names_ = set([
    'country_list',
    'phone_code_map'])
SerializedPhoneInputData._all_fields_ = [
    ('country_list', SerializedPhoneInputData.country_list.validator),
    ('phone_code_map', SerializedPhoneInputData.phone_code_map.validator)]
SerializedSkuContent.display_brand_is_dropbox_business.validator = bv.Boolean()
SerializedSkuContent.display_brand_is_dropbox_business.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent.has_unlimited_space.validator = bv.Boolean()
SerializedSkuContent.has_unlimited_space.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent.is_trial.validator = bv.Boolean()
SerializedSkuContent.is_trial.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent.name.validator = bv.String()
SerializedSkuContent.name.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent.quota_gb.validator = bv.Float64()
SerializedSkuContent.quota_gb.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent.sku_schedule.validator = bv.String()
SerializedSkuContent.sku_schedule.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent.trademark_name_has_dropbox.validator = bv.Boolean()
SerializedSkuContent.trademark_name_has_dropbox.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent.vacuuming_policy_max_days.validator = bv.Int64()
SerializedSkuContent.vacuuming_policy_max_days.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent.sku_type.validator = bv.String()
SerializedSkuContent.sku_type.validator._redact = bv.BlotRedactor(None)
SerializedSkuContent._all_field_names_ = set([
    'display_brand_is_dropbox_business',
    'has_unlimited_space',
    'is_trial',
    'name',
    'quota_gb',
    'sku_schedule',
    'trademark_name_has_dropbox',
    'vacuuming_policy_max_days',
    'sku_type'])
SerializedSkuContent._all_fields_ = [
    ('display_brand_is_dropbox_business', SerializedSkuContent.display_brand_is_dropbox_business.validator),
    ('has_unlimited_space', SerializedSkuContent.has_unlimited_space.validator),
    ('is_trial', SerializedSkuContent.is_trial.validator),
    ('name', SerializedSkuContent.name.validator),
    ('quota_gb', SerializedSkuContent.quota_gb.validator),
    ('sku_schedule', SerializedSkuContent.sku_schedule.validator),
    ('trademark_name_has_dropbox', SerializedSkuContent.trademark_name_has_dropbox.validator),
    ('vacuuming_policy_max_days', SerializedSkuContent.vacuuming_policy_max_days.validator),
    ('sku_type', SerializedSkuContent.sku_type.validator)]
SerializedSkuContentV2.display_brand_is_dropbox_business.validator = bv.Boolean()
SerializedSkuContentV2.display_brand_is_dropbox_business.validator._redact = bv.BlotRedactor(None)
SerializedSkuContentV2.has_unlimited_space.validator = bv.Boolean()
SerializedSkuContentV2.has_unlimited_space.validator._redact = bv.BlotRedactor(None)
SerializedSkuContentV2.is_trial.validator = bv.Boolean()
SerializedSkuContentV2.is_trial.validator._redact = bv.BlotRedactor(None)
SerializedSkuContentV2.name.validator = bv.String()
SerializedSkuContentV2.name.validator._redact = bv.BlotRedactor(None)
SerializedSkuContentV2.quota_gb.validator = bv.Float64()
SerializedSkuContentV2.quota_gb.validator._redact = bv.BlotRedactor(None)
SerializedSkuContentV2.sku_schedule.validator = bv.String()
SerializedSkuContentV2.sku_schedule.validator._redact = bv.BlotRedactor(None)
SerializedSkuContentV2.trademark_name_has_dropbox.validator = bv.Boolean()
SerializedSkuContentV2.trademark_name_has_dropbox.validator._redact = bv.BlotRedactor(None)
SerializedSkuContentV2.vacuuming_policy_max_days.validator = bv.Int64()
SerializedSkuContentV2.vacuuming_policy_max_days.validator._redact = bv.BlotRedactor(None)
SerializedSkuContentV2.sku_type.validator = cash_catalog_constants_stone.ProductPlanType_validator
SerializedSkuContentV2.sku_family.validator = cash_catalog_constants_stone.ProductFamily_validator
SerializedSkuContentV2._all_field_names_ = set([
    'display_brand_is_dropbox_business',
    'has_unlimited_space',
    'is_trial',
    'name',
    'quota_gb',
    'sku_schedule',
    'trademark_name_has_dropbox',
    'vacuuming_policy_max_days',
    'sku_type',
    'sku_family'])
SerializedSkuContentV2._all_fields_ = [
    ('display_brand_is_dropbox_business', SerializedSkuContentV2.display_brand_is_dropbox_business.validator),
    ('has_unlimited_space', SerializedSkuContentV2.has_unlimited_space.validator),
    ('is_trial', SerializedSkuContentV2.is_trial.validator),
    ('name', SerializedSkuContentV2.name.validator),
    ('quota_gb', SerializedSkuContentV2.quota_gb.validator),
    ('sku_schedule', SerializedSkuContentV2.sku_schedule.validator),
    ('trademark_name_has_dropbox', SerializedSkuContentV2.trademark_name_has_dropbox.validator),
    ('vacuuming_policy_max_days', SerializedSkuContentV2.vacuuming_policy_max_days.validator),
    ('sku_type', SerializedSkuContentV2.sku_type.validator),
    ('sku_family', SerializedSkuContentV2.sku_family.validator)]
SerializedSubStateContent.has_unlimited_space.validator = bv.Boolean()
SerializedSubStateContent.total_quota_gb.validator = bv.Nullable(bv.Float64())
SerializedSubStateContent.vacuuming_policy_max_days.validator = bv.Int64()
SerializedSubStateContent._all_field_names_ = set([
    'has_unlimited_space',
    'total_quota_gb',
    'vacuuming_policy_max_days'])
SerializedSubStateContent._all_fields_ = [
    ('has_unlimited_space', SerializedSubStateContent.has_unlimited_space.validator),
    ('total_quota_gb', SerializedSubStateContent.total_quota_gb.validator),
    ('vacuuming_policy_max_days', SerializedSubStateContent.vacuuming_policy_max_days.validator)]
TeamRootInfo.home_path.validator = bv.String()
TeamRootInfo._field_names_ = set([
    'home_path'])
TeamRootInfo._all_field_names_ = RootInfo._all_field_names_.union(TeamRootInfo._field_names_)
TeamRootInfo._fields_ = [
    ('home_path', TeamRootInfo.home_path.validator)]
TeamRootInfo._all_fields_ = RootInfo._all_fields_ + TeamRootInfo._fields_
UrlByProtocol.http_url.validator = bv.String()
UrlByProtocol.client_url.validator = bv.Nullable(bv.String())
UrlByProtocol._all_field_names_ = set([
    'http_url',
    'client_url'])
UrlByProtocol._all_fields_ = [
    ('http_url', UrlByProtocol.http_url.validator),
    ('client_url', UrlByProtocol.client_url.validator)]
UserRootInfo.home_path.validator = bv.Nullable(bv.String())
UserRootInfo._field_names_ = set([
    'home_path'])
UserRootInfo._all_field_names_ = RootInfo._all_field_names_.union(UserRootInfo._field_names_)
UserRootInfo._fields_ = [
    ('home_path', UserRootInfo.home_path.validator)]
UserRootInfo._all_fields_ = RootInfo._all_fields_ + UserRootInfo._fields_
ROUTES = { }
