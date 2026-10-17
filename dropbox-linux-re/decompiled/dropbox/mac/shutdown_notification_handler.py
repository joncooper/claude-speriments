# Source Generated with Decompyle++
# File: shutdown_notification_handler.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import objc
from AppKit import NSObject, NSWorkspace, NSWorkspaceWillPowerOffNotification
from objc import typedSelector
from dropbox.callbacks import Handler
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import event_handler
from dropbox.trace import TRACE

class ShutDownNotificationHandler(NSObject):
    
    def init(self):
        self = objc.super(ShutDownNotificationHandler, self).init()
    # WARNING: Decompyle incomplete

    
    def dealloc(self):
        
        try:
            NSWorkspace.sharedWorkspace().notificationCenter().removeObserver_(self)
        except Exception:
            report_exception(severity = Severity.TRACE, component = DesktopComponent.UNKNOWN)

        objc.super(ShutDownNotificationHandler, self).dealloc()

    add_shutdown_callback = (lambda self, callback: self._shutdown_callbacks.add_handler(callback))()
    onPowerOff_ = (lambda self, notification: TRACE('ShutDownNotificationHandler: about to power off')self._shutdown_callbacks.run_handlers())()()

