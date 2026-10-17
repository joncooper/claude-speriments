# Source Generated with Decompyle++
# File: file_properties.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class AddPropertiesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddPropertiesArg_validator = bv.Struct(AddPropertiesArg)

class TemplateError(bb.Union):
    pass
# WARNING: Decompyle incomplete

TemplateError_validator = bv.Union(TemplateError)

class PropertiesError(TemplateError):
    pass
# WARNING: Decompyle incomplete

PropertiesError_validator = bv.Union(PropertiesError)

class InvalidPropertyGroupError(PropertiesError):
    pass
# WARNING: Decompyle incomplete

InvalidPropertyGroupError_validator = bv.Union(InvalidPropertyGroupError)

class AddPropertiesError(InvalidPropertyGroupError):
    pass
# WARNING: Decompyle incomplete

AddPropertiesError_validator = bv.Union(AddPropertiesError)

class PropertyGroupTemplate(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertyGroupTemplate_validator = bv.Struct(PropertyGroupTemplate)

class AddTemplateArg(PropertyGroupTemplate):
    pass
# WARNING: Decompyle incomplete

AddTemplateArg_validator = bv.Struct(AddTemplateArg)

class AddTemplateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

AddTemplateResult_validator = bv.Struct(AddTemplateResult)

class GetTemplateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetTemplateArg_validator = bv.Struct(GetTemplateArg)

class GetTemplateResult(PropertyGroupTemplate):
    pass
# WARNING: Decompyle incomplete

GetTemplateResult_validator = bv.Struct(GetTemplateResult)

class ListTemplateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

ListTemplateResult_validator = bv.Struct(ListTemplateResult)

class LogicalOperator(bb.Union):
    pass
# WARNING: Decompyle incomplete

LogicalOperator_validator = bv.Union(LogicalOperator)

class LookUpPropertiesError(bb.Union):
    pass
# WARNING: Decompyle incomplete

LookUpPropertiesError_validator = bv.Union(LookUpPropertiesError)

class LookupError(bb.Union):
    pass
# WARNING: Decompyle incomplete

LookupError_validator = bv.Union(LookupError)

class ModifyTemplateError(TemplateError):
    pass
# WARNING: Decompyle incomplete

ModifyTemplateError_validator = bv.Union(ModifyTemplateError)

class OverwritePropertyGroupArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OverwritePropertyGroupArg_validator = bv.Struct(OverwritePropertyGroupArg)

class PropertiesSearchArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertiesSearchArg_validator = bv.Struct(PropertiesSearchArg)

class PropertiesSearchContinueArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertiesSearchContinueArg_validator = bv.Struct(PropertiesSearchContinueArg)

class PropertiesSearchContinueError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PropertiesSearchContinueError_validator = bv.Union(PropertiesSearchContinueError)

class PropertiesSearchError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PropertiesSearchError_validator = bv.Union(PropertiesSearchError)

class PropertiesSearchMatch(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertiesSearchMatch_validator = bv.Struct(PropertiesSearchMatch)

class PropertiesSearchMode(bb.Union):
    pass
# WARNING: Decompyle incomplete

PropertiesSearchMode_validator = bv.Union(PropertiesSearchMode)

class PropertiesSearchQuery(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertiesSearchQuery_validator = bv.Struct(PropertiesSearchQuery)

class PropertiesSearchResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertiesSearchResult_validator = bv.Struct(PropertiesSearchResult)

class PropertyField(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertyField_validator = bv.Struct(PropertyField)

class PropertyFieldTemplate(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertyFieldTemplate_validator = bv.Struct(PropertyFieldTemplate)

class PropertyGroup(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertyGroup_validator = bv.Struct(PropertyGroup)

class PropertyGroupUpdate(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PropertyGroupUpdate_validator = bv.Struct(PropertyGroupUpdate)

class PropertyType(bb.Union):
    pass
# WARNING: Decompyle incomplete

PropertyType_validator = bv.Union(PropertyType)

class RemovePropertiesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RemovePropertiesArg_validator = bv.Struct(RemovePropertiesArg)

class RemovePropertiesError(PropertiesError):
    pass
# WARNING: Decompyle incomplete

RemovePropertiesError_validator = bv.Union(RemovePropertiesError)

class RemoveTemplateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RemoveTemplateArg_validator = bv.Struct(RemoveTemplateArg)

class TemplateFilterBase(bb.Union):
    pass
# WARNING: Decompyle incomplete

TemplateFilterBase_validator = bv.Union(TemplateFilterBase)

class TemplateFilter(TemplateFilterBase):
    pass
# WARNING: Decompyle incomplete

TemplateFilter_validator = bv.Union(TemplateFilter)

class TemplateOwnerType(bb.Union):
    pass
# WARNING: Decompyle incomplete

TemplateOwnerType_validator = bv.Union(TemplateOwnerType)

class UpdatePropertiesArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdatePropertiesArg_validator = bv.Struct(UpdatePropertiesArg)

class UpdatePropertiesError(InvalidPropertyGroupError):
    pass
# WARNING: Decompyle incomplete

UpdatePropertiesError_validator = bv.Union(UpdatePropertiesError)

class UpdateTemplateArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateTemplateArg_validator = bv.Struct(UpdateTemplateArg)

class UpdateTemplateResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

UpdateTemplateResult_validator = bv.Struct(UpdateTemplateResult)
Id_validator = bv.String(min_length = 1)
Id_validator._redact = bv.BlotRedactor(None)
PathOrId_validator = bv.String(pattern = '/(.|[\\r\\n])*|id:.*|(ns:[0-9]+(/.*)?)')
PathOrId_validator._redact = bv.BlotRedactor(None)
PropertiesSearchCursor_validator = bv.String(min_length = 1)
PropertiesSearchCursor_validator._redact = bv.BlotRedactor(None)
TemplateId_validator = bv.String(min_length = 1, pattern = '(/|ptid:).*')
TemplateId_validator._redact = bv.BlotRedactor(None)
AddPropertiesArg.path.validator = PathOrId_validator
AddPropertiesArg.property_groups.validator = bv.List(PropertyGroup_validator)
AddPropertiesArg._all_field_names_ = set([
    'path',
    'property_groups'])
AddPropertiesArg._all_fields_ = [
    ('path', AddPropertiesArg.path.validator),
    ('property_groups', AddPropertiesArg.property_groups.validator)]
TemplateError._template_not_found_validator = TemplateId_validator
TemplateError._restricted_content_validator = bv.Void()
TemplateError._other_validator = bv.Void()
TemplateError._tagmap = {
    'template_not_found': TemplateError._template_not_found_validator,
    'restricted_content': TemplateError._restricted_content_validator,
    'other': TemplateError._other_validator }
TemplateError.restricted_content = TemplateError('restricted_content')
TemplateError.other = TemplateError('other')
PropertiesError._path_validator = LookupError_validator
PropertiesError._unsupported_folder_validator = bv.Void()
PropertiesError._tagmap = {
    'path': PropertiesError._path_validator,
    'unsupported_folder': PropertiesError._unsupported_folder_validator }
PropertiesError._tagmap.update(TemplateError._tagmap)
PropertiesError.unsupported_folder = PropertiesError('unsupported_folder')
InvalidPropertyGroupError._property_field_too_large_validator = bv.Void()
InvalidPropertyGroupError._does_not_fit_template_validator = bv.Void()
InvalidPropertyGroupError._duplicate_property_groups_validator = bv.Void()
InvalidPropertyGroupError._tagmap = {
    'property_field_too_large': InvalidPropertyGroupError._property_field_too_large_validator,
    'does_not_fit_template': InvalidPropertyGroupError._does_not_fit_template_validator,
    'duplicate_property_groups': InvalidPropertyGroupError._duplicate_property_groups_validator }
InvalidPropertyGroupError._tagmap.update(PropertiesError._tagmap)
InvalidPropertyGroupError.property_field_too_large = InvalidPropertyGroupError('property_field_too_large')
InvalidPropertyGroupError.does_not_fit_template = InvalidPropertyGroupError('does_not_fit_template')
InvalidPropertyGroupError.duplicate_property_groups = InvalidPropertyGroupError('duplicate_property_groups')
AddPropertiesError._property_group_already_exists_validator = bv.Void()
AddPropertiesError._tagmap = {
    'property_group_already_exists': AddPropertiesError._property_group_already_exists_validator }
AddPropertiesError._tagmap.update(InvalidPropertyGroupError._tagmap)
AddPropertiesError.property_group_already_exists = AddPropertiesError('property_group_already_exists')
PropertyGroupTemplate.name.validator = bv.String()
PropertyGroupTemplate.name.validator._redact = bv.BlotRedactor(None)
PropertyGroupTemplate.description.validator = bv.String()
PropertyGroupTemplate.description.validator._redact = bv.BlotRedactor(None)
PropertyGroupTemplate.fields.validator = bv.List(PropertyFieldTemplate_validator)
PropertyGroupTemplate._all_field_names_ = set([
    'name',
    'description',
    'fields'])
PropertyGroupTemplate._all_fields_ = [
    ('name', PropertyGroupTemplate.name.validator),
    ('description', PropertyGroupTemplate.description.validator),
    ('fields', PropertyGroupTemplate.fields.validator)]
AddTemplateArg._all_field_names_ = PropertyGroupTemplate._all_field_names_.union(set([]))
AddTemplateArg._all_fields_ = PropertyGroupTemplate._all_fields_ + []
AddTemplateResult.template_id.validator = TemplateId_validator
AddTemplateResult._all_field_names_ = set([
    'template_id'])
AddTemplateResult._all_fields_ = [
    ('template_id', AddTemplateResult.template_id.validator)]
GetTemplateArg.template_id.validator = TemplateId_validator
GetTemplateArg._all_field_names_ = set([
    'template_id'])
GetTemplateArg._all_fields_ = [
    ('template_id', GetTemplateArg.template_id.validator)]
GetTemplateResult._all_field_names_ = PropertyGroupTemplate._all_field_names_.union(set([]))
GetTemplateResult._all_fields_ = PropertyGroupTemplate._all_fields_ + []
ListTemplateResult.template_ids.validator = bv.List(TemplateId_validator)
ListTemplateResult._all_field_names_ = set([
    'template_ids'])
ListTemplateResult._all_fields_ = [
    ('template_ids', ListTemplateResult.template_ids.validator)]
LogicalOperator._or_operator_validator = bv.Void()
LogicalOperator._other_validator = bv.Void()
LogicalOperator._tagmap = {
    'or_operator': LogicalOperator._or_operator_validator,
    'other': LogicalOperator._other_validator }
LogicalOperator.or_operator = LogicalOperator('or_operator')
LogicalOperator.other = LogicalOperator('other')
LookUpPropertiesError._property_group_not_found_validator = bv.Void()
LookUpPropertiesError._other_validator = bv.Void()
LookUpPropertiesError._tagmap = {
    'property_group_not_found': LookUpPropertiesError._property_group_not_found_validator,
    'other': LookUpPropertiesError._other_validator }
LookUpPropertiesError.property_group_not_found = LookUpPropertiesError('property_group_not_found')
LookUpPropertiesError.other = LookUpPropertiesError('other')
LookupError._malformed_path_validator = bv.String()
LookupError._malformed_path_validator._redact = bv.BlotRedactor(None)
LookupError._not_found_validator = bv.Void()
LookupError._not_file_validator = bv.Void()
LookupError._not_folder_validator = bv.Void()
LookupError._restricted_content_validator = bv.Void()
LookupError._other_validator = bv.Void()
LookupError._tagmap = {
    'malformed_path': LookupError._malformed_path_validator,
    'not_found': LookupError._not_found_validator,
    'not_file': LookupError._not_file_validator,
    'not_folder': LookupError._not_folder_validator,
    'restricted_content': LookupError._restricted_content_validator,
    'other': LookupError._other_validator }
LookupError.not_found = LookupError('not_found')
LookupError.not_file = LookupError('not_file')
LookupError.not_folder = LookupError('not_folder')
LookupError.restricted_content = LookupError('restricted_content')
LookupError.other = LookupError('other')
ModifyTemplateError._conflicting_property_names_validator = bv.Void()
ModifyTemplateError._too_many_properties_validator = bv.Void()
ModifyTemplateError._too_many_templates_validator = bv.Void()
ModifyTemplateError._template_attribute_too_large_validator = bv.Void()
ModifyTemplateError._tagmap = {
    'conflicting_property_names': ModifyTemplateError._conflicting_property_names_validator,
    'too_many_properties': ModifyTemplateError._too_many_properties_validator,
    'too_many_templates': ModifyTemplateError._too_many_templates_validator,
    'template_attribute_too_large': ModifyTemplateError._template_attribute_too_large_validator }
ModifyTemplateError._tagmap.update(TemplateError._tagmap)
ModifyTemplateError.conflicting_property_names = ModifyTemplateError('conflicting_property_names')
ModifyTemplateError.too_many_properties = ModifyTemplateError('too_many_properties')
ModifyTemplateError.too_many_templates = ModifyTemplateError('too_many_templates')
ModifyTemplateError.template_attribute_too_large = ModifyTemplateError('template_attribute_too_large')
OverwritePropertyGroupArg.path.validator = PathOrId_validator
OverwritePropertyGroupArg.property_groups.validator = bv.List(PropertyGroup_validator, min_items = 1)
OverwritePropertyGroupArg._all_field_names_ = set([
    'path',
    'property_groups'])
OverwritePropertyGroupArg._all_fields_ = [
    ('path', OverwritePropertyGroupArg.path.validator),
    ('property_groups', OverwritePropertyGroupArg.property_groups.validator)]
PropertiesSearchArg.queries.validator = bv.List(PropertiesSearchQuery_validator, min_items = 1)
PropertiesSearchArg.template_filter.validator = TemplateFilter_validator
PropertiesSearchArg._all_field_names_ = set([
    'queries',
    'template_filter'])
PropertiesSearchArg._all_fields_ = [
    ('queries', PropertiesSearchArg.queries.validator),
    ('template_filter', PropertiesSearchArg.template_filter.validator)]
PropertiesSearchContinueArg.cursor.validator = PropertiesSearchCursor_validator
PropertiesSearchContinueArg._all_field_names_ = set([
    'cursor'])
PropertiesSearchContinueArg._all_fields_ = [
    ('cursor', PropertiesSearchContinueArg.cursor.validator)]
PropertiesSearchContinueError._reset_validator = bv.Void()
PropertiesSearchContinueError._other_validator = bv.Void()
PropertiesSearchContinueError._tagmap = {
    'reset': PropertiesSearchContinueError._reset_validator,
    'other': PropertiesSearchContinueError._other_validator }
PropertiesSearchContinueError.reset = PropertiesSearchContinueError('reset')
PropertiesSearchContinueError.other = PropertiesSearchContinueError('other')
PropertiesSearchError._property_group_lookup_validator = LookUpPropertiesError_validator
PropertiesSearchError._other_validator = bv.Void()
PropertiesSearchError._tagmap = {
    'property_group_lookup': PropertiesSearchError._property_group_lookup_validator,
    'other': PropertiesSearchError._other_validator }
PropertiesSearchError.other = PropertiesSearchError('other')
PropertiesSearchMatch.id.validator = Id_validator
PropertiesSearchMatch.path.validator = bv.String()
PropertiesSearchMatch.path.validator._redact = bv.BlotRedactor(None)
PropertiesSearchMatch.is_deleted.validator = bv.Boolean()
PropertiesSearchMatch.is_deleted.validator._redact = bv.BlotRedactor(None)
PropertiesSearchMatch.property_groups.validator = bv.List(PropertyGroup_validator)
PropertiesSearchMatch._all_field_names_ = set([
    'id',
    'path',
    'is_deleted',
    'property_groups'])
PropertiesSearchMatch._all_fields_ = [
    ('id', PropertiesSearchMatch.id.validator),
    ('path', PropertiesSearchMatch.path.validator),
    ('is_deleted', PropertiesSearchMatch.is_deleted.validator),
    ('property_groups', PropertiesSearchMatch.property_groups.validator)]
PropertiesSearchMode._field_name_validator = bv.String()
PropertiesSearchMode._field_name_validator._redact = bv.BlotRedactor(None)
PropertiesSearchMode._other_validator = bv.Void()
PropertiesSearchMode._tagmap = {
    'field_name': PropertiesSearchMode._field_name_validator,
    'other': PropertiesSearchMode._other_validator }
PropertiesSearchMode.other = PropertiesSearchMode('other')
PropertiesSearchQuery.query.validator = bv.String()
PropertiesSearchQuery.query.validator._redact = bv.BlotRedactor(None)
PropertiesSearchQuery.mode.validator = PropertiesSearchMode_validator
PropertiesSearchQuery.logical_operator.validator = LogicalOperator_validator
PropertiesSearchQuery._all_field_names_ = set([
    'query',
    'mode',
    'logical_operator'])
PropertiesSearchQuery._all_fields_ = [
    ('query', PropertiesSearchQuery.query.validator),
    ('mode', PropertiesSearchQuery.mode.validator),
    ('logical_operator', PropertiesSearchQuery.logical_operator.validator)]
PropertiesSearchResult.matches.validator = bv.List(PropertiesSearchMatch_validator)
PropertiesSearchResult.cursor.validator = bv.Nullable(PropertiesSearchCursor_validator)
PropertiesSearchResult._all_field_names_ = set([
    'matches',
    'cursor'])
PropertiesSearchResult._all_fields_ = [
    ('matches', PropertiesSearchResult.matches.validator),
    ('cursor', PropertiesSearchResult.cursor.validator)]
PropertyField.name.validator = bv.String()
PropertyField.name.validator._redact = bv.BlotRedactor(None)
PropertyField.value.validator = bv.String()
PropertyField.value.validator._redact = bv.BlotRedactor(None)
PropertyField._all_field_names_ = set([
    'name',
    'value'])
PropertyField._all_fields_ = [
    ('name', PropertyField.name.validator),
    ('value', PropertyField.value.validator)]
PropertyFieldTemplate.name.validator = bv.String()
PropertyFieldTemplate.name.validator._redact = bv.BlotRedactor(None)
PropertyFieldTemplate.description.validator = bv.String()
PropertyFieldTemplate.description.validator._redact = bv.BlotRedactor(None)
PropertyFieldTemplate.type.validator = PropertyType_validator
PropertyFieldTemplate._all_field_names_ = set([
    'name',
    'description',
    'type'])
PropertyFieldTemplate._all_fields_ = [
    ('name', PropertyFieldTemplate.name.validator),
    ('description', PropertyFieldTemplate.description.validator),
    ('type', PropertyFieldTemplate.type.validator)]
PropertyGroup.template_id.validator = TemplateId_validator
PropertyGroup.fields.validator = bv.List(PropertyField_validator)
PropertyGroup._all_field_names_ = set([
    'template_id',
    'fields'])
PropertyGroup._all_fields_ = [
    ('template_id', PropertyGroup.template_id.validator),
    ('fields', PropertyGroup.fields.validator)]
PropertyGroupUpdate.template_id.validator = TemplateId_validator
PropertyGroupUpdate.add_or_update_fields.validator = bv.Nullable(bv.List(PropertyField_validator))
PropertyGroupUpdate.remove_fields.validator = bv.Nullable(bv.List(bv.String()))
PropertyGroupUpdate.remove_fields.validator._redact = bv.BlotRedactor(None)
PropertyGroupUpdate._all_field_names_ = set([
    'template_id',
    'add_or_update_fields',
    'remove_fields'])
PropertyGroupUpdate._all_fields_ = [
    ('template_id', PropertyGroupUpdate.template_id.validator),
    ('add_or_update_fields', PropertyGroupUpdate.add_or_update_fields.validator),
    ('remove_fields', PropertyGroupUpdate.remove_fields.validator)]
PropertyType._string_validator = bv.Void()
PropertyType._other_validator = bv.Void()
PropertyType._tagmap = {
    'string': PropertyType._string_validator,
    'other': PropertyType._other_validator }
PropertyType.string = PropertyType('string')
PropertyType.other = PropertyType('other')
RemovePropertiesArg.path.validator = PathOrId_validator
RemovePropertiesArg.property_template_ids.validator = bv.List(TemplateId_validator)
RemovePropertiesArg._all_field_names_ = set([
    'path',
    'property_template_ids'])
RemovePropertiesArg._all_fields_ = [
    ('path', RemovePropertiesArg.path.validator),
    ('property_template_ids', RemovePropertiesArg.property_template_ids.validator)]
RemovePropertiesError._property_group_lookup_validator = LookUpPropertiesError_validator
RemovePropertiesError._tagmap = {
    'property_group_lookup': RemovePropertiesError._property_group_lookup_validator }
RemovePropertiesError._tagmap.update(PropertiesError._tagmap)
RemoveTemplateArg.template_id.validator = TemplateId_validator
RemoveTemplateArg._all_field_names_ = set([
    'template_id'])
RemoveTemplateArg._all_fields_ = [
    ('template_id', RemoveTemplateArg.template_id.validator)]
TemplateFilterBase._filter_some_validator = bv.List(TemplateId_validator, min_items = 1)
TemplateFilterBase._other_validator = bv.Void()
TemplateFilterBase._tagmap = {
    'filter_some': TemplateFilterBase._filter_some_validator,
    'other': TemplateFilterBase._other_validator }
TemplateFilterBase.other = TemplateFilterBase('other')
TemplateFilter._filter_none_validator = bv.Void()
TemplateFilter._tagmap = {
    'filter_none': TemplateFilter._filter_none_validator }
TemplateFilter._tagmap.update(TemplateFilterBase._tagmap)
TemplateFilter.filter_none = TemplateFilter('filter_none')
TemplateOwnerType._user_validator = bv.Void()
TemplateOwnerType._team_validator = bv.Void()
TemplateOwnerType._other_validator = bv.Void()
TemplateOwnerType._tagmap = {
    'user': TemplateOwnerType._user_validator,
    'team': TemplateOwnerType._team_validator,
    'other': TemplateOwnerType._other_validator }
TemplateOwnerType.user = TemplateOwnerType('user')
TemplateOwnerType.team = TemplateOwnerType('team')
TemplateOwnerType.other = TemplateOwnerType('other')
UpdatePropertiesArg.path.validator = PathOrId_validator
UpdatePropertiesArg.update_property_groups.validator = bv.List(PropertyGroupUpdate_validator)
UpdatePropertiesArg._all_field_names_ = set([
    'path',
    'update_property_groups'])
UpdatePropertiesArg._all_fields_ = [
    ('path', UpdatePropertiesArg.path.validator),
    ('update_property_groups', UpdatePropertiesArg.update_property_groups.validator)]
UpdatePropertiesError._property_group_lookup_validator = LookUpPropertiesError_validator
UpdatePropertiesError._tagmap = {
    'property_group_lookup': UpdatePropertiesError._property_group_lookup_validator }
UpdatePropertiesError._tagmap.update(InvalidPropertyGroupError._tagmap)
UpdateTemplateArg.template_id.validator = TemplateId_validator
UpdateTemplateArg.name.validator = bv.Nullable(bv.String())
UpdateTemplateArg.description.validator = bv.Nullable(bv.String())
UpdateTemplateArg.add_fields.validator = bv.Nullable(bv.List(PropertyFieldTemplate_validator))
UpdateTemplateArg._all_field_names_ = set([
    'template_id',
    'name',
    'description',
    'add_fields'])
UpdateTemplateArg._all_fields_ = [
    ('template_id', UpdateTemplateArg.template_id.validator),
    ('name', UpdateTemplateArg.name.validator),
    ('description', UpdateTemplateArg.description.validator),
    ('add_fields', UpdateTemplateArg.add_fields.validator)]
UpdateTemplateResult.template_id.validator = TemplateId_validator
UpdateTemplateResult._all_field_names_ = set([
    'template_id'])
UpdateTemplateResult._all_fields_ = [
    ('template_id', UpdateTemplateResult.template_id.validator)]
PropertiesSearchArg.template_filter.default = TemplateFilter.filter_none
PropertiesSearchQuery.logical_operator.default = LogicalOperator.or_operator
# WARNING: Decompyle incomplete
