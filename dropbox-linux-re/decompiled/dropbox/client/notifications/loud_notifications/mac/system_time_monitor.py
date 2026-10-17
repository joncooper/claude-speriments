# Source Generated with Decompyle++
# File: system_time_monitor.pyc (Python 3.11)

from __future__ import absolute_import
from typing import Any, Callable
import objc
from AppKit import NSNotificationCenter, NSObject, NSSystemClockDidChangeNotification
from dropbox.callbacks import Handler
from dropbox.client.notifications.loud_notifications.interfaces import SystemTimeMonitor
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import event_handler
from dropbox.mac.internal import autoreleasepool
from dropbox.trace import TRACE

class MacSystemTimeMonitor(SystemTimeMonitor):
    
    def __init__(self = None):
        self._time_change_handler = Handler(handle_exc = report_exception)
        self._notifier = EFTimeChangeNotifier(self)

    
    def add_time_changed_callback(self = None, callback = None):
        self._time_change_handler.add_handler(callback)

    
    def remove_time_changed_callback(self = None, callback = None):
        self._time_change_handler.remove_handler(callback)



class EFTimeChangeNotifier(NSObject):
    
    def __new__(cls, tracker):
        autoreleasepool()
        None(None, None)
        return 
        with None:
            if not None, EFTimeChangeNotifier.alloc().initWithTracker_(tracker):
                pass

    
    def initWithTracker_(self, tracker):
        self = objc.super(EFTimeChangeNotifier, self).init()
    # WARNING: Decompyle incomplete

    
    def dealloc(self):
        
        try:
            NSNotificationCenter.defaultCenter().removeObserver_(self)
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.NATIVE_NOTIFICATIONS)

        objc.super(EFTimeChangeNotifier, self).dealloc()

    timeChanged_ = (lambda self, notification: TRACE('SystemTimeChangeMonitor reporting a time change event')self._tracker._time_change_handler.run_handlers())()()

