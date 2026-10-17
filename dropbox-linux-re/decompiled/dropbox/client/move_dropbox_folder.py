# Source Generated with Decompyle++
# File: move_dropbox_folder.pyc (Python 3.11)

import enum
import errno
import os
import time
from typing import Callable, cast, ContextManager, Dict, List, Mapping, Optional, Text, Tuple, Union
from six import string_types
from build_number.features import feature_enabled
from dropbox import fsutil
from dropbox.client import unlink_cookie
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.client.constants import DEFAULT_DROPBOX_FOLDER_NAME, DEFAULT_DROPBOX_PATH
from dropbox.client.dropbox_folder_path import DropboxFolderPath
from dropbox.client.features.cloud_files_migration.helpers import is_nested_under_cloud_files_root
from dropbox.client.features.coauth.coauth_controller import CoauthController
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.file_system_support import is_supported_fs_type
from dropbox.client.gandalf import Gandalf
from dropbox.client.hidden_symlink import get_hidden_symlink, move_hidden_symlink
from dropbox.client.status.label import StatusLabel
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client.unlink_handlers import UnlinkReason
from dropbox.client.util import switch_sidebar_link
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.infinite import infinite_exposed, is_user_running_cloud_files
from dropbox.infinite.state_machine import InfiniteConfiguration
from dropbox.install_type import get_dropbox_install_type, InstallType
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.util import AnyPath, db_lower
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
from dropbox.sync_engine_boundary.file_system_constants import FILE_TYPE_DIRECTORY, FILE_TYPE_POSIX_SYMLINK, FILE_TYPE_REGULAR
from dropbox.sync_engine_boundary.file_system_exceptions import CannotMoveJunctionPointError, CannotMoveSymlinkError, FileExistsError, FileSystemError
from dropbox.sync_engine_boundary.types import FilesystemInfo
from dropbox.sync_root.gating import cloud_files_capable
from dropbox.sync_root.helpers import folder_conflicts_with_icloud
from dropbox.sync_root.interface import SyncRootManagerInterface
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class MoveErrorCode:
    UPLOADING_PHOTOS_ERROR = 1
    LOCATION_ERROR = 2
    UNEXPECTED_ERROR = 3
    USED_BY_OTHER_PROGRAM = 4
    COULD_NOT_MOVE_JUNCTION_POINT = 5
    FILE_EXISTS = 6
    COULD_NOT_MOVE_SYMLINK = 7
    UNRECOVERABLE_ERROR = 8
    CONFLICTS_WITH_BACKUP = 9
    CONFLICTS_WITH_ICLOUD_DRIVE = 10
    NUCLEUS_NOT_AVAILABLE = 11
    CONFLICTS_WITH_BACKUP_ANCHOR_TARGET_PATH = 12
    get_error_code_string = (lambda cls = None, error_code = None, error_args = classmethod: 