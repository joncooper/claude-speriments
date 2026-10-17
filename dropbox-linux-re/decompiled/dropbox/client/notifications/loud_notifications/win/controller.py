# Source Generated with Decompyle++
# File: controller.pyc (Python 3.11)

import time
from typing import Any, Callable, Optional, Text, Tuple
from regutils import is_dropbox_banners_disabled, is_quiet_hours_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.desktop_login import DesktopLogin
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.constants import ToastDismissedReason
from dropbox.client.notifications.loud_notifications.events import BubbleClickInfo, report_click_bubble, report_show_bubble
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId, LoudNotificationType
from dropbox.client.notifications.loud_notifications.win.toast_interface import ActivatedToast, DisplayToastResult, ToastNotifierInterface
from dropbox.client.notifications.notification_adapter import UserNotificationControllerAdapter
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.client.ui.win32.avatar_cache import AvatarCache
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import lrudict
from dropbox.trace import TRACE
from dropbox.win32.version import WIN10, WINDOWS_VERSION
if WINDOWS_VERSION.version_number() >= WIN10.version_number():
    from toast_startmenu_verifier import ToastStartMenuVerifier
    from dropbox.client.notifications.loud_notifications.win.toast import ContextLessActionArgument, WindowsToastNotifier

class LoudNotificationController(object):
    _LAST_SHOWN_CAPACITY = 5
    _LAST_SHOWN_DURATION = 43200
    _DISMISS_CACHE_SIZE = 50
    
    def __init__(self, bubble_context = None, conn = None, desktop_login = None, notification_controller_adapter = ('bubble_context', 'BubbleContext', 'conn', 'DropboxConnection', 'desktop_login', 'DesktopLogin', 'notification_controller_adapter', 'UserNotificationControllerAdapter', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def clear_toasts_for_account(self = None, account = None):
        if self._toast_ui_win10:
            self._toast_ui_win10.clear_toasts(account)
            return None

    
    def use_alt_toast_notifier_for_bypass_silent_mode(self = None):
        if WINDOWS_VERSION.version_number() < WIN10.version_number():
            return False
        if is_quiet_hours_enabled() or is_dropbox_banners_disabled():
            return True
        return not ToastStartMenuVerifier.is_valid()

    
    def get_toast_notifier(self = None, loud_notification = None):
        if not self._toast_ui_alt:
            return self._toast_ui
        if None.bypass_silent_mode and self.use_alt_toast_notifier_for_bypass_silent_mode():
            return self._toast_ui_alt
        return None._toast_ui

    
    def set_gandalf(self = None, gandalf = None):
        self._gandalf = gandalf
        if self._gandalf:
            
            try:
                self._gandalf.add_on_changed_callback_any_account(self._on_gandalf_changed)
            except Exception:
                report_exception(severity = Severity.WARN, component = DesktopComponent.NATIVE_NOTIFICATIONS)

            if self._toast_ui_win10:
                self._toast_ui_win10.set_gandalf(gandalf)
                return None
            return None

    
    def _on_gandalf_changed(self = None):
        self._configure_toast_ui()

    
    def _configure_toast_ui(self = None):
        if WINDOWS_VERSION.version_number() >= WIN10.version_number():
            self._toast_ui = self._toast_ui_win10
            self._toast_ui_alt = None
            return None

    
    def is_supported(self = None, loud_notification = None):
        if not self._toast_ui:
            return (False, 'Toast UI is undefined')

    _render_toast = (lambda self = None, loud_notification = None, avatar_filepath = on_ui_thread, toast_rendered_callback = (None, None): toast_notifier = self.get_toast_notifier(loud_notification)if not toast_notifier:
Noneresult = None.render_toast_same_thread(loud_notification, avatar_filepath = avatar_filepath, toast_rendered_callback = toast_rendered_callback)if (result == DisplayToastResult.FAILED or result == DisplayToastResult.REJECTED_BY_OS) and loud_notification.bypass_silent_mode and self._toast_ui_alt and toast_notifier != self._toast_ui_alt:
self._toast_ui_alt.render_toast_same_thread(loud_notification, avatar_filepath = avatar_filepath, toast_rendered_callback = toast_rendered_callback)Noneif None != DisplayToastResult.DISPLAYED or result != DisplayToastResult.QUEUED:
if toast_rendered_callback:
toast_rendered_callback(False)NoneNone)()
    
    def _hide_toast(self = None, loud_notification_id = None):
        if self._toast_ui or self._toast_ui.hide_toast(loud_notification_id) or self._toast_ui_alt:
            self._toast_ui_alt.hide_toast(loud_notification_id)
            return None
        return None
        return None

    
    def show_loud_notification(self = None, loud_notification = None):
        pass
    # WARNING: Decompyle incomplete

    
    def clear_notification(self = None, loud_notification_id = None):
        if not self._toast_ui:
            return None
        None._hide_toast(loud_notification_id)

    _on_notification_activated = (lambda self = None, info = None: if info.is_same_process:
try:
answer = info.inputs['answer'] if info.inputs and 'answer' in info.inputs else Noneif answer == '':
answer = Noneclick_info = BubbleClickInfo(display_time = info.display_time, is_contextless = info.is_contextless, is_same_process = info.is_same_process, has_action = True)self._bubble_context.thunk_and_expire_context_ref(click_info, info.ctxt_ref, answer)Noneexcept KeyError:
report_exception(severity = Severity.DEBUG, component = DesktopComponent.NATIVE_NOTIFICATIONS)Noneexcept Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.NATIVE_NOTIFICATIONS)Nonereport_click_bubble(info.loud_notification_type, BubbleClickInfo(display_time = info.display_time, is_contextless = info.is_contextless, is_same_process = info.is_same_process, has_action = True), None)uri_fragment = Noneif info.loud_notification_type == LoudNotificationType.QUOTA_EXCEEDED:
uri_fragment = 'out-of-space?oqa=dt_oq_ln'elif info.loud_notification_type == LoudNotificationType.QUOTA_WARNING:
uri_fragment = 'low-space?oqa=dt_nq_ln'else:
TRACE('The notification that was clicked came from a previous Dropbox session.')NoneTRACE('Over-quota notification hack')try:
self._desktop_login.login_and_redirect(uri_fragment)Noneexcept Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.NATIVE_NOTIFICATIONS)None)()
    _on_notification_dismissed = (lambda self = None, loud_notification_id = None, reason = on_ui_thread: TRACE('Notification dismissed with reason %r: %r', reason.name, loud_notification_id)if loud_notification_id or loud_notification_id in self._dismiss_callbacks:
callback = self._dismiss_callbacks.pop(loud_notification_id)if reason == ToastDismissedReason.UserCanceled:
callback()NoneNoneNone)()

