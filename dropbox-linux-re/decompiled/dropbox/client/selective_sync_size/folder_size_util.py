# Source Generated with Decompyle++
# File: folder_size_util.pyc (Python 3.11)

from typing import Dict, List, Set, Text
from build_number.features import feature_enabled
from exceptions import MultipleNamespaceError
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.gandalf import Gandalf
from dropbox.i18n import format_bytes
from dropbox.shared.server_path import get_parent_paths, ServerPath
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client_api.dropbox_connection import DropboxConnection

def get_folders_total_size(account = None, connection = None, folder_paths = None):
    if not folder_paths:
        return 0
    _validate_folders_under_same_namespace(folder_paths)
    valid_paths = _remove_overlapping_paths(folder_paths)
    paths = valid_paths()
# WARNING: Decompyle incomplete


def get_path_sizes_map(account = None, connection = None, folder_paths = None):
