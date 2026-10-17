# Source Generated with Decompyle++
# File: threading.pyc (Python 3.11)

from __future__ import absolute_import
from dropbox.client.message_queue import MessageQueueThread
from dropbox.db_thread import db_thread

class _HarmonyThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete


class _HarmonyPluginThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete


class _HarmonyBackgroundThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

MYPY = False

class _UserCacheThreadImpl(MessageQueueThread):
    pass
# WARNING: Decompyle incomplete

UserCacheThread = db_thread(_UserCacheThreadImpl)
