# Source Generated with Decompyle++
# File: file_cache_entry.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import sqlite3
from typing import Any, cast, Dict, Iterable, Text, Tuple, Union
from six import iteritems
from six.moves import zip as izip
from constants import SyncType
from file_cache.types import ConflictType, ExtraPendingDetails
from infinite_details import InfiniteDetails
from list_details import ListDetails
from updated_details import UpdatedDetails
from dropbox.assertions import assert_
from dropbox.attrs import Attributes
from dropbox.exception.reporting import report_rare_event
from dropbox.fastdetails import FastDetails
from dropbox.shared.server_path import MRFilenameCaseServerPath, MRLowerServerPath, ServerPath
from dropbox.shared.util import db_lower
from dropbox.shared.validated_record import BaseString, Field, ValidatedRecord
from dropbox.sqlite3_helpers import Cursor, dict_like_row

class FileCacheEntryBase(ValidatedRecord):
    pass
# WARNING: Decompyle incomplete


class FileCacheEntry(FileCacheEntryBase):
    row_factory = (lambda cursor = None, row = None: pass# WARNING: Decompyle incomplete
)()
    create_at = (lambda server_path = None: pass# WARNING: Decompyle incomplete
)()
    
    def mutable(self = None):
        return MutableFileCacheEntry(self)



class MutableFileCacheEntry(FileCacheEntryBase):
    __slots__ = ('_file_cache_entry',)
    
    def __init__(self = None, file_cache_entry = None):
        self._file_cache_entry = file_cache_entry

    
    def immutable(self = None):
        fields = dict(self)
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, item = None):
        return getattr(self._file_cache_entry, item)

    
    def __setattr__(self = None, key = None, value = None):
        object.__setattr__(self, key, value)

    
    def __setitem__(self = None, key = None, value = None):
        setattr(self, key, value)

    
    def update(self = None, iterable = None, **kw):
        pass
    # WARNING: Decompyle incomplete

    
    def queue_revert_to_parent(self = None, reason = None):
        pass
    # WARNING: Decompyle incomplete

    set_updated_details = (lambda cls = None, ent = None, deets = classmethod: pass# WARNING: Decompyle incomplete
)()

