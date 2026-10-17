# Source Generated with Decompyle++
# File: migration_sync_tracker.pyc (Python 3.11)

from typing import cast, Optional, Text
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.cloud_files_migration.constants import CF_MIGRATION_ROUGH_SYNC_ESTIMATE, CF_MIGRATION_SYNC_PROGRESS_JOB_NAME, MINUTES_TO_INCREMENT_BY
from dropbox.client.features.cloud_files_migration.logger import CloudFilesMigrationEvent, CloudFilesMigrationExtraKeys, CloudFilesMigrationLogger
from dropbox.client.features.cloud_files_migration.state_machine import MigrationStateMachine
from dropbox.client.features.cloud_files_migration.types import CloudFilesAccountMigrationState
from dropbox.client.periodic import PeriodicScheduler
from dropbox.foundation.account_manager import AccountManager
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.types import CallbackRemovalToken
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress

class MigrationSyncTracker(Destroyable):
    pass
# WARNING: Decompyle incomplete

