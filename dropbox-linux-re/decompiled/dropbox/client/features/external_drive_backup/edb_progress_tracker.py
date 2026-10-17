# Source Generated with Decompyle++
# File: edb_progress_tracker.pyc (Python 3.11)

from typing import Any, Dict, Optional
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.errors import convert_to_failure
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventSession
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.device_anchor_state import DeviceAnchorState as DeviceAnchorStateBidl
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_sync_progress import EdbSyncProgress
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_sync_status import EdbSyncStatus
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.home_feed.shared.util.signals import RepeatedEventSignalWithPayload
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import Severity
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.signals import Signal
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.types.backup_sync_progress import ActiveIndexingState, ActiveSyncState, DeviceAnchorState, DoneState, SyncProgressForDeviceAnchor, SyncProgressForDeviceAnchorSummary
from dropbox.threading import Lock
from dropbox.trace import TRACE

def EDB_PROGRESS_TRACKER_TRACE(fmt = None, session_id = None, *args):
    pass
# WARNING: Decompyle incomplete


class EDBProgressTracker(UserSingleton):
    pass
# WARNING: Decompyle incomplete

