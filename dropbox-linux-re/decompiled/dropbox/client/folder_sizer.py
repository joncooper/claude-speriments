# Source Generated with Decompyle++
# File: folder_sizer.pyc (Python 3.11)

import errno
import os
import sys
import time
from typing import Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict
from dropbox.client.gandalf import Gandalf
from dropbox.client.user_folder_paths import UserFolderPaths
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fastwalk_bridge import fastwalk
from dropbox.gui import message_sender, spawn_thread_with_name
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_REGULAR
from dropbox.trace import TRACE
STORMCROW_FEATURE = 'desktop-folder-sizer'
STORMCROW_ALWAYS_VARIANT = 'ALWAYS'
STORMCROW_ONCE_VARIANT = 'ONCE'
CONFIG_KEY = 'folder_sizer_run_count'

def start_folder_sizer(account = None, config = None, gandalf = None):
    if not account.is_primary:
        return None
    if None:
        return None
# WARNING: Decompyle incomplete

_size_user_folders = (lambda : TRACE('Sizing User Folders')paths_dict = UserFolderPaths.create().paths_dict()for folder_key in paths_dict:
start_time = time.time()folder_path = paths_dict[folder_key]if not os.path.exists(folder_path):
TRACE("Skipping User Folder %s at path %s because it doesn't exist", folder_key, folder_path)continueif not os.path.isdir(folder_path):
TRACE('Skipping User Folder %s at path %s because it is not a directory', folder_key, folder_path)continueTRACE('Sizing User Folder %s at path %s', folder_key, folder_path)(size, count) = get_folder_stats(folder_path)duration = time.time() - start_timereport('folder-sizer', folder = str(folder_key), size = size, count = count, duration = duration)except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.FOLDER_OVERVIEW)continueTRACE('Done Sizing User Folders')None)()

def _on_error(path = None):
    exc_value = sys.exc_info()[1]
    if hasattr(exc_value, 'errno') and getattr(exc_value, 'errno') in (errno.EPERM, errno.ENOENT):
        severity = Severity.TRACE
    elif hasattr(exc_value.args[0], 'startswith') and exc_value.args[0].startswith('FindFirstFileExW(') and exc_value.args[0].endswith(', ..) --> 5'):
        severity = Severity.TRACE
    else:
        severity = Severity.WARN
    report_exception(severity = severity, component = DesktopComponent.FOLDER_OVERVIEW)


def get_folder_stats(path = None):
    size = 0
    count = 0
    for _, ents in fastwalk(path, on_explore_error = _on_error, no_atime = True):
        for dirent in ents:
            if dirent.type == FILE_TYPE_REGULAR:
                size += dirent.size
                count += 1
            return (size, count)

