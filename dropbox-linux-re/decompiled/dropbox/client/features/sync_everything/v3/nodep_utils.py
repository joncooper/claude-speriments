# Source Generated with Decompyle++
# File: nodep_utils.pyc (Python 3.11)

from typing import Any, List, Optional, Set, Text
from build_number.platform import IS_WINDOWS
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.trace import TRACE, WARNING

def map_names(ids = None):
    return ids()


def map_names_l(ids = None):
    return ids()


def ignored_merge_errors():
    if IS_WINDOWS:
        return {
            'desktop.ini'}
    return set()


def are_roles_equal(bidl_role = None, role = None):
