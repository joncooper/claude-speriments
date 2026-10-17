# Source Generated with Decompyle++
# File: auth_thread.pyc (Python 3.11)

from contextlib import contextmanager
from typing import Any, Callable, Iterator
from dropbox.client.message_queue import InstrumentedMessageQueueThread
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread_with_task_timing
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.threadutils import Stoppable

class _AuthenticationThreadImpl(InstrumentedMessageQueueThread):
    instrumented_name = (lambda cls = None: 'AUTHENTICATE')()

AuthenticationThread = db_thread_with_task_timing(_AuthenticationThreadImpl, DesktopComponent.AUTH, _AuthenticationThreadImpl.instrumented_name())
on_auth_thread: 'Callable[..., Any]' = AuthenticationThread.on_queue
on_auth_thread_blocking = AuthenticationThread.on_queue_blocking
on_auth_thread_returns_none = AuthenticationThread.on_queue_returns_none
assert_on_auth_thread = AuthenticationThread.assert_on_queue
on_auth_thread_future = make_on_thread_future_decorator(on_auth_thread, 'on_auth_thread_future')
wakeup_on_reconnect = (lambda thread = None, conn = None: pass# WARNING: Decompyle incomplete
)()
