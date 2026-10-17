# Source Generated with Decompyle++
# File: system_status.pyc (Python 3.11)

from __future__ import absolute_import
import time
from typing import Any, Callable, Optional
import objc
from AppKit import NSDistributedNotificationCenter, NSNotification, NSObject, NSWorkspace, NSWorkspaceDidWakeNotification, NSWorkspaceWillSleepNotification
from dropbox.callbacks import Handler
from dropbox.client.system_status.system_status_monitor_interface import SystemStatusMonitorTestingInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.gui import event_handler
from dropbox.trace import TRACE

class MacSystemStatusMonitor(SystemStatusMonitorTestingInterface):
    
    def __init__(self = None):
        self._suspend_handler = Handler(handle_exc = report_exception)
        self._resume_handler = Handler(handle_exc = report_exception)
        self._sleep_start_time = None
        self._sleep_end_time = None
        self._notifier = EFSystemStatusNotifier(self)

    
    def add_suspend_callback(self = None, callback = None):
        self._suspend_handler.add_handler(callback)

    
    def remove_suspend_callback(self = None, callback = None):
        self._suspend_handler.remove_handler(callback)

    
    def trigger_suspend_callbacks(self = None):
        self._suspend_handler.run_handlers()

    
    def add_resume_callback(self = None, callback = None):
        self._resume_handler.add_handler(callback)

    
    def remove_resume_callback(self = None, callback = None):
        self._resume_handler.remove_handler(callback)

    
    def trigger_resume_callbacks(self = None):
        self._resume_handler.run_handlers()

    sleep_start_time = (lambda self = None: self._sleep_start_time)()
    sleep_start_time = (lambda self = None, value = None: self._sleep_start_time = valueself._sleep_end_time = None)()
    sleep_end_time = (lambda self = None: self._sleep_end_time)()
    sleep_end_time = (lambda self = None, value = None: pass# WARNING: Decompyle incomplete
)()


class EFSystemStatusNotifier(NSObject):
    
    def __new__(cls = None, tracker = None):
        return EFSystemStatusNotifier.alloc().initWithTracker_(tracker)

    
    def initWithTracker_(self = None, tracker = None):
        self = objc.super(EFSystemStatusNotifier, self).init()
    # WARNING: Decompyle incomplete

    
    def dealloc(self):
        
        try:
            NSDistributedNotificationCenter.defaultCenter().removeObserver_(self)
            self._notification_center.removeObserver_(self)
        except Exception:
            report_exception(component = DesktopComponent.UNKNOWN)

        objc.super(EFSystemStatusNotifier, self).dealloc()

    onScreenLocked_ = (lambda self = None, notification = objc.typedSelector(b'v@:@'): TRACE('[EFSystemStatusNotifier] screen locked...')self._tracker._suspend_handler.run_handlers())()()
    onScreenUnlocked_ = (lambda self = None, notification = objc.typedSelector(b'v@:@'): TRACE('[EFSystemStatusNotifier] ...screen unlocked.')self._tracker._resume_handler.run_handlers())()()
    onSleep_ = (lambda self = None, notification = objc.typedSelector(b'v@:@'): TRACE('[EFSystemStatusNotifier] host entering sleep...')self._tracker.sleep_start_time = time.time())()()
    onWakeUp_ = (lambda self = None, notification = objc.typedSelector(b'v@:@'): TRACE('[EFSystemStatusNotifier] ...host woke up.')self._tracker.sleep_end_time = time.time())()()

