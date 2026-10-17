# Source Generated with Decompyle++
# File: sync_engine_monitor.pyc (Python 3.11)

from typing import Dict, List, Optional, Tuple
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import LifetimeReporter
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.errors import SyncEverythingException
from dropbox.client.features.sync_everything.v3.event_reporter import SyncEverythingEventReporter
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent
from dropbox.foundation.account_manager import AccountManager, AccountUpdate, AccountUpdateType
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import EasyFuture, FailedFuture, Future
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.threading import Lock

class SyncEngineMonitorTimeoutException(SyncEverythingException):
    pass


class SyncEngineMonitorAssertion(SyncEverythingException):
    pass


class SyncEngineNotPresentException(SyncEverythingException):
    pass


class SyncEngineStatus(Destroyable):
    pass
# WARNING: Decompyle incomplete


class SyncEngineMonitor(Destroyable):
    pass
# WARNING: Decompyle incomplete

