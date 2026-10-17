# Source Generated with Decompyle++
# File: cb_progress_tracker.pyc (Python 3.11)

from typing import Any, Callable, Dict, Optional
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.computer_backup.event_reporter import OperationEventSession as ComputerBackupOperationEventSession
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.home_feed.shared.util.signals import RepeatedEventSignalWithPayload
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.errors import convert_to_failure
from dropbox.client.features.sync_everything.v3.event_reporter import OperationEventSession as SyncEverythingOperationEventSession
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent, SyncEverythingLogger
from dropbox.client.features.sync_everything.view_model.bridge_gen.cb_sync_progress import CbSyncProgress
from dropbox.client.features.sync_everything.view_model.bridge_gen.cb_sync_status import CbSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import Severity
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.signals import Signal
from dropbox.model.types import FileId
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types.backup_sync_progress import ActiveIndexingState, ActiveSyncState, DoneState, SyncProgressForComputerBackup, SyncProgressForComputerBackupSummary
from dropbox.threading import Lock
from dropbox.trace import TRACE

def CB_PROGRESS_TRACKER_TRACE(fmt = None, session_id = None, *args):
    pass
# WARNING: Decompyle incomplete


class CBProgressTracker(UserSingleton):
    pass
# WARNING: Decompyle incomplete

