# Source Generated with Decompyle++
# File: notification_strategy.pyc (Python 3.11)

from typing import Callable, List, Optional
from apex.metrics import Metric, MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client.ui.sync_engine_ui.accumulator import SyncOperationBucketingAccumulator, SyncOperationFileTracker
from dropbox.client.ui.sync_engine_ui.notification_generator import NotificationGenerator
from dropbox.client.ui.sync_engine_ui.utils import get_time, SYNC_NOTIFICATION_AMP_NAMESPACE, SyncNotificationSettings
from dropbox.client.users import UserCache, UserInfo
from dropbox.model.types import UserId
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.threading import Lock
from dropbox.trace import TRACE

class NotificationStrategy:
    DEFAULT_BUCKETING_DELAY = 180
    
    def __init__(self, user_cache, notif_generator = None, account = None, metrics_reporter = None, sync_notif_pref = ('user_cache', 'UserCache', 'notif_generator', 'NotificationGenerator', 'account', 'AccountInterface', 'metrics_reporter', 'MetricsReporter', 'sync_notif_pref', 'SyncNotificationSettings', 'return', 'None')):
        self._user_cache = user_cache
        self._notif_generator = notif_generator
        self._account = account
        self._reporter = metrics_reporter
        self._sync_notif_pref = sync_notif_pref
        self._bucketed_accumulator = SyncOperationBucketingAccumulator()
        self.will_flush = False
        self._lock = Lock()

    
    def handle_sync_completed_summary(self = None, sync_completed_summary = None):
        results = SyncOperationBucketingAccumulator()
    # WARNING: Decompyle incomplete

    
    def schedule_bubble(self = None):
        bubbling_delay = 0
        if IS_LINUX:
            on_ui_thread(f = self._flush_my_bubble, delay = bubbling_delay, debounce = True)()
            on_ui_thread(f = self._flush_bucketed_others_bubbles, delay = bubbling_delay + self.DEFAULT_BUCKETING_DELAY, debounce = True)()
        if not (IS_MAC or IS_WINDOWS) and self.will_flush:
            self.will_flush = True
            bubbling_delay = max(self._notif_generator.last_bubble_time_remaining, 1)
            on_ui_thread(f = self._flush_my_bubble, delay = bubbling_delay, debounce = True)()
            on_ui_thread(f = self._flush_bucketed_others_bubbles, delay = bubbling_delay + self.DEFAULT_BUCKETING_DELAY, debounce = True)()
        self._reporter.create_stats(Metric(SYNC_NOTIFICATION_AMP_NAMESPACE, 'bubbling_delay'), { }).record(bubbling_delay)

    
    def _flush_my_bubble(self = None):
        TRACE('[Sync Notification] Flushing my notification immediately')
        self._lock
        for user_id, file_tracker in self._bucketed_accumulator.pop_users(self._my_user_ids()):
            self._notif_generator.show_notif_with_avatar(user_info = None, user_id = user_id, file_tracker = file_tracker, num_other_users = 0)
            self.will_flush = False
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def _my_user_ids(self = None):
        my_user_ids = []
        if self._account.uid:
            my_user_ids.append(UserId(self._account.uid))
        if self._account.paired_uid:
            my_user_ids.append(UserId(self._account.paired_uid))
        return my_user_ids

    
    def _make_notif_callback(self = None, user_id = None, file_tracker = None, other_user_count = ('user_id', 'Optional[UserId]', 'file_tracker', 'SyncOperationFileTracker', 'other_user_count', 'int', 'return', 'Callable[[Optional[UserInfo]], None]')):
        pass
    # WARNING: Decompyle incomplete

    
    def _flush_bucketed_others_bubbles(self = None):
        TRACE('[Sync Notification] Checking on delayed notifications and maybe flushing them, accumulator.is_empty: %r', self._bucketed_accumulator.is_empty())
        self._lock
        delay_time = get_time() - self.DEFAULT_BUCKETING_DELAY
        my_user_ids = self._my_user_ids()
    # WARNING: Decompyle incomplete

    
    def get_file_trackers(self = None):
        return self._bucketed_accumulator.get_file_trackers()

    
    def clear(self = None):
        self._lock
        self._bucketed_accumulator.clear()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def is_empty(self = None):
        return self._bucketed_accumulator.is_empty()


