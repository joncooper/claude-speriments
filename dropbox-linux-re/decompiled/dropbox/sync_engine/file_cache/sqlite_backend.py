# Source Generated with Decompyle++
# File: sqlite_backend.pyc (Python 3.11)

from __future__ import absolute_import
import contextlib
import functools
import itertools
import pprint
import sqlite3
import sys
import time
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Text, Tuple, Union
from six import iteritems, reraise
from six.moves import map as imap, zip as izip
from constants import SyncType
from datatypes.file_cache_entry import FileCacheEntry, MutableFileCacheEntry
from datatypes.hashed_details import HashedDetails
from datatypes.infinite_details import InfiniteDetails
from datatypes.list_details import ListDetails
from datatypes.updated_details import UpdatedDetails
from reassociate_on_conflict import CONFIG_REASSOCIATE_ON_CONFLICT, ReassociateOnConflict
from constants import CONFIG_VERSION
from schema.latest import TABLE_DEFS, TABLE_DEFS_VERSION
from types import ConflictType, ExtraPendingDetails, MountRequest, NSMetadata, PendingParentDetails
from util import check_db_entries, clear_extra_pending_details, db_has_parent, db_infinite_details_kind, db_no_data_plat, db_parent_dir, db_parent_size, db_parent_sjid, FlushBefore, highest_sjid_selector_full_machineid, highest_sjid_selector_machineid_attr, is_valid_filejournal_entry, local_details_from_entry, MachineIdDict, most_recent_date_selector, RECONSTRUCT_DETAILS_TO_UPDATED_DETAILS, server_path_descendants_sql_predicate, serverpath_to_sqlite, set_local_fileid_info_on_row, set_local_fileid_on_row, set_parent_fileid_info_on_pending_row, sqlite_to_serverpath, why_isnt_valid_filejournal_entry
from dropbox.assertions import assert_
from dropbox.attrs import Attributes
from dropbox.client_api.hashing import DROPBOX_HASH_LENGTH, split_blocklist
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import DB_MIGRATION_EVENT
from dropbox.exception.exception_decorators import handle_exceptions, handle_exceptions_ex_2, handle_exceptions_ex_3
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.fastdetails import FastDetails
from dropbox.functions import frozendict, make_bytes, make_str
from dropbox.infinite import infinite_platform_supported
from dropbox.shared.server_path import MRLowerServerPath, ServerPath
from dropbox.shared.util import container, db_lower, wrap_tuple
from dropbox.sqlite3_helpers import create_tables, Cursor, dict_like_row, enable_converters, from_db_type, get_tables, just_the_first, MutableFileCacheEntry as sqlite_MutableFileCacheEntry, row_factory, sqlite3_get_table_entries, sqlite3_get_table_entries_with_no_in_clause, SqliteConnectionHub, to_db_type, unique_in_memory_database_uri, using_row_factory
from dropbox.trace import is_debugging, TRACE
CONFIG_ATTRS = 'attrs'
CONFIG_FILETYPE = 'filetype'

def _entries_debugging(entries_iterable):
    pass
# WARNING: Decompyle incomplete


