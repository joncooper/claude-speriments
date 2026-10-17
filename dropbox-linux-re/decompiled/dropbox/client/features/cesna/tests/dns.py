# Source Generated with Decompyle++
# File: dns.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import time
from typing import Any, Dict, Text
from six.moves.urllib.parse import ParseResult, urlparse
from base import CesnaTestBase
from dropbox.client.features.cesna.tests.base import CesnaTestInterface, InvalidCesnaTestError
from dropbox.client.features.cesna.tests.network_utils import resolve_target
TCP_TIMEOUT_SECONDS = 5

def construct_dns_test(test_def = None):
    if 'dns' not in test_def or 'domainName' not in test_def['dns']:
        raise InvalidCesnaTestError('DNS specific arguments not found')
    if 'recordType' not in test_def['dns']:
        raise InvalidCesnaTestError('No DNS record type specified')
    if test_def['dns']['recordType'] == 'A':
        uri = 'tcp4://{0}:0'.format(test_def['dns']['domainName'])
    elif test_def['dns']['recordType'] == 'AAAA':
        uri = 'tcp6://{0}:0'.format(test_def['dns']['domainName'])
    else:
        raise InvalidCesnaTestError('Invalid DNS record type: {0}'.format(test_def['dns']['recordType']))
    target = urlparse(uri)
    return DnsTest(test_def, target)


class DnsTest(CesnaTestBase):
    pass
# WARNING: Decompyle incomplete

