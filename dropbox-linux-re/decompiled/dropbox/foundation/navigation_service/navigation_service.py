# Source Generated with Decompyle++
# File: navigation_service.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod
from typing import Dict, List, Optional, Text, TypeVar
from six import add_metaclass
from bridge_gen.bridge_interface_activity_monitor import ActivityMonitorBridgeInterface
from bridge_gen.navigation_load_policy import NavigationLoadPolicy
from embeddable_host import EmbeddableViewHost
from interface import NavigationServiceInterface, NavigationWindowType, ViewBridgeSerializable
from navigation_service_popover_host_interface import NavServicePopoverHostInterface
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.context.machine import Context, MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.common.threading import assert_on_ui_thread
from dropbox.foundation.navigation_service.interface import MachineNavigationManifest, NavigationVisibilityConfig, UserNavigationManifest, ViewHandle
from dropbox.foundation.raii2.quick import Destroyable
MachineUiDispatcherFactoryInterface = <NODE:12>()

class MachineUiDispatcherInterface(Destroyable):
    pass

UserUiDispatcherFactoryInterface = <NODE:12>()

class UserUiDispatcherInterface(Destroyable):
    pass

EmbeddableHostManager = <NODE:12>()
_T = TypeVar('_T')
_P = TypeVar('_P', bound = Optional[ViewBridgeSerializable])

class NavigationService(Actor, ActivityMonitorBridgeInterface, NavServicePopoverHostInterface, NavigationServiceInterface):
    open_view_names = (lambda self = None: pass)()
    navigate = (lambda self, manifest, view_key, parameter, call_site_name, window_type, load_policy = None, visibility_config = None, start_time = abstractmethod, perf_session_extras = (None, None, None, None, NavigationLoadPolicy.ALLOW_REUSE, None, None, None, None), parent_id = ('manifest', 'MachineNavigationManifest[_P]', 'view_key', 'Optional[Text]', 'parameter', 'Optional[_P]', 'call_site_name', 'Optional[Text]', 'window_type', 'Optional[NavigationWindowType]', 'load_policy', 'NavigationLoadPolicy', 'visibility_config', 'Optional[NavigationVisibilityConfig]', 'start_time', 'Optional[float]', 'perf_session_extras', 'Optional[Dict[Text, Text]]', 'parent_id', 'Optional[int]', 'return', 'Future[ViewHandle]'): pass)()
    navigate_user_bound = (lambda self, manifest, account, view_key, parameter, call_site_name, window_type = None, load_policy = None, visibility_config = abstractmethod, start_time = (None, None, None, None, NavigationLoadPolicy.ALLOW_REUSE, None, None, None), perf_session_extras = ('manifest', 'UserNavigationManifest[_P]', 'account', 'AccountInterface', 'view_key', 'Optional[Text]', 'parameter', 'Optional[_P]', 'call_site_name', 'Optional[Text]', 'window_type', 'Optional[NavigationWindowType]', 'load_policy', 'NavigationLoadPolicy', 'visibility_config', 'Optional[NavigationVisibilityConfig]', 'start_time', 'Optional[float]', 'perf_session_extras', 'Optional[Dict[Text, Text]]', 'return', 'Future[ViewHandle]'): pass)()
    start_dispatch = (lambda self = None: pass)()

