# Source Generated with Decompyle++
# File: periodic.pyc (Python 3.11)

import threading
from typing import Callable, Dict, NamedTuple, Optional, Text
from dropbox.assertions import assert_
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.sync_engine_boundary.exceptions import ServiceNotAvailableException, SyncEngineStoppedError
from dropbox.threading import Lock
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
PeriodicJob = NamedTuple('PeriodicJob', [
    ('name', Text),
    ('period', int),
    ('fn', Callable[([], None)])])
MAX_JOB_DURATION = 30
PERIOD_GRANULARITY_SECS = 60

class _Worker(StoppableThread):
    pass
# WARNING: Decompyle incomplete


class JobNameAlreadyExistsError(Exception):
    pass


class PeriodicScheduler(object):
    
    def __init__(self = None):
        self._jobs = { }
        self._config_lock = Lock()
        self._last_runs = { }
        self._worker = db_thread(_Worker)(self._run_jobs)

    
    def _get_job_name_for_account(self = None, name = None, account = None):
