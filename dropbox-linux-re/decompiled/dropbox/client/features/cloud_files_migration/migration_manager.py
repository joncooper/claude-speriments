# Source Generated with Decompyle++
# File: migration_manager.pyc (Python 3.11)

import math
import time
import uuid
from typing import Any, Dict, List, Optional
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.cloud_files_migration.constants import CLOUD_FILES_MIGRATION_UI_STORMCROW, CLOUD_FILES_SESSION_ID_CONFIG_KEY
from dropbox.client.features.cloud_files_migration.gating import should_migrate_to_cloud_files
from dropbox.client.features.cloud_files_migration.helpers import get_cf_migration_start_time, get_local_config, set_cf_migration_start_time, state_to_logger_event
from dropbox.client.features.cloud_files_migration.logger import CloudFilesMigrationEvent, CloudFilesMigrationExtraKeys, CloudFilesMigrationLogger, CloudFilesMigrationSurfaceUI
from dropbox.client.features.cloud_files_migration.migration_sync_tracker import MigrationSyncTracker
from dropbox.client.features.cloud_files_migration.notification_controller import CloudFilesMigrationNotificationController
from dropbox.client.features.cloud_files_migration.state_machine import MigrationStateMachine
from dropbox.client.features.cloud_files_migration.types import CloudFilesAccountMigrationState
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext, MachineStormcrow
from dropbox.foundation.environment import debugging_features_are_enabled
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.platform import IS_WINDOWS
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class CloudFilesMigrationManager(SingletonActor):
    pass
# WARNING: Decompyle incomplete

