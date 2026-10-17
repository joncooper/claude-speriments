# Source Generated with Decompyle++
# File: migration_config.pyc (Python 3.11)

from typing import List, Tuple
from dropbox.client.features.computer_backup.cb_migration_state import CBMigrationState, ComputerBackupMigrationState
from dropbox.client.features.computer_backup.computer_backup_logging import ComputerBackupLogger
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.machine import MachineContext
from dropbox.sync_engine_boundary.constants import OSFolderID

class CBMigrationConfig:
    
    def __init__(self = None, machine_context = None):
        self.machine_context = machine_context

    
    def current_state(self = None):
        if not self.machine_context.primary_account_config:
            report_bad_assumption('missing_primary_account_config')
            return ComputerBackupMigrationState(CBMigrationState.MIGRATION_ATTEMPT_INIT)
        stored_state = None.machine_context.primary_account_config.computer_backup_migration_state
        if not stored_state:
            return ComputerBackupMigrationState(CBMigrationState.MIGRATION_ATTEMPT_INIT)

    
    def finish_update(self = None, new_state = None):
        if not self.machine_context.primary_account_config:
            report_bad_assumption('missing_primary_account_config')
            return None
        self.machine_context.primary_account_config.computer_backup_migration_state = None
        ComputerBackupLogger.report_migration_state_event(self.machine_context, new_state)

    
    def set_folders_to_migrate(self = None, folders_to_migrate = None):
        new_state = self.current_state()
        new_state.folders_to_migrate = folders_to_migrate
        self.finish_update(new_state)

    
    def get_folders_to_migrate(self = None):
        current_state = self.current_state()
        return current_state.folders_to_migrate


