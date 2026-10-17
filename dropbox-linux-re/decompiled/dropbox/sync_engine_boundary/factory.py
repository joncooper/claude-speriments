# Source Generated with Decompyle++
# File: factory.pyc (Python 3.11)

import os
from typing import Any, Callable, cast, Dict, Iterable, Iterator, List, Optional, Text
from apex.context import ApexContext
from build_number import is_test, VERSION
from dropbox.attrs import Attributes
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.quarantine_xattr import check_and_remove_quarantine_xattr
from dropbox.metrics.reporter import PeriodicMetricsReporter
from dropbox.model.types import FileId
from dropbox.nucleus.bolt_client import NucleusBoltClient
from dropbox.nucleus.enabled import NucleusEnabled
from dropbox.nucleus.migration import SyncEngineMigration
from dropbox.sync_engine.attrs_handler import AttributesHandler
from dropbox.sync_engine.attrs_whitelist import ATTRS_WHITELIST_HARDCODED
from dropbox.sync_engine.fileid_utils import PERSISTED_FILEID_PRESERVED_NAME, serialize_fileid_and_rev
from dropbox.sync_engine.fileids import extra_attrs_from_fileid_xattr, map_fileid_to_ascii, new_fileid_xattr
from dropbox.sync_engine_boundary.exceptions import IncompleteMigrationException
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
from dropbox.sync_engine_boundary.monitored_thread_pool import MonitoredThreadPoolExecutor
from dropbox.sync_engine_boundary.nucleus_types import FileCacheDumpTimedOut
from dropbox.sync_engine_boundary.sync_engine_interface import SyncEngineClassicInterface
from dropbox.sync_engine_boundary.sync_engine_util.interface import SyncEngineUtilInterface
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import LocalConfigurationInterface
    from dropbox.client.fsw.fsw_nucleus_args import FSWManagerArgs
    from dropbox.client.gandalf import Gandalf
    from dropbox.client.periodic import PeriodicScheduler
    from dropbox.client.shell.multiaccount_shell_adapter import MultiaccountShellAdapter
    from dropbox.client_api.dropbox_connection import DropboxConnection
    from dropbox.fileevents import FileEvents
    from dropbox.shared.local_path import LocalPath
    from dropbox.sync_engine.file_system.memory import MemoryFS

class SyncEngineFactory(object):
    
    def __init__(self = None):
        self._initialize_classes()

    
    def _initialize_classes(self = None):
        dump_filecache_for_nucleus_migration = dump_filecache_for_nucleus_migration
        import dropbox.sync_engine.dump_filecache
        FileSystem = FileSystem
        import dropbox.sync_engine.file_system.file_system
        NucleusClassicClient = NucleusClassicClient
        import dropbox.sync_engine.nucleus.classic_client.sync_engine
        SyncEngineUtil = SyncEngineUtil
        import dropbox.sync_engine.sync_engine_util
        if is_test():
            MemoryFS = MemoryFS
            import dropbox.sync_engine.file_system.memory
        self._dump_filecache_for_nucleus_migration = dump_filecache_for_nucleus_migration
        self._FileSystem = FileSystem
        self._SyncEngineUtil = SyncEngineUtil
        self._NucleusClassicClient = NucleusClassicClient
        if is_test():
            self._MemoryFS = MemoryFS
            return None

    make_default_file_system = (lambda : SyncEngineFactory().make_file_system())()
    make_memory_file_system = (lambda case_sensitive = None: pass# WARNING: Decompyle incomplete
)()
    make_default_sync_engine_util = (lambda : SyncEngineFactory().make_sync_engine_util())()
    
    def make_sync_engine(self, account, local_config, sync_root_type, file_events, conn, gandalf, periodic_scheduler, nucleus_bolt_client, restart_fn, safe_makedirs_fn, client_session_id, version_hint_fn, fsw_args, blocking_paths, shell_adapter, apex_context = None, boundary_thread_pool = None, periodic_metrics_reporter = None, set_connecting_engine_status_label_fn = (tuple,), linked_accounts_provider = ('account', 'AccountInterface', 'local_config', 'LocalConfigurationInterface', 'sync_root_type', 'SyncRootType', 'file_events', 'FileEvents', 'conn', 'DropboxConnection', 'gandalf', 'Gandalf', 'periodic_scheduler', 'PeriodicScheduler', 'nucleus_bolt_client', 'NucleusBoltClient', 'restart_fn', 'Callable[[], None]', 'safe_makedirs_fn', 'Callable[[Text], None]', 'client_session_id', 'Optional[Text]', 'version_hint_fn', 'Callable[[AccountInterface, Text], None]', 'fsw_args', 'FSWManagerArgs', 'blocking_paths', 'List[LocalPath]', 'shell_adapter', 'MultiaccountShellAdapter', 'apex_context', 'ApexContext', 'boundary_thread_pool', 'MonitoredThreadPoolExecutor', 'periodic_metrics_reporter', 'PeriodicMetricsReporter', 'set_connecting_engine_status_label_fn', 'Callable[[bool], None]', 'linked_accounts_provider', 'Callable[[], Iterable[Account]]', 'return', 'SyncEngineClassicInterface')):
        pass
    # WARNING: Decompyle incomplete

    
    def make_sync_engine_util(self = None):
        return self._SyncEngineUtil()

    
    def make_file_system(self = None):
        return self._FileSystem()

    write_nucleus_fileid = (lambda local_path = None, fileid = None, filerev = staticmethod: FileSystem = FileSystemimport dropbox.sync_engine.file_system.file_systemfs = FileSystem()extra_attrs = extra_attrs_from_fileid_xattr(new_fileid_xattr())attr_handler = AttributesHandler(fs, ATTRS_WHITELIST_HARDCODED, ignore_finderinfo = False)fileid_in_bytes = map_fileid_to_ascii(fileid)# WARNING: Decompyle incomplete
)()


def make_test_factory():
    return SyncEngineFactory()

