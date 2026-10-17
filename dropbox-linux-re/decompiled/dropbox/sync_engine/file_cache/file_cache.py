# Source Generated with Decompyle++
# File: file_cache.pyc (Python 3.11)

from __future__ import absolute_import
import contextlib
import sqlite3
import threading
from typing import Iterator, NamedTuple, Optional, Set
from sqlite_backend import SQLiteBackend
from transactions import ReadTransaction, SQLiteBackendWrapper, WriteTransaction
from dropbox import sqlite3_helpers
from dropbox.callbacks import Handler
from dropbox.exception.reporting import report_exception
SHARED_LOCK_PRIORITIZED_THREADS = set([
    'FILEACTION',
    'MainThread',
    'MOVE_TO_DROPBOX',
    'SCREENSHOTS_LISTENER',
    'SCREENSHOTS_PROCESSING',
    'SHMODEL_HANDLER',
    'STATUS',
    'USERNOTIFICATIONACTION'])
TransactionState = NamedTuple('TransactionState', [
    ('is_read', bool),
    ('read_trans', Optional[ReadTransaction]),
    ('write_trans', Optional[WriteTransaction])])

class FileCache:
    VERSION = SQLiteBackend.VERSION
    FILETYPE = SQLiteBackend.FILETYPE
    
    def __init__(self, database_file = None, keystore = None, infinite_stubfolders_enabled = None, infinite_cloud_docs_enabled = (None, False, False, True), symlink_filtering_enabled = ('return', 'None')):
        self.prevent_main_thread = False
        self.trans_local = threading.local()
        self.root_ns = None
        self.home_ns = None
        self.infinite_stubfolders_enabled = infinite_stubfolders_enabled
        self.infinite_cloud_docs_enabled = infinite_cloud_docs_enabled
        self.symlink_filtering_enabled = symlink_filtering_enabled
        self._internal_mount_table = None
        self._internal_server_mount_table = None
        on_commit_callbacks = Handler(recursive = False, handle_exc = report_exception)
        on_rollback_callbacks = Handler(recursive = False)
        self._rollback_exception_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_rollback_exception_callback = self._rollback_exception_callbacks.add_handler
        self.block_reference_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_block_reference_callback = self.block_reference_callbacks.add_handler
        self.remove_block_reference_callback = self.block_reference_callbacks.remove_handler
        self.remote_files_event_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_remote_files_event_callback = self.remote_files_event_callbacks.add_handler
        self.remove_remote_files_event_callback = self.remote_files_event_callbacks.remove_handler
        self.mount_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_mount_callback = self.mount_callbacks.add_handler
        self.remove_mount_callback = self.mount_callbacks.remove_handler
        self.synced_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_synced_files_callback = self.synced_callbacks.add_handler
        self.remove_synced_files_callback = self.synced_callbacks.remove_handler
        self.unreconstructable_files_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_unreconstructable_files_callback = self.unreconstructable_files_callbacks.add_handler
        self.remove_unreconstructable_files_callback = self.unreconstructable_files_callbacks.remove_handler
        self.unsyncable_roots_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.dropbox_root_changed_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_dropbox_root_changed_callback = self.dropbox_root_changed_callbacks.add_handler
        self.remove_dropbox_root_changed_callback = self.dropbox_root_changed_callbacks.remove_handler
        self.resolve_name_callbacks = Handler(recursive = False, handle_exc = report_exception)
        self.add_resolve_name_callback = self.resolve_name_callbacks.add_handler
        self.remove_resolve_name_callback = self.resolve_name_callbacks.remove_handler
        sqlite_backend = SQLiteBackend(self, database_file, keystore = keystore)
        
        try:
            self.backend = SQLiteBackendWrapper(self, sqlite_backend, on_commit_callbacks, on_rollback_callbacks)
        except Exception:
            sqlite_backend.close()
            raise 

        self._fake_deletes_blocked_by_list = True
        self._blocked_upload_ns_ids = set()
        self._can_create_confidential_nses = None

    lockless_transaction = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    read_transaction = lockless_transaction
    _acquire_trans = (lambda self = None, read_only = None: pass# WARNING: Decompyle incomplete
)()
    
    def close(self):
        self.backend.close()

    create_database_connection = (lambda cls, database_file: pass# WARNING: Decompyle incomplete
)()

