# Source Generated with Decompyle++
# File: desktop_prompt_action_handler_service.pyc (Python 3.11)

from build_number.platform import IS_MAC
from dropbox.client.features.backup_common.base_event_reporter import random_session_id
from dropbox.client.features.cloud_files_migration.logger import CloudFilesMigrationSurfaceUI
from dropbox.client.features.cloud_files_migration.migration_manager import CloudFilesMigrationManager
from dropbox.client.features.computer_backup.cb_manager_wrapper import ComputerBackupManagerWrapper
from dropbox.client.features.file_provider_migration.file_provider_migration_logger import FileProviderMigrationLogger
from dropbox.client.features.file_provider_migration.migration_session import FPMigrationSessionData
from dropbox.client.features.file_provider_migration.ui.controllers.pre_migration_flow import PreMigrationFlowController
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_action_surface import FileProviderActionSurface
from dropbox.client.features.file_provider_migration.ui.pre_migration_carousel.bridge_gen.file_provider_migration_event import FileProviderMigrationEvent
from dropbox.client.features.sync_everything.v3.sync_everything_manager import SyncEverythingManager
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.client.fenix.utils import fenix_api, get_account_linked_or_from_cache
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.electron.ipc import ElectronIpc
from dropbox.foundation.html_views.electron.ipc._interface import JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2 import destroying
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class DesktopPromptActionHandlerService(Actor):
    pass
# WARNING: Decompyle incomplete

