# Source Generated with Decompyle++
# File: nsusernotification_builder.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
from time import time as _time
from typing import Optional, Text
from AppKit import NSAttributedString, NSImage, NSUserNotification
from Foundation import NSDictionary, NSMutableDictionary, NSNumber, NSString
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification
from dropbox.exception.reporting import report_bad_assumption

class NSUserNotificationBuilder(object):
    _user_info_dictionary_size = 16
    from_fields = (lambda cls, title, informative_text, pid, is_persistent, notification_id, loud_notification_type, is_contextless, display_time, surface_action, has_content_image, image_content, avatar_image, has_buttons, action_button_title, button_action, can_reply, reply_callback = None, activation_type = None, response = classmethod, should_deliver = (None, None, False, None), bluenote_id = ('title', 'Optional[Text]', 'informative_text', 'Text', 'pid', 'Text', 'is_persistent', 'bool', 'notification_id', 'Text', 'loud_notification_type', 'Text', 'is_contextless', 'bool', 'display_time', 'float', 'surface_action', 'Optional[Text]', 'has_content_image', 'bool', 'image_content', 'Optional[NSImage]', 'avatar_image', 'Optional[NSImage]', 'has_buttons', 'bool', 'action_button_title', 'Optional[Text]', 'button_action', 'Optional[Text]', 'can_reply', 'bool', 'reply_callback', 'Optional[Text]', 'activation_type', 'Optional[int]', 'response', 'Optional[Text]', 'should_deliver', 'bool', 'bluenote_id', 'Optional[int]', 'return', 'NSUserNotification'): user_notification = NSUserNotification.alloc().init()if not user_notification:
None# WARNING: Decompyle incomplete
)()
    from_loud_notification = (lambda cls = None, loud_notification = None, avatar_image = classmethod, should_deliver = (None, False): title = Noneif len(loud_notification.caption) > 0:
title = loud_notification.captioninformative_text = loud_notification.msgpid = Text(os.getpid())is_persistent = loud_notification.is_persistentnotification_id = loud_notification.idloud_notification_type = loud_notification.loud_notification_type.valueis_contextless = Falsedisplay_time = _time()surface_action = None# WARNING: Decompyle incomplete
)()
    _set_image_content = (lambda user_notification = None, image_content = None: user_notification.setContentImage_(image_content))()
    _set_avatar = (lambda user_notification = None, avatar_image = None: if not user_notification.respondsToSelector_('set_identityImage:'):
report_bad_assumption("Can't show avatar since set_identityImage is not defined.")NoneNone.set_identityImage_(avatar_image)user_notification.set_identityImageHasBorder_(False))()
    _set_buttons = (lambda user_notification = None, action_button_title = None, button_action = staticmethod, user_info = ('user_notification', 'NSUserNotification', 'action_button_title', 'Text', 'button_action', 'Text', 'user_info', 'NSDictionary[Text, Text]', 'return', 'None'): if not user_notification.respondsToSelector_('set_showsButtons:'):
report_bad_assumption("Can't use showsButtons to change alert style")NoneNone.set_showsButtons_(True)user_notification.setHasActionButton_(True)user_notification.setActionButtonTitle_(action_button_title)user_info['button_action'] = NSString.stringWithString_(button_action))()
    _set_reply_callback = (lambda user_notification = None, reply_callback = None, user_info = staticmethod: user_notification.setHasReplyButton_(True)user_info['reply_callback'] = NSString.stringWithString_(reply_callback))()
    _disable_show_button = (lambda user_notification = None: user_notification.setHasActionButton_(False))()

