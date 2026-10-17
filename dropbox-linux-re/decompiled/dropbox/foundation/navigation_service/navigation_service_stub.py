# Source Generated with Decompyle++
# File: navigation_service_stub.pyc (Python 3.11)

from typing import Dict, List, Optional, Text, Type, TypeVar
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context import Context
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.interface import MachineNavigationManifest, NavigationDisabledError, NavigationVisibilityConfig, NavigationWindowType, UserNavigationManifest, ViewBridgeSerializable, ViewHandle
from dropbox.foundation.navigation_service.navigation_service import NavigationService
from dropbox.foundation.navigation_service.types import NavigationContentType
from dropbox.foundation.navigation_service.view_manager_interface import ViewManagerInterface
from dropbox.foundation.navigation_service.window_manager_delegate.collection import StubWindowManagerDelegateCollection
from dropbox.foundation.navigation_service.window_manager_delegate.collection_interface import WindowManagerDelegateCollectionInterface
from dropbox.gui import assert_message_queue
_T = TypeVar('_T')
_P = TypeVar('_P', bound = Optional[ViewBridgeSerializable])
_EV = TypeVar('_EV')

class StubNavigationService(NavigationService):
    pass
# WARNING: Decompyle incomplete

