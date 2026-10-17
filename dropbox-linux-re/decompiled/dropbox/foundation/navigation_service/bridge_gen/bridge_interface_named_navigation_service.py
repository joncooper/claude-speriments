# Source Generated with Decompyle++
# File: bridge_interface_named_navigation_service.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import Optional
from dropbox.foundation.futures import Future
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface
from dropbox.foundation.navigation_service.bridge_gen.bridge_interface_view_handle import ViewHandleBridgeInterface
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy

class NamedNavigationServiceBridgeInterface(ABC):
    navigate = (lambda self, manifest_name, view_key = None, parameter = None, call_site_name = abstractmethod, load_policy = ('manifest_name', 'str', 'view_key', 'Optional[str]', 'parameter', 'Optional[str]', 'call_site_name', 'Optional[str]', 'load_policy', 'Optional[NavigationLoadPolicy]', 'return', 'Future[Optional[ViewHandleBridgeInterface]]'): pass)()
    navigate_user_bound = (lambda self, manifest_name, context, view_key = None, parameter = None, call_site_name = abstractmethod, load_policy = ('manifest_name', 'str', 'context', 'UserContextBridgeInterface', 'view_key', 'Optional[str]', 'parameter', 'Optional[str]', 'call_site_name', 'Optional[str]', 'load_policy', 'Optional[NavigationLoadPolicy]', 'return', 'Future[Optional[ViewHandleBridgeInterface]]'): pass)()

