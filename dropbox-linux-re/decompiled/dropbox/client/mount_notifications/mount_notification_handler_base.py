# Source Generated with Decompyle++
# File: mount_notification_handler_base.pyc (Python 3.11)

from typing import Callable, Optional
from dropbox.client.mount_notifications.common_event import CommonEvent

class MountNotificationHandler:
    
    def __init__(self = None):
        self.on_volume_change = None

    
    def set_volume_change_handler(self = None, handler = None):
        self.on_volume_change = handler

    
    def start_listening(self = None):
        raise NotImplementedError('This method should be implemented by subclasses')

    
    def stop_listening(self = None):
        raise NotImplementedError('This method should be implemented by subclasses')


