# Source Generated with Decompyle++
# File: auto_selsync_manager.pyc (Python 3.11)

import uuid
from typing import List, Set
from dropbox.api.v2.datatypes.external_drive_backup import ExternalDriveBackupStateEnum, ListBackupsResult as ListDriveBackupsResult
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.apollo_alerts.model.apollo_alerts import AlertResult, ApolloAlerts
from dropbox.client.features.backup_auto_selsync.auto_selsync_result import BackupAutoSelSyncResult, BackupAutoSelSyncResultCode
from dropbox.client.features.backup_auto_selsync.constants import AUTO_SEL_SYNC_INVARIANT_INTERVAL_DEFAULT, AutoSelSyncUIStrings
from dropbox.client.features.backup_auto_selsync.event_reporter import OperationEventReporter
from dropbox.client.features.backup_auto_selsync.gating import BackupAutoSelSyncFeature
from dropbox.client.features.backup_auto_selsync.logging import AutoSelSyncLogger
from dropbox.client.features.backup_auto_selsync.types import BackupAutoSelSyncEvent
from dropbox.client.features.backup_common.base_event_reporter import LifetimeReporter, random_session_id
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.external_drive_backup.server_interface import catch_and_convert_network_exceptions, ServerInterface
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function
from dropbox.client.features.sync_everything.v3.server_interface import catch_and_convert_network_exceptions_list_backups, ServerInterface as DeviceServerInterface
from dropbox.client.features.sync_everything.v3.url_utils import open_backup_all_on_web
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.types.ids import FileID
from dropbox.model.types import FileId
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types import DeviceAnchorTargetType, ListDeviceAnchorsResult

class AutoSelSyncManager(SingletonActor):
    pass
# WARNING: Decompyle incomplete

