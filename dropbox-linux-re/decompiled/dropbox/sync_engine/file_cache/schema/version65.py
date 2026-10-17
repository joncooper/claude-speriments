# Source Generated with Decompyle++
# File: version65.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import sys
from typing import Text
from six import iteritems
from six.moves import range
from constants import CONFIG_VERSION
from exceptions import ResyncRequiredMigrationException
from  import upgrade_single_version
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.shared.server_path import server_path_join_unicode, ServerPath
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
        ('local_sync_type', 'INTEGER'),
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
        ('updated_sync_type', 'INTEGER')], [], [
        ('sp', [
            'server_path']),
        ('ul', [
            'updated_sjid',
            'local_sjid']),
        ('pp', [
            'parent_path']),
        ('sjid_ns_idx', [
            'local_sjid',
            'server_path'])]),
    ('namespace_map', [
        ('ns', 'INTEGER PRIMARY KEY NOT NULL'),
        ('last_sjid', 'INTEGER NOT NULL'),
        ('list_cursor', 'TEXT'),
        ('list_dirs_cursor', 'TEXT')], [], []),
    ('mount_table', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('target_ns', 'INTEGER UNIQUE NOT NULL'),
        ('permissions', 'INTEGER'),
        ('properties', 'INTEGER DEFAULT NULL'),
        ('team_id', 'INTEGER DEFAULT NULL')], [], []),
    ('server_mount_table', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('target_ns', 'INTEGER NOT NULL')], [], []),
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
    ('unreconstructable', [
        ('unrecon_server_path', 'TEXT PRIMARY KEY NOT NULL')], [], []),
    ('directory_add_hold', [
        ('root_relative_server_path', 'SERVERPATH NOT NULL PRIMARY KEY'),
        ('details', 'HASHEDDETAILS NOT NULL')], [], []),
    ('directory_delete_hold', [
        ('root_relative_server_path', 'SERVERPATH NOT NULL PRIMARY KEY'),
        ('details', 'HASHEDDETAILS NOT NULL')], [], []),
    ('file_journal_extra_metadata_transient', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('directory_not_empty_recommit', 'INTEGER DEFAULT 0'),
        ('reconstruct_while_pending', 'INTEGER CHECK (reconstruct_while_pending > 0)')], [], []),
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
        ('reconstruct_fileid_rev', 'INTEGER'),
        ('reconstruct_sync_type', 'INTEGER')], [], []),
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
        ('is_completed', 'INTEGER NOT NULL')], [], []),
    ('sync_engine_features', [
        ('feature_name', 'TEXT PRIMARY KEY NOT NULL'),
        ('enabled', 'INTEGER NOT NULL'),
        ('last_modified_ts', 'INTEGER NOT NULL')], [], [])]

def _upgrade_46_to_47(trans):
    trans.execute('\n        UPDATE file_journal\n        SET local_sjid=updated_sjid\n        WHERE local_sjid=1 AND force_reconstruct=1\n        ')
    trans.execute('\n        UPDATE file_journal\n        SET force_reconstruct=1\n        WHERE updated_sjid=1 AND local_sjid=1 AND updated_size<0\n        ')
    NUM_TO_TRACE = 50
    BAD_ENTRY_CONDITION = 'local_sjid=1 AND force_reconstruct IS NULL'
    bad_entry_count = trans.execute('SELECT COUNT(*) FROM file_journal WHERE %s' % BAD_ENTRY_CONDITION).fetchone()[0]
# WARNING: Decompyle incomplete


def _upgrade_47_to_48(trans):
    trans._drop_column('server_mount_table', 'local_state')
    trans.set_config_key(CONFIG_VERSION, 48)


def _upgrade_48_to_49(trans):
    trans._add_column('file_journal_reconstruct', 'reconstruct_is_infinite', 'INTEGER NOT NULL DEFAULT 0 CHECK (reconstruct_is_infinite IN (0, 1))')
    trans.set_config_key(CONFIG_VERSION, 49)


