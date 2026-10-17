# Source Generated with Decompyle++
# File: version_tree.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv

class Hlc(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Hlc_validator = bv.Struct(Hlc)

class Oid(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Oid_validator = bv.Struct(Oid)

class Sid(bb.Struct):
    pass
# WARNING: Decompyle incomplete

Sid_validator = bv.Struct(Sid)
Hlc.unix_micros.validator = bv.UInt64()
Hlc.unix_micros.validator._redact = bv.BlotRedactor(None)
Hlc._all_field_names_ = set([
    'unix_micros'])
Hlc._all_fields_ = [
    ('unix_micros', Hlc.unix_micros.validator)]
Oid.val.validator = bv.UInt64()
Oid.val.validator._redact = bv.BlotRedactor(None)
Oid._all_field_names_ = set([
    'val'])
Oid._all_fields_ = [
    ('val', Oid.val.validator)]
Sid.val.validator = bv.UInt64()
Sid.val.validator._redact = bv.BlotRedactor(None)
Sid._all_field_names_ = set([
    'val'])
Sid._all_fields_ = [
    ('val', Sid.val.validator)]
Hlc.unix_micros.default = 0
Oid.val.default = 0
Sid.val.default = 0
ROUTES = { }
