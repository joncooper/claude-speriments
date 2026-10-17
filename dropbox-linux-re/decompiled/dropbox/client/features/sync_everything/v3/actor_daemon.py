# Source Generated with Decompyle++
# File: actor_daemon.pyc (Python 3.11)

from typing import Generic, List, Optional, Text, Type, TypeVar
from dropbox.client.features.backup_common.base_event_reporter import EventReporter
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcInfo
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.threading import Lock
_ActorType = TypeVar('_ActorType', bound = Actor)
_DaemonFuture = Future[None]

def _report_exception(_exc = None, exc_info = None, severity = None, component = ('_exc', 'Exception', 'exc_info', 'ExcInfo', 'severity', 'Severity', 'component', 'DesktopComponent', 'return', '_DaemonFuture')):
    report_exception(severity = severity, exc_type = exc_info[0], exc_val = exc_info[1], exc_traceback = exc_info[2], component = component)
    return ResolvedFuture(None)


def ActorDaemon():
    '''ActorDaemon'''
    
    def __init__(self, actor, action = None, interval = None, severity = None, run_first = (Severity.CRITICAL, False, None), exceptions_to_trace = ('actor', '_ActorType', 'action', 'Text', 'interval', 'int', 'severity', 'Severity', 'run_first', 'bool', 'exceptions_to_trace', 'Optional[List[Type[Exception]]]', 'return', 'None')):
        self._actor = actor
        self._name = type(actor).__name__
        self._lock = Lock()
        self._daemon_name = 'ActorDaemon:{}:{}'.format(self._name, action)
        self._action = getattr(actor, action)
        self._interval = interval
        self._is_running = False
        self._next_check = None
        self._reporter = EventReporter(self._daemon_name, trace_only = True, interval = interval)
        self._severity = severity
    # WARNING: Decompyle incomplete

    _internal_action = (lambda self = None, _none = None: self._action())()
    _loop = (lambda self = None, _none = None: pass# WARNING: Decompyle incomplete
)()
    
    def set_interval(self = None, interval = None):
        self._lock
        shorter = interval < self._interval
        self._reporter.trace('set_interval', interval = interval)
        self._reporter.update_metadata(interval = interval)
        self._interval = interval
        if self._next_check:
            needs_restart = shorter
            None(None, None)
        else:
            with None:
                if not self._next_check:
                    pass
        if needs_restart:
            self.restart()
            return None

    
    def get_interval(self = None):
        return self._interval

    
    def stop(self = None):
        self._lock
        if self._next_check:
            self._next_check.cancel()
        self._next_check = None
        self._is_running = False
        self._reporter.report('stopped')
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def startup(self = None):
        self._lock
        self._reporter.report('started')
        self._next_check = ResolvedFuture(None)
        self._is_running = True
        None(None, None)

    
    def restart(self = None):
        self.stop()
        self.startup()

    is_running = (lambda self = None: self._is_running)()

ActorDaemon = <NODE:27>(ActorDaemon, 'ActorDaemon', Generic[_ActorType])
