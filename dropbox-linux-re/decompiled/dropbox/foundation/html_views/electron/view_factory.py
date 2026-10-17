# Source Generated with Decompyle++
# File: view_factory.pyc (Python 3.11)

from typing import Text
from build_number import VERSION
from dropbox.client.ui.common.uikit import FrameworkProps
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.common import HtmlViewStateMachine
from dropbox.foundation.html_views.common.content_metadata import StandaloneHtmlContentMetadata
from dropbox.foundation.html_views.common.interface import HtmlViewAffinityGroup
from dropbox.foundation.html_views.common.top_level_html_view_params import TopLevelHtmlViewParams
from dropbox.foundation.html_views.common.view import PlatformHtmlViewCreationData, PlatformHtmlViewFactory, ViewType
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.html_views.electron.view import ElectronBrowserWindow, ElectronWebContents
from dropbox.foundation.navigation_service.view_manager_interface import StandaloneViewIdentifier
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2.wrappers import Transferable

def ElectronHtmlViewFactory():
    '''ElectronHtmlViewFactory'''
    
    def __init__(self = None, machine_context = None, electron_host_driver = None):
        self._machine_context = machine_context
        self._electron_host_driver = electron_host_driver

    framework_props = (lambda self = None: FrameworkProps.ELECTRON)()
    
    def create_blank_standalone(self, metadata = None, perf_session = None, context = None, window_manager_delegate = ('metadata', 'StandaloneHtmlContentMetadata', 'perf_session', 'PerfSession', 'context', 'MachineContext', 'window_manager_delegate', 'WindowManagerDelegateInterface', 'return', 'Future[PlatformHtmlViewCreationData[ElectronWebContents]]')):
        pass

    
    def create_embeddable(self, state_machine, top_level_html_view_params = None, scheme_name = None, affinity_group = None, view_type = ('state_machine', 'HtmlViewStateMachine', 'top_level_html_view_params', 'Transferable[TopLevelHtmlViewParams]', 'scheme_name', 'Text', 'affinity_group', 'HtmlViewAffinityGroup', 'view_type', 'ViewType', 'return', 'Future[ElectronWebContents]')):
        pass
    # WARNING: Decompyle incomplete

    
    def create_pre_embedded_standalone(self = None, perf_session = None, context = None, web_view = ('perf_session', 'PerfSession', 'context', 'MachineContext', 'web_view', 'ElectronWebContents', 'return', 'Future[PlatformHtmlViewCreationData[ElectronWebContents]]')):
        pass
    # WARNING: Decompyle incomplete

    
    def create_standalone(self, view_id, metadata, perf_session = None, context = None, window_manager_delegate = None, web_view = ('view_id', 'StandaloneViewIdentifier', 'metadata', 'StandaloneHtmlContentMetadata', 'perf_session', 'PerfSession', 'context', 'MachineContext', 'window_manager_delegate', 'WindowManagerDelegateInterface', 'web_view', 'ElectronWebContents', 'return', 'Future[PlatformHtmlViewCreationData[ElectronWebContents]]')):
        pass


ElectronHtmlViewFactory = <NODE:27>(ElectronHtmlViewFactory, 'ElectronHtmlViewFactory', PlatformHtmlViewFactory[ElectronWebContents])
