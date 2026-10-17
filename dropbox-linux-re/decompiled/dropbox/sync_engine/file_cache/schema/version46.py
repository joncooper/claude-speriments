# Source Generated with Decompyle++
# File: version46.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import sys
from six.moves import range
from constants import CONFIG_VERSION, DROPBOX_FOLDER_VOLUMEID
from migrations import check_for_empty_resource_forks, clear_jan_2015_consistency_checker, clear_reconstruct_in_progress_migration, forums_entries_without_machineids_migration
from  import upgrade_single_version
from dropbox.sjid_format import assert_packed_sjid, internal_packed_to_client_sjid
from dropbox.sqlite3_helpers import create_tables
from dropbox.trace import TRACE
TABLE_DEFS = [
    ('file_journal', [
        ('id', 'INTEGER PRIMARY KEY NOT NULL'),
        ('server_path', 'TEXT NOT NULL UNIQUE'),
        ('parent_path', 'TEXT NOT NULL'),
        ('extra_pending_details', 'PENDINGDETAILS2'),
        ('force_reconstruct', 'INTEGER CHECK (force_reconstruct=1)'),
        ('local_sjid', 'INTEGER'),
        ('local_host_id', 'INTEGER'),
        ('local_filename', 'TEXT'),
        ('local_blocklist', 'BYTETEXT'),
        ('local_size', 'INTEGER'),
        ('local_mtime', 'INTEGER'),
        ('local_ctime', 'INTEGER'),
        ('local_dir', 'INTEGER'),
        ('local_attrs', 'ATTRIBUTETEXT'),
        ('local_timestamp', 'INTEGER'),
        ('local_user_id', 'INTEGER'),
        ('local_is_infinite', 'INTEGER CHECK (local_is_infinite IN (0, 1))'),
        ('updated_sjid', 'INTEGER'),
        ('updated_host_id', 'INTEGER'),
        ('updated_filename', 'TEXT'),
        ('updated_blocklist', 'BYTETEXT'),
        ('updated_size', 'INTEGER'),
        ('updated_mtime', 'INTEGER'),
        ('updated_dir', 'INTEGER'),
        ('updated_timestamp', 'INTEGER'),
        ('updated_user_id', 'INTEGER'),
        ('updated_attrs', 'ATTRIBUTETEXT'),
        ('updated_is_infinite', 'INTEGER CHECK (updated_is_infinite IN (0, 1))')], [], [
        ('sp', [
            'server_path']),
        ('ul', [
            'updated_sjid',
            'local_sjid']),
        ('pp', [
            'parent_path'])]),
    ('namespace_map', [
        ('ns', 'INTEGER PRIMARY KEY NOT NULL'),
        ('last_sjid', 'INTEGER NOT NULL'),
        ('list_cursor', 'TEXT'),
        ('list_dirs_cursor', 'TEXT')], [], []),
    ('mount_table', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('target_ns', 'INTEGER UNIQUE NOT NULL'),
        ('permissions', 'INTEGER'),
        ('properties', 'INTEGER DEFAULT NULL')], [], []),
    ('server_mount_table', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('target_ns', 'INTEGER NOT NULL'),
        ('local_state', 'INTEGER')], [], []),
    ('block_ref', [
        ('hash_id', 'INTEGER NOT NULL'),
        ('fj_id', 'INTEGER NOT NULL'),
        ('how', 'INTEGER NOT NULL')], [
        'PRIMARY KEY (hash_id, fj_id, how)'], []),
    ('block_cache', [
        ('id', 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'),
        ('hash', 'BYTETEXT NOT NULL UNIQUE')], [], [
        ('hash', [
            'hash'])]),
    ('config', [
        ('key', 'TEXT PRIMARY KEY NOT NULL'),
        ('value', 'BLOB')], [], []),
    ('conflicted', [
        ('con_server_path', 'TEXT PRIMARY KEY NOT NULL')], [], []),
    ('unreconstructable', [
        ('unrecon_server_path', 'TEXT PRIMARY KEY NOT NULL')], [], []),
    ('permission_conflicted', [
        ('permission_conflicted_server_path', 'TEXT PRIMARY KEY NOT NULL')], [], []),
    ('directory_add_hold', [
        ('root_relative_server_path', 'SERVERPATH NOT NULL PRIMARY KEY'),
        ('details', 'FASTDETAILS NOT NULL')], [], []),
    ('directory_delete_hold', [
        ('root_relative_server_path', 'SERVERPATH NOT NULL PRIMARY KEY'),
        ('details', 'FASTDETAILS NOT NULL')], [], []),
    ('file_journal_extra_metadata_transient', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('directory_not_empty_recommit', 'INTEGER DEFAULT 0')], [], []),
    ('file_journal_extra_metadata_persistent', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('reassociate_flag', 'INTEGER DEFAULT 0'),
        ('bundle_root', 'TEXT'),
        ('mount_transition_no_volumeid', 'INTEGER DEFAULT 0')], [], []),
    ('file_journal_reconstruct', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('reconstruct_sjid', 'INTEGER'),
        ('reconstruct_blocklist', 'BYTETEXT'),
        ('reconstruct_size', 'INTEGER'),
        ('reconstruct_dir', 'INTEGER'),
        ('reconstruct_attrs', 'ATTRIBUTETEXT'),
        ('reconstruct_host_id', 'INTEGER'),
        ('reconstruct_timestamp', 'INTEGER'),
        ('reconstruct_user_id', 'INTEGER'),
        ('reconstruct_fileid', 'BYTETEXT'),
        ('reconstruct_fileid_rev', 'INTEGER')], [], []),
    ('file_journal_fileid', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('local_fileid', 'BYTETEXT'),
        ('local_fileid_rev', 'INTEGER'),
        ('updated_fileid', 'BYTETEXT'),
        ('updated_fileid_rev', 'INTEGER'),
        ('machineid_inode', 'INTEGER'),
        ('machineid_volumeid', 'INTEGER'),
        ('machineid_attr', 'BYTETEXT'),
        ('parent_fileid', 'BYTETEXT'),
        ('parent_fileid_rev', 'INTEGER'),
        ('parent_machineid_inode', 'INTEGER'),
        ('parent_machineid_volumeid', 'INTEGER'),
        ('parent_machineid_attr', 'BYTETEXT'),
        ('local_fileid_parent_fileid', 'BYTETEXT'),
        ('local_fileid_parent_fileid_rev', 'INTEGER'),
        ('local_fileid_parent_fileid_type', 'INTEGER')], [], [
        ('fileid_attr_i', [
            'machineid_attr',
            'machineid_volumeid',
            'machineid_inode']),
        ('fileid_extra_attr_i', [
            'parent_machineid_attr',
            'parent_machineid_volumeid',
            'parent_machineid_inode'])]),
    ('deleted_fileids', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('machineid_inode', 'INTEGER'),
        ('machineid_volumeid', 'INTEGER'),
        ('machineid_attr', 'BYTETEXT'),
        ('fileid', 'BYTETEXT'),
        ('fileid_rev', 'INTEGER'),
        ('date_added', 'INTEGER'),
        ('is_conflicted', 'INTEGER')], [], [
        ('deleted_attr_i', [
            'machineid_attr',
            'machineid_volumeid',
            'machineid_inode'])]),
    ('backfill_namespace_map', [
        ('ns', 'INTEGER PRIMARY KEY NOT NULL'),
        ('list_cursor', 'TEXT'),
        ('version', 'INTEGER NOT NULL'),
        ('is_completed', 'INTEGER NOT NULL')], [], [])]

