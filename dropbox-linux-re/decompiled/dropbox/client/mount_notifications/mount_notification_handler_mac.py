# Source Generated with Decompyle++
# File: mount_notification_handler_mac.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import objc
from AppKit import NSNotification, NSObject, NSWorkspace, NSWorkspaceDidUnmountNotification
from Foundation import NSDistributedNotificationCenter
from dropbox.client.mount_notifications.common_event import CommonEvent, MountChangeKind
from dropbox.client.mount_notifications.mount_notification_handler_base import MountNotificationHandler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.gui import event_handler, spawn_thread_with_name
from dropbox.mac.internal import autoreleasepool
from dropbox.trace import TRACE

class EFMountNotificationHandler(MountNotificationHandler, NSObject):
    
    def __new__(cls = None):
        return EFMountNotificationHandler.alloc().init()

    
    def init(self = None):
        self = objc.super(EFMountNotificationHandler, self).init()
    # WARNING: Decompyle incomplete

    
    def dealloc(self = None):
        self.stop_listening()
        objc.super(EFMountNotificationHandler, self).dealloc()

    start_listening = (lambda self = None: pass)()
    stop_listening = (lambda self = None: try:
NSDistributedNotificationCenter.defaultCenter().removeObserver_(self)except Exception:
report_exception(component = DesktopComponent.UNKNOWN)try:
NSWorkspace.sharedWorkspace().notificationCenter().removeObserver_(self)Noneexcept Exception:
report_exception(component = DesktopComponent.UNKNOWN)None)()
    _on_volume_change_helper = (lambda self = None, notification = None: autoreleasepool()cmd = notification.name()info = notification.userInfo()device_path = info['NSDevicePath']event_kind = MountChangeKind.UNMOUNT if cmd == 'NSWorkspaceDidUnmountNotification' else MountChangeKind.UNKNOWNcommon_event = CommonEvent(device_path, event_kind)if self.on_volume_change:
self.on_volume_change(common_event)None(None, None)Nonewith None:
if not None:
pass)()
    onchanged_ = (lambda self = None, notification = objc.typedSelector(b'v@:@'): if self.on_volume_change:
spawn_thread_with_name('DISK_MOUNT_NOTIFICATION')(self._on_volume_change_helper, notification)None)()()

