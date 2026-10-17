# Source Generated with Decompyle++
# File: sync_notification_dispatcher.pyc (Python 3.11)

from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.client.ui.sync_engine_ui.strategies.notification_strategy import NotificationStrategy
from dropbox.client.ui.sync_engine_ui.utils import get_time
from dropbox.threading import Lock
from dropbox.trace import TRACE
DELAYED_DISPATCH_THRESHOLD = 30

class SyncNotificationDispatcher:
    
    def __init__(self = None, strategy = None, account = None):
        self._strategy = strategy
        self._account = account
        self._lock = Lock()
        self._prev_dispatch_time = get_time()

    
    def dispatch(self = None):
        self._lock
        if not self._should_dispatch():
            TRACE('[Sync Notification] Skip dispatching due to rate limiting.')
            None(None, None)
            return None
        None(None, None)

    
    def _should_dispatch(self = None):
        return get_time() - DELAYED_DISPATCH_THRESHOLD > self._prev_dispatch_time

    throttled_dispatch = (lambda self = None: self._lockTRACE('[Sync notification] _inner_dispatch called')self._strategy.schedule_bubble()self._prev_dispatch_time = get_time()None(None, None)Nonewith None:
if not None:
pass)()

