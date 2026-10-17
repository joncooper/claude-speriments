# Source Generated with Decompyle++
# File: threading.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.client.message_queue import MessageQueueThread
from dropbox.db_thread import db_thread
from dropbox.threadutils import AccountAvailableMixin

class _UnityStartStopThreadImpl(MessageQueueThread, AccountAvailableMixin):
    pass
# WARNING: Decompyle incomplete

UnityStartStopThread = db_thread(_UnityStartStopThreadImpl)

class _UnityWorkerThreadImpl(MessageQueueThread, AccountAvailableMixin):
    pass
# WARNING: Decompyle incomplete

UnityWorkerThread = db_thread(_UnityWorkerThreadImpl)
on_unity_start_stop_thread = UnityStartStopThread.on_queue
on_unity_worker_thread = UnityWorkerThread.on_queue
