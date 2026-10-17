# Source Generated with Decompyle++
# File: folder_icon_table.pyc (Python 3.11)

from __future__ import absolute_import
from typing import cast, Text
from dropbox.shared.validated_record import ValidatedRecord
from dropbox.sqlite3_definitions import insert_values_for_record_sqlite_columns, SQLiteValidatedColumn, SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor

class FolderIconRecord(ValidatedRecord):
    folder_tag = cast(Text, SQLiteValidatedColumn('folder_tag', Text, primary = True))
    image = cast(bytes, SQLiteValidatedColumn('image', bytes))
    created_time = cast(int, SQLiteValidatedColumn('created_time', int))


def FolderIconTable():
    '''FolderIconTable'''
    pass
# WARNING: Decompyle incomplete

FolderIconTable = <NODE:27>(FolderIconTable, 'FolderIconTable', SQLiteValidatedTable[FolderIconRecord])