def _upgrade_49_to_50(trans):
    trans.execute('CREATE INDEX IF NOT EXISTS sjid_ns_idx ON file_journal (local_sjid, server_path)')
    trans.set_config_key(CONFIG_VERSION, 50)


def _upgrade_50_to_51(trans):
    trans._add_column('file_journal_extra_metadata_transient', 'reconstruct_while_pending', 'INTEGER CHECK (reconstruct_while_pending > 0)')
    trans.execute('DROP TABLE conflicted')
    trans.execute('DROP TABLE permission_conflicted')
    trans.set_config_key(CONFIG_VERSION, 51)


def _upgrade_51_to_52(trans):
    trans.set_config_key(CONFIG_VERSION, 52)


def _upgrade_52_to_53(trans):
    pass
# WARNING: Decompyle incomplete


def _upgrade_53_to_54(trans):
    pass
# WARNING: Decompyle incomplete


def _upgrade_54_to_55(trans):
    for table in ('directory_add_hold', 'directory_delete_hold'):
        trans.execute('DELETE FROM %s' % table)
        trans._drop_column(table, 'details')
        trans._add_column(table, 'details', 'HASHEDDETAILS NOT NULL')
        trans.set_config_key(CONFIG_VERSION, 55)
        return None


def _upgrade_55_to_56(trans = None):
    pass


def _upgrade_56_to_57(trans = None):
    COUNT_INCONSISTENT_ENTRIES_SQL = '\n        SELECT COUNT(*)\n        FROM file_journal\n        JOIN file_journal_reconstruct USING (server_path)\n        WHERE updated_sjid IS NULL\n    '
    (num_inconsistent_rows,) = trans.execute(COUNT_INCONSISTENT_ENTRIES_SQL).fetchone()
    if num_inconsistent_rows > 0:
        report_rare_event('Found entries in file_journal with reconstruct-in-progress set and no updated side!')
        TRACE('%d entries with reconstruct-in-progress and no updated side.', num_inconsistent_rows)
    trans.set_config_key(CONFIG_VERSION, 57)


def _upgrade_57_to_58(trans):
    create_tables(trans, TABLE_DEFS, force = False)
    trans.set_config_key(CONFIG_VERSION, 58)


def _upgrade_58_to_59(trans = None):
    pass
# WARNING: Decompyle incomplete


def _upgrade_59_to_60(trans = None):
    exists_inconsistent_entries = trans.execute('\n        SELECT 1\n        FROM file_journal\n        JOIN file_journal_reconstruct USING (server_path)\n        WHERE updated_sjid IS NULL\n        LIMIT 1\n    ').fetchone()
# WARNING: Decompyle incomplete


def _upgrade_60_to_61(trans = None):
    trans._add_column('mount_table', 'team_id', 'INTEGER DEFAULT NULL')


def _upgrade_61_to_62(trans = None):
    pass


def _upgrade_62_to_63(trans = None):
    pass
# WARNING: Decompyle incomplete


def _upgrade_63_to_64(trans = None):
    
    def migrate_extra_pending_details_from_63_to_64(extra_pending_details_str):
        
        try:
            extra = json.loads(extra_pending_details_str)
            if 'previous_entry_status' in extra:
                extra.pop('previous_entry_status')
                return json.dumps(extra)
            return None
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_ENGINE)
            raise 


    trans.connection.create_function('migrate_extra_pending_details_from_63_to_64', 1, migrate_extra_pending_details_from_63_to_64)
    trans.execute('UPDATE file_journal SET extra_pending_details = migrate_extra_pending_details_from_63_to_64(extra_pending_details) WHERE local_sjid = 0')


def _upgrade_64_to_65(trans):
    _upgrade_62_to_63(trans)


def upgrade(trans, from_version, to_version):
    for version in range(46, 65):
        args = ()
        upgrade_fn = getattr(sys.modules[__name__], '_upgrade_%d_to_%d' % (version, version + 1))
        upgrade_single_version(trans, upgrade_fn, from_version, version, to_version, args)
        return None

