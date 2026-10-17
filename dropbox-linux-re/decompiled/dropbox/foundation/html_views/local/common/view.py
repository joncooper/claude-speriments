# Source Generated with Decompyle++
# File: view.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from typing import Callable, Dict, List, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.environment import local_view_hmr_enabled
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.html_views.common import BlockNavigationResult, HtmlViewStateMachineStrategy
from dropbox.foundation.html_views.common.debug import html_view_debugging_features_enabled
from dropbox.foundation.html_views.common.navigation_rules import LOCAL_VIEW_NAVIGATION_PREFS, LOCAL_VIEW_NAVIGATION_PREFS_DEBUG
from dropbox.foundation.scheme_handler.interface import CustomSchemeRouterInterface
from dropbox.foundation.scheme_handler.types import CustomSchemeHandlerResult, CustomSchemeUrlRequest

class LocalViewCreationCheckpoints:
    CREATE_NATIVE_OBJECTS_START = 'create_native_objects_start'
    WINDOW_WILL_CREATE_INVOKED = 'create_native_objects_window_will_create_invoked'
    WINDOW_CREATED = 'create_native_objects_window_created'
    METADATA_PROPS_SET = 'create_native_objects_metadata_props_set'
    VIEW_EMBEDDED = 'create_native_objects_view_embedded'
    CREATE_NATIVE_OBJECTS_END = 'create_native_objects_end'
    VIEW_OFFSCREEN_RENDERED = 'create_native_objects_rendered_offscreen'


def complete_url_request_for_debugging(response_future = None, completion_handler = None):
    
    def delay_html_response_when_debugging(response = None):
        if html_view_debugging_features_enabled() and response.mimetype == 'text/html' and 'LOCAL_VIEW_HTML_RESPONSE_DELAY' in os.environ:
            delay = float(os.environ['LOCAL_VIEW_HTML_RESPONSE_DELAY'])
            return sleep_async(delay).discard_value(replace_with = response)
        return ResolvedFuture(response)

    response_future.then(delay_html_response_when_debugging).then(completion_handler).ground(component = DesktopComponent.HTML_VIEWS)


class LocalViewStateMachineStrategy(HtmlViewStateMachineStrategy):
    
    def __init__(self = None, scheme_handler = None, has_startup_completed = None):
        self._custom_scheme_handler = scheme_handler
        self._has_startup_completed = has_startup_completed

    
    def override_request_headers(self, request_url = None, is_initial_load = None, is_main_frame = None, header_dict = ('request_url', 'Text', 'is_initial_load', 'bool', 'is_main_frame', 'bool', 'header_dict', 'Dict[Text, Text]', 'return', 'None')):
        pass

    load_timeout = (lambda self = None: 300 if self._has_startup_completed() else 600)()


class LocalViewProdStateMachineStrategy(LocalViewStateMachineStrategy):
    
    def block_invalid_navigation(self, url_scheme = None, url_host = None, url_path = None, is_main_frame = ('url_scheme', 'str', 'url_host', 'str', 'url_path', 'str', 'is_main_frame', 'bool', 'return', 'BlockNavigationResult')):
        pass
    # WARNING: Decompyle incomplete

    
    def process_custom_protocol_request(self = None, request = None, completion_handler = None):
        self._custom_scheme_handler.process_request(request).then(completion_handler).ground(component = DesktopComponent.HTML_VIEWS)

    
    def construct_request_url(self = None, path = None, parameters = None):
        pass
    # WARNING: Decompyle incomplete

    load_timeout = (lambda self = None: 300 if self._has_startup_completed() else 600)()


class LocalViewDevStateMachineStrategy(LocalViewStateMachineStrategy):
    HMR_DEV_SERVER_PROTOCOL = 'http'
    HMR_DEV_SERVER_HOST = 'localhost:9000'
    
    def block_invalid_navigation(self, url_scheme = None, url_host = None, url_path = None, is_main_frame = ('url_scheme', 'str', 'url_host', 'str', 'url_path', 'str', 'is_main_frame', 'bool', 'return', 'BlockNavigationResult')):
        pass
    # WARNING: Decompyle incomplete

    
    def process_custom_protocol_request(self = None, request = None, completion_handler = None):
        complete_url_request_for_debugging(self._custom_scheme_handler.process_request(request), completion_handler)

    
    def construct_request_url(self = None, path = None, parameters = None):
        pass
    # WARNING: Decompyle incomplete



def create_local_view_state_machine_strategy(scheme_router = None, has_startup_completed = None):
    if html_view_debugging_features_enabled():
        return LocalViewDevStateMachineStrategy(scheme_router, has_startup_completed)
    return LocalViewProdStateMachineStrategy(scheme_router, has_startup_completed)

