# Source Generated with Decompyle++
# File: users.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account_id
from dropbox.api.v2.datatypes import common
from dropbox.api.v2.datatypes import premium_kit_assets
from dropbox.api.v2.datatypes import public_id
from dropbox.api.v2.datatypes import security_settings
from dropbox.api.v2.datatypes import store
from dropbox.api.v2.datatypes import storefront_platform
from dropbox.api.v2.datatypes import team_common
from dropbox.api.v2.datatypes import team_policies
from dropbox.api.v2.datatypes import users_common

class Account(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Account_validator = bv.Struct(Account)

class BasicAccount(Account):
    pass
# WARNING: Decompyle incomplete

BasicAccount_validator = bv.Struct(BasicAccount)

class BrandingInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BrandingInfo_validator = bv.Struct(BrandingInfo)

class BrandingVariant(bb.Union):
    pass
# WARNING: Decompyle incomplete

BrandingVariant_validator = bv.Union(BrandingVariant)

class CdmInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

CdmInfo_validator = bv.Struct(CdmInfo)

class DistinctMemberHomeValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

DistinctMemberHomeValue_validator = bv.Union(DistinctMemberHomeValue)

class DomainRestrictionInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

DomainRestrictionInfo_validator = bv.Struct(DomainRestrictionInfo)

class DomainRestrictionState(bb.Union):
    pass
# WARNING: Decompyle incomplete

DomainRestrictionState_validator = bv.Union(DomainRestrictionState)

class EnrollmentSource(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnrollmentSource_validator = bv.Union(EnrollmentSource)

class FamilyQuotaInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

FamilyQuotaInfo_validator = bv.Struct(FamilyQuotaInfo)

class FileLockingValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileLockingValue_validator = bv.Union(FileLockingValue)

class FullAccount(Account):
    pass
# WARNING: Decompyle incomplete

FullAccount_validator = bv.Struct(FullAccount)

class Team(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Team_validator = bv.Struct(Team)

class FullTeam(Team):
    pass
# WARNING: Decompyle incomplete

FullTeam_validator = bv.Struct(FullTeam)

class GetAccountArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetAccountArg_validator = bv.Struct(GetAccountArg)

class GetAccountBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetAccountBatchArg_validator = bv.Struct(GetAccountBatchArg)

class GetAccountBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetAccountBatchError_validator = bv.Union(GetAccountBatchError)

class GetAccountError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetAccountError_validator = bv.Union(GetAccountError)

class GetFileModifierAccountArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileModifierAccountArg_validator = bv.Struct(GetFileModifierAccountArg)

class GetFileModifierAccountError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileModifierAccountError_validator = bv.Union(GetFileModifierAccountError)

class GetLinkedUsersError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetLinkedUsersError_validator = bv.Union(GetLinkedUsersError)

class GetLinkedUsersRequest(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetLinkedUsersRequest_validator = bv.Struct(GetLinkedUsersRequest)

class GetLinkedUsersResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetLinkedUsersResult_validator = bv.Struct(GetLinkedUsersResult)

class GetPlanInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetPlanInfoArg_validator = bv.Struct(GetPlanInfoArg)

class GetPlanInfoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetPlanInfoError_validator = bv.Union(GetPlanInfoError)

class GetSharingPrefsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetSharingPrefsError_validator = bv.Union(GetSharingPrefsError)

class IndividualSpaceAllocation(bb.Struct):
    pass
# WARNING: Decompyle incomplete

IndividualSpaceAllocation_validator = bv.Struct(IndividualSpaceAllocation)

class InviteAfterSharingModalVariant(bb.Union):
    pass
# WARNING: Decompyle incomplete

InviteAfterSharingModalVariant_validator = bv.Union(InviteAfterSharingModalVariant)

class LinkedUserInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkedUserInfo_validator = bv.Struct(LinkedUserInfo)

class LinkedUserTeamInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkedUserTeamInfo_validator = bv.Struct(LinkedUserTeamInfo)

class MobileClientPlatform(bb.Union):
    pass
# WARNING: Decompyle incomplete

MobileClientPlatform_validator = bv.Union(MobileClientPlatform)

class Name(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Name_validator = bv.Struct(Name)

class PairUserArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PairUserArg_validator = bv.Struct(PairUserArg)

class PairUserError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PairUserError_validator = bv.Union(PairUserError)

class PaperAsFilesValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaperAsFilesValue_validator = bv.Union(PaperAsFilesValue)

class PlanInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PlanInfo_validator = bv.Struct(PlanInfo)

class PlanInfoV2(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PlanInfoV2_validator = bv.Struct(PlanInfoV2)

class PreviewsSharedLinkOpenOnDesktop(bb.Union):
    pass
# WARNING: Decompyle incomplete

PreviewsSharedLinkOpenOnDesktop_validator = bv.Union(PreviewsSharedLinkOpenOnDesktop)

class QuotaInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

QuotaInfo_validator = bv.Struct(QuotaInfo)

class ReferralBonusInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ReferralBonusInfo_validator = bv.Struct(ReferralBonusInfo)

class RootInfo(bb.Union):
    pass
# WARNING: Decompyle incomplete

RootInfo_validator = bv.Union(RootInfo)

class SaveMobileClientDeviceSettingsInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SaveMobileClientDeviceSettingsInfoArg_validator = bv.Struct(SaveMobileClientDeviceSettingsInfoArg)

class SaveMobileClientDeviceSettingsInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SaveMobileClientDeviceSettingsInfoResult_validator = bv.Struct(SaveMobileClientDeviceSettingsInfoResult)

class SaveMobileClientSettingsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SaveMobileClientSettingsError_validator = bv.Union(SaveMobileClientSettingsError)

class ScaleMitigationError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ScaleMitigationError_validator = bv.Union(ScaleMitigationError)

class ScaleMitigationReason(bb.Union):
    pass
# WARNING: Decompyle incomplete

ScaleMitigationReason_validator = bv.Union(ScaleMitigationReason)

class ScaleMitigationResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ScaleMitigationResult_validator = bv.Struct(ScaleMitigationResult)

class SetSharingPrefsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

SetSharingPrefsError_validator = bv.Union(SetSharingPrefsError)

class SharingAccessLevel(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharingAccessLevel_validator = bv.Union(SharingAccessLevel)

class SharingLinkAudience(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharingLinkAudience_validator = bv.Union(SharingLinkAudience)

class SharingPrefs(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SharingPrefs_validator = bv.Struct(SharingPrefs)

class SiblingUserInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SiblingUserInfo_validator = bv.Struct(SiblingUserInfo)

class SpaceAllocation(bb.Union):
    pass
# WARNING: Decompyle incomplete

SpaceAllocation_validator = bv.Union(SpaceAllocation)

class SpaceUsage(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SpaceUsage_validator = bv.Struct(SpaceUsage)

class SubscriptionInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubscriptionInfo_validator = bv.Struct(SubscriptionInfo)

class SubscriptionInfoDetails(bb.Struct):
    pass
# WARNING: Decompyle incomplete

SubscriptionInfoDetails_validator = bv.Struct(SubscriptionInfoDetails)

class TeamSharedDropboxValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

TeamSharedDropboxValue_validator = bv.Union(TeamSharedDropboxValue)

class TeamSpaceAllocation(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamSpaceAllocation_validator = bv.Struct(TeamSpaceAllocation)

class TeamUserPermissions(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamUserPermissions_validator = bv.Struct(TeamUserPermissions)

class TooManyFilesReason(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TooManyFilesReason_validator = bv.Struct(TooManyFilesReason)

class UsageUnit(bb.Union):
    pass
# WARNING: Decompyle incomplete

UsageUnit_validator = bv.Union(UsageUnit)

class UserAccountType(bb.Union):
    pass
# WARNING: Decompyle incomplete

UserAccountType_validator = bv.Union(UserAccountType)

class UserFeature(bb.Union):
    pass
# WARNING: Decompyle incomplete

UserFeature_validator = bv.Union(UserFeature)

class UserFeatureValue(bb.Union):
    pass
# WARNING: Decompyle incomplete

UserFeatureValue_validator = bv.Union(UserFeatureValue)

class UserFeaturesGetValuesBatchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserFeaturesGetValuesBatchArg_validator = bv.Struct(UserFeaturesGetValuesBatchArg)

class UserFeaturesGetValuesBatchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UserFeaturesGetValuesBatchError_validator = bv.Union(UserFeaturesGetValuesBatchError)

class UserFeaturesGetValuesBatchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserFeaturesGetValuesBatchResult_validator = bv.Struct(UserFeaturesGetValuesBatchResult)

class UserUsageUnit(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserUsageUnit_validator = bv.Struct(UserUsageUnit)
ExternalCustomerId_validator = bv.Bytes()
ExternalCustomerId_validator._redact = bv.BlotRedactor(None)
GetAccountBatchResult_validator = bv.List(BasicAccount_validator)
Account.account_id.validator = users_common.AccountId_validator
Account.name.validator = Name_validator
Account.email.validator = bv.String()
Account.email.validator._redact = bv.HashRedactor('^()(?:[^@]+)(@[^@]{1,2})(?:[^@]*)(\\.[^@\\.]+)$')
Account.email_verified.validator = bv.Boolean()
Account.profile_photo_url.validator = bv.Nullable(bv.String())
Account.profile_photo_url.validator._redact = bv.BlotRedactor(None)
Account.disabled.validator = bv.Boolean()
Account._all_field_names_ = set([
    'account_id',
    'name',
    'email',
    'email_verified',
    'profile_photo_url',
    'disabled'])
Account._all_fields_ = [
    ('account_id', Account.account_id.validator),
    ('name', Account.name.validator),
    ('email', Account.email.validator),
    ('email_verified', Account.email_verified.validator),
    ('profile_photo_url', Account.profile_photo_url.validator),
    ('disabled', Account.disabled.validator)]
BasicAccount.is_teammate.validator = bv.Boolean()
BasicAccount.team_member_id.validator = bv.Nullable(bv.String())
BasicAccount.is_suspended.validator = bv.Nullable(bv.Boolean())
BasicAccount._all_field_names_ = Account._all_field_names_.union(set([
    'is_teammate',
    'team_member_id']))
BasicAccount._all_fields_ = Account._all_fields_ + [
    ('is_teammate', BasicAccount.is_teammate.validator),
    ('team_member_id', BasicAccount.team_member_id.validator)]
BasicAccount._all_internal_field_names_ = set([
    'is_suspended'])
BasicAccount._all_internal_fields_ = [
    ('is_suspended', BasicAccount.is_suspended.validator)]
BrandingInfo.logo.validator = bv.Nullable(premium_kit_assets.Asset_validator)
BrandingInfo.background.validator = bv.Nullable(premium_kit_assets.Asset_validator)
BrandingInfo.variant.validator = bv.Nullable(BrandingVariant_validator)
BrandingInfo._all_field_names_ = set([
    'logo',
    'background',
    'variant'])
BrandingInfo._all_fields_ = [
    ('logo', BrandingInfo.logo.validator),
    ('background', BrandingInfo.background.validator),
    ('variant', BrandingInfo.variant.validator)]
BrandingVariant._not_enabled_validator = bv.Void()
BrandingVariant._try_pro_validator = bv.Void()
BrandingVariant._enabled_validator = bv.Void()
BrandingVariant._other_validator = bv.Void()
BrandingVariant._tagmap = {
    'not_enabled': BrandingVariant._not_enabled_validator,
    'try_pro': BrandingVariant._try_pro_validator,
    'enabled': BrandingVariant._enabled_validator,
    'other': BrandingVariant._other_validator }
BrandingVariant.not_enabled = BrandingVariant('not_enabled')
BrandingVariant.try_pro = BrandingVariant('try_pro')
BrandingVariant.enabled = BrandingVariant('enabled')
BrandingVariant.other = BrandingVariant('other')
CdmInfo.path_root.validator = bv.String()
CdmInfo.path_root.validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
CdmInfo.home_path.validator = bv.String()
CdmInfo.home_path.validator._redact = bv.HashRedactor('^(id:|ns:|rev:|/|)(?:.*)()$')
CdmInfo.home_ns_id.validator = bv.String()
CdmInfo._all_field_names_ = set([
    'path_root',
    'home_path',
    'home_ns_id'])
CdmInfo._all_fields_ = [
    ('path_root', CdmInfo.path_root.validator),
    ('home_path', CdmInfo.home_path.validator),
    ('home_ns_id', CdmInfo.home_ns_id.validator)]
DistinctMemberHomeValue._enabled_validator = bv.Boolean()
DistinctMemberHomeValue._other_validator = bv.Void()
DistinctMemberHomeValue._tagmap = {
    'enabled': DistinctMemberHomeValue._enabled_validator,
    'other': DistinctMemberHomeValue._other_validator }
DistinctMemberHomeValue.other = DistinctMemberHomeValue('other')
DomainRestrictionInfo.state.validator = bv.Nullable(DomainRestrictionState_validator)
DomainRestrictionInfo.enrollment_source.validator = bv.Nullable(EnrollmentSource_validator)
DomainRestrictionInfo.scheduled_capture_utc_ms.validator = bv.Nullable(bv.Int64())
DomainRestrictionInfo._all_field_names_ = set([
    'state',
    'enrollment_source',
    'scheduled_capture_utc_ms'])
DomainRestrictionInfo._all_fields_ = [
    ('state', DomainRestrictionInfo.state.validator),
    ('enrollment_source', DomainRestrictionInfo.enrollment_source.validator),
    ('scheduled_capture_utc_ms', DomainRestrictionInfo.scheduled_capture_utc_ms.validator)]
DomainRestrictionState._not_restricted_validator = bv.Void()
DomainRestrictionState._warning_validator = bv.Void()
DomainRestrictionState._captured_validator = bv.Void()
DomainRestrictionState._other_validator = bv.Void()
DomainRestrictionState._tagmap = {
    'not_restricted': DomainRestrictionState._not_restricted_validator,
    'warning': DomainRestrictionState._warning_validator,
    'captured': DomainRestrictionState._captured_validator,
    'other': DomainRestrictionState._other_validator }
DomainRestrictionState.not_restricted = DomainRestrictionState('not_restricted')
DomainRestrictionState.warning = DomainRestrictionState('warning')
DomainRestrictionState.captured = DomainRestrictionState('captured')
DomainRestrictionState.other = DomainRestrictionState('other')
EnrollmentSource._signup_validator = bv.Void()
EnrollmentSource._retroactive_validator = bv.Void()
EnrollmentSource._other_validator = bv.Void()
EnrollmentSource._tagmap = {
    'signup': EnrollmentSource._signup_validator,
    'retroactive': EnrollmentSource._retroactive_validator,
    'other': EnrollmentSource._other_validator }
EnrollmentSource.signup = EnrollmentSource('signup')
EnrollmentSource.retroactive = EnrollmentSource('retroactive')
EnrollmentSource.other = EnrollmentSource('other')
FamilyQuotaInfo.my_usage.validator = UsageUnit_validator
FamilyQuotaInfo.other_family_usages.validator = bv.List(UsageUnit_validator)
FamilyQuotaInfo.quota_in_bytes.validator = bv.UInt64()
FamilyQuotaInfo.quota_in_bytes.validator._redact = bv.BlotRedactor(None)
FamilyQuotaInfo._all_field_names_ = set([
    'my_usage',
    'other_family_usages',
    'quota_in_bytes'])
FamilyQuotaInfo._all_fields_ = [
    ('my_usage', FamilyQuotaInfo.my_usage.validator),
    ('other_family_usages', FamilyQuotaInfo.other_family_usages.validator),
    ('quota_in_bytes', FamilyQuotaInfo.quota_in_bytes.validator)]
FileLockingValue._enabled_validator = bv.Boolean()
FileLockingValue._other_validator = bv.Void()
FileLockingValue._tagmap = {
    'enabled': FileLockingValue._enabled_validator,
    'other': FileLockingValue._other_validator }
FileLockingValue.other = FileLockingValue('other')
FullAccount.country.validator = bv.Nullable(bv.String(min_length = 2, max_length = 2))
FullAccount.locale.validator = bv.String(min_length = 2)
FullAccount.referral_link.validator = bv.String()
FullAccount.team.validator = bv.Nullable(FullTeam_validator)
FullAccount.team_member_id.validator = bv.Nullable(bv.String())
FullAccount.is_paired.validator = bv.Boolean()
FullAccount.account_type.validator = users_common.AccountType_validator
FullAccount.root_info.validator = common.RootInfo_validator
FullAccount.uid.validator = bv.Int64()
FullAccount.uid.validator._redact = bv.BlotRedactor(None)
FullAccount.user_name.validator = bv.String()
FullAccount.user_name.validator._redact = bv.BlotRedactor(None)
FullAccount.can_share_folders_outside_team.validator = bv.Nullable(bv.String())
FullAccount.is_deferred_password.validator = bv.Boolean()
FullAccount.is_deferred_password.validator._redact = bv.BlotRedactor(None)
FullAccount.is_deferred_password_set.validator = bv.Boolean()
FullAccount.is_deferred_password_set.validator._redact = bv.BlotRedactor(None)
FullAccount.has_user_added_files.validator = bv.Boolean()
FullAccount.has_user_added_files.validator._redact = bv.BlotRedactor(None)
FullAccount.has_ever_linked_desktop.validator = bv.Boolean()
FullAccount.has_ever_linked_desktop.validator._redact = bv.BlotRedactor(None)
FullAccount.video_uploads_enabled_default.validator = bv.Boolean()
FullAccount.video_uploads_enabled_default.validator._redact = bv.BlotRedactor(None)
FullAccount.ios_last_deactivation_utc_ms.validator = bv.Nullable(bv.Int64())
FullAccount.is_paid.validator = bv.Boolean()
FullAccount.is_paid.validator._redact = bv.BlotRedactor(None)
FullAccount.uses_apple_relay_email.validator = bv.Boolean()
FullAccount.uses_apple_relay_email.validator._redact = bv.BlotRedactor(None)
FullAccount.pending_forced_migration.validator = bv.Boolean()
FullAccount.pending_forced_migration.validator._redact = bv.BlotRedactor(None)
FullAccount.referral_bonus_info.validator = ReferralBonusInfo_validator
FullAccount.sibling.validator = bv.Nullable(SiblingUserInfo_validator)
FullAccount.linked_users.validator = bv.List(SiblingUserInfo_validator)
FullAccount.visibility_quota_info.validator = QuotaInfo_validator
FullAccount.quota_info.validator = QuotaInfo_validator
FullAccount.home_path.validator = bv.Nullable(bv.String())
FullAccount.is_business_domain.validator = bv.Boolean()
FullAccount.is_business_domain.validator._redact = bv.BlotRedactor(None)
FullAccount.domain_restriction_state.validator = bv.Nullable(DomainRestrictionState_validator)
FullAccount.domain_restriction_scheduled_capture_utc_ms.validator = bv.Nullable(bv.Int64())
FullAccount.domain_restriction_info.validator = bv.Nullable(DomainRestrictionInfo_validator)
FullAccount.role.validator = bv.String()
FullAccount.role.validator._redact = bv.BlotRedactor(None)
FullAccount.linked_user_id.validator = bv.String()
FullAccount.linked_user_id.validator._redact = bv.BlotRedactor(None)
FullAccount.teams_member.validator = bv.Boolean()
FullAccount.teams_member.validator._redact = bv.BlotRedactor(None)
FullAccount.family_quota_info.validator = bv.Nullable(FamilyQuotaInfo_validator)
FullAccount.is_family_user.validator = bv.Nullable(bv.Boolean())
FullAccount.uses_sign_in_with_apple.validator = bv.Boolean()
FullAccount.uses_sign_in_with_apple.validator._redact = bv.BlotRedactor(None)
FullAccount.public_account_id.validator = bv.Nullable(ExternalCustomerId_validator)
FullAccount.twofactor_info.validator = bv.Nullable(security_settings.TwofactorInfo_validator)
FullAccount.domain_restriction_pending_email_verification.validator = bv.Nullable(bv.Boolean())
FullAccount.user_account_type.validator = bv.Nullable(UserAccountType_validator)
FullAccount.primary_account_user_id.validator = bv.Nullable(bv.Int64())
FullAccount.uses_sign_in_with_google.validator = bv.Boolean()
FullAccount.uses_sign_in_with_google.validator._redact = bv.BlotRedactor(None)
FullAccount.account_identity_id.validator = bv.Nullable(bv.Int64())
FullAccount._all_field_names_ = Account._all_field_names_.union(set([
    'country',
    'locale',
    'referral_link',
    'team',
    'team_member_id',
    'is_paired',
    'account_type',
    'root_info']))
FullAccount._all_fields_ = Account._all_fields_ + [
    ('country', FullAccount.country.validator),
    ('locale', FullAccount.locale.validator),
    ('referral_link', FullAccount.referral_link.validator),
    ('team', FullAccount.team.validator),
    ('team_member_id', FullAccount.team_member_id.validator),
    ('is_paired', FullAccount.is_paired.validator),
    ('account_type', FullAccount.account_type.validator),
    ('root_info', FullAccount.root_info.validator)]
FullAccount._all_internal_field_names_ = set([
    'uid',
    'user_name',
    'can_share_folders_outside_team',
    'is_deferred_password',
    'is_deferred_password_set',
    'has_user_added_files',
    'has_ever_linked_desktop',
    'video_uploads_enabled_default',
    'ios_last_deactivation_utc_ms',
    'is_paid',
    'uses_apple_relay_email',
    'pending_forced_migration',
    'referral_bonus_info',
    'sibling',
    'linked_users',
    'visibility_quota_info',
    'quota_info',
    'home_path',
    'is_business_domain',
    'domain_restriction_state',
    'domain_restriction_scheduled_capture_utc_ms',
    'domain_restriction_info',
    'role',
    'linked_user_id',
    'teams_member',
    'family_quota_info',
    'is_family_user',
    'uses_sign_in_with_apple',
    'public_account_id',
    'twofactor_info',
    'domain_restriction_pending_email_verification',
    'user_account_type',
    'primary_account_user_id',
    'uses_sign_in_with_google',
    'account_identity_id'])
FullAccount._all_internal_fields_ = [][('uid', FullAccount.uid.validator)][('user_name', FullAccount.user_name.validator)][('can_share_folders_outside_team', FullAccount.can_share_folders_outside_team.validator)][('is_deferred_password', FullAccount.is_deferred_password.validator)][('is_deferred_password_set', FullAccount.is_deferred_password_set.validator)][('has_user_added_files', FullAccount.has_user_added_files.validator)][('has_ever_linked_desktop', FullAccount.has_ever_linked_desktop.validator)][('video_uploads_enabled_default', FullAccount.video_uploads_enabled_default.validator)][('ios_last_deactivation_utc_ms', FullAccount.ios_last_deactivation_utc_ms.validator)][('is_paid', FullAccount.is_paid.validator)][('uses_apple_relay_email', FullAccount.uses_apple_relay_email.validator)][('pending_forced_migration', FullAccount.pending_forced_migration.validator)][('referral_bonus_info', FullAccount.referral_bonus_info.validator)][('sibling', FullAccount.sibling.validator)][('linked_users', FullAccount.linked_users.validator)][('visibility_quota_info', FullAccount.visibility_quota_info.validator)][('quota_info', FullAccount.quota_info.validator)][('home_path', FullAccount.home_path.validator)][('is_business_domain', FullAccount.is_business_domain.validator)][('domain_restriction_state', FullAccount.domain_restriction_state.validator)][('domain_restriction_scheduled_capture_utc_ms', FullAccount.domain_restriction_scheduled_capture_utc_ms.validator)][('domain_restriction_info', FullAccount.domain_restriction_info.validator)][('role', FullAccount.role.validator)][('linked_user_id', FullAccount.linked_user_id.validator)][('teams_member', FullAccount.teams_member.validator)][('family_quota_info', FullAccount.family_quota_info.validator)][('is_family_user', FullAccount.is_family_user.validator)][('uses_sign_in_with_apple', FullAccount.uses_sign_in_with_apple.validator)][('public_account_id', FullAccount.public_account_id.validator)][('twofactor_info', FullAccount.twofactor_info.validator)][('domain_restriction_pending_email_verification', FullAccount.domain_restriction_pending_email_verification.validator)][('user_account_type', FullAccount.user_account_type.validator)][('primary_account_user_id', FullAccount.primary_account_user_id.validator)][('uses_sign_in_with_google', FullAccount.uses_sign_in_with_google.validator)][('account_identity_id', FullAccount.account_identity_id.validator)]
Team.id.validator = bv.String()
Team.name.validator = bv.String()
Team._all_field_names_ = set([
    'id',
    'name'])
Team._all_fields_ = [
    ('id', Team.id.validator),
    ('name', Team.name.validator)]
FullTeam.sharing_policies.validator = team_policies.TeamSharingPolicies_validator
FullTeam.office_addin_policy.validator = team_policies.OfficeAddInPolicy_validator
FullTeam.top_level_content_policy.validator = team_policies.TopLevelContentPolicy_validator
FullTeam.is_locked_team.validator = bv.Boolean()
FullTeam.is_locked_team.validator._redact = bv.BlotRedactor(None)
FullTeam.locked_team_reason.validator = bv.String()
FullTeam.locked_team_reason.validator._redact = bv.BlotRedactor(None)
FullTeam.camera_uploads_policy.validator = team_policies.CameraUploadsPolicyState_validator
FullTeam.smarter_smart_sync_policy.validator = bv.Nullable(team_policies.SmarterSmartSyncPolicyState_validator)
FullTeam.file_locking_policy.validator = bv.Nullable(team_policies.FileLockingPolicyState_validator)
FullTeam.file_provider_migration_policy.validator = bv.Nullable(team_policies.FileProviderMigrationPolicyState_validator)
FullTeam.computer_backup_policy.validator = bv.Nullable(team_policies.ComputerBackupPolicyState_validator)
FullTeam.external_drive_backup_policy.validator = bv.Nullable(team_policies.ExternalDriveBackupPolicyState_validator)
FullTeam.sso_state.validator = bv.String()
FullTeam.sso_state.validator._redact = bv.BlotRedactor(None)
FullTeam.emm_state.validator = bv.String()
FullTeam.emm_state.validator._redact = bv.BlotRedactor(None)
FullTeam.is_limited.validator = bv.Boolean()
FullTeam.is_limited.validator._redact = bv.BlotRedactor(None)
FullTeam.path_root.validator = bv.Nullable(bv.String())
FullTeam.quota_info.validator = QuotaInfo_validator
FullTeam.msl_caps_type.validator = bv.String()
FullTeam.msl_caps_type.validator._redact = bv.BlotRedactor(None)
FullTeam.team_user_permissions.validator = TeamUserPermissions_validator
FullTeam.is_msl.validator = bv.Boolean()
FullTeam.is_msl.validator._redact = bv.BlotRedactor(None)
FullTeam.public_team_id.validator = bv.Nullable(ExternalCustomerId_validator)
FullTeam.team_logo_url.validator = bv.Nullable(bv.String())
FullTeam.member_count.validator = bv.Nullable(bv.UInt32())
FullTeam._all_field_names_ = Team._all_field_names_.union(set([
    'sharing_policies',
    'office_addin_policy',
    'top_level_content_policy']))
FullTeam._all_fields_ = Team._all_fields_ + [
    ('sharing_policies', FullTeam.sharing_policies.validator),
    ('office_addin_policy', FullTeam.office_addin_policy.validator),
    ('top_level_content_policy', FullTeam.top_level_content_policy.validator)]
FullTeam._all_internal_field_names_ = set([
    'is_locked_team',
    'locked_team_reason',
    'camera_uploads_policy',
    'smarter_smart_sync_policy',
    'file_locking_policy',
    'file_provider_migration_policy',
    'computer_backup_policy',
    'external_drive_backup_policy',
    'sso_state',
    'emm_state',
    'is_limited',
    'path_root',
    'quota_info',
    'msl_caps_type',
    'team_user_permissions',
    'is_msl',
    'public_team_id',
    'team_logo_url',
    'member_count'])
FullTeam._all_internal_fields_ = [
    ('is_locked_team', FullTeam.is_locked_team.validator),
    ('locked_team_reason', FullTeam.locked_team_reason.validator),
    ('camera_uploads_policy', FullTeam.camera_uploads_policy.validator),
    ('smarter_smart_sync_policy', FullTeam.smarter_smart_sync_policy.validator),
    ('file_locking_policy', FullTeam.file_locking_policy.validator),
    ('file_provider_migration_policy', FullTeam.file_provider_migration_policy.validator),
    ('computer_backup_policy', FullTeam.computer_backup_policy.validator),
    ('external_drive_backup_policy', FullTeam.external_drive_backup_policy.validator),
    ('sso_state', FullTeam.sso_state.validator),
    ('emm_state', FullTeam.emm_state.validator),
    ('is_limited', FullTeam.is_limited.validator),
    ('path_root', FullTeam.path_root.validator),
    ('quota_info', FullTeam.quota_info.validator),
    ('msl_caps_type', FullTeam.msl_caps_type.validator),
    ('team_user_permissions', FullTeam.team_user_permissions.validator),
    ('is_msl', FullTeam.is_msl.validator),
    ('public_team_id', FullTeam.public_team_id.validator),
    ('team_logo_url', FullTeam.team_logo_url.validator),
    ('member_count', FullTeam.member_count.validator)]
GetAccountArg.account_id.validator = users_common.AccountId_validator
GetAccountArg._all_field_names_ = set([
    'account_id'])
GetAccountArg._all_fields_ = [
    ('account_id', GetAccountArg.account_id.validator)]
GetAccountBatchArg.account_ids.validator = bv.List(users_common.AccountId_validator, min_items = 1)
GetAccountBatchArg._all_field_names_ = set([
    'account_ids'])
GetAccountBatchArg._all_fields_ = [
    ('account_ids', GetAccountBatchArg.account_ids.validator)]
GetAccountBatchError._no_account_validator = users_common.AccountId_validator
GetAccountBatchError._other_validator = bv.Void()
GetAccountBatchError._tagmap = {
    'no_account': GetAccountBatchError._no_account_validator,
    'other': GetAccountBatchError._other_validator }
GetAccountBatchError.other = GetAccountBatchError('other')
GetAccountError._no_account_validator = bv.Void()
GetAccountError._other_validator = bv.Void()
GetAccountError._tagmap = {
    'no_account': GetAccountError._no_account_validator,
    'other': GetAccountError._other_validator }
GetAccountError.no_account = GetAccountError('no_account')
GetAccountError.other = GetAccountError('other')
GetFileModifierAccountArg.user_id.validator = bv.Int64()
GetFileModifierAccountArg.file_id.validator = bv.String()
GetFileModifierAccountArg._all_field_names_ = set([
    'user_id',
    'file_id'])
GetFileModifierAccountArg._all_fields_ = [
    ('user_id', GetFileModifierAccountArg.user_id.validator),
    ('file_id', GetFileModifierAccountArg.file_id.validator)]
GetFileModifierAccountError._file_not_found_validator = bv.Void()
GetFileModifierAccountError._modifier_not_found_validator = bv.Void()
GetFileModifierAccountError._user_not_found_validator = bv.Void()
GetFileModifierAccountError._other_validator = bv.Void()
GetFileModifierAccountError._tagmap = {
    'file_not_found': GetFileModifierAccountError._file_not_found_validator,
    'modifier_not_found': GetFileModifierAccountError._modifier_not_found_validator,
    'user_not_found': GetFileModifierAccountError._user_not_found_validator,
    'other': GetFileModifierAccountError._other_validator }
GetFileModifierAccountError.file_not_found = GetFileModifierAccountError('file_not_found')
GetFileModifierAccountError.modifier_not_found = GetFileModifierAccountError('modifier_not_found')
GetFileModifierAccountError.user_not_found = GetFileModifierAccountError('user_not_found')
GetFileModifierAccountError.other = GetFileModifierAccountError('other')
GetLinkedUsersError._other_validator = bv.Void()
GetLinkedUsersError._tagmap = {
    'other': GetLinkedUsersError._other_validator }
GetLinkedUsersError.other = GetLinkedUsersError('other')
GetLinkedUsersRequest._all_field_names_ = set([])
GetLinkedUsersRequest._all_fields_ = []
GetLinkedUsersResult.linked_users.validator = bv.List(LinkedUserInfo_validator)
GetLinkedUsersResult._all_field_names_ = set([
    'linked_users'])
GetLinkedUsersResult._all_fields_ = [
    ('linked_users', GetLinkedUsersResult.linked_users.validator)]
GetPlanInfoArg.account_id.validator = users_common.AccountId_validator
GetPlanInfoArg.get_renew_status.validator = bv.Nullable(bv.Boolean())
GetPlanInfoArg.get_subscription_info.validator = bv.Nullable(bv.Boolean())
GetPlanInfoArg._all_field_names_ = set([
    'account_id',
    'get_renew_status',
    'get_subscription_info'])
GetPlanInfoArg._all_fields_ = [
    ('account_id', GetPlanInfoArg.account_id.validator),
    ('get_renew_status', GetPlanInfoArg.get_renew_status.validator),
    ('get_subscription_info', GetPlanInfoArg.get_subscription_info.validator)]
GetPlanInfoError._no_account_validator = bv.Void()
GetPlanInfoError._v2_user_validator = bv.Void()
GetPlanInfoError._other_validator = bv.Void()
GetPlanInfoError._tagmap = {
    'no_account': GetPlanInfoError._no_account_validator,
    'v2_user': GetPlanInfoError._v2_user_validator,
    'other': GetPlanInfoError._other_validator }
GetPlanInfoError.no_account = GetPlanInfoError('no_account')
GetPlanInfoError.v2_user = GetPlanInfoError('v2_user')
GetPlanInfoError.other = GetPlanInfoError('other')
GetSharingPrefsError._invalid_pref_value_validator = bv.Void()
GetSharingPrefsError._other_validator = bv.Void()
GetSharingPrefsError._tagmap = {
    'invalid_pref_value': GetSharingPrefsError._invalid_pref_value_validator,
    'other': GetSharingPrefsError._other_validator }
GetSharingPrefsError.invalid_pref_value = GetSharingPrefsError('invalid_pref_value')
GetSharingPrefsError.other = GetSharingPrefsError('other')
IndividualSpaceAllocation.allocated.validator = bv.UInt64()
IndividualSpaceAllocation._all_field_names_ = set([
    'allocated'])
IndividualSpaceAllocation._all_fields_ = [
    ('allocated', IndividualSpaceAllocation.allocated.validator)]
InviteAfterSharingModalVariant._not_enabled_validator = bv.Void()
InviteAfterSharingModalVariant._admin_invite_expand_eligibility_validator = bv.Void()
InviteAfterSharingModalVariant._member_suggestion_expand_eligibility_validator = bv.Void()
InviteAfterSharingModalVariant._member_invite_expand_eligibility_validator = bv.Void()
InviteAfterSharingModalVariant._member_invite_partial_eligibility_validator = bv.Void()
InviteAfterSharingModalVariant._other_validator = bv.Void()
InviteAfterSharingModalVariant._tagmap = {
    'not_enabled': InviteAfterSharingModalVariant._not_enabled_validator,
    'admin_invite_expand_eligibility': InviteAfterSharingModalVariant._admin_invite_expand_eligibility_validator,
    'member_suggestion_expand_eligibility': InviteAfterSharingModalVariant._member_suggestion_expand_eligibility_validator,
    'member_invite_expand_eligibility': InviteAfterSharingModalVariant._member_invite_expand_eligibility_validator,
    'member_invite_partial_eligibility': InviteAfterSharingModalVariant._member_invite_partial_eligibility_validator,
    'other': InviteAfterSharingModalVariant._other_validator }
InviteAfterSharingModalVariant.not_enabled = InviteAfterSharingModalVariant('not_enabled')
InviteAfterSharingModalVariant.admin_invite_expand_eligibility = InviteAfterSharingModalVariant('admin_invite_expand_eligibility')
InviteAfterSharingModalVariant.member_suggestion_expand_eligibility = InviteAfterSharingModalVariant('member_suggestion_expand_eligibility')
InviteAfterSharingModalVariant.member_invite_expand_eligibility = InviteAfterSharingModalVariant('member_invite_expand_eligibility')
InviteAfterSharingModalVariant.member_invite_partial_eligibility = InviteAfterSharingModalVariant('member_invite_partial_eligibility')
InviteAfterSharingModalVariant.other = InviteAfterSharingModalVariant('other')
LinkedUserInfo.uid.validator = bv.Int64()
LinkedUserInfo.account_id.validator = bv.String()
LinkedUserInfo.email.validator = bv.String()
LinkedUserInfo.email.validator._redact = bv.HashRedactor('^()(?:[^@]+)(@[^@]{1,2})(?:[^@]*)(\\.[^@\\.]+)$')
LinkedUserInfo.email_verified.validator = bv.Boolean()
LinkedUserInfo.role.validator = bv.String()
LinkedUserInfo.linked_user_id.validator = bv.String()
LinkedUserInfo.name.validator = Name_validator
LinkedUserInfo.team.validator = bv.Nullable(LinkedUserTeamInfo_validator)
LinkedUserInfo._all_field_names_ = set([
    'uid',
    'account_id',
    'email',
    'email_verified',
    'role',
    'linked_user_id',
    'name',
    'team'])
LinkedUserInfo._all_fields_ = [
    ('uid', LinkedUserInfo.uid.validator),
    ('account_id', LinkedUserInfo.account_id.validator),
    ('email', LinkedUserInfo.email.validator),
    ('email_verified', LinkedUserInfo.email_verified.validator),
    ('role', LinkedUserInfo.role.validator),
    ('linked_user_id', LinkedUserInfo.linked_user_id.validator),
    ('name', LinkedUserInfo.name.validator),
    ('team', LinkedUserInfo.team.validator)]
LinkedUserTeamInfo.id.validator = bv.Int64()
LinkedUserTeamInfo.name.validator = bv.Nullable(bv.String())
LinkedUserTeamInfo._all_field_names_ = set([
    'id',
    'name'])
LinkedUserTeamInfo._all_fields_ = [
    ('id', LinkedUserTeamInfo.id.validator),
    ('name', LinkedUserTeamInfo.name.validator)]
MobileClientPlatform._ios_validator = bv.Void()
MobileClientPlatform._android_validator = bv.Void()
MobileClientPlatform._windows_validator = bv.Void()
MobileClientPlatform._other_validator = bv.Void()
MobileClientPlatform._tagmap = {
    'ios': MobileClientPlatform._ios_validator,
    'android': MobileClientPlatform._android_validator,
    'windows': MobileClientPlatform._windows_validator,
    'other': MobileClientPlatform._other_validator }
MobileClientPlatform.ios = MobileClientPlatform('ios')
MobileClientPlatform.android = MobileClientPlatform('android')
MobileClientPlatform.windows = MobileClientPlatform('windows')
MobileClientPlatform.other = MobileClientPlatform('other')
Name.given_name.validator = bv.String()
Name.given_name.validator._redact = bv.BlotRedactor(None)
Name.surname.validator = bv.String()
Name.surname.validator._redact = bv.BlotRedactor(None)
Name.familiar_name.validator = bv.String()
Name.familiar_name.validator._redact = bv.BlotRedactor(None)
Name.display_name.validator = bv.String()
Name.display_name.validator._redact = bv.BlotRedactor(None)
Name.abbreviated_name.validator = bv.String()
Name.abbreviated_name.validator._redact = bv.BlotRedactor(None)
Name._all_field_names_ = set([
    'given_name',
    'surname',
    'familiar_name',
    'display_name',
    'abbreviated_name'])
Name._all_fields_ = [
    ('given_name', Name.given_name.validator),
    ('surname', Name.surname.validator),
    ('familiar_name', Name.familiar_name.validator),
    ('display_name', Name.display_name.validator),
    ('abbreviated_name', Name.abbreviated_name.validator)]
PairUserArg.checkpoint_token.validator = bv.String()
PairUserArg._all_field_names_ = set([
    'checkpoint_token'])
PairUserArg._all_fields_ = [
    ('checkpoint_token', PairUserArg.checkpoint_token.validator)]
PairUserError._invalid_checkpoint_token_validator = bv.Void()
PairUserError._invalid_pairing_validator = bv.Void()
PairUserError._invalid_credentials_validator = bv.Void()
PairUserError._other_validator = bv.Void()
PairUserError._tagmap = {
    'invalid_checkpoint_token': PairUserError._invalid_checkpoint_token_validator,
    'invalid_pairing': PairUserError._invalid_pairing_validator,
    'invalid_credentials': PairUserError._invalid_credentials_validator,
    'other': PairUserError._other_validator }
PairUserError.invalid_checkpoint_token = PairUserError('invalid_checkpoint_token')
PairUserError.invalid_pairing = PairUserError('invalid_pairing')
PairUserError.invalid_credentials = PairUserError('invalid_credentials')
PairUserError.other = PairUserError('other')
PaperAsFilesValue._enabled_validator = bv.Boolean()
PaperAsFilesValue._other_validator = bv.Void()
PaperAsFilesValue._tagmap = {
    'enabled': PaperAsFilesValue._enabled_validator,
    'other': PaperAsFilesValue._other_validator }
PaperAsFilesValue.other = PaperAsFilesValue('other')
PlanInfo.account_id.validator = users_common.AccountId_validator
PlanInfo.account_type.validator = users_common.AccountType_validator
PlanInfo.plan_text.validator = bv.String()
PlanInfo.plan_text.validator._redact = bv.BlotRedactor(None)
PlanInfo.plan_detail_text.validator = bv.Nullable(bv.String())
PlanInfo.has_scheduled_plan.validator = bv.Nullable(bv.Boolean())
PlanInfo.is_trial.validator = bv.Nullable(bv.Boolean())
PlanInfo.serialized_sku_content.validator = common.SerializedSkuContent_validator
PlanInfo._all_field_names_ = set([
    'account_id',
    'account_type',
    'plan_text',
    'plan_detail_text',
    'has_scheduled_plan',
    'is_trial',
    'serialized_sku_content'])
PlanInfo._all_fields_ = [
    ('account_id', PlanInfo.account_id.validator),
    ('account_type', PlanInfo.account_type.validator),
    ('plan_text', PlanInfo.plan_text.validator),
    ('plan_detail_text', PlanInfo.plan_detail_text.validator),
    ('has_scheduled_plan', PlanInfo.has_scheduled_plan.validator),
    ('is_trial', PlanInfo.is_trial.validator),
    ('serialized_sku_content', PlanInfo.serialized_sku_content.validator)]
PlanInfoV2.account_id.validator = users_common.AccountId_validator
PlanInfoV2.account_type.validator = users_common.AccountType_validator
PlanInfoV2.plan_text.validator = bv.String()
PlanInfoV2.plan_text.validator._redact = bv.BlotRedactor(None)
PlanInfoV2.plan_detail_text.validator = bv.Nullable(bv.String())
PlanInfoV2.has_scheduled_plan.validator = bv.Nullable(bv.Boolean())
PlanInfoV2.is_trial.validator = bv.Nullable(bv.Boolean())
PlanInfoV2.serialized_sku_content.validator = common.SerializedSkuContentV2_validator
PlanInfoV2.subscriptions.validator = bv.Nullable(bv.List(SubscriptionInfo_validator))
PlanInfoV2.is_trial_eligible_ios.validator = bv.Boolean()
PlanInfoV2.is_trial_eligible_ios.validator._redact = bv.BlotRedactor(None)
PlanInfoV2._all_field_names_ = set([
    'account_id',
    'account_type',
    'plan_text',
    'plan_detail_text',
    'has_scheduled_plan',
    'is_trial',
    'serialized_sku_content',
    'subscriptions',
    'is_trial_eligible_ios'])
PlanInfoV2._all_fields_ = [
    ('account_id', PlanInfoV2.account_id.validator),
    ('account_type', PlanInfoV2.account_type.validator),
    ('plan_text', PlanInfoV2.plan_text.validator),
    ('plan_detail_text', PlanInfoV2.plan_detail_text.validator),
    ('has_scheduled_plan', PlanInfoV2.has_scheduled_plan.validator),
    ('is_trial', PlanInfoV2.is_trial.validator),
    ('serialized_sku_content', PlanInfoV2.serialized_sku_content.validator),
    ('subscriptions', PlanInfoV2.subscriptions.validator),
    ('is_trial_eligible_ios', PlanInfoV2.is_trial_eligible_ios.validator)]
PreviewsSharedLinkOpenOnDesktop._off_validator = bv.Void()
PreviewsSharedLinkOpenOnDesktop._on_validator = bv.Void()
PreviewsSharedLinkOpenOnDesktop._other_validator = bv.Void()
PreviewsSharedLinkOpenOnDesktop._tagmap = {
    'off': PreviewsSharedLinkOpenOnDesktop._off_validator,
    'on': PreviewsSharedLinkOpenOnDesktop._on_validator,
    'other': PreviewsSharedLinkOpenOnDesktop._other_validator }
PreviewsSharedLinkOpenOnDesktop.off = PreviewsSharedLinkOpenOnDesktop('off')
PreviewsSharedLinkOpenOnDesktop.on = PreviewsSharedLinkOpenOnDesktop('on')
PreviewsSharedLinkOpenOnDesktop.other = PreviewsSharedLinkOpenOnDesktop('other')
QuotaInfo.normal.validator = bv.Int64()
QuotaInfo.shared.validator = bv.Int64()
QuotaInfo.quota.validator = bv.Int64()
QuotaInfo._all_field_names_ = set([
    'normal',
    'shared',
    'quota'])
QuotaInfo._all_fields_ = [
    ('normal', QuotaInfo.normal.validator),
    ('shared', QuotaInfo.shared.validator),
    ('quota', QuotaInfo.quota.validator)]
ReferralBonusInfo.bonus_space.validator = bv.Int64()
ReferralBonusInfo.max_num_bonus.validator = bv.Int64()
ReferralBonusInfo._all_field_names_ = set([
    'bonus_space',
    'max_num_bonus'])
ReferralBonusInfo._all_fields_ = [
    ('bonus_space', ReferralBonusInfo.bonus_space.validator),
    ('max_num_bonus', ReferralBonusInfo.max_num_bonus.validator)]
RootInfo._cdm_team_validator = CdmInfo_validator
RootInfo._not_on_cdm_team_validator = bv.String()
RootInfo._other_validator = bv.Void()
RootInfo._tagmap = {
    'cdm_team': RootInfo._cdm_team_validator,
    'not_on_cdm_team': RootInfo._not_on_cdm_team_validator,
    'other': RootInfo._other_validator }
RootInfo.other = RootInfo('other')
SaveMobileClientDeviceSettingsInfoArg.user_id.validator = bv.String()
SaveMobileClientDeviceSettingsInfoArg.setting_type.validator = bv.String()
SaveMobileClientDeviceSettingsInfoArg.settings.validator = bv.Map(bv.String(), bv.String())
SaveMobileClientDeviceSettingsInfoArg.mobile_client_platform.validator = MobileClientPlatform_validator
SaveMobileClientDeviceSettingsInfoArg.device_id.validator = bv.String()
SaveMobileClientDeviceSettingsInfoArg.device_name.validator = bv.String()
SaveMobileClientDeviceSettingsInfoArg._all_field_names_ = set([
    'user_id',
    'setting_type',
    'settings',
    'mobile_client_platform',
    'device_id',
    'device_name'])
SaveMobileClientDeviceSettingsInfoArg._all_fields_ = [
    ('user_id', SaveMobileClientDeviceSettingsInfoArg.user_id.validator),
    ('setting_type', SaveMobileClientDeviceSettingsInfoArg.setting_type.validator),
    ('settings', SaveMobileClientDeviceSettingsInfoArg.settings.validator),
    ('mobile_client_platform', SaveMobileClientDeviceSettingsInfoArg.mobile_client_platform.validator),
    ('device_id', SaveMobileClientDeviceSettingsInfoArg.device_id.validator),
    ('device_name', SaveMobileClientDeviceSettingsInfoArg.device_name.validator)]
SaveMobileClientDeviceSettingsInfoResult._all_field_names_ = set([])
SaveMobileClientDeviceSettingsInfoResult._all_fields_ = []
SaveMobileClientSettingsError._setting_name_or_value_too_long_validator = bv.Void()
SaveMobileClientSettingsError._no_such_user_validator = bv.Void()
SaveMobileClientSettingsError._too_many_settings_validator = bv.Void()
SaveMobileClientSettingsError._unknown_setting_type_validator = bv.Void()
SaveMobileClientSettingsError._other_validator = bv.Void()
SaveMobileClientSettingsError._tagmap = {
    'setting_name_or_value_too_long': SaveMobileClientSettingsError._setting_name_or_value_too_long_validator,
    'no_such_user': SaveMobileClientSettingsError._no_such_user_validator,
    'too_many_settings': SaveMobileClientSettingsError._too_many_settings_validator,
    'unknown_setting_type': SaveMobileClientSettingsError._unknown_setting_type_validator,
    'other': SaveMobileClientSettingsError._other_validator }
SaveMobileClientSettingsError.setting_name_or_value_too_long = SaveMobileClientSettingsError('setting_name_or_value_too_long')
SaveMobileClientSettingsError.no_such_user = SaveMobileClientSettingsError('no_such_user')
SaveMobileClientSettingsError.too_many_settings = SaveMobileClientSettingsError('too_many_settings')
SaveMobileClientSettingsError.unknown_setting_type = SaveMobileClientSettingsError('unknown_setting_type')
SaveMobileClientSettingsError.other = SaveMobileClientSettingsError('other')
ScaleMitigationError._other_validator = bv.Void()
ScaleMitigationError._tagmap = {
    'other': ScaleMitigationError._other_validator }
ScaleMitigationError.other = ScaleMitigationError('other')
ScaleMitigationReason._too_many_files_validator = TooManyFilesReason_validator
ScaleMitigationReason._other_validator = bv.Void()
ScaleMitigationReason._tagmap = {
    'too_many_files': ScaleMitigationReason._too_many_files_validator,
    'other': ScaleMitigationReason._other_validator }
ScaleMitigationReason.other = ScaleMitigationReason('other')
ScaleMitigationResult.needs_scale_mitigation.validator = bv.Boolean()
ScaleMitigationResult.reason.validator = bv.Nullable(ScaleMitigationReason_validator)
ScaleMitigationResult._all_field_names_ = set([
    'needs_scale_mitigation',
    'reason'])
ScaleMitigationResult._all_fields_ = [
    ('needs_scale_mitigation', ScaleMitigationResult.needs_scale_mitigation.validator),
    ('reason', ScaleMitigationResult.reason.validator)]
SetSharingPrefsError._invalid_pref_value_validator = bv.Void()
SetSharingPrefsError._user_not_gated_validator = bv.Void()
SetSharingPrefsError._other_validator = bv.Void()
SetSharingPrefsError._tagmap = {
    'invalid_pref_value': SetSharingPrefsError._invalid_pref_value_validator,
    'user_not_gated': SetSharingPrefsError._user_not_gated_validator,
    'other': SetSharingPrefsError._other_validator }
SetSharingPrefsError.invalid_pref_value = SetSharingPrefsError('invalid_pref_value')
SetSharingPrefsError.user_not_gated = SetSharingPrefsError('user_not_gated')
SetSharingPrefsError.other = SetSharingPrefsError('other')
SharingAccessLevel._unknown_validator = bv.Void()
SharingAccessLevel._edit_validator = bv.Void()
SharingAccessLevel._view_validator = bv.Void()
SharingAccessLevel._other_validator = bv.Void()
SharingAccessLevel._tagmap = {
    'unknown': SharingAccessLevel._unknown_validator,
    'edit': SharingAccessLevel._edit_validator,
    'view': SharingAccessLevel._view_validator,
    'other': SharingAccessLevel._other_validator }
SharingAccessLevel.unknown = SharingAccessLevel('unknown')
SharingAccessLevel.edit = SharingAccessLevel('edit')
SharingAccessLevel.view = SharingAccessLevel('view')
SharingAccessLevel.other = SharingAccessLevel('other')
SharingLinkAudience._unknown_validator = bv.Void()
SharingLinkAudience._public_validator = bv.Void()
SharingLinkAudience._no_one_validator = bv.Void()
SharingLinkAudience._team_validator = bv.Void()
SharingLinkAudience._other_validator = bv.Void()
SharingLinkAudience._tagmap = {
    'unknown': SharingLinkAudience._unknown_validator,
    'public': SharingLinkAudience._public_validator,
    'no_one': SharingLinkAudience._no_one_validator,
    'team': SharingLinkAudience._team_validator,
    'other': SharingLinkAudience._other_validator }
SharingLinkAudience.unknown = SharingLinkAudience('unknown')
SharingLinkAudience.public = SharingLinkAudience('public')
SharingLinkAudience.no_one = SharingLinkAudience('no_one')
SharingLinkAudience.team = SharingLinkAudience('team')
SharingLinkAudience.other = SharingLinkAudience('other')
SharingPrefs.invite_after_sharing_modal_variant.validator = bv.Nullable(InviteAfterSharingModalVariant_validator)
SharingPrefs.has_seen_esign_post_sharing.validator = bv.Nullable(bv.Boolean())
SharingPrefs.links_in_member_list_in_sdk_share_modal_variant.validator = bv.Nullable(bv.String())
SharingPrefs.is_in_esign_post_sharing_exclusion_period.validator = bv.Nullable(bv.Boolean())
SharingPrefs.bsx_organize_around_people.validator = bv.Nullable(bv.Boolean())
SharingPrefs.branding_info.validator = bv.Nullable(BrandingInfo_validator)
SharingPrefs.is_showing_file_upload_toolkit_campaign.validator = bv.Nullable(bv.Boolean())
SharingPrefs.product_business.validator = bv.Nullable(bv.String())
SharingPrefs.product_professional.validator = bv.Nullable(bv.String())
SharingPrefs.product_essentials.validator = bv.Nullable(bv.String())
SharingPrefs.product_standard.validator = bv.Nullable(bv.String())
SharingPrefs.default_sharing_access_level_setting.validator = bv.Nullable(SharingAccessLevel_validator)
SharingPrefs.default_sharing_link_audience_setting.validator = bv.Nullable(SharingLinkAudience_validator)
SharingPrefs.default_previews_shared_link_open_on_desktop_setting.validator = bv.Nullable(PreviewsSharedLinkOpenOnDesktop_validator)
SharingPrefs.last_seen_team_policy_audience.validator = bv.Nullable(SharingLinkAudience_validator)
SharingPrefs.is_file_transfer_enabled.validator = bv.Nullable(bv.Boolean())
SharingPrefs.core_act_docsend_advanced_sharing.validator = bv.Nullable(bv.String())
SharingPrefs.is_basic_user.validator = bv.Nullable(bv.Boolean())
SharingPrefs.is_replay_in_share_modal_enabled.validator = bv.Nullable(bv.Boolean())
SharingPrefs.num_available_licenses.validator = bv.Nullable(bv.Int64())
SharingPrefs.should_auto_show_link_settings_tooltip.validator = bv.Nullable(bv.Boolean())
SharingPrefs.tmr_tf_share_link_exp.validator = bv.Nullable(bv.Boolean())
SharingPrefs.logged_out_commenting_enabled.validator = bv.Nullable(bv.Boolean())
SharingPrefs.logged_out_commenting_variant.validator = bv.Nullable(bv.String())
SharingPrefs.should_reduce_upsells_churn_analysis.validator = bv.Nullable(bv.Boolean())
SharingPrefs.post_share_magnet_variant.validator = bv.Nullable(bv.String())
SharingPrefs.post_share_magnet_access_m1_variant.validator = bv.Nullable(bv.String())
SharingPrefs._all_field_names_ = set([
    'invite_after_sharing_modal_variant',
    'has_seen_esign_post_sharing',
    'links_in_member_list_in_sdk_share_modal_variant',
    'is_in_esign_post_sharing_exclusion_period',
    'bsx_organize_around_people',
    'branding_info',
    'is_showing_file_upload_toolkit_campaign',
    'product_business',
    'product_professional',
    'product_essentials',
    'product_standard',
    'default_sharing_access_level_setting',
    'default_sharing_link_audience_setting',
    'default_previews_shared_link_open_on_desktop_setting',
    'last_seen_team_policy_audience',
    'is_file_transfer_enabled',
    'core_act_docsend_advanced_sharing',
    'is_basic_user',
    'is_replay_in_share_modal_enabled',
    'num_available_licenses',
    'should_auto_show_link_settings_tooltip',
    'tmr_tf_share_link_exp',
    'logged_out_commenting_enabled',
    'logged_out_commenting_variant',
    'should_reduce_upsells_churn_analysis',
    'post_share_magnet_variant',
    'post_share_magnet_access_m1_variant'])
SharingPrefs._all_fields_ = [
    ('invite_after_sharing_modal_variant', SharingPrefs.invite_after_sharing_modal_variant.validator),
    ('has_seen_esign_post_sharing', SharingPrefs.has_seen_esign_post_sharing.validator),
    ('links_in_member_list_in_sdk_share_modal_variant', SharingPrefs.links_in_member_list_in_sdk_share_modal_variant.validator),
    ('is_in_esign_post_sharing_exclusion_period', SharingPrefs.is_in_esign_post_sharing_exclusion_period.validator),
    ('bsx_organize_around_people', SharingPrefs.bsx_organize_around_people.validator),
    ('branding_info', SharingPrefs.branding_info.validator),
    ('is_showing_file_upload_toolkit_campaign', SharingPrefs.is_showing_file_upload_toolkit_campaign.validator),
    ('product_business', SharingPrefs.product_business.validator),
    ('product_professional', SharingPrefs.product_professional.validator),
    ('product_essentials', SharingPrefs.product_essentials.validator),
    ('product_standard', SharingPrefs.product_standard.validator),
    ('default_sharing_access_level_setting', SharingPrefs.default_sharing_access_level_setting.validator),
    ('default_sharing_link_audience_setting', SharingPrefs.default_sharing_link_audience_setting.validator),
    ('default_previews_shared_link_open_on_desktop_setting', SharingPrefs.default_previews_shared_link_open_on_desktop_setting.validator),
    ('last_seen_team_policy_audience', SharingPrefs.last_seen_team_policy_audience.validator),
    ('is_file_transfer_enabled', SharingPrefs.is_file_transfer_enabled.validator),
    ('core_act_docsend_advanced_sharing', SharingPrefs.core_act_docsend_advanced_sharing.validator),
    ('is_basic_user', SharingPrefs.is_basic_user.validator),
    ('is_replay_in_share_modal_enabled', SharingPrefs.is_replay_in_share_modal_enabled.validator),
    ('num_available_licenses', SharingPrefs.num_available_licenses.validator),
    ('should_auto_show_link_settings_tooltip', SharingPrefs.should_auto_show_link_settings_tooltip.validator),
    ('tmr_tf_share_link_exp', SharingPrefs.tmr_tf_share_link_exp.validator),
    ('logged_out_commenting_enabled', SharingPrefs.logged_out_commenting_enabled.validator),
    ('logged_out_commenting_variant', SharingPrefs.logged_out_commenting_variant.validator),
    ('should_reduce_upsells_churn_analysis', SharingPrefs.should_reduce_upsells_churn_analysis.validator),
    ('post_share_magnet_variant', SharingPrefs.post_share_magnet_variant.validator),
    ('post_share_magnet_access_m1_variant', SharingPrefs.post_share_magnet_access_m1_variant.validator)]
SiblingUserInfo.uid.validator = bv.Int64()
SiblingUserInfo.email.validator = bv.String()
SiblingUserInfo.email.validator._redact = bv.HashRedactor('^()(?:[^@]+)(@[^@]{1,2})(?:[^@]*)(\\.[^@\\.]+)$')
SiblingUserInfo.role.validator = bv.String()
SiblingUserInfo.linked_user_id.validator = bv.String()
SiblingUserInfo.user_account_type.validator = bv.Nullable(UserAccountType_validator)
SiblingUserInfo.primary_account_user_id.validator = bv.Nullable(bv.Int64())
SiblingUserInfo.team_name.validator = bv.Nullable(bv.String())
SiblingUserInfo.team_logo_url.validator = bv.Nullable(bv.String())
SiblingUserInfo.member_count.validator = bv.Nullable(bv.UInt32())
SiblingUserInfo.account_identity_id.validator = bv.Nullable(bv.Int64())
SiblingUserInfo._all_field_names_ = set([
    'uid',
    'email',
    'role',
    'linked_user_id',
    'user_account_type',
    'primary_account_user_id',
    'team_name',
    'team_logo_url',
    'member_count',
    'account_identity_id'])
SiblingUserInfo._all_fields_ = [
    ('uid', SiblingUserInfo.uid.validator),
    ('email', SiblingUserInfo.email.validator),
    ('role', SiblingUserInfo.role.validator),
    ('linked_user_id', SiblingUserInfo.linked_user_id.validator),
    ('user_account_type', SiblingUserInfo.user_account_type.validator),
    ('primary_account_user_id', SiblingUserInfo.primary_account_user_id.validator),
    ('team_name', SiblingUserInfo.team_name.validator),
    ('team_logo_url', SiblingUserInfo.team_logo_url.validator),
    ('member_count', SiblingUserInfo.member_count.validator),
    ('account_identity_id', SiblingUserInfo.account_identity_id.validator)]
SpaceAllocation._individual_validator = IndividualSpaceAllocation_validator
SpaceAllocation._team_validator = TeamSpaceAllocation_validator
SpaceAllocation._other_validator = bv.Void()
SpaceAllocation._tagmap = {
    'individual': SpaceAllocation._individual_validator,
    'team': SpaceAllocation._team_validator,
    'other': SpaceAllocation._other_validator }
SpaceAllocation.other = SpaceAllocation('other')
SpaceUsage.used.validator = bv.UInt64()
SpaceUsage.allocation.validator = SpaceAllocation_validator
SpaceUsage._all_field_names_ = set([
    'used',
    'allocation'])
SpaceUsage._all_fields_ = [
    ('used', SpaceUsage.used.validator),
    ('allocation', SpaceUsage.allocation.validator)]
SubscriptionInfo.subscription_type.validator = storefront_platform.StorefrontPlatformProductLine_validator
SubscriptionInfo.active.validator = bv.Nullable(SubscriptionInfoDetails_validator)
SubscriptionInfo.previous.validator = bv.Nullable(SubscriptionInfoDetails_validator)
SubscriptionInfo.scheduled.validator = bv.Nullable(SubscriptionInfoDetails_validator)
SubscriptionInfo._all_field_names_ = set([
    'subscription_type',
    'active',
    'previous',
    'scheduled'])
SubscriptionInfo._all_fields_ = [
    ('subscription_type', SubscriptionInfo.subscription_type.validator),
    ('active', SubscriptionInfo.active.validator),
    ('previous', SubscriptionInfo.previous.validator),
    ('scheduled', SubscriptionInfo.scheduled.validator)]
SubscriptionInfoDetails.unique_transaction_id.validator = bv.Nullable(bv.String())
SubscriptionInfoDetails.last_transaction_id.validator = bv.Nullable(bv.String())
SubscriptionInfoDetails.storefront.validator = storefront_platform.StorefrontPlatformBillingProvider_validator
SubscriptionInfoDetails.start_date.validator = common.Date_validator
SubscriptionInfoDetails.original_start_date.validator = common.Date_validator
SubscriptionInfoDetails.expiration_date.validator = common.Date_validator
SubscriptionInfoDetails.is_in_billing_retry_period.validator = bv.Boolean()
SubscriptionInfoDetails.is_in_billing_retry_period.validator._redact = bv.BlotRedactor(None)
SubscriptionInfoDetails.grace_period_expiry_date.validator = bv.Nullable(common.Date_validator)
SubscriptionInfoDetails.auto_renew_status.validator = bv.Boolean()
SubscriptionInfoDetails.auto_renew_status.validator._redact = bv.BlotRedactor(None)
SubscriptionInfoDetails.billing_period.validator = storefront_platform.ContractLength_validator
SubscriptionInfoDetails.api_product_family.validator = store.ApiProductFamily_validator
SubscriptionInfoDetails.is_trial.validator = bv.Boolean()
SubscriptionInfoDetails.is_trial.validator._redact = bv.BlotRedactor(None)
SubscriptionInfoDetails.storefront_product_id.validator = bv.String()
SubscriptionInfoDetails.storefront_product_id.validator._redact = bv.BlotRedactor(None)
SubscriptionInfoDetails.mobile_subscription_group.validator = bv.Nullable(bv.String())
SubscriptionInfoDetails._all_field_names_ = set([
    'unique_transaction_id',
    'last_transaction_id',
    'storefront',
    'start_date',
    'original_start_date',
    'expiration_date',
    'is_in_billing_retry_period',
    'grace_period_expiry_date',
    'auto_renew_status',
    'billing_period',
    'api_product_family',
    'is_trial',
    'storefront_product_id',
    'mobile_subscription_group'])
SubscriptionInfoDetails._all_fields_ = [
    ('unique_transaction_id', SubscriptionInfoDetails.unique_transaction_id.validator),
    ('last_transaction_id', SubscriptionInfoDetails.last_transaction_id.validator),
    ('storefront', SubscriptionInfoDetails.storefront.validator),
    ('start_date', SubscriptionInfoDetails.start_date.validator),
    ('original_start_date', SubscriptionInfoDetails.original_start_date.validator),
    ('expiration_date', SubscriptionInfoDetails.expiration_date.validator),
    ('is_in_billing_retry_period', SubscriptionInfoDetails.is_in_billing_retry_period.validator),
    ('grace_period_expiry_date', SubscriptionInfoDetails.grace_period_expiry_date.validator),
    ('auto_renew_status', SubscriptionInfoDetails.auto_renew_status.validator),
    ('billing_period', SubscriptionInfoDetails.billing_period.validator),
    ('api_product_family', SubscriptionInfoDetails.api_product_family.validator),
    ('is_trial', SubscriptionInfoDetails.is_trial.validator),
    ('storefront_product_id', SubscriptionInfoDetails.storefront_product_id.validator),
    ('mobile_subscription_group', SubscriptionInfoDetails.mobile_subscription_group.validator)]
TeamSharedDropboxValue._enabled_validator = bv.Boolean()
TeamSharedDropboxValue._other_validator = bv.Void()
TeamSharedDropboxValue._tagmap = {
    'enabled': TeamSharedDropboxValue._enabled_validator,
    'other': TeamSharedDropboxValue._other_validator }
TeamSharedDropboxValue.other = TeamSharedDropboxValue('other')
TeamSpaceAllocation.used.validator = bv.UInt64()
TeamSpaceAllocation.allocated.validator = bv.UInt64()
TeamSpaceAllocation.user_within_team_space_allocated.validator = bv.UInt64()
TeamSpaceAllocation.user_within_team_space_limit_type.validator = team_common.MemberSpaceLimitType_validator
TeamSpaceAllocation.user_within_team_space_used_cached.validator = bv.UInt64()
TeamSpaceAllocation._all_field_names_ = set([
    'used',
    'allocated',
    'user_within_team_space_allocated',
    'user_within_team_space_limit_type',
    'user_within_team_space_used_cached'])
TeamSpaceAllocation._all_fields_ = [
    ('used', TeamSpaceAllocation.used.validator),
    ('allocated', TeamSpaceAllocation.allocated.validator),
    ('user_within_team_space_allocated', TeamSpaceAllocation.user_within_team_space_allocated.validator),
    ('user_within_team_space_limit_type', TeamSpaceAllocation.user_within_team_space_limit_type.validator),
    ('user_within_team_space_used_cached', TeamSpaceAllocation.user_within_team_space_used_cached.validator)]
TeamUserPermissions.is_admin.validator = bv.Boolean()
TeamUserPermissions.admin_role.validator = bv.Nullable(bv.String())
TeamUserPermissions.membership_type.validator = bv.String()
TeamUserPermissions.join_state.validator = bv.String()
TeamUserPermissions.suggest_members_enabled.validator = bv.Boolean()
TeamUserPermissions._all_field_names_ = set([
    'is_admin',
    'admin_role',
    'membership_type',
    'join_state',
    'suggest_members_enabled'])
TeamUserPermissions._all_fields_ = [
    ('is_admin', TeamUserPermissions.is_admin.validator),
    ('admin_role', TeamUserPermissions.admin_role.validator),
    ('membership_type', TeamUserPermissions.membership_type.validator),
    ('join_state', TeamUserPermissions.join_state.validator),
    ('suggest_members_enabled', TeamUserPermissions.suggest_members_enabled.validator)]
TooManyFilesReason.approximate_file_count.validator = bv.Int64()
TooManyFilesReason.file_limit.validator = bv.Int64()
TooManyFilesReason._all_field_names_ = set([
    'approximate_file_count',
    'file_limit'])
TooManyFilesReason._all_fields_ = [
    ('approximate_file_count', TooManyFilesReason.approximate_file_count.validator),
    ('file_limit', TooManyFilesReason.file_limit.validator)]
UsageUnit._user_validator = UserUsageUnit_validator
UsageUnit._other_validator = bv.Void()
UsageUnit._tagmap = {
    'user': UsageUnit._user_validator,
    'other': UsageUnit._other_validator }
UsageUnit.other = UsageUnit('other')
UserAccountType._primary_validator = bv.Void()
UserAccountType._sub_account_validator = bv.Void()
UserAccountType._other_validator = bv.Void()
UserAccountType._tagmap = {
    'primary': UserAccountType._primary_validator,
    'sub_account': UserAccountType._sub_account_validator,
    'other': UserAccountType._other_validator }
UserAccountType.primary = UserAccountType('primary')
UserAccountType.sub_account = UserAccountType('sub_account')
UserAccountType.other = UserAccountType('other')
UserFeature._paper_as_files_validator = bv.Void()
UserFeature._file_locking_validator = bv.Void()
UserFeature._team_shared_dropbox_validator = bv.Void()
UserFeature._distinct_member_home_validator = bv.Void()
UserFeature._other_validator = bv.Void()
UserFeature._tagmap = {
    'paper_as_files': UserFeature._paper_as_files_validator,
    'file_locking': UserFeature._file_locking_validator,
    'team_shared_dropbox': UserFeature._team_shared_dropbox_validator,
    'distinct_member_home': UserFeature._distinct_member_home_validator,
    'other': UserFeature._other_validator }
UserFeature.paper_as_files = UserFeature('paper_as_files')
UserFeature.file_locking = UserFeature('file_locking')
UserFeature.team_shared_dropbox = UserFeature('team_shared_dropbox')
UserFeature.distinct_member_home = UserFeature('distinct_member_home')
UserFeature.other = UserFeature('other')
UserFeatureValue._paper_as_files_validator = PaperAsFilesValue_validator
UserFeatureValue._file_locking_validator = FileLockingValue_validator
UserFeatureValue._team_shared_dropbox_validator = TeamSharedDropboxValue_validator
UserFeatureValue._distinct_member_home_validator = DistinctMemberHomeValue_validator
UserFeatureValue._other_validator = bv.Void()
UserFeatureValue._tagmap = {
    'paper_as_files': UserFeatureValue._paper_as_files_validator,
    'file_locking': UserFeatureValue._file_locking_validator,
    'team_shared_dropbox': UserFeatureValue._team_shared_dropbox_validator,
    'distinct_member_home': UserFeatureValue._distinct_member_home_validator,
    'other': UserFeatureValue._other_validator }
UserFeatureValue.other = UserFeatureValue('other')
UserFeaturesGetValuesBatchArg.features.validator = bv.List(UserFeature_validator)
UserFeaturesGetValuesBatchArg._all_field_names_ = set([
    'features'])
UserFeaturesGetValuesBatchArg._all_fields_ = [
    ('features', UserFeaturesGetValuesBatchArg.features.validator)]
UserFeaturesGetValuesBatchError._empty_features_list_validator = bv.Void()
UserFeaturesGetValuesBatchError._other_validator = bv.Void()
UserFeaturesGetValuesBatchError._tagmap = {
    'empty_features_list': UserFeaturesGetValuesBatchError._empty_features_list_validator,
    'other': UserFeaturesGetValuesBatchError._other_validator }
UserFeaturesGetValuesBatchError.empty_features_list = UserFeaturesGetValuesBatchError('empty_features_list')
UserFeaturesGetValuesBatchError.other = UserFeaturesGetValuesBatchError('other')
UserFeaturesGetValuesBatchResult.values.validator = bv.List(UserFeatureValue_validator)
UserFeaturesGetValuesBatchResult._all_field_names_ = set([
    'values'])
UserFeaturesGetValuesBatchResult._all_fields_ = [
    ('values', UserFeaturesGetValuesBatchResult.values.validator)]
UserUsageUnit.name.validator = Name_validator
UserUsageUnit.usage_in_bytes.validator = bv.UInt64()
UserUsageUnit.usage_in_bytes.validator._redact = bv.BlotRedactor(None)
UserUsageUnit.uid.validator = bv.Int64()
UserUsageUnit.uid.validator._redact = bv.BlotRedactor(None)
UserUsageUnit._all_field_names_ = set([
    'name',
    'usage_in_bytes',
    'uid'])
UserUsageUnit._all_fields_ = [
    ('name', UserUsageUnit.name.validator),
    ('usage_in_bytes', UserUsageUnit.usage_in_bytes.validator),
    ('uid', UserUsageUnit.uid.validator)]
# WARNING: Decompyle incomplete
