# Source Generated with Decompyle++
# File: sqlite3_exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import sqlite3
from dropbox.exception.exceptions import SuppressedExceptionMixin
from dropbox.exception.severity import Severity

class DropboxSqliteError(Exception):
    pass


class CorruptedDBError(DropboxSqliteError):
    pass


class MemoryCacheCorruptedDBError(DropboxSqliteError):
    pass


class ConnectionClosedError(DropboxSqliteError):
    _severity_class = Severity.TRACE


class DisallowedFullTableScanError(DropboxSqliteError):
    pass


class DatabaseOrDiskFullError(SuppressedExceptionMixin, DropboxSqliteError):
    _severity_class = Severity.TRACE


class DiskIOError(SuppressedExceptionMixin, DropboxSqliteError):
    _severity_class = Severity.TRACE

POSSIBLE_CORRUPTED_DB_EXCEPTIONS = (CorruptedDBError, sqlite3.DatabaseError, sqlite3.IntegrityError, sqlite3.OperationalError)
