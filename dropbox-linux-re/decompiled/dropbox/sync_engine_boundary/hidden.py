# Source Generated with Decompyle++
# File: hidden.pyc (Python 3.11)

from __future__ import absolute_import
from typing import AbstractSet, Any, FrozenSet, Iterable, NamedTuple, Optional, Text
from dropbox.exception.reporting import report_bad_assumption, Severity
from dropbox.shared.server_path import RRLowerServerPath, ServerPath
from dropbox.shared.util import db_lower
from dropbox.shared.validated_record import Field, ValidatedRecord
from dropbox.trace import TRACE
_PathSet = FrozenSet[RRLowerServerPath]
_SetDiff = NamedTuple('_SetDiff', [
    ('added', _PathSet),
    ('removed', _PathSet)])

def _set_diff(old = None, new = None):
    added = new.difference(old)
    removed = old.difference(new)
    return _SetDiff(added = added, removed = removed)


def _server_paths(text_paths = None):
    new_set = set()
# WARNING: Decompyle incomplete


def path_has_parent_in_set_with_overrides(path = None, path_set = None, override_set = None):
    pass
# WARNING: Decompyle incomplete


def path_has_parent_in_set(path = None, path_set = None):
    return path_has_parent_in_set_with_overrides(path, path_set, frozenset())


def remove_already_hidden(paths = None, hidden = None):
    pass
# WARNING: Decompyle incomplete


def dedup_parents(paths = None):
    return remove_already_hidden(paths, paths)


class HiddenSet(ValidatedRecord):
    pass
# WARNING: Decompyle incomplete