def _upgrade_27_to_28(trans):
    trans.set_config_key(CONFIG_VERSION, 28)


def _upgrade_28_to_29(trans):
    trans.execute('DROP TABLE IF EXISTS backfill_namespace_map')
    create_tables(trans, TABLE_DEFS, force = False)
    trans.set_config_key(CONFIG_VERSION, 29)


def _upgrade_29_to_30(trans):
    trans._add_column('file_journal_extra_metadata_persistent', 'mount_transition_no_volumeid', 'INTEGER DEFAULT 0')
    trans.set_config_key(CONFIG_VERSION, 30)


def _upgrade_30_to_31(trans, config):
    pass
# WARNING: Decompyle incomplete


def _upgrade_31_to_32(trans):
    trans.set_config_key(CONFIG_VERSION, 32)


def _upgrade_32_to_33(trans):
    forums_entries_without_machineids_migration(trans)
    trans.execute('DROP TABLE IF EXISTS backfill_namespace_map')
    create_tables(trans, TABLE_DEFS, force = False)
    trans.set_config_key(CONFIG_VERSION, 33)


def _upgrade_33_to_34(trans):
    trans._recreate_fileids_tables()
    trans.set_config_key(CONFIG_VERSION, 34)


def _upgrade_34_to_35(trans):
    trans.execute('DROP TABLE IF EXISTS backfill_namespace_map')
    create_tables(trans, TABLE_DEFS, force = False)
    trans.set_config_key(CONFIG_VERSION, 35)


