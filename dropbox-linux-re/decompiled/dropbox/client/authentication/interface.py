# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Callable, List, Optional, Set, Text, Tuple
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.auth_state import AuthState
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.multiaccount.constants import Role
from dropbox.foundation.futures import Future
from dropbox.foundation.runtime import ExitCode
from dropbox.sync_root.types import SyncRootType, SyncRootTypeReason
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import LocalConfigurationInterface
    from dropbox.client.gandalf import Gandalf
    from dropbox.client.notifications.legacy_notifications import PairedUserNotification
    from dropbox.client_api.dropbox_connection import DropboxConnection
ACCOUNTS_CHANGED_PRIORITY_POLARIS_ACCOUNT_MANAGER = 105
ACCOUNTS_CHANGED_PRIORITY_GANDALF = 100
ACCOUNTS_CHANGED_PRIORITY_EVENTS = 90
AccountChangeCallback = Callable[([
    Account,
    AccountChangeType], None)]

def AccountManagerInterface():
    '''AccountManagerInterface'''
    load_known_accounts = (lambda self = None, on_link_complete = None: pass)()
    unlink = (lambda self = None, account = None: pass)()
    add_account = (lambda self = None, account = None, primary = abstractmethod: pass)()
    on_account_linked = (lambda self = None, account = None: pass)()
    handle_paired_notification = (lambda self = None, notification = None: pass)()
    get_account = (lambda self = None, host_int = None: pass)()
    account_for_uid = (lambda self = None, uid = None: pass)()
    add_accounts_changed_callback = (lambda self = None, callback = None, event_filter = abstractmethod, priority = (0, 0): pass)()
    remove_accounts_changed_callback = (lambda self = None, callback = None: pass)()
    add_known_accounts_linked_callback = (lambda self = None, callback = None, priority = abstractmethod: pass)()
    remove_known_accounts_linked_callback = (lambda self = None, callback = None: pass)()
    add_multiaccount_linking_enabled_changed_callback = (lambda self = None, callback = None: pass)()
    remove_multiaccount_linking_enabled_changed_callback = (lambda self = None, callback = None: pass)()
    get_new_sync_root_type = (lambda self = None, account = None, local_config = abstractmethod, gandalf = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'gandalf', 'Gandalf', 'return', 'Tuple[SyncRootType, Set[SyncRootType], SyncRootTypeReason]'): pass)()
    is_standard_dropbox_location = (lambda self = None, path = None: pass)()
    get_valid_path_in_unlink_cookie = (lambda self = None, account = None, local_config = abstractmethod: pass)()
    get_new_dropbox_location = (lambda self = None, account = None, local_config = abstractmethod, override_path = (None, True), use_cookie = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'override_path', 'Optional[str]', 'use_cookie', 'bool', 'return', 'str'): pass)()
    get_current_dropbox_name = (lambda self = None, account = None, suffix = abstractmethod: pass)()
    generate_fp_domain_display_name = (lambda self = None, account = None: pass)()
    generate_dropbox_name = (lambda self = None, account = None, suffix = abstractmethod: pass)()
    
    def account_for_role(self = None, role = None):
        pass

    
    def can_link_secondary(self = None):
        pass

    has_configured_non_primary_accounts = (lambda self = None: pass)()
    linked_accounts_all = (lambda self = None: pass)()
    linked_accounts = (lambda self = None: pass)()
    personal = (lambda self = None: pass)()
    business = (lambda self = None: pass)()
    primary = (lambda self = None: pass)()
    secondary = (lambda self = None: pass)()
    is_paired = (lambda self = None: pass)()
    paired_pending_link = (lambda self = None: pass)()
    paired_pending_link = (lambda self = None, val = None: pass)()
    ensure_paired_pending_link_for_account = (lambda self = None, account_id = None, conn = abstractmethod: pass)()
    get_display_name_account_component = (lambda self = None, account = None, unsanitized_name_replacement = abstractmethod: pass)()
    disable_async_startup = (lambda self = None: pass)()
    disable_async_startup_on_bad_exit = (lambda self = None, exit_code = None: pass)()
    update_multiaccount_linking_enabled = (lambda self = None, linking_enabled = None: pass)()

AccountManagerInterface = <NODE:27>(AccountManagerInterface, 'AccountManagerInterface', metaclass = ABCMeta)

def LinkControllerInterface():
    '''LinkControllerInterface'''
    link_account = (lambda self = None, unlinked_account = None, done_callback = None, linked_on_server = abstractmethod, setup_wizard_ui_appeared_callback = (False, None), *, is_pairing, 