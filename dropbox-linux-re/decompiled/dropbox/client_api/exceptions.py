# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import errno
from http.client import client as httplib
import socket
import ssl
from typing import Any, Dict, List, Optional, Text, Tuple, Union
from apex.http_client import ClientInitiatedReconnect as NewClientInitiatedReconnect, ProtocolError, Timeout as RequestTimeout
from dropbox.exception.severity import Severity
from dropbox.platform import IS_WINDOWS

class ProxyError(Exception):
    
    def __init__(self = None, value = None):
        self.value = value

    
    def __str__(self = None):
        return repr(self.value)



class GeneralProxyError(ProxyError):
    pass


class Socks5AuthError(ProxyError):
    pass


class Socks5Error(ProxyError):
    pass


class Socks4Error(ProxyError):
    pass


class HTTPError(ProxyError):
    pass


class HTTPAuthenticationNeededError(ProxyError):
    pass


class UnsupportedProxyConfigurationError(ProxyError):
    pass


class TransientNetworkError(Exception):
    pass
# WARNING: Decompyle incomplete


class DropboxServerError(Exception):
    pass
# WARNING: Decompyle incomplete


class DropboxResponseClientError(DropboxServerError):
    pass


class DropboxResponseServerError(TransientNetworkError, DropboxServerError):
    pass
# WARNING: Decompyle incomplete


class HTTP400Error(DropboxResponseClientError):
    pass


class HTTP401Error(DropboxResponseClientError):
    pass


class HTTP403Error(DropboxResponseClientError):
    pass


class HTTP404Error(DropboxResponseClientError):
    pass


class HTTP409Error(DropboxResponseClientError):
    pass


class HTTP415Error(DropboxResponseClientError):
    pass


class HTTP429Error(DropboxResponseClientError):
    pass


class HTTP500Error(DropboxResponseServerError):
    pass


class HTTP502Error(DropboxResponseServerError):
    pass


class HTTP503Error(DropboxResponseServerError):
    pass
# WARNING: Decompyle incomplete


class HTTP504Error(DropboxResponseServerError):
    _severity_class = Severity.TRACE


class ClientInitiatedDisconnect(TransientNetworkError):
    pass
# WARNING: Decompyle incomplete


class ClientInitiatedReconnect(TransientNetworkError):
    pass
# WARNING: Decompyle incomplete


class ServerListChangedDisconnect(TransientNetworkError):
    pass
# WARNING: Decompyle incomplete


class ConnectFailedOnAllAddressesError(socket.error):
    pass
# WARNING: Decompyle incomplete


class EmptyAddressesError(socket.error):
    pass
# WARNING: Decompyle incomplete


class ThumbnailerError(Exception):
    pass
# WARNING: Decompyle incomplete


class ConnectionAbortReason(object):
    CLIENT_INITIATED_DISCONNECT = 'client_initiated_disconnect'
    CLIENT_INITIATED_RECONNECT = 'client_initiated_reconnect'
    SERVER_LIST_CHANGED = 'server_list_changed'
    should_hard_kill_socket = (lambda cls = None, reason = None: reason in {
cls.CLIENT_INITIATED_DISCONNECT,
cls.CLIENT_INITIATED_RECONNECT})()
    raise_abort_exception = (lambda cls = None, reason = None: if reason == cls.CLIENT_INITIATED_DISCONNECT:
raise ClientInitiatedDisconnect()if reason == cls.CLIENT_INITIATED_RECONNECT:
raise ClientInitiatedReconnect()if reason == cls.SERVER_LIST_CHANGED:
raise ServerListChangedDisconnect()# WARNING: Decompyle incomplete
)()


class TransientErrorType(object):
    HTTP_5XX = 'TRANSIENT_HTTP_5XX'
    HTTP_503 = 'TRANSIENT_HTTP_503'
    HTTP_429 = 'TRANSIENT_HTTP_429'
    DNS_LOOKUP = 'TRANSIENT_DNS_LOOKUP'
    CONNECTION_DROPPED = 'TRANSIENT_CONNECTION_DROPPED'
    CLIENT_INITIATED = 'CLIENT_INITIATED_TRANSIENT_ERROR'
    INVALID_SSL_CERT = 'TRANSIENT_INVALID_SSL_CERT'
    OTHER_SSL_ERROR = 'TRANSIENT_OTHER_SSL_ERROR'
    SOCKET_ERROR = 'TRANSIENT_SOCKET_ERROR'
    PROXY_CONNECTION_ERROR = 'TRANSIENT_PROXY_CONNECTION_ERROR'
    UNKNOWN = 'UNKNOWN_TRANSIENT_ERROR'


def transient_error_quick_retry(e = None):
    return _transient_error_from_types(e, (TransientErrorType.HTTP_503,))


def transient_error_from_server_load(e = None):
    return _transient_error_from_types(e, (TransientErrorType.HTTP_5XX, TransientErrorType.CONNECTION_DROPPED, TransientErrorType.UNKNOWN))


def transient_error_from_network_issues(e = None):
    return _transient_error_from_types(e, (TransientErrorType.SOCKET_ERROR, TransientErrorType.DNS_LOOKUP))


def _transient_error_from_types(e = None, types_to_filter = None):
    error_type = is_transient_error(e)
# WARNING: Decompyle incomplete


def is_transient_error(e = None):