def _upgrade_35_to_36(trans):
    
    def _db_rename_extra_ts_to_timestamp(extra_pending_details_str):
        if not extra_pending_details_str:
            return extra_pending_details_str
        extra = json.loads(extra_pending_details_str)
        if 'parent' in extra and 'ts' in extra['parent']:
            extra['parent']['timestamp'] = extra['parent'].pop('ts')
            return json.dumps(extra)

    trans.sqlite_cursor().connection.create_function('rename_extra_ts_to_timestamp', 1, _db_rename_extra_ts_to_timestamp)
    columns_to_add = [
        'local_host_id',
        'updated_host_id',
        'local_timestamp',
        'updated_timestamp',
        'local_user_id',
        'updated_user_id']
    for column in columns_to_add:
        trans._add_column('file_journal', column, 'INTEGER')
        trans.execute('\n        INSERT OR REPLACE INTO file_journal\n        (id, server_path, parent_path, extra_pending_details, local_sjid,\n         local_host_id, local_timestamp, local_user_id,\n         local_filename, local_blocklist, local_size, local_mtime, local_ctime,\n         local_dir, local_attrs, updated_sjid,\n         updated_host_id, updated_timestamp, updated_user_id,\n         updated_filename, updated_blocklist, updated_size, updated_mtime, updated_dir,\n         updated_attrs)\n\n        SELECT f.id,\n               f.server_path,\n               f.parent_path,\n               rename_extra_ts_to_timestamp(f.extra_pending_details),\n               f.local_sjid,\n               h1.host_id as local_host_id,\n               t1.timestamp as local_timestamp,\n               u1.user_id as local_user_id,\n               f.local_filename,\n               f.local_blocklist,\n               f.local_size,\n               f.local_mtime,\n               f.local_ctime,\n               f.local_dir,\n               f.local_attrs,\n               f.updated_sjid,\n               h2.host_id as updated_host_id,\n               t2.timestamp as updated_timestamp,\n               u2.user_id as updated_user_id,\n               f.updated_filename,\n               f.updated_blocklist,\n               f.updated_size,\n               f.updated_mtime,\n               f.updated_dir,\n               f.updated_attrs\n        FROM file_journal as f\n        LEFT JOIN host_id as h1\n            ON f.local_sjid=h1.sjid AND server_path_ns(f.server_path)=h1.ns_id\n        LEFT JOIN host_id as h2\n            ON f.updated_sjid=h2.sjid AND server_path_ns(f.server_path)=h2.ns_id\n        LEFT JOIN timestamp as t1\n            ON f.local_sjid=t1.sjid AND server_path_ns(f.server_path)=t1.ns_id\n        LEFT JOIN timestamp as t2\n            ON f.updated_sjid=t2.sjid AND server_path_ns(f.server_path)=t2.ns_id\n        LEFT JOIN user_id as u1\n            ON f.local_sjid=u1.sjid AND server_path_ns(f.server_path)=u1.ns_id\n        LEFT JOIN user_id as u2\n            ON f.updated_sjid=u2.sjid AND server_path_ns(f.server_path)=u2.ns_id\n    ')
        trans.execute('DROP TABLE host_id')
        trans.execute('DROP TABLE timestamp')
        trans.execute('DROP TABLE user_id')
        trans.set_config_key(CONFIG_VERSION, 36)
        return None


