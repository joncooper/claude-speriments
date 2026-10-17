# Source Generated with Decompyle++
# File: file_provider_cdm_migrator.pyc (Python 3.11)

import os
from enum import Enum
from time import sleep
from typing import Callable, Optional, Text
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.databases import clear_appdata_without_unlink
from dropbox.client.features.sync_everything.v3.config_utils import write_sync_everything_cdm_flag_if_needed
from dropbox.client.folder_tagger.folder_tagger import FolderTagger
from dropbox.client.high_trace import force_flush, send_trace_log
from dropbox.client.unlink_cookie import write_unlink_cookie_no_sync_engine
from dropbox.event import report
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.interface import SyncRootManagerInterface, SyncRootType
from dropbox.sync_root.types import RemovalMode
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import LocalConfigurationInterface
    from dropbox.client.main import DropboxApplication
    from dropbox.shared.local_path import LocalPath
    from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
_CDM_MIGRATION_ONGOING_KEY = 'fp_cdm_migration_ongoing'

def is_fp_cdm_migration_ongoing(config = None):
    return _CDM_MIGRATION_ONGOING_KEY in config.config_dict


class FileProviderCdmMigratorException(Exception):
    pass


class EventType(Enum):
    START = 'start'
    END = 'end'
    ERROR = 'error'


class FileProviderCdmMigrator:
    
    def __init__(self, app, file_system = None, config = None, update_tray_status = None, account = ('app', 'DropboxApplication', 'file_system', 'AbstractFileSystem', 'config', 'LocalConfigurationInterface', 'update_tray_status', 'Callable[[], None]', 'account', 'AccountInterface', 'return', 'None')):
        self._app = app
        self._fs = file_system
        self._config = config
        self._account = account
        self._update_tray_status_fn = update_tray_status
        self._folder_tagger = FolderTagger(self._fs, None)

    
    def migrate(self = None, home_ns_localpath = None, server_relocation_ongoing = None):
        TRACE('CDM_RELOCATE: inside migrate call for account %r', self._account)
        self._assert_fp_root(self._app.root_manager)
        dropbox_path = self._config.get_dropbox_path()
    # WARNING: Decompyle incomplete

    
    def _assert_fp_root(self = None, root_manager = None):
        root_type_fut = root_manager.get_root_type(self._account)
        root_type_fut.block()
        root_type = root_type_fut.result()
    # WARNING: Decompyle incomplete

    
    def _should_migrate(self = None, dropbox_path = None, home_ns_path = None):
        if is_fp_cdm_migration_ongoing(self._config):
            TRACE('CDM_RELOCATE: Detected ongoing migration.')
            return True
        if not None.path.exists(Text(dropbox_path)):
            TRACE('CDM_RELOCATE: No Dropbox root - nothing to relocate.')
            return False
        root_ns_id = None._account.root_ns_id
        home_ns_id = self._account.home_ns_id
        client_home_ns_path_unicode = self._config.config_dict.get('home_ns_path', None)
        root_tag_ns = self._folder_tagger.get_folder_ns(dropbox_path)
    # WARNING: Decompyle incomplete

    
    def _handle_ongoing_server_relocation(self = None):
        TRACE('CDM_RELOCATE: server relocation in progress. Crash-loop until the server relocates.')
        sleep(10)
        self._app.restart()

    
    def _write_migration_ongoing(self = None):
        self._config.config_dict[_CDM_MIGRATION_ONGOING_KEY] = True

    
    def _write_migration_done(self = None):
        del self._config.config_dict[_CDM_MIGRATION_ONGOING_KEY]

    _flush_logs = (lambda : force_flush()send_trace_log())()
    _report_migration_event = (lambda ev_type = None: event_name = 'fp_migration_' + ev_type.valuereport('cdm-relocate-attempt', event_name = event_name))()

