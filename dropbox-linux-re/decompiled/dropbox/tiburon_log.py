# Source Generated with Decompyle++
# File: tiburon_log.pyc (Python 3.11)

from __future__ import absolute_import
import hashlib
from datetime import datetime
from typing import Any, Callable, Dict, Optional, Text, Tuple
from six import iteritems
from six.moves.urllib.parse import parse_qs, urlparse
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.model.types import FileId
from dropbox.platform import platform as system_platform
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath, ServerPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.remote_props import MountProperties, RemoteLocationProperties
log_tiburon_event = (lambda event_name, data: if 'extra' in data and 'shared_link' in data['extra']:
report_bad_assumption('Leaking shared link in tiburon logs!')del data['extra']['shared_link']platform = 'desktop_' + system_platformnow = datetime.utcnow()new_data = data.copy()new_data['event_name'] = event_namenew_data['utc_ts'] = int((now - datetime(1970, 1, 1)).total_seconds())new_data['utc_date'] = now.strftime('%Y-%m-%d')new_data['platform'] = platform# WARNING: Decompyle incomplete
)()
get_nsid_nspath_content_type = (lambda account = None, sync_engine_adapter = handle_exceptions, server_path = handle_exceptions, is_dir = ('account', 'AccountInterface', 'sync_engine_adapter', 'SyncEngineAdapter', 'server_path', 'ServerPath', 'is_dir', 'bool', 'return', 'Tuple[int, Optional[str], str]'): pass# WARNING: Decompyle incomplete
)()

def get_tkey_sha1_from_url(shared_link_url = None):
    if shared_link_url:
        url_path_parts = urlparse(shared_link_url).path.split('/')
        if len(url_path_parts) <= 2:
            return None
        tkey = None[2].encode()
        return hashlib.sha1(tkey).hexdigest()


def get_scl_token_sha1_from_url(scl_link_url = None):
    if scl_link_url:
        url_path_parts = urlparse(scl_link_url).path.split('/')
        if len(url_path_parts) <= 3:
            return None
        key = None[3].encode()
        return hashlib.sha1(key).hexdigest()


def get_rlkey_sha1_from_url(scl_link_url = None):
