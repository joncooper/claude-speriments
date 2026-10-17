# Source Generated with Decompyle++
# File: growth.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import cash_catalog_constants_stone
from dropbox.api.v2.datatypes import common

class ActivationMilestoneProps(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ActivationMilestoneProps_validator = bv.Struct(ActivationMilestoneProps)

class ActivationModulesProps(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ActivationModulesProps_validator = bv.Struct(ActivationModulesProps)

class BoltChannelState(bb.Struct):
    pass
# WARNING: Decompyle incomplete

BoltChannelState_validator = bv.Struct(BoltChannelState)

class ContinuousOnboardingError(bb.Union):
    pass
# WARNING: Decompyle incomplete

ContinuousOnboardingError_validator = bv.Union(ContinuousOnboardingError)

class ContinuousOnboardingSurface(bb.Union):
    pass
# WARNING: Decompyle incomplete

ContinuousOnboardingSurface_validator = bv.Union(ContinuousOnboardingSurface)

class ContinuousOnboardingSurfaceProps(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ContinuousOnboardingSurfaceProps_validator = bv.StructTree(ContinuousOnboardingSurfaceProps)

class GetContinuousOnboardingArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetContinuousOnboardingArg_validator = bv.Struct(GetContinuousOnboardingArg)

class GetContinuousOnboardingResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetContinuousOnboardingResult_validator = bv.Struct(GetContinuousOnboardingResult)

class GetRightsizingPropsResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetRightsizingPropsResult_validator = bv.Struct(GetRightsizingPropsResult)

class GetSharedContentMetadataArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSharedContentMetadataArg_validator = bv.Struct(GetSharedContentMetadataArg)

class GetSharedContentMetadataError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetSharedContentMetadataError_validator = bv.Union(GetSharedContentMetadataError)

class GetSharedContentMetadataResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSharedContentMetadataResult_validator = bv.Struct(GetSharedContentMetadataResult)

class GetSkuRoutingDecisionArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSkuRoutingDecisionArg_validator = bv.Struct(GetSkuRoutingDecisionArg)

class GetSkuRoutingDecisionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetSkuRoutingDecisionError_validator = bv.Union(GetSkuRoutingDecisionError)

class GetSkuRoutingDecisionResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetSkuRoutingDecisionResult_validator = bv.Struct(GetSkuRoutingDecisionResult)

class GetTrialCardInfoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTrialCardInfoArg_validator = bv.Struct(GetTrialCardInfoArg)

class GetTrialCardInfoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTrialCardInfoResult_validator = bv.Struct(GetTrialCardInfoResult)

class LeftNavChecklistSurfaceProps(ContinuousOnboardingSurfaceProps):
    pass
# WARNING: Decompyle incomplete

LeftNavChecklistSurfaceProps_validator = bv.Struct(LeftNavChecklistSurfaceProps)

class LinkQrTokenArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkQrTokenArg_validator = bv.Struct(LinkQrTokenArg)

class LinkQrTokenError(bb.Union):
    pass
# WARNING: Decompyle incomplete

LinkQrTokenError_validator = bv.Union(LinkQrTokenError)

class LinkQrTokenResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LinkQrTokenResult_validator = bv.Struct(LinkQrTokenResult)

class MovableSharedFoldersEntry(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MovableSharedFoldersEntry_validator = bv.Struct(MovableSharedFoldersEntry)

class MovableSharedFoldersError(bb.Union):
    pass
# WARNING: Decompyle incomplete

MovableSharedFoldersError_validator = bv.Union(MovableSharedFoldersError)

class MovableSharedFoldersResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

MovableSharedFoldersResult_validator = bv.Struct(MovableSharedFoldersResult)

class NpTrialStartArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NpTrialStartArg_validator = bv.Struct(NpTrialStartArg)

class NpTrialStartError(bb.Union):
    pass
# WARNING: Decompyle incomplete

NpTrialStartError_validator = bv.Union(NpTrialStartError)

class NpTrialStartResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

NpTrialStartResult_validator = bv.Struct(NpTrialStartResult)

class PcoemGetOnboardingEligibilityArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PcoemGetOnboardingEligibilityArg_validator = bv.Struct(PcoemGetOnboardingEligibilityArg)

class PcoemGetOnboardingEligibilityResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PcoemGetOnboardingEligibilityResult_validator = bv.Struct(PcoemGetOnboardingEligibilityResult)

class PcoemLogLoggedOutEventArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PcoemLogLoggedOutEventArg_validator = bv.Struct(PcoemLogLoggedOutEventArg)

class PcoemLogLoggedOutEventError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PcoemLogLoggedOutEventError_validator = bv.Union(PcoemLogLoggedOutEventError)

class PcoemShowOnboardingError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PcoemShowOnboardingError_validator = bv.Union(PcoemShowOnboardingError)

class ProgressionProps(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ProgressionProps_validator = bv.Struct(ProgressionProps)

class RightsizeSimpleSku(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RightsizeSimpleSku_validator = bv.Struct(RightsizeSimpleSku)

class SharedContentAccessLevel(bb.Union):
    pass
# WARNING: Decompyle incomplete

SharedContentAccessLevel_validator = bv.Union(SharedContentAccessLevel)

class ShiftUserActionTimeArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ShiftUserActionTimeArg_validator = bv.Struct(ShiftUserActionTimeArg)

class SkuRoutingDecision(bb.Union):
    pass
# WARNING: Decompyle incomplete

SkuRoutingDecision_validator = bv.Union(SkuRoutingDecision)

class TeamChecklistData(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TeamChecklistData_validator = bv.Struct(TeamChecklistData)

class TrialCardInfo(bb.Struct):
    pass
# WARNING: Decompyle incomplete

TrialCardInfo_validator = bv.Struct(TrialCardInfo)

class TrialCardLocationEnum(bb.Union):
    pass
# WARNING: Decompyle incomplete

TrialCardLocationEnum_validator = bv.Union(TrialCardLocationEnum)

class UserActionArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserActionArg_validator = bv.Struct(UserActionArg)

class UserActionError(bb.Union):
    pass
# WARNING: Decompyle incomplete

UserActionError_validator = bv.Union(UserActionError)

class UserActionPerformedArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserActionPerformedArg_validator = bv.Struct(UserActionPerformedArg)

class UserActionPerformedAtLeastArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserActionPerformedAtLeastArg_validator = bv.Struct(UserActionPerformedAtLeastArg)

class UserActionPerformedResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserActionPerformedResult_validator = bv.Struct(UserActionPerformedResult)

class UserActionTimeDelta(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UserActionTimeDelta_validator = bv.Struct(UserActionTimeDelta)
PathR_validator = bv.String(pattern = '(/(.|[\\r\\n])*)|(ns:[0-9]+(/.*)?)')
PathR_validator._redact = bv.BlotRedactor(None)
ActivationMilestoneProps.milestone_id.validator = bv.String()
ActivationMilestoneProps.milestone_id.validator._redact = bv.BlotRedactor(None)
ActivationMilestoneProps.milestone_key.validator = bv.String()
ActivationMilestoneProps.milestone_key.validator._redact = bv.BlotRedactor(None)
ActivationMilestoneProps.is_completed.validator = bv.Boolean()
ActivationMilestoneProps.is_completed.validator._redact = bv.BlotRedactor(None)
ActivationMilestoneProps._all_field_names_ = set([
    'milestone_id',
    'milestone_key',
    'is_completed'])
ActivationMilestoneProps._all_fields_ = [
    ('milestone_id', ActivationMilestoneProps.milestone_id.validator),
    ('milestone_key', ActivationMilestoneProps.milestone_key.validator),
    ('is_completed', ActivationMilestoneProps.is_completed.validator)]
ActivationModulesProps.module_id.validator = bv.String()
ActivationModulesProps.module_id.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.skip_string.validator = bv.String()
ActivationModulesProps.skip_string.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.dismiss_string.validator = bv.String()
ActivationModulesProps.dismiss_string.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.seen_string.validator = bv.String()
ActivationModulesProps.seen_string.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.should_show.validator = bv.Boolean()
ActivationModulesProps.should_show.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.is_skipped.validator = bv.Boolean()
ActivationModulesProps.is_skipped.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.is_dismissed.validator = bv.Boolean()
ActivationModulesProps.is_dismissed.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.is_seen.validator = bv.Boolean()
ActivationModulesProps.is_seen.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.completed_module_goals.validator = bv.Boolean()
ActivationModulesProps.completed_module_goals.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps.completed_module_goals_time.validator = bv.Nullable(bv.UInt64())
ActivationModulesProps.milestone_keys.validator = bv.List(bv.String())
ActivationModulesProps.milestone_keys.validator._redact = bv.BlotRedactor(None)
ActivationModulesProps._all_field_names_ = set([
    'module_id',
    'skip_string',
    'dismiss_string',
    'seen_string',
    'should_show',
    'is_skipped',
    'is_dismissed',
    'is_seen',
    'completed_module_goals',
    'completed_module_goals_time',
    'milestone_keys'])
ActivationModulesProps._all_fields_ = [
    ('module_id', ActivationModulesProps.module_id.validator),
    ('skip_string', ActivationModulesProps.skip_string.validator),
    ('dismiss_string', ActivationModulesProps.dismiss_string.validator),
    ('seen_string', ActivationModulesProps.seen_string.validator),
    ('should_show', ActivationModulesProps.should_show.validator),
    ('is_skipped', ActivationModulesProps.is_skipped.validator),
    ('is_dismissed', ActivationModulesProps.is_dismissed.validator),
    ('is_seen', ActivationModulesProps.is_seen.validator),
    ('completed_module_goals', ActivationModulesProps.completed_module_goals.validator),
    ('completed_module_goals_time', ActivationModulesProps.completed_module_goals_time.validator),
    ('milestone_keys', ActivationModulesProps.milestone_keys.validator)]
BoltChannelState.unique_id.validator = bv.String()
BoltChannelState.unique_id.validator._redact = bv.BlotRedactor(None)
BoltChannelState.revision.validator = bv.String()
BoltChannelState.revision.validator._redact = bv.BlotRedactor(None)
BoltChannelState.token.validator = bv.String()
BoltChannelState.token.validator._redact = bv.BlotRedactor(None)
BoltChannelState._all_field_names_ = set([
    'unique_id',
    'revision',
    'token'])
BoltChannelState._all_fields_ = [
    ('unique_id', BoltChannelState.unique_id.validator),
    ('revision', BoltChannelState.revision.validator),
    ('token', BoltChannelState.token.validator)]
ContinuousOnboardingError._unimplemented_surface_validator = bv.Void()
ContinuousOnboardingError._unimplemented_bolt_channel_in_milestone_validator = bv.Void()
ContinuousOnboardingError._unimplemented_data_source_validator = bv.Void()
ContinuousOnboardingError._other_validator = bv.Void()
ContinuousOnboardingError._tagmap = {
    'unimplemented_surface': ContinuousOnboardingError._unimplemented_surface_validator,
    'unimplemented_bolt_channel_in_milestone': ContinuousOnboardingError._unimplemented_bolt_channel_in_milestone_validator,
    'unimplemented_data_source': ContinuousOnboardingError._unimplemented_data_source_validator,
    'other': ContinuousOnboardingError._other_validator }
ContinuousOnboardingError.unimplemented_surface = ContinuousOnboardingError('unimplemented_surface')
ContinuousOnboardingError.unimplemented_bolt_channel_in_milestone = ContinuousOnboardingError('unimplemented_bolt_channel_in_milestone')
ContinuousOnboardingError.unimplemented_data_source = ContinuousOnboardingError('unimplemented_data_source')
ContinuousOnboardingError.other = ContinuousOnboardingError('other')
ContinuousOnboardingSurface._is_dash_checklist_validator = bv.Void()
ContinuousOnboardingSurface._left_nav_checklist_validator = bv.Void()
ContinuousOnboardingSurface._dash_new_user_checklist_validator = bv.Void()
ContinuousOnboardingSurface._device_connectivity_validator = bv.Void()
ContinuousOnboardingSurface._dash_nux_v2_checklist_validator = bv.Void()
ContinuousOnboardingSurface._other_validator = bv.Void()
ContinuousOnboardingSurface._tagmap = {
    'is_dash_checklist': ContinuousOnboardingSurface._is_dash_checklist_validator,
    'left_nav_checklist': ContinuousOnboardingSurface._left_nav_checklist_validator,
    'dash_new_user_checklist': ContinuousOnboardingSurface._dash_new_user_checklist_validator,
    'device_connectivity': ContinuousOnboardingSurface._device_connectivity_validator,
    'dash_nux_v2_checklist': ContinuousOnboardingSurface._dash_nux_v2_checklist_validator,
    'other': ContinuousOnboardingSurface._other_validator }
ContinuousOnboardingSurface.is_dash_checklist = ContinuousOnboardingSurface('is_dash_checklist')
ContinuousOnboardingSurface.left_nav_checklist = ContinuousOnboardingSurface('left_nav_checklist')
ContinuousOnboardingSurface.dash_new_user_checklist = ContinuousOnboardingSurface('dash_new_user_checklist')
ContinuousOnboardingSurface.device_connectivity = ContinuousOnboardingSurface('device_connectivity')
ContinuousOnboardingSurface.dash_nux_v2_checklist = ContinuousOnboardingSurface('dash_nux_v2_checklist')
ContinuousOnboardingSurface.other = ContinuousOnboardingSurface('other')
ContinuousOnboardingSurfaceProps._field_names_ = set([])
ContinuousOnboardingSurfaceProps._all_field_names_ = ContinuousOnboardingSurfaceProps._field_names_
ContinuousOnboardingSurfaceProps._fields_ = []
ContinuousOnboardingSurfaceProps._all_fields_ = ContinuousOnboardingSurfaceProps._fields_
ContinuousOnboardingSurfaceProps._tag_to_subtype_ = {
    ('left_nav_checklist',): LeftNavChecklistSurfaceProps_validator }
ContinuousOnboardingSurfaceProps._pytype_to_tag_and_subtype_ = {
    LeftNavChecklistSurfaceProps: (('left_nav_checklist',), LeftNavChecklistSurfaceProps_validator) }
ContinuousOnboardingSurfaceProps._is_catch_all_ = True
GetContinuousOnboardingArg.surface.validator = bv.Nullable(ContinuousOnboardingSurface_validator)
GetContinuousOnboardingArg.surface_path.validator = bv.Nullable(bv.String())
GetContinuousOnboardingArg.surface_path.validator._redact = bv.BlotRedactor(None)
GetContinuousOnboardingArg.include_hidden.validator = bv.Boolean()
GetContinuousOnboardingArg.include_hidden.validator._redact = bv.BlotRedactor(None)
GetContinuousOnboardingArg.show_modules_completed_before_seen.validator = bv.Boolean()
GetContinuousOnboardingArg.show_modules_completed_before_seen.validator._redact = bv.BlotRedactor(None)
GetContinuousOnboardingArg._all_field_names_ = set([
    'surface',
    'surface_path',
    'include_hidden',
    'show_modules_completed_before_seen'])
GetContinuousOnboardingArg._all_fields_ = [
    ('surface', GetContinuousOnboardingArg.surface.validator),
    ('surface_path', GetContinuousOnboardingArg.surface_path.validator),
    ('include_hidden', GetContinuousOnboardingArg.include_hidden.validator),
    ('show_modules_completed_before_seen', GetContinuousOnboardingArg.show_modules_completed_before_seen.validator)]
GetContinuousOnboardingResult.progression.validator = bv.Nullable(ProgressionProps_validator)
GetContinuousOnboardingResult.display_surface_props.validator = bv.Nullable(ContinuousOnboardingSurfaceProps_validator)
GetContinuousOnboardingResult.bolt_channel_states.validator = bv.Map(bv.String(), BoltChannelState_validator)
GetContinuousOnboardingResult.open_on_load.validator = bv.Boolean()
GetContinuousOnboardingResult.open_on_load.validator._redact = bv.BlotRedactor(None)
GetContinuousOnboardingResult._all_field_names_ = set([
    'progression',
    'display_surface_props',
    'bolt_channel_states',
    'open_on_load'])
GetContinuousOnboardingResult._all_fields_ = [
    ('progression', GetContinuousOnboardingResult.progression.validator),
    ('display_surface_props', GetContinuousOnboardingResult.display_surface_props.validator),
    ('bolt_channel_states', GetContinuousOnboardingResult.bolt_channel_states.validator),
    ('open_on_load', GetContinuousOnboardingResult.open_on_load.validator)]
GetRightsizingPropsResult.is_advanced.validator = bv.Boolean()
GetRightsizingPropsResult.is_advanced.validator._redact = bv.BlotRedactor(None)
GetRightsizingPropsResult.standard.validator = RightsizeSimpleSku_validator
GetRightsizingPropsResult.advanced.validator = RightsizeSimpleSku_validator
GetRightsizingPropsResult.professional.validator = RightsizeSimpleSku_validator
GetRightsizingPropsResult.trial_days.validator = bv.UInt64()
GetRightsizingPropsResult.trial_days.validator._redact = bv.BlotRedactor(None)
GetRightsizingPropsResult.user_first_name.validator = bv.Nullable(bv.String())
GetRightsizingPropsResult._all_field_names_ = set([
    'is_advanced',
    'standard',
    'advanced',
    'professional',
    'trial_days',
    'user_first_name'])
GetRightsizingPropsResult._all_fields_ = [
    ('is_advanced', GetRightsizingPropsResult.is_advanced.validator),
    ('standard', GetRightsizingPropsResult.standard.validator),
    ('advanced', GetRightsizingPropsResult.advanced.validator),
    ('professional', GetRightsizingPropsResult.professional.validator),
    ('trial_days', GetRightsizingPropsResult.trial_days.validator),
    ('user_first_name', GetRightsizingPropsResult.user_first_name.validator)]
GetSharedContentMetadataArg.cont.validator = bv.String()
GetSharedContentMetadataArg.cont.validator._redact = bv.BlotRedactor(None)
GetSharedContentMetadataArg._all_field_names_ = set([
    'cont'])
GetSharedContentMetadataArg._all_fields_ = [
    ('cont', GetSharedContentMetadataArg.cont.validator)]
GetSharedContentMetadataError._other_validator = bv.Void()
GetSharedContentMetadataError._tagmap = {
    'other': GetSharedContentMetadataError._other_validator }
GetSharedContentMetadataError.other = GetSharedContentMetadataError('other')
GetSharedContentMetadataResult.size_bytes.validator = bv.Nullable(bv.Int64())
GetSharedContentMetadataResult.access_level.validator = SharedContentAccessLevel_validator
GetSharedContentMetadataResult._all_field_names_ = set([
    'size_bytes',
    'access_level'])
GetSharedContentMetadataResult._all_fields_ = [
    ('size_bytes', GetSharedContentMetadataResult.size_bytes.validator),
    ('access_level', GetSharedContentMetadataResult.access_level.validator)]
GetSkuRoutingDecisionArg._all_field_names_ = set([])
GetSkuRoutingDecisionArg._all_fields_ = []
GetSkuRoutingDecisionError._other_validator = bv.Void()
GetSkuRoutingDecisionError._tagmap = {
    'other': GetSkuRoutingDecisionError._other_validator }
GetSkuRoutingDecisionError.other = GetSkuRoutingDecisionError('other')
GetSkuRoutingDecisionResult.decision.validator = SkuRoutingDecision_validator
GetSkuRoutingDecisionResult._all_field_names_ = set([
    'decision'])
GetSkuRoutingDecisionResult._all_fields_ = [
    ('decision', GetSkuRoutingDecisionResult.decision.validator)]
GetTrialCardInfoArg.product_plan_types_requested.validator = bv.List(cash_catalog_constants_stone.ProductPlanType_validator)
GetTrialCardInfoArg.trial_card_location.validator = bv.Nullable(TrialCardLocationEnum_validator)
GetTrialCardInfoArg._all_field_names_ = set([
    'product_plan_types_requested',
    'trial_card_location'])
GetTrialCardInfoArg._all_fields_ = [
    ('product_plan_types_requested', GetTrialCardInfoArg.product_plan_types_requested.validator),
    ('trial_card_location', GetTrialCardInfoArg.trial_card_location.validator)]
GetTrialCardInfoResult.trial_card_infos.validator = bv.List(TrialCardInfo_validator)
GetTrialCardInfoResult._all_field_names_ = set([
    'trial_card_infos'])
GetTrialCardInfoResult._all_fields_ = [
    ('trial_card_infos', GetTrialCardInfoResult.trial_card_infos.validator)]
LeftNavChecklistSurfaceProps.user_created_time.validator = bv.UInt64()
LeftNavChecklistSurfaceProps.user_created_time.validator._redact = bv.BlotRedactor(None)
LeftNavChecklistSurfaceProps.user_account_age_ms.validator = bv.UInt64()
LeftNavChecklistSurfaceProps.user_account_age_ms.validator._redact = bv.BlotRedactor(None)
LeftNavChecklistSurfaceProps.checklist_expanded_time.validator = bv.Nullable(bv.UInt64())
LeftNavChecklistSurfaceProps.checklist_colllapsed_viewed.validator = bv.Boolean()
LeftNavChecklistSurfaceProps.checklist_colllapsed_viewed.validator._redact = bv.BlotRedactor(None)
LeftNavChecklistSurfaceProps.team_checklist_data.validator = bv.Nullable(TeamChecklistData_validator)
LeftNavChecklistSurfaceProps.desktop_tof_copy_refresh_checklist_variant.validator = bv.Nullable(bv.String())
LeftNavChecklistSurfaceProps._field_names_ = set([
    'user_created_time',
    'user_account_age_ms',
    'checklist_expanded_time',
    'checklist_colllapsed_viewed',
    'team_checklist_data',
    'desktop_tof_copy_refresh_checklist_variant'])
LeftNavChecklistSurfaceProps._all_field_names_ = ContinuousOnboardingSurfaceProps._all_field_names_.union(LeftNavChecklistSurfaceProps._field_names_)
LeftNavChecklistSurfaceProps._fields_ = [
    ('user_created_time', LeftNavChecklistSurfaceProps.user_created_time.validator),
    ('user_account_age_ms', LeftNavChecklistSurfaceProps.user_account_age_ms.validator),
    ('checklist_expanded_time', LeftNavChecklistSurfaceProps.checklist_expanded_time.validator),
    ('checklist_colllapsed_viewed', LeftNavChecklistSurfaceProps.checklist_colllapsed_viewed.validator),
    ('team_checklist_data', LeftNavChecklistSurfaceProps.team_checklist_data.validator),
    ('desktop_tof_copy_refresh_checklist_variant', LeftNavChecklistSurfaceProps.desktop_tof_copy_refresh_checklist_variant.validator)]
LeftNavChecklistSurfaceProps._all_fields_ = ContinuousOnboardingSurfaceProps._all_fields_ + LeftNavChecklistSurfaceProps._fields_
LinkQrTokenArg.token.validator = bv.String()
LinkQrTokenArg.token.validator._redact = bv.BlotRedactor(None)
LinkQrTokenArg._all_field_names_ = set([
    'token'])
LinkQrTokenArg._all_fields_ = [
    ('token', LinkQrTokenArg.token.validator)]
LinkQrTokenError._token_already_linked_validator = bv.Void()
LinkQrTokenError._token_expired_validator = bv.Void()
LinkQrTokenError._token_not_found_validator = bv.Void()
LinkQrTokenError._token_not_linked_validator = bv.Void()
LinkQrTokenError._other_validator = bv.Void()
LinkQrTokenError._tagmap = {
    'token_already_linked': LinkQrTokenError._token_already_linked_validator,
    'token_expired': LinkQrTokenError._token_expired_validator,
    'token_not_found': LinkQrTokenError._token_not_found_validator,
    'token_not_linked': LinkQrTokenError._token_not_linked_validator,
    'other': LinkQrTokenError._other_validator }
LinkQrTokenError.token_already_linked = LinkQrTokenError('token_already_linked')
LinkQrTokenError.token_expired = LinkQrTokenError('token_expired')
LinkQrTokenError.token_not_found = LinkQrTokenError('token_not_found')
LinkQrTokenError.token_not_linked = LinkQrTokenError('token_not_linked')
LinkQrTokenError.other = LinkQrTokenError('other')
LinkQrTokenResult.platform.validator = bv.String()
LinkQrTokenResult.platform.validator._redact = bv.BlotRedactor(None)
LinkQrTokenResult.browser.validator = bv.String()
LinkQrTokenResult.browser.validator._redact = bv.BlotRedactor(None)
LinkQrTokenResult.installer_type.validator = bv.String()
LinkQrTokenResult.installer_type.validator._redact = bv.BlotRedactor(None)
LinkQrTokenResult._all_field_names_ = set([
    'platform',
    'browser',
    'installer_type'])
LinkQrTokenResult._all_fields_ = [
    ('platform', LinkQrTokenResult.platform.validator),
    ('browser', LinkQrTokenResult.browser.validator),
    ('installer_type', LinkQrTokenResult.installer_type.validator)]
MovableSharedFoldersEntry.path.validator = PathR_validator
MovableSharedFoldersEntry.is_shared.validator = bv.Boolean()
MovableSharedFoldersEntry.is_shared.validator._redact = bv.BlotRedactor(None)
MovableSharedFoldersEntry.icon.validator = bv.String()
MovableSharedFoldersEntry.icon.validator._redact = bv.BlotRedactor(None)
MovableSharedFoldersEntry.contained_ns.validator = bv.UInt64()
MovableSharedFoldersEntry.contained_ns.validator._redact = bv.BlotRedactor(None)
MovableSharedFoldersEntry._all_field_names_ = set([
    'path',
    'is_shared',
    'icon',
    'contained_ns'])
MovableSharedFoldersEntry._all_fields_ = [
    ('path', MovableSharedFoldersEntry.path.validator),
    ('is_shared', MovableSharedFoldersEntry.is_shared.validator),
    ('icon', MovableSharedFoldersEntry.icon.validator),
    ('contained_ns', MovableSharedFoldersEntry.contained_ns.validator)]
MovableSharedFoldersError._user_not_cdm_validator = bv.Void()
MovableSharedFoldersError._tmf_path_not_found_validator = bv.Void()
MovableSharedFoldersError._other_validator = bv.Void()
MovableSharedFoldersError._tagmap = {
    'user_not_cdm': MovableSharedFoldersError._user_not_cdm_validator,
    'tmf_path_not_found': MovableSharedFoldersError._tmf_path_not_found_validator,
    'other': MovableSharedFoldersError._other_validator }
MovableSharedFoldersError.user_not_cdm = MovableSharedFoldersError('user_not_cdm')
MovableSharedFoldersError.tmf_path_not_found = MovableSharedFoldersError('tmf_path_not_found')
MovableSharedFoldersError.other = MovableSharedFoldersError('other')
MovableSharedFoldersResult.folders.validator = bv.List(MovableSharedFoldersEntry_validator)
MovableSharedFoldersResult._all_field_names_ = set([
    'folders'])
MovableSharedFoldersResult._all_fields_ = [
    ('folders', MovableSharedFoldersResult.folders.validator)]
NpTrialStartArg.trial_project_type.validator = bv.Nullable(bv.String())
NpTrialStartArg._all_field_names_ = set([
    'trial_project_type'])
NpTrialStartArg._all_fields_ = [
    ('trial_project_type', NpTrialStartArg.trial_project_type.validator)]
NpTrialStartError._access_denied_validator = bv.Void()
NpTrialStartError._not_eligible_for_trial_validator = bv.Void()
NpTrialStartError._too_many_trial_skus_validator = bv.Void()
NpTrialStartError._gps_client_error_validator = bv.Void()
NpTrialStartError._gps_server_error_validator = bv.Void()
NpTrialStartError._invalid_trial_project_type_validator = bv.Void()
NpTrialStartError._start_trial_failed_validator = bv.Void()
NpTrialStartError._unsupported_trial_project_type_validator = bv.Void()
NpTrialStartError._other_validator = bv.Void()
NpTrialStartError._tagmap = {
    'access_denied': NpTrialStartError._access_denied_validator,
    'not_eligible_for_trial': NpTrialStartError._not_eligible_for_trial_validator,
    'too_many_trial_skus': NpTrialStartError._too_many_trial_skus_validator,
    'gps_client_error': NpTrialStartError._gps_client_error_validator,
    'gps_server_error': NpTrialStartError._gps_server_error_validator,
    'invalid_trial_project_type': NpTrialStartError._invalid_trial_project_type_validator,
    'start_trial_failed': NpTrialStartError._start_trial_failed_validator,
    'unsupported_trial_project_type': NpTrialStartError._unsupported_trial_project_type_validator,
    'other': NpTrialStartError._other_validator }
NpTrialStartError.access_denied = NpTrialStartError('access_denied')
NpTrialStartError.not_eligible_for_trial = NpTrialStartError('not_eligible_for_trial')
NpTrialStartError.too_many_trial_skus = NpTrialStartError('too_many_trial_skus')
NpTrialStartError.gps_client_error = NpTrialStartError('gps_client_error')
NpTrialStartError.gps_server_error = NpTrialStartError('gps_server_error')
NpTrialStartError.invalid_trial_project_type = NpTrialStartError('invalid_trial_project_type')
NpTrialStartError.start_trial_failed = NpTrialStartError('start_trial_failed')
NpTrialStartError.unsupported_trial_project_type = NpTrialStartError('unsupported_trial_project_type')
NpTrialStartError.other = NpTrialStartError('other')
NpTrialStartResult.interval_end.validator = common.DropboxTimestamp_validator
NpTrialStartResult.interval_start.validator = common.DropboxTimestamp_validator
NpTrialStartResult.trial_project_type.validator = bv.String()
NpTrialStartResult.trial_project_type.validator._redact = bv.BlotRedactor(None)
NpTrialStartResult.status.validator = bv.String()
NpTrialStartResult.status.validator._redact = bv.BlotRedactor(None)
NpTrialStartResult._all_field_names_ = set([
    'interval_end',
    'interval_start',
    'trial_project_type',
    'status'])
NpTrialStartResult._all_fields_ = [
    ('interval_end', NpTrialStartResult.interval_end.validator),
    ('interval_start', NpTrialStartResult.interval_start.validator),
    ('trial_project_type', NpTrialStartResult.trial_project_type.validator),
    ('status', NpTrialStartResult.status.validator)]
PcoemGetOnboardingEligibilityArg.host_id.validator = bv.UInt64()
PcoemGetOnboardingEligibilityArg.host_id.validator._redact = bv.BlotRedactor(None)
PcoemGetOnboardingEligibilityArg._all_field_names_ = set([
    'host_id'])
PcoemGetOnboardingEligibilityArg._all_fields_ = [
    ('host_id', PcoemGetOnboardingEligibilityArg.host_id.validator)]
PcoemGetOnboardingEligibilityResult.new_device_eligible.validator = bv.Boolean()
PcoemGetOnboardingEligibilityResult.new_device_eligible.validator._redact = bv.BlotRedactor(None)
PcoemGetOnboardingEligibilityResult.old_device_eligible.validator = bv.Boolean()
PcoemGetOnboardingEligibilityResult.old_device_eligible.validator._redact = bv.BlotRedactor(None)
PcoemGetOnboardingEligibilityResult._all_field_names_ = set([
    'new_device_eligible',
    'old_device_eligible'])
PcoemGetOnboardingEligibilityResult._all_fields_ = [
    ('new_device_eligible', PcoemGetOnboardingEligibilityResult.new_device_eligible.validator),
    ('old_device_eligible', PcoemGetOnboardingEligibilityResult.old_device_eligible.validator)]
PcoemLogLoggedOutEventArg.action.validator = bv.String()
PcoemLogLoggedOutEventArg.action.validator._redact = bv.BlotRedactor(None)
PcoemLogLoggedOutEventArg.user_id.validator = bv.Nullable(bv.UInt64())
PcoemLogLoggedOutEventArg._all_field_names_ = set([
    'action',
    'user_id'])
PcoemLogLoggedOutEventArg._all_fields_ = [
    ('action', PcoemLogLoggedOutEventArg.action.validator),
    ('user_id', PcoemLogLoggedOutEventArg.user_id.validator)]
PcoemLogLoggedOutEventError._internal_error_validator = bv.Void()
PcoemLogLoggedOutEventError._other_validator = bv.Void()
PcoemLogLoggedOutEventError._tagmap = {
    'internal_error': PcoemLogLoggedOutEventError._internal_error_validator,
    'other': PcoemLogLoggedOutEventError._other_validator }
PcoemLogLoggedOutEventError.internal_error = PcoemLogLoggedOutEventError('internal_error')
PcoemLogLoggedOutEventError.other = PcoemLogLoggedOutEventError('other')
PcoemShowOnboardingError._internal_error_validator = bv.Void()
PcoemShowOnboardingError._invalid_arg_validator = bv.Void()
PcoemShowOnboardingError._other_validator = bv.Void()
PcoemShowOnboardingError._tagmap = {
    'internal_error': PcoemShowOnboardingError._internal_error_validator,
    'invalid_arg': PcoemShowOnboardingError._invalid_arg_validator,
    'other': PcoemShowOnboardingError._other_validator }
PcoemShowOnboardingError.internal_error = PcoemShowOnboardingError('internal_error')
PcoemShowOnboardingError.invalid_arg = PcoemShowOnboardingError('invalid_arg')
PcoemShowOnboardingError.other = PcoemShowOnboardingError('other')
ProgressionProps.progression_id.validator = bv.String()
ProgressionProps.progression_id.validator._redact = bv.BlotRedactor(None)
ProgressionProps.module_ids.validator = bv.List(bv.String())
ProgressionProps.module_ids.validator._redact = bv.BlotRedactor(None)
ProgressionProps.module_map.validator = bv.Map(bv.String(), ActivationModulesProps_validator)
ProgressionProps.milestone_map.validator = bv.Map(bv.String(), ActivationMilestoneProps_validator)
ProgressionProps._all_field_names_ = set([
    'progression_id',
    'module_ids',
    'module_map',
    'milestone_map'])
ProgressionProps._all_fields_ = [
    ('progression_id', ProgressionProps.progression_id.validator),
    ('module_ids', ProgressionProps.module_ids.validator),
    ('module_map', ProgressionProps.module_map.validator),
    ('milestone_map', ProgressionProps.milestone_map.validator)]
RightsizeSimpleSku.min_license.validator = bv.Nullable(bv.String())
RightsizeSimpleSku.features.validator = bv.Nullable(bv.List(bv.String()))
RightsizeSimpleSku.features.validator._redact = bv.BlotRedactor(None)
RightsizeSimpleSku.display_name.validator = bv.Nullable(bv.String())
RightsizeSimpleSku.dropbox_brand_display_name.validator = bv.Nullable(bv.String())
RightsizeSimpleSku.advertised_space_long_rounded.validator = bv.Nullable(bv.String())
RightsizeSimpleSku.advertised_space_short_gb_rounded.validator = bv.Nullable(bv.String())
RightsizeSimpleSku.advertised_monthly_price_text.validator = bv.Nullable(bv.String())
RightsizeSimpleSku.advertised_monthly_price_per_license_text.validator = bv.Nullable(bv.String())
RightsizeSimpleSku._all_field_names_ = set([
    'min_license',
    'features',
    'display_name',
    'dropbox_brand_display_name',
    'advertised_space_long_rounded',
    'advertised_space_short_gb_rounded',
    'advertised_monthly_price_text',
    'advertised_monthly_price_per_license_text'])
RightsizeSimpleSku._all_fields_ = [
    ('min_license', RightsizeSimpleSku.min_license.validator),
    ('features', RightsizeSimpleSku.features.validator),
    ('display_name', RightsizeSimpleSku.display_name.validator),
    ('dropbox_brand_display_name', RightsizeSimpleSku.dropbox_brand_display_name.validator),
    ('advertised_space_long_rounded', RightsizeSimpleSku.advertised_space_long_rounded.validator),
    ('advertised_space_short_gb_rounded', RightsizeSimpleSku.advertised_space_short_gb_rounded.validator),
    ('advertised_monthly_price_text', RightsizeSimpleSku.advertised_monthly_price_text.validator),
    ('advertised_monthly_price_per_license_text', RightsizeSimpleSku.advertised_monthly_price_per_license_text.validator)]
SharedContentAccessLevel._shared_content_access_level_unspecified_validator = bv.Void()
SharedContentAccessLevel._shared_content_access_level_editor_validator = bv.Void()
SharedContentAccessLevel._shared_content_access_level_viewer_validator = bv.Void()
SharedContentAccessLevel._shared_content_access_level_viewer_no_comment_validator = bv.Void()
SharedContentAccessLevel._other_validator = bv.Void()
SharedContentAccessLevel._tagmap = {
    'shared_content_access_level_unspecified': SharedContentAccessLevel._shared_content_access_level_unspecified_validator,
    'shared_content_access_level_editor': SharedContentAccessLevel._shared_content_access_level_editor_validator,
    'shared_content_access_level_viewer': SharedContentAccessLevel._shared_content_access_level_viewer_validator,
    'shared_content_access_level_viewer_no_comment': SharedContentAccessLevel._shared_content_access_level_viewer_no_comment_validator,
    'other': SharedContentAccessLevel._other_validator }
SharedContentAccessLevel.shared_content_access_level_unspecified = SharedContentAccessLevel('shared_content_access_level_unspecified')
SharedContentAccessLevel.shared_content_access_level_editor = SharedContentAccessLevel('shared_content_access_level_editor')
SharedContentAccessLevel.shared_content_access_level_viewer = SharedContentAccessLevel('shared_content_access_level_viewer')
SharedContentAccessLevel.shared_content_access_level_viewer_no_comment = SharedContentAccessLevel('shared_content_access_level_viewer_no_comment')
SharedContentAccessLevel.other = SharedContentAccessLevel('other')
ShiftUserActionTimeArg.project.validator = bv.String()
ShiftUserActionTimeArg.project.validator._redact = bv.BlotRedactor(None)
ShiftUserActionTimeArg.action.validator = bv.String()
ShiftUserActionTimeArg.action.validator._redact = bv.BlotRedactor(None)
ShiftUserActionTimeArg.time_delta.validator = bv.Nullable(UserActionTimeDelta_validator)
ShiftUserActionTimeArg._all_field_names_ = set([
    'project',
    'action',
    'time_delta'])
ShiftUserActionTimeArg._all_fields_ = [
    ('project', ShiftUserActionTimeArg.project.validator),
    ('action', ShiftUserActionTimeArg.action.validator),
    ('time_delta', ShiftUserActionTimeArg.time_delta.validator)]
SkuRoutingDecision._sku_routing_decision_no_treatment_validator = bv.Void()
SkuRoutingDecision._sku_routing_decision_team_intent_validator = bv.Void()
SkuRoutingDecision._sku_routing_decision_individual_intent_validator = bv.Void()
SkuRoutingDecision._other_validator = bv.Void()
SkuRoutingDecision._tagmap = {
    'sku_routing_decision_no_treatment': SkuRoutingDecision._sku_routing_decision_no_treatment_validator,
    'sku_routing_decision_team_intent': SkuRoutingDecision._sku_routing_decision_team_intent_validator,
    'sku_routing_decision_individual_intent': SkuRoutingDecision._sku_routing_decision_individual_intent_validator,
    'other': SkuRoutingDecision._other_validator }
SkuRoutingDecision.sku_routing_decision_no_treatment = SkuRoutingDecision('sku_routing_decision_no_treatment')
SkuRoutingDecision.sku_routing_decision_team_intent = SkuRoutingDecision('sku_routing_decision_team_intent')
SkuRoutingDecision.sku_routing_decision_individual_intent = SkuRoutingDecision('sku_routing_decision_individual_intent')
SkuRoutingDecision.other = SkuRoutingDecision('other')
TeamChecklistData.can_invite_member.validator = bv.Boolean()
TeamChecklistData.can_invite_member.validator._redact = bv.BlotRedactor(None)
TeamChecklistData.can_suggest_member.validator = bv.Boolean()
TeamChecklistData.can_suggest_member.validator._redact = bv.BlotRedactor(None)
TeamChecklistData.members_send_invite_domain_restriction_enabled.validator = bv.Boolean()
TeamChecklistData.members_send_invite_domain_restriction_enabled.validator._redact = bv.BlotRedactor(None)
TeamChecklistData.team_business_domains.validator = bv.List(bv.String())
TeamChecklistData.team_business_domains.validator._redact = bv.BlotRedactor(None)
TeamChecklistData.available_licenses_number.validator = bv.UInt64()
TeamChecklistData.available_licenses_number.validator._redact = bv.BlotRedactor(None)
TeamChecklistData.modal_variant.validator = bv.UInt64()
TeamChecklistData.modal_variant.validator._redact = bv.BlotRedactor(None)
TeamChecklistData._all_field_names_ = set([
    'can_invite_member',
    'can_suggest_member',
    'members_send_invite_domain_restriction_enabled',
    'team_business_domains',
    'available_licenses_number',
    'modal_variant'])
TeamChecklistData._all_fields_ = [
    ('can_invite_member', TeamChecklistData.can_invite_member.validator),
    ('can_suggest_member', TeamChecklistData.can_suggest_member.validator),
    ('members_send_invite_domain_restriction_enabled', TeamChecklistData.members_send_invite_domain_restriction_enabled.validator),
    ('team_business_domains', TeamChecklistData.team_business_domains.validator),
    ('available_licenses_number', TeamChecklistData.available_licenses_number.validator),
    ('modal_variant', TeamChecklistData.modal_variant.validator)]
TrialCardInfo.product_plan_type.validator = cash_catalog_constants_stone.ProductPlanType_validator
TrialCardInfo.trial_duration.validator = bv.Nullable(bv.Int32())
TrialCardInfo.is_eligible_for_trial.validator = bv.Nullable(bv.Boolean())
TrialCardInfo.features.validator = bv.List(bv.String())
TrialCardInfo.features.validator._redact = bv.BlotRedactor(None)
TrialCardInfo._all_field_names_ = set([
    'product_plan_type',
    'trial_duration',
    'is_eligible_for_trial',
    'features'])
TrialCardInfo._all_fields_ = [
    ('product_plan_type', TrialCardInfo.product_plan_type.validator),
    ('trial_duration', TrialCardInfo.trial_duration.validator),
    ('is_eligible_for_trial', TrialCardInfo.is_eligible_for_trial.validator),
    ('features', TrialCardInfo.features.validator)]
TrialCardLocationEnum._general_tab_validator = bv.Void()
TrialCardLocationEnum._plan_tab_validator = bv.Void()
TrialCardLocationEnum._other_validator = bv.Void()
TrialCardLocationEnum._tagmap = {
    'general_tab': TrialCardLocationEnum._general_tab_validator,
    'plan_tab': TrialCardLocationEnum._plan_tab_validator,
    'other': TrialCardLocationEnum._other_validator }
TrialCardLocationEnum.general_tab = TrialCardLocationEnum('general_tab')
TrialCardLocationEnum.plan_tab = TrialCardLocationEnum('plan_tab')
TrialCardLocationEnum.other = TrialCardLocationEnum('other')
UserActionArg.project.validator = bv.String()
UserActionArg.project.validator._redact = bv.BlotRedactor(None)
UserActionArg.action.validator = bv.String()
UserActionArg.action.validator._redact = bv.BlotRedactor(None)
UserActionArg.duration.validator = bv.Nullable(bv.UInt64())
UserActionArg.endpoint.validator = bv.Nullable(bv.String())
UserActionArg.experiment.validator = bv.Nullable(bv.String())
UserActionArg.variant.validator = bv.Nullable(bv.String())
UserActionArg.extra.validator = bv.Nullable(bv.String())
UserActionArg._all_field_names_ = set([
    'project',
    'action',
    'duration',
    'endpoint',
    'experiment',
    'variant',
    'extra'])
UserActionArg._all_fields_ = [
    ('project', UserActionArg.project.validator),
    ('action', UserActionArg.action.validator),
    ('duration', UserActionArg.duration.validator),
    ('endpoint', UserActionArg.endpoint.validator),
    ('experiment', UserActionArg.experiment.validator),
    ('variant', UserActionArg.variant.validator),
    ('extra', UserActionArg.extra.validator)]
UserActionError._internal_error_validator = bv.Void()
UserActionError._unknown_action_validator = bv.Void()
UserActionError._invalid_data_validator = bv.Void()
UserActionError._unauthorized_validator = bv.Void()
UserActionError._not_found_validator = bv.Void()
UserActionError._email_not_verified_validator = bv.Void()
UserActionError._other_validator = bv.Void()
UserActionError._tagmap = {
    'internal_error': UserActionError._internal_error_validator,
    'unknown_action': UserActionError._unknown_action_validator,
    'invalid_data': UserActionError._invalid_data_validator,
    'unauthorized': UserActionError._unauthorized_validator,
    'not_found': UserActionError._not_found_validator,
    'email_not_verified': UserActionError._email_not_verified_validator,
    'other': UserActionError._other_validator }
UserActionError.internal_error = UserActionError('internal_error')
UserActionError.unknown_action = UserActionError('unknown_action')
UserActionError.invalid_data = UserActionError('invalid_data')
UserActionError.unauthorized = UserActionError('unauthorized')
UserActionError.not_found = UserActionError('not_found')
UserActionError.email_not_verified = UserActionError('email_not_verified')
UserActionError.other = UserActionError('other')
UserActionPerformedArg.project.validator = bv.String()
UserActionPerformedArg.project.validator._redact = bv.BlotRedactor(None)
UserActionPerformedArg.action.validator = bv.String()
UserActionPerformedArg.action.validator._redact = bv.BlotRedactor(None)
UserActionPerformedArg.performed_since.validator = bv.Nullable(bv.UInt64())
UserActionPerformedArg._all_field_names_ = set([
    'project',
    'action',
    'performed_since'])
UserActionPerformedArg._all_fields_ = [
    ('project', UserActionPerformedArg.project.validator),
    ('action', UserActionPerformedArg.action.validator),
    ('performed_since', UserActionPerformedArg.performed_since.validator)]
UserActionPerformedAtLeastArg.project.validator = bv.String()
UserActionPerformedAtLeastArg.project.validator._redact = bv.BlotRedactor(None)
UserActionPerformedAtLeastArg.action.validator = bv.String()
UserActionPerformedAtLeastArg.action.validator._redact = bv.BlotRedactor(None)
UserActionPerformedAtLeastArg.count.validator = bv.UInt64()
UserActionPerformedAtLeastArg.count.validator._redact = bv.BlotRedactor(None)
UserActionPerformedAtLeastArg.performed_since.validator = bv.Nullable(bv.UInt64())
UserActionPerformedAtLeastArg._all_field_names_ = set([
    'project',
    'action',
    'count',
    'performed_since'])
UserActionPerformedAtLeastArg._all_fields_ = [
    ('project', UserActionPerformedAtLeastArg.project.validator),
    ('action', UserActionPerformedAtLeastArg.action.validator),
    ('count', UserActionPerformedAtLeastArg.count.validator),
    ('performed_since', UserActionPerformedAtLeastArg.performed_since.validator)]
UserActionPerformedResult.has_performed.validator = bv.Boolean()
UserActionPerformedResult.has_performed.validator._redact = bv.BlotRedactor(None)
UserActionPerformedResult._all_field_names_ = set([
    'has_performed'])
UserActionPerformedResult._all_fields_ = [
    ('has_performed', UserActionPerformedResult.has_performed.validator)]
UserActionTimeDelta.days.validator = bv.Nullable(bv.Int64())
UserActionTimeDelta.hours.validator = bv.Nullable(bv.Int64())
UserActionTimeDelta.minutes.validator = bv.Nullable(bv.Int64())
UserActionTimeDelta.seconds.validator = bv.Nullable(bv.Int64())
UserActionTimeDelta._all_field_names_ = set([
    'days',
    'hours',
    'minutes',
    'seconds'])
UserActionTimeDelta._all_fields_ = [
    ('days', UserActionTimeDelta.days.validator),
    ('hours', UserActionTimeDelta.hours.validator),
    ('minutes', UserActionTimeDelta.minutes.validator),
    ('seconds', UserActionTimeDelta.seconds.validator)]
GetContinuousOnboardingArg.include_hidden.default = False
GetContinuousOnboardingArg.show_modules_completed_before_seen.default = False
GetSharedContentMetadataArg.cont.default = ''
GetSharedContentMetadataResult.access_level.default = SharedContentAccessLevel.shared_content_access_level_unspecified
GetSkuRoutingDecisionResult.decision.default = SkuRoutingDecision.sku_routing_decision_no_treatment
MovableSharedFoldersEntry.is_shared.default = False
TrialCardInfo.product_plan_type.default = cash_catalog_constants_stone.ProductPlanType.unknown_product_plan_type
# WARNING: Decompyle incomplete
