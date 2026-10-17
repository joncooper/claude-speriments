# Source Generated with Decompyle++
# File: transfer_status.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import math
from enum import Enum
from typing import Optional, Tuple
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.sync_engine_boundary.transfer_status import ProgressBottleneck, TransferStatusSnapshot
from dropbox.sync_engine_boundary.types.sync_progress import SyncingSnapshot, SyncProgress
from dropbox.trace import TRACE
HASH_COUNT_SUPPRESSION_DURATION_SECS = 10

class ProgressType(Enum):
    HASH = 1
    UPLOAD = 2
    DOWNLOAD = 3


def _transfer_time_estimate(trace_name = None, ops_count = None, ops_rate = None, bytes_count = (0, 0), bytes_rate = ('trace_name', 'str', 'ops_count', 'int', 'ops_rate', 'float', 'bytes_count', 'int', 'bytes_rate', 'float', 'return', 'Tuple[Optional[float], ProgressBottleneck]')):
    max_time = 0
    bottleneck = ProgressBottleneck.OPS_RATE
    if ops_rate >= 1:
        time_by_ops_rate = float(ops_count) / ops_rate
        if time_by_ops_rate > max_time:
            max_time = time_by_ops_rate
            bottleneck = ProgressBottleneck.OPS_RATE
    if bytes_rate >= 1:
        time_by_bytes_rate = float(bytes_count) / bytes_rate
        if time_by_bytes_rate > max_time:
            max_time = time_by_bytes_rate
            bottleneck = ProgressBottleneck.BYTES_RATE
    if math.isclose(max_time, 0):
        if ops_count > 0 and ops_rate < 1:
            TRACE('%s: Not making progress on %d ops', trace_name, ops_count)
            return (None, bottleneck)
        if None > 0 and bytes_rate < 1:
            TRACE('%s: Not making progress on %d bytes', trace_name, bytes_count)
            return (None, bottleneck)
        return (None, bottleneck)
    TRACE('%s: %.1f sec remaining (%d ops @ %d/sec) (%d bytes @ %d/sec) - bottleneck %s', trace_name, max_time, ops_count, ops_rate, bytes_count, bytes_rate, bottleneck)
    return (max_time, bottleneck)


class TransferStatusMonitor:
    
    def __init__(self = None):
        self._last_syncing_snapshot = None
        self._last_hash_count_suppression = None

    
    def get_last_syncing_snapshot(self = None):
        return self._last_syncing_snapshot

    
    def set_sync_progress(self = None, progress = None):
        self._last_syncing_snapshot = progress.syncing_snapshot
        TRACE('[Sync Progress] Set sync progress: %r', progress.phase)
    # WARNING: Decompyle incomplete

    
    def get_hash_status_snapshot(self = None):
        progress_snapshot = self._last_syncing_snapshot
    # WARNING: Decompyle incomplete

    
    def get_upload_status_snapshot(self = None):
        progress_snapshot = self._last_syncing_snapshot
    # WARNING: Decompyle incomplete

    
    def get_download_status_snapshot(self = None):
        progress_snapshot = self._last_syncing_snapshot
    # WARNING: Decompyle incomplete

    
    def get_percent_complete(self = None):
        progress_snapshot = self._last_syncing_snapshot
    # WARNING: Decompyle incomplete


