# Source Generated with Decompyle++
# File: ping.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import base64
import json
import random as insecure_random
import time
import uuid
from typing import Any, Callable, Dict, Optional, Tuple
from six.moves.urllib.error import HTTPError
from six.moves.urllib.parse import urlencode
from six.moves.urllib.request import build_opener, HTTPRedirectHandler, Request
from build_number import BUILDID
from dropbox.build_common import get_build_number
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountDataSource
from dropbox.client.ping_constants import DualPingSource
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures.basic import Future, ResolvedFuture
from dropbox.functions import make_bytes, make_str, python_version_string
from dropbox.legacy_crypto.dropboxy import encrypt_blob_with_new_session_key
from dropbox.trace import debugging_features_are_enabled, debugging_run_type, TRACE
from dropbox.url_info import dropbox_url_info

class NoRedirectHandler(HTTPRedirectHandler):
    
    def http_error_302(self, req, fp, code, msg, headers):
        raise HTTPError(req.get_full_url(), code, msg, headers, fp)

    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302


def source_name(source = None):
    if source == DualPingSource.HOURLY_REFRESH:
        return 'hourly_refresh'
    if None == DualPingSource.REGISTER_HOST_FAILURE:
        return 'register_host'
    if None == DualPingSource.OFFLINE_STARTUP:
        return None
    return None.value


def ping_and_report(account = None, conn = None, ping_sync_frontend_fn = None, source = ('account', 'AccountInterface', 'conn', 'DropboxConnection', 'ping_sync_frontend_fn', 'Callable[[], Future[Optional[bool]]]', 'source', 'DualPingSource')):
    pass
# WARNING: Decompyle incomplete


def ping(account = None, conn = None, ping_sync_frontend = None, source = ('account', 'AccountInterface', 'conn', 'DropboxConnection', 'ping_sync_frontend', 'Callable[[], Future[Optional[bool]]]', 'source', 'DualPingSource', 'return', 'Tuple[bool, bool, Future[Optional[bool]]]')):
    pass
# WARNING: Decompyle incomplete


def _ping_http(ping_uuid, ping_number, was_linked, buildno, python_version, using_proxy = None, host_int = None, other_ping_succeeded = None, source = ('ping_uuid', 'uuid.UUID', 'ping_number', 'int', 'was_linked', 'bool', 'buildno', 'Optional[str]', 'python_version', 'str', 'using_proxy', 'bool', 'host_int', 'Optional[int]', 'other_ping_succeeded', 'Optional[bool]', 'source', 'DualPingSource', 'return', 'Dict[str, Any]')):
    url = dropbox_url_info.ping_http_url()
# WARNING: Decompyle incomplete

