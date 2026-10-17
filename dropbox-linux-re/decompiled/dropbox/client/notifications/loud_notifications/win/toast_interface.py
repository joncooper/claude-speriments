# Source Generated with Decompyle++
# File: toast_interface.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from enum import Enum
from typing import Callable, Dict, Optional, Text
from dropbox.client.notifications.loud_notifications.constants import LoudNotificationActivationType
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId, LoudNotificationType
from dropbox.client.notifications.loud_notifications.types import BubbleContextRef

class ActivatedToast(object):
    
    def __init__(self, is_same_process, is_contextless, display_time = None, loud_notification_type = None, ctxt_ref = None, activation_type = (None,), inputs = ('is_same_process', 'bool', 'is_contextless', 'bool', 'display_time', 'float', 'loud_notification_type', 'LoudNotificationType', 'ctxt_ref', 'BubbleContextRef', 'activation_type', 'LoudNotificationActivationType', 'inputs', 'Optional[Dict[Text, Text]]', 'return', 'None')):
        self.is_same_process = is_same_process
        self.is_contextless = is_contextless
        self.display_time = display_time
        self.loud_notification_type = loud_notification_type
        self.ctxt_ref = ctxt_ref
        self.activation_type = activation_type
        self.inputs = inputs



class DisplayToastResult(Enum):
    DISPLAYED = 0
    QUEUED = 1
    REJECTED_BY_OS = 2
    REJECTED_BY_APP = 3
    FAILED = 4


class ToastNotifierInterface(object):
    
    def render_toast(self = None, loud_notification = None, avatar_filepath = None, toast_rendered_callback = (None, None)):
        pass

    
    def render_toast_same_thread(self = None, loud_notification = None, avatar_filepath = None, toast_rendered_callback = (None, None)):
        pass

    
    def hide_toast(self = None, loud_notification_id = None):
        pass


