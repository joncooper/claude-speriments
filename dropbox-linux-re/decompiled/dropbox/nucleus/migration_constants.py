# Source Generated with Decompyle++
# File: migration_constants.pyc (Python 3.11)

from __future__ import annotations
from enum import Enum, IntEnum
from typing import Callable, List, Optional, Text
from dropbox.proto.nucleus.migration_pb2 import UpgradeFromClassicIgnorePath
from dropbox.proto.nucleus.published_event_pb2 import PublishedEvent

class SyncEngineState(IntEnum):
    CLASSIC = 1
    NUCLEUS = 2
    MIGRATING_CLASSIC_TO_NUCLEUS = 3
    DEPRECATED_MIGRATING_NUCLEUS_TO_CLASSIC = 4
    PREPARING_CLASSIC_TO_NUCLEUS_MIGRATION = 6
    DEPRECATED_CLEANUP_AFTER_NUCLEUS_TO_CLASSIC_MIGRATION = 7

SYNC_ENGINE_STATE_TO_STRING = {
    SyncEngineState.PREPARING_CLASSIC_TO_NUCLEUS_MIGRATION: 'preparing_classic_to_nucleus_migration',
    SyncEngineState.MIGRATING_CLASSIC_TO_NUCLEUS: 'migrating_classic_to_nucleus',
    SyncEngineState.NUCLEUS: 'nucleus',
    SyncEngineState.CLASSIC: 'classic' }

class SyncEngineType(Enum):
    CLASSIC = 1
    NUCLEUS = 2

SYNC_ENGINE_STATE_KEY = 'sync_engine_state'
MIGRATION_BLOCKED_KEY = 'nucleus_premigration_blocked'
SYNC_ENGINE_MIGRATION_COUNT = 'sync_engine_migration_count'

class NucleusMigrationArgs(object):
    
    def __init__(self, migration_state, upgrade_completed_fn = None, initial_hidden_fileid_set = None, initial_ignore_path_set = None, filecache_migration_db_path = (None, None, None, None, None), timeout_secs = ('migration_state', 'SyncEngineState', 'upgrade_completed_fn', 'Optional[Callable[[PublishedEvent.MigrationCompletedInfo.V], None]]', 'initial_hidden_fileid_set', 'Optional[List[Text]]', 'initial_ignore_path_set', 'Optional[List[UpgradeFromClassicIgnorePath]]', 'filecache_migration_db_path', 'Optional[Text]', 'timeout_secs', 'Optional[int]', 'return', 'None')):
        self.migration_state = migration_state
        self.upgrade_completed_fn = upgrade_completed_fn
        self.initial_hidden_fileid_set = initial_hidden_fileid_set
        self.initial_ignore_path_set = initial_ignore_path_set
        self.filecache_migration_db_path = filecache_migration_db_path
        self.timeout_secs = timeout_secs
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return 'NucleusMigrationArgs: migration_state: {} initial_hidden_fileid_set: {} initial_ignore_path_set: {} filecache_migration_db_path: {} timeout_secs: {}'.format(self.migration_state, self.initial_hidden_fileid_set, self.initial_ignore_path_set, self.filecache_migration_db_path, self.timeout_secs)


