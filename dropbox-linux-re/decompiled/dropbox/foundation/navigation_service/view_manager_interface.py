# Source Generated with Decompyle++
# File: view_manager_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from abc import abstractmethod, abstractproperty
from typing import Callable, Generic, List, Optional, Text, TypeVar
from embeddable_host import EmbeddableViewHost
from view_interface import StandaloneViewIdentifier, ViewInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.foundation.html_views.bridge.interface import ViewBridgeSerializable
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.foundation.navigation_service.types import NavigationVisibilityConfig, NavigationWindowType
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.collection_interface import WindowManagerDelegateCollectionInterface
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2.quick import Destroyable
MYPY = False
if MYPY:
    from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
_EV = TypeVar('_EV')

def EmbeddableViewFuture():
    '''EmbeddableViewFuture'''
    pass

EmbeddableViewFuture = <NODE:27>(EmbeddableViewFuture, 'EmbeddableViewFuture', EasyFuture[_EV], Destroyable)

def FailedEmbeddableViewFuture():
    '''FailedEmbeddableViewFuture'''
    pass
# WARNING: Decompyle incomplete

FailedEmbeddableViewFuture = <NODE:27>(FailedEmbeddableViewFuture, 'FailedEmbeddableViewFuture', Actor, EmbeddableViewFuture[_EV])

def ViewManagerInterface():
    '''ViewManagerInterface'''
    embeddable_view_type = (lambda self = None: pass)()
    open_standalone_view_by_id = (lambda self, view_id, load_policy, call_site_name, perf_session = None, window_manager_delegate = None, parameter = abstractmethod, visibility_config = (None, None), parent_id = ('view_id', 'StandaloneViewIdentifier', 'load_policy', 'NavigationLoadPolicy', 'call_site_name', 'Text', 'perf_session', 'PerfSession', 'window_manager_delegate', 'WindowManagerDelegateInterface', 'parameter', 'Optional[ViewBridgeSerializable]', 'visibility_config', 'Optional[NavigationVisibilityConfig]', 'parent_id', 'Optional[int]', 'return', 'Future[ViewInterface]'): pass)()
    open_embeddable_view_by_id_within_host = (lambda self, embeddable_host, view_id, load_policy = None, call_site_name = None, perf_session = abstractmethod, parameter = ('embeddable_host', 'EmbeddableViewHost[_EV]', 'view_id', 'StandaloneViewIdentifier', 'load_policy', 'NavigationLoadPolicy', 'call_site_name', 'Text', 'perf_session', 'PerfSession', 'parameter', 'Optional[ViewBridgeSerializable]', 'return', 'Future[None]'): pass)()
    create_embeddable_view_by_id = (lambda self, view_id = None, call_site_name = None, perf_session = abstractmethod, parameter = ('view_id', 'StandaloneViewIdentifier', 'call_site_name', 'Text', 'perf_session', 'PerfSession', 'parameter', 'Optional[ViewBridgeSerializable]', 'return', 'EmbeddableViewFuture[_EV]'): pass)()
    get_embeddable_host = (lambda self = None, window_type = None, window_manager_delegate_col = abstractmethod, view_key = (None,): pass)()
    close_standalone_view_by_id = (lambda self = None, view_id = None: pass)()
    close_all_standalone_views = (lambda self = None, close_reason = None: pass)()
    close_all_standalone_views_where = (lambda self = None, predicate = None, close_reason = abstractmethod: pass)()
    open_view_names = (lambda self = None: pass)()

ViewManagerInterface = <NODE:27>(ViewManagerInterface, 'ViewManagerInterface', Actor, Generic[_EV])
