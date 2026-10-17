# Source Generated with Decompyle++
# File: external_drive_backup_view_model.pyc (Python 3.11)

from typing import Dict, List, Optional
from dropbox.client.features.external_drive_backup.external_backup_logging import ExternalBackupLogger
from dropbox.client.features.external_drive_backup.gating import ExternalDriveBackupFeature
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.client.features.external_drive_backup.trace import EDB_WARN
from dropbox.client.features.external_drive_backup.utils import fetch_subfolders, get_account_subscription_type, is_overquota, is_overquota_upsell, read_dbx_ignore_contents
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.bridge_interface_external_drive_backup_manager_view_model import ExternalDriveBackupManagerViewModelBridgeInterface, FetchSubFoldersResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.drive_info import DriveInfo
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_action_surface import EdbActionSurface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_stormcrow_values import EdbStormcrowValues
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.get_dbx_ignore_contents_result import GetDbxIgnoreContentsResult
from dropbox.client.features.sync_everything.v3.utils import context_from_models, open_finder_or_explorer_home_ns_role
from dropbox.client.features.users.bridge_gen.role import Role as BIDLRole
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.bridge_gen.bridge_interface_user_context import UserContextBridgeInterface
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.model.types import FileId

class ExternalDriveBackupManagerViewModel(ExternalDriveBackupManagerViewModelBridgeInterface, Actor):
    pass
# WARNING: Decompyle incomplete

