# Source Generated with Decompyle++
# File: check.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class EchoArg(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EchoArg_validator = bv.Struct(EchoArg)

class EchoError(bb.Union):
    pass
# WARNING: Decompyle incomplete

EchoError_validator = bv.Union(EchoError)

class EchoResult(bb.Struct):
    pass
# WARNING: Decompyle incomplete

EchoResult_validator = bv.Struct(EchoResult)
EchoArg.query.validator = bv.String(max_length = 500)
EchoArg.query.validator._redact = bv.BlotRedactor(None)
EchoArg.trigger_error.validator = bv.Boolean()
EchoArg.trigger_error.validator._redact = bv.BlotRedactor(None)
EchoArg._all_field_names_ = set([
    'query'])
EchoArg._all_fields_ = [
    ('query', EchoArg.query.validator)]
EchoArg._all_internal_field_names_ = set([
    'trigger_error'])
EchoArg._all_internal_fields_ = [
    ('trigger_error', EchoArg.trigger_error.validator)]
EchoError._user_requested_validator = bv.Void()
EchoError._other_validator = bv.Void()
EchoError._tagmap = {
    'user_requested': EchoError._user_requested_validator,
    'other': EchoError._other_validator }
EchoError.user_requested = EchoError('user_requested')
EchoError.other = EchoError('other')
EchoResult.result.validator = bv.String()
EchoResult.result.validator._redact = bv.BlotRedactor(None)
EchoResult.secret.validator = bv.String()
EchoResult.secret.validator._redact = bv.BlotRedactor(None)
EchoResult._all_field_names_ = set([
    'result'])
EchoResult._all_fields_ = [
    ('result', EchoResult.result.validator)]
EchoResult._all_internal_field_names_ = set([
    'secret'])
EchoResult._all_internal_fields_ = [
    ('secret', EchoResult.secret.validator)]
EchoArg.query.default = ''
EchoArg.trigger_error.default = False
EchoResult.result.default = ''
EchoResult.secret.default = ''
# WARNING: Decompyle incomplete
