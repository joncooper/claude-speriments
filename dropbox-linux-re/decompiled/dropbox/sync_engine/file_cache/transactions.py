# Source Generated with Decompyle++
# File: transactions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import contextlib
import functools
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Sequence, TypeVar
from build_number import dropbox_version
from constants import SyncAttrs, SyncPolicy
from datatypes.file_cache_entry import FileCacheEntry, FileCacheEntryBase
from datatypes.pending_details import PendingDetails
from datatypes.synced_callback_details import SyncedCallbackDetails
from datatypes.updated_details import UpdatedDetails
from sqlite_backend import SQLiteBackend, SQLiteBackendCursor
from util import FlushBefore, is_edit, is_local_change, is_muted, is_sync_change, is_sync_policy_change
from dropbox.assertions import assert_
from dropbox.attrs import FrozenAttributes
from dropbox.callbacks import Handler
from dropbox.exception.reporting import report_bad_assumption
from dropbox.shared.server_path import MRLowerServerPath, ServerPath
from dropbox.trace import TRACE

class ReadTransaction(object):
    
    def __init__(self = None, backend_wrapper = None):
        self.backend_wrapper = backend_wrapper
        self.trans = None

    
    def flush_in_memory_state(self):
        pass

    
    def sqlite_cursor(self):
        return self.trans.sqlite_cursor()

    transaction = (lambda self: pass# WARNING: Decompyle incomplete
)()


class WriteTransaction(ReadTransaction):
    pass
# WARNING: Decompyle incomplete


class SQLiteBackendWrapper(object):
    
    def __init__(self, fc = None, backend = None, on_commit_callbacks = None, on_rollback_callbacks = ('fc', 'FileCache', 'backend', 'SQLiteBackend', 'on_commit_callbacks', 'Handler', 'on_rollback_callbacks', 'Handler', 'return', 'None')):
        self.fc = fc
        self.backend = backend
        self.on_commit_callbacks = on_commit_callbacks
        self.on_rollback_callbacks = on_rollback_callbacks

    
    def read_transaction(self):
        return ReadTransaction(self).transaction()

    
    def write_transaction(self):
        return WriteTransaction(self, self.on_commit_callbacks, self.on_rollback_callbacks).transaction()

    connhub = (lambda self: self.backend.connhub)()
    sqlite_cursor = (lambda self: self.backend.sqlite_cursor)()
    
    def close(self):
        self.backend.close()


