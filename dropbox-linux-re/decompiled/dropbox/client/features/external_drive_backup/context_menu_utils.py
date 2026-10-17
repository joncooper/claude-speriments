# Source Generated with Decompyle++
# File: context_menu_utils.pyc (Python 3.11)

from typing import Text
from build_number.platform import IS_WINDOWS
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.errors import convert_to_failure
from dropbox.client.features.external_drive_backup.event_reporter import OperationEventSession
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future
from dropbox.foundation.raii2 import destroying
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.device_anchor_interface import DeviceAnchorError
if IS_WINDOWS:
    from dropbox.client.features.external_drive_backup.disk_arbitration.windows import build_drive_info
pause_edb_backup = (lambda user_context = None, session_id = None, local_path = future_function: pass# WARNING: Decompyle incomplete
)()
resume_edb_backup = (lambda user_context = None, session_id = None, local_path = future_function: pass# WARNING: Decompyle incomplete
)()
