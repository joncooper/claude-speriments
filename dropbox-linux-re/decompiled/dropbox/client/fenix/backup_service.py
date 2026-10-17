# Source Generated with Decompyle++
# File: backup_service.pyc (Python 3.11)

import typing
import uuid
from typing import Optional, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper, DeviceStateWithStatus
from dropbox.client.features.computer_backup.device_state_vm import DeviceStateVM
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventAction, EventClass, EventObject, EventState
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.features.external_drive_backup.types import SeparatedAnchorsByEngineAndState
from dropbox.client.features.external_drive_backup.utils import list_anchors_by_uuid_both_engines
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.sync_everything.constants import DeviceStatus
from dropbox.client.features.sync_everything.v3.fs_utils import get_sync_everything_path
from dropbox.client.features.sync_everything.v3.sync_everything_manager import SyncEverythingManager
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_app_params import BackupAppParams
from dropbox.client.features.sync_everything.view_model.bridge_gen.bridge_interface_sync_everything_manager_view_model import Source
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.sync_everything_manager_view_model import SyncEverythingManagerViewModel
from dropbox.client.fenix.utils import get_user_context_from_account_id
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.futures import Future
from dropbox.foundation.futures.basic import ResolvedFuture
from dropbox.foundation.futures.sleep import sleep_async
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2 import destroying
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.types import DeviceAnchorState
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
COMPUTER_BACKUP_STATUS_CHECK_TIMEOUT = 1

class BackupService(Actor):
    pass
# WARNING: Decompyle incomplete

