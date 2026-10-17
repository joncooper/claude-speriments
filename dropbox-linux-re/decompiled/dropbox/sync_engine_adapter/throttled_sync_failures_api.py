# Source Generated with Decompyle++
# File: throttled_sync_failures_api.pyc (Python 3.11)

import time
from typing import Any, Dict, Literal, NamedTuple, Optional, Tuple
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception, Severity
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.proto.nucleus.sync_failures_pb2 import GetSyncFailuresSummaryReq
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailuresSummary
from dropbox.threading import RLock
InstanceType = Literal[('sync', 'backup')]
CacheType = Literal[('count', 'sample')]
CacheKey = Tuple[(Optional[int], CacheType, int)]

class CacheEntry(NamedTuple):
    in_flight_future: 'Optional[Future[SyncFailuresSummary]]' = 'CacheEntry'


class CacheNamespace:
    
    def __init__(self = None):
        self.entries = { }
        self.lock = RLock()
        self.last_eviction_time = time.time()



class ThrottledSyncFailuresApi(SingletonActor):
    pass
# WARNING: Decompyle incomplete