class FileJournalRowLogic(object):
    IS_NORMAL = 0
    IS_PARENT = 0x40000000000
    IS_ATTRS = 0x80000000000
    INSERT_SQL = ','.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(FileCacheEntry.UPDATED_MIRRORED_FIELDS()) + ')'
    UPDATE_SQL = ','.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(itertools.chain(FileCacheEntry.LOCAL_MIRRORED_FIELDS, FileCacheEntry.UPDATED_MIRRORED_FIELDS)()) + ',force_reconstruct = :force_reconstruct ,extra_pending_details = :extra_pending_details ,local_ctime = :local_ctime ,local_infinite_details = :local_infinite_details WHERE server_path = :server_path'
    DELETE_SQL = 'DELETE FROM file_journal WHERE id = ?'
    RECOMMENDED_BATCH_SIZE = 500
    
    def __init__(self, mount_points):
        self.to_remove_hash_ref = set()
        self.to_add_hash_ref = set()
        self.to_insert = []
        self.to_update = []
        self.to_delete = []
        self.mount_table = (lambda .0: pass# WARNING: Decompyle incomplete
)(mount_points())
        self.server_paths_inserting = set()
        self.new_sp_to_fileid = []
        self.dead_sp_to_fileid = []
        self.new_unreconstructable = []
        self.dead_unreconstructable = []
        self.deleted_fileids = []
        self.new_extra_metadata_transient = []
        self.new_extra_metadata_persistent = []
        self.dead_extra_metadata = []
        self.dead_in_progress_reconstruct = []

    
    def _create_accessor(col = 'INSERT INTO file_journal (' + ','.join(itertools.chain([
        'server_path',
        'parent_path',
        'local_ctime',
        'local_infinite_details',
        'extra_pending_details',
        'force_reconstruct'], FileCacheEntry.LOCAL_MIRRORED_FIELDS, FileCacheEntry.UPDATED_MIRRORED_FIELDS)) + ') VALUES (' + ':server_path,:parent_path,:local_ctime,:local_infinite_details,' + ':extra_pending_details,:force_reconstruct,'):
        pass
    # WARNING: Decompyle incomplete

    _get_updated_host_id = _create_accessor('updated_host_id')
    _get_local_host_id = _create_accessor('local_host_id')
    _get_updated_timestamp = _create_accessor('updated_timestamp')
    _get_local_timestamp = _create_accessor('local_timestamp')
    _get_updated_user_id = _create_accessor('updated_user_id')
    _get_local_user_id = _create_accessor('local_user_id')
    _get_local_fileid = _create_accessor('local_fileid')
    _get_local_fileid_rev = _create_accessor('local_fileid_rev')
    _get_updated_fileid = _create_accessor('updated_fileid')
    _get_updated_fileid_rev = _create_accessor('updated_fileid_rev')
    _get_parent_fileid = _create_accessor('parent_fileid')
    _get_parent_fileid_rev = _create_accessor('parent_fileid_rev')
    _get_local_fileid_parent_fileid = _create_accessor('local_fileid_parent_fileid')
    _get_local_fileid_parent_fileid_rev = _create_accessor('local_fileid_parent_fileid_rev')
    _get_local_fileid_parent_fileid_type = _create_accessor('local_fileid_parent_fileid_type')
    del _create_accessor
    _get_machineid = (lambda row: pass# WARNING: Decompyle incomplete
)()
    _get_parent_machineid = (lambda row: pass# WARNING: Decompyle incomplete
)()
    
    def __len__(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)((self.to_insert, self.to_update, self.to_delete, self.to_add_hash_ref, self.to_remove_hash_ref)())

    column_default = (lambda col_name = staticmethod: if col_name == 'reassociate_flag':
0if None == 'unreconstructable':
False)()
    clear_updated_details = (lambda cls = None, ent = None: pass# WARNING: Decompyle incomplete
)()
    set_updated_details = (lambda cls = None, ent = None, deets = classmethod: MutableFileCacheEntry.set_updated_details(ent, deets))()
    revert_to_parent = (lambda cls, ent, parent_details, mtime, ctime, local_filename, infinite_details, machineid, fileid, fileid_rev: ent['local_blocklist'] = parent_details.blocklistent['local_size'] = parent_details.sizeent['local_dir'] = parent_details.dirent['local_sjid'] = parent_details.sjident['local_attrs'] = parent_details.attrsent['local_mtime'] = mtimeent['local_ctime'] = ctimeent['local_filename'] = local_filenameent['local_host_id'] = parent_details.host_ident['local_timestamp'] = parent_details.timestampent['local_user_id'] = parent_details.user_ident['local_sync_type'] = parent_details.sync_typeent['local_infinite_details'] = infinite_detailsent['local_folder_policy'] = parent_details.folder_policyent['conflict_type'] = Noneent['reassociate_flag'] = 0clear_extra_pending_details(ent)set_local_fileid_on_row(ent, local_fileid = fileid, local_fileid_rev = fileid_rev)ent['machineid_volumeid'] = machineid[0]ent['machineid_inode'] = machineid[1]ent['machineid_attr'] = machineid[2])()
    clear_local_details = (lambda cls = None, ent = classmethod: pass# WARNING: Decompyle incomplete
)()
    copy_synced_local_details = (lambda cls = None, from_ent = None, to_ent = classmethod: pass# WARNING: Decompyle incomplete
)()
    set_pending_details = (lambda cls, ent, deets, local_fileid = None, local_fileid_rev = None, local_fileid_parent_fileid = classmethod, local_fileid_parent_fileid_rev = (None, None, None, None, None), local_fileid_parent_fileid_type = ('deets', 'HashedDetails', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    move_updated_to_local = (lambda cls, newent: for local_name, updated_name in izip(FileCacheEntry.LOCAL_MIRRORED_FIELDS, FileCacheEntry.UPDATED_MIRRORED_FIELDS):
if updated_name == 'updated_filename':
continueif updated_name in ('updated_host_id', 'updated_timestamp', 'updated_user_id'):
newent[local_name] = newent.get(updated_name)else:
newent[local_name] = newent[updated_name]newent[updated_name] = Noneif not newent['local_sync_type'] == SyncType.PLACEHOLDER and newent['local_dir']:
newent['local_infinite_details'] = InfiniteDetails(ns = ServerPath(newent['server_path']).ns, sjid = newent['local_sjid'])else:
newent['local_infinite_details'] = Nonenewent['local_folder_policy'] = newent['updated_folder_policy']newent['updated_folder_policy'] = Noneset_local_fileid_on_row(newent, local_fileid = newent.get('updated_fileid'), local_fileid_rev = newent.get('updated_fileid_rev'))newent['updated_fileid'] = Nonenewent['updated_fileid_rev'] = Noneclear_extra_pending_details(newent)# WARNING: Decompyle incomplete
)()
    queue_force_reconstruct = (lambda ent = None, details = classmethod: pass# WARNING: Decompyle incomplete
)()
    needs_machineid_reconstruct = (lambda ent, new_details: if new_details.size < 0:
FalseNone in (ent['machineid_volumeid'], ent['machineid_inode']))()
    
    def _assert_hash(self, _hash):
        pass
    # WARNING: Decompyle incomplete

    
    def _add_hash_ref(self, _hash, server_path, how):
        self._assert_hash(_hash)
        toadd = (how, make_str(_hash), server_path)
        
        try:
            self.to_remove_hash_ref.remove(toadd)
            return None
        except KeyError:
            self.to_add_hash_ref.add(toadd)
            return None


    
    def _remove_hash_ref(self, _hash, server_path, how):
        self._assert_hash(_hash)
        toadd = (how, make_str(_hash), server_path)
        
        try:
            self.to_add_hash_ref.remove(toadd)
            return None
        except KeyError:
            self.to_remove_hash_ref.add(toadd)
            return None


    
    def hashes_added(self):
        return self.new_hashes

    
    def hashes_removed(self):
        return self.dead_hashes

    
    def __repr__(self):
        return f'''FileJournalRowLogic(to_add_hash_ref={pprint.pformat(self.to_add_hash_ref)!s}, to_remove_hash_ref={pprint.pformat(self.to_remove_hash_ref)!s})'''

    _modify_block_refs = (lambda cls, single, row: for i, _hash in enumerate(split_blocklist(row['local_blocklist'])):
single(_hash, row['server_path'], i)if row['local_attrs']:
for _hash, ref in row['local_attrs'].get_blockrefs():
single(_hash, row['server_path'], cls.IS_ATTRS | ref)extra = row['extra_pending_details']if extra:
parent_details = extra.parentif parent_details:
for i, _hash in enumerate(split_blocklist(parent_details.blocklist)):
single(_hash, row['server_path'], cls.IS_PARENT | i)if parent_details.attrs:
for _hash, ref in parent_details.attrs.get_blockrefs():
single(_hash, row['server_path'], cls.IS_ATTRS | cls.IS_PARENT | ref)NoneNoneNoneNone)()
    check_row = (lambda cls, row: pass# WARNING: Decompyle incomplete
)()
    
    def _remove_in_progress_reconstruct(self, row):
        self.dead_in_progress_reconstruct.append(row['server_path'])

    
    def _remove_extra_metadata(self, row):
        self.dead_extra_metadata.append((row['server_path'],))

    
    def _maybe_add_extra_metadata_refs(self, row, new_row):
        pass
    # WARNING: Decompyle incomplete

    
    def _remove_fileid_refs(self, row):
        self.dead_sp_to_fileid.append((row['server_path'],))

    
    def _add_fileid_refs(self, row):
        (machineid_volumeid, machineid_inode, machineid_attr) = self._get_machineid(row)
        (parent_machineid_volumeid, parent_machineid_inode, parent_machineid_attr) = self._get_parent_machineid(row)
        local_fileid = self._get_local_fileid(row)
        local_fileid_rev = self._get_local_fileid_rev(row)
        updated_fileid = self._get_updated_fileid(row)
        updated_fileid_rev = self._get_updated_fileid_rev(row)
        parent_fileid = self._get_parent_fileid(row)
        parent_fileid_rev = self._get_parent_fileid_rev(row)
        local_fileid_parent_fileid = self._get_local_fileid_parent_fileid(row)
        local_fileid_parent_fileid_rev = self._get_local_fileid_parent_fileid_rev(row)
        local_fileid_parent_fileid_type = self._get_local_fileid_parent_fileid_type(row)
    # WARNING: Decompyle incomplete

    
    def update_entry(self, old_row, new_row):
        pass
    # WARNING: Decompyle incomplete

    _get_synced_fileid_info_from_row = (lambda row: pass# WARNING: Decompyle incomplete
)()
    
    def _maybe_add_overwritten_entry_to_deleted_fileids(self, old_row, new_row):
        (old_volumeid, old_inode, old_attr, old_fileid, old_fileid_rev, old_sjid) = self._get_synced_fileid_info_from_row(old_row)
        (new_volumeid, new_inode, new_attr, new_fileid, new_fileid_rev, new_sjid) = self._get_synced_fileid_info_from_row(new_row)
    # WARNING: Decompyle incomplete

    _add_deleted_entry_to_deleted_fileids = (lambda self, row: pass# WARNING: Decompyle incomplete
)()
    
    def delete_entry(self, old_row):
        self.check_row(old_row)
        if old_row['local_sync_type'] == SyncType.NORMAL:
            self._modify_block_refs(self._remove_hash_ref, old_row)
        self.to_delete.append((old_row['id'],))
        self._remove_fileid_refs(old_row)
        self._remove_in_progress_reconstruct(old_row)
        self._remove_extra_metadata(old_row)
        self._add_deleted_entry_to_deleted_fileids(old_row)
        self.server_paths_inserting.discard(old_row['server_path'])
        if old_row.get('unreconstructable'):
            self.dead_unreconstructable.append(old_row['server_path'])
        return self

    
    def insert_entry(self, new_row):
        pass
    # WARNING: Decompyle incomplete

    
    def execute_da_sql(self, cursor):
        pass
    # WARNING: Decompyle incomplete

    
    def _sqlite_params_from_entries(self = classmethod, ents = staticmethod):
        ent_dicts = []
    # WARNING: Decompyle incomplete



class SQLiteBackendCursor(Cursor):
    pass
# WARNING: Decompyle incomplete


class SQLiteBackend(object):
    VERSION = SQLiteBackendCursor.VERSION
    FILETYPE = SQLiteBackendCursor.FILETYPE
    _sqlite_init = (lambda cls: converters = [
('ATTRIBUTETEXT', Attributes.unmarshal),
('PENDINGDETAILS2', ExtraPendingDetails.unmarshal),
('INFINITEDETAILS', InfiniteDetails.unmarshal),
('BYTETEXT', make_bytes),
('SERVERPATH', sqlite_to_serverpath),
('HASHEDDETAILS', HashedDetails.unmarshal)]adapters = [
(ServerPath, serverpath_to_sqlite),
(HashedDetails, HashedDetails.marshal)]enable_converters(converters, adapters = adapters))()
    
    def sqlite_cursor(self):
        return self.connhub.conn().cursor()

    
    def create_database_functions(self, conn):
        pass
    # WARNING: Decompyle incomplete

    cls_cursor = (lambda cls, conn: conn.cursor(SQLiteBackendCursor))()
    cls_get_config_key = (lambda cls, key, cursor: cls.cls_cursor(cursor.connection).get_config_key(key))()
    cls_set_config_key = (lambda cls, key, value, cursor: cls.cls_cursor(cursor.connection).set_config_key(key, value))()
    cls_get_mount_points = (lambda cls, cursor: cls.cls_cursor(cursor.connection).get_mount_points())()
    cls_get_mount_points_info = (lambda cls, cursor: cls.cls_cursor(cursor.connection).get_mount_points_info())()
    cls_get_namespace_attributes = (lambda cls, cursor: cls.cls_cursor(cursor.connection).get_namespace_attributes())()
    cls_get_server_mount_table_entries = (lambda cls, cursor: cursor = cls.cls_cursor(cursor.connection)cursor.get_server_mount_table_entries())()
    cls_last_revisions = (lambda cls, cursor: cls.cls_cursor(cursor.connection).last_revisions())()
    
    def __init__(self, fc, database_file, keystore, trevor, _check_latest = (None, None, True)):
        self._sqlite_init()
        self.fc = fc
    # WARNING: Decompyle incomplete

    
    def close(self):
        
        try:
            ch = self.connhub
            ch.close()
            return None
        except AttributeError:
            return None


    get_entries_by_mtime = (lambda cls, cursor, start_sp, start_mtime, end_mtime, limit: curs = cursor.connection.cursor(SQLiteBackendCursor)curs.get_entries_by_mtime(start_sp, start_mtime, end_mtime, limit))()
    _get_entries = (lambda cls, cursor, server_paths_iterable, lower = (False,): curs = cursor.connection.cursor(SQLiteBackendCursor)curs.get_entries(server_paths_iterable, lower = lower))()
    transaction_from_conn = (lambda cls, conn, on_commit_callbacks, on_rollback_callbacks = (None, None): pass# WARNING: Decompyle incomplete
)()()
    
    def transaction(self, on_commit_callbacks, on_rollback_callbacks = (None, None)):
        conn = self.connhub.conn()
        return self.transaction_from_conn(conn, on_commit_callbacks = on_commit_callbacks, on_rollback_callbacks = on_rollback_callbacks)

    migrate_path = (lambda cls, path, keystore, data_plats, server_conn, trevor, config = (None, None): pass# WARNING: Decompyle incomplete
)()

