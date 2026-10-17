# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from typing import Any, Callable, cast, Dict, FrozenSet, List, Optional, TypeVar, Union
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountId
from dropbox.client.features.sync_everything.v3.async_tools import IdentityFutureProtocol
from dropbox.client.fenix.account_cache import FenixAccountCache
from dropbox.client.fenix.types.account import AuthenticatedAccount, LocalAccount
from dropbox.client.multiaccount.role import Roles
from dropbox.exception.reporting import assert_not_none
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.electron.ipc import JSONDict
T = TypeVar('T')

def fenix_api(required_args = None):
    pass
# WARNING: Decompyle incomplete


def get_user_context_from_account_id(machine_context = None, account_id = None):
    account_models = machine_context.account_manager.account_models
    for account, model in account_models.items():
        if account.account_id == AccountId(account_id):
            
            return None, model.user_context
        return None


def get_account_linked_or_from_cache(account_or_id = None, account_manager = None, legacy_account_manager = None):
    pass
# WARNING: Decompyle incomplete


def convert_to_local_account(account = None):
    pass
# WARNING: Decompyle incomplete

