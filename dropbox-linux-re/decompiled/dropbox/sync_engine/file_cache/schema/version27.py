# Source Generated with Decompyle++
# File: version27.pyc (Python 3.11)

from __future__ import absolute_import
import sqlite3
import sys
from six.moves import range
from  import upgrade_single_version
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.sqlite3_helpers import create_tables
from dropbox.trace import TRACE
TABLE_DEFS = [
    ('file_journal', [
        ('id', 'INTEGER PRIMARY KEY NOT NULL'),
        ('server_path', 'TEXT NOT NULL UNIQUE'),
        ('parent_path', 'TEXT NOT NULL '),
        ('extra_pending_details', 'PENDINGDETAILS2'),
        ('local_sjid', 'INTEGER'),
        ('local_filename', 'TEXT'),
        ('local_blocklist', 'BYTETEXT'),
        ('local_size', 'INTEGER'),
        ('local_mtime', 'INTEGER'),
        ('local_ctime', 'INTEGER'),
        ('local_dir', 'INTEGER'),
        ('local_attrs', 'ATTRIBUTETEXT'),
        ('updated_sjid', 'INTEGER'),
        ('updated_filename', 'TEXT'),
        ('updated_blocklist', 'BYTETEXT'),
        ('updated_size', 'INTEGER'),
        ('updated_mtime', 'INTEGER'),
        ('updated_dir', 'INTEGER'),
        ('updated_attrs', 'ATTRIBUTETEXT')], [], [
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
        ('permissions', 'INTEGER')], [], []),
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
    ('host_id', [
        ('ns_id', 'INTEGER NOT NULL'),
        ('sjid', 'INTEGER NOT NULL'),
        ('host_id', 'INTEGER NOT NULL')], [
        'PRIMARY KEY (ns_id, sjid)'], []),
    ('timestamp', [
        ('ns_id', 'INTEGER NOT NULL'),
        ('sjid', 'INTEGER NOT NULL'),
        ('timestamp', 'INTEGER NOT NULL')], [
        'PRIMARY KEY (ns_id, sjid)'], []),
    ('user_id', [
        ('ns_id', 'INTEGER NOT NULL'),
        ('sjid', 'INTEGER NOT NULL'),
        ('user_id', 'INTEGER NOT NULL')], [
        'PRIMARY KEY (ns_id, sjid)'], []),
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
        ('fileid_attr_reconstruct', 'INTEGER DEFAULT 0'),
        ('reassociate_flag', 'INTEGER DEFAULT 0'),
        ('bundle_root', 'TEXT')], [], []),
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

def _upgrade_3_to_4(trans, data_plats, attrs_whitelist):
    trans.set_config_key('attrs_whitelist', dict(attrs_whitelist))
    trans.set_config_key('attrs_data_plats', list(data_plats))


def _upgrade_4_to_5(trans, server_conn = (None,)):
    create_tables(trans, TABLE_DEFS, force = False)
    if IS_WINDOWS:
        TRACE('Migration: Updating local_ctime column in file_journal')
        trans.execute('UPDATE file_journal SET local_ctime = local_mtime WHERE local_ctime != 0')
        return None


def _upgrade_5_to_6(trans):
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_6_to_7(trans):
    trans.execute('DROP TABLE IF EXISTS directory_hold')
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_7_to_8(trans):
    pass


def _upgrade_8_to_9(trans):
    
    try:
        trans.execute('ALTER TABLE mount_table ADD COLUMN permissions INTEGER')
    except sqlite3.OperationalError:
        pass

    create_permission_conflicted = '\n    CREATE TABLE IF NOT EXISTS permission_conflicted (\n        permission_conflicted_server_path TEXT PRIMARY KEY NOT NULL\n    )\n    '
    trans.execute(create_permission_conflicted)


def _upgrade_9_to_10(trans):
    trans.execute('DROP TABLE IF EXISTS guid_back_references')
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_10_to_11(trans):
    trans.execute('CREATE TABLE new_namespace_map (ns INTEGER PRIMARY KEY NOT NULL, last_sjid INTEGER NOT NULL)')
    trans.execute('INSERT INTO new_namespace_map (ns, last_sjid) SELECT ns, last_sjid FROM namespace_map')
    trans.execute('DROP TABLE namespace_map')
    trans.execute('ALTER TABLE new_namespace_map RENAME TO namespace_map')


def _upgrade_11_to_12(trans):
    trans.execute('DROP TABLE IF EXISTS file_journal_fileid')
    trans.execute('DROP TABLE IF EXISTS fileid_conflicted')
    trans.execute('DROP TABLE IF EXISTS deleted_fileids')
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_12_to_13(trans):
    trans.execute('ALTER TABLE namespace_map ADD COLUMN list_cursor TEXT')
    trans.execute('ALTER TABLE namespace_map ADD COLUMN list_dirs_cursor TEXT')


def _upgrade_13_to_14(trans):
    trans._recreate_fileids_tables()


def _upgrade_14_to_15(trans):
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_15_to_16(trans):
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_16_to_17(trans):
    trans._recreate_fileids_tables()


def _upgrade_17_to_18(trans):
    trans._recreate_fileids_tables()


def _upgrade_18_to_19(trans):
    trans._recreate_fileids_tables()


def _upgrade_19_to_20(trans):
    trans.execute('DROP TABLE IF EXISTS file_journal_guid')
    trans.execute('DROP TABLE IF EXISTS guid_journal')


def _upgrade_20_to_21(trans):
    trans.execute('DROP TABLE IF EXISTS deleted_fileids')
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_21_to_22(trans):
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_22_to_23(trans):
    if IS_MAC:
        trans.recreate_fileids_tables()
        return None


def _upgrade_23_to_24(trans):
    if 'reassociate_flag' in trans.get_columns('file_journal_extra_metadata_persistent'):
        TRACE('Found reassociate_flag column in file_journal_extra_metadata_persistent, not adding.')
        return None
    sql = None
    trans.execute(sql)


def _upgrade_24_to_25(trans):
    create_tables(trans, TABLE_DEFS, force = False)


def _upgrade_25_to_26(trans):
    if 'bundle_root' in trans.get_columns('file_journal_extra_metadata_persistent'):
        TRACE('Found bundle_root column in file_journal_extra_metadata_persistent, not adding.')
        return None
    sql = None
    trans.execute(sql)


def _upgrade_26_to_27(trans):
    if IS_MAC:
        UUID_TO_PERSISTENT_VOLUMEID_KEY = UUID_TO_PERSISTENT_VOLUMEID_KEY
        import constants
        trans.recreate_fileids_tables()
        trans.remove_config_key(UUID_TO_PERSISTENT_VOLUMEID_KEY)
        return None


def upgrade(trans, from_version, to_version, **kwargs):
    for version in range(3, 27):
        args = ()
        if version == 3:
            if not trans.get_config_key('attrs', None):
                config_attrs_whitelist = { }
                args = (kwargs.get('data_plats'), config_attrs_whitelist)
            elif version == 4:
                args = (kwargs.get('server_conn'),)
        upgrade_fn = getattr(sys.modules[__name__], '_upgrade_%d_to_%d' % (version, version + 1))
        upgrade_single_version(trans, upgrade_fn, from_version, version, to_version, args)
        return None

