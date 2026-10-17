# Source Generated with Decompyle++
# File: download_ui.pyc (Python 3.11)

from collections import defaultdict
from typing import Callable, cast, Dict, List, Optional, Text, Tuple
from six import iteritems
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.types import AccountChangeType
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.notifications.legacy_notifications import InfiniteUIStickyNotification
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationButton, LoudNotificationType
from dropbox.client.notifications.strings import UserNotificationStrings
from dropbox.client.ui.common.strings import shorten_filename
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_returns_none
from dropbox.client.ui.ui_timer import UITimerFactory
from dropbox.client.util import highlight_file
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.i18n import format_number, trans, ungettext
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.notification_common import determine_soft_downgrade_text, get_loud_notification_type
from dropbox.infinite.recall_tracker import RecallTracker
from dropbox.infinite.util import report_infinite_event
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.recall_events import InfiniteRecallEvent, InfiniteRecallStatus, InfiniteRecallType
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIAccountState, InfiniteUIAction, InfiniteUIBubbleNotification, InfiniteUIControllerInterface, InfiniteUIDispatcherInterface, InfiniteUIEvent, InfiniteUIEventType, InfiniteUIInterface, InfiniteUIKextInstallFlowSource, InfiniteUINotification, InfiniteUINotificationType, InfiniteUIRequest, InfiniteUIState
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.ui.common.uikit import BaseUIKit
RECALL_STATUS_TO_UI_EVENT = {
    InfiniteRecallStatus.ACTIVE: InfiniteUIEventType.RECALL_DELAYED,
    InfiniteRecallStatus.FAILED_NO_SPACE: InfiniteUIEventType.RECALL_FAILED_NO_SPACE,
    InfiniteRecallStatus.FAILED_SYNC_ENGINE_PAUSED: InfiniteUIEventType.RECALL_FAILED_SYNC_ENGINE_PAUSED,
    InfiniteRecallStatus.FAILED_NO_NETWORK: InfiniteUIEventType.RECALL_FAILED_NETWORK,
    InfiniteRecallStatus.FAILED: InfiniteUIEventType.RECALL_FAILED,
    InfiniteRecallStatus.COMPLETE: InfiniteUIEventType.RECALL_FINISHED }

class HeadlessInfiniteUI(InfiniteUIInterface):
    
    def __init__(self = None, app = None, ui_kit = None):
        self._app = app
        self._ui_kit = ui_kit

    
    def update_state(self = None, state = None):
        TRACE('Recall State Update: %s', state)

    
    def post_event(self = None, event = None):
        TRACE('Recall Event: %s', event)

    
    def push_bubble(self = None, bubble_notification = None, is_persistent = None):
        TRACE('[Infinite Bubble] %s', bubble_notification.notification_type)

    
    def post_notification(self = None, notification = None, include_in_badge_count = None):
        if notification.notification_type == InfiniteUINotificationType.INFINITE_SOFT_DOWNGRADE:
            TRACE('[Infinite Notification] %s: %s', UserNotificationStrings.infinite_soft_downgrade_title, UserNotificationStrings.infinite_soft_downgrade_message)
            return None
        TRACE('[Infinite Notification] %s', notification.notification_type)

    
    def remove_notification(self = None, account = None, notification_type = None):
        pass

    
    def enter_kext_installer(self = None, source = None):
        pass



