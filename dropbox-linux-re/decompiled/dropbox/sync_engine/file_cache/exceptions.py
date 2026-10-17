# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Text
from dropbox.sync_engine_boundary.exceptions import NamespaceNotMountedError

class _ReallyBadDatabaseError(Exception):
    pass


class FileJournalEntryDoesNotExist(Exception):
    pass


class InvalidDatabaseError(Exception):
    pass


class MultipleRootNamespaceError(Exception):
    pass
# WARNING: Decompyle incomplete


class InvalidFileJournalEntryError(Exception):
    create = (lambda suffix = None, desc = None: sub_class = type('InvalidFileJournalEntryError_%s' % suffix, (InvalidFileJournalEntryError,), { })sub_class(desc))()


class ResyncRequiredMigrationException(Exception):
    pass

