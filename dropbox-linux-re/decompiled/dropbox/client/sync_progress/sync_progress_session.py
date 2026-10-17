# Source Generated with Decompyle++
# File: sync_progress_session.pyc (Python 3.11)

from __future__ import division
import math
from enum import IntEnum
from time import asctime, gmtime, time as _time
from typing import Optional, Text, Tuple
from uuid import uuid4
from dropbox.client.sync_progress.sync_progress_common import MIN_SYNC_PROGRESS, NO_SYNC_PROGRESS, SMOOTHING_FACTOR_ALPHA, SYNC_FINAL_OFFSET, SYNC_FINAL_UPDATE_DELAY_SEC
from dropbox.client.sync_progress.sync_progress_logging import report_sync_progress_event
from dropbox.client.transient_simple_metric.allowed_simple_metric import SimpleMetricCategoryWhitelist
from dropbox.client.transient_simple_metric.transient_simple_metric import report_transient_simple_metric
from dropbox.trace import TRACE

class SyncSessionState(IntEnum):
    CLEARED = 0
    RUNNING = 1
    WAITING_TO_CLEAR = 2


class SyncProgressSessionErrorCode(IntEnum):
    NONE = 0
    INVALID_FILE_COUNT = 1
    INVALID_SESSION_TS = 2


class SyncProgressSession:
    
    def __init__(self = None):
        self._start_ts = None
        self._end_ts = None
        self._session_id = None
        self._queued_file_count = 0
        self._synced_file_count = 0
        self._state = SyncSessionState.CLEARED
        self._last_progress = NO_SYNC_PROGRESS
        self._time_remaining = 0
        self._is_nucleus_mode = False

    
    def toggle_nucleus_mode(self = None, is_nucleus_mode_enabled = None):
        if self._is_nucleus_mode != is_nucleus_mode_enabled:
            self._is_nucleus_mode = is_nucleus_mode_enabled
        TRACE('[Sync Progress] !! Sync progress Nucleus mode: %s.', str(self._is_nucleus_mode))

    
    def update_sync_session(self = None, queued_file_count = None, synced_file_count = None, queued_time_estimate = ('queued_file_count', 'int', 'synced_file_count', 'int', 'queued_time_estimate', 'float', 'return', 'bool')):
        if not self._is_valid():
            return False
        if None > 0:
            pass
        queued_file_count = self, self._synced_file_count += synced_file_count, ._synced_file_count
        self._time_remaining = queued_time_estimate
        self._update_session_state()
        return self._state == SyncSessionState.WAITING_TO_CLEAR

    
    def get_sync_progress(self = None, percent_complete = None):
        if self._is_valid() or self._state == SyncSessionState.CLEARED:
            new_progress = NO_SYNC_PROGRESS
    # WARNING: Decompyle incomplete

    
    def get_session_id(self = None):
        return self._session_id

    
    def _calculate_percent_done(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _update_session_state(self = None):
        now = _time()
        if self._state == SyncSessionState.CLEARED:
            if self._is_nucleus_mode or self._queued_file_count > 0 or self._is_nucleus_mode or self._time_remaining > 0:
                self._state = SyncSessionState.RUNNING
                self._start_ts = now
                self._session_id = uuid4().hex
                return None
            return None
        return None
        if self._state == SyncSessionState.RUNNING:
            if self._is_nucleus_mode or self._queued_file_count == 0 or self._is_nucleus_mode or self._time_remaining == 0:
                self._state = SyncSessionState.WAITING_TO_CLEAR
                self._set_end_ts(now)
                return None
            return None
        return None
        if (self._is_nucleus_mode or self._queued_file_count > 0 or self._is_nucleus_mode) and self._time_remaining > 0:
            self._state = SyncSessionState.RUNNING
            self._end_ts = None
            return None
    # WARNING: Decompyle incomplete

    
    def _is_valid(self = None):
        error_code = self._get_sync_session_error_code()
        if error_code != SyncProgressSessionErrorCode.NONE:
            self._report_corruption(error_code)
            self._reset()
            return False

    
    def _get_sync_session_error_code(self = None):
        if self._synced_file_count < 0 or self._queued_file_count < 0:
            return SyncProgressSessionErrorCode.INVALID_FILE_COUNT
    # WARNING: Decompyle incomplete

    
    def _report_corruption(self = None, error_code = None):
