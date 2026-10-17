# Source Generated with Decompyle++
# File: migration_state.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.event import report
from dropbox.nucleus.migration_constants import SYNC_ENGINE_MIGRATION_COUNT, SYNC_ENGINE_STATE_KEY, SYNC_ENGINE_STATE_TO_STRING, SyncEngineState, SyncEngineType
from dropbox.threading import Lock
from dropbox.trace import TRACE
_sync_engine_state_lock = Lock()
_sync_engine_migration_count_lock = Lock()

class SyncEngineStateManager(object):
    get_sync_engine_state = (lambda config = None: _sync_engine_state_lockNone(None, None)with None:
if not None, SyncEngineStateManager._get_sync_engine_state_unlocked(config):
pass)()
    _get_sync_engine_state_unlocked = (lambda config = None: pass# WARNING: Decompyle incomplete
)()
    is_fully_migrated_to_nucleus = (lambda config = None: migration_state = SyncEngineStateManager.get_sync_engine_state(config)migration_state == SyncEngineState.NUCLEUS)()
    is_migrating_to_or_is_nucleus = (lambda config = None: migration_state = SyncEngineStateManager.get_sync_engine_state(config)migration_state in (SyncEngineState.NUCLEUS, SyncEngineState.MIGRATING_CLASSIC_TO_NUCLEUS))()
    is_migrating = (lambda config = None: migration_state = SyncEngineStateManager.get_sync_engine_state(config)migration_state == SyncEngineState.MIGRATING_CLASSIC_TO_NUCLEUS)()
    current_sync_engine_type = (lambda config = None: migration_state = SyncEngineStateManager.get_sync_engine_state(config)if migration_state in (None, SyncEngineState.CLASSIC, SyncEngineState.PREPARING_CLASSIC_TO_NUCLEUS_MIGRATION, SyncEngineState.MIGRATING_CLASSIC_TO_NUCLEUS):
SyncEngineType.CLASSIC# WARNING: Decompyle incomplete
)()
    _report_sync_engine_state = (lambda old_state = None, new_state = None, account = staticmethod: pass# WARNING: Decompyle incomplete
)()
    set_and_report_sync_engine_state = (lambda config = None, state = None, account = staticmethod: TRACE('Setting sync engine migration state %r for account %r', state, account)# WARNING: Decompyle incomplete
)()
    _set_sync_engine_state_unlocked = (lambda config = None, state = None: pass# WARNING: Decompyle incomplete
)()
    test_only_set_state_to_classic = (lambda config = None: _sync_engine_state_lockconfig.update_preferences({
SYNC_ENGINE_STATE_KEY: int(SyncEngineState.CLASSIC) })None(None, None)Nonewith None:
if not None:
pass)()
    test_only_set_state_to_nucleus = (lambda config = None: _sync_engine_state_lockconfig.update_preferences({
SYNC_ENGINE_STATE_KEY: int(SyncEngineState.NUCLEUS) })None(None, None)Nonewith None:
if not None:
pass)()
    should_restart_if_running = (lambda state = None: state == SyncEngineState.MIGRATING_CLASSIC_TO_NUCLEUS)()
    handle_sync_engine_type_update = (lambda config = None, account = None: _sync_engine_state_lockupdated_state = Nonecurrent_state = SyncEngineStateManager._get_sync_engine_state_unlocked(config)# WARNING: Decompyle incomplete
)()
    reset_migration_count = (lambda config = None: _sync_engine_migration_count_lockconfig.config_dict[SYNC_ENGINE_MIGRATION_COUNT] = 0None(None, None)Nonewith None:
if not None:
pass)()
    get_migration_count = (lambda config = None: _sync_engine_migration_count_lockNone(None, None)with None:
if not None, SyncEngineStateManager._get_migration_count_unlocked(config):
pass)()
    increment_migration_count = (lambda config = None: _sync_engine_migration_count_lockmigration_count = SyncEngineStateManager._get_migration_count_unlocked(config) + 1TRACE('Setting migration count to %r', migration_count)config.config_dict[SYNC_ENGINE_MIGRATION_COUNT] = migration_countNone(None, None)with None:
if not None, migration_count:
pass)()
    _get_migration_count_unlocked = (lambda config = None: config.config_dict.get(SYNC_ENGINE_MIGRATION_COUNT, 0))()

