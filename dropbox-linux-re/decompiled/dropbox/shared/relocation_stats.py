# Source Generated with Decompyle++
# File: relocation_stats.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Any, Dict, Text
OPERATION_META_FILE = '.dropbox-relocate3640a06ba127'

class RootNotFoundInCacheException(Exception):
    pass


class OperationStatus(Enum):
    NOT_RUN = 'no_run'
    SUCCESS = 'success'
    INVALID_CACHE = 'invalid_cache'
    UNEXPECTED_EXCEPTION = 'unexpected_exception'


class RemoveSyncedContentStats(object):
    
    def __init__(self = None):
        self.num_files_deleted_success = 0
        self.num_files_deleted_truncated = 0
        self.num_files_deleted_fail = 0
        self.num_infinitized_files = 0
        self.num_skipped_symlinks = 0
        self.num_ignored_files = 0
        self.num_matching_files = 0
        self.num_skipped_abnormal_files = 0
        self.num_skipped_bundles = 0
        self.num_hash_mismatched_files = 0
        self.num_pending_files = 0
        self.num_unseen_files = 0
        self.num_error_files_checking_fs = 0
        self.num_error_files_checking_fc = 0
        self.root_empty_post_op = False
        self.op_status = OperationStatus.NOT_RUN
        self.duration_secs = 0

    
    def complete_with_status_and_duration(self = None, status = None, duration_secs = None):
        self.op_status = status
        self.duration_secs = duration_secs

    
    def get_stats_dict(self = None):
        pass
    # WARNING: Decompyle incomplete


