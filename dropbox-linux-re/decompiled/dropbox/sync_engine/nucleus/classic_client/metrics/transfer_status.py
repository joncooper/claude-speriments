# Source Generated with Decompyle++
# File: transfer_status.pyc (Python 3.11)

from __future__ import division
from statistics import mean, median, stdev
from time import time
from typing import Callable, Dict, List, NamedTuple, Optional
from apex.metrics import Metric, MetricsReporter, TagSet
from build_number import get_build_channel, VERSION
from dropbox.exception.reporting import report_bad_assumption
from dropbox.metrics.constants import SYNC_ENGINE_GENERATION_TAG
from dropbox.platform import platform
from dropbox.proto.nucleus.sync_engine_pb2 import BackupModeArgs
from dropbox.proto.nucleus.sync_epoch_pb2 import SyncEpoch
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_engine_boundary.utils import backup_mode_args_to_engine_generation

class _Estimate(NamedTuple):
    utc_current_time: 'Optional[int]' = '_Estimate'


class SyncEstimateGrader:
    
    def __init__(self, metrics_reporter = None, now_func = None, nucleus = None, backup_mode = ('metrics_reporter', 'MetricsReporter', 'now_func', 'Callable[[], float]', 'nucleus', 'NucleusInterface', 'backup_mode', 'Optional[BackupModeArgs]', 'return', 'None')):
        self._estimates = []
        self._now = now_func
        self._reporter = metrics_reporter
        self._nucleus = nucleus
        self._backup_mode = backup_mode
        self._keep_every = 1
        self._seen_progress = 0
        self._nucleus.on_sync_progress(self._on_sync_progress)

    
    def _on_sync_progress(self = None, sync_progress = None):
        pass
    # WARNING: Decompyle incomplete

    _did_internal_epoch_change = (lambda estimates = None: set((lambda .0: pass# WARNING: Decompyle incomplete
)(estimates())) > 1
)()
    
    def _common_tags(self = None, estimates = None, elapsed_seconds = None):
        if elapsed_seconds < 60:
            time_tag = 'seconds'
        elif elapsed_seconds < 3600:
            time_tag = 'minutes'
        elif elapsed_seconds < 86400:
            time_tag = 'hours'
        else:
            time_tag = 'days'
        file_count = (lambda .0: pass# WARNING: Decompyle incomplete
)(estimates())
        file_count_ceiling = 10
    # WARNING: Decompyle incomplete

    
    def _finish_sync_and_score_estimates(self = None):
        pass
    # WARNING: Decompyle incomplete


