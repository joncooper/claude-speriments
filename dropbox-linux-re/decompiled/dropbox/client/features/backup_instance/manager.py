# Source Generated with Decompyle++
# File: manager.pyc (Python 3.11)

from typing import Dict, List, Optional, TYPE_CHECKING
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_auto_selsync.bi_auto_selsync_manager import BackupAutoSelSyncManager
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.backup_instance.backup_instance_logging import BackupInstanceLogger
from dropbox.client.features.backup_instance.backup_root_description import BackupRootDescription, BackupRootDescriptionNS
from dropbox.client.features.backup_instance.constants import BACKUP_INSTANCE_AUTO_RELINK_INTERVAL_DEFAULT, BackupInstanceStrings
from dropbox.client.features.backup_instance.controller import BackupInstanceController
from dropbox.client.features.backup_instance.event_reporter import OperationEventReporter
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.server_interface import ServerInterface
from dropbox.client.features.backup_instance.types import BackupInstance, BackupInstanceEvent, RootValidationError
from dropbox.client.features.backup_instance.ui_manager import BackupInstanceUIManager
from dropbox.client.features.backup_instance.utils import BI_TRACE, BI_WARN, has_local_bkup_root_parent
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.legacy_ui_launcher import LegacyUILauncher
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.async_tools import assert_on_actor_thread, async_queued_local_function, future_function
from dropbox.client.features.sync_everything.v3.fs_utils import relative_path_depth
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager import AccountUpdate, AccountUpdateType
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import EasyFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
if TYPE_CHECKING:
    from dropbox.client.main import DropboxApplication

class BackupInstanceManager(SingletonActor):
    pass
# WARNING: Decompyle incomplete

