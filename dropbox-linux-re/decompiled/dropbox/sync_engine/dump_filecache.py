# Source Generated with Decompyle++
# File: dump_filecache.pyc (Python 3.11)

from file_cache.database import load_dropbox_filecache
from file_cache.nucleus_migration import FilecacheNucleusMigrationManager, MigrationFileCacheDump
from file_cache.sqlite_backend import SQLiteBackendCursor
from file_system.file_system import BaseFileSystem as FileSystem
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.shared.server_path import RRLowerServerPath
from dropbox.sync_engine_boundary.hidden import HiddenSet
from dropbox.sync_engine_boundary.nucleus_types import FileCacheDumpResult
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import LocalConfigurationInterface

def dump_filecache_for_nucleus_migration(local_config = None):
    fs = FileSystem()
    TRACE('Directly loading filecache for nucleus migration.')
    fc = load_dropbox_filecache(database_dir = local_config.appdata_path, server_conn = None, config = local_config.config_dict, sigstore = None, keystore = local_config.keystore, corruptdb_handler = None, infinite_stubfolders_enabled = False, infinite_cloud_docs_enabled = False, symlink_filtering_enabled = False)
    
    try:
        trans = fc.read_transaction()
        hidden_set = read_hidden_set_from_disk(trans.sqlite_cursor())
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        start_ts = get_monotonic_time_seconds()
                        fcmm = FilecacheNucleusMigrationManager(fc, fs.make_path(local_config.appdata_path))
                        result = fcmm.generate_snapshot(timeout = None)
                        elapsed_secs = get_monotonic_time_seconds() - start_ts
                        fc.close()
                    except:
                        fc.close()

                    return FileCacheDumpResult(timed_out = result.timed_out, time_to_generate_ms = int(elapsed_secs * 1000), number_of_entries_processed = result.number_of_entries, path = result.path, hidden_set = hidden_set)




CONFIG_SELSYNC_ALL_HIDDEN_PATHS_KEY = 'selective_sync_ignore_list'
CONFIG_SELSYNC_USER_OVERRIDE_PATHS_KEY = 'selective_sync_user_override_paths'
CONFIG_ADMIN_DEFAULT_HIDDEN_PATHS = 'selective_sync_admin_default_hidden_paths'

def read_hidden_set_from_disk(cursor = None):
    cached_user_excludes = cursor.get_config_key(CONFIG_SELSYNC_ALL_HIDDEN_PATHS_KEY, default = [])
    cached_user_includes = cursor.get_config_key(CONFIG_SELSYNC_USER_OVERRIDE_PATHS_KEY, default = [])
    cached_admin_default_excludes = cursor.get_config_key(CONFIG_ADMIN_DEFAULT_HIDDEN_PATHS, default = [])
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(cached_user_includes())(user_hidden_paths = None, user_override_paths = frozenset, admin_default_hidden_paths = (lambda .0: pass# WARNING: Decompyle incomplete
)(cached_admin_default_excludes()))

