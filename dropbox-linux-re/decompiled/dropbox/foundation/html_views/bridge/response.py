# Source Generated with Decompyle++
# File: response.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import Any, Callable, NamedTuple, Optional, Text
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.futures.basic import BaseFuture
from dropbox.foundation.html_views.common.logging import HtmlViewLogger, HtmlViewLoggerEvent
from dropbox.foundation.trace.trace_js_bridge import JavaScriptBridgeEventTracing
from dropbox.trace import TRACE
BridgeResultPayload = NamedTuple('BridgeResultPayload', [
    ('response_code', Optional[int]),
    ('response_object', Any),
    ('on_send', Callable[([], None)]),
    ('debug_name', Optional[Text])])

def BridgeFunctionResponseInfo():
    '''BridgeFunctionResponseInfo'''
    pass
# WARNING: Decompyle incomplete

BridgeFunctionResponseInfo = <NODE:27>(BridgeFunctionResponseInfo, 'BridgeFunctionResponseInfo', ResolvedFuture[BridgeResultPayload])

def DeferredBridgeFunctionResponse():
    '''DeferredBridgeFunctionResponse'''
    
    def resolve(self = None, result = None):
        self.set_result(BridgeResultPayload(None, result, (lambda : pass), None))

    
    def reject(self = None, code = None, message = None):
        self.set_result(BridgeResultPayload(code, message, (lambda : pass), None))

    
    def _cancel_impl(self = None):
        pass
    # WARNING: Decompyle incomplete


DeferredBridgeFunctionResponse = <NODE:27>(DeferredBridgeFunctionResponse, 'DeferredBridgeFunctionResponse', BaseFuture[BridgeResultPayload])
BridgeFunctionResult = Future[BridgeResultPayload]
