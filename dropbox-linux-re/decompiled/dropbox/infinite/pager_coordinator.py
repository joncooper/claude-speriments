# Source Generated with Decompyle++
# File: pager_coordinator.pyc (Python 3.11)

from enum import Enum
from typing import Callable, Dict, List, Optional
from build_number.features import feature_enabled
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.periodic import JobNameAlreadyExistsError
from dropbox.db_thread import db_thread
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.infinite import infinite_release_channel
from dropbox.infinite.kernel_component_manager import KernelComponentManager
from dropbox.infinite.pager import PagerNotLoadedError
from dropbox.infinite.paging_thread import PagingThread
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.gandalf import Gandalf
    from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
    from dropbox.infinite.blacklist import InfiniteModuleBlacklist, InfiniteRecallBlacklist
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class InfinitePagerDriverState(Enum):
    CONNECTED = 'connected'
    INCOMPATIBLE = 'incompatible'
    RUNNING = 'running'
    INSTALLED = 'installed'
    NOT_INSTALLED = 'not_installed'
    NOT_NEEDED = 'not_needed'


class InfinitePagerCoordinator(object):
    
    def __init__(self, sync_engine_adapter, account_manager = None, tray_menu_controller = None, gandalf = None, log_pager_state = ('sync_engine_adapter', 'SyncEngineAdapter', 'account_manager', 'AccountManagerInterface', 'tray_menu_controller', 'TrayMenuController', 'gandalf', 'Gandalf', 'log_pager_state', 'Callable[[], None]', 'return', 'None')):
        self._sync_engine_adapter = sync_engine_adapter
        self._account_manager = account_manager
        self._tray_menu_controller = tray_menu_controller
        self._gandalf = gandalf
        self._log_pager_state = log_pager_state
        self._recall_blacklist = None
        self._module_blacklist = None
        self._controller_lock = Lock()
        self._infinite_enabled = False
        release_channel = infinite_release_channel(self._gandalf)
        self._kernel_component_manager = KernelComponentManager.create(release_channel)
        self._paging_thread_map = { }
        self._callbacks_added = False
        self._need_mitigation = False

    infinite_enabled = (lambda self = None: self._infinite_enabled)()
    need_mitigation = (lambda self = None: self._need_mitigation)()
    
    def enable_infinite_if_needed(self = None):
        self._controller_lock
    # WARNING: Decompyle incomplete

    
    def disable_infinite_if_needed(self = None):
        self._controller_lock
        self._infinite_enabled = False
    # WARNING: Decompyle incomplete

    
    def update_recall_blacklist(self = None, recall_blacklist = None):
        self._controller_lock
        self._recall_blacklist = recall_blacklist
        for _, paging_thread in self._paging_thread_map.items():
            paging_thread.pager.recall_blacklist = recall_blacklist
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    kernel_components_compatible = (lambda module_blacklist = None: KernelComponentManager.kernel_components_compatible(module_blacklist))()
    
    def status_for_account(self = None, account = None):
        self._controller_lock
        if not self._kernel_component_manager:
            None(None, None)
            return 
        if paging_thread and paging_thread.connected:
            None(None, None)
            return 
        if None._paging_thread_map.get(account)._kernel_component_manager.is_running():
            None(None, None)
            return 
        if None._kernel_component_manager.is_installed():
            None(None, None)
            return 
        None(None, None)
        return 
        with None:
            if not None, None.NOT_INSTALLED:
                pass

    
    def add_callbacks(self = None, on_quit = None, account_manager = None):
        self._controller_lock
        if not self._callbacks_added:
            on_quit.add_handler(self._on_quit_callback)
            account_manager.add_accounts_changed_callback(self._accounts_changed_callback)
            self._callbacks_added = True
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def remove_callbacks(self = None, on_quit = None, account_manager = None):
        self._controller_lock
        if self._callbacks_added:
            on_quit.remove_handler(self._on_quit_callback)
            account_manager.remove_accounts_changed_callback(self._accounts_changed_callback)
            self._callbacks_added = False
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def register_kernel_memory_logging_job(self, periodic_scheduler):
        pass
    # WARNING: Decompyle incomplete

    
    def unregister_kernel_memory_logging_job(self, periodic_scheduler):
        periodic_scheduler.unregister_job('infinite_memory_metrics')

    
    def _log_state(self = None):
        self._kernel_component_manager.report_kernel_components_status()
        self._log_pager_state()

    
    def _update_paging_threads_unlocked(self = None):
        new_accounts = set(self._syncing_accounts())
        old_accounts = set(self._paging_thread_map.keys())
        added = new_accounts - old_accounts
        removed = old_accounts - new_accounts
        for account in added:
            TRACE('Starting paging thread for account %r', account)
            paging_thread = db_thread(PagingThread)(account, self._sync_engine_adapter, self._tray_menu_controller, self._recall_blacklist, self._log_state, self._gandalf, self._need_mitigation)
            paging_thread.start()
            self._paging_thread_map[account] = paging_thread
            for account in removed:
                TRACE('Stopping paging thread for account %r', account)
                old_paging_thread = self._paging_thread_map.pop(account)
                old_paging_thread.signal_stop()
                return None

    
    def _syncing_accounts(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _accounts_changed_callback(self = None, account = None, change_type = None):
        if change_type in (AccountChangeType.LINK, AccountChangeType.REMOVE):
            self._controller_lock
            if self._infinite_enabled:
                self._update_paging_threads_unlocked()
            None(None, None)
            return None
        with None:
            if not None:
                pass
        return None

    
    def _on_quit_callback(self = None, exit_code = None):
        self._controller_lock
    # WARNING: Decompyle incomplete


