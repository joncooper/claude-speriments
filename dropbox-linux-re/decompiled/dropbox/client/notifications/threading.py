# Source Generated with Decompyle++
# File: threading.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from dropbox.client.message_queue import MessageQueueThread
from dropbox.db_thread import db_thread

class _UserNotificationThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

UserNotificationThread = db_thread(_UserNotificationThreadImpl)
on_user_notification_thread = UserNotificationThread.on_queue
