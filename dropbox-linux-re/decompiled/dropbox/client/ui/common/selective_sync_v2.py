# Source Generated with Decompyle++
# File: selective_sync_v2.pyc (Python 3.11)

import os
import threading
from abc import ABCMeta, abstractmethod
from concurrent.futures import Future
from enum import Enum
from hashlib import md5
from typing import Any, Callable, Dict, FrozenSet, Generic, Iterable, List, Optional, Text, Tuple, TypeVar
from mypy_extensions import TypedDict
from six import add_metaclass, iteritems, itervalues
from six.moves.urllib import parse as urlparse
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.client.multiaccount.role import Roles
from dropbox.client.product_span import ProductSpan
from dropbox.client.scalability.scale_mitigation import ScaleLimitReason, ScaleMitigationUserInfo
from dropbox.client.selective_sync_size.folder_size_util import convert_to_normalized_ns_server_path, get_path_sizes_map, is_selsync_folder_size_enabled
from dropbox.client.status.label import StatusLabel
from dropbox.client.ui.common.dropbox_menu import MenuItem
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.gui import event_handler, message_sender, spawn_thread_with_name
from dropbox.i18n import format_number, ungettext
from dropbox.infinite import infinite_exposed
from dropbox.model.types import FileId
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.shared.server_path import MRCasedServerPath, RRCasedServerPath, RRLowerServerPath, RRUnknownCaseServerPath
from dropbox.shared.util import db_lower
from dropbox.sync_engine_boundary.exceptions import InvalidLocalPathError, NamespaceNotMountedError
from dropbox.sync_engine_boundary.selective_sync_by_path_interface import FileIdRRServerPaths
from dropbox.sync_engine_boundary.selsync import FileIdSet, SelectiveSyncSet
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.threading import Lock
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
ADMIN_DEFAULTS_FIXED = False
_K = TypeVar('_K')
_V = TypeVar('_V')

class TSSNoSyncChildrenPartialFailure(Exception):
    pass
# WARNING: Decompyle incomplete


def CachedFetcher():
    '''CachedFetcher'''
    
    def __init__(self = None, function = None):
        self._cache = { }
        self._lock = Lock()
        self.function = function

    
    def load(self = None, key = None):
        TRACE('loading %r', key)
        new = None
        self._lock
        future = self._cache.get(key, None)
    # WARNING: Decompyle incomplete


CachedFetcher = <NODE:27>(CachedFetcher, 'CachedFetcher', Generic[(_K, _V)])

class SelectiveSyncStrings(UIStrings):
    prefs_working_button = UI('Updating...')
    window_title = UI('Selective Sync')
    info = UI("Unselected folders won't appear on this computer.")
    ignored_folder_size_info_header = UI('%(size)s unselected.')
    window_ok_button = UI('Update')
    cancel_button = UI('Cancel')
    confirmation_caption = UI('Update Selective Sync settings?')
    confirmation_message_ignore_only = UI("Unselected folders will be removed from this computer's Dropbox. They will still be available on the web and other devices.")
    confirmation_message_ignore_and_unignore = UI('Dropbox on this computer will be updated with your changes.')
    confirmation_message_ignore_and_unignore_infinite = UI("Unselected folders will be removed from this computer's Dropbox. Any folders you just selected will be online-only.")
    nested_selsync_warning_title = UI('Some folders under "%(folder_name)s" aren\'t selected, so they won\'t appear on this computer')
    nested_selsync_warning_title_multiple = UI("Folders you chose have subfolders that aren't selected and won't appear on this computer")
    nested_selsync_warning_body = UI('Select any subfolders you want to appear on this computer.')
    confirmation_ok_button = UI('Update')
    really_bad_error_caption = UI('Unable to update')
    really_bad_error_message = UI('Dropbox was unable to update your selective sync preferences.')
    really_bad_error_button = UI('OK')
    really_bad_learn_more_button = UI('Learn More')
    context_menu_open_folder = UI('Open Folder')
    context_menu_browse_on_website = UI('View on Dropbox.com...')
    selsync_listing = UI('Loading your folders...')
    info_infinite = UI("Unselected folders won't appear on this computer.")
    select_all = UI('Select all')
    network_error_message = UI('Unable to connect')
    too_many_files_warning = (lambda number_of_files = None, threshold = None: ungettext('Your account has %(number_of_files)s file. If you sync more than %(threshold)s files, syncing will take a while.', 'Your account has %(number_of_files)s files. If you sync more than %(threshold)s files, syncing will take a while.', number_of_files) % dict(number_of_files = format_number(number_of_files), threshold = format_number(threshold)))()
    scale_continue_warning_title = (lambda num = None: ungettext('Continue syncing %(number_of_files)s file?', 'Continue syncing %(number_of_files)s files?', num) % dict(number_of_files = format_number(num)))()
    scale_continue_warning_body = UI("Syncing will take a long time because you've selected more than %(threshold)s files. We recommend selecting fewer folders.")
    scale_continue_warning_cancel = UI('Cancel')
    scale_continue_warning_continue = UI('Continue anyway')
    prefs_group_title_sync_tab = UI('Selective sync')
    prefs_group_label_sync_tab = UI('')
    prefs_group_description_sync_tab = UI("Hide folders you don't want to see on this PC. Hidden folders will be available on dropbox.com", mac = UI("Hide folders you don't want to see on this Mac. Hidden folders will be available on dropbox.com"))
    ss_removal_mitigation_prefs_group_title_sync_tab = UI('Select folders to sync to this Mac')
    prefs_change_label_sync_tab = UI('Select folders')

selsync_strings = SelectiveSyncStrings
SELSYNC_ERROR_HELP_URL = 'https://www.dropbox.com/help/9149'

def log_selsync_user_action(account = None, action = None, extra = None):
