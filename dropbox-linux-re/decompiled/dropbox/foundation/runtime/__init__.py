# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import atexit
import contextlib
import datetime
import functools
import re
import sys
import threading
import traceback
from types import TracebackType
from typing import Callable, IO, Iterable, Iterator, List, Mapping, Optional, Tuple, Type, TypeVar, Union
from mypy_extensions import NoReturn
import build_number
from dropbox.components.desktop_components import DesktopComponent
from dropbox.debugging import DEBUG_SHELL_THREAD_NAME
from dropbox.event import report
from dropbox.exception.exceptions import FoundationPanicError
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_with_stack_trace, Severity
from dropbox.foundation.exception_info import ExcInfo, typed_exc_info
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sqlite3_exceptions import DatabaseOrDiskFullError, DiskIOError
from dropbox.threading import RLock
from dropbox.trace import TRACE
if IS_WINDOWS:
    from win import halt_process as _halt_process, notify_monitor_clean_termination as _notify_monitor, notify_request_restart as _request_restart, set_restart_state
elif IS_MAC:
    from mac import halt_process as _halt_process, notify_monitor_clean_termination as _notify_monitor, notify_request_restart as _request_restart, set_restart_state
elif IS_LINUX:
    from linux import halt_process as _halt_process, notify_monitor_clean_termination as _notify_monitor, notify_request_restart as _request_restart, set_restart_state
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import LocalConfigurationInterface
CONFIG_AUTORESTART_UI_STATE = 'restart_ui_state'

class AutorestartRequestManager:
    _instance: "Optional['AutorestartRequestManager']" = None
    _singleton_lock: 'RLock' = RLock()
    
    def __init__(self = None):
        self._eligible = False
        self._mark_no_autorestart = False
        self._no_autorestart_reason = None
        self._config = None
        self._state_lock = RLock()
        self._ui_state_callback = None

    
    def set_config(self = None, config = None):
        TRACE('[autorestart] Set local storage.')
        self._config = config

    instance = (lambda : pass# WARNING: Decompyle incomplete
)()
    
    def mark_no_autorestart(self = None, reason = None):
        TRACE('[autorestart]: Mark no autorestart because of %r', reason)
        self._state_lock
        self._mark_no_autorestart = True
        self._disable_autorestart()
        self._no_autorestart_reason = reason
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def undo_mark_no_autorestart(self = None, reason = None):
        TRACE('[autorestart]: Unmarked no autorestart because of %r', reason)
        if not self._eligible:
            TRACE('[autorestart]: Cannot enable autorestart due to ineligibility')
            return None
        None._state_lock
        self._mark_no_autorestart = False
        self._no_autorestart_reason = None
        set_restart_state(enable = True)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def mark_user_quit_intent(self = None):
        self.mark_no_autorestart('User initiated exit')

    
    def set_ui_state_callback(self = None, callback = None):
        self._state_lock
        self._ui_state_callback = callback
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def refresh_ui_state(self = None):
        if not self._config:
            TRACE('[autorestart] Local storage was not set!')
            return None
    # WARNING: Decompyle incomplete

    
    def _disable_autorestart(self = None):
        TRACE('[autorestart] Disabling autorestart')
        if not self._eligible:
            TRACE('[autorestart]: Not eligible to disable autorestart. Additional reason: %r', self._no_autorestart_reason)
            return None
        None._state_lock
        set_restart_state(enable = False)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def notify_request_restart(self = None):
        if not self._eligible and self._mark_no_autorestart:
            TRACE('Requesting restart...')
            report('autorestart', attempted = True)
            _request_restart()
            TRACE('Restart requested')
            return None
        TRACE('Not requesting restart due to reason: %r', self._no_autorestart_reason)
        report('autorestart', attempted = False, reason = self._no_autorestart_reason)

    
    def mark_restart_eligible(self = None, eligible = None, reason = None):
        self._eligible = eligible
        self._no_autorestart_reason = reason
        if eligible:
            TRACE('[autorestart] Enabling autorestart')
            self._state_lock
            if self._mark_no_autorestart:
                TRACE('[autorestart] Not enabling autorestart because of %r', self._no_autorestart_reason)
                None(None, None)
                return None
            set_restart_state(enable = True)
            None(None, None)
            return None
        with None:
            if not None:
                pass
        return None


_C = TypeVar('_C', bound = Callable[(..., object)])

class _Shutdown(object):
    detected = False
    
    def _Shutdown__on_exit(self = None):
        _Shutdown.detected = True

    atexit.register(_Shutdown__on_exit, 0)
    del _Shutdown__on_exit


