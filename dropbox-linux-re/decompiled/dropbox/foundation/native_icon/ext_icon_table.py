# Source Generated with Decompyle++
# File: ext_icon_table.pyc (Python 3.11)

from __future__ import absolute_import
from typing import cast, Text
from dropbox.shared.validated_record import ValidatedRecord
from dropbox.sqlite3_definitions import insert_values_for_record_sqlite_columns, SQLiteValidatedColumn, SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor

class ExtensionIconRecord(ValidatedRecord):
    file_extension = cast(Text, SQLiteValidatedColumn('file_extension', Text, primary = True))
    image = cast(bytes, SQLiteValidatedColumn('image', bytes))
    created_time = cast(int, SQLiteValidatedColumn('created_time', int))


def ExtensionIconTable():
    '''ExtensionIconTable'''
    pass
# WARNING: Decompyle incomplete

ExtensionIconTable = <NODE:27>(ExtensionIconTable, 'ExtensionIconTable', SQLiteValidatedTable[ExtensionIconRecord])
