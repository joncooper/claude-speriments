# Source Generated with Decompyle++
# File: sync_ui_update_thread.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from dropbox.client.message_queue import InstrumentedMessageQueueThread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread_with_task_timing
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator

class _SyncUIUpdateThreadImpl(InstrumentedMessageQueueThread):
    instrumented_name = (lambda cls = None: 'SYNC_UI_UPDATE')()

SyncUIUpdateThread = db_thread_with_task_timing(_SyncUIUpdateThreadImpl, DesktopComponent.SYNC_STATUS_IN_TRAY, _SyncUIUpdateThreadImpl.instrumented_name())
on_sync_ui_update_thread = SyncUIUpdateThread.on_queue
on_sync_ui_update_thread_blocking = SyncUIUpdateThread.on_queue_blocking
on_sync_ui_update_thread_returns_none = SyncUIUpdateThread.on_queue_returns_none
on_sync_ui_update_thread_future = make_on_thread_future_decorator(on_sync_ui_update_thread, 'on_sync_ui_update_thread_future')
