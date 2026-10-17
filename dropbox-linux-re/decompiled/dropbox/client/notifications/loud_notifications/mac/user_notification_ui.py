# Source Generated with Decompyle++
# File: user_notification_ui.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import List, Optional, Text
import objc
from AppKit import NSImage, NSUserNotification, NSUserNotificationCenter
from dropbox.client.notifications.loud_notifications.events import NoInteractionWhenPoppedReason, report_notclicked_bubble
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification
from dropbox.client.notifications.loud_notifications.mac.nsusernotification_builder import NSUserNotificationBuilder
from dropbox.client.notifications.loud_notifications.mac.user_notification_ui_base import ClickCallback, EFUserNotificationUIBase, GetDisplayedNotificationsCallback
from dropbox.client.ui.common.uikit import ensure_on_ui_thread
from dropbox.gui import assert_message_queue
from dropbox.mac.typed_objc import typed_python_method
from dropbox.trace import TRACE
NSUserNotificationActivationTypeActionReplied = 3

class EFUserNotificationUI(EFUserNotificationUIBase):
    __new__ = (lambda cls = None, click_callback = None: EFUserNotificationUI.alloc().initWithClickCallback_(click_callback))()
    
    def initWithClickCallback_(self = None, click_callback = None):
        self = objc.super(EFUserNotificationUI, self).initWithClickCallback_(click_callback)
    # WARNING: Decompyle incomplete

    userNotificationCenter_shouldPresentNotification_ = (lambda self = None, center = objc.typedSelector(b'Z@:@@'), notification = assert_message_queue: True)()()
    userNotificationCenter_didDeliverNotification_ = (lambda self = None, center = objc.typedSelector(b'v@:@@'), notification = assert_message_queue: self.on_NSUserNotification_delivered(notification))()()
    userNotificationCenter_didActivateNotification_ = (lambda self = None, center = objc.typedSelector(b'v@:@@'), notification = assert_message_queue: self.on_NSUserNotification_activated(notification))()()
    clear_all_notifications = (lambda self = None: objc.super(EFUserNotificationUI, self).clear_all_notifications()NSUserNotificationCenter.defaultUserNotificationCenter().removeAllDeliveredNotifications())()
    clear_notification = (lambda self = None, loud_notification_id = None: objc.super(EFUserNotificationUI, self).clear_notification(loud_notification_id)displayed_notifications = NSUserNotificationCenter.defaultUserNotificationCenter().deliveredNotifications()if not displayed_notifications:
Nonefor user_notification in None:
if user_notification.userInfo()['id'] == loud_notification_id:
NSUserNotificationCenter.defaultUserNotificationCenter().removeDeliveredNotification_(user_notification)NoneNone)()
    get_displayed_notification_ids_with_callback = (lambda self = None, displayed_notifications_callback = None: displayed_notifications = NSUserNotificationCenter.defaultUserNotificationCenter().deliveredNotifications()if not displayed_notifications:
None(lambda .0: pass# WARNING: Decompyle incomplete
)(displayed_notifications())
)()
    displayed_notification_ids = (lambda self = None: 