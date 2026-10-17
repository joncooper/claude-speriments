# Source Generated with Decompyle++
# File: view_model.pyc (Python 3.11)

import json
from typing import Any, Dict, List, Optional, Tuple
from dropbox.client.authentication.account import Account
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_schedule import BackupSchedule
from dropbox.client.features.backup_app.view_model.bridge_gen.bridge_interface_backup_app_view_model import BackupAppViewModelBridgeInterface
from dropbox.client.features.backup_app.view_model.bridge_gen.device_backup_info import DeviceBackupInfo
from dropbox.client.features.backup_app.view_model.bridge_gen.external_drive_backup_info import ExternalDriveBackupInfo
from dropbox.client.features.backup_app.view_model.bridge_gen.team_features import TeamFeatures
from dropbox.client.features.backup_app.view_model.utils import _drive_info_to_drive_backup_info, both_engine_result_to_drive_backup_info_list, device_state_to_device_backup_info, get_bandwidth_tab, get_newly_added_external_drive_backup, get_platform_type, get_team_account_and_user_context, get_user_context_from_role, list_backups_result_to_device_backup_list, list_drive_backups_result_to_drive_backup_list, redirect_status_to_backup_status_code, strip_apiv2_id_prefix
from dropbox.client.features.backup_common.cb_progress_tracker import CBProgressTracker
from dropbox.client.features.backup_common.scheduling import BackupScheduler
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper, DeviceStateWithStatus
from dropbox.client.features.external_drive_backup.api_utils import get_eligibility_info, list_backups as list_drive_backups
from dropbox.client.features.external_drive_backup.edb_in_memory_tracker import EDBInMemoryTracker
from dropbox.client.features.external_drive_backup.edb_progress_tracker import EDBProgressTracker
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventReporter
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.trace import EDB_TRACE
from dropbox.client.features.external_drive_backup.utils import list_anchors_by_uuid_both_engines
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_sync_progress import EdbSyncProgress
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.external_drive_backup.view_model.external_drive_backup_view_model import ExternalBackupManager
from dropbox.client.features.sync_everything.v3.api_utils import list_backups
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingLogger
from dropbox.client.features.sync_everything.v3.url_utils import open_account_plan_on_server, open_backup_on_web_by_name
from dropbox.client.features.sync_everything.v3.utils import open_finder_or_explorer_by_fileid
from dropbox.client.features.sync_everything.v3.ux_param_utils import translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.cb_sync_progress import CbSyncProgress
from dropbox.client.features.sync_everything.view_model.bridge_gen.product_logging_event import ProductLoggingEvent
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.constants import ACTION_SURFACE_MAP, LOGGING_EVENT_MAP, SOURCE_MAP
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.client.features.users.bridge_gen.user_info import UserInfo
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.features.users.view_model.users_vm import convert_user
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.signals import Signal
from dropbox.model.types import FileId
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.trace import TRACE
BROWSE_CLIENT_ROUTE = 'browse'
REWIND_CLIENT_ROUTE = 'rewind'

def BACKUP_APP_VIEW_MODEL_TRACE(fmt = None, session_id = None, *args):
    real_fmt = '[BACKUP-APP-VIEW-MODEL][{}] {}'.format(session_id if session_id else '', fmt)
# WARNING: Decompyle incomplete


class BackupAppViewModel(Actor, BackupAppViewModelBridgeInterface):
    pass
# WARNING: Decompyle incomplete

