# Source Generated with Decompyle++
# File: routing.pyc (Python 3.11)

import json
from collections import namedtuple
from functools import partial, wraps
from typing import Any, AnyStr, Callable, Dict, List, NamedTuple, Optional, Text, Tuple, Union
from apex.metrics.metrics import Metric
from dropbox.client.authentication.account import Account
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.bridge import impl as bridge_v2
from dropbox.foundation.html_views.bridge.context import JavaScriptBridgeViewContext
from dropbox.foundation.html_views.bridge.pipe_interface import JavaScriptBridgePipeInterface, MessageToBrowser
from dropbox.foundation.html_views.bridge.response import BridgeFunctionResponseInfo, BridgeFunctionResult, BridgeResultPayload, DeferredBridgeFunctionResponse
from dropbox.foundation.html_views.bridge.timed_bridge_call_tracker import TimedBridgeCallTracker
from dropbox.foundation.html_views.common.logging import HtmlViewLogger
from dropbox.foundation.runtime import panic_with_report
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.foundation.trace.trace_js_bridge import JavaScriptBridgeEventTracing
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
ClientBridgeFunctionInfo = namedtuple('ClientBridgeFunctionInfo', [
    'function',
    'parameterTypes'])
_CLIENT_LOOKUP: 'Dict[Text, ClientBridgeFunctionInfo]' = { }

