# Source Generated with Decompyle++
# File: mount_notification_handler_factory.pyc (Python 3.11)

from typing import Optional
from apex.metrics import MetricsReporter
from dropbox.client.mount_notifications.mount_notification_handler_base import MountNotificationHandler
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE

class MountNotificationHandlerFactory:
    
    def __init__(self = None, metrics_reporter = None):
        self.metrics_reporter = metrics_reporter

    
    def get_mount_notification_handler(self = None):
        if IS_MAC:
            EFMountNotificationHandler = EFMountNotificationHandler
            import dropbox.client.mount_notifications.mount_notification_handler_mac
            return EFMountNotificationHandler()
        if None:
            MountNotificationHandlerWin = MountNotificationHandlerWin
            import dropbox.client.mount_notifications.mount_notification_handler_win
            return MountNotificationHandlerWin(self.metrics_reporter)
        TRACE('Unsupported platform for mount notifications')


