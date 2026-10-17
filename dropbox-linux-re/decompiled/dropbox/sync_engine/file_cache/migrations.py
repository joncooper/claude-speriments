# Source Generated with Decompyle++
# File: migrations.pyc (Python 3.11)

from __future__ import absolute_import
import contextlib
import json
import sqlite3
from six.moves import range
from constants import CONFIG_JAN_2015_INCONSISTENT_STATE_KEY
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, report_rare_event
from dropbox.functions import batch
from dropbox.shared.util import safe_navigate
from dropbox.sqlite3_helpers import dict_like_row, row_factory
from dropbox.trace import TRACE
disable_converters = (lambda : pass# WARNING: Decompyle incomplete
)()

class EmptyResourceForkException(Exception):
    pass


def check_for_empty_resource_forks(cursor):
    pass
# WARNING: Decompyle incomplete

FORUMS_ENTRIES_WITHOUT_MACHINEIDS_BATCH_SIZE = 200

def forums_entries_without_machineids_migration(trans):
    all_server_paths = trans.execute('SELECT server_path FROM file_journal_fileid WHERE (machineid_volumeid IS NULL or machineid_inode IS NULL) AND local_fileid IS NOT NULL').fetchall()
    ct = 0
    for server_paths in batch(all_server_paths, FORUMS_ENTRIES_WITHOUT_MACHINEIDS_BATCH_SIZE):
        server_paths = (lambda .0: pass# WARNING: Decompyle incomplete
)(server_paths())
        ct += len(server_paths)
        TRACE('Clearing fileids for entries without machineids: %r', server_paths)
        'UPDATE file_journal_fileid SET local_fileid = NULL, local_fileid_rev = NULL WHERE server_path IN (%s)'(', '.join % (lambda .0: pass# WARNING: Decompyle incomplete
)(range(len(server_paths))()), server_paths)
        'UPDATE file_journal_extra_metadata_persistent SET mount_transition_no_volumeid = NULL WHERE server_path IN (%s)'(', '.join % (lambda .0: pass# WARNING: Decompyle incomplete
)(range(len(server_paths))()), server_paths)
        TRACE('Modified %d entries', ct)
        return None


def clear_reconstruct_in_progress_migration(trans):
    trans.execute('DELETE FROM file_journal_reconstruct')


def clear_jan_2015_consistency_checker(trans):
    
    try:
        trans.get_config_key(CONFIG_JAN_2015_INCONSISTENT_STATE_KEY)
        trans.remove_config_key(CONFIG_JAN_2015_INCONSISTENT_STATE_KEY)
    except KeyError:
        pass

    trans.execute('DROP TABLE IF EXISTS jan_2015_namespace_map')
    trans.execute('DROP TABLE IF EXISTS jan_2015_snapshot')
    trans.execute('DROP TABLE IF EXISTS jan_2015_job_state')

