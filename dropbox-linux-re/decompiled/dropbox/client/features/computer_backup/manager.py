# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

import os.path as os
import unicodedata
from datetime import datetime, timedelta
from functools import partial
from os import scandir
from os.path import isdir, islink
from typing import Callable, Dict, List, Optional, Text, Tuple, Union
from build_number.platform import IS_WINDOWS
from dropbox.callbacks import Handler
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_schedule import BackupSchedule as BackupScheduleResult, ScheduleDetail as ScheduleDetailResult, ScheduleType as ScheduleTypeResult
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.base_manager import BaseBackupManager
from dropbox.client.features.backup_common.constants import APPLE_DOUBLE_REGEX, CLOUD_DOCS_REGEX, DBXIGNORE_FILENAME, DEFAULT_IGNORED_GLOBS, NUCLEUS_UNSYNCED_FILENAMES_REGEX
from dropbox.client.features.backup_common.scheduling import BackupSchedule, ScheduleType
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_accounts
from dropbox.client.features.backup_common.utils import _Status
from dropbox.client.features.computer_backup.computer_backup_logging import ComputerBackupLogger
from dropbox.client.features.computer_backup.computer_backup_state import ComputerBackupState, ComputerBackupStatus, KnownCBFolder
from dropbox.client.features.computer_backup.config_utils import cb_is_active_account
from dropbox.client.features.computer_backup.constants import CB_ANCHOR_INVARIANT_CHECK_INTERVAL_DEFAULT, CB_CUSTOM_FOLDER_NAME, CB_IC_WAIT_AFTER_INITIAL_SETUP_SEC, CB_USAGE_REPORT_INTERVAL_HOURS_DEFAULT, CBFolderId, ComputerBackupUsage, PROGRAM_FILES_FOLDER_NAMES_MAP_WINDOWS
from dropbox.client.features.computer_backup.controller import ComputerBackupController
from dropbox.client.features.computer_backup.errors import RequestAssertion, RequestFailedException
from dropbox.client.features.computer_backup.event_reporter import ComputerBackupEventReporter, ManagerBoundaryEventReporter, OperationEventReporter
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.computer_backup.nav_service import show_custom_folders_selector
from dropbox.client.features.computer_backup.operations import EnableBackupSanityCheckOperation
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.computer_backup.utils import FolderNucleusStats, get_dropbox_usage, get_folder_nucleus_stats, get_nucleus_local_file_count, get_nucleus_local_online_size, get_nucleus_local_physical_size, get_nucleus_remote_size, get_os_folder_path, get_third_party_providers_nopii_from_folder_list, read_dbx_ignore_contents
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event_label import ComputerBackupEventLabel
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_fetch_sub_folders_error_types import ComputerBackupFetchSubFoldersErrorTypes
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_fetch_sub_folders_result import ComputerBackupFetchSubFoldersResult
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_get_dbx_ignore_contents_result import ComputerBackupGetDbxIgnoreContentsResult
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_sub_folder_info import ComputerBackupSubFolderInfo
from dropbox.client.features.external_drive_backup.edb_in_memory_tracker import EDBInMemoryTracker
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.utils import list_anchors_for_se_accounts
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.constants import ADMIN_POLICY_REFRESH_DELAY_SEC, CustomFolderRequest, FIFTEEN_MINUTES_AS_SECONDS, FolderIgnorePaths, KnownFolderRequest
from dropbox.client.features.sync_everything.gating import get_known_folders
from dropbox.client.features.sync_everything.nav_service import show_backup_app, show_backup_restorations_onboarding, show_backup_sku_modal, show_sync_everything_onboarding, show_sync_everything_preferences
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.api_utils import list_backups
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger, SyncEverythingUnlinkType
from dropbox.client.features.sync_everything.v3.utils import FolderUpdateCallback, FolderUpdateHandler, is_offline, wait_for_fully_synced
from dropbox.client.features.sync_everything.v3.ux_param_utils import get_backups_dict, get_roles_dict, translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.constants import ACTION_SURFACE_MAP
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult, OperationResultData
from dropbox.client.multiaccount.constants import Role
from dropbox.client.multiaccount.role import Roles
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.client_api.exceptions import HTTP401Error, HTTP429Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context import ContextInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.i18n import get_system_languages
from dropbox.shared.util import safe_navigate
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.types import DeviceAnchorInfo, DeviceAnchorState, DropboxFolderDiskInfo
if IS_WINDOWS:
    from winffi.kernel32.api import FILE_ATTRIBUTE_HIDDEN, FILE_ATTRIBUTE_SYSTEM, GetFileAttributesW
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
_UpdateAction = Callable[([], OperationResult)]

def ComputerBackupManager():
    '''ComputerBackupManager'''
    pass
# WARNING: Decompyle incomplete

ComputerBackupManager = <NODE:27>(ComputerBackupManager, 'ComputerBackupManager', BaseBackupManager[ComputerBackupController])
