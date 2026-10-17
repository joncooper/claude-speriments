# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any, Callable, Dict, Text, Tuple, Type
from base import CesnaTestBase, CesnaTestInterface, InvalidCesnaTestError
from dns import construct_dns_test
from https import construct_https_test
from tcp_connect import construct_tcpconnect_test
TEST_CONSTRUCTORS: 'Dict[Text, Callable[[Dict[Text, Any]], CesnaTestInterface]]' = {
    'TCP_CONNECT': construct_tcpconnect_test,
    'DNS': construct_dns_test,
    'HTTPS': construct_https_test }

def _verify_test_json(json_data = None):