class HtmlViewTransportHandler:
    JSONRPC_INVALID_REQUEST_ERROR = -32600
    JSONRPC_METHOD_NOT_FOUND_ERROR = -32601
    JSONRPC_INVALID_PARAMS_ERROR = -32602
    JSONRPC_INTERNAL_ERROR = -32603
    JSONRPC_PARSE_ERROR = -32700
    AUTH_ERROR = -32000
    INVALID_EVENT_NAME = -32001
    INVALID_PROMISE_NAME = -32002
    METHOD_NOT_SUPPORTED = -32003
    SETUP_CONTROLLER_MISSING_ERROR = 10001
    SETUP_WIZARD_LINK_ERROR = 10002
    SETUP_WIZARD_HOST_NONCE_GEN_ERROR = 10003
    SETUP_WIZARD_SHOW_INFINITE_DOWNGRADE_CALLED_UNEXPECTEDLY = 10004
    SETUP_WIZARD_REROUTE_ERROR = 10005
    TWO_ACCOUNT_CONTROLLER_MISSING = 10101
    NAVIGATION_SERVICE_UNAVAILABLE = 10701
    NAVIGATION_FAILED = 10702
    INFINITE_STATE_UPDATE_FAILED = 10802
    
    def __init__(self, javascript_bridge_view_context, pipe, csp_error_func, logger = None, machine_context = None, instance_tracker = None, timed_bridge_call_tracker = ('javascript_bridge_view_context', 'Optional[JavaScriptBridgeViewContext]', 'pipe', 'JavaScriptBridgePipeInterface', 'csp_error_func', 'Callable[[Text, Text, Text, int], None]', 'logger', 'HtmlViewLogger', 'machine_context', 'MachineContext', 'instance_tracker', 'bridge_v2.MarshalledInstanceTracker', 'timed_bridge_call_tracker', 'TimedBridgeCallTracker', 'return', 'None')):
        self._connection_opened = False
        self._message_buffer_lock = Lock()
        self._message_buffer = []
        self._javascript_bridge_view_context = javascript_bridge_view_context
        self._pipe = pipe
        self._pipe.register_callbacks(self.on_message, self.on_connection_opened, csp_error_func)
        self._logger = logger
        self._machine_context = machine_context
        self._instance_tracker = instance_tracker
        self._timed_bridge_call_tracker = timed_bridge_call_tracker

    
    def on_connection_opened(self = None):
        self._message_buffer_lock
        if JavaScriptBridgeEventTracing.should_trace():
            TRACE('SERVERVIEW_JS_BRIDGE on_connection_opened: %d early events', len(self._message_buffer))
        if not self._connection_opened:
            self._connection_opened = True
            for message in self._message_buffer:
                TRACE('SERVERVIEW_JS_BRIDGE on_connection_opened[early] %s', message.payload[:256])
                self._send_message(message)
                self._message_buffer = []
                None(None, None)
                return None
                with None:
                    if not None:
                        pass

    
    def on_message(self = None, message = None):
        
        try:
            if JavaScriptBridgeEventTracing.should_trace():
                TRACE('SERVERVIEW_JS_BRIDGE on_message [message=%r]', message)
            request = json.loads(message, object_hook = bridge_v2.json_unbox_records)
        except ValueError:
            e = None
            self._sendParseError(e.args[0])
            e = None
            del e
            return None
            e = None
            del e

        (isValidRequest, requestId, errorMessage) = self._validateRequest(request)
    # WARNING: Decompyle incomplete

    
    def cleanup(self = None):
        self._pipe.cleanup()

    
    def get_javascript_bridge_view_context(self = None):
        return self._javascript_bridge_view_context

    
    def get_logger(self = None):
        return self._logger

    
    def get_machine_context(self = None):
        return self._machine_context

    
    def get_app(self = None):
        return self._machine_context.account_manager._account_manager._app

    
    def get_instance_tracker(self = None):
        return self._instance_tracker

    
    def get_timed_bridge_call_tracker(self = None):
        return self._timed_bridge_call_tracker

    
    def send_message(self = None, message = None):
        self._message_buffer_lock
        if not self._connection_opened:
            self._message_buffer.append(message)
            if JavaScriptBridgeEventTracing.should_trace():
                TRACE('SERVERVIEW_JS_BRIDGE send_message[early events] %r', message[:256])
            None(None, None)
            return None
        None(None, None)

    
    def _send_message(self = None, message = None):
        self._pipe.send_message_to_browser(message)

    
    def _validateRequest(self = None, request = None):
        if type(request) is not dict:
            return (False, None, 'Request root is not a dictionary.')
        if None not in request or request['jsonrpc'] != '2.0':
            return (False, None, 'JSON-RPC version is incorrectly specified. Must be 2.0.')
        if None not in request or type(request['id']) is not int:
            return (False, None, 'Request has missing or malformed Id. Must be a number.')
        if None not in request or type(request['method']) is not Text:
            return (False, request['id'], 'Request has missing or malformed method signature. Must be string.')
        return (None, request['id'], None)

    
    def _handleValidRequest(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _send_method_response(self = None, requestId = None, response = None):
        (response_code, response_object, on_send, debug_name) = response
    # WARNING: Decompyle incomplete

    
    def _catch_internal_exceptions(self = None, fut = None):
        if fut.state() == Future.State.Exception:
            exc_info = fut.exc_info()
            panic_with_report(ExitCode.FATAL_EXCEPTION, 'bridge future in bad state {}'.format(fut.state()), DesktopComponent.HTML_VIEWS, exc_info = exc_info)
        return fut

    
    def _sendMethodResponseSuccess(self, requestId = None, result = None, on_send = None, debug_name = ('requestId', 'int', 'result', 'Dict[Text, Any]', 'on_send', 'Callable[[], None]', 'debug_name', 'Optional[Text]', 'return', 'None')):
        response = {
            'jsonrpc': '2.0',
            'id': requestId,
            'result': result }
        self.send_message(MessageToBrowser(json.dumps(response, default = bridge_v2.json_box_records), on_send, debug_name))

    
    def _sendMethodResponseError(self = None, requestId = None, errorCode = None, errorMessage = ('requestId', 'Optional[int]', 'errorCode', 'int', 'errorMessage', 'Text', 'return', 'None')):
        response = {
            'jsonrpc': '2.0',
            'id': requestId,
            'error': {
                'code': errorCode,
                'message': errorMessage } }
        self.send_message(MessageToBrowser(json.dumps(response, default = bridge_v2.json_box_records), (lambda : pass), None))

    
    def _sendParseError(self = None, errorMessage = None, requestId = None):
        self._sendMethodResponseError(requestId, self.JSONRPC_PARSE_ERROR, errorMessage)

    
    def _sendInvalidRequestError(self = None, errorMessage = None, requestId = None):
        self._sendMethodResponseError(requestId, self.JSONRPC_INVALID_REQUEST_ERROR, errorMessage)

    
    def send_event(self = None, event_name = None, args = None):
        raise NotImplementedError('Server View Named Events are not supported anymore')

    
    def send_signal(self, signal_id = None, data = None, on_send = None, debug_name = ('signal_id', 'Text', 'data', 'Any', 'on_send', 'Callable[[], None]', 'debug_name', 'Text', 'return', 'None')):
        self._send_notification('onSignalFromDesktopClient', {
            'name': signal_id,
            'args': [
                data] }, on_send, debug_name)

    
    def send_promise(self = None, name = None, *args):
        raise NotImplementedError('Server View Named Promises are not supported anymore')

    
    def _send_notification(self, method_name = None, parameters = None, on_send = None, debug_name = ('method_name', 'Text', 'parameters', 'Dict[AnyStr, Any]', 'on_send', 'Callable[[], None]', 'debug_name', 'Optional[Text]', 'return', 'None')):
        request = {
            'jsonrpc': '2.0',
            'method': method_name,
            'params': parameters }
        self.send_message(MessageToBrowser(json.dumps(request, default = bridge_v2.json_box_records), on_send, debug_name))



class JavaScriptBridgeTransport(HtmlViewTransportHandler):
    pass
# WARNING: Decompyle incomplete

ServerViewTransportHandler = JavaScriptBridgeTransport

def invokeBridgeMethod(methodName = None, connection = None, id = None, parameters = (None,)):
    pass
# WARNING: Decompyle incomplete

BridgeFunctionParams = NamedTuple('BridgeFunctionParams', [
    ('method_name', Text),
    ('args', List[Any]),
    ('message_id', int)])
BridgeFunction = Callable[([
    ServerViewTransportHandler,
    BridgeFunctionParams], Future[BridgeResultPayload])]

def _client_bridge_function(bridgeFunctionName = None, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete

_invoke_static_method = (lambda connection = None, function_params = None: (class_name, method_name, params, stack) = function_params.argsbridge_v2.invoke_static_method(connection.get_instance_tracker(), class_name, method_name, params, stack, connection.get_timed_bridge_call_tracker(), function_params.message_id, connection.get_logger().component))()
_invoke_instance_method = (lambda connection = None, function_params = None: (instance_type, instance_id, method_name, params, stack) = function_params.argsbridge_v2.invoke_instance_method(connection.get_instance_tracker(), instance_type, instance_id, method_name, params, stack, connection.get_timed_bridge_call_tracker(), function_params.message_id, connection.get_logger().component))()
_connect_signal = (lambda connection = None, function_params = None: pass# WARNING: Decompyle incomplete
)()
_disconnect_signal = (lambda connection = None, function_params = None: (signal_id, stack) = function_params.argsbridge_v2.disconnect_signal(connection.get_instance_tracker(), signal_id, stack, connection.get_logger().component))()
