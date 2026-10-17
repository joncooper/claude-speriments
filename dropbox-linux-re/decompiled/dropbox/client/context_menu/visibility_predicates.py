# Source Generated with Decompyle++
# File: visibility_predicates.pyc (Python 3.11)

from typing import List, Optional, Text
from dropbox.client.context_menu.interfaces import ContextMenuConfigInterface
from dropbox.client.context_menu.visibility_inputs import ContextMenuDbxPathProps, ContextMenuMountProps, ContextMenuUserProps
from dropbox.client.ui.common.context_menu_verbs import ContextMenuVerb
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.infinite import InfiniteAllowedContextMenus
from dropbox.sync_engine_boundary.file_locking.file_locking_types import FileLockState
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus

def _pnm_behavior_predicate_allows(dbx_path_props = None, verb_name = None):
    any_has_suppress_all = False
    any_has_suppress_shared_link = False
    any_has_suppress_ns_partition = False
    for dbx_path_prop in dbx_path_props:
        if dbx_path_prop.has_suppress_all:
            any_has_suppress_all = True
        elif dbx_path_prop.has_suppress_ns_partition:
            any_has_suppress_ns_partition = True
        if dbx_path_prop.has_suppress_shared_link:
            any_has_suppress_shared_link = True
        if any_has_suppress_all:
            return False
        if (None or any_has_suppress_ns_partition) and verb_name and verb_name in (ContextMenuVerb.SHARE, ContextMenuVerb.TIBURON_SHARE_FILE, ContextMenuVerb.CREATE_FILE_REQUEST, ContextMenuVerb.ADD_TO_TRANSFER):
            return False
        return None


def allow_open_with_hellosign(user_props = None, mount_props = None, dbx_path_props = None, context_menu_config = (None,)):
