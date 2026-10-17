# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Callable, List, Optional
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.sync_root.interface import SyncRootType
from dropbox.sync_root.types import RemovalMode, SyncRootCreationResult, SyncRootHydrationPolicy, SyncRootRepairAction

class _SyncRootHandler(ABC):
    root_type = (lambda : pass)()()
    is_root_enabled = (lambda self = None: pass)()
    register = (lambda self = None, root_display_name = None, parent_path = abstractmethod, hydration_policy = (None, SyncRootHydrationPolicy.FULL): pass)()
    unregister = (lambda self = None, mode = None: pass)()
    migrate = (lambda self = None, from_handler = None, root_parent_path = abstractmethod, root_display_name = (SyncRootHydrationPolicy.FULL,), hydration_policy = ('from_handler', "'_SyncRootHandler'", 'root_parent_path', 'str', 'root_display_name', 'str', 'hydration_policy', 'SyncRootHydrationPolicy', 'return', 'Future[Optional[SyncRootCreationResult]]'): pass)()
    
    def set_hydration_policy(self = None, desired = None):
        return ResolvedFuture(None)

    get_mount_path = (lambda self = None: pass)()
    rename = (lambda self = None, new_name = None: pass)()
    move = (lambda self = None, new_parent_path = None: pass)()
    
    def show_consent_window(self = None):
        pass

    check_root_consistency = (lambda self = None: pass)()
    repair = (lambda self = None, action = None: pass)()
    register_root_change_listener = (lambda self = None, on_root_change = None: pass)()
    unregister_root_change_listener = (lambda self = None: pass)()

