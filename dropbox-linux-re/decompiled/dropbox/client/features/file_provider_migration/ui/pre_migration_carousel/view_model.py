# Source Generated with Decompyle++
# File: view_model.pyc (Python 3.11)

from datetime import timezone
from typing import Any, Dict, Optional
from dateutil.parser import isoparse
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.external_drive_backup.manager import ExternalBackupManager
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_result import BackupResult
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.backup_status_code import BackupStatusCode
from dropbox.client.features.file_provider_migration.config import FPMigrationStateStore
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FileProviderMigrationEvent as FileProviderMigrLoggingEvent, FileProviderMigrationExtraKeys, FileProviderMigrationLogger
from dropbox.client.features.file_provider_migration.helpers import get_formatted_time_estimate, get_num_files_per_account, get_time_estimate, get_total_num_files_in_dbx, get_total_time_estimate
from dropbox.client.features.file_provider_migration.implementation import FileProviderMigrationControllerWrapper
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.bridge_interface_fp_migration_carousel_view_model import FpMigrationCarouselViewModelBridgeInterface
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_action_surface import FileProviderActionSurface
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_migration_event import FileProviderMigrationEvent
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.fp_migration_status_code import FpMigrationStatusCode
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function
from dropbox.client.features.sync_everything.view_model.operation_result import OperationResult
from dropbox.client.tray.active_account_tracker import ActiveAccountTracker
from dropbox.client.ui.common.selective_sync_v4 import show_selsync_mev
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.trace import TRACE
DEFAULT_SELSYNC_SOFT_LIMIT = 300000
DEFAULT_SELSYNC_HARD_LIMIT = 500000
FP_SELSYNC_SOFT_LIMIT = 'desktop-fp-selsync-soft-limit'
FP_SELSYNC_HARD_LIMIT = 'desktop-fp-selsync-hard-limit'

class FPPreMigrationCarouselViewModel(Actor, FpMigrationCarouselViewModelBridgeInterface):
    pass
# WARNING: Decompyle incomplete

