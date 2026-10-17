# Source Generated with Decompyle++
# File: sqlite3_helpers.pyc (Python 3.11)

from __future__ import absolute_import
import binascii
import errno
import gc
import itertools
import os
import sqlite3
import sys
import threading
import time
from contextlib import contextmanager
from functools import wraps
from types import TracebackType
from typing import Any, Callable, cast, Dict, Generator, Iterable, Iterator, List, Mapping, Optional, overload, Text, Tuple, TypeVar, Union
from weakref import WeakValueDictionary
from mypy_extensions import NoReturn
from six import integer_types, reraise, string_types
from six.moves import cPickle as pickle, range
from build_number import is_frozen
from dropbox.assertions import assert_
from dropbox.callbacks import Handler
from dropbox.client.util import get_contents_root, get_repo_root_unfrozen
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.foundation.reporting import report_app_framework_event_restricted
from dropbox.functions import random_string
from dropbox.keystore import KeystoreMissingItem
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sqlite3_exceptions import ConnectionClosedError, CorruptedDBError, DatabaseOrDiskFullError, DisallowedFullTableScanError, DiskIOError, POSSIBLE_CORRUPTED_DB_EXCEPTIONS
from dropbox.threading import Lock, RLock, RWLock
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.client.util.mac import get_frameworks_dir
DISK_IO_ERROR_THRESHOLD = 5
DEFAULT_SELECT_LIMIT = 200
DISALLOW_FULL_TABLE_SCANS = False
MISNAMED_ENCRYPTED_DATABASES = [
    'browse_cache.db',
    'contacts_polaris.db',
    'contacts.db',
    'folder_preferences.db',
    'onboarding.db']

def get_sqlite_exc_message(exc_info):
    (exc_type, exc_val, exc_tb) = exc_info
    if exc_type in (sqlite3.DatabaseError, sqlite3.OperationalError, sqlite3.IntegrityError):
        if isinstance(exc_val, str):
            return exc_val
        
        try:
            return exc_val.args[0]
        except Exception:
            TRACE('Strange exc value: %r', exc_val)
            report_exception(component = DesktopComponent.DATABASES)
            return None
            return None



def enable_converters(converters = None, adapters = None):
    pass
# WARNING: Decompyle incomplete

_tracing_sql = False

def set_tracing_sql(tracing = None):
    global _tracing_sql
    _tracing_sql = tracing


class Savepoint(object):
    
    def __init__(self = None, cursor = None, name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def save(self = None):
        self._cursor.execute('SAVEPOINT {0}'.format(self.name))

    
    def release(self = None):
        self._cursor.execute('RELEASE SAVEPOINT {0}'.format(self.name))

    
    def rollback(self = None):
        self._cursor.execute('ROLLBACK TO SAVEPOINT {0}'.format(self.name))

    
    def __enter__(self = None):
        self.save()
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, exc_tb = ('exc_type', 'Optional[type]', 'exc_value', 'Optional[BaseException]', 'exc_tb', 'Optional[TracebackType]', 'return', 'None')):
        self.release()



def _dump_diagnostic_info_about_path(path = None):
    pass
# WARNING: Decompyle incomplete


def _raise_better_operational_exception(hub = None, e = None, sql = None, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def Cursor():
    '''Cursor'''
    pass
# WARNING: Decompyle incomplete

Cursor = <NODE:27>(Cursor, 'Cursor', sqlite3.Cursor, Iterable[Any])

class Connection(sqlite3.Connection):
    pass
# WARNING: Decompyle incomplete


def _find_sqlite_ext():
    if IS_WINDOWS:
        target_name = 'dropbox_sqlite_ext'
    elif IS_MAC:
        target_name = 'libdropbox_sqlite_ext'
    elif IS_LINUX:
        target_name = 'libdropbox_sqlite_ext'
# WARNING: Decompyle incomplete


def load_sqlite_ext(conn = None):
    path = _find_sqlite_ext()
    conn.load_extension(path)


def connect(*n, **kw):
    kw.setdefault('factory', Connection)
# WARNING: Decompyle incomplete


class SqliteConnectionHub(object):
    
    def __init__(self = None, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.close_lock = RWLock()
        self.closed = False
        self._thread_local_storage = threading.local()
        self._all_conns = WeakValueDictionary()
        self.post_create = kwargs.pop('post_create', None)
        self.connection_string = self.args[0]
    # WARNING: Decompyle incomplete

    
    def close_thread_connection(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self.close_lock.acquire_write()
        
        try:
            self.closed = True
            self.close_lock.release_write()
        except:
            self.close_lock.release_write()

        self.close_thread_connection()
        self._thread_local_storage = None
        self.in_memory_keepalive_conn = None
        if sys.version_info >= (3, 11):
            gc.collect()
            return None

    
    def _create_conn(self = None):
        kwargs = self.kwargs
        keystore = kwargs.get('keystore')
    # WARNING: Decompyle incomplete

    
    def conn(self = None):
        self.close_lock
        if self.closed:
            raise ConnectionClosedError('Already closed!')
        conn = getattr(self._thread_local_storage, 'conn', None)
    # WARNING: Decompyle incomplete

    cursor = (lambda self: pass# WARNING: Decompyle incomplete
)()
    reuse_cursor = (lambda self = None, cursor = contextmanager: pass# WARNING: Decompyle incomplete
)()


def sqlite3_get_table_entries_with_no_in_clause(cursor, table, desired_columns, row_factory, conditions, order_by_column, limit, params = (None, sqlite3.Row, None, None, DEFAULT_SELECT_LIMIT, ())):
    pass
# WARNING: Decompyle incomplete


def sqlite3_get_table_entries(cursor, table, checked_column, column_iterable, select_limit, desired_columns, row_factory, extra_conditions, custom_query_fn = (None, None, sqlite3.Row, None, None)):
    pass
# WARNING: Decompyle incomplete

row_factory = (lambda cursor = None, row_factory = None: pass# WARNING: Decompyle incomplete
)()

def using_row_factory(row_factory_):
    pass
# WARNING: Decompyle incomplete

_row_factory = row_factory
buffer_type = memoryview
PINNED_PICKLE_PROTOCOL = 2

def to_db_type(value):
    pass
# WARNING: Decompyle incomplete


def from_db_type(value):
    if isinstance(value, bytes):
        
        try:
            return pickle.loads(value)
        except UnicodeDecodeError:
            return 
            return value



def is_corrupted_db_exception(exc_type, exc_val, exc_tb, tables, **kw):
