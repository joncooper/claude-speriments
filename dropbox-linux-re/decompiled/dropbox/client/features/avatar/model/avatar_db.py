# Source Generated with Decompyle++
# File: avatar_db.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import sqlite3
from contextlib import contextmanager
from time import time as _time
from typing import Any, cast, Iterator, List, Optional, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.shared.validated_record import ValidatedRecord
from dropbox.sqlite3_definitions import insert_values_for_record_sqlite_columns, SQLiteValidatedColumn, SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor, VersionedSqlite3Cache
from dropbox.trace import TRACE

class AvatarItem(ValidatedRecord):
    account_id = cast(Text, SQLiteValidatedColumn('account_id', Text, unique = True))
    avatar = cast(Text, SQLiteValidatedColumn('avatar', Text, nullable = True))
    fetch_ts = cast(int, SQLiteValidatedColumn('fetch_ts', int))
    use_ts = cast(int, SQLiteValidatedColumn('use_ts', int))


def AvatarItemsTable():
    '''AvatarItemsTable'''
    pass
# WARNING: Decompyle incomplete

AvatarItemsTable = <NODE:27>(AvatarItemsTable, 'AvatarItemsTable', SQLiteValidatedTable[AvatarItem])

class _AvatarDb(VersionedSqlite3Cache):
    pass
# WARNING: Decompyle incomplete


class AvatarDbActor(SingletonActor):
    pass
# WARNING: Decompyle incomplete

