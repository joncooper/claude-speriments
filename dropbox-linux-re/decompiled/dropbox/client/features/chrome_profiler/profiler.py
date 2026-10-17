# Source Generated with Decompyle++
# File: profiler.pyc (Python 3.11)

import os
import sys
import threading
import time
from typing import Any, Dict, Optional
from dropbox.client.features.chrome_profiler.thread_timers import seconds_to_microseconds, ThreadTimers, ThreadTimingTuple
from dropbox.client.features.chrome_profiler.trace_writer import TraceWriter
from dropbox.db_thread import db_thread
from dropbox.threading import Lock
from dropbox.trace import TRACE

class Profiler:
    DEFAULT_FILENAME_FILTER = 'dropbox'
    
    def __init__(self = None):
        self._pid = os.getpid()
        self._writer = None
        self._running = False
        self._lock = Lock()
        self._path_prefix = os.path.abspath(Profiler.DEFAULT_FILENAME_FILTER)
        self._thread_timers = ThreadTimers()
        self._skip_extras = False
        self._stop_time = None

    
    def _profile(self = None, frame = None, event = None, _arg = ('frame', 'Any', 'event', 'str', '_arg', 'Any', 'return', 'None')):
        if not self._running:
            return None
        if None._stop_time and time.monotonic() > self._stop_time:
            self.stop()
            return None
    # WARNING: Decompyle incomplete

    
    def _should_skip(self = None, function_name = None, filename = None, current_thread = ('function_name', 'str', 'filename', 'str', 'current_thread', 'threading.Thread', 'return', 'bool')):
        if filename == __file__:
            return True
        if None == self._writer:
            return True
        if not None.startswith(self._path_prefix):
            return True
        if None in ('current_thread_named', 'do_execute'):
            return True
        if None.name in ('ActorThread', 'PERSISTENT_EVENT_LOGGER'):
            return True

    
    def _shorten_filename(self = None, filename = None):
        return filename[len(self._path_prefix):]

    
    def _enhance_function_name(self = None, function_name = None, locals = None):
