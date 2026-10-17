# Source Generated with Decompyle++
# File: selector.pyc (Python 3.11)

from typing import Iterable, List, Optional, Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ui.common.strings import AccountString

class MultiAccountSelector(object):
    
    def __init__(self, description_text, choose_dropbox_text, personal_string = None, business_string = None, force_choice_caption = None, force_choice_text = ('description_text', 'Text', 'choose_dropbox_text', 'Text', 'personal_string', 'Text', 'business_string', 'Text', 'force_choice_caption', 'Text', 'force_choice_text', 'Text', 'return', 'None')):
        self._text = description_text
        self._choose_dropbox_text = choose_dropbox_text
        self._force_choice_title = force_choice_caption
        self._force_choice_text = force_choice_text
        self._personal_string = personal_string
        self._business_string = business_string
        self._disabled_role = None

    build_from_account_manager = (lambda text, choose_dropbox_text, dropbox_choice_string = None, force_choice_title = None, force_choice_text = staticmethod, account_manager = ('text', 'Text', 'choose_dropbox_text', 'Text', 'dropbox_choice_string', 'AccountString', 'force_choice_title', 'Text', 'force_choice_text', 'Text', 'account_manager', 'AccountManagerInterface', 'return', 'MultiAccountSelector'): pass# WARNING: Decompyle incomplete
)()
    build_from_accounts = (lambda text, choose_dropbox_text, dropbox_choice_string, force_choice_title = None, force_choice_text = None, disabled_message = staticmethod, accounts = ('text', 'Text', 'choose_dropbox_text', 'Text', 'dropbox_choice_string', 'AccountString', 'force_choice_title', 'Text', 'force_choice_text', 'Text', 'disabled_message', 'Optional[AccountString]', 'accounts', 'Iterable[Tuple[AccountInterface, bool]]', 'return', 'MultiAccountSelector'): personal_string = Nonebusiness_string = Nonedisabled_account = None# WARNING: Decompyle incomplete
)()
    
    def set_disabled(self = None, account = None, disabled_message = None):
        self._disabled_role = account.role
        if disabled_message:
            self._text = account.render_string(disabled_message, assume_paired = True)
            return None

    text = (lambda self = None: self._text)()
    force_choice_title = (lambda self = None: self._force_choice_title)()
    force_choice_text = (lambda self = None: self._force_choice_text)()
    selections = (lambda self = None: if self._disabled_role == Roles.BUSINESS:
[
self._personal_string]if None._disabled_role == Roles.PERSONAL:
[
self._business_string][
None._choose_dropbox_text,
self._personal_string,
self._business_string])()
    default_index = (lambda self = None: 0)()
    
    def translate_index(self = None, index = None):
        pass
    # WARNING: Decompyle incomplete


