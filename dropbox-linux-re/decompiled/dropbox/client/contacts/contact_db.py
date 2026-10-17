# Source Generated with Decompyle++
# File: contact_db.pyc (Python 3.11)

from __future__ import absolute_import
import json
import sqlite3
from collections import namedtuple
from typing import Any, Callable, cast, Dict, List, Optional, Text, Tuple
from dropbox.client.bolt.types import BoltToken, BoltUniqueID
from dropbox.client.contacts.polaris.types import ContactLocalMetadata, ContactType
from dropbox.exception.reporting import report_bad_assumption, report_rare_event
from dropbox.functions import make_unicode
from dropbox.shared.util import safe_navigate
from dropbox.shared.validated_record import ValidatedRecord
from dropbox.sqlite3_definitions import insert_values_for_record_sqlite_columns, SQLiteValidatedColumn, SQLiteValidatedTable
from dropbox.sqlite3_helpers import Cursor, VersionedSqlite3Cache
from dropbox.trace import TRACE
CONTACTS_READ_LIMIT = 100000
LightweightCacheEntry = namedtuple('LightweightCacheEntry', 'display_name contact_value is_same_team dropbox_id photo_url is_directory_restricted contact_type member_count is_member sort_key')
MIGRATION_SERVER_DIGEST = 'MIGRATIONDIGEST'

class ContactsDB(VersionedSqlite3Cache):
    pass
# WARNING: Decompyle incomplete


class DropboxContactLocalMetaRecord(ValidatedRecord):
    dropbox_id = cast(Text, SQLiteValidatedColumn('dropbox_id', Text, primary = True))
    pinned = cast(bool, SQLiteValidatedColumn('pinned', bool, nullable = True))
    dismissed = cast(bool, SQLiteValidatedColumn('dismissed', bool, nullable = True))
    user_info = cast(Text, SQLiteValidatedColumn('user_info', Text, nullable = True))
    extra = cast(Text, SQLiteValidatedColumn('extra', Text, nullable = True))


def DropboxContactLocalMetaTable():
    '''DropboxContactLocalMetaTable'''
    pass
# WARNING: Decompyle incomplete

DropboxContactLocalMetaTable = <NODE:27>(DropboxContactLocalMetaTable, 'DropboxContactLocalMetaTable', SQLiteValidatedTable[DropboxContactLocalMetaRecord])
