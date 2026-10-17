# Source Generated with Decompyle++
# File: async_.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class LaunchResultBase(bb.Union):
    pass
# WARNING: Decompyle incomplete

LaunchResultBase_validator = bv.Union(LaunchResultBase)

class LaunchEmptyResult(LaunchResultBase):
    pass
# WARNING: Decompyle incomplete

LaunchEmptyResult_validator = bv.Union(LaunchEmptyResult)

class PollArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

PollArg_validator = bv.Struct(PollArg)

class PollResultBase(bb.Union):
    pass
# WARNING: Decompyle incomplete

PollResultBase_validator = bv.Union(PollResultBase)

class PollEmptyResult(PollResultBase):
    pass
# WARNING: Decompyle incomplete

PollEmptyResult_validator = bv.Union(PollEmptyResult)

class PollError(bb.Union):
    pass
# WARNING: Decompyle incomplete

PollError_validator = bv.Union(PollError)
AsyncJobId_validator = bv.String(min_length = 1)
AsyncJobId_validator._redact = bv.BlotRedactor(None)
LaunchResultBase._async_job_id_validator = AsyncJobId_validator
LaunchResultBase._tagmap = {
    'async_job_id': LaunchResultBase._async_job_id_validator }
LaunchEmptyResult._complete_validator = bv.Void()
LaunchEmptyResult._tagmap = {
    'complete': LaunchEmptyResult._complete_validator }
LaunchEmptyResult._tagmap.update(LaunchResultBase._tagmap)
LaunchEmptyResult.complete = LaunchEmptyResult('complete')
PollArg.async_job_id.validator = AsyncJobId_validator
PollArg._all_field_names_ = set([
    'async_job_id'])
PollArg._all_fields_ = [
    ('async_job_id', PollArg.async_job_id.validator)]
PollResultBase._in_progress_validator = bv.Void()
PollResultBase._tagmap = {
    'in_progress': PollResultBase._in_progress_validator }
PollResultBase.in_progress = PollResultBase('in_progress')
PollEmptyResult._complete_validator = bv.Void()
PollEmptyResult._tagmap = {
    'complete': PollEmptyResult._complete_validator }
PollEmptyResult._tagmap.update(PollResultBase._tagmap)
PollEmptyResult.complete = PollEmptyResult('complete')
PollError._invalid_async_job_id_validator = bv.Void()
PollError._internal_error_validator = bv.Void()
PollError._other_validator = bv.Void()
PollError._tagmap = {
    'invalid_async_job_id': PollError._invalid_async_job_id_validator,
    'internal_error': PollError._internal_error_validator,
    'other': PollError._other_validator }
PollError.invalid_async_job_id = PollError('invalid_async_job_id')
PollError.internal_error = PollError('internal_error')
PollError.other = PollError('other')
ROUTES = { }
