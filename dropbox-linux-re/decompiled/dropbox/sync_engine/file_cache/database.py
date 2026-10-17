# Source Generated with Decompyle++
# File: database.pyc (Python 3.11)

from __future__ import absolute_import
import os
from contextlib import closing
from typing import Text
from exceptions import ResyncRequiredMigrationException
from file_cache import FileCache
from sqlite_backend import SQLiteBackend
from dropbox.client.databases import _FILE_CACHE_ENC_FILENAME
from dropbox.client.util import fs_supports_attrs
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import DB_MIGRATION_ERROR_EVENT
from dropbox.exception.reporting import report_exception
from dropbox.fileutils import safe_remove
from dropbox.handler_registries import add_exception_handler, remove_exception_handler
from dropbox.platform import IS_LINUX, IS_MAC, platform
from dropbox.trace import TRACE
_PENDING_DATABASE_PREFIX = 'PENDING_'
_UPDATED_DATABASE_PREFIX = 'UPDATED_'

def filecache_version_1_2_data_plats(dropbox_dir):
    if not IS_MAC and IS_LINUX:
        platforms = ()
    else:
        platforms = set(('posix',))
        if dropbox_dir and fs_supports_attrs(dropbox_dir):
            platforms.add(platform)
    return platforms


def _check_migration_filecache(database_dir, server_conn, config, keystore, sigstore = (None,)):
    pass
# WARNING: Decompyle incomplete


def load_dropbox_filecache(database_dir, server_conn, config, sigstore, keystore, corruptdb_handler = None, infinite_stubfolders_enabled = None, infinite_cloud_docs_enabled = None, symlink_filtering_enabled = ('database_dir', 'Text', 'server_conn', 'Optional[DropboxConnection]', 'config', 'ConfigDict', 'sigstore', 'Optional[SigStore]', 'keystore', 'DBKeyStore', 'corruptdb_handler', 'Any', 'infinite_stubfolders_enabled', 'bool', 'infinite_cloud_docs_enabled', 'bool', 'symlink_filtering_enabled', 'bool', 'return', 'FileCache')):
    remove_exception_handler(corruptdb_handler)
    
    try:
        _check_migration_filecache(database_dir, server_conn, config, keystore, sigstore)
    except Exception:
        report_exception(component = DesktopComponent.SYNC_ENGINE)

    add_exception_handler(corruptdb_handler)
    
    try:
        for file_ in os.listdir(database_dir):
            if file_.startswith(_PENDING_DATABASE_PREFIX) or file_.startswith(_UPDATED_DATABASE_PREFIX):
                safe_remove(os.path.join(database_dir, file_))
    except Exception:
        report_exception(component = DesktopComponent.SYNC_ENGINE)

    file_cache_filename = os.path.join(database_dir, _FILE_CACHE_ENC_FILENAME)
    TRACE('Using FileCache db: %r', file_cache_filename)
    
    try:
        return FileCache(file_cache_filename, keystore, infinite_stubfolders_enabled, infinite_cloud_docs_enabled, symlink_filtering_enabled)
    except Exception:
        report_exception(component = DesktopComponent.SYNC_ENGINE)
        TRACE('Exception while loading file_cache, clearing file and trying again')
        safe_remove(file_cache_filename)
        return 


