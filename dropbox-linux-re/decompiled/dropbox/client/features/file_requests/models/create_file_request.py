# Source Generated with Decompyle++
# File: create_file_request.pyc (Python 3.11)

from typing import Any, cast, Iterable, Optional, Text
from six.moves.urllib import parse as urlparse
from build_number.features import feature_enabled
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.file_requests.models.constants import FILE_REQUEST_DESKTOP_CREATION_FEATURE, FileRequestEventType
from dropbox.client.gandalf import Gandalf
from dropbox.client.multiaccount.role import Roles
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import FILE_REQUEST_EVENT
from dropbox.shared.server_path import ServerPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

def file_request_creation_enabled(gandalf = None, account = None):
    if not account:
        return False
    if not feature_enabled(FILE_REQUEST_DESKTOP_CREATION_FEATURE):
        return False
    gating_variant = None.get_variant(FILE_REQUEST_DESKTOP_CREATION_FEATURE, account = account)
    return gating_variant == 'ON'


def report_file_request_event(event_name = None, account = None, **extra_dict):
    pass
# WARNING: Decompyle incomplete


def validate_path_and_build_url_params(sync_engine_adapter = None, account = None, path = None):
    pass
# WARNING: Decompyle incomplete


def build_url_params(account = None, server_ns_path = None):
    (ns_id, relative_path) = server_ns_path.ns_rel()
    url_params = f'''path={urlparse.quote(relative_path.encode('utf-8'))!s}&ns_id={ns_id!s}&referrer={'collab_browse'!s}'''
    if account.role:
        role = Roles.to_server(account.role)
        if role:
            url_params += '&role=%s' % role
    return url_params

