# Source Generated with Decompyle++
# File: dropbox_connection.pyc (Python 3.11)

import base64
import contextlib
import gzip
import json
import pprint
import zlib
from io import BytesIO
from time import time as _time
from typing import Any, Callable, cast, Dict, Iterable, List, Mapping, Optional, Set, Text, Tuple, Union
from uuid import UUID
from apex.context import ApexContext
from six import iteritems
from six.moves.urllib.parse import urlencode
from build_number import BUILDID
from dropbox.build_common import get_build_number
from dropbox.callbacks import Handler
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.linked_host_telemetry import get_linked_host_ids_for_telemetry, has_mti_team_accounts as _has_mti_team_accounts
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.sync_everything.constants import BackupDisableType
from dropbox.client.ping_constants import DualPingSource
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.status.label import StatusLabel
from dropbox.client.unlink_cookie import get_insecure_unique_host_ints
from dropbox.client_api.connection.connection import Connection
from dropbox.client_api.connection.retry import default_legacy_retry
from dropbox.client_api.connection_util import ConnectionResponse
from dropbox.client_api.exceptions import DropboxServerError, HTTP401Error
from dropbox.client_api.throttle import ThrottlePrefs
from dropbox.client_typing import JSONable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.connectivity_watch.watch_interface import ConnectivityWatchInterface
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future as _Future, ResolvedFuture
from dropbox.functions import bytesafe_json_dumps, lenient_decode, make_bytes, make_str, python_version_string
from dropbox.install_type import InstallType
from dropbox.model.types import FileId
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath
from dropbox.shared.util import restrict_keys
from dropbox.sjid_format import client_to_raw_sjid, raw_to_client_sjid
from dropbox.sync_root.handlers.macos.types import FileProviderDomainProperties
from dropbox.threading import Lock
from dropbox.trace import TRACE
from dropbox.url_info import HostPort
MYPY = False
if MYPY:
    from dropbox.client.bolt.types import BoltEncodedChannelState
    from dropbox.client.device_info import DeviceInfo
    from dropbox.client.installer_tag import InstallerTag
    from dropbox.client.proxy import MetaProxyInfo
    from dropbox.client.unsent_exceptions import UnsentExceptionInfo
DEFAULT_MAX_DATA_SIZE = 4194304
DEFAULT_STARRED_FETCH_LIMIT = 1000
API_V2_NS_PATH_PREFIX = 'nspath:'
_to_websafe = bytes.maketrans(b'+/=', b'-_~')
DROPBOX_TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
CLIENT_TRACES_ROUTE_VERSION_STORMCROW = 'desktop-dx-client-traces-route-version'

def _make_bytes_dict(**kwargs):
    pass
# WARNING: Decompyle incomplete


def validate_batch_arg(batch_arg, expected_keys):
    pass
# WARNING: Decompyle incomplete


def _byte_encode_dict(input_dict = None):
    bytes_io = contextlib.closing(BytesIO())
    g_zip = contextlib.closing(gzip.GzipFile(mode = 'wb', compresslevel = 9, fileobj = bytes_io))
    (lambda .0: pass# WARNING: Decompyle incomplete
)(json.JSONEncoder(separators = (',', ':')).iterencode(input_dict)())
    None(None, None)


class AbstractDropboxConnection:
    pass


class DropboxConnection(AbstractDropboxConnection):
    pass
# WARNING: Decompyle incomplete

