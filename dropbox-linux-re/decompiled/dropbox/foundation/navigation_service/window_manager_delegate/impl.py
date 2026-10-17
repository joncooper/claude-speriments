# Source Generated with Decompyle++
# File: impl.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import Optional
from ui_flow import WindowUIFlow
from dropbox.client.flow_tracker import NonBlockingFlow
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.navigation_service.view_interface import StandaloneViewIdentifier
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.foreground_process_tracker import ForegroundProcessStateTracker
from dropbox.foundation.navigation_service.window_manager_delegate.types import WindowWillCreateResult
from dropbox.foundation.types.rect import Size

class StubWindowManagerDelegate(WindowManagerDelegateInterface):
    
    def window_did_resize(self = None, size = None):
        pass

    
    def window_did_become_visible(self = None, view_id = None):
        pass

    
    def window_will_create(self = None, width = None, height = None):
        return ResolvedFuture(WindowWillCreateResult(size = Size(width, height)))

    
    def window_did_create(self = None):
        return ResolvedFuture(True)

    
    def window_will_hide(self = None, view_id = None):
        pass

    
    def window_did_become_main(self = None, size = None, is_full_screen = None, view_id = (None,)):
        pass

    
    def window_will_close(self = None, size = None, is_full_screen = None, is_visible = (None,), view_id = ('size', 'Size', 'is_full_screen', 'bool', 'is_visible', 'bool', 'view_id', 'Optional[StandaloneViewIdentifier]', 'return', 'Future[bool]')):
        return ResolvedFuture(True)

    
    def window_did_resign_main(self = None, size = None, is_full_screen = None, view_id = (None,)):
        pass



class DefaultWindowManagerDelegate(WindowManagerDelegateInterface):
    pass
# WARNING: Decompyle incomplete


class SetupWizardWindowManagerDelegate(DefaultWindowManagerDelegate):
    FLOW_NAME = 'setup_wizard_window_manager_delegate_flow'
    DEFAULT_WINDOW_FLOW_NAME = 'setup_wizard_window_manager_delegate_active_flow'
    
    def window_did_become_main(self = None, size = None, is_full_screen = None, view_id = (None,)):
        self._foreground_signal.fire(view_id)

    
    def window_did_resign_main(self = None, size = None, is_full_screen = None, view_id = (None,)):
        self._background_signal.fire(view_id)


