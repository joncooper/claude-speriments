# Source Generated with Decompyle++
# File: rpc.pyc (Python 3.11)

import json
from typing import Any, Callable, Dict, Optional, Set, Text
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import EasyFuture, Future
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict, JSONish
from dropbox.foundation.html_views.electron.ipc.electron_rpc_reporter import ElectronRpcReporter
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.trace.trace_js_bridge import ElectronIpcEventTracing
from dropbox.threading import Lock
from dropbox.trace import TRACE
SignalCallback = Callable[([
    JSONDict], None)]
InvocationCallback = Callable[([
    JSONDict], Future[JSONish])]

class ElectronRpc(Destroyable):
    pass
# WARNING: Decompyle incomplete

