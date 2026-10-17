# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod, abstractproperty
from typing import cast, Dict, List, Optional
from six import add_metaclass
from account_model import AccountModel
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.exception.reporting import report_assertion_error
from dropbox.foundation.account_manager.bridge_gen.account_update_type import AccountUpdateType
from dropbox.foundation.account_manager.bridge_gen.bridge_interface_account_manager import AccountManagerBridgeInterface
from dropbox.foundation.account_manager.bridge_gen.bridge_interface_account_update import AccountUpdateBridgeInterface
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.signals import Signal

class AccountUpdate(AccountUpdateBridgeInterface):
    
    def __init__(self = None, update_type = None, account = None, context = ('update_type', 'AccountUpdateType', 'account', 'AccountInterface', 'context', 'Optional[UserContext]', 'return', 'None')):
        self._type = update_type
        self._account = account
        self._context = context

    type = (lambda self = None: self._type)()
    context = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    account = (lambda self = None: cast(Account, self._account))()
    
    def get_context(self = None):
        pass
    # WARNING: Decompyle incomplete


AccountManager = <NODE:12>()
