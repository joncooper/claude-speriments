# Source Generated with Decompyle++
# File: interface.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Any, Dict, Generic, Optional, Text, Type, TypeVar
from six import add_metaclass
from bridge_gen.bridge_interface_view_handle import ViewHandleBridgeInterface
from bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context import Context
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.bridge.interface import ViewBridgeSerializable
from dropbox.foundation.navigation_service.types import NavigationContentType, NavigationVisibilityConfig, NavigationWindowType
from dropbox.foundation.navigation_service.view_manager_interface import ViewManagerInterface
from dropbox.foundation.navigation_service.window_manager_delegate.collection_interface import WindowManagerDelegateCollectionInterface
from dropbox.foundation.navigation_service.window_manager_delegate.types import WindowManagerDelegateType
from dropbox.repr_utils import easy_repr
_P = TypeVar('_P', bound = Optional[ViewBridgeSerializable])

def NavigationManifest():
    '''NavigationManifest'''
    
    def __init__(self, content_type, content_identifier = None, parameter_type = None, component = None, default_window_type = (NavigationWindowType.STANDALONE, WindowManagerDelegateType.DEFAULT), window_manager_delegate_type = ('content_type', 'NavigationContentType', 'content_identifier', 'Text', 'parameter_type', 'Type[_P]', 'component', 'DesktopComponent', 'default_window_type', 'NavigationWindowType', 'window_manager_delegate_type', 'WindowManagerDelegateType', 'return', 'None')):
        self._content_type = content_type
        self._content_identifier = content_identifier
        self._parameter_type = parameter_type
        self._default_window_type = default_window_type
        self._window_manager_delegate_type = window_manager_delegate_type
        self._component = component

    
    def __repr__(self = None):
        return easy_repr(self, 'content_type', 'content_identifier', 'parameter_type', 'default_window_type', 'window_manager_delegate_type', 'component')

    
    def __eq__(self = None, other = None):
