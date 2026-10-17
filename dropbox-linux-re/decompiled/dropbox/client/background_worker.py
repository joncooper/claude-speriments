# Source Generated with Decompyle++
# File: background_worker.pyc (Python 3.11)

from __future__ import absolute_import
from dropbox.client.message_queue import InstrumentedMessageQueueThread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread_with_task_timing

class _BackgroundWorkerThreadImpl(InstrumentedMessageQueueThread):
    instrumented_name = (lambda cls = None: 'BACKGROUNDWORKER')()

BackgroundWorkerThread = db_thread_with_task_timing(_BackgroundWorkerThreadImpl, DesktopComponent.POLARIS_PRIMITIVES, _BackgroundWorkerThreadImpl.instrumented_name())
on_background_thread = BackgroundWorkerThread.on_queue
on_background_thread_returns_none = BackgroundWorkerThread.on_queue_returns_none
