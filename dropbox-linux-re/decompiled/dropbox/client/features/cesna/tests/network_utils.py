# Source Generated with Decompyle++
# File: network_utils.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import functools
import ipaddress
import socket
import time
from contextlib import closing
from socket import AddressFamily, getaddrinfo as _getaddrinfo, socket as _socket, SocketKind
from typing import Any, Callable, Dict, Optional, Sequence, Tuple
from urllib.parse import ParseResult, urlparse
V6_CHECK_DOMAIN = 'tcp6://www.dropbox.com:443'
V6_CHECK_TIMEOUT = 1
V6_CACHE_EXPIRE = 3600

class V4MappedAddress(Exception):
    pass


def _time_memoized(timeout_seconds = None):
    pass
# WARNING: Decompyle incomplete

has_ipv6_support = (lambda : found_v6 = False# WARNING: Decompyle incomplete
)()

def resolve_target(target = None):
    netloc_parts = target.netloc.split(':')
    host = ':'.join(netloc_parts[0:-1])
    port = int(netloc_parts[-1])
    addr_type = 0
    if target.scheme == 'tcp4':
        addr_type = socket.AF_INET
    elif target.scheme == 'tcp6':
        addr_type = socket.AF_INET6
    elif target.scheme == 'tcp':
        addr_type = 0
    addrinfo = _getaddrinfo(host, port, addr_type, 0, socket.IPPROTO_TCP)
    return (addrinfo[0][0], addrinfo[0][4])

