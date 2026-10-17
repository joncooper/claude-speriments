# Source Generated with Decompyle++
# File: collection_interface.pyc (Python 3.11)

from abc import abstractmethod
from typing import Callable, Optional, Text
from dropbox.foundation.futures import Future
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.types import WindowManagerDelegateType

class WindowManagerDelegateCollectionInterface:
    is_tracking_windows = (lambda self = None: pass)()
    increment_window_count = (lambda self = None: pass)()
    decrement_window_count = (lambda self = None: pass)()
    add_close_windows_callback = (lambda self = None, callback = None: pass)()
    remove_close_windows_callback = (lambda self = None, callback = None: pass)()
    trigger_close_windows_event = (lambda self = None: pass)()
    get_foreground_management_variant = (lambda self = None: pass)()
    get = (lambda self = None, delegate_type = None: pass)()
    reset = (lambda self = None, delegate_type = None: pass)()

