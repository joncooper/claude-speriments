# Source Generated with Decompyle++
# File: tcp_connect.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import socket
import time
from contextlib import closing
from socket import socket as _socket
from typing import Any, Dict, Text
from six.moves.urllib.parse import ParseResult, urlparse
from base import CesnaTestBase, CesnaTestInterface
from dropbox.client.features.cesna.tests.base import InvalidCesnaTestError, UnsupportedCesnaTestError
from dropbox.client.features.cesna.tests.network_utils import has_ipv6_support, resolve_target
TCP_TIMEOUT_SECONDS = 5

def construct_tcpconnect_test(test_def = None):
    if 'tcpConnect' not in test_def or 'targetUri' not in test_def['tcpConnect']:
        raise InvalidCesnaTestError('TCP_CONNECT specific arguments not found')
    target_uri = test_def['tcpConnect']['targetUri']
    target = urlparse(target_uri)
    if target.scheme not in ('tcp', 'tcp4', 'tcp6'):
        raise InvalidCesnaTestError('Invalid target_uri scheme: "{0}"'.format(target.scheme))
    if not target.scheme == 'tcp6' and has_ipv6_support():
        raise UnsupportedCesnaTestError('This client does not support IPv6 tests')
    return TcpConnectTest(test_def, target)


class TcpConnectTest(CesnaTestBase):
    pass
# WARNING: Decompyle incomplete

