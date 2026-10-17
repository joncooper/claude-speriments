# Source Generated with Decompyle++
# File: sync_everything_manager_view_model.pyc (Python 3.11)

import json
import os
from datetime import datetime, timezone
from typing import Callable, cast, Dict, List, Optional, Text
from build_number.platform import IS_MAC
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.computer_backup.computer_backup_state import KnownCBFolder
from dropbox.client.features.computer_backup.constants import CBFolderId
from dropbox.client.features.computer_backup.device_state_vm import DeviceStateVM
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_fetch_sub_folders_result import ComputerBackupFetchSubFoldersResult
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_get_dbx_ignore_contents_result import ComputerBackupGetDbxIgnoreContentsResult
from dropbox.client.features.sync_everything.constants import DeviceStatus, FolderIgnorePaths, ONE_MONTH_AS_SECONDS, STRING_TO_ROLE, TWO_WEEKS_AS_SECONDS
from dropbox.client.features.sync_everything.gating import ActpaSyncEverythingPlusTrial, SyncEverythingFeature, SyncEverythingOnboardingFeature
from dropbox.client.features.sync_everything.nav_service import show_backup_unlimited_storage_modal
from dropbox.client.features.sync_everything.v3.api_utils import get_plan_name, list_backups, next_available_name
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function
from dropbox.client.features.sync_everything.v3.delay_injection import DebugDelayManager, DelayPoint
from dropbox.client.features.sync_everything.v3.device_state import KnownFolder
from dropbox.client.features.sync_everything.v3.event_reporter import PerformanceEventReporter
from dropbox.client.features.sync_everything.v3.fs_utils import calculate_single_folder_size, fast_over_quota_check, live_updating_folder_metadata
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.v3.url_utils import open_backup_all_on_web, open_client_route_on_server_by_device_name
from dropbox.client.features.sync_everything.v3.utils import context_from_models, context_from_models_account_id, convert_third_party_providers_to_in_use_providers, get_third_party_providers, open_finder_or_explorer_os_folder
from dropbox.client.features.sync_everything.v3.ux_param_utils import get_allowed_roles, get_device_id, get_stormcrow_values, translate_role
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_unlimited_storage_modal_actions import BackupUnlimitedStorageModalActions
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_folder_metadata import FolderMetadataBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_sync_everything_manager_view_model import ActionSurface, ProductLoggingEvent, Source, SyncEverythingManagerViewModelBridgeInterface
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_state import DeviceState as DeviceStateBIDL
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.eligible_roles import EligibleRoles
from dropbox.client.features.sync_everything.view_model.bridge_gen.in_use_provider import InUseProvider
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_status import RedirectStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.stormcrow_values import StormcrowValues
from dropbox.client.features.sync_everything.view_model.constants import ACTION_SURFACE_MAP, KNOWN_FOLDER_NAME_MAP, LOGGING_EVENT_MAP, SOURCE_MAP
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.client.features.users.bridge_gen.user_info import UserInfo
from dropbox.client.features.users.model.users_wrapper import UserCacheWrapper
from dropbox.client.features.users.view_model.users_vm import convert_user
from dropbox.client.features.web_viewer.model.desktop_login_wrapper import DesktopLoginWrapper
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.platform import IS_MAC
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
if IS_MAC:
    from dropbox.mac.system_preferences import open_full_disk_access_preferences, open_icloud_preferences

def _ignore_retry_ic(status = None):
    if status.redirect_status_code == RedirectRequestStatus.RETRY_IC:
        return ResolvedFuture(RedirectStatus(RedirectRequestStatus.OK))
    return ResolvedFuture(status)


class SyncEverythingManagerViewModel(SyncEverythingManagerViewModelBridgeInterface, Actor):
    pass
# WARNING: Decompyle incomplete

