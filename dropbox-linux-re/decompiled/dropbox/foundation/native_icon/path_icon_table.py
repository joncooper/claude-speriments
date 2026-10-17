# Source Generated with Decompyle++
# File: path_icon_table.pyc (Python 3.11)

from __future__ import absolute_import
from typing import cast, Optional, Text
from dropbox.shared.validated_record import ValidatedRecord
from dropbox.sqlite3_definitions import insert_values_for_record_sqlite_columns, SQLiteValidatedColumn, SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor

class PathIconRecord(ValidatedRecord):
    file_path = cast(Text, SQLiteValidatedColumn('file_path', Text, primary = True))
    image = cast(bytes, SQLiteValidatedColumn('image', bytes))
    created_time = cast(int, SQLiteValidatedColumn('created_time', int))
    file_mtime = cast(int, SQLiteValidatedColumn('file_mtime', int, nullable = True))


def PathIconTable():
    '''PathIconTable'''
    pass
# WARNING: Decompyle incomplete

PathIconTable = <NODE:27>(PathIconTable, 'PathIconTable', SQLiteValidatedTable[PathIconRecord])
