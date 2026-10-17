# Source Generated with Decompyle++
# File: paging_worker_thread.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Any
from dropbox.client.message_queue import MessageQueueThread
from dropbox.db_thread import db_thread

class _PagingWorkerThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

PagingWorkerThread = db_thread(_PagingWorkerThreadImpl)
on_paging_worker_thread = PagingWorkerThread.on_queue
