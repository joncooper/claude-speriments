# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import uuid
from contextlib import suppress
from functools import partial
from typing import Any, Dict, Iterable, List, Optional, Text
from uuid import UUID
from AppKit import NSImage
from PyObjCTools import AppHelper
from six.moves.queue import Empty, Queue
from build_number import dropbox_version
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventClass
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.constants import LoudNotificationActivationType
from dropbox.client.notifications.loud_notifications.events import BubbleClickInfo, NoInteractionWhenPoppedReason, report_click_bubble, report_notclicked_bubble, report_show_bubble
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId, LoudNotificationType
from dropbox.client.notifications.loud_notifications.mac.avatar import get_avatar_image_async
from dropbox.client.notifications.loud_notifications.mac.user_notification_ui import EFUserNotificationUI
from dropbox.client.notifications.loud_notifications.mac.user_notification_ui_base import EFUserNotificationUIBase, GetDisplayedNotificationsCallback
from dropbox.client.notifications.loud_notifications.types import BubbleContextRef
from dropbox.client.ui.common.uikit import ensure_on_ui_thread, on_ui_thread, on_ui_thread_blocking
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC
from dropbox.threadutils import is_main_thread
from dropbox.trace import TRACE
from dropbox.webdebugger.server import WebDebugger
if IS_MAC:
    from dropbox.mac.version import HIGH_SIERRA, MAC_VERSION, MOJAVE

class LoudNotificationController(object):
    DEFAULT_POPUP_DURATION = 5
    DEBUG_DELIVERED_NOTIFICATIONS_TIMEOUT_SECONDS = 4
    MAX_QUEUE_SIZE_INTERNAL = 10
    MAX_QUEUE_SIZE = 100
    
    def __init__(self = None, bubble_context = None, local_config = None):
        self._bubble_context = bubble_context
        self._local_config = local_config
        self._current_notifications = { }
        self._ready_to_display_next_notif = True
        self._callback_mapping = { }
        self._pending_notifications = Queue()
        self._max_queue_size = self.MAX_QUEUE_SIZE_INTERNAL if dropbox_version.is_internal_alpha() else self.MAX_QUEUE_SIZE
        self._gandalf = None
        self._ui = None
        self._initialize_notification_ui_if_needed()
        if WebDebugger.is_enabled():
            WebDebugger.register('notifications/get_delivered_mac_notification_texts', self._debug_get_delivered_notification_texts)
            return None

    
    def _debug_get_delivered_notification_texts(self = None):
        pass
    # WARNING: Decompyle incomplete

    _debug_request_displayed_notification_ids = (lambda self = None, displayed_notifications_callback = None: pass# WARNING: Decompyle incomplete
)()
    _initialize_notification_ui_if_needed = (lambda self = None: if self._ui:
TRACE('[_initialize_notification_ui_if_needed] Notification UI already initialized.')Noneuse_modern_notification_ui = None >= MOJAVEif not use_modern_notification_ui:
self._ui = EFUserNotificationUI(self._on_notification_click)# WARNING: Decompyle incomplete
)()
    
    def set_gandalf(self = None, gandalf = None):
        pass
    # WARNING: Decompyle incomplete

    _on_notification_click = (lambda self, is_same_process, is_contextless, display_time, loud_notification_type = None, loud_notification_id = None, action_ctxt_ref = on_ui_thread, activation_type = (None,), reply_message = ('is_same_process', 'bool', 'is_contextless', 'bool', 'display_time', 'float', 'loud_notification_type', 'LoudNotificationType', 'loud_notification_id', 'LoudNotificationId', 'action_ctxt_ref', 'Optional[BubbleContextRef]', 'activation_type', 'Optional[LoudNotificationActivationType]', 'reply_message', 'Optional[Text]', 'return', 'None'): click_info = BubbleClickInfo(display_time = display_time, is_contextless = is_contextless, is_same_process = is_same_process, has_action = action_ctxt_ref is not None)loud_notification = self._current_notifications.get(loud_notification_id)bluenote_id = loud_notification.bluenote_id if loud_notification else Noneif not is_same_process:
TRACE('The notification that was clicked came from a previous Dropbox session.')report_click_bubble(loud_notification_type, click_info, bluenote_id)NoneNone.clear_notification(loud_notification_id)# WARNING: Decompyle incomplete
)()
    
    def _reset_non_persistent_notifications_and_show_next(self = None, loud_notification = None):
        self._pending_notifications = Queue()
        self._ready_to_display_next_notif = True
        current_notification_ids = list(self._current_notifications.keys())
        for notification_id in current_notification_ids:
            if not self._current_notifications[notification_id].is_persistent:
                formatted_notification_id = self._current_notifications[notification_id].id
                self.clear_notification(formatted_notification_id)
            self.show_loud_notification(loud_notification)
            return None

    
    def show_loud_notification(self = None, loud_notification = None):
        if not self._ui:
            TRACE('[show_loud_notification] Not showing notification since the UI is not initialized.')
            return None
    # WARNING: Decompyle incomplete

    
    def _show_loud_notification(self = None, loud_notification = None, avatar_image = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_transient_popup_duration(self = None):
        duration = self.DEFAULT_POPUP_DURATION
        if self._gandalf:
            pass
        variant = self._gandalf.get_variant('desktop-mac-loud-notification-duration')
        if variant:
            
            try:
                duration = int(variant)
            except ValueError:
                pass

        return duration if duration > 0 else self.DEFAULT_POPUP_DURATION

    
    def _clear_notification_via_callback(self = None, loud_notification_id = None, clear_callback_id = None):
        if clear_callback_id and self._callback_mapping.get(loud_notification_id) != clear_callback_id:
            return None
        
        try:
            loud_notification = self._current_notifications[loud_notification_id]
            report_notclicked_bubble(loud_notification.loud_notification_type, None, NoInteractionWhenPoppedReason.TIMED_OUT, 0, loud_notification.bluenote_id)
        except KeyError:
            return None

        self.clear_notification(loud_notification_id)

    
    def _display_next_notification_via_callback(self = None, loud_notification_id = None, clear_callback_id = None):
        if clear_callback_id and self._callback_mapping.get(loud_notification_id) != clear_callback_id:
            return None
        self._ready_to_display_next_notif = None
        self._display_next_notification()

    
    def clear_notification(self = None, loud_notification_id = None):
        if not self._ui:
            TRACE('[show_loud_notification] Not clearing notification since the UI is not initialized.')
            return None
        
        try:
            loud_notification = self._current_notifications.pop(loud_notification_id)
        except KeyError:
            return None

        self._ui.clear_notification(loud_notification_id)
        self._callback_mapping.pop(loud_notification_id, None)
        if not loud_notification.is_persistent:
            self._ready_to_display_next_notif = True
            self._display_next_notification()
            return None

    
    def _display_next_notification(self = None):
        if not self._ready_to_display_next_notif:
            report_bad_assumption('_display_next_notification() called at inappropriate time', component = DesktopComponent.NATIVE_NOTIFICATIONS)
        suppress(Empty)
        loud_notification = self._pending_notifications.get(False)
        self.show_loud_notification(loud_notification)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def _clear_dismissed_persistent_notifications(self = None):
        pass
    # WARNING: Decompyle incomplete


