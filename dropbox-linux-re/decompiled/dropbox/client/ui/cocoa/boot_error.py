# Source Generated with Decompyle++
# File: boot_error.pyc (Python 3.11)

from __future__ import absolute_import
from threading import Event
import objc
from AppKit import NSAlert, NSApplication, NSCriticalAlertStyle, NSTextField, NSWorkspace
from Foundation import NSAutoreleasePool, NSObject, NSURL, NSWidth
from PyObjCTools import AppHelper
from dropbox_controls import TextFieldWithLink
from dropbox.client.util import hard_exit
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.mac.internal import raise_application
from dropbox.trace import TRACE

class BootErrorAlert(object):
    runModal = (lambda self, title, message, help_link, text = ('',): pool = NSAutoreleasePool.alloc().init()try:
app = NSApplication.sharedApplication()if app.isRunning():
death_event = Event()app_delegate = BootErrorAppDelegate(title, message, help_link, text, death_event)AppHelper.callAfter(app_delegate.applicationWillFinishLaunching_, None)death_event.wait()else:
AppHelper.installMachInterrupt()app_delegate = BootErrorAppDelegate(title, message, help_link, text, None)app.setDelegate_(app_delegate)AppHelper.runEventLoop()del poolNoneexcept:
del pool)()


class BootErrorAppDelegate(NSObject):
    
    def __new__(cls, title, message, help_link, text, done_event):
        return BootErrorAppDelegate.alloc().initWithTitle_message_helpLink_tracebackText_doneEvent_(title, message, help_link, text, done_event)

    
    def initWithTitle_message_helpLink_tracebackText_doneEvent_(self, title, message, help_link, text, done_event):
        self = objc.super(BootErrorAppDelegate, self).init()
    # WARNING: Decompyle incomplete

    
    def applicationWillFinishLaunching_(self, notification):
        AppHelper.callAfter(self.alertLoop)

    
    def alertLoop(self):
        raise_application()
        alert = NSAlert.alertWithMessageText_defaultButton_alternateButton_otherButton_informativeTextWithFormat_(self._title, None, None, None, self._message)
        alert.setAlertStyle_(NSCriticalAlertStyle)
        if self._help_link:
            alert.setShowsHelp_(True)
            alert.setHelpAnchor_(self._help_link)
            alert.setDelegate_(self)
        if hasattr(alert, 'setAccessoryView_') and self._text:
            alert.setAccessoryView_(self._create_accessory_view(alert))
        alert.runModal()
        if self._done_event:
            AppHelper.stopEventLoop()
            self._done_event.set()
            return None
        hard_exit(ExitCode.FATAL_EXCEPTION, reason = 'boot error')

    _create_accessory_view = (lambda self, alert: text_width = 0font = None# WARNING: Decompyle incomplete
)()
    
    def alertShowHelp_(self, alert):
        TRACE('Help button clicked on boot error dialog')
        help_link = alert.helpAnchor()
    # WARNING: Decompyle incomplete


