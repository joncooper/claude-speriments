# Source Generated with Decompyle++
# File: migration.pyc (Python 3.11)

from __future__ import annotations
import os
from typing import Any, Callable, Dict, List, NamedTuple, Optional, Text, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import HIDDEN_FILEID_SET_KEY
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.unlink_cookie import write_unlink_cookie
from dropbox.client_api.exceptions import HTTP409Error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_remove, safe_rmtree_with_retry
from dropbox.functions import retry, RetryException
from dropbox.model.types import FileId
from dropbox.nucleus.migration_constants import NucleusMigrationArgs, SyncEngineState, SyncEngineType
from dropbox.nucleus.migration_state import SyncEngineStateManager
from dropbox.preferences import EVER_FINISHED_INITIAL_LIST
from dropbox.proto.nucleus.migration_pb2 import UpgradeFromClassicIgnorePath
from dropbox.proto.nucleus.published_event_pb2 import PublishedEvent
from dropbox.shared.server_path import RRCasedServerPath
from dropbox.stopwatch import global_sw
from dropbox.sync_engine_boundary.hidden import HiddenSet
from dropbox.sync_engine_boundary.nucleus_types import FileCacheDumpResult, FileCacheDumpTimedOut
from dropbox.sync_engine_boundary.selsync import FileIdSet
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client_api.dropbox_connection import DropboxConnection
ConvertSelsyncSetResult = NamedTuple('ConvertSelsyncSetResult', [
    ('fileid_set', FileIdSet),
    ('cased_paths', List[RRCasedServerPath])])
convert_selsync_set_network = (lambda conn = None, account = None, parent_path = retry(999999, delay = 10, backoff = 2, max_backoff = 90), retry_request = ('conn', 'DropboxConnection', 'account', 'AccountInterface', 'parent_path', 'Text', 'retry_request', 'bool', 'return', 'Dict[Text, Any]'): try:
conn.api_v2_tree_view_folders(account, parent_path)except HTTP409Error:
raise except Exception:
e = Noneif retry_request:
raise RetryException(inner = e)raise e = Nonedel e)()

def convert_selsync_set(account = None, conn = None, server_paths = None, retry_network = (True,)):
    root_ns = account.root_ns_id
# WARNING: Decompyle incomplete

SEC_DB_TO_DELETE_PREFIX = [
    'PENDING_',
    'TO_HASH_',
    'UPDATED_']
SEC_DB_TO_DELETE = [
    'checker.dbx',
    'deleted.dbx',
    'filecache.db',
    'filecache.dbx',
    'filecache1.db',
    'filecache2.db',
    'filecache_migration.db',
    'resync.dbx',
    'sigstore.db',
    'sigstore.dbx']

class SyncEngineMigration(object):
    should_run_cdm_migration = (lambda config = None: pass# WARNING: Decompyle incomplete
)()
    initialize = (lambda config = None, account = None: updated_state = SyncEngineStateManager.handle_sync_engine_type_update(config, account)restart_if_running = SyncEngineStateManager.should_restart_if_running(updated_state) if updated_state else False(updated_state, restart_if_running))()
    compute_migration_args = (lambda config = None, account = None, conn = staticmethod, dump_filecache_for_nucleus_migration = ('config', 'LocalConfigurationInterface', 'account', 'AccountInterface', 'conn', 'DropboxConnection', 'dump_filecache_for_nucleus_migration', 'Callable[[LocalConfigurationInterface], FileCacheDumpResult]', 'return', 'NucleusMigrationArgs'): pass# WARNING: Decompyle incomplete
)()
    reset_app_config_after_migration = (lambda config = None: config.config_dict[EVER_FINISHED_INITIAL_LIST] = False)()
    get_nucleus_shadow_appdata_dir = (lambda appdata_path = None: os.path.join(appdata_path, 'sync_ro'))()
    get_nucleus_appdata_dir = (lambda appdata_path = None: os.path.join(appdata_path, 'sync'))()
    cleanup_shadow_migration_appdata = (lambda config = None: path = SyncEngineMigration.get_nucleus_shadow_appdata_dir(config.appdata_path)if os.path.exists(path):
if safe_rmtree_with_retry(path):
TRACE('[SyncEngineMigration] successfully deleted previous shadow migration addpdata_path at %r', path)else:
TRACE('[SyncEngineMigration] exception while deleting previous shadow migration appdata_path %r', path)if os.path.exists(config.appdata_path):
for fname in os.listdir(config.appdata_path):
if fname.startswith('nucleus.sqlite3'):
path = os.path.join(config.appdata_path, fname)TRACE('Attempting to delete leftover Nucleus metadata file: %r', path)safe_remove(path)NoneNone)()
    cleanup_nucleus_appdata = (lambda config = None: migration_state = SyncEngineStateManager.get_sync_engine_state(config)if migration_state not in (SyncEngineState.CLASSIC, SyncEngineState.PREPARING_CLASSIC_TO_NUCLEUS_MIGRATION, SyncEngineState.MIGRATING_CLASSIC_TO_NUCLEUS, None):
TRACE('Not cleaning up Nucleus appdata in state %r', migration_state)Nonemetadata_directory = None.get_nucleus_appdata_dir(config.appdata_path)# WARNING: Decompyle incomplete
)()
    cleanup_sec_appdata = (lambda config = None: migration_state = SyncEngineStateManager.get_sync_engine_state(config)if migration_state != SyncEngineState.NUCLEUS:
TRACE('Not cleaning up SEC appdata in state %r', migration_state)Noneto_delete = None[:]try:
files = os.listdir(config.appdata_path)for fn in files:
for prefix in SEC_DB_TO_DELETE_PREFIX:
if fn.find(prefix) == 0:
to_delete.append(fn)except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.NUCLEUS)for fn in to_delete:
db_path = os.path.join(config.appdata_path, fn)TRACE('Cleaning up SEC appdata db at path %r', db_path)safe_remove(db_path)None)()

