# Source Generated with Decompyle++
# File: bridge.pyc (Python 3.11)

from typing import Any, Callable, Optional, Text
from dropbox.foundation.html_views.bridge.pipe_interface import JavaScriptBridgePipeInterface, MessageToBrowser
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.trace.trace_js_bridge import JavaScriptBridgeEventTracing
from dropbox.trace import TRACE

class ElectronBridgePipe(JavaScriptBridgePipeInterface):
    
    def __init__(self = None, web_contents_id = None, electron_ipc = None):
        self._web_contents_id = web_contents_id
        self._electron_ipc = electron_ipc
        self._electron_ipc.add_message_handler(f'''bridge_{self._web_contents_id}''', self._handle_browser_message)
        self._on_message_from_view = None
        self._on_browser_connection_opened = None
        self._on_security_policy_violation = None
        self._callbacks_registered = False

    
    def send_message_to_browser(self = None, message = None):
        if JavaScriptBridgeEventTracing.should_trace():
            TRACE('ElectronBridgePipe.send_message_to_browser id = %s, payload = %s', self._web_contents_id, message.payload)
        self._electron_ipc.send_message(f'''bridge_{self._web_contents_id}''', message.payload)

    
    def _handle_browser_message(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    def register_callbacks(self = None, on_message_from_view = None, on_browser_connection_opened = None, on_security_policy_volation = ('on_message_from_view', 'Callable[[Text], None]', 'on_browser_connection_opened', 'Callable[[], None]', 'on_security_policy_volation', 'Callable[[Text, Text, Text, int], None]', 'return', 'None')):
        self._on_message_from_view = on_message_from_view
        self._on_browser_connection_opened = on_browser_connection_opened
        self._on_security_policy_violation = on_security_policy_volation
        self._callbacks_registered = True

    
    def cleanup(self = None):
        self._on_message_from_view = None
        self._on_browser_connection_opened = None
        self._on_security_policy_violation = None


