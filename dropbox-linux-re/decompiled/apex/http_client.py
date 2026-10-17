# Source Generated with Decompyle++
# File: http_client.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
import itertools
from concurrent.futures import Future as CFFuture, InvalidStateError as CFInvalidStateError
from typing import Dict, Iterator, List, Optional, Tuple, TYPE_CHECKING
from apex._apex import ffi, lib
from dropbox.proto.apex.dbxconn_pb2 import Request, Response as ResponseProto
if TYPE_CHECKING:
    from apex.context import ApexContext
CHUNK_TYPE_HEAD = 0
CHUNK_TYPE_BODY = 1
CHUNK_TYPE_END = 2
CHUNK_TYPE_ERROR = 3
Response = <NODE:12>()
ResponseHead = <NODE:12>()

class ReceiverDropped(Exception):
    pass


class InvalidHost(Exception):
    pass


class ClientInitiatedReconnect(Exception):
    pass


class Timeout(Exception):
    pass


class ProtocolError(Exception):
    pass


def _error_from_response_proto(response = None):
    which = response.WhichOneof('response')
    if which == 'receiver_dropped':
        return ReceiverDropped()
    if None == 'invalid_host':
        return InvalidHost()
    if None == 'client_initiated_reconnect':
        return ClientInitiatedReconnect()
    if None == 'timeout':
        return Timeout()
    if None == 'protocol_error':
        return ProtocolError(response.protocol_error.msg, response.protocol_error.request_id)
    return Exception(f'''unexpected response enum {which!r}''')


class _BufferedHandler:
    
    def __init__(self = None, future = None):
        self._future = future
        self._head = None
        self._chunks = []

    
    def on_head(self = None, head = None):
        self._head = head

    
    def on_body(self = None, chunk = None):
        self._chunks.append(chunk)

    
    def on_end(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def on_error(self = None, err = None):
        self._set_exception(err)

    
    def _set_exception(self = None, err = None):
        
        try:
            self._future.set_exception(err)
            return None
        except CFInvalidStateError:
            return None



_CALLBACK_ID: 'Iterator[int]' = itertools.count()
_CALLBACK_CONTEXTS: 'Dict[int, _BufferedHandler]' = { }
handle_response = (lambda context = None, chunk_type = None, response_bytes = ffi.def_extern(), response_len = ('context', 'ffi.CData', 'chunk_type', 'int', 'response_bytes', 'ffi.CData', 'response_len', 'int', 'return', 'None'): callback_id = int(ffi.cast('unsigned long', context))handler = _CALLBACK_CONTEXTS.get(callback_id)# WARNING: Decompyle incomplete
)()

class HttpClient:
    
    def __init__(self = None, context = None, locale = None, legacy_usage_skip_metrics = ('context', 'ApexContext', 'locale', 'str', 'legacy_usage_skip_metrics', 'bool', 'return', 'None')):
        c_locale = ffi.new('char[]', locale.encode('utf-8'))
        self.inner = lib.http_client_init(context.inner, c_locale, legacy_usage_skip_metrics)

    
    def __del__(self = None):
        lib.http_client_destroy(self.inner)

    
    def request(self = None, request = None):
        pass
    # WARNING: Decompyle incomplete


