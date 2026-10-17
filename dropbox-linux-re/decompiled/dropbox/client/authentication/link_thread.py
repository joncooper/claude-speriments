# Source Generated with Decompyle++
# File: link_thread.pyc (Python 3.11)

from dropbox.client.message_queue import MessageQueueThread
from dropbox.db_thread import db_thread

class _LinkThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

LinkThread = db_thread(_LinkThreadImpl)
on_link_thread = LinkThread.on_queue
on_link_thread_returns_none = LinkThread.on_queue_returns_none