def _upgrade_36_to_37(trans):
    
    def _db_convert_extra_pending_sjids(extra_pending_details_str):
        if not extra_pending_details_str:
            return extra_pending_details_str
        extra = json.loads(extra_pending_details_str)
        if 'parent' in extra:
            assert_packed_sjid(extra['parent']['sjid'], 'ExtraPendingDetails sjid not valid!')
            extra['parent']['sjid'] = internal_packed_to_client_sjid(extra['parent']['sjid'])
            return json.dumps(extra)

    trans.sqlite_cursor().connection.create_function('convert_extra_pending_sjids', 1, _db_convert_extra_pending_sjids)
    countall = trans.execute('SELECT count(*) FROM file_journal').fetchone()[0]
    countvalid = trans.execute('SELECT count(*) FROM file_journal WHERE local_sjid IS NULL OR local_sjid in (0, 1) OR local_sjid >= (1 << 32) ').fetchone()[0]
    if countall != countvalid:
        invalid_paths = trans.execute('SELECT server_path, local_sjid FROM file_journal WHERE local_sjid IS NOT NULL AND local_sjid != 0 AND local_sjid != 1 AND local_sjid < (1 << 32)').fetchall()
        TRACE('Paths with invalid sjids: %r', invalid_paths)
        raise AssertionError('Found sjids outside of expected range')
    trans.execute('UPDATE file_journal SET local_sjid = ((local_sjid >> 32) << 1) WHERE local_sjid >= (1 << 32)')
    trans.execute('UPDATE file_journal SET updated_sjid = ((updated_sjid >> 32) << 1) WHERE updated_sjid >= (1 << 32)')
    trans.execute('UPDATE file_journal SET extra_pending_details = convert_extra_pending_sjids(extra_pending_details) WHERE extra_pending_details IS NOT NULL')
    trans.execute('UPDATE namespace_map SET last_sjid = ((last_sjid >> 32) << 1) WHERE last_sjid >= (1 << 32)')
    trans.set_config_key(CONFIG_VERSION, 37)


def _upgrade_37_to_38(trans):
    create_tables(trans, TABLE_DEFS, force = False)
    trans.set_config_key(CONFIG_VERSION, 38)


def _upgrade_38_to_39(trans):
    clear_reconstruct_in_progress_migration(trans)
    trans.set_config_key(CONFIG_VERSION, 39)


def _upgrade_39_to_40(trans):
    check_for_empty_resource_forks(trans)
    trans.set_config_key(CONFIG_VERSION, 40)


def _upgrade_40_to_41(trans):
    clear_jan_2015_consistency_checker(trans)
    trans.set_config_key(CONFIG_VERSION, 41)


def _upgrade_41_to_42(trans):
    create_tables(trans, TABLE_DEFS, force = False)
    trans.set_config_key(CONFIG_VERSION, 42)


def _upgrade_42_to_43(trans, from_version):
    if from_version == 42:
        raise AssertionError('Forcing resync during migration to DB v43')
    trans.set_config_key(CONFIG_VERSION, 43)


def _upgrade_43_to_44(trans):
    trans._add_column('mount_table', 'properties', 'INTEGER DEFAULT NULL')
    trans.set_config_key(CONFIG_VERSION, 44)


def _upgrade_44_to_45(trans):
    columns = [
        'local_is_infinite',
        'updated_is_infinite']
    for col in columns:
        trans._add_column('file_journal', col, 'INTEGER CHECK (%s IN (0, 1))' % col)
        trans.execute('\n        UPDATE file_journal\n        SET local_is_infinite = 0\n        WHERE local_sjid IS NOT NULL\n        ')
        trans.execute('\n        UPDATE file_journal\n        SET updated_is_infinite = 0\n        WHERE updated_sjid IS NOT NULL\n        ')
        trans.set_config_key(CONFIG_VERSION, 45)
        return None


def _upgrade_45_to_46(trans):
    trans._add_column('file_journal', 'force_reconstruct', 'INTEGER CHECK (force_reconstruct=1)')
    trans.execute('\n        UPDATE file_journal\n        SET force_reconstruct=\n            (SELECT (CASE fjemp.fileid_attr_reconstruct WHEN 1 THEN 1 ELSE NULL END)\n             FROM file_journal_extra_metadata_persistent AS fjemp\n             WHERE fjemp.server_path=file_journal.server_path)\n        WHERE EXISTS(SELECT *\n                     FROM file_journal_extra_metadata_persistent AS fjemp\n                     WHERE fjemp.server_path=file_journal.server_path)\n        ')
    trans._drop_column('file_journal_extra_metadata_persistent', 'fileid_attr_reconstruct')
    trans.set_config_key(CONFIG_VERSION, 46)


def upgrade(trans, from_version, to_version, **kwargs):
    for version in range(28, 46):
        args = ()
        if version == 30:
            args = (kwargs.get('config'),)
        elif version == 42:
            args = (from_version,)
        upgrade_fn = getattr(sys.modules[__name__], '_upgrade_%d_to_%d' % (version, version + 1))
        upgrade_single_version(trans, upgrade_fn, from_version, version, to_version, args)
        return None

