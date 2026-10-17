# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

from typing import Callable, List, Optional, Text, TypeVar
from parameters.bridge_gen.preferences_pane_params import PreferencesPaneParams
from parameters.bridge_gen.sharing_dialog_params import SharingDialogParams
from threading import assert_on_legacy_view_thread, on_legacy_view_thread_future
from dropbox.client.features.account_switcher.bridge_gen.account_switcher_nav_params import AccountSwitcherNavParams
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.client.ui.common.uikit import BaseUIKit, on_ui_thread_future
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context import Context
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.embeddable_host import EmbeddableViewHost
from dropbox.foundation.navigation_service.interface import NavigationServiceInterface, NavigationVisibilityConfig, NavigationWindowType, ViewBridgeSerializable
from dropbox.foundation.navigation_service.manifest_registry import IMPORT_PROGRESS, PREFERENCES_PANE, SETUP_WIZARD, SHARE_DIALOG, SHOW_TRAY_POPUP
from dropbox.foundation.navigation_service.view_manager_interface import EmbeddableViewFuture, FailedEmbeddableViewFuture, StandaloneViewIdentifier, ViewInterface, ViewManagerInterface
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.collection_interface import WindowManagerDelegateCollectionInterface
from dropbox.foundation.performance import PerfSession
from dropbox.sync_engine_adapter.adapter import RRCasedServerPath, SyncEngineAdapter
_EV = TypeVar('_EV')

class LegacyDummyView(ViewInterface):
    is_visible = (lambda self = None: True)()
    
    def is_foreground(self = None):
        return ResolvedFuture(True)

    close = (lambda self = None, close_reason = None: close_reason)()
    
    def add_closed_handler(self = None, callback = None):
        pass

    
    def foreground(self = None):
        return ResolvedFuture(None)

    
    def render_offscreen(self = None):
        return ResolvedFuture(None)



def LegacyViewManager():
    '''LegacyViewManager'''
    pass
# WARNING: Decompyle incomplete

LegacyViewManager = <NODE:27>(LegacyViewManager, 'LegacyViewManager', ViewManagerInterface[None])
