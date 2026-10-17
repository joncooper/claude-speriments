# Source Generated with Decompyle++
# File: sync_error_logger.pyc (Python 3.11)

import hashlib
import time
from collections import defaultdict
from enum import Enum
from typing import Dict, Optional, Text
from dropbox.client.features.sync_error.model.common import SyncErrorDetail, SyncErrorType, SyncStuckEvents
from dropbox.client.transient_simple_metric.allowed_simple_metric import SimpleMetricCategoryWhitelist
from dropbox.client.transient_simple_metric.transient_simple_metric import report_transient_simple_metric
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.performance.perf_session import get_perf_timestamp
from dropbox.sync_engine_boundary.constants import SyncOperationFailureReason
from dropbox.trace import TRACE

class PermissionEvent(Enum):
    PERMISSIONS_RESOLVER_ATTEMPTED = 'permissions_remediation_attempted'
    PERMISSIONS_RESOLVER_STARTED = 'permissions_remediation_started'
    PERMISSIONS_RESOLVER_RESOLVED = 'permissions_remediation_resolved'
    PERMISSIONS_RESOLVER_ERRORED = 'permissions_remediation_errored'
    PERMISSIONS_RESOLVER_FAILED_FINAL = 'permissions_remediation_failed_final'
    PERMISSIONS_RESOLVER_CANCELLED = 'permissions_remediation_cancelled'
    PERMISSIONS_RESOLVER_RETRIED = 'permissions_remediation_retried'


class SyncErrorLogger:
    pass
# WARNING: Decompyle incomplete

