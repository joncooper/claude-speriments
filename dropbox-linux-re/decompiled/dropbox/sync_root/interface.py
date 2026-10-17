# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Callable, List, Optional
from types import RemovalMode, SyncRootCreationResult, SyncRootHydrationPolicy, SyncRootInfo, SyncRootRepairAction, SyncRootType
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.gandalf import Gandalf
from dropbox.foundation.futures import Future

class SyncRootConsentInterface(ABC):
    is_root_enabled = (lambda self = None, account = None: pass)()
    get_known_accounts = (lambda self = None: pass)()
    get_non_consented_accounts = (lambda self = None: pass)()


class GetSyncRootTypeInterface(ABC):
    get_root_type = (lambda self = None, account = None: pass)()


class SyncRootManagerInterface(SyncRootConsentInterface, GetSyncRootTypeInterface):
    create_root = (lambda self, account = None, root_type = None, root_display_name = abstractmethod, root_parent_path = (None, SyncRootHydrationPolicy.FULL), hydration_policy = ('account', 'AccountInterface', 'root_type', 'SyncRootType', 'root_display_name', 'str', 'root_parent_path', 'Optional[str]', 'hydration_policy', 'SyncRootHydrationPolicy', 'return', 'Future[None]'): pass)()
    convert_root = (lambda self, account = None, target_root_type = None, root_display_name = abstractmethod, root_parent_path = (SyncRootHydrationPolicy.FULL,), hydration_policy = ('account', 'AccountInterface', 'target_root_type', 'SyncRootType', 'root_display_name', 'str', 'root_parent_path', 'str', 'hydration_policy', 'SyncRootHydrationPolicy', 'return', 'Future[Optional[SyncRootCreationResult]]'): pass)()
    destroy_root = (lambda self = None, account = None, mode = abstractmethod: pass)()
    destroy_root_from_config = (lambda self = None, local_config = None, is_primary = abstractmethod, mode = ('local_config', 'LocalConfigurationInterface', 'is_primary', 'bool', 'mode', 'RemovalMode', 'return', 'Future[Optional[str]]'): pass)()
    get_root_info = (lambda self = None, account = None: pass)()
    get_root_creation_timestamp = (lambda self = None, account = None: pass)()
    is_root_enabled = (lambda self = None, account = None: pass)()
    show_consent_window = (lambda self = None, account = None: pass)()
    get_known_accounts = (lambda self = None: pass)()
    check_root_consistency = (lambda self = None, account = None: pass)()
    repair_root = (lambda self = None, account = None, action = abstractmethod: pass)()
    set_hydration_policy = (lambda self = None, account = None, desired = abstractmethod: pass)()
    check_global_consistency = (lambda self = None, gandalf = None: pass)()
    register_root_change_listener = (lambda self = None, account = None, on_root_change = abstractmethod: pass)()
    unregister_all_root_listeners = (lambda self = None: pass)()
    is_debug = (lambda self = None: pass)()()
    
    def debug_grant_all_consent(self = None):
        pass

    
    def debug_revoke_all_consent(self = None):
        pass

    
    def debug_set_consent(self = None, account = None, granted = None):
        pass

    
    def debug_set_consent_window(self = None, func = None):
        pass


