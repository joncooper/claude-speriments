# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

import base64
import json
import random as insecure_random
from typing import Any, Callable, cast, Dict, List, Optional, Tuple, Type, Union


stone_validators
from apex.context import ApexContext
import stone.backends.python_rsrc.stone_validators, backends, python_rsrc
from apex.dbxconn import Connection as ApexConnection
from apex.http_client import HttpClient, Response
from stone.backends.python_rsrc.stone_serializers import CallerPermissionsInterface, json_compat_obj_decode, json_decode, json_encode
from exceptions import APIv2AccessError, APIv2AuthError, APIv2EndpointError
from interface import AppAuth, ClientAuth, HostKeyAuth, NoAuth, OAuthTokenAuth
import dropbox.api.v2.datatypes.auth as dropbox

socks
from dropbox.client.configuration.interface import LocalConfigurationInterface
import dropbox.client_api.socks, client_api
from dropbox.client.constants import DROPBOX_API_APP_KEY, DROPBOX_API_APP_SECRET
from dropbox.client.message_queue import InstrumentedMessageQueueThread
from dropbox.client.proxy import ProxyInfo
from dropbox.client.reporting.request_status import REPORT_PERCENT_URL
from dropbox.client_api.chillout_tracker import ChilloutTracker
from dropbox.client_api.exceptions import DropboxResponseClientError, DropboxResponseServerError, HTTP400Error, HTTP401Error, HTTP403Error, HTTP404Error, HTTP409Error, HTTP429Error, is_transient_error, TransientNetworkError
from dropbox.client_api.throttle import get_throttle_prefs, ThrottlePrefs
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connectivity_watch.watch_interface import ConnectivityState, ConnectivityWatchInterface
from dropbox.db_thread import db_thread_with_task_timing
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures.basic import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.foundation.transitional.wrapper_future import WrapperFuture
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.proto.apex.dbxconn_pb2 import Config, Header, Request
from dropbox.proto.network.network_pb2 import UrlInfo
from dropbox.sqlite3_exceptions import DropboxSqliteError
from dropbox.sqlite3_helpers import Cursor
from dropbox.sync_root.gating import file_provider_supported
from dropbox.timed_event import TimedEvent
from dropbox.trace import TRACE
from dropbox.url_info import dropbox_url_info, DropboxURLInfo, ProtocolHostPort, to_protocol_host_port
MYPY = False
if MYPY:
    from dropbox.client.proxy import MetaProxyInfo
PERIODIC_CONFIG_UPDATE_SECS: 'int' = 3600
DEFAULT_HOSTS: 'Dict[str, ProtocolHostPort]' = {
    'authserver': to_protocol_host_port(dropbox_url_info.api_host),
    'apiv2server': to_protocol_host_port(dropbox_url_info.hosts['apiv2server']),
    'metaserver': to_protocol_host_port(dropbox_url_info.hosts['metaserver']),
    'webserver': to_protocol_host_port(dropbox_url_info.webserver_host),
    'metaexcserver': to_protocol_host_port(dropbox_url_info.hosts['metaexcserver']),
    'blockexcserver': to_protocol_host_port(dropbox_url_info.hosts['blockexcserver']),
    'staticserver': to_protocol_host_port(dropbox_url_info.hosts['staticserver']),
    'edgelivecdnserver': to_protocol_host_port(dropbox_url_info.hosts['edgelivecdnserver']),
    'boltserver': to_protocol_host_port(dropbox_url_info.hosts['boltserver']),
    't8': to_protocol_host_port(dropbox_url_info.hosts['t8']),
    'd6': to_protocol_host_port(dropbox_url_info.hosts['d6']) }
UPDATEABLE_HOST_LIST: 'List[str]' = [
    'apiv2server',
    'apiv2blockserver',
    'beaconserver',
    'blockexcserver',
    'blockserver',
    'boltserver',
    'metaexcserver',
    'metaserver',
    'nsfserver',
    'paperserver',
    'photo-blockserver',
    'previews-dbx-server',
    'previews-duc-server',
    'sfeserver',
    't8',
    'thunderserver',
    'staticserver',
    'edgelivecdnserver',
    'webserver']
THROTTLE_PREF_HOSTS: 'List[str]' = [
    'blockexcserver',
    'blockserver',
    'nsfserver',
    'photo-blockserver',
    'sfeserver']
SUCCESS_STATUS_CODES = (200, 204)

class InternalCallerPermissions(CallerPermissionsInterface):
    permissions = (lambda self = None: [
'internal'])()


class Connection:
    
    def __init__(self, apex_context = None, locale = None, meta_proxy_info = None, throttle_prefs = ('apex_context', 'ApexContext', 'locale', 'Optional[str]', 'meta_proxy_info', 'Optional[MetaProxyInfo]', 'throttle_prefs', 'Optional[ThrottlePrefs]', 'legacy_usage_skip_metrics', 'bool', 'return', 'None'), *, legacy_usage_skip_metrics):
