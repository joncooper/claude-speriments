# Source Generated with Decompyle++
# File: add_to_transfer.pyc (Python 3.11)

from typing import Any, cast, Iterable, Iterator, List, Optional
from six.moves.urllib import parse as urlparse
import dropbox.fsutil as dropbox
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.transfer.constants import TRANSFER_MAX_FILE_NUM, TransferEventType, TransferInadequatePermissionsError, TransferTooManyItemsError, TransferUnsyncedItemsError
from dropbox.client.multiaccount.role import Roles
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.event_names import TRANSFER_EVENT
from dropbox.platform import IS_LINUX
from dropbox.sharing.permissions import allow_copy_dropbox_link_nucleus
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
FileSystem = Any

def report_transfer_event(event_name = None, account = None, **extra_dict):
    pass
# WARNING: Decompyle incomplete


def validate_paths_and_get_file_ids(sync_engine_adapter = None, account = None, pathlist = None):
    nucleus_api = sync_engine_adapter.nucleus_api(account)
# WARNING: Decompyle incomplete


def build_url_params(account = None, fileids = None):
    delimited = '.'.join(fileids)
    url_params = 'fileids=%s' % urlparse.quote(delimited.encode('utf-8'))
    if account.role:
        role = Roles.to_server(account.role)
        if role:
            url_params += '&role=%s' % role
    return url_params


def transfer_desktop_creation_enabled(account = None):
    if not account:
        return False
    if None:
        return False
    if None.ui_flags.get('team_file_transfers_disabled', False):
        return False


def _pathlist_is_dir(file_system = None, pathlist = None):
    pass
# WARNING: Decompyle incomplete

