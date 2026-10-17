# Source Generated with Decompyle++
# File: sync_history_db.pyc (Python 3.11)

import os
import sqlite3
from contextlib import contextmanager
from enum import StrEnum
from typing import Any, Callable, cast, Iterator, List, Optional, Sequence
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.singleton import UserSingleton
from dropbox.foundation.context.user import UserContext
from dropbox.model.types import FileId
from dropbox.shared.validated_record import ValidatedRecord
from dropbox.sqlite3_definitions import insert_values_for_records_sqlite_columns, SQLiteValidatedColumn, SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor, locked_and_handled_1, locked_and_handled_2_default_return_none, VersionedSqlite3Cache
from dropbox.trace import TRACE

class DBSyncEventType(StrEnum):
    FILE = 'file'
    DIRECTORY = 'directory'


class FileEventType(StrEnum):
    ADD = 'add'
    EDIT = 'edit'
    DELETE = 'delete'
    MOVE = 'move'


class Direction(StrEnum):
    UP = 'upload'
    DOWN = 'download'


class SyncHistoryRecord(ValidatedRecord):
    event_type = cast(DBSyncEventType, SQLiteValidatedColumn('event_type', DBSyncEventType))
    file_event_type = cast(FileEventType, SQLiteValidatedColumn('file_event_type', FileEventType))
    direction = cast(Direction, SQLiteValidatedColumn('direction', Direction))
    file_id = cast(FileId, SQLiteValidatedColumn('file_id', str))
    local_path = cast(str, SQLiteValidatedColumn('local_path', str))
    timestamp = cast(int, SQLiteValidatedColumn('timestamp', int))
    other_user = cast(Optional[bool], SQLiteValidatedColumn('other_user', bool, nullable = True))
    server_path = cast(Optional[str], SQLiteValidatedColumn('server_path', str, nullable = True))


class SyncHistoryDB(UserSingleton, VersionedSqlite3Cache):
    pass
# WARNING: Decompyle incomplete


def SyncHistoryTable():
    '''SyncHistoryTable'''
    pass
# WARNING: Decompyle incomplete

SyncHistoryTable = <NODE:27>(SyncHistoryTable, 'SyncHistoryTable', SQLiteValidatedTable[SyncHistoryRecord])
