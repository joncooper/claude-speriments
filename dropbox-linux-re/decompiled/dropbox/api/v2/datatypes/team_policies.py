# Source Generated with Decompyle++
# File: team_policies.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class CameraUploadsPolicyState(bb.Union):
    pass
# WARNING: Decompyle incomplete

CameraUploadsPolicyState_validator = bv.Union(CameraUploadsPolicyState)

class ComputerBackupPolicyState(bb.Union):
    pass
# WARNING: Decompyle incomplete

ComputerBackupPolicyState_validator = bv.Union(ComputerBackupPolicyState)

class DefaultLinkExpirationDaysPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

DefaultLinkExpirationDaysPolicy_validator = bv.Union(DefaultLinkExpirationDaysPolicy)

class EmmState(bb.Union):
    pass
# WARNING: Decompyle incomplete

EmmState_validator = bv.Union(EmmState)

class EnforceLinkPasswordPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

EnforceLinkPasswordPolicy_validator = bv.Union(EnforceLinkPasswordPolicy)

class ExternalDriveBackupPolicyState(bb.Union):
    pass
# WARNING: Decompyle incomplete

ExternalDriveBackupPolicyState_validator = bv.Union(ExternalDriveBackupPolicyState)

class FileLockingPolicyState(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileLockingPolicyState_validator = bv.Union(FileLockingPolicyState)

class FileProviderMigrationPolicyState(bb.Union):
    pass
# WARNING: Decompyle incomplete

FileProviderMigrationPolicyState_validator = bv.Union(FileProviderMigrationPolicyState)

class GroupCreation(bb.Union):
    pass
# WARNING: Decompyle incomplete

GroupCreation_validator = bv.Union(GroupCreation)

class OfficeAddInPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

OfficeAddInPolicy_validator = bv.Union(OfficeAddInPolicy)

class PaperDefaultFolderPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaperDefaultFolderPolicy_validator = bv.Union(PaperDefaultFolderPolicy)

class PaperDeploymentPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaperDeploymentPolicy_validator = bv.Union(PaperDeploymentPolicy)

class PaperDesktopPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaperDesktopPolicy_validator = bv.Union(PaperDesktopPolicy)

class PaperEnabledPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

PaperEnabledPolicy_validator = bv.Union(PaperEnabledPolicy)

class PasswordControlMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

PasswordControlMode_validator = bv.Union(PasswordControlMode)

class PasswordStrengthPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

PasswordStrengthPolicy_validator = bv.Union(PasswordStrengthPolicy)

class RolloutMethod(bb.Union):
    pass
# WARNING: Decompyle incomplete

RolloutMethod_validator = bv.Union(RolloutMethod)

class SharedFolderBlanketLinkRestrictionPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedFolderBlanketLinkRestrictionPolicy_validator = bv.Union(SharedFolderBlanketLinkRestrictionPolicy)

class SharedFolderJoinPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedFolderJoinPolicy_validator = bv.Union(SharedFolderJoinPolicy)

class SharedFolderMemberPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedFolderMemberPolicy_validator = bv.Union(SharedFolderMemberPolicy)

class SharedLinkCreatePolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedLinkCreatePolicy_validator = bv.Union(SharedLinkCreatePolicy)

class SharedLinkDefaultPermissionsPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedLinkDefaultPermissionsPolicy_validator = bv.Union(SharedLinkDefaultPermissionsPolicy)

class ShowcaseDownloadPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

ShowcaseDownloadPolicy_validator = bv.Union(ShowcaseDownloadPolicy)

class ShowcaseEnabledPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

ShowcaseEnabledPolicy_validator = bv.Union(ShowcaseEnabledPolicy)

class ShowcaseExternalSharingPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

ShowcaseExternalSharingPolicy_validator = bv.Union(ShowcaseExternalSharingPolicy)

class SmartSyncPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SmartSyncPolicy_validator = bv.Union(SmartSyncPolicy)

class SmarterSmartSyncPolicyState(bb.Union):
    pass
# WARNING: Decompyle incomplete

SmarterSmartSyncPolicyState_validator = bv.Union(SmarterSmartSyncPolicyState)

class SsoPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SsoPolicy_validator = bv.Union(SsoPolicy)

class SuggestMembersPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

SuggestMembersPolicy_validator = bv.Union(SuggestMembersPolicy)

class TeamMemberPolicies(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamMemberPolicies_validator = bv.Struct(TeamMemberPolicies)

class TeamSharingPolicies(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamSharingPolicies_validator = bv.Struct(TeamSharingPolicies)

class TopLevelContentPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

TopLevelContentPolicy_validator = bv.Union(TopLevelContentPolicy)

class TwoStepVerificationPolicy(bb.Union):
    pass
# WARNING: Decompyle incomplete

TwoStepVerificationPolicy_validator = bv.Union(TwoStepVerificationPolicy)

class TwoStepVerificationState(bb.Union):
    pass
# WARNING: Decompyle incomplete

TwoStepVerificationState_validator = bv.Union(TwoStepVerificationState)
CameraUploadsPolicyState._disabled_validator = bv.Void()
CameraUploadsPolicyState._enabled_validator = bv.Void()
CameraUploadsPolicyState._other_validator = bv.Void()
CameraUploadsPolicyState._tagmap = {
    'disabled': CameraUploadsPolicyState._disabled_validator,
    'enabled': CameraUploadsPolicyState._enabled_validator,
    'other': CameraUploadsPolicyState._other_validator }
CameraUploadsPolicyState.disabled = CameraUploadsPolicyState('disabled')
CameraUploadsPolicyState.enabled = CameraUploadsPolicyState('enabled')
CameraUploadsPolicyState.other = CameraUploadsPolicyState('other')
ComputerBackupPolicyState._disabled_validator = bv.Void()
ComputerBackupPolicyState._enabled_validator = bv.Void()
ComputerBackupPolicyState._default_validator = bv.Void()
ComputerBackupPolicyState._other_validator = bv.Void()
ComputerBackupPolicyState._tagmap = {
    'disabled': ComputerBackupPolicyState._disabled_validator,
    'enabled': ComputerBackupPolicyState._enabled_validator,
    'default': ComputerBackupPolicyState._default_validator,
    'other': ComputerBackupPolicyState._other_validator }
ComputerBackupPolicyState.disabled = ComputerBackupPolicyState('disabled')
ComputerBackupPolicyState.enabled = ComputerBackupPolicyState('enabled')
ComputerBackupPolicyState.default = ComputerBackupPolicyState('default')
ComputerBackupPolicyState.other = ComputerBackupPolicyState('other')
DefaultLinkExpirationDaysPolicy._none_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._day_1_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._day_3_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._day_7_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._day_30_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._day_90_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._day_180_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._year_1_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._other_validator = bv.Void()
DefaultLinkExpirationDaysPolicy._tagmap = {
    'none': DefaultLinkExpirationDaysPolicy._none_validator,
    'day_1': DefaultLinkExpirationDaysPolicy._day_1_validator,
    'day_3': DefaultLinkExpirationDaysPolicy._day_3_validator,
    'day_7': DefaultLinkExpirationDaysPolicy._day_7_validator,
    'day_30': DefaultLinkExpirationDaysPolicy._day_30_validator,
    'day_90': DefaultLinkExpirationDaysPolicy._day_90_validator,
    'day_180': DefaultLinkExpirationDaysPolicy._day_180_validator,
    'year_1': DefaultLinkExpirationDaysPolicy._year_1_validator,
    'other': DefaultLinkExpirationDaysPolicy._other_validator }
DefaultLinkExpirationDaysPolicy.none = DefaultLinkExpirationDaysPolicy('none')
DefaultLinkExpirationDaysPolicy.day_1 = DefaultLinkExpirationDaysPolicy('day_1')
DefaultLinkExpirationDaysPolicy.day_3 = DefaultLinkExpirationDaysPolicy('day_3')
DefaultLinkExpirationDaysPolicy.day_7 = DefaultLinkExpirationDaysPolicy('day_7')
DefaultLinkExpirationDaysPolicy.day_30 = DefaultLinkExpirationDaysPolicy('day_30')
DefaultLinkExpirationDaysPolicy.day_90 = DefaultLinkExpirationDaysPolicy('day_90')
DefaultLinkExpirationDaysPolicy.day_180 = DefaultLinkExpirationDaysPolicy('day_180')
DefaultLinkExpirationDaysPolicy.year_1 = DefaultLinkExpirationDaysPolicy('year_1')
DefaultLinkExpirationDaysPolicy.other = DefaultLinkExpirationDaysPolicy('other')
EmmState._disabled_validator = bv.Void()
EmmState._optional_validator = bv.Void()
EmmState._required_validator = bv.Void()
EmmState._other_validator = bv.Void()
EmmState._tagmap = {
    'disabled': EmmState._disabled_validator,
    'optional': EmmState._optional_validator,
    'required': EmmState._required_validator,
    'other': EmmState._other_validator }
EmmState.disabled = EmmState('disabled')
EmmState.optional = EmmState('optional')
EmmState.required = EmmState('required')
EmmState.other = EmmState('other')
EnforceLinkPasswordPolicy._optional_validator = bv.Void()
EnforceLinkPasswordPolicy._required_validator = bv.Void()
EnforceLinkPasswordPolicy._other_validator = bv.Void()
EnforceLinkPasswordPolicy._tagmap = {
    'optional': EnforceLinkPasswordPolicy._optional_validator,
    'required': EnforceLinkPasswordPolicy._required_validator,
    'other': EnforceLinkPasswordPolicy._other_validator }
EnforceLinkPasswordPolicy.optional = EnforceLinkPasswordPolicy('optional')
EnforceLinkPasswordPolicy.required = EnforceLinkPasswordPolicy('required')
EnforceLinkPasswordPolicy.other = EnforceLinkPasswordPolicy('other')
ExternalDriveBackupPolicyState._disabled_validator = bv.Void()
ExternalDriveBackupPolicyState._enabled_validator = bv.Void()
ExternalDriveBackupPolicyState._default_validator = bv.Void()
ExternalDriveBackupPolicyState._other_validator = bv.Void()
ExternalDriveBackupPolicyState._tagmap = {
    'disabled': ExternalDriveBackupPolicyState._disabled_validator,
    'enabled': ExternalDriveBackupPolicyState._enabled_validator,
    'default': ExternalDriveBackupPolicyState._default_validator,
    'other': ExternalDriveBackupPolicyState._other_validator }
ExternalDriveBackupPolicyState.disabled = ExternalDriveBackupPolicyState('disabled')
ExternalDriveBackupPolicyState.enabled = ExternalDriveBackupPolicyState('enabled')
ExternalDriveBackupPolicyState.default = ExternalDriveBackupPolicyState('default')
ExternalDriveBackupPolicyState.other = ExternalDriveBackupPolicyState('other')
FileLockingPolicyState._disabled_validator = bv.Void()
FileLockingPolicyState._enabled_validator = bv.Void()
FileLockingPolicyState._other_validator = bv.Void()
FileLockingPolicyState._tagmap = {
    'disabled': FileLockingPolicyState._disabled_validator,
    'enabled': FileLockingPolicyState._enabled_validator,
    'other': FileLockingPolicyState._other_validator }
FileLockingPolicyState.disabled = FileLockingPolicyState('disabled')
FileLockingPolicyState.enabled = FileLockingPolicyState('enabled')
FileLockingPolicyState.other = FileLockingPolicyState('other')
FileProviderMigrationPolicyState._disabled_validator = bv.Void()
FileProviderMigrationPolicyState._enabled_validator = bv.Void()
FileProviderMigrationPolicyState._default_validator = bv.Void()
FileProviderMigrationPolicyState._immediate_validator = bv.Void()
FileProviderMigrationPolicyState._other_validator = bv.Void()
FileProviderMigrationPolicyState._tagmap = {
    'disabled': FileProviderMigrationPolicyState._disabled_validator,
    'enabled': FileProviderMigrationPolicyState._enabled_validator,
    'default': FileProviderMigrationPolicyState._default_validator,
    'immediate': FileProviderMigrationPolicyState._immediate_validator,
    'other': FileProviderMigrationPolicyState._other_validator }
FileProviderMigrationPolicyState.disabled = FileProviderMigrationPolicyState('disabled')
FileProviderMigrationPolicyState.enabled = FileProviderMigrationPolicyState('enabled')
FileProviderMigrationPolicyState.default = FileProviderMigrationPolicyState('default')
FileProviderMigrationPolicyState.immediate = FileProviderMigrationPolicyState('immediate')
FileProviderMigrationPolicyState.other = FileProviderMigrationPolicyState('other')
GroupCreation._admins_and_members_validator = bv.Void()
GroupCreation._admins_only_validator = bv.Void()
GroupCreation._tagmap = {
    'admins_and_members': GroupCreation._admins_and_members_validator,
    'admins_only': GroupCreation._admins_only_validator }
GroupCreation.admins_and_members = GroupCreation('admins_and_members')
GroupCreation.admins_only = GroupCreation('admins_only')
OfficeAddInPolicy._disabled_validator = bv.Void()
OfficeAddInPolicy._enabled_validator = bv.Void()
OfficeAddInPolicy._other_validator = bv.Void()
OfficeAddInPolicy._tagmap = {
    'disabled': OfficeAddInPolicy._disabled_validator,
    'enabled': OfficeAddInPolicy._enabled_validator,
    'other': OfficeAddInPolicy._other_validator }
OfficeAddInPolicy.disabled = OfficeAddInPolicy('disabled')
OfficeAddInPolicy.enabled = OfficeAddInPolicy('enabled')
OfficeAddInPolicy.other = OfficeAddInPolicy('other')
PaperDefaultFolderPolicy._everyone_in_team_validator = bv.Void()
PaperDefaultFolderPolicy._invite_only_validator = bv.Void()
PaperDefaultFolderPolicy._other_validator = bv.Void()
PaperDefaultFolderPolicy._tagmap = {
    'everyone_in_team': PaperDefaultFolderPolicy._everyone_in_team_validator,
    'invite_only': PaperDefaultFolderPolicy._invite_only_validator,
    'other': PaperDefaultFolderPolicy._other_validator }
PaperDefaultFolderPolicy.everyone_in_team = PaperDefaultFolderPolicy('everyone_in_team')
PaperDefaultFolderPolicy.invite_only = PaperDefaultFolderPolicy('invite_only')
PaperDefaultFolderPolicy.other = PaperDefaultFolderPolicy('other')
PaperDeploymentPolicy._full_validator = bv.Void()
PaperDeploymentPolicy._partial_validator = bv.Void()
PaperDeploymentPolicy._other_validator = bv.Void()
PaperDeploymentPolicy._tagmap = {
    'full': PaperDeploymentPolicy._full_validator,
    'partial': PaperDeploymentPolicy._partial_validator,
    'other': PaperDeploymentPolicy._other_validator }
PaperDeploymentPolicy.full = PaperDeploymentPolicy('full')
PaperDeploymentPolicy.partial = PaperDeploymentPolicy('partial')
PaperDeploymentPolicy.other = PaperDeploymentPolicy('other')
PaperDesktopPolicy._disabled_validator = bv.Void()
PaperDesktopPolicy._enabled_validator = bv.Void()
PaperDesktopPolicy._other_validator = bv.Void()
PaperDesktopPolicy._tagmap = {
    'disabled': PaperDesktopPolicy._disabled_validator,
    'enabled': PaperDesktopPolicy._enabled_validator,
    'other': PaperDesktopPolicy._other_validator }
PaperDesktopPolicy.disabled = PaperDesktopPolicy('disabled')
PaperDesktopPolicy.enabled = PaperDesktopPolicy('enabled')
PaperDesktopPolicy.other = PaperDesktopPolicy('other')
PaperEnabledPolicy._disabled_validator = bv.Void()
PaperEnabledPolicy._enabled_validator = bv.Void()
PaperEnabledPolicy._unspecified_validator = bv.Void()
PaperEnabledPolicy._other_validator = bv.Void()
PaperEnabledPolicy._tagmap = {
    'disabled': PaperEnabledPolicy._disabled_validator,
    'enabled': PaperEnabledPolicy._enabled_validator,
    'unspecified': PaperEnabledPolicy._unspecified_validator,
    'other': PaperEnabledPolicy._other_validator }
PaperEnabledPolicy.disabled = PaperEnabledPolicy('disabled')
PaperEnabledPolicy.enabled = PaperEnabledPolicy('enabled')
PaperEnabledPolicy.unspecified = PaperEnabledPolicy('unspecified')
PaperEnabledPolicy.other = PaperEnabledPolicy('other')
PasswordControlMode._disabled_validator = bv.Void()
PasswordControlMode._enabled_validator = bv.Void()
PasswordControlMode._other_validator = bv.Void()
PasswordControlMode._tagmap = {
    'disabled': PasswordControlMode._disabled_validator,
    'enabled': PasswordControlMode._enabled_validator,
    'other': PasswordControlMode._other_validator }
PasswordControlMode.disabled = PasswordControlMode('disabled')
PasswordControlMode.enabled = PasswordControlMode('enabled')
PasswordControlMode.other = PasswordControlMode('other')
PasswordStrengthPolicy._minimal_requirements_validator = bv.Void()
PasswordStrengthPolicy._moderate_password_validator = bv.Void()
PasswordStrengthPolicy._strong_password_validator = bv.Void()
PasswordStrengthPolicy._other_validator = bv.Void()
PasswordStrengthPolicy._tagmap = {
    'minimal_requirements': PasswordStrengthPolicy._minimal_requirements_validator,
    'moderate_password': PasswordStrengthPolicy._moderate_password_validator,
    'strong_password': PasswordStrengthPolicy._strong_password_validator,
    'other': PasswordStrengthPolicy._other_validator }
PasswordStrengthPolicy.minimal_requirements = PasswordStrengthPolicy('minimal_requirements')
PasswordStrengthPolicy.moderate_password = PasswordStrengthPolicy('moderate_password')
PasswordStrengthPolicy.strong_password = PasswordStrengthPolicy('strong_password')
PasswordStrengthPolicy.other = PasswordStrengthPolicy('other')
RolloutMethod._unlink_all_validator = bv.Void()
RolloutMethod._unlink_most_inactive_validator = bv.Void()
RolloutMethod._add_member_to_exceptions_validator = bv.Void()
RolloutMethod._tagmap = {
    'unlink_all': RolloutMethod._unlink_all_validator,
    'unlink_most_inactive': RolloutMethod._unlink_most_inactive_validator,
    'add_member_to_exceptions': RolloutMethod._add_member_to_exceptions_validator }
RolloutMethod.unlink_all = RolloutMethod('unlink_all')
RolloutMethod.unlink_most_inactive = RolloutMethod('unlink_most_inactive')
RolloutMethod.add_member_to_exceptions = RolloutMethod('add_member_to_exceptions')
SharedFolderBlanketLinkRestrictionPolicy._members_validator = bv.Void()
SharedFolderBlanketLinkRestrictionPolicy._anyone_validator = bv.Void()
SharedFolderBlanketLinkRestrictionPolicy._other_validator = bv.Void()
SharedFolderBlanketLinkRestrictionPolicy._tagmap = {
    'members': SharedFolderBlanketLinkRestrictionPolicy._members_validator,
    'anyone': SharedFolderBlanketLinkRestrictionPolicy._anyone_validator,
    'other': SharedFolderBlanketLinkRestrictionPolicy._other_validator }
SharedFolderBlanketLinkRestrictionPolicy.members = SharedFolderBlanketLinkRestrictionPolicy('members')
SharedFolderBlanketLinkRestrictionPolicy.anyone = SharedFolderBlanketLinkRestrictionPolicy('anyone')
SharedFolderBlanketLinkRestrictionPolicy.other = SharedFolderBlanketLinkRestrictionPolicy('other')
SharedFolderJoinPolicy._from_team_only_validator = bv.Void()
SharedFolderJoinPolicy._from_anyone_validator = bv.Void()
SharedFolderJoinPolicy._other_validator = bv.Void()
SharedFolderJoinPolicy._tagmap = {
    'from_team_only': SharedFolderJoinPolicy._from_team_only_validator,
    'from_anyone': SharedFolderJoinPolicy._from_anyone_validator,
    'other': SharedFolderJoinPolicy._other_validator }
SharedFolderJoinPolicy.from_team_only = SharedFolderJoinPolicy('from_team_only')
SharedFolderJoinPolicy.from_anyone = SharedFolderJoinPolicy('from_anyone')
SharedFolderJoinPolicy.other = SharedFolderJoinPolicy('other')
SharedFolderMemberPolicy._team_validator = bv.Void()
SharedFolderMemberPolicy._anyone_validator = bv.Void()
SharedFolderMemberPolicy._team_and_approved_validator = bv.Void()
SharedFolderMemberPolicy._other_validator = bv.Void()
SharedFolderMemberPolicy._tagmap = {
    'team': SharedFolderMemberPolicy._team_validator,
    'anyone': SharedFolderMemberPolicy._anyone_validator,
    'team_and_approved': SharedFolderMemberPolicy._team_and_approved_validator,
    'other': SharedFolderMemberPolicy._other_validator }
SharedFolderMemberPolicy.team = SharedFolderMemberPolicy('team')
SharedFolderMemberPolicy.anyone = SharedFolderMemberPolicy('anyone')
SharedFolderMemberPolicy.team_and_approved = SharedFolderMemberPolicy('team_and_approved')
SharedFolderMemberPolicy.other = SharedFolderMemberPolicy('other')
SharedLinkCreatePolicy._default_public_validator = bv.Void()
SharedLinkCreatePolicy._default_team_only_validator = bv.Void()
SharedLinkCreatePolicy._team_only_validator = bv.Void()
SharedLinkCreatePolicy._default_no_one_validator = bv.Void()
SharedLinkCreatePolicy._other_validator = bv.Void()
SharedLinkCreatePolicy._tagmap = {
    'default_public': SharedLinkCreatePolicy._default_public_validator,
    'default_team_only': SharedLinkCreatePolicy._default_team_only_validator,
    'team_only': SharedLinkCreatePolicy._team_only_validator,
    'default_no_one': SharedLinkCreatePolicy._default_no_one_validator,
    'other': SharedLinkCreatePolicy._other_validator }
SharedLinkCreatePolicy.default_public = SharedLinkCreatePolicy('default_public')
SharedLinkCreatePolicy.default_team_only = SharedLinkCreatePolicy('default_team_only')
SharedLinkCreatePolicy.team_only = SharedLinkCreatePolicy('team_only')
SharedLinkCreatePolicy.default_no_one = SharedLinkCreatePolicy('default_no_one')
SharedLinkCreatePolicy.other = SharedLinkCreatePolicy('other')
SharedLinkDefaultPermissionsPolicy._default_validator = bv.Void()
SharedLinkDefaultPermissionsPolicy._edit_validator = bv.Void()
SharedLinkDefaultPermissionsPolicy._view_validator = bv.Void()
SharedLinkDefaultPermissionsPolicy._other_validator = bv.Void()
SharedLinkDefaultPermissionsPolicy._tagmap = {
    'default': SharedLinkDefaultPermissionsPolicy._default_validator,
    'edit': SharedLinkDefaultPermissionsPolicy._edit_validator,
    'view': SharedLinkDefaultPermissionsPolicy._view_validator,
    'other': SharedLinkDefaultPermissionsPolicy._other_validator }
SharedLinkDefaultPermissionsPolicy.default = SharedLinkDefaultPermissionsPolicy('default')
SharedLinkDefaultPermissionsPolicy.edit = SharedLinkDefaultPermissionsPolicy('edit')
SharedLinkDefaultPermissionsPolicy.view = SharedLinkDefaultPermissionsPolicy('view')
SharedLinkDefaultPermissionsPolicy.other = SharedLinkDefaultPermissionsPolicy('other')
ShowcaseDownloadPolicy._disabled_validator = bv.Void()
ShowcaseDownloadPolicy._enabled_validator = bv.Void()
ShowcaseDownloadPolicy._other_validator = bv.Void()
ShowcaseDownloadPolicy._tagmap = {
    'disabled': ShowcaseDownloadPolicy._disabled_validator,
    'enabled': ShowcaseDownloadPolicy._enabled_validator,
    'other': ShowcaseDownloadPolicy._other_validator }
ShowcaseDownloadPolicy.disabled = ShowcaseDownloadPolicy('disabled')
ShowcaseDownloadPolicy.enabled = ShowcaseDownloadPolicy('enabled')
ShowcaseDownloadPolicy.other = ShowcaseDownloadPolicy('other')
ShowcaseEnabledPolicy._disabled_validator = bv.Void()
ShowcaseEnabledPolicy._enabled_validator = bv.Void()
ShowcaseEnabledPolicy._other_validator = bv.Void()
ShowcaseEnabledPolicy._tagmap = {
    'disabled': ShowcaseEnabledPolicy._disabled_validator,
    'enabled': ShowcaseEnabledPolicy._enabled_validator,
    'other': ShowcaseEnabledPolicy._other_validator }
ShowcaseEnabledPolicy.disabled = ShowcaseEnabledPolicy('disabled')
ShowcaseEnabledPolicy.enabled = ShowcaseEnabledPolicy('enabled')
ShowcaseEnabledPolicy.other = ShowcaseEnabledPolicy('other')
ShowcaseExternalSharingPolicy._disabled_validator = bv.Void()
ShowcaseExternalSharingPolicy._enabled_validator = bv.Void()
ShowcaseExternalSharingPolicy._other_validator = bv.Void()
ShowcaseExternalSharingPolicy._tagmap = {
    'disabled': ShowcaseExternalSharingPolicy._disabled_validator,
    'enabled': ShowcaseExternalSharingPolicy._enabled_validator,
    'other': ShowcaseExternalSharingPolicy._other_validator }
ShowcaseExternalSharingPolicy.disabled = ShowcaseExternalSharingPolicy('disabled')
ShowcaseExternalSharingPolicy.enabled = ShowcaseExternalSharingPolicy('enabled')
ShowcaseExternalSharingPolicy.other = ShowcaseExternalSharingPolicy('other')
SmartSyncPolicy._local_validator = bv.Void()
SmartSyncPolicy._on_demand_validator = bv.Void()
SmartSyncPolicy._other_validator = bv.Void()
SmartSyncPolicy._tagmap = {
    'local': SmartSyncPolicy._local_validator,
    'on_demand': SmartSyncPolicy._on_demand_validator,
    'other': SmartSyncPolicy._other_validator }
SmartSyncPolicy.local = SmartSyncPolicy('local')
SmartSyncPolicy.on_demand = SmartSyncPolicy('on_demand')
SmartSyncPolicy.other = SmartSyncPolicy('other')
SmarterSmartSyncPolicyState._disabled_validator = bv.Void()
SmarterSmartSyncPolicyState._enabled_validator = bv.Void()
SmarterSmartSyncPolicyState._other_validator = bv.Void()
SmarterSmartSyncPolicyState._tagmap = {
    'disabled': SmarterSmartSyncPolicyState._disabled_validator,
    'enabled': SmarterSmartSyncPolicyState._enabled_validator,
    'other': SmarterSmartSyncPolicyState._other_validator }
SmarterSmartSyncPolicyState.disabled = SmarterSmartSyncPolicyState('disabled')
SmarterSmartSyncPolicyState.enabled = SmarterSmartSyncPolicyState('enabled')
SmarterSmartSyncPolicyState.other = SmarterSmartSyncPolicyState('other')
SsoPolicy._disabled_validator = bv.Void()
SsoPolicy._optional_validator = bv.Void()
SsoPolicy._required_validator = bv.Void()
SsoPolicy._other_validator = bv.Void()
SsoPolicy._tagmap = {
    'disabled': SsoPolicy._disabled_validator,
    'optional': SsoPolicy._optional_validator,
    'required': SsoPolicy._required_validator,
    'other': SsoPolicy._other_validator }
SsoPolicy.disabled = SsoPolicy('disabled')
SsoPolicy.optional = SsoPolicy('optional')
SsoPolicy.required = SsoPolicy('required')
SsoPolicy.other = SsoPolicy('other')
SuggestMembersPolicy._disabled_validator = bv.Void()
SuggestMembersPolicy._enabled_validator = bv.Void()
SuggestMembersPolicy._other_validator = bv.Void()
SuggestMembersPolicy._tagmap = {
    'disabled': SuggestMembersPolicy._disabled_validator,
    'enabled': SuggestMembersPolicy._enabled_validator,
    'other': SuggestMembersPolicy._other_validator }
SuggestMembersPolicy.disabled = SuggestMembersPolicy('disabled')
SuggestMembersPolicy.enabled = SuggestMembersPolicy('enabled')
SuggestMembersPolicy.other = SuggestMembersPolicy('other')
TeamMemberPolicies.sharing.validator = TeamSharingPolicies_validator
TeamMemberPolicies.emm_state.validator = EmmState_validator
TeamMemberPolicies.office_addin.validator = OfficeAddInPolicy_validator
TeamMemberPolicies.suggest_members_policy.validator = SuggestMembersPolicy_validator
TeamMemberPolicies.top_level_content_policy.validator = TopLevelContentPolicy_validator
TeamMemberPolicies._all_field_names_ = set([
    'sharing',
    'emm_state',
    'office_addin',
    'suggest_members_policy',
    'top_level_content_policy'])
TeamMemberPolicies._all_fields_ = [
    ('sharing', TeamMemberPolicies.sharing.validator),
    ('emm_state', TeamMemberPolicies.emm_state.validator),
    ('office_addin', TeamMemberPolicies.office_addin.validator),
    ('suggest_members_policy', TeamMemberPolicies.suggest_members_policy.validator),
    ('top_level_content_policy', TeamMemberPolicies.top_level_content_policy.validator)]
TeamSharingPolicies.shared_folder_member_policy.validator = SharedFolderMemberPolicy_validator
TeamSharingPolicies.shared_folder_join_policy.validator = SharedFolderJoinPolicy_validator
TeamSharingPolicies.shared_link_create_policy.validator = SharedLinkCreatePolicy_validator
TeamSharingPolicies.group_creation_policy.validator = GroupCreation_validator
TeamSharingPolicies.shared_folder_link_restriction_policy.validator = SharedFolderBlanketLinkRestrictionPolicy_validator
TeamSharingPolicies.enforce_link_password_policy.validator = EnforceLinkPasswordPolicy_validator
TeamSharingPolicies.default_link_expiration_days_policy.validator = DefaultLinkExpirationDaysPolicy_validator
TeamSharingPolicies.shared_link_default_permissions_policy.validator = SharedLinkDefaultPermissionsPolicy_validator
TeamSharingPolicies._all_field_names_ = set([
    'shared_folder_member_policy',
    'shared_folder_join_policy',
    'shared_link_create_policy',
    'group_creation_policy',
    'shared_folder_link_restriction_policy',
    'enforce_link_password_policy',
    'default_link_expiration_days_policy',
    'shared_link_default_permissions_policy'])
TeamSharingPolicies._all_fields_ = [
    ('shared_folder_member_policy', TeamSharingPolicies.shared_folder_member_policy.validator),
    ('shared_folder_join_policy', TeamSharingPolicies.shared_folder_join_policy.validator),
    ('shared_link_create_policy', TeamSharingPolicies.shared_link_create_policy.validator),
    ('group_creation_policy', TeamSharingPolicies.group_creation_policy.validator),
    ('shared_folder_link_restriction_policy', TeamSharingPolicies.shared_folder_link_restriction_policy.validator),
    ('enforce_link_password_policy', TeamSharingPolicies.enforce_link_password_policy.validator),
    ('default_link_expiration_days_policy', TeamSharingPolicies.default_link_expiration_days_policy.validator),
    ('shared_link_default_permissions_policy', TeamSharingPolicies.shared_link_default_permissions_policy.validator)]
TopLevelContentPolicy._admin_only_validator = bv.Void()
TopLevelContentPolicy._everyone_validator = bv.Void()
TopLevelContentPolicy._other_validator = bv.Void()
TopLevelContentPolicy._tagmap = {
    'admin_only': TopLevelContentPolicy._admin_only_validator,
    'everyone': TopLevelContentPolicy._everyone_validator,
    'other': TopLevelContentPolicy._other_validator }
TopLevelContentPolicy.admin_only = TopLevelContentPolicy('admin_only')
TopLevelContentPolicy.everyone = TopLevelContentPolicy('everyone')
TopLevelContentPolicy.other = TopLevelContentPolicy('other')
TwoStepVerificationPolicy._require_tfa_enable_validator = bv.Void()
TwoStepVerificationPolicy._require_tfa_disable_validator = bv.Void()
TwoStepVerificationPolicy._other_validator = bv.Void()
TwoStepVerificationPolicy._tagmap = {
    'require_tfa_enable': TwoStepVerificationPolicy._require_tfa_enable_validator,
    'require_tfa_disable': TwoStepVerificationPolicy._require_tfa_disable_validator,
    'other': TwoStepVerificationPolicy._other_validator }
TwoStepVerificationPolicy.require_tfa_enable = TwoStepVerificationPolicy('require_tfa_enable')
TwoStepVerificationPolicy.require_tfa_disable = TwoStepVerificationPolicy('require_tfa_disable')
TwoStepVerificationPolicy.other = TwoStepVerificationPolicy('other')
TwoStepVerificationState._required_validator = bv.Void()
TwoStepVerificationState._optional_validator = bv.Void()
TwoStepVerificationState._disabled_validator = bv.Void()
TwoStepVerificationState._other_validator = bv.Void()
TwoStepVerificationState._tagmap = {
    'required': TwoStepVerificationState._required_validator,
    'optional': TwoStepVerificationState._optional_validator,
    'disabled': TwoStepVerificationState._disabled_validator,
    'other': TwoStepVerificationState._other_validator }
TwoStepVerificationState.required = TwoStepVerificationState('required')
TwoStepVerificationState.optional = TwoStepVerificationState('optional')
TwoStepVerificationState.disabled = TwoStepVerificationState('disabled')
TwoStepVerificationState.other = TwoStepVerificationState('other')
ROUTES = { }
