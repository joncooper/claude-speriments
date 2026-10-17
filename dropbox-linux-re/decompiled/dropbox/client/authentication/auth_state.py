# Source Generated with Decompyle++
# File: auth_state.pyc (Python 3.11)

from typing import Optional
from dropbox.assertions import assert_
from dropbox.client.authentication.account import Account
from dropbox.client.setup_wizard.account_link_state import LinkPreferences

class AuthState:
    
    def __init__(self = None, account = None, paired_account = None):
        pass
    # WARNING: Decompyle incomplete

    linked = (lambda self = None: self._account.linked)()
    account = (lambda self = None: self._account)()
    paired_account = (lambda self = None: self._paired_account)()
    preferences = (lambda self = None: self._link_preferences)()

