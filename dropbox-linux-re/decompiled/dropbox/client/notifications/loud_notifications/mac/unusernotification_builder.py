# Source Generated with Decompyle++
# File: unusernotification_builder.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from time import time as _time
from typing import List, Optional, Set, Text
from AppKit import NSBitmapImageRep, NSImage, NSPNGFileType, NSURL
from Foundation import NSMakeRect, NSMutableDictionary, NSNumber, NSProcessInfo, NSString, NSTemporaryDirectory
from UserNotifications import UNMutableNotificationContent, UNNotificationAction, UNNotificationActionOptionNone, UNNotificationAttachment, UNNotificationCategory, UNNotificationCategoryOptionCustomDismissAction, UNNotificationIcon, UNNotificationRequest, UNTextInputNotificationAction, UNUserNotificationCenter
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, ReplyButtonInNotificationParams
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.mac.internal import autoreleasepool
from dropbox.trace import TRACE

class UNUserNotificationBuilder:
    _user_info_dictionary_size = 16
    _global_categories: 'Set[UNNotificationCategory]' = set([])
    _global_category_identifiers: 'Set[str]' = set([])
    write_image_to_tempfile = (lambda cls = None, image = None: autoreleasepool()path = Noneimage.lockFocus()bitmap_rep = NSBitmapImageRep.alloc().initWithFocusedViewRect_(NSMakeRect(0, 0, image.size().width, image.size().height))image.unlockFocus()if bitmap_rep:
png_img = bitmap_rep.representationUsingType_properties_(NSPNGFileType, None)if png_img:
path = f'''{NSTemporaryDirectory()}/{NSProcessInfo.processInfo().globallyUniqueString()}.png'''png_img.writeToFile_atomically_(path, True)else:
except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.NATIVE_NOTIFICATIONS)None(None, None)with None:
if not None:
pass)()
    from_fields = (lambda cls, title, informative_text, pid, is_persistent, notification_id, loud_notification_type, is_contextless, display_time, surface_action, has_content_image, image_content, avatar_image, has_buttons, action_button_titles, button_actions, can_reply, reply_callback, reply_button_params, can_handle_dismiss, dismiss_callback, use_attachments = None, activation_type = None, response = classmethod, should_deliver = (None, None, False, None), bluenote_id = ('title', 'Optional[Text]', 'informative_text', 'Text', 'pid', 'Text', 'is_persistent', 'bool', 'notification_id', 'Text', 'loud_notification_type', 'Text', 'is_contextless', 'bool', 'display_time', 'float', 'surface_action', 'Optional[Text]', 'has_content_image', 'bool', 'image_content', 'Optional[NSImage]', 'avatar_image', 'Optional[NSImage]', 'has_buttons', 'bool', 'action_button_titles', 'Optional[List[Text]]', 'button_actions', 'Optional[List[Text]]', 'can_reply', 'bool', 'reply_callback', 'Optional[Text]', 'reply_button_params', 'Optional[ReplyButtonInNotificationParams]', 'can_handle_dismiss', 'bool', 'dismiss_callback', 'Optional[Text]', 'use_attachments', 'bool', 'activation_type', 'Optional[int]', 'response', 'Optional[Text]', 'should_deliver', 'bool', 'bluenote_id', 'Optional[int]', 'return', 'UNNotificationRequest'): pass# WARNING: Decompyle incomplete
)()
    from_loud_notification = (lambda cls = None, loud_notification = None, avatar_image = classmethod, use_attachments = (False,), should_deliver = ('loud_notification', 'LoudNotification', 'avatar_image', 'Optional[NSImage]', 'use_attachments', 'bool', 'should_deliver', 'bool', 'return', 'UNNotificationRequest'): title = Noneif len(loud_notification.caption) > 0:
title = loud_notification.captioninformative_text = loud_notification.msgpid = Text(os.getpid())is_persistent = loud_notification.is_persistentnotification_id = loud_notification.idloud_notification_type = loud_notification.loud_notification_type.valueis_contextless = Falsedisplay_time = _time()surface_action = None# WARNING: Decompyle incomplete
)()