class InfiniteUIKit(InfiniteUIInterface):
    EVENT_QUEUE_MIN_FLUSH_PERIOD = 3
    EVENT_QUEUE_MAX_FLUSH_PERIOD = 5
    
    def __init__(self, app, ui_kit = None, sync_engine_adapter = None, bubble_context = None, desktop_login = ('app', 'DropboxApplication', 'ui_kit', 'BaseUIKit', 'sync_engine_adapter', 'SyncEngineAdapter', 'bubble_context', 'BubbleContext', 'desktop_login', 'DesktopLogin', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def update_state(self = None, state = None):
        pass

    post_event = (lambda self = None, event = None: is_first_event = len(self._event_queue) == 0for old_event in self._event_queue:
if old_event.request.local_path == event.request.local_path and old_event.event_type == event.event_type:
TRACE('Skipped posting event with path %r because there is already a pending event for this path', event.request.local_path)self._event_queue.append(event)if is_first_event:
self._first_event_timer.start(InfiniteUIKit.EVENT_QUEUE_MAX_FLUSH_PERIOD, self._flush_events)self._next_event_timer.start(InfiniteUIKit.EVENT_QUEUE_MIN_FLUSH_PERIOD, self._flush_events))()
    
    def push_bubble(self = None, bubble_notification = None, is_persistent = None):
        (title, message) = self._get_notification_bubble_strings(bubble_notification.account, bubble_notification.notification_type)
        buttons = []
        for action_title, action_callback in bubble_notification.actions:
            buttons.append(LoudNotificationButton(title = action_title, action = action_callback, contextless_action = None))
            if is_persistent and bubble_notification.actions and len(bubble_notification.actions) > 1:
                is_persistent = True
                TRACE('!! Notification changed from non-persistent to persistent due actions length')
        loud_notification_type = get_loud_notification_type(bubble_notification)
        loud_notification = LoudNotification(loud_notification_type = loud_notification_type, msg = message, caption = title, bubble_context = self._bubble_context, surface_action = bubble_notification.surface_action, buttons = buttons, is_persistent = is_persistent, account = bubble_notification.account, bypass_silent_mode = True, add_to_notification_center = is_persistent)
        self._ui_kit.show_bubble(loud_notification)

    
    def post_notification(self = None, notification = None, include_in_badge_count = None):
        sticky_notification = InfiniteUIStickyNotification(notification, visible = True, include_in_badge_count = include_in_badge_count)
        self._app.add_sticky_notification(notification.account, sticky_notification)

    
    def remove_notification(self = None, account = None, notification_type = None):
        self._app.remove_sticky_notification(account, InfiniteUIStickyNotification.sticky_key_for_notif_type(notification_type))

    
    def _get_notification_bubble_strings(self = None, account = None, notification_type = None):
        strings_map = {
            InfiniteUINotificationType.INFINITE_KEXT_NOT_APPROVED_WEB_OPTIN: (UserNotificationStrings.prompt_infinite_kext_approval_from_web_optin_title, UserNotificationStrings.prompt_infinite_kext_approval_message),
            InfiniteUINotificationType.INFINITE_KEXT_NOT_APPROVED: (UserNotificationStrings.infinite_bubble_online_only_title, UserNotificationStrings.prompt_infinite_kext_approval_message),
            InfiniteUINotificationType.INFINITE_LOW_DISK: (UserNotificationStrings.infinite_bubble_low_disk_title, UserNotificationStrings.infinite_bubble_low_disk_message),
            InfiniteUINotificationType.INFINITE_REQUIRES_RESTART: (UserNotificationStrings.prompt_online_only_restart_title, UserNotificationStrings.prompt_online_only_restart_message),
            InfiniteUINotificationType.INFINITE_REQUIRES_REINSTALL: (UserNotificationStrings.infinite_bubble_reinstall_dropbox_title, UserNotificationStrings.prompt_online_only_reinstall_message),
            InfiniteUINotificationType.INFINITE_TEMPORARILY_DISABLED: (UserNotificationStrings.infinite_bubble_sync_title, ''),
            InfiniteUINotificationType.INFINITE_CONFIGURATION_FAILED: (UserNotificationStrings.infinite_bubble_sync_title, ''),
            InfiniteUINotificationType.INFINITE_SOFT_DOWNGRADE: determine_soft_downgrade_text(account) }
        if notification_type in strings_map:
            return strings_map[notification_type]
        report_bad_assumption('Received InfiniteUINotification with unknown notification_type %r', notification_type, component = DesktopComponent.INFINITE)
        return (Text(notification_type), '')

    
    def _get_event_string(self = None, event_type = None, requests = None):
        num_events = len(requests)
        if num_events == 0:
            report_bad_assumption('Cannot generate an event string for zero events.', component = DesktopComponent.INFINITE)
            return None
        if None == InfiniteUIEventType.RECALL_DELAYED:
            if num_events == 1:
                result = trans("Downloading '%(filename)s'.")
            else:
                result = ungettext('Downloading %(num_files)s file.', 'Downloading %(num_files)s files.', num_events)
        elif event_type == InfiniteUIEventType.RECALL_FINISHED:
            if num_events == 1:
                result = trans("Done downloading '%(filename)s'. Opening...")
            else:
                result = ungettext('Done downloading %(num_files)s file. Opening...', 'Done downloading %(num_files)s files. Opening...', num_events)
        elif event_type == InfiniteUIEventType.RECALL_FAILED_NETWORK:
            if num_events == 1:
                result = trans("Failed to download '%(filename)s'. Dropbox is having trouble connecting.")
            else:
                result = ungettext('Failed to download %(num_files)s file. Dropbox is having trouble connecting.', 'Failed to download %(num_files)s files. Dropbox is having trouble connecting.', num_events)
        elif event_type == InfiniteUIEventType.RECALL_FAILED_SYNC_ENGINE_PAUSED:
            if num_events == 1:
                result = trans("Failed to download '%(filename)s'. Resume syncing and try again.")
            else:
                result = ungettext('Failed to download %(num_files)s file. Resume syncing and try again.', 'Failed to download %(num_files)s files. Resume syncing and try again.', num_events)
        elif event_type == InfiniteUIEventType.RECALL_FAILED_NO_SPACE:
            if num_events == 1:
                result = trans("Failed to download '%(filename)s'. Free up space on your hard drive.")
            else:
                result = ungettext('Failed to download %(num_files)s file. Free up space on your hard drive.', 'Failed to download %(num_files)s files. Free up space on your hard drive.', num_events)
        elif event_type == InfiniteUIEventType.RECALL_FAILED:
            if num_events == 1:
                result = trans("Failed to download '%(filename)s'.")
            else:
                result = ungettext('Failed to download %(num_files)s file.', 'Failed to download %(num_files)s files.', num_events)
        elif event_type == InfiniteUIEventType.RETRIED_RECALL_FINISHED:
            if num_events == 1:
                result = trans("Click to view finished download '%(filename)s'.")
            else:
                result = ungettext('Finished downloading %(num_files)s file.', 'Finished downloading %(num_files)s files.', num_events)
        elif event_type == InfiniteUIEventType.RECALL_FAILED_OUTSIDE_DROPBOX:
            if num_events == 1:
                result = trans("'%(filename)s' is an online-only file. To open it, first move it into your Dropbox folder.")
            else:
                result = trans('These files are online-only. To open them, first move them into your Dropbox folder.')
        else:
            report_bad_assumption('Invalid infinite recall event type.', component = DesktopComponent.INFINITE)
            return None
        return None % {
            'filename': shorten_filename(requests[0].filename, 20),
            'num_files': format_number(num_events, frac_precision = 0) }

    
    def _get_event_buttons(self = None, event_type = None, requests = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_event_surface_action(self = None, event_type = None, requests = None):
        pass
    # WARNING: Decompyle incomplete

    _flush_events = (lambda self = None: if len(self._event_queue) > 0:
self._first_event_timer.start(InfiniteUIKit.EVENT_QUEUE_MAX_FLUSH_PERIOD, self._flush_events)event_type_to_requests = { }# WARNING: Decompyle incomplete
)()
    
    def _retry_recall_requests(self = None, requests = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _cancel_delayed_recall(self = None, requests = None):
        report_infinite_event(InfiniteEventType.INFINITE_RECALL_CANCELLED)
    # WARNING: Decompyle incomplete

    
    def _view_recalled_files(self = None, requests = None):
        if len(requests) == 1:
            request = requests[0]
            highlight_file(Text(request.local_path))
            return None

    
    def enter_kext_installer(self = None, source = None):
        self._ui_kit.enter_kext_installer(source)



class InfiniteUIMultiplexer(InfiniteUIDispatcherInterface, InfiniteUIControllerInterface, InfiniteUIInterface):
    pass
# WARNING: Decompyle incomplete

