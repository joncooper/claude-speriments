# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import
import contextlib
import sys
from collections import defaultdict, namedtuple
from typing import Any, Dict, List, Optional, Text, Tuple, Union
from six import iteritems, reraise
from six.moves import range
from constants import DROPBOX_SYMLINK_KEY, DROPBOX_SYMLINK_PLAT, NUCLEUS_SYMLINK_MIGRATION_PLAT, SyncPolicy, SyncType
from datatypes.infinite_details import InfiniteDetails
from datatypes.updated_details import UpdatedDetails
from constants import FileModificationType, UPLOAD_INVALID_PATH_CODE
from exceptions import InvalidFileJournalEntryError
from types import ConflictType, ExtraPendingDetails
from dropbox.assertions import assert_
from dropbox.attrs import Attributes, copy_file_tag_gid_v3, copy_server_fileid, has_file_tag_gid_v3, mute_attr_set
from dropbox.exception.exception_decorators import handle_exceptions_ex_1
from dropbox.exception.reporting import report_bad_assumption, report_rare_event
from dropbox.fastdetails import FastDetails
from dropbox.functions import EitherStr, is_four_byte_unicode, make_str
from dropbox.model.types import NsId
from dropbox.nfcdetector import is_nfc
from dropbox.shared.server_path import ServerPath
from dropbox.shared.util import db_lower
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from datatypes.file_cache_entry import FileCacheEntryBase, MutableFileCacheEntry
sqlite_to_serverpath = (lambda sqlite_type: ServerPath(sqlite_type.decode('utf-8')))()
serverpath_to_sqlite = (lambda sp: Text(sp))()

def is_invalid_path_upload_code(code):
    if not code == UPLOAD_INVALID_PATH_CODE:
        pass
    return code.startswith('extended_')


def create_extended_upload_code(desc):
    return 'extended_%s' % desc


def why_isnt_valid_filejournal_entry(ent):
    
    try:
        check_filejournal_entry(ent)
        return None
    except InvalidFileJournalEntryError:
        e = None
        del e
        return None
        None = 
        del e



def check_filejournal_entry(ent):
    pass
# WARNING: Decompyle incomplete


def check_db_entries(entries):
    for newent in entries:
        check_filejournal_entry(newent)
        return True


def is_valid_filejournal_entry(ent):
    return not why_isnt_valid_filejournal_entry(ent)


def event_type_from_pending_details(pending_details):
    if pending_details.size == -1:
        return FileModificationType.DELETE
# WARNING: Decompyle incomplete


def event_type_from_updated_details(updated_details):
    if updated_details.size == -1:
        return FileModificationType.DELETE
# WARNING: Decompyle incomplete


def local_details_from_entry(ent):
    sp = ServerPath(ServerPath(ent['parent_path'], lowered = True), ent['local_filename'])
# WARNING: Decompyle incomplete


def is_valid_sjid(ns = None, sjid = handle_exceptions_ex_1(should_raise = True)):
    return isinstance(sjid, int)


def merge_locally_unreadable_for_compare(comparing_against, local_attrs):
    new_attr_dict = dict(local_attrs.attr_dict)
    for plat, plat_attrs in iteritems(comparing_against.attr_dict):
        if plat not in new_attr_dict and plat not in local_attrs.data_plats:
            new_attr_dict[plat] = plat_attrs
        return local_attrs.copy(attr_dict = new_attr_dict)


def generate_attrs_for_compare(remote_attrs, local_attrs, first_local_edit):
    merged_local_attrs = merge_locally_unreadable_for_compare(remote_attrs, local_attrs)
    if first_local_edit:
        merged_local_attrs = copy_file_tag_gid_v3(remote_attrs, merged_local_attrs)
        merged_local_attrs = copy_server_fileid(remote_attrs, merged_local_attrs)
    return merged_local_attrs


def set_upcoming_sync_type_on_pending_row(ent = None, upcoming_sync_type = None):
    pass
# WARNING: Decompyle incomplete


def set_upcoming_folder_policy_on_pending_row(ent = None, upcoming_folder_policy = None):
    pass
