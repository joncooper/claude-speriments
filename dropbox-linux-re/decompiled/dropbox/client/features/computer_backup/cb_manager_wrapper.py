# Source Generated with Decompyle++
# File: cb_manager_wrapper.pyc (Python 3.11)

import os
import time
from typing import Any, Callable, Dict, List, NamedTuple, Optional, Text, Tuple, TypeVar, Union
from dropbox.api.v2.datatypes.device_sync import PingServerArg
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_schedule import BackupSchedule as BackupScheduleResult
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_common.config_utils import is_se_migration_active
from dropbox.client.features.backup_common.errors import report_exception_and_ignore
from dropbox.client.features.backup_common.scheduling import BackupSchedule
from dropbox.client.features.backup_common.ui_utils import BackupImplementationUISwitcher
from dropbox.client.features.computer_backup.cb_migration_manager import CBMigrationManager
from dropbox.client.features.computer_backup.computer_backup_logging import ComputerBackupLogger
from dropbox.client.features.computer_backup.computer_backup_state import ComputerBackupState, KnownCBFolder
from dropbox.client.features.computer_backup.constants import BackupStatus, CBFolderId, ComputerBackupStatus
from dropbox.client.features.computer_backup.device_state_vm import DeviceStateVM
from dropbox.client.features.computer_backup.event_reporter import OperationEventReporter
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature, ComputerBackupOnboardingFeature
from dropbox.client.features.computer_backup.manager import ComputerBackupManager
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_fetch_sub_folders_result import ComputerBackupFetchSubFoldersResult
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_get_dbx_ignore_contents_result import ComputerBackupGetDbxIgnoreContentsResult
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_suppression_reason import ComputerBackupSuppressionReason
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.constants import CustomFolderRequest, DeviceStatus, FolderIgnorePaths, KnownFolderRequest, REMOTE_ACCOUNT_DELETE_TIMEOUT
from dropbox.client.features.sync_everything.gating import SyncEverythingOnboardingFeature
from dropbox.client.features.sync_everything.v3.api_utils import list_backups
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function
from dropbox.client.features.sync_everything.v3.config_utils import se_is_active_account
from dropbox.client.features.sync_everything.v3.device_state import DeviceState, KnownFolder
from dropbox.client.features.sync_everything.v3.errors import RequestFailedException
from dropbox.client.features.sync_everything.v3.os_folder_state import FolderLocationType, OSFolderInterface, OSFolderState
from dropbox.client.features.sync_everything.v3.sync_everything_manager import SyncEverythingManager, SyncEverythingUnlinkType
from dropbox.client.features.sync_everything.v3.utils import FolderUpdateCallback
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.client.multiaccount.constants import Role
from dropbox.client_api.apiv2.generated import device_sync
from dropbox.client_api.connection.interface import HostKeyAuth
from dropbox.client_api.exceptions import HTTP401Error, TransientNetworkError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context import ContextInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
ManagerArcType = Union[(Arc[ComputerBackupManager], Arc[SyncEverythingManager])]
ManagerType = Union[(ComputerBackupManager, SyncEverythingManager)]
_T = TypeVar('_T')

def with_wrapper_ready(func = None):
    pass
# WARNING: Decompyle incomplete


class DeviceStateWithStatus(NamedTuple):
    display_name: 'Optional[Text]' = 'DeviceStateWithStatus'


class ComputerBackupManagerWrapper(SingletonActor):
    pass
# WARNING: Decompyle incomplete

