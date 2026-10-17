# Source Generated with Decompyle++
# File: user_notification_ui_base.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import os
from typing import Callable, Iterable, List, Optional, Text
import objc
from AppKit import NSImage, NSObject, NSUserNotification, NSUserNotificationActivationTypeActionButtonClicked, NSUserNotificationActivationTypeContentsClicked, NSUserNotificationCenter
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.constants import LoudNotificationActivationType
from dropbox.client.notifications.loud_notifications.events import NoInteractionWhenPoppedReason, report_failed_to_send_xpc_notification, report_notclicked_bubble, report_sent_xpc_notification
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId, LoudNotificationType
from dropbox.client.notifications.loud_notifications.mac.alternate_notifier import AlternateNotifier
from dropbox.client.notifications.loud_notifications.mac.nsusernotification_builder import NSUserNotificationBuilder
from dropbox.client.notifications.loud_notifications.types import BubbleContextRef
from dropbox.client.ui.common.uikit import ensure_on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.gui import assert_message_queue
from dropbox.mac.typed_objc import typed_python_method
from dropbox.mac.version import HIGH_SIERRA, MAC_VERSION
from dropbox.trace import TRACE
NSUserNotificationActivationTypeActionReplied = 3
ClickCallback = Callable[([
    bool,
    bool,
    float,
    LoudNotificationType,
    LoudNotificationId,
    Optional[BubbleContextRef],
    Optional[LoudNotificationActivationType],
    Optional[Text]], None)]
GetDisplayedNotificationsCallback = Callable[([
    Iterable[Text]], None)]

class EFUserNotificationUIBase(NSObject):
    __new__ = (lambda cls = None, click_callback = None: EFUserNotificationUIBase.alloc().initWithClickCallback_(click_callback))()
    
    def initWithClickCallback_(self = None, click_callback = None):
        self = objc.super(EFUserNotificationUIBase, self).init()
    # WARNING: Decompyle incomplete

    is_using_alternate_notifier = (lambda self = None: self._alternate_notifier is not None)()
    _on_gandalf_changed = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    set_gandalf = (lambda self = None, gandalf = None: self._gandalf = gandalfself._gandalf.add_on_changed_callback_any_account(self._on_gandalf_changed))()
    clear_all_notifications = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    clear_notification = (lambda self = None, loud_notification_id = None: pass# WARNING: Decompyle incomplete
)()
    displayed_notification_ids = (lambda self = None: [])()
    get_displayed_notification_ids_with_callback = (lambda self = None, displayed_notifications_callback = None: pass)()
    render_user_notification = (lambda self = None, loud_notification = typed_python_method, avatar_image = ensure_on_ui_thread(): pass)()()
    _send_to_service = (lambda self = None, loud_notification = None, avatar_image = typed_python_method: pass# WARNING: Decompyle incomplete
)()
    on_NSUserNotification_delivered = (lambda self = None, notification = typed_python_method: try:
if not notification.isPresented():
user_info = notification.userInfo()if not user_info:
report_bad_assumption("Processed a notification that didn't have a userInfo.")Nonereport_notclicked_bubble(LoudNotificationType(user_info.get('loud_notification_type')), None, NoInteractionWhenPoppedReason.UNKNOWN, notification.isPresented(), user_info.get('bluenote_id'))NoneNoneexcept Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.NATIVE_NOTIFICATIONS)None)()()
    on_NSUserNotification_activated = (lambda self = None, notification = None: pass# WARNING: Decompyle incomplete
)()

