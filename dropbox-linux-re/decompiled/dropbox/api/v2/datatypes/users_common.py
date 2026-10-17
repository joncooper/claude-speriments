# Source Generated with Decompyle++
# File: users_common.pyc (Python 3.11)

from __future__ import unicode_literals
from stone.backends.python_rsrc import stone_base as bb
from stone.backends.python_rsrc import stone_validators as bv
from dropbox.api.v2.datatypes import account_id

class AccountType(bb.Union):
    pass
# WARNING: Decompyle incomplete

AccountType_validator = bv.Union(AccountType)
AccountId_validator = bv.String(min_length = 40, max_length = 40)
AccountId_validator._redact = bv.HashRedactor(None)
AccountType._basic_validator = bv.Void()
AccountType._pro_validator = bv.Void()
AccountType._business_validator = bv.Void()
AccountType._tagmap = {
    'basic': AccountType._basic_validator,
    'pro': AccountType._pro_validator,
    'business': AccountType._business_validator }
AccountType.basic = AccountType('basic')
AccountType.pro = AccountType('pro')
AccountType.business = AccountType('business')
ROUTES = { }
