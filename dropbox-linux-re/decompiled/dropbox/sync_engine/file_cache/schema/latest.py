# Source Generated with Decompyle++
# File: latest.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import sys
from collections import defaultdict
from typing import Any, cast, Dict, Set, Text, Tuple
from build_number import dropbox_version
from six import iteritems
from six.moves import range
from constants import LACONIC_GRASSHOPPER_RECOVERY_NEEDED
from file_cache.util import server_path_descendants_sql_predicate
from exceptions import ResyncRequiredMigrationException
from  import upgrade_single_version
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import SYNC_ENGINE_MIGRATION_STATS_EVENT
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.shared.server_path import MRLowerServerPath, RRLowerServerPath, server_path_join_unicode, ServerPath
from dropbox.sqlite3_helpers import get_tables
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from sqlite_backend import SQLiteBackendCursor
TABLE_DEFS_VERSION: 'int' = 80
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
        ('local_blocklist', "BYTETEXT CHECK(local_blocklist IS NULL OR TYPEOF(local_blocklist) == 'text')"),
        ('local_infinite_details', 'INFINITEDETAILS'),
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
        ('updated_blocklist', "BYTETEXT CHECK(updated_blocklist IS NULL OR TYPEOF(updated_blocklist) == 'text')"),
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
            'server_path']),
        ('st_dir_sp_idx ', [
            'local_sync_type',
            'local_dir',
            'server_path'])]),
    ('namespace_map', [
        ('ns', 'INTEGER PRIMARY KEY NOT NULL'),
        ('last_sjid', 'INTEGER NOT NULL'),
        ('list_cursor', 'TEXT'),
        ('list_dirs_cursor', 'TEXT')], [], []),
    ('namespace_attributes', [
        ('ns', 'INTEGER PRIMARY KEY NOT NULL'),
        ('permissions', 'INTEGER'),
        ('properties', 'INTEGER DEFAULT NULL'),
        ('team_id', 'INTEGER DEFAULT NULL'),
        ('owner_id_hash', 'TEXT DEFAULT NULL')], [], []),
    ('mount_table', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('target_ns', 'INTEGER UNIQUE NOT NULL')], [], []),
    ('server_mount_table', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('target_ns', 'INTEGER NOT NULL'),
        ('permissions', 'INTEGER'),
        ('properties', 'INTEGER DEFAULT NULL'),
        ('team_id', 'INTEGER DEFAULT NULL'),
        ('owner_id_hash', 'TEXT DEFAULT NULL')], [], []),
    ('block_ref', [
        ('hash_id', 'INTEGER NOT NULL'),
        ('fj_id', 'INTEGER NOT NULL'),
        ('how', 'INTEGER NOT NULL')], [
        'PRIMARY KEY (hash_id, fj_id, how)'], []),
    ('block_cache', [
        ('id', 'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'),
        ('hash', "BYTETEXT NOT NULL UNIQUE CHECK(TYPEOF(hash) == 'text')")], [], [
        ('hash', [
            'hash'])]),
    ('config', [
        ('key', "TEXT PRIMARY KEY NOT NULL CHECK(TYPEOF(key) == 'text')"),
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
        ('mount_transition_no_volumeid', 'INTEGER DEFAULT 0'),
        ('local_folder_policy', 'INTEGER DEFAULT NULL'),
        ('updated_folder_policy', 'INTEGER DEFAULT NULL')], [], [
        ('lfp_sp_idx', [
            'local_folder_policy',
            'server_path'])]),
    ('file_journal_reconstruct', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('reconstruct_sjid', 'INTEGER'),
        ('reconstruct_blocklist', "BYTETEXT CHECK(reconstruct_blocklist IS NULL OR TYPEOF(reconstruct_blocklist) == 'text')"),
        ('reconstruct_size', 'INTEGER'),
        ('reconstruct_dir', 'INTEGER'),
        ('reconstruct_attrs', 'ATTRIBUTETEXT'),
        ('reconstruct_host_id', 'INTEGER'),
        ('reconstruct_timestamp', 'INTEGER'),
        ('reconstruct_user_id', 'INTEGER'),
        ('reconstruct_fileid', "BYTETEXT CHECK(reconstruct_fileid IS NULL OR TYPEOF(reconstruct_fileid) == 'text')"),
        ('reconstruct_fileid_rev', 'INTEGER'),
        ('reconstruct_sync_type', 'INTEGER')], [], []),
    ('file_journal_fileid', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('local_fileid', "BYTETEXT CHECK(local_fileid IS NULL OR TYPEOF(local_fileid) == 'text')"),
        ('local_fileid_rev', 'INTEGER'),
        ('updated_fileid', "BYTETEXT CHECK(updated_fileid IS NULL OR TYPEOF(updated_fileid) == 'text')"),
        ('updated_fileid_rev', 'INTEGER'),
        ('machineid_inode', 'INTEGER'),
        ('machineid_volumeid', 'INTEGER'),
        ('machineid_attr', "BYTETEXT CHECK(machineid_attr IS NULL OR TYPEOF(machineid_attr) == 'text')"),
        ('parent_fileid', "BYTETEXT CHECK(parent_fileid IS NULL OR TYPEOF(parent_fileid) == 'text')"),
        ('parent_fileid_rev', 'INTEGER'),
        ('parent_machineid_inode', 'INTEGER'),
        ('parent_machineid_volumeid', 'INTEGER'),
        ('parent_machineid_attr', "BYTETEXT CHECK(parent_machineid_attr IS NULL OR TYPEOF(parent_machineid_attr) == 'text')"),
        ('local_fileid_parent_fileid', "BYTETEXT CHECK(local_fileid_parent_fileid IS NULL OR TYPEOF(local_fileid_parent_fileid) == 'text')"),
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
    ('orphaned_placeholder_details', [
        ('machineid_attr', "BYTETEXT PRIMARY KEY NOT NULL CHECK(TYPEOF(machineid_attr) == 'text')"),
        ('machineid_volumeid', 'INTEGER'),
        ('machineid_inode', 'INTEGER'),
        ('placeholder_details', 'BYTETEXT')], [], []),
    ('deleted_fileids', [
        ('server_path', 'TEXT PRIMARY KEY NOT NULL'),
        ('machineid_inode', 'INTEGER'),
        ('machineid_volumeid', 'INTEGER'),
        ('machineid_attr', "BYTETEXT CHECK(machineid_attr IS NULL OR TYPEOF(machineid_attr) == 'text')"),
        ('fileid', "BYTETEXT CHECK(fileid IS NULL OR TYPEOF(fileid) == 'text')"),
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

def _upgrade_65_to_66(trans = None):
    trans.execute('CREATE INDEX IF NOT EXISTS st_sp_idx ON file_journal(local_sync_type, server_path)')


def _upgrade_66_to_67(trans = None):
    _upgrade_65_to_66(trans)


def _upgrade_67_to_68(trans = None):
    trans._add_column('file_journal_extra_metadata_persistent', 'local_folder_policy', 'INTEGER DEFAULT NULL')
    trans._add_column('file_journal_extra_metadata_persistent', 'updated_folder_policy', 'INTEGER DEFAULT NULL')
    local_folder_policy_case = 'CASE WHEN local_dir = 1 THEN local_sync_type ELSE NULL END'
    updated_folder_policy_case = 'CASE WHEN updated_dir = 1 THEN  updated_sync_type ELSE NULL END'
    trans.execute(f'''\n        UPDATE file_journal_extra_metadata_persistent SET\n        local_folder_policy = (\n            SELECT {local_folder_policy_case!s} AS local_folder_policy\n            FROM file_journal AS fj\n            WHERE fj.server_path = file_journal_extra_metadata_persistent.server_path\n        ), updated_folder_policy = (\n            SELECT {updated_folder_policy_case!s} AS updated_folder_policy\n            FROM file_journal AS fj\n            WHERE fj.server_path = file_journal_extra_metadata_persistent.server_path\n        )\n    ''')
    trans.execute(f'''\n        INSERT OR IGNORE\n        INTO file_journal_extra_metadata_persistent (server_path, local_folder_policy, updated_folder_policy)\n            SELECT server_path, {local_folder_policy_case!s} as local_folder_policy, {updated_folder_policy_case!s} AS updated_folder_policy\n            FROM file_journal\n            WHERE NOT (local_folder_policy IS NULL AND updated_folder_policy IS NULL)\n    ''')
    sync_types = {
        'normal': 1,
        'hidden': 2,
        'placeholder': 3 }
    trans.execute('\n        UPDATE file_journal SET\n        local_sync_type = %(normal)d\n        WHERE local_sync_type = %(placeholder)d AND local_dir = 1\n    ' % sync_types)
    trans.execute('\n        UPDATE file_journal SET\n        updated_sync_type = %(normal)d\n        WHERE updated_sync_type = %(placeholder)d AND updated_dir = 1\n    ' % sync_types)
    
    def migrate_extra_pending_details_from_67_to_68(is_dir = None, extra_pending_details = None):
        pass
    # WARNING: Decompyle incomplete

    trans.connection.create_function('migrate_extra_pending_details_from_67_to_68', 2, migrate_extra_pending_details_from_67_to_68)
    trans.execute('\n            UPDATE file_journal SET\n            extra_pending_details = migrate_extra_pending_details_from_67_to_68(local_dir, extra_pending_details)\n            WHERE local_sjid = 0\n        ')


def _upgrade_68_to_69(trans = None):
    trans.execute('DROP INDEX IF EXISTS st_sp_idx')
    trans.execute('CREATE INDEX IF NOT EXISTS st_dir_sp_idx ON file_journal(local_sync_type, local_dir, server_path)')
    trans.execute('CREATE INDEX IF NOT EXISTS lfp_sp_idx ON file_journal_extra_metadata_persistent(local_folder_policy, server_path)')


def _upgrade_69_to_70(trans = None):
    trans.execute('CREATE TABLE IF NOT EXISTS orphaned_placeholder_details (machineid_attr BYTETEXT PRIMARY KEY NOT NULL, machineid_volumeid INTEGER, machineid_inode INTEGER, placeholder_details BYTETEXT)')


def _upgrade_70_to_71(trans):
    pass


def _upgrade_71_to_72(trans = None):
    pass
# WARNING: Decompyle incomplete


def _upgrade_72_to_73(trans = None):
    trans._add_column('file_journal', 'local_infinite_details', 'INFINITEDETAILS')
    
    def migrate_infinite_details_from_72_to_73(server_path = None, local_sjid = None, extra_pending_details = None):
        pass
    # WARNING: Decompyle incomplete

    trans.connection.create_function('migrate_infinite_details_from_72_to_73', 3, migrate_infinite_details_from_72_to_73)
    trans.execute('\n        UPDATE file_journal SET\n        local_infinite_details = migrate_infinite_details_from_72_to_73(server_path, local_sjid, extra_pending_details)\n        WHERE local_sync_type == 3 AND local_dir = 0\n    ')


def _upgrade_73_to_74(trans = None):
    trans.execute('UPDATE file_journal SET local_infinite_details = NULL WHERE local_sync_type IS NOT 3')


def _upgrade_74_to_75(trans = None):
    local_fields = ('local_host_id', 'local_user_id', 'local_timestamp', 'local_filename', 'local_blocklist', 'local_infinite_details', 'local_size', 'local_mtime', 'local_ctime', 'local_dir', 'local_attrs', 'local_sync_type')
    query = '\n        SELECT %(values)s, id\n        FROM file_journal\n        WHERE local_sjid IS NULL AND (%(condition)s)\n    '
    (lambda .0: pass# WARNING: Decompyle incomplete
)(local_fields()) %= {
        'values': ' OR '.join,
        'condition': (lambda .0: pass# WARNING: Decompyle incomplete
)(local_fields()) }
    rows_to_migrate = set()
    unexpected_non_null_fields = defaultdict(int)
    for entry in trans.execute(query):
        row_id = entry[-1]
        for field, field_is_not_null in zip(local_fields, entry):
            if field_is_not_null:
                if field in ('local_host_id', 'local_user_id', 'local_timestamp'):
                    rows_to_migrate.add(row_id)
                    continue
                rows_to_migrate.discard(row_id)
            '\n        UPDATE file_journal\n        SET\n            local_host_id = NULL,\n            local_user_id = NULL,\n            local_timestamp = NULL\n        WHERE id = ?\n    ' = ', '.join
            
            def <listcomp>(.0):
                return [ (rid,) for rid in .0 ]

            migration(<listcomp>, rows_to_migrate())
            report_data = { }
            if rows_to_migrate:
                report_data['rows_migrated'] = Text(len(rows_to_migrate))
    for field, count in iteritems(unexpected_non_null_fields):
        report_data[field] = Text(count)
        if report_data:
            report(SYNC_ENGINE_MIGRATION_STATS_EVENT, to_version = 75, extra = report_data)
            return None
        return trans.executemany


def _upgrade_75_to_76(trans = None):
    if not dropbox_version.is_stable():
        local_placeholder_query = '\n            SELECT server_path FROM file_journal\n            WHERE local_sync_type = 3 AND local_dir = 0 AND local_sjid > 0 AND updated_sjid IS NULL\n        '
        server_paths = trans.execute(local_placeholder_query)()
        fj_migration = '\n            UPDATE file_journal\n            SET\n                updated_sjid = local_sjid,\n                updated_host_id = local_host_id,\n                updated_filename = local_filename,\n                updated_blocklist = local_blocklist,\n                updated_size = local_size,\n                updated_mtime = local_mtime,\n                updated_dir = local_dir,\n                updated_timestamp = local_timestamp,\n                updated_user_id = local_user_id,\n                updated_attrs = local_attrs,\n                updated_sync_type = local_sync_type,\n                force_reconstruct = 1\n            WHERE server_path = ?\n        '
        
        def <listcomp>(.0):
            return [ (sp,) for sp in .0 ]

        fj_migration(<listcomp>, server_paths())
        fj_fileid_migration = '\n            UPDATE file_journal_fileid\n            SET\n                updated_fileid = local_fileid,\n                updated_fileid_rev = local_fileid_rev\n            WHERE server_path = ?\n        '
        
        def <listcomp>(.0):
            return [ (sp,) for sp in .0 ]

        fj_fileid_migration(<listcomp>, server_paths())
        trans.execute('\n            UPDATE file_journal\n            SET force_reconstruct = 1\n            WHERE updated_sjid IS NOT NULL AND updated_sync_type = 3 AND updated_dir = 0\n        ')
        return None


def _upgrade_76_to_77(trans = None):
    existing_tables = get_tables(trans)
    if 'mount_table' not in existing_tables:
        raise ResyncRequiredMigrationException('mount_table not in %r' % existing_tables)
    trans.execute('DROP TABLE IF EXISTS namespace_attributes')
    trans.execute('DROP TABLE IF EXISTS new_mount_table')
    trans.execute('\n                  CREATE TABLE namespace_attributes\n                  (ns INTEGER PRIMARY KEY NOT NULL,\n                  permissions INTEGER,\n                  properties INTEGER DEFAULT NULL,\n                  team_id INTEGER DEFAULT NULL)\n                  ')
    trans.execute('\n                  INSERT INTO namespace_attributes (ns)\n                  SELECT ns FROM namespace_map WHERE NOT EXISTS (\n                  SELECT target_ns FROM mount_table WHERE target_ns = ns)\n                  ')
    root_nses = trans.execute('SELECT ns FROM namespace_attributes')()
    if len(root_nses) > 1:
        raise ResyncRequiredMigrationException('Got multiple root_nses: %r' % root_nses)
    trans.execute('\n                  INSERT INTO namespace_attributes (ns, permissions, properties, team_id)\n                  SELECT target_ns, permissions, properties, team_id FROM mount_table\n                  ')
    trans.execute('\n                  CREATE TABLE new_mount_table (\n                  server_path TEXT PRIMARY KEY NOT NULL, target_ns INTEGER UNIQUE NOT NULL)\n                  ')
    trans.execute('\n                  INSERT INTO new_mount_table (server_path, target_ns)\n                  SELECT server_path, target_ns FROM mount_table\n                  ')
    trans.execute('DROP TABLE mount_table')
    trans.execute('ALTER TABLE new_mount_table RENAME TO mount_table')


def _upgrade_77_to_78(trans = None):
    trans._add_column('namespace_attributes', 'owner_id_hash', 'TEXT DEFAULT NULL')


def _upgrade_78_to_79(trans = None):
    trans._add_column('server_mount_table', 'permissions', 'INTEGER')
    trans._add_column('server_mount_table', 'properties', 'INTEGER DEFAULT NULL')
    trans._add_column('server_mount_table', 'team_id', 'INTEGER DEFAULT NULL')
    trans._add_column('server_mount_table', 'owner_id_hash', 'TEXT DEFAULT NULL')


def _upgrade_79_to_80(trans = None):
    trans.set_config_key(LACONIC_GRASSHOPPER_RECOVERY_NEEDED, True)


def upgrade(trans = None, from_version = None, to_version = None):
    for version in range(65, to_version):
        args = ()
        upgrade_fn = getattr(sys.modules[__name__], '_upgrade_%d_to_%d' % (version, version + 1))
        upgrade_single_version(trans, upgrade_fn, from_version, version, to_version, args)
        return None

