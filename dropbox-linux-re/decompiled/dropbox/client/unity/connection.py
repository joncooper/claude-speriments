# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

from __future__ import absolute_import, annotations
import binascii
import json
import os
import re
import socket
from collections import namedtuple
from functools import partial
from threading import Event
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
import psutil
from apex.metrics.metrics import Counter, Metric, MetricsReporter
from six import iteritems
from six.moves import range
from tornado import httpserver, ioloop, tcpserver, web, websocket
from build_number import is_frozen
from dropbox.build_common import get_build_number
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventClass
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.gandalf import Gandalf
from dropbox.client.unity.threading import on_unity_start_stop_thread, on_unity_worker_thread, UnityStartStopThread, UnityWorkerThread
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import DropboxServerError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import UNITY_SERVER_EVENT
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_bytes, make_str, make_unicode
from dropbox.platform import platform
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info
UNITY_VERSION = 16

def hexencode_nonce(nonce = None):
    return make_str(binascii.hexlify(make_bytes(nonce)))


def UnityPermissionLevel():
    '''UnityPermissionLevel'''
    
    def __repr__(self):
        if self.web_has_auth and self.client_has_auth:
            if self.local_information_allowed:
                return 'secure_local'
            return None
        if None.client_has_auth:
            return 'insecure_web'
        if None.web_has_auth:
            return 'insecure_client'


UnityPermissionLevel = <NODE:27>(UnityPermissionLevel, 'UnityPermissionLevel', namedtuple('UnityPermissionLevel', [
    'web_has_auth',
    'client_has_auth',
    'local_information_allowed']))
SECURE_LOCAL_PERMISSION = UnityPermissionLevel(True, True, True)
SECURE_PERMISSION = UnityPermissionLevel(True, True, False)
INSECURE_CLIENT_PERMISSION = UnityPermissionLevel(True, False, False)
INSECURE_WEB_PERMISSION = UnityPermissionLevel(False, True, False)
INSECURE_PERMISSION = UnityPermissionLevel(False, False, False)
UnityRoutingInfo = namedtuple('UnityRoutingInfo', [
    'handler',
    'is_feature',
    'asynchronous',
    'allowed_permissions'])

class UnityError(Exception):
    pass
# WARNING: Decompyle incomplete


class UnityLogger(object):
    UNITY_SESSION_ID_LEN = 32
    
    def __init__(self = None, host_int = None, account_manager = None, account = (None,)):
        self._data = {
            'logging_source': 'client',
            'client_unity_version': UNITY_VERSION,
            'os_version': platform,
            'host_id': host_int }
        self._update_authed_user_ids(account_manager)
        self._account = account

    
    def generate_session_id(self):
        self._data['unity_session_id'] = hexencode_nonce(os.urandom(self.UNITY_SESSION_ID_LEN))

    
    def _update_authed_user_ids(self, account_manager):
        authed_ids = []
        if len(account_manager.linked_accounts) == 0:
            report_bad_assumption('UnityLogger initialized but no accounts linked')
        if account_manager.personal and account_manager.personal.uid:
            authed_ids.append(account_manager.personal.uid)
        if account_manager.business and account_manager.business.uid:
            authed_ids.append(account_manager.business.uid)
        self._data['authed_user_ids'] = authed_ids

    
    def update(self, **attrs):
        self._data.update(attrs)

    
    def report_event(self, event_name, uid = (None,), **extra):
        self._data['event_name'] = event_name
        if self._data['authed_user_ids']:
            pass
        self._data['user_id'] = self._data['authed_user_ids'][0] if not uid else None
        self._data['extra'] = extra
    # WARNING: Decompyle incomplete

    
    def get_log_data_for_web(self, is_secure = (False,)):
        pass
    # WARNING: Decompyle incomplete

    
    def is_web_data_valid(self, web_data):
