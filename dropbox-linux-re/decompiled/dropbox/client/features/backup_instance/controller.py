# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import os
from os.path import exists
from typing import Any, cast, Optional, Text, TYPE_CHECKING
from dropbox import fsutil
from dropbox.client.authentication.account import Account
from dropbox.client.features.backup_common.backup_logging import BackupLogger
from dropbox.client.features.backup_instance.backup_instance_logging import BackupInstanceLogger
from dropbox.client.features.backup_instance.backup_root_description import BackupRootDescription, BackupRootDescriptionNS
from dropbox.client.features.backup_instance.constants import ACCEPTABLE_NEW_INSTANCE_VALIDATION_RESULTS, BACKUP_INSTANCE_SHUTDOWN_PAUSE_TIME_SEC, BI_SYNC_FOLDER
from dropbox.client.features.backup_instance.event_reporter import OperationEventReporter
from dropbox.client.features.backup_instance.nucleus_local_config import _MemoryLocalConfig
from dropbox.client.features.backup_instance.types import BackupInstance, BackupInstanceEvent, RootValidationError, RootValidationResult
from dropbox.client.features.backup_instance.utils import apply_time_machine_ignore_xattr_if_missing, BI_TRACE, build_sync_engine_boundary_threadpool, compute_new_local_backup_root_location, validate_root_path, wipe_nucleus_db
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import Destroyable
from dropbox.foundation.raii2.arc import Arc
from dropbox.fsutil import FileSystem
from dropbox.nucleus.migration_constants import NucleusMigrationArgs, SyncEngineState
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine.nucleus.classic_client.sync_engine import NucleusClassicClient
from dropbox.sync_engine_boundary.monitored_thread_pool import MonitoredThreadPoolExecutor
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.utils import backup_mode_args_to_engine_generation
from dropbox.sync_root.interface import SyncRootType
if TYPE_CHECKING:
    from dropbox.client.main import DropboxApplication
if TYPE_CHECKING:
    _NucleusParentType = NucleusInterface
else:
    _NucleusParentType = object

class _NucleusInstanceWrapper(_NucleusParentType, Destroyable):
    pass
# WARNING: Decompyle incomplete


class _AccountWrapper(_AccountParentType):
    pass
# WARNING: Decompyle incomplete


class BackupInstanceController(Destroyable):
    pass
# WARNING: Decompyle incomplete