# WARNING: Decompyle incomplete


def set_parent_fileid_info_on_pending_row(ent, machineid_volumeid, machineid_inode, machineid_attr, fileid, fileid_rev):
    pass
# WARNING: Decompyle incomplete


def clear_extra_pending_details(ent):
    ent['extra_pending_details'] = None
    ent['parent_fileid'] = None
    ent['parent_fileid_rev'] = None
    ent['parent_machineid_volumeid'] = None
    ent['parent_machineid_inode'] = None
    ent['parent_machineid_attr'] = None


def set_local_fileid_info_on_row(ent, local_fileid, local_fileid_rev, local_fileid_parent_fileid, local_fileid_parent_fileid_rev, local_fileid_parent_fileid_type = (None, None, None, None, None)):
    pass
# WARNING: Decompyle incomplete


def set_local_fileid_on_row(ent, local_fileid, local_fileid_rev):
    set_local_fileid_info_on_row(ent, local_fileid = local_fileid, local_fileid_rev = local_fileid_rev)


def set_local_fileid_parent_on_row(ent, local_fileid_parent_fileid, local_fileid_parent_fileid_rev, local_fileid_parent_fileid_type):
    set_local_fileid_info_on_row(ent, local_fileid_parent_fileid = local_fileid_parent_fileid, local_fileid_parent_fileid_rev = local_fileid_parent_fileid_rev, local_fileid_parent_fileid_type = local_fileid_parent_fileid_type)


def f(fn):
    pass
# WARNING: Decompyle incomplete


class FlushBefore(object):
    
    def __init__(self, flusher, curs):
        self.inner = curs
        self.flusher = flusher

    lastrowid = (lambda self: self.inner.lastrowid)()
    rowcount = (lambda self: self.inner.rowcount)()
    row_factory = (lambda self: self.inner.row_factory)()
    row_factory = (lambda self, value: self.inner.row_factory = value)()
    connection = (lambda self: self.inner.connection)()
    execute = (lambda self: pass# WARNING: Decompyle incomplete
)()
    executemany = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def __iter__(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def next(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def __next__(self):
        return next(self.inner)

    
    def fetchone(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchmany(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def fetchall(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def get_config_key(self, *args, **kw):
        pass
    # WARNING: Decompyle incomplete


FileIdInfoAndComparisonValue = namedtuple('FileIdInfoAndComparisonValue', [
    'fileid_info',
    'comparison_value'])

class MachineIdDict(object):
    
    def __init__(self, selector_fn):
        self._dict = defaultdict(list)
        self.selector_fn = selector_fn

    
    def update(self, iterator):
        for fileid_info, comparison_value in iterator:
            self._dict[key].append(FileIdInfoAndComparisonValue(fileid_info, comparison_value))
            return None

    
    def as_dict(self):
        ret = { }
    # WARNING: Decompyle incomplete



def is_keynote_path(server_path):
    cur_path = ServerPath(server_path)
# WARNING: Decompyle incomplete


def highest_sjid_selector_full_machineid(key, matches):
    (ns_id, sjid, best_match) = (None, None, None)
# WARNING: Decompyle incomplete


def highest_sjid_selector_machineid_attr(key, matches):
    (ns_id, sjid, best_match) = (None, None, None)
# WARNING: Decompyle incomplete


def most_recent_date_selector(key, matches):
    ordered = sorted(matches, key = (lambda value: value.comparison_value), reverse = True)
    if ordered[0].comparison_value - ordered[1].comparison_value < 5:
        report_bad_assumption('Deleted matches for fileids have very close timestamps: %r', ordered[:5])
    return ordered[0].fileid_info

raise_keyerror_transaction = (lambda fc: pass# WARNING: Decompyle incomplete
)()
db_parent_sjid = (lambda extra_pending_details: pass# WARNING: Decompyle incomplete
)()

def is_muted(old_entry = None):
    if old_entry['updated_attrs']:
        pass
    return bool(mute_attr_set(old_entry['updated_attrs']))


def is_sync_change(old_entry = None, new_entry = None):
    
    def local_sjid_if_synced(entry):
