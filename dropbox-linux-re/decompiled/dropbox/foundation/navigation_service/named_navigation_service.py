# Source Generated with Decompyle++
# File: named_navigation_service.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
from typing import cast, Optional, Text, Type, TypeVar
from  import manifest_registry
from bridge_gen.bridge_interface_named_navigation_service import NamedNavigationServiceBridgeInterface
from bridge_gen.bridge_interface_view_handle import ViewHandleBridgeInterface
from interface import MachineNavigationManifest, NavigationManifest, NavigationServiceInterface, UserNavigationManifest, ViewBridgeSerializable
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.bridge.impl import json_unbox_records
from dropbox.foundation.navigation_service.bridge_gen.navigation_load_policy import NavigationLoadPolicy
from dropbox.functions import make_str
from dropbox.trace import TRACE
_T = TypeVar('_T', bound = Optional[ViewBridgeSerializable])

class NamedNavigationService(NamedNavigationServiceBridgeInterface):
    
    def __init__(self = None, navigation_service = None):
        self._navigation_service = navigation_service

    
    def navigate(self, manifest_name = None, view_key = None, parameter = None, call_site_name = (None, None, None, None), load_policy = ('manifest_name', 'Text', 'view_key', 'Optional[Text]', 'parameter', 'Optional[Text]', 'call_site_name', 'Optional[Text]', 'load_policy', 'Optional[NavigationLoadPolicy]', 'return', 'Future[Optional[ViewHandleBridgeInterface]]')):
        manifest = NamedNavigationService.get_manifest(manifest_name)
        arguments = self._unbox_arguments(manifest.parameter_type, parameter)
    # WARNING: Decompyle incomplete

    
    def navigate_user_bound(self, manifest_name, context = None, view_key = None, parameter = None, call_site_name = (None, None, None, None), load_policy = ('manifest_name', 'Text', 'context', 'UserContextBridgeInterface', 'view_key', 'Optional[Text]', 'parameter', 'Optional[Text]', 'call_site_name', 'Optional[Text]', 'load_policy', 'Optional[NavigationLoadPolicy]', 'return', 'Future[Optional[ViewHandleBridgeInterface]]')):
        manifest = NamedNavigationService.get_manifest(manifest_name)
        arguments = self._unbox_arguments(manifest.parameter_type, parameter)
    # WARNING: Decompyle incomplete

    get_manifest = (lambda manifest_name = None: manifest = manifest_registry.__dict__.get(make_str(manifest_name))# WARNING: Decompyle incomplete
)()
    
    def _unbox_arguments(self = None, parameter_type = None, boxed_parameter = None):
        pass
    # WARNING: Decompyle incomplete


