# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

import datetime
import os
import time
from typing import MutableMapping
from build_number.environment import magic_trace_key_is_set
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.cloud_files_migration.constants import CLOUD_FILES_MIGRATION_STORMCROW, CLOUD_FILES_MIGRATION_TTL
from dropbox.client.features.cloud_files_migration.helpers import get_cf_migration_start_time, get_local_config, has_multiple_owners_for_same_path, is_nested_under_cloud_files_root, within_file_count_limit
from dropbox.client.features.cloud_files_migration.logger import CloudFilesMigrationEvent, CloudFilesMigrationExtraKeys, CloudFilesMigrationLogger
from dropbox.client.features.cloud_files_migration.state_machine import MigrationStateMachine
from dropbox.client.features.cloud_files_migration.types import CloudFilesAccountMigrationState, CloudFilesAccountMigrationStateExtras
from dropbox.client.features.external_drive_backup.utils import user_has_enabled_non_fission_edb
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.gandalf import Gandalf
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.nucleus.migration_state import SyncEngineStateManager
from dropbox.platform import IS_WINDOWS
from dropbox.sync_root.gating import cloud_files_eligible
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE
_ENV: 'MutableMapping[str, str]' = os.environ

def is_scheduled_to_be_on_cloud_files_root(local_config = None):
