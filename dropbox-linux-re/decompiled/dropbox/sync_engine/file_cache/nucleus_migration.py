# Source Generated with Decompyle++
# File: nucleus_migration.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import base64
import time
from typing import Callable, cast, Dict, Iterable, List, NamedTuple, Optional, Text, Tuple
from constants import SyncType
from file_system.constants import RESOURCE_FORK_XATTR
from file_cache import FileCache
from sqlite_backend import SQLiteBackendCursor
from transactions import ReadTransaction
from types import ExtraPendingDetails
from dropbox.attrs import Attributes
from dropbox.functions import batch, make_bytes
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import unicode_path as ServerPath_unicode_path
from dropbox.sjid_format import client_to_raw_sjid
from dropbox.sqlite3_helpers import VersionedSqlite3Cache
from dropbox.trace import TRACE
SnapshotMetadata = NamedTuple('SnapshotMetadata', [
    ('fileid', bytes),
    ('fileid_rev', Optional[int]),
    ('inode', int),
    ('machineid', Optional[bytes]),
    ('filename', Text),
    ('locally_synced_blocklist', bytes),
    ('locally_synced_size', int),
    ('locally_synced_resource_fork_blocklist', Optional[bytes]),
    ('locally_synced_resource_fork_size', Optional[int]),
    ('is_dir', bool),
    ('folder_policy', Optional[SyncType]),
    ('locally_synced_mtime', int),
    ('is_file', bool),
    ('is_synced', bool)])
MigrationFileJournalEntry = NamedTuple('MigrationFileJournalEntry', [
    ('server_path', Text),
    ('parent_path', Text),
    ('local_filename', Text),
    ('local_blocklist', bytes),
    ('local_size', int),
    ('local_attrs', Attributes),
    ('local_dir', int),
    ('extra_pending_details', Optional[ExtraPendingDetails]),
    ('local_fileid', bytes),
    ('local_fileid_rev', Optional[int]),
    ('machineid_inode', int),
    ('machineid_attr', Optional[bytes]),
    ('local_folder_policy', Optional[SyncType]),
    ('local_sjid', int),
    ('local_mtime', int),
    ('local_sync_type', int)])
MigrationFileCacheDump = NamedTuple('MigrationFileCacheDump', [
    ('path', str),
    ('number_of_entries', int),
    ('timed_out', bool)])

def safe_make_bytes(b):
    pass
# WARNING: Decompyle incomplete

SNAPSHOT_BATCH_SIZE = 10000
FCM_DB_NAME = 'filecache_migration.db'

class FilecacheNucleusMigrationManager(VersionedSqlite3Cache):
    pass
# WARNING: Decompyle incomplete

