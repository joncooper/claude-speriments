# Source Generated with Decompyle++
# File: cf_migration.pyc (Python 3.11)

from datetime import datetime, timedelta
from typing import Optional, Sequence
from dropbox.client.features.cloud_files_migration.constants import CLOUD_FILES_LAST_DISMISSED_CONFIG_KEY, CLOUD_FILES_MIGRATION_UI_STORMCROW, CLOUD_FILES_NUM_DISMISSED_CONFIG_KEY
from dropbox.client.features.cloud_files_migration.helpers import get_local_config
from dropbox.client.features.cloud_files_migration.logger import CloudFilesMigrationSurfaceUI
from dropbox.client.features.cloud_files_migration.migration_manager import CloudFilesMigrationManager
from dropbox.client.features.cloud_files_migration.notification_controller import CloudFilesMigrationNotificationController
from dropbox.client.features.cloud_files_migration.state_machine import MigrationStateMachine
from dropbox.client.features.cloud_files_migration.types import CloudFilesAccountMigrationState
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
from dropbox.foundation.raii2 import destroying
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def get_cf_migration_subitems(app = None):
    pass
# WARNING: Decompyle incomplete

