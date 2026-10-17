# Source Generated with Decompyle++
# File: named_pipe_ipc.pyc (Python 3.11)

import json
import pywintypes
import win32api
import win32con
import win32event
import win32file
import win32pipe
import winerror
from dropbox.client.util.win import FILE_FLAG_FIRST_PIPE_INSTANCE, get_named_pipe_security_attributes, PIPE_REJECT_REMOTE_CLIENTS
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.html_views.common.threading import background_event_handler
from dropbox.foundation.html_views.electron.ipc._base import ElectronIpcBase
from dropbox.foundation.html_views.electron.ipc.electron_rpc_reporter import ElectronRpcReporter
from dropbox.foundation.trace.trace_js_bridge import ElectronIpcEventTracing
from dropbox.functions import make_bytes
from dropbox.threadutils import StoppableThread
from dropbox.trace import TRACE
ERROR_PIPE_BUSY = 231
ERROR_NO_DATA = 232
ERROR_PIPE_LISTENING = 536

class ElectronNamedPipeIpc(ElectronIpcBase, Actor):
    pass
# WARNING: Decompyle incomplete

