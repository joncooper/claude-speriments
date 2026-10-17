# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.attrs import Attributes
from dropbox.shared.validated_record import Field, ValidatedRecord
CANCEL_BLACKLIST_TIMEOUT_SEC = 10
PLACEHOLDER_BLOCKCACHE_PRUNE_DELAY_SEC = 36000
MAX_CONCURRENT_EXTERNAL_RECALLS = 32

class PlaceholderMissingFromFileJournalError(Exception):
    pass


class PlaceholderNamespaceAccessDenied(Exception):
    pass


class RecallCancelledByUser(Exception):
    pass


class RecallCancelledByPager(Exception):
    pass


class RecallFailedNoNetwork(Exception):
    pass


class PlaceholderMetadataFetchError(Exception):
    pass


class PlaceholderMovedError(Exception):
    pass


class ApfsDecmpfsCorruptionRisk(Exception):
    pass


class RecalledPlaceholderSizeMismatch(Exception):
    pass


class PlaceholderMetadata(ValidatedRecord):
    blocklist = Field.required(bytes)
    attrs = Field.required(Attributes)
    size = Field.required(int)
    is_dir = Field.required(bool)
    
    def validate(self = None):
        if self.size < 0:
            raise TypeError('size must be >=0, but was %s' % self.size)


