# Source Generated with Decompyle++
# File: account_link_state.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Callable, Dict, Optional, Text, TypedDict
from dropbox.foundation.futures import Future
from dropbox.sync_engine_boundary.selsync import SelectiveSyncSet
from dropbox.sync_root.types import SyncRootType, SyncRootTypeReason
LinkPreferences = TypedDict('LinkPreferences', {
    'dropbox_path': Optional[str],
    'directory_ignore_set': SelectiveSyncSet,
    'open_dropbox_folder': bool,
    'show_linked_bubble': bool,
    'content_starts_online_only': Optional[bool],
    'sync_root_type': Optional[SyncRootType],
    'sync_root_type_reason': Optional[SyncRootTypeReason],
    'cloud_files_migration_opt_out': Optional[bool],
    'file_provider_opt_out': Optional[bool],
    'promote_tray_icon': Optional[bool],
    'root_folder_file_count': Optional[int],
    'selected_file_count': Optional[int] }, total = False)

class AccountLinkState(object):
    
    def __init__(self = None, directory_ignore_set = None, preauth_nonce = None):
        self.preauthed = False
        self.preauth_nonce = preauth_nonce
        self.using_typescript_auth = False
        self.dropbox_path = None
        self.dropbox_folder_name = None
        self.dropbox_path_changed = False
        self.directory_ignore_set = directory_ignore_set
        self.content_starts_online_only = None
        self.user_modified_infinite_settings = False
        self.infinite_exposed = False
        self.tray_icon_promotion_enabled = False
        self.promote_tray_icon = None
        self.cloud_files_migration_opt_out = None
        self.file_provider_opt_out = None
        self.sync_root_type = None
        self.sync_root_type_reason = None
        self.post_link_setup_flags = None
        self.linked = False
        self.link_error = False
        self.root_folder_file_count = None
        self.selected_file_count = None
        self.setup_link_callback = None
        self.setup_complete_callback = None
        self.on_link_success_callback = None


