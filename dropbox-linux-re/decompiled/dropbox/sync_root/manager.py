# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

import time
from typing import Callable, cast, Dict, List, Mapping, MutableMapping, Optional, Set
from build_number import BUILD_KEY, dropbox_version
from build_number.features import feature_enabled
from constants import SyncRootConstants
from events.reporter import report_sync_root_event
from events.types import ExtraInfo, SyncRootEvent, SyncRootEventType
from gating import cloud_files_capable, file_provider_supported
from handlers.debug import _DebugRootHandler
from handlers.interface import _SyncRootHandler
from interface import SyncRootManagerInterface
from types import RemovalMode, SyncRootCreationResult, SyncRootHydrationPolicy, SyncRootInfo, SyncRootInvalid, SyncRootNotInitialized, SyncRootRepairAction, SyncRootType, SyncRootTypeInvalid
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.gandalf import Gandalf
from dropbox.client.util import hard_exit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.threading import Lock
from dropbox.trace import TRACE

def _to_account(account = None):
    return cast(Account, account)


class SyncRootManager(SyncRootManagerInterface):
    
    def __init__(self = None, config_manager = None):
        TRACE('[RootManager] Initializing')
        self._config_manager = config_manager
        self._state_lock = Lock()
        self._account_to_handler = dict()
        self._last_root_consistency_check = None
        self._debug_default_granted_state = True

    
    def __make_handler(self = None, account = None, root_type = None, local_config = ('account', 'AccountInterface', 'root_type', 'SyncRootType', 'local_config', 'Optional[LocalConfigurationInterface]', 'return', '_SyncRootHandler')):
        pass
    # WARNING: Decompyle incomplete

    
    def __make_handler_from_config(self = None, config_dict = None, is_primary = None, local_config = ('config_dict', 'MutableMapping', 'is_primary', 'bool', 'local_config', 'LocalConfigurationInterface', 'return', 'Optional[_SyncRootHandler]')):
        account = Account()
        account._account_id = config_dict.get('account_id')
        account.uid = config_dict.get(SyncRootConstants.CONFIG_KEY_ACCOUNT_UID)
        account.is_primary = is_primary
        root_type = self.__get_root_type_for_config(config_dict)
    # WARNING: Decompyle incomplete

    
    def __get_root_type_for_account(self = None, account = None):
        local_config = self._config_manager.local_config(account)
    # WARNING: Decompyle incomplete

    __get_root_type_for_config = (lambda config_dict = None: _type = config_dict.get(SyncRootConstants.CONFIG_KEY_SYNC_ROOT_TYPE)TRACE('[RootManager] sync root type from config: %r', _type)# WARNING: Decompyle incomplete
)()
    
    def __get_handler_for_account(self = None, account = None):
        account = _to_account(account)
        ret = self._account_to_handler.get(account)
    # WARNING: Decompyle incomplete

    
    def _create_handler_for_account(self = None, account = None, root_type = None):
        self._state_lock
        ret = self.__get_handler_for_account(account)
    # WARNING: Decompyle incomplete

    
    def _get_handler_for_account(self = None, account = None):
        self._state_lock
        ret = self.__get_handler_for_account(account)
        None(None, None)
    # WARNING: Decompyle incomplete

    
    def _set_handler_for_account(self = None, account = None, handler = None):
        TRACE('[RootManager] setting handler %r for account %s', handler, account.uid)
        self._state_lock
        self.__set_root_info_for_account(account, handler.root_type())
        account = _to_account(account)
        self._account_to_handler[account] = handler
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def __set_root_info_for_account(self = None, account = None, root_type = None):
        local_config = self._config_manager.local_config(account)
    # WARNING: Decompyle incomplete

    __set_handler_in_config = (lambda account = None, root_type = None, config_dict = staticmethod: pass# WARNING: Decompyle incomplete
)()
    
    def _delete_handler_for_account(self = None, account = None):
        TRACE('[RootManager] removing handler for account %s', account.uid)
        self._state_lock
        local_config = self._config_manager.local_config(account)
    # WARNING: Decompyle incomplete

    __delete_handler_from_config = (lambda config_dict = None: del config_dict[SyncRootConstants.CONFIG_KEY_SYNC_ROOT_TYPE]del config_dict[SyncRootConstants.CONFIG_KEY_ACCOUNT_UID]del config_dict[SyncRootConstants.CONFIG_KEY_SYNC_ROOT_CREATION_TIMESTAMP])()
    
    def create_root(self, account = None, root_type = None, root_display_name = None, root_parent_path = (None, SyncRootHydrationPolicy.FULL), hydration_policy = ('account', 'AccountInterface', 'root_type', 'SyncRootType', 'root_display_name', 'str', 'root_parent_path', 'Optional[str]', 'hydration_policy', 'SyncRootHydrationPolicy', 'return', 'Future[None]')):
        
        try:
            TRACE('[RootManager] create_root of type %s with display name %s for account %s. parent path: %s', root_type.name, root_display_name, account, root_parent_path)
            handler = self._create_handler_for_account(account, root_type)
            return handler.register(root_display_name, root_parent_path, hydration_policy = hydration_policy)
        except Exception:
            return 


    
    def convert_root(self, account = None, target_root_type = None, root_display_name = None, root_parent_path = (SyncRootHydrationPolicy.FULL,), hydration_policy = ('account', 'AccountInterface', 'target_root_type', 'SyncRootType', 'root_display_name', 'str', 'root_parent_path', 'str', 'hydration_policy', 'SyncRootHydrationPolicy', 'return', 'Future[Optional[SyncRootCreationResult]]')):
        pass
    # WARNING: Decompyle incomplete

    
    def destroy_root(self = None, account = None, mode = None):
        pass
    # WARNING: Decompyle incomplete

    
    def destroy_root_from_config(self = None, local_config = None, is_primary = None, mode = ('local_config', 'LocalConfigurationInterface', 'is_primary', 'bool', 'mode', 'RemovalMode', 'return', 'Future[Optional[str]]')):
        pass
    # WARNING: Decompyle incomplete

    
    def get_root_info(self = None, account = None):
        pass
    # WARNING: Decompyle incomplete

    
    def check_root_consistency(self = None, account = None):
        TRACE('[RootManager] Checking root consistency for account %r', account)
        now = time.time()
        if self._last_root_consistency_check and now - self._last_root_consistency_check < SyncRootConstants.ROOT_CONSISTENCY_INTERVAL_SECONDS:
            TRACE('[RootManager] Too soon to check. Return early')
            return ResolvedFuture(None)
        self._last_root_consistency_check = None
        
        try:
            handler = self._get_handler_for_account(account)
        except SyncRootNotInitialized:
            TRACE('[RootManager] check_root_consistency before root initialized, returning None')
            return 
            except Exception:
                return 

    # WARNING: Decompyle incomplete

    
    def repair_root(self = None, account = None, action = None):
        
        try:
            handler = self._get_handler_for_account(account)
        except Exception:
            return 

    # WARNING: Decompyle incomplete

    
    def set_hydration_policy(self = None, account = None, desired = None):
        TRACE('[RootManager] set_hydration_policy %r for account %r', desired, account)
        
        try:
            handler = self._get_handler_for_account(account)
        except Exception:
            return 

    # WARNING: Decompyle incomplete

    
    def get_root_type(self = None, account = None):
        TRACE('[RootManager] get_type for account %r', account)
        
        try:
            handler = self._get_handler_for_account(account)
        except SyncRootNotInitialized:
            return 

        return ResolvedFuture(handler.root_type())

    
    def get_root_creation_timestamp(self = None, account = None):
        TRACE('[RootManager] get_root_creation_timestamp for account %r', account)
        local_config = self._config_manager.local_config(account)
    # WARNING: Decompyle incomplete

    
    def is_root_enabled(self = None, account = None):
        TRACE('[RootManager] is_root_enabled called for account %s', account)
        
        try:
            handler = self._get_handler_for_account(account)
        except Exception:
            TRACE('Failed to get root state')
            return 

        return handler.is_root_enabled()

    
    def show_consent_window(self = None, account = None):
        handler = self._get_handler_for_account(account)
        return handler.show_consent_window()

    
    def get_known_accounts(self = None):
        return ResolvedFuture(list(self._account_to_handler.keys()))

    
    def check_global_consistency(self = None, gandalf = None):
        pass
    # WARNING: Decompyle incomplete

    
    def register_root_change_listener(self = None, account = None, on_root_change = None):
        
        try:
            handler = self._get_handler_for_account(account)
            handler.register_root_change_listener(on_root_change)
            return None
        except Exception:
            TRACE('Failed to register domain listener')
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SYNC_ENGINE)
            if dropbox_version.is_internal_alpha():
                hard_exit(ExitCode.FAILURE, reason = 'Failed to register domain listener')
                return None
            return None


    
    def _unregister_root_change_listener(self = None, account = None):
        
        try:
            handler = self._get_handler_for_account(account)
            handler.unregister_root_change_listener()
            return None
        except Exception:
            TRACE('Failed to unregister domain listener')
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.SYNC_ENGINE)
            return None


    
    def unregister_all_root_listeners(self = None):
        for account in self._account_to_handler:
            self._unregister_root_change_listener(account)
            return None

    
    def get_non_consented_accounts(self = None):
        pass
    # WARNING: Decompyle incomplete

    is_debug = (lambda self = None: 