# Source Generated with Decompyle++
# File: cf_dialog.pyc (Python 3.11)

from typing import Text
from CoreFoundation import CFUserNotificationCancel, CFUserNotificationCreate, kCFAllocatorDefault, kCFUserNotificationAlertHeaderKey, kCFUserNotificationAlertMessageKey, kCFUserNotificationNoteAlertLevel

class CFMacDialog:
    
    def __init__(self = None):
        self.mac_notification = None

    
    def display_mac_notification(self = None, caption = None, message = None):
        keys = [
            kCFUserNotificationAlertHeaderKey,
            kCFUserNotificationAlertMessageKey]
        values = [
            caption,
            message]
        dictionary = dict(zip(keys, values))
        (self.mac_notification, _) = CFUserNotificationCreate(kCFAllocatorDefault, 0, kCFUserNotificationNoteAlertLevel, None, dictionary)

    
    def destroy_mac_notification(self = None):
        CFUserNotificationCancel(self.mac_notification)


