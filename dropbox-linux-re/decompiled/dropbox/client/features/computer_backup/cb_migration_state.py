# Source Generated with Decompyle++
# File: cb_migration_state.pyc (Python 3.11)

from enum import auto, Enum
from typing import List, Optional, Tuple
from dropbox.sync_engine_boundary.constants import OSFolderID

class CBMigrationState(Enum):
    MIGRATION_ATTEMPT_INIT = auto()
    MIGRATION_START = auto()
    CBOS_DISABLE_FAIL = auto()
    CBOS_DISABLE_COMPLETE = auto()
    CBOA_SANITY_FAIL = auto()
    CBOA_SANITY_SUCCESS = auto()
    CBOA_SETUP_COMPLETE = auto()
    CBOA_SETUP_FAIL = auto()
    MIGRATION_COMPLETE = auto()


class ComputerBackupMigrationState:
    
    def __init__(self = None, last_state = None, folders_to_migrate = None):
        self._last_migration_state = last_state
        self._folders_to_migrate = folders_to_migrate
        self._folders_disabled_successfully = None
        self._folders_enabled_successfully = None

    
    def __str__(self = None):
        folder_str = (lambda .0: [ str(f) for f in .0 ])(self._folders_to_migrate()) if self._folders_to_migrate else '[]'
        folders_disabled_str = (lambda .0: [ str(f) for f in .0 ])(self._folders_disabled_successfully()) if self._folders_disabled_successfully else '[]'
        folders_setup_str = (lambda .0: [ str(f) for f in .0 ])(self._folders_enabled_successfully()) if self._folders_enabled_successfully else '[]'
        return 'MigrationState(last_state={} folders={} folders_disabled={} folders_enabled={}'.format(self._last_migration_state, folder_str, folders_disabled_str, folders_setup_str)

    
    def __repr__(self = None):
        return str(self)

    last_migration_state = (lambda self = None: self._last_migration_state)()
    last_migration_state = (lambda self = None, new_migration_state = None: self._last_migration_state = new_migration_state)()
    folders_to_migrate = (lambda self = None: self._folders_to_migrate if self._folders_to_migrate else [])()
    folders_to_migrate = (lambda self = None, folders_to_migrate = None: self._folders_to_migrate = folders_to_migrate)()
    folders_disabled_successfully = (lambda self = None: self._folders_disabled_successfully if self._folders_disabled_successfully else [])()
    folders_disabled_successfully = (lambda self = None, folders_disabled = None: self._folders_disabled_successfully = folders_disabled)()
    folders_enabled_successfully = (lambda self = None: self._folders_enabled_successfully if self._folders_enabled_successfully else [])()
    folders_enabled_successfully = (lambda self = None, folders_enabled = None: self._folders_enabled_successfully = folders_enabled)()

