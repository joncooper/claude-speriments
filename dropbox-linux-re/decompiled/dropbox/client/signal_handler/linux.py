# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

import faulthandler
import hashlib
import os
import re
import signal
import sys
import tempfile
from ctypes import create_string_buffer
from typing import BinaryIO, Callable, Dict, List, Optional
from build_number import dropbox_version, is_frozen
from dropbox import rclone
from dropbox.client.constants import AppDataPaths
from dropbox.client.high_trace import force_flush
from dropbox.client.util import hard_exit_unwatched
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.functions import make_unicode
from dropbox.hard_trace import report_crash
from dropbox.linux_libc import backtrace, backtrace_symbols, MAX_TRACE_LENGTH, sig_handler_t, signal as libc_signal
from dropbox.platform import IS_LINUX
from dropbox.trace import TRACE
MYPY = False

class StackTraceBuffer:
    
    def __init__(self = None):
        self.f = None

    
    def fileno(self = None):
        if not self.f:
            self.f = tempfile.TemporaryFile()
    # WARNING: Decompyle incomplete

    
    def getvalue(self = None):
        if self.f:
            self.f.seek(0)
            return self.f.read()



class SignalHandler:
    ADDRESS = re.compile(b'0[xX][0-9a-fA-F]{8}')
    FATAL_SIGNALS: 'Dict[int, str]' = {
        signal.SIGSEGV: 'SIGSEGV',
        signal.SIGILL: 'SIGILL',
        signal.SIGFPE: 'SIGFPE',
        signal.SIGBUS: 'SIGBUS',
        signal.SIGABRT: 'SIGABRT' }
    SIGNAL_HANDLER_TIMEOUT = 5
    _callbacks: 'List[Callable[[int], None]]' = []
    
    def __init__(self = None, client_session_id = None):
        if not IS_LINUX:
            raise NotImplementedError('Not available on this non-Linux platform.')
        self._death_bell_flag = False
        self._stack_buffer = StackTraceBuffer()
        self.client_session_id = client_session_id

    
    def register(self = None):
        for sig in self.FATAL_SIGNALS:
            self._signal(sig, self._handle_fatal)
            
            try:
                faulthandler.enable(self._stack_buffer, all_threads = False)
            except FileNotFoundError:
                faulthandler.enable(all_threads = False)

            self._register_debug_handlers()
            return None

    
    def _generate_trace(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _signal(self = None, sig = None, handler = None):
        pass
    # WARNING: Decompyle incomplete

    _register_debug_handlers = (lambda : if rclone.rclone_enabled():
signal.signal(signal.SIGINT, SignalHandler._handle_exit_signal)signal.signal(signal.SIGTERM, SignalHandler._handle_exit_signal)else:
signal.signal(signal.SIGINT, signal.SIG_DFL)if not dropbox_version.is_internal_alpha() or is_frozen():
threaddump_file = open(os.path.join(AppDataPaths.dropbox_appdata_path, 'logs', 'threaddump.log'), 'w')if MYPY and sys.platform.startswith('win'):
Nonefaulthandler.register(signal.SIGQUIT, file = threaddump_file, all_threads = True)None)()
    _handle_exit_signal = (lambda signum = None, _frame = None: signal.signal(signum, signal.SIG_DFL)try:
if rclone.rclone_enabled():
rclone.run_atexit_handlers()os.kill(os.getpid(), signum)Noneexcept:
os.kill(os.getpid(), signum))()
    
    def _death_bell(self = None):
        if not self._death_bell_flag:
            signal.alarm(self.SIGNAL_HANDLER_TIMEOUT)
            self._death_bell_flag = True
            return None

    
    def _handle_fatal(self = None, signum = None):
        self._death_bell()
        
        try:
            c_trace = self._generate_trace()
            signal_s = self.FATAL_SIGNALS[signum]
            self._send_report(signal_s, c_trace)
            force_flush()
            hard_exit_unwatched(ExitCode(-signum))
            
            try:
                pass
            except Exception:
                report_exception(severity = Severity.CRITICAL, component = DesktopComponent.CRASH_AND_EXCEPTION_REPORTING)
                force_flush()
                
                try:
                    pass
                try:
                    os._exit(-signum)
                    return None
                except:
                    os._exit(-signum)




    
    def _send_report(self = None, signal_s = None, c_stack = None):
        pass
    # WARNING: Decompyle incomplete


