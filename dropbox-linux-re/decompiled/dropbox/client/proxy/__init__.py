# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import
import sqlite3
import types
from typing import Any, Callable, cast, Dict, List, Optional, Text, Tuple, TypeVar, Union
from six.moves.urllib import parse as urlparse
from six.moves.urllib.request import getproxies, proxy_bypass

socks
from dropbox.callbacks import Handler
import dropbox.client_api.socks, client_api
from dropbox.client.background_worker import on_background_thread
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.high_trace import report_bad_assumption
from dropbox.client.proxy.wpad_proxy_base import WpadProxyBase
from dropbox.client_api.exceptions import HTTPAuthenticationNeededError, HTTPError, ProxyError, Socks4Error, Socks5AuthError, Socks5Error, UnsupportedProxyConfigurationError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_bytes, make_str
from dropbox.i18n import trans
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.preferences import AUTO_PROXY, MANUAL_PROXY, NO_PROXY, SOCKS4, SOCKS5
from dropbox.sqlite3_exceptions import ConnectionClosedError, DatabaseOrDiskFullError, DiskIOError
from dropbox.threading import Lock
from dropbox.trace import TRACE
_F = TypeVar('_F', bound = Callable)

def get_proxy_for_platform():
    if IS_MAC:
        autoreleasepool = autoreleasepool
        import dropbox.mac.internal
        autoreleasepool()
        wpad_proxy_mac = wpad_proxy_mac
        import dropbox.client.proxy
        None(None, None)
        return 
    with None:
        if not None:
            pass
    return None
    if IS_WINDOWS:
        wpad_proxy_win
        return wpad_proxy_win.WpadProxyWin()


def exc_arg(e = None, idx = None):
    if hasattr(e, 'args'):
        return e.args[idx]
    return None[idx]


class ProxyInfo(object):
    
    def __init__(self, proxy_type, proxy_host = None, proxy_port = None, proxy_rdns = None, proxy_user = (True, None, None), proxy_pass = ('proxy_type', 'int', 'proxy_host', 'Text', 'proxy_port', 'int', 'proxy_rdns', 'bool', 'proxy_user', 'Optional[bytes]', 'proxy_pass', 'Optional[bytes]', 'return', 'None')):
        (self.proxy_type, self.proxy_host, self.proxy_port, self.proxy_rdns, self.proxy_user, self.proxy_pass) = (proxy_type, proxy_host, proxy_port, proxy_rdns, proxy_user, proxy_pass)
        if not self.isgood():
            report_bad_assumption('constructed a bad ProxyInfo: %s', self)
            return None

    
    def __str__(self = None):
