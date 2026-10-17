# Source Generated with Decompyle++
# File: account.pyc (Python 3.11)

from typing import Any, Dict, List, Optional, TypedDict
MYPY = False
if MYPY:
    from dropbox.client.fenix.authentication_service import FenixRegisterHostResponse

class BaseAccount(TypedDict):
    client_uuid: 'str' = 'BaseAccount'


class ServerAccount(TypedDict):
    team_name: 'Optional[str]' = 'ServerAccount'


class QuotaInfo(TypedDict):
    root_quota: 'int' = 'QuotaInfo'


class AuthenticatedAccount(BaseAccount, ServerAccount):
    disable_multiaccount_link: 'Optional[bool]' = 'AuthenticatedAccount'


class LocalAccount(AuthenticatedAccount):
    pass


class AccountChangeArgs(TypedDict):
    accountChangeType: 'int' = 'AccountChangeArgs'


class FenixLinkPreferences(TypedDict):
    selected_file_count: 'Optional[int]' = 'FenixLinkPreferences'


class RegisterLocallyAuthenticatedAccountArgs(TypedDict):
    enabled_variants: 'List[str]' = 'RegisterLocallyAuthenticatedAccountArgs'


class InitializeMinimalAuthenticatedServicesArgs(TypedDict):
    register_host_response: 'FenixRegisterHostResponse' = 'InitializeMinimalAuthenticatedServicesArgs'

