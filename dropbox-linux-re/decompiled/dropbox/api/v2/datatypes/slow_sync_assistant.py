# Source Generated with Decompyle++
# File: slow_sync_assistant.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import version_tree

class GetFileCountByNsArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileCountByNsArg_validator = bv.Struct(GetFileCountByNsArg)

class GetFileCountByNsError(bb.Union):
    pass
# WARNING: Decompyle incomplete

GetFileCountByNsError_validator = bv.Union(GetFileCountByNsError)

class GetFileCountByNsResponse(bb.Struct):
    pass
# WARNING: Decompyle incomplete

GetFileCountByNsResponse_validator = bv.Struct(GetFileCountByNsResponse)
GetFileCountByNsArg.ns_id.validator = bv.UInt64()
GetFileCountByNsArg.ns_id.validator._redact = bv.BlotRedactor(None)
GetFileCountByNsArg.hlc.validator = bv.Nullable(version_tree.Hlc_validator)
GetFileCountByNsArg._all_field_names_ = set([
    'ns_id',
    'hlc'])
GetFileCountByNsArg._all_fields_ = [
    ('ns_id', GetFileCountByNsArg.ns_id.validator),
    ('hlc', GetFileCountByNsArg.hlc.validator)]
GetFileCountByNsError._namespace_not_mounted_by_user_validator = bv.Void()
GetFileCountByNsError._invalid_namespace_validator = bv.Void()
GetFileCountByNsError._other_validator = bv.Void()
GetFileCountByNsError._tagmap = {
    'namespace_not_mounted_by_user': GetFileCountByNsError._namespace_not_mounted_by_user_validator,
    'invalid_namespace': GetFileCountByNsError._invalid_namespace_validator,
    'other': GetFileCountByNsError._other_validator }
GetFileCountByNsError.namespace_not_mounted_by_user = GetFileCountByNsError('namespace_not_mounted_by_user')
GetFileCountByNsError.invalid_namespace = GetFileCountByNsError('invalid_namespace')
GetFileCountByNsError.other = GetFileCountByNsError('other')
GetFileCountByNsResponse.ns_id.validator = bv.UInt64()
GetFileCountByNsResponse.ns_id.validator._redact = bv.BlotRedactor(None)
GetFileCountByNsResponse.file_count.validator = bv.UInt64()
GetFileCountByNsResponse.file_count.validator._redact = bv.BlotRedactor(None)
GetFileCountByNsResponse._all_field_names_ = set([
    'ns_id',
    'file_count'])
GetFileCountByNsResponse._all_fields_ = [
    ('ns_id', GetFileCountByNsResponse.ns_id.validator),
    ('file_count', GetFileCountByNsResponse.file_count.validator)]
GetFileCountByNsArg.ns_id.default = 0
GetFileCountByNsResponse.ns_id.default = 0
GetFileCountByNsResponse.file_count.default = 0
# WARNING: Decompyle incomplete
