# Source Generated with Decompyle++
# File: fql.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class GroupBy(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GroupBy_validator = bv.Struct(GroupBy)

class GroupByFieldRange(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GroupByFieldRange_validator = bv.Struct(GroupByFieldRange)

class GroupBySortOption(bb.Union):
    pass
# WARNING: Decompyle incomplete

GroupBySortOption_validator = bv.Union(GroupBySortOption)

class LeafNode(bb.Struct):
    pass
# WARNING: Decompyle incomplete

LeafNode_validator = bv.Struct(LeafNode)

class MatchType(bb.Union):
    pass
# WARNING: Decompyle incomplete

MatchType_validator = bv.Union(MatchType)

class OperationNode(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OperationNode_validator = bv.Struct(OperationNode)

class Operator(bb.Union):
    pass
# WARNING: Decompyle incomplete

Operator_validator = bv.Union(Operator)

class OrderBy(bb.Struct):
    pass
# WARNING: Decompyle incomplete

OrderBy_validator = bv.Struct(OrderBy)

class RawQuery(bb.Struct):
    pass
# WARNING: Decompyle incomplete

RawQuery_validator = bv.Struct(RawQuery)

class StringMetadata(bb.Struct):
    pass
# WARNING: Decompyle incomplete

StringMetadata_validator = bv.Struct(StringMetadata)

class Token(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Token_validator = bv.Struct(Token)

class Weight(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Weight_validator = bv.Struct(Weight)

class DataUnion(bb.Union):
    pass
# WARNING: Decompyle incomplete

DataUnion_validator = bv.Union(DataUnion)
GroupBy.groupby_field_ids.validator = bv.Nullable(bv.List(bv.Int64()))
GroupBy.groupby_field_ids.validator._redact = bv.BlotRedactor(None)
GroupBy.sort_option.validator = GroupBySortOption_validator
GroupBy.descending_order.validator = bv.Boolean()
GroupBy.descending_order.validator._redact = bv.BlotRedactor(None)
GroupBy.group_by_field_ranges.validator = bv.Nullable(bv.List(GroupByFieldRange_validator))
GroupBy._all_field_names_ = set([
    'groupby_field_ids',
    'sort_option',
    'descending_order',
    'group_by_field_ranges'])
GroupBy._all_fields_ = [
    ('groupby_field_ids', GroupBy.groupby_field_ids.validator),
    ('sort_option', GroupBy.sort_option.validator),
    ('descending_order', GroupBy.descending_order.validator),
    ('group_by_field_ranges', GroupBy.group_by_field_ranges.validator)]
GroupByFieldRange.start_index.validator = bv.Int32()
GroupByFieldRange.start_index.validator._redact = bv.BlotRedactor(None)
GroupByFieldRange.length.validator = bv.UInt32()
GroupByFieldRange.length.validator._redact = bv.BlotRedactor(None)
GroupByFieldRange._all_field_names_ = set([
    'start_index',
    'length'])
GroupByFieldRange._all_fields_ = [
    ('start_index', GroupByFieldRange.start_index.validator),
    ('length', GroupByFieldRange.length.validator)]
GroupBySortOption._count_validator = bv.Void()
GroupBySortOption._key_validator = bv.Void()
GroupBySortOption._other_validator = bv.Void()
GroupBySortOption._tagmap = {
    'count': GroupBySortOption._count_validator,
    'key': GroupBySortOption._key_validator,
    'other': GroupBySortOption._other_validator }
GroupBySortOption.count = GroupBySortOption('count')
GroupBySortOption.key = GroupBySortOption('key')
GroupBySortOption.other = GroupBySortOption('other')
LeafNode.token.validator = bv.Nullable(Token_validator)
LeafNode.field_id.validator = bv.Int64()
LeafNode.field_id.validator._redact = bv.BlotRedactor(None)
LeafNode.match_type.validator = MatchType_validator
LeafNode.range_start_token.validator = bv.Nullable(Token_validator)
LeafNode.range_end_token.validator = bv.Nullable(Token_validator)
LeafNode.vector.validator = bv.Nullable(bv.List(bv.Float32()))
LeafNode.vector.validator._redact = bv.BlotRedactor(None)
LeafNode.vector_score_threshold.validator = bv.Float32()
LeafNode.vector_score_threshold.validator._redact = bv.BlotRedactor(None)
LeafNode.vector_max_magnitude_threshold.validator = bv.Float32()
LeafNode.vector_max_magnitude_threshold.validator._redact = bv.BlotRedactor(None)
LeafNode.weight.validator = bv.Nullable(Weight_validator)
LeafNode._all_field_names_ = set([
    'token',
    'field_id',
    'match_type',
    'range_start_token',
    'range_end_token',
    'vector',
    'vector_score_threshold',
    'vector_max_magnitude_threshold',
    'weight'])
LeafNode._all_fields_ = [
    ('token', LeafNode.token.validator),
    ('field_id', LeafNode.field_id.validator),
    ('match_type', LeafNode.match_type.validator),
    ('range_start_token', LeafNode.range_start_token.validator),
    ('range_end_token', LeafNode.range_end_token.validator),
    ('vector', LeafNode.vector.validator),
    ('vector_score_threshold', LeafNode.vector_score_threshold.validator),
    ('vector_max_magnitude_threshold', LeafNode.vector_max_magnitude_threshold.validator),
    ('weight', LeafNode.weight.validator)]
MatchType._matchtype_unknown_validator = bv.Void()
MatchType._exact_validator = bv.Void()
MatchType._prefix_validator = bv.Void()
MatchType._range_validator = bv.Void()
MatchType._vector_validator = bv.Void()
MatchType._location_validator = bv.Void()
MatchType._other_validator = bv.Void()
MatchType._permissioned_tagmaps = {
    'internal'}
MatchType._tagmap = {
    'matchtype_unknown': MatchType._matchtype_unknown_validator,
    'exact': MatchType._exact_validator,
    'prefix': MatchType._prefix_validator,
    'range': MatchType._range_validator,
    'vector': MatchType._vector_validator,
    'other': MatchType._other_validator }
MatchType._internal_tagmap = {
    'location': MatchType._location_validator }
MatchType.matchtype_unknown = MatchType('matchtype_unknown')
MatchType.exact = MatchType('exact')
MatchType.prefix = MatchType('prefix')
MatchType.range = MatchType('range')
MatchType.vector = MatchType('vector')
MatchType.location = MatchType('location')
MatchType.other = MatchType('other')
OperationNode.operator.validator = Operator_validator
OperationNode.child_operation_nodes.validator = bv.Nullable(bv.List(OperationNode_validator))
OperationNode.child_leaf_nodes.validator = bv.Nullable(bv.List(LeafNode_validator))
OperationNode.raw_query.validator = bv.Nullable(RawQuery_validator)
OperationNode.group_by.validator = bv.Nullable(GroupBy_validator)
OperationNode.order_by.validator = bv.Nullable(OrderBy_validator)
OperationNode.user_specified_operator.validator = bv.Boolean()
OperationNode.user_specified_operator.validator._redact = bv.BlotRedactor(None)
OperationNode._all_field_names_ = set([
    'operator',
    'child_operation_nodes',
    'child_leaf_nodes',
    'raw_query',
    'group_by',
    'order_by',
    'user_specified_operator'])
OperationNode._all_fields_ = [
    ('operator', OperationNode.operator.validator),
    ('child_operation_nodes', OperationNode.child_operation_nodes.validator),
    ('child_leaf_nodes', OperationNode.child_leaf_nodes.validator),
    ('raw_query', OperationNode.raw_query.validator),
    ('group_by', OperationNode.group_by.validator),
    ('order_by', OperationNode.order_by.validator),
    ('user_specified_operator', OperationNode.user_specified_operator.validator)]
Operator._operator_unknown_validator = bv.Void()
Operator._or_op_validator = bv.Void()
Operator._and_op_validator = bv.Void()
Operator._group_by_op_validator = bv.Void()
Operator._order_by_op_validator = bv.Void()
Operator._other_validator = bv.Void()
Operator._tagmap = {
    'operator_unknown': Operator._operator_unknown_validator,
    'or_op': Operator._or_op_validator,
    'and_op': Operator._and_op_validator,
    'group_by_op': Operator._group_by_op_validator,
    'order_by_op': Operator._order_by_op_validator,
    'other': Operator._other_validator }
Operator.operator_unknown = Operator('operator_unknown')
Operator.or_op = Operator('or_op')
Operator.and_op = Operator('and_op')
Operator.group_by_op = Operator('group_by_op')
Operator.order_by_op = Operator('order_by_op')
Operator.other = Operator('other')
OrderBy.sorting_field_id.validator = bv.Int64()
OrderBy.sorting_field_id.validator._redact = bv.BlotRedactor(None)
OrderBy.descending_order.validator = bv.Boolean()
OrderBy.descending_order.validator._redact = bv.BlotRedactor(None)
OrderBy._all_field_names_ = set([
    'sorting_field_id',
    'descending_order'])
OrderBy._all_fields_ = [
    ('sorting_field_id', OrderBy.sorting_field_id.validator),
    ('descending_order', OrderBy.descending_order.validator)]
RawQuery.operator.validator = Operator_validator
RawQuery.raw_query.validator = bv.String()
RawQuery.raw_query.validator._redact = bv.BlotRedactor(None)
RawQuery.field_ids.validator = bv.Nullable(bv.List(bv.Int64()))
RawQuery.field_ids.validator._redact = bv.BlotRedactor(None)
RawQuery.metadata.validator = bv.Nullable(StringMetadata_validator)
RawQuery._all_field_names_ = set([
    'operator',
    'raw_query',
    'field_ids',
    'metadata'])
RawQuery._all_fields_ = [
    ('operator', RawQuery.operator.validator),
    ('raw_query', RawQuery.raw_query.validator),
    ('field_ids', RawQuery.field_ids.validator),
    ('metadata', RawQuery.metadata.validator)]
StringMetadata.value.validator = bv.String()
StringMetadata.value.validator._redact = bv.BlotRedactor(None)
StringMetadata.start.validator = bv.Int32()
StringMetadata.start.validator._redact = bv.BlotRedactor(None)
StringMetadata.dropped.validator = bv.Boolean()
StringMetadata.dropped.validator._redact = bv.BlotRedactor(None)
StringMetadata._all_field_names_ = set([
    'value',
    'start',
    'dropped'])
StringMetadata._all_fields_ = [
    ('value', StringMetadata.value.validator),
    ('start', StringMetadata.start.validator),
    ('dropped', StringMetadata.dropped.validator)]
Token.data.validator = bv.Nullable(DataUnion_validator)
Token.metadata.validator = bv.Nullable(StringMetadata_validator)
Token._all_field_names_ = set([
    'data',
    'metadata'])
Token._all_fields_ = [
    ('data', Token.data.validator),
    ('metadata', Token.metadata.validator)]
Weight.boost.validator = bv.Float32()
Weight.boost.validator._redact = bv.BlotRedactor(None)
Weight._all_field_names_ = set([
    'boost'])
Weight._all_fields_ = [
    ('boost', Weight.boost.validator)]
DataUnion._str_data_validator = bv.String()
DataUnion._str_data_validator._redact = bv.BlotRedactor(None)
DataUnion._int_data_validator = bv.Int64()
DataUnion._int_data_validator._redact = bv.BlotRedactor(None)
DataUnion._double_data_validator = bv.Float64()
DataUnion._double_data_validator._redact = bv.BlotRedactor(None)
DataUnion._bytes_data_validator = bv.Bytes()
DataUnion._other_validator = bv.Void()
DataUnion._tagmap = {
    'str_data': DataUnion._str_data_validator,
    'int_data': DataUnion._int_data_validator,
    'double_data': DataUnion._double_data_validator,
    'bytes_data': DataUnion._bytes_data_validator,
    'other': DataUnion._other_validator }
DataUnion.other = DataUnion('other')
GroupBy.sort_option.default = GroupBySortOption.count
GroupBy.descending_order.default = False
GroupByFieldRange.start_index.default = 0
GroupByFieldRange.length.default = 0
LeafNode.field_id.default = 0
LeafNode.match_type.default = MatchType.matchtype_unknown
LeafNode.vector_score_threshold.default = 0
LeafNode.vector_max_magnitude_threshold.default = 0
OperationNode.operator.default = Operator.operator_unknown
OperationNode.user_specified_operator.default = False
OrderBy.sorting_field_id.default = 0
OrderBy.descending_order.default = False
RawQuery.operator.default = Operator.operator_unknown
RawQuery.raw_query.default = ''
StringMetadata.value.default = ''
StringMetadata.start.default = 0
StringMetadata.dropped.default = False
Weight.boost.default = 0
ROUTES = { }
