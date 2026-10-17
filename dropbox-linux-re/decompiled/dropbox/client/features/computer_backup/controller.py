# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

from datetime import datetime, timezone
from typing import Callable, cast, Dict, List, Optional, Set, Text, Tuple, Union
from build_number import IS_MAC
from dropbox import fsutil
from dropbox.api.v2.datatypes.device_sync import BackupInfo, ComputerBackupFolder, ComputerBackupFolderState, ComputerBackupState as ServerComputerBackupState, DeviceSyncStatus, EmailType, ListBackupsResult
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, random_session_id
from dropbox.client.features.backup_common.cb_progress_tracker import CBProgressTracker
from dropbox.client.features.backup_common.errors import report_exception_and_ignore
from dropbox.client.features.backup_common.logging_helpers import convert_folder_id_to_nopii_name, convert_folder_id_to_nopii_value
from dropbox.client.features.backup_common.metric_sampler import MetricSampler
from dropbox.client.features.backup_common.scheduling import BackupSchedule, BackupScheduler, ScheduleType
from dropbox.client.features.backup_common.ui_utils import get_sync_everything_preferences_accounts
from dropbox.client.features.backup_instance.backup_root_description import BackupRootDescription
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.manager import BackupInstanceManager
from dropbox.client.features.backup_instance.types import DestroyableNucleus
from dropbox.client.features.computer_backup.computer_backup_logging import ComputerBackupLogger
from dropbox.client.features.computer_backup.computer_backup_state import ComputerBackupState, ComputerBackupStatus, KnownCBFolder
from dropbox.client.features.computer_backup.constants import BackupStatus, CB_REBIND_WAIT_AFTER_INITIAL_SETUP_SEC, CB_SYNC_PROGRESS_SERVER_CALL_QUIET_PERIOD_SEC, CBFolderId, CbHiveAnchorState, ComputerBackupFolderStatus, ComputerBackupUIStrings, UpdateAnchorInfoData
from dropbox.client.features.computer_backup.errors import RequestAssertion
from dropbox.client.features.computer_backup.event_reporter import OperationEventReporter
from dropbox.client.features.computer_backup.fully_synced_tracker import FirstSyncLoggingData, FullySyncedTracker
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.computer_backup.ic_disable_backup_backoff import ICDisableBackupBackoffController
from dropbox.client.features.computer_backup.nav_service import show_custom_folders_selector
from dropbox.client.features.computer_backup.operations import ClearAllQuotaExemptOperation, DisableOperation, MarkQuotaExemptOperation, Operation, PauseOperation, RenameOperation, RestoreOperation, ResumeOperation, UpdateOperation
from dropbox.client.features.computer_backup.server_interface import catch_and_convert_network_exceptions, os_folder_id_from_api, ServerInterface
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.computer_backup.utils import backup_info_to_bidl, find_enabled_backup_on_server, get_os_folder_path, local_anchor_exist
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event_label import ComputerBackupEventLabel
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.constants import CustomFolderRequest, FolderIgnorePaths, KnownFolderRequest
from dropbox.client.features.sync_everything.nav_service import show_backup_app
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function, future_sequence, FutureGenerator
from dropbox.client.features.sync_everything.v3.sync_everything_manager import _return_ok_op
from dropbox.client.features.sync_everything.v3.utils import _is_paused, is_offline
from dropbox.client.features.sync_everything.v3.ux_param_utils import get_roles_dict, translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.anchor_folder import AnchorFolder
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo as BIDLBackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.cb_sync_progress import CbSyncProgress, CbSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.deep_link_action import DeepLinkAction
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus as BIDLDeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.platform_type import PlatformType
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.constants import DEEP_LINK_ACTIONS_MAP
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.client.ui.common.uikit import BaseUIKit
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.navigation_service import NavigationServiceInterface
from dropbox.foundation.navigation_service.interface import ViewHandle
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import SignalConnection
from dropbox.foundation.types.ids import FileID
from dropbox.model.types import FileId
from dropbox.proto.nucleus.device_anchor_pb2 import BreakBackupReason
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, DeviceAnchorInfo, DeviceAnchorState, DeviceAnchorTargetType, DeviceAnchorUnbindInfo, DeviceAnchorUnbindReason, ErredDeviceAnchorInfo, HangReason, ListDeviceAnchorsResult, OneWaySyncRemediationInfo
from dropbox.threading import Lock
ShowCFSCallback = Callable[([
    UserContext,
    str,
    Optional[ActionSurface],
    Source,
    BIDLBackupInfo,
    Dict[(Text, List[Text])],
    Optional[int],
    Optional[Dict[(Text, bool)]],
    Optional[str],
    Optional[List[str]],
    Optional[bool]], Future[Optional[ViewHandle]])]

class ComputerBackupConfig:
    
    def __init__(self = None, account = None, machine_config = None):
        self._account = account
        self._account_id = account.account_id
        self._machine_config = machine_config
        self._on_state_change()

    
    def _on_state_change(self = None):
        current_state = self.current_state()
        if current_state.status != ComputerBackupStatus.DISABLED:
            ComputerBackupFeature.add_to_force_allowed(self._account)
            if (lambda .0: pass# WARNING: Decompyle incomplete
)(current_state.folders.items()()):
                ComputerBackupFeature.add_to_custom_folders_force_allowed(self._account)
                return None
            return any

    
    def current_state(self = None):
        current_state = self._machine_config.computer_backup_device_state
        current_account_id = self._machine_config.computer_backup_active_account_id
        if current_account_id and current_state or current_account_id != self._account_id:
            return ComputerBackupState(status = ComputerBackupStatus.DISABLED)

    
    def finish_update(self = None, new_state = None, account = None):
        if new_state.status == ComputerBackupStatus.DISABLED:
            self._machine_config.computer_backup_active_account_id = None
        elif account:
            self._machine_config.computer_backup_active_account_id = account.account_id
        self._machine_config.computer_backup_device_state = new_state
        self._on_state_change()



class ComputerBackupController(SingletonActor):
    pass
# WARNING: Decompyle incomplete