class Interpreter(object):
    is_shutting_down = (lambda : _Shutdown.detected)()
    _truncation_points = [
        (re.compile('_pytest[\\\\/]python.py$'), 'pytest_pyfunc_call'),
        (re.compile('unittest[\\\\/]case.py$'), 'run'),
        (re.compile('unittest[\\\\/]case.py$'), '_callTestMethod')]
    current_stack = (lambda trim_frames = None: stack = traceback.extract_stack(limit = 32)[:-(1 + trim_frames)]trimmed = 0if not hasattr(sys, 'frozen'):
for i, fs in enumerate(list(stack)):
for t_file_rx, t_function in Interpreter._truncation_points:
if fs.name == t_function and t_file_rx.search(fs.filename):
trimmed = iif trimmed:
del stack[0:trimmed]out = traceback.format_list(stack)if trimmed:
out.insert(0, '  [test-harness frames omitted]\n')out)()
    _signal_and_exit = (lambda exit_code = None: try:
if exit_code != ExitCode.FATAL_EXCEPTION:
AutorestartRequestManager.instance().mark_no_autorestart('Disabling autorestart since this is not a FATAL exception.')_notify_monitor()if isinstance(exit_code, ExitCode):
_halt_process(exit_code.value)Nonereport_bad_assumption('Expected ExitCode enumeration, received: %r' % exit_code)_halt_process(exit_code)Noneexcept:
if isinstance(exit_code, ExitCode):
_halt_process(exit_code.value)report_bad_assumption('Expected ExitCode enumeration, received: %r' % exit_code)_halt_process(exit_code))()


class LineList(object):
    
    def __init__(self = None, lines = None):
        if isinstance(lines, str):
            lines = [
                lines]
        self._LineList__prefix = ''
        self._LineList__suffix = ''
        self.lines = []
        arr = []
        for line in lines:
            if isinstance(line, str):
                arr.extend(line.split('\n'))
                if arr and arr[-1] == '':
                    arr.pop()
                continue
            arr.append(line)
            return None

    
    def write_to(self = None, outfile = None):
        self._write_to_impl(outfile, '', '')

    
    def _write_to_impl(self = None, outfile = None, prefix = None, suffix = ('outfile', 'IO[str]', 'prefix', 'str', 'suffix', 'str', 'return', 'None')):
        prefix = prefix + self._LineList__prefix
        suffix = self._LineList__suffix + suffix
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        cStringIO = cStringIO
        import six.moves
        buffer = cStringIO()
        
        try:
            self.write_to(buffer)
            buffer.close()
            return buffer.getvalue()
        except:
            buffer.close()


    
    def __repr__(self = None):
        cStringIO = cStringIO
        import six.moves
        buffer = cStringIO()
        
        try:
            buffer.write('[prefix: {!r}; suffix {!r}; lines \n{}\n]'.format(self._LineList__prefix, self._LineList__suffix, self.lines))
            buffer.close()
            return buffer.getvalue()
        except:
            buffer.close()


    __add_impl = (lambda lines_a = None, lines_b = None, prefix = staticmethod, suffix = ('lines_a', "List[Union[str, 'LineList']]", 'lines_b', "List[Union[str, 'LineList']]", 'prefix', 'str', 'suffix', 'str', 'return', "'LineList'"): obj = LineList([])obj.lines = lines_a + lines_bobj._LineList__prefix = prefixobj._LineList__suffix = suffixobj)()
    
    def __add__(self = None, other = None):
        if isinstance(other, str):
            return self.__add__(LineList(other))
    # WARNING: Decompyle incomplete

    
    def __radd__(self = None, other = None):
        return LineList(other) + self

    
    def indent(self = None, indent_length = None):
        return self.prefix(' ' * indent_length)

    
    def prefix(self = None, _LineList__str = None):
        return self.wrap(prefix = _LineList__str)

    
    def suffix(self = None, _LineList__str = None):
        return self.wrap(suffix = _LineList__str)

    
    def wrap(self = None, prefix = None, suffix = None):
        ret = LineList(())
        ret.lines = list(self.lines)
        ret._LineList__prefix = self._LineList__prefix + prefix
        ret._LineList__suffix = suffix + self._LineList__suffix
        return ret



def panic_with_report(exit_code, reason, component, exc_info = None, objects = None, stacks = None, relevant_test = (None, None, None, None, Severity.FATAL), severity = ('exit_code', 'ExitCode', 'reason', 'str', 'component', 'DesktopComponent', 'exc_info', 'Optional[ExcInfo]', 'objects', 'Optional[Mapping[str, object]]', 'stacks', 'Optional[List[Tuple[str, List[str]]]]', 'relevant_test', 'Optional[str]', 'severity', 'Severity', 'return', 'NoReturn')):
    pass
# WARNING: Decompyle incomplete


def panic_on_exception(reason = None):
    pass
# WARNING: Decompyle incomplete


def __runtime_excepthook(exc_type = None, exc_value = None, exc_traceback = None):
