# Source Generated with Decompyle++
# File: mount_notification_handler.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import objc
from AppKit import NSObject, NSWorkspace, NSWorkspaceDidMountNotification, NSWorkspaceDidUnmountNotification
from Foundation import NSDistributedNotificationCenter
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.gui import event_handler, spawn_thread_with_name
from dropbox.trace import TRACE

class MountNotificationHandler(NSObject):
    
    def __new__(cls):
        return MountNotificationHandler.alloc().init()

    
    def __init__(self):
        self.on_volume_change = None
        notification_center = NSWorkspace.sharedWorkspace().notificationCenter()
        notification_center.addObserver_selector_name_object_(self, 'onchanged:', NSWorkspaceDidMountNotification, None)
        notification_center.addObserver_selector_name_object_(self, 'onchanged:', NSWorkspaceDidUnmountNotification, None)
        TRACE('MountNotificationHandler: initialized.')

    
    def dealloc(self):
        
        try:
            NSDistributedNotificationCenter.defaultCenter().removeObserver_(self)
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)

        
        try:
            NSWorkspace.sharedWorkspace().notificationCenter().removeObserver_(self)
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)

        objc.super(MountNotificationHandler, self).dealloc()

    set_volume_change_handler = (lambda self, handler: self.on_volume_change = handler)()
    onchanged_ = (lambda self, notification: if self.on_volume_change:
spawn_thread_with_name('DISK_MOUNT_NOTIFICATION')(self.on_volume_change)None)()()

