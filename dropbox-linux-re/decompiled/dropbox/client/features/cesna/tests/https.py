# Source Generated with Decompyle++
# File: https.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import time
from typing import Any, Dict, Text
from six.moves import http_client as httplib
from six.moves.urllib.parse import ParseResult, urlparse
from base import CesnaTestBase, CesnaTestInterface
from dropbox.client.features.cesna.tests.base import InvalidCesnaTestError
from dropbox.ssl.context import get_dropbox_ssl_context
HTTPS_TIMEOUT_SECONDS = 5

def construct_https_test(test_def = None):
    if 'https' not in test_def or 'targetUri' not in test_def['https']:
        raise InvalidCesnaTestError('HTTPS specific arguments not found')
    target_uri = test_def['https']['targetUri']
    target = urlparse(target_uri)
    if target.scheme not in ('https', 'http'):
        raise InvalidCesnaTestError('Invalid target_uri scheme: "{0}"'.format(target.scheme))
    return HttpsConnectTest(test_def, target)


class HttpsConnectTest(CesnaTestBase):
    pass
# WARNING: Decompyle incomplete

