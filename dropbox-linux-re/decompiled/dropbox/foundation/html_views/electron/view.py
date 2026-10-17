# Source Generated with Decompyle++
# File: view.pyc (Python 3.11)

from typing import Callable, Dict, List, Optional, Text
from apex.metrics import MetricsReporter
from dropbox.callbacks import create_weakref_callback, Handler
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread_future, record_view_event
from dropbox.client.ui.ui_timer import UITimerFactory
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import EasyFuture, Future, ResolvedFuture
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.html_views.bridge.routing import HtmlViewTransportHandler, JavaScriptBridgeViewContext
from dropbox.foundation.html_views.common import StateMachineNavigationRequest
from dropbox.foundation.html_views.common.bridge_gen.view_close_reason import ViewCloseReason
from dropbox.foundation.html_views.common.content_metadata import StandaloneHtmlContentMetadata
from dropbox.foundation.html_views.common.embeddable_mixin import EmbeddableViewMixin
from dropbox.foundation.html_views.common.errors import ChromiumErrorCategory
from dropbox.foundation.html_views.common.interface import HtmlViewContentErrorData, HtmlViewContentErrorType
from dropbox.foundation.html_views.common.logging import HtmlViewLoggerEvent
from dropbox.foundation.html_views.common.state_machine import HtmlViewStateMachine
from dropbox.foundation.html_views.common.top_level_html_view_params import TopLevelHtmlViewParams
from dropbox.foundation.html_views.common.view import PlatformStandaloneHtmlViewInterface, ViewType
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriverInterface
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc, JSONDict
from dropbox.foundation.navigation_service.embeddable_host import EmbeddableViewHost
from dropbox.foundation.navigation_service.view_interface import StandaloneViewIdentifier
from dropbox.foundation.navigation_service.window_manager_delegate import WindowManagerDelegateInterface
from dropbox.foundation.navigation_service.window_manager_delegate.types import WindowWillCreateResult
from dropbox.foundation.raii2 import Destroyable, destroying
from dropbox.foundation.raii2.wrappers import Transferable
from dropbox.foundation.types.rect import Size
from dropbox.trace import TRACE

class ElectronWebContents(EmbeddableViewMixin):
    pass
# WARNING: Decompyle incomplete


def ElectronBrowserWindow():
    '''ElectronBrowserWindow'''
    
    def __init__(self = None, host_driver = None, web_contents = None):
        self._host_driver = host_driver
        self._rpc_future = EasyFuture('ElectronBrowserWindow._rpc')
        self._rpc = None
        self._window_id = None
        self
        self._web_contents = web_contents
        self._delayed_close_timer = UITimerFactory.create()
        self._close_handlers = Handler(handle_exc = report_exception)

    electron_window_id = (lambda self = None: self._window_id)()
    register_window_manager_delegate_handlers = (lambda ipc, window_id, window_closing_handler, window_closed_handler, window_did_resize_handler, window_did_become_main_handler, window_did_resign_main_handler = None, window_did_become_visible_handler = None, window_will_hide_handler = staticmethod, window_metrics_reporter = ('ipc', 'ElectronIpc', 'window_id', 'int', 'window_closing_handler', 'Callable[[JSONDict], None]', 'window_closed_handler', 'Callable[[JSONDict], None]', 'window_did_resize_handler', 'Callable[[JSONDict], None]', 'window_did_become_main_handler', 'Callable[[JSONDict], None]', 'window_did_resign_main_handler', 'Callable[[JSONDict], None]', 'window_did_become_visible_handler', 'Callable[[JSONDict], None]', 'window_will_hide_handler', 'Callable[[JSONDict], None]', 'window_metrics_reporter', 'MetricsReporter', 'return', 'Transferable[ElectronRpc]'): Transferable(ElectronRpc(ipc, f'''window_{window_id}''', DesktopComponent.HTML_VIEWS, signal_handlers = {
'event_window_closing': window_closing_handler,
'event_window_closed': window_closed_handler,
'window_did_resize': window_did_resize_handler,
'window_did_become_main': window_did_become_main_handler,
'window_did_resign_main': window_did_resign_main_handler,
'window_did_become_visible': window_did_become_visible_handler,
'window_will_hide': window_will_hide_handler }, logging_topic = 'window')))()
    
    def initialize_from_metadata(self = None, metadata = None, window_manager_delegate = None, metrics_reporter = ('metadata', 'StandaloneHtmlContentMetadata', 'window_manager_delegate', 'WindowManagerDelegateInterface', 'metrics_reporter', 'MetricsReporter', 'return', 'Future[None]')):
        pass
    # WARNING: Decompyle incomplete

    
    def extract_view(self = None, view_id = None):
        raise NotImplementedError("Electron doesn't support extracting views")

    
    def embed_view(self = None, view_id = None, view = None):
        raise NotImplementedError()

    
    def get_view(self = None, view_id = None):
        return self._web_contents

    
    def bring_view_to_front(self = None, view_id = None):
        raise NotImplementedError()

    
    def foreground_window(self = None):
        self._rpc_future.map_parasitically((lambda rpc: rpc.send_signal('foreground', { }))).ground(component = DesktopComponent.HTML_VIEWS)

    
    def close_views(self = None):
        self.close_view(ViewCloseReason.API)
        return ResolvedFuture(None)

    
    def get_view_id(self = None):
        return self._web_contents.view_id

    
    def destroy(self = None):
        self._rpc_future.cancel()
        if self._rpc:
            self._rpc.destroy()
    # WARNING: Decompyle incomplete

    
    def close_view(self = None, close_reason = None):
        pass
    # WARNING: Decompyle incomplete

    
    def show_view(self = None):
        self._delayed_close_timer.stop()
        self._rpc_future.map_parasitically((lambda rpc: rpc.send_signal('show', { }))).ground(component = DesktopComponent.HTML_VIEWS)

    
    def render_offscreen(self = None):
        pass

    
    def hide_view(self = None):
        self._rpc_future.map_parasitically((lambda rpc: rpc.send_signal('hide', { }))).ground(component = DesktopComponent.HTML_VIEWS)

    
    def autoclose_view(self = None, close_timeout_secs = None):
        pass
    # WARNING: Decompyle incomplete

    
    def foreground_view(self = None):
        self._delayed_close_timer.stop()
        self._rpc_future.map_parasitically((lambda rpc: rpc.send_signal('foreground', { }))).ground(component = DesktopComponent.HTML_VIEWS)

    
    def add_view_closed_handler(self = None, callback = None):
        self._close_handlers.add_handler(callback)

    
    def remove_view_closed_handler(self = None, callback = None):
        self._close_handlers.remove_handler(callback)

    
    def is_foreground(self = None):
        return self._rpc_future.then((lambda rpc: rpc.invoke_method('is_foreground', { })))

    
    def _event_window_closing(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _event_window_closed(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _window_did_resize(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _window_did_become_main(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _window_did_resign_main(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    _window_did_create = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _window_did_become_visible(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _window_will_hide(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete


ElectronBrowserWindow = <NODE:27>(ElectronBrowserWindow, 'ElectronBrowserWindow', PlatformStandaloneHtmlViewInterface, EmbeddableViewHost[ElectronWebContents])
