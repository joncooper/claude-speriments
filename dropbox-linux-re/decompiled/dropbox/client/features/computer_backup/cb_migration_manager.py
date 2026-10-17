# Source Generated with Decompyle++
# File: cb_migration_manager.pyc (Python 3.11)

from typing import List, Optional, Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import EventReporter, random_session_id
from dropbox.client.features.computer_backup.cb_migration_state import CBMigrationState, ComputerBackupMigrationState
from dropbox.client.features.computer_backup.gating import ComputerBackupFeature
from dropbox.client.features.computer_backup.migration_config import CBMigrationConfig
from dropbox.client.features.computer_backup.trace import CB_TRACE
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function
from dropbox.client.features.sync_everything.v3.device_state import DeviceState
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.threading import Lock

class CBMigrationManager(SingletonActor):
    pass
# WARNING: Decompyle incomplete

