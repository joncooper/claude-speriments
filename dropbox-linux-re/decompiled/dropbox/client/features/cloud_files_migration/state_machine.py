# Source Generated with Decompyle++
# File: state_machine.pyc (Python 3.11)

from typing import Any, Callable, Dict, Optional, Tuple
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.cloud_files_migration.constants import CLOUD_FILES_MIGRATION_STATE_CONFIG_KEY, CLOUD_FILES_MIGRATION_STATE_EXTRAS_CONFIG_KEY
from dropbox.client.features.cloud_files_migration.types import CloudFilesAccountMigrationState, CloudFilesAccountMigrationStateExtras
from dropbox.trace import TRACE

class MigrationStateMachine:
    update = (lambda local_config = None, state = None, force_callbacks = staticmethod, extras = (False, None): old_state = local_config.config_dict.get(CLOUD_FILES_MIGRATION_STATE_CONFIG_KEY, CloudFilesAccountMigrationState.CHECK_ELIGIBILITY)to_persist = {
CLOUD_FILES_MIGRATION_STATE_CONFIG_KEY: state }# WARNING: Decompyle incomplete
)()
    get_state = (lambda local_config = None: migration_state = local_config.config_dict.get(CLOUD_FILES_MIGRATION_STATE_CONFIG_KEY, CloudFilesAccountMigrationState.CHECK_ELIGIBILITY)extras = local_config.config_dict.get(CLOUD_FILES_MIGRATION_STATE_EXTRAS_CONFIG_KEY, None)(migration_state, extras))()
    add_state_change_callback = (lambda local_config = None, callback = None: local_config.add_pref_callback(CLOUD_FILES_MIGRATION_STATE_CONFIG_KEY, callback))()
    remove_state_change_callback = (lambda local_config = None, callback = None: local_config.remove_pref_callback(CLOUD_FILES_MIGRATION_STATE_CONFIG_KEY, callback))()

