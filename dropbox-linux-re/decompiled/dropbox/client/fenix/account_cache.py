# Source Generated with Decompyle++
# File: account_cache.pyc (Python 3.11)

from typing import Dict, Optional, Union
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.multiaccount.role import Roles
from dropbox.exception.reporting import report_bad_assumption
from dropbox.threading import Lock
from dropbox.trace import WARNING
MYPY = False
if MYPY:
    from dropbox.client.fenix.types.account import AuthenticatedAccount, BaseAccount

class FenixAccountCache:
    __account_objects: 'Dict[str, Account]' = { }
    __lock = Lock()
    _key = (lambda cls = None, account_like = None: pass# WARNING: Decompyle incomplete
)()
    register_account = (lambda cls = None, account = None: key = cls._key(account)cls.__lockif key in cls.__account_objects and account is not cls.__account_objects[key]:
WARNING(f'''registered duplicate Account instance for key {key}, overwriting the existing value''')report_bad_assumption('registered duplicate Account instance')cls.__account_objects[key] = accountNone(None, None)Nonewith None:
if not None:
pass)()
    get_account_instance = (lambda cls = None, account_fields = None: key = cls._key(account_fields)cls.__lockNone(None, None)with None:
if not None, cls.__account_objects.get(key):
pass)()
    unregister_account = (lambda cls = None, account = None: key = cls._key(account)cls.__lockif key not in cls.__account_objects:
WARNING(f'''unregistering account {account} but it is not in the cache''')report_bad_assumption('unregistering account but it is not in the cache')None(None, None)NoneNone.__account_objects.pop(key)None(None, None)Nonewith None:
if not None:
pass)()
    update_fields_for_account = (lambda cls = None, account = None, account_fields = classmethod: field_name_mapping = {
'account_id': '_account_id',
'display_name': 'user_display_name',
'first_name': 'user_first_name',
'team_name': 'team' }disallowed_fields = {
'linked',
'host_int',
'is_primary',
'paired_uid',
'host_secret',
'_paired_account_id',
'_paired_host_secret'}for ts_field_name, field_value in account_fields.items():
field_name = field_name_mapping.get(ts_field_name, ts_field_name)if field_name in disallowed_fields:
continueif field_name == 'role':
account.role = Roles.PERSONAL if field_value == 'personal' else Roles.BUSINESScontinueif hasattr(account, field_name):
setattr(account, field_name, field_value)continueWARNING('field %r does not exist on Account', field_name)None)()

