# Source Generated with Decompyle++
# File: url_asset_table.pyc (Python 3.11)

from __future__ import absolute_import
from typing import cast, Text
from dropbox.shared.validated_record import ValidatedRecord
from dropbox.sqlite3_definitions import insert_values_for_record_sqlite_columns, SQLiteValidatedColumn, SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor

class URLAssetRecord(ValidatedRecord):
    url = cast(Text, SQLiteValidatedColumn('url', Text, primary = True))
    asset_data = cast(bytes, SQLiteValidatedColumn('asset_data', bytes))
    created_time = cast(int, SQLiteValidatedColumn('created_time', int))
    size = cast(int, SQLiteValidatedColumn('size', int))


def URLAssetTable():
    '''URLAssetTable'''
    pass
# WARNING: Decompyle incomplete

URLAssetTable = <NODE:27>(URLAssetTable, 'URLAssetTable', SQLiteValidatedTable[URLAssetRecord])
