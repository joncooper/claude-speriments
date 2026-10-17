# Source Generated with Decompyle++
# File: shell.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import os
from collections import OrderedDict
from typing import Any
import objc
from AppKit import NSApp, NSApplicationDidBecomeActiveNotification, NSApplicationDidResignActiveNotification, NSBundle, NSKeyValueObservingOptionNew, NSNotificationCenter, NSObject, NSRunningApplication, NSWorkspace
from macffi.CoreFoundation import CFError, CFMachPortCreateRunLoopSource, CFMachPortCreateWithPort, CFRunLoopAddSource, CFRunLoopGetCurrent, ffi as ffi_core_foundation, kCFRunLoopDefaultMode
from macffi.CoreGraphics import CGError, kCGErrorIllegalArgument
from macffi.CoreGraphicsServices import CGEventCreateNextEvent, CGSConnectionNotifyProc, CGSCopyWindowProperty, CGSGetEventPort, CGSGetWindowList, CGSNewConnection, CGSRegisterConnectionNotifyProc, CGSRemoveConnectionNotifyProc, CGSRequestNotificationsForWindows, CGSWindowIsOrderedIn, kCGSWindowTitle
from macffi.CoreProcess import CPSEqualProcess, CPSGetWindowOwner, ffi as ffi_core_process
from six import iterkeys
from dropbox.callbacks import Handler
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.gui import event_handler
from dropbox.harmony.mac.office_coauthoring import office_license_supports_coauthoring
from dropbox.harmony.model import HarmonyWindow
from dropbox.harmony.models.types import ApplicationDetails, ApplicationID, ProcessID, WindowDetails, WindowFile
from dropbox.harmony.plugins.office_coauthoring import application_supports_coauthoring
from dropbox.harmony.utility.exceptions import SEVERITY_BENIGN, StateNotAvailableError
from dropbox.harmony.window_tracking.shell_interface import HarmonyShellInterface
from dropbox.mac.internal import autoreleasepool
from dropbox.threading import RLock
from dropbox.trace import TRACE
procNotFound = -600
get_window_title = (lambda wid: context = NSApp().contextID()try:
CGSCopyWindowProperty(context, wid, kCGSWindowTitle)except CGError:
e = Noneif e.errno == kCGErrorIllegalArgument:
raise KeyError()raise e = Nonedel e)()
ProcessSerialNumber = objc.createOpaquePointerType('ProcessSerialNumber', b'^{ProcessSerialNumber=II}', None)

def NSRunningApplication():
    '''NSRunningApplication'''
    
    def processSerialNumber(self):
        psn_container = ffi_core_process.new('CPSProcessSerNum[]', 1)
        pointer = int(ffi_core_process.cast('unsigned long', psn_container))
        self._getProcessSerialNumber_(ProcessSerialNumber(c_void_p = pointer))
        return psn_container


NSRunningApplication = <NODE:27>(NSRunningApplication, 'NSRunningApplication', objc.Category(NSRunningApplication))
is_window_ordered_in = (lambda wid: context = NSApp().contextID()try:
CGSWindowIsOrderedIn(context, wid)except CGError:
e = Noneif e.errno == kCGErrorIllegalArgument:
raise KeyError()raise e = Nonedel e)()

class EFWorkspaceNotifier(NSObject):
    __new__ = (lambda cls, tracker: EFWorkspaceNotifier.alloc().initWithTracker_(tracker))()
    
    def initWithTracker_(self, tracker):
        self = objc.super(EFWorkspaceNotifier, self).init()
    # WARNING: Decompyle incomplete

    
    def dealloc(self):
        
        try:
            NSNotificationCenter.defaultCenter().removeObserver_(self)
        except Exception:
            report_exception(component = DesktopComponent.HARMONY)

        
        try:
            NSWorkspace.sharedWorkspace().removeObserver_forKeyPath_(self, 'frontmostApplication')
        except Exception:
            report_exception(component = DesktopComponent.HARMONY)

        objc.super(EFWorkspaceNotifier, self).dealloc()

    
    def observeValueForKeyPath_ofObject_change_context_(self, key_path, obj, change, context):
        if key_path != 'frontmostApplication':
            return None
        None._tracker._window_focused_handler.run_handlers()

    applicationNotificationTriggered_ = (lambda self, notification: self._tracker._window_focused_handler.run_handlers())()()


class HarmonyMacShell(HarmonyShellInterface):
    _WINDOW_CAPACITY = 1000
    _EVENT_MOVE = 806
    _EVENT_RESIZE = 807
    _POSITION_EVENTS = (_EVENT_MOVE, _EVENT_RESIZE)
    _EVENT_ORDERED_IN_OLD = 802
    _EVENT_ORDERED_OUT_OLD = 803
    _EVENT_DESTROYED = 804
    _EVENT_CREATED = 811
    _EVENT_ORDERED_FRONT = 808
    _EVENT_ORDERED_IN = 815
    _EVENT_ORDERED_OUT = 816
    _GENERAL_EVENTS = {
        _EVENT_ORDERED_OUT: 'ordered out',
        _EVENT_ORDERED_IN: 'ordered in',
        _EVENT_ORDERED_FRONT: 'ordered front',
        _EVENT_CREATED: 'created',
        _EVENT_DESTROYED: 'destroyed',
        _EVENT_ORDERED_OUT_OLD: 'ordered out [old]',
        _EVENT_ORDERED_IN_OLD: 'ordered in [old]' }
    _POSITION_REFRESH_EVENTS = frozenset((_EVENT_MOVE, _EVENT_RESIZE))
    _MAGIC_FLAG = 4
    
    def __init__(self):
        pass
    # WARNING: Decompyle incomplete

    track_window = (lambda self = None, wid = None: pass# WARNING: Decompyle incomplete
)()
    _is_wid_in_frontmost_app = (lambda wid, frontmost_application: pass# WARNING: Decompyle incomplete
)()
    
    def set_app_whitelist_enabled(self = None, enabled = None):
        self._app_whitelist_enabled = enabled

    
    def add_to_app_whitelist(self = None, *app_bundle_ids):
        self._app_whitelist.update(app_bundle_ids)

    
    def remove_from_app_whitelist(self = None, *app_bundle_ids):
        pass

    
    def _init_notifications(self):
        pass
    # WARNING: Decompyle incomplete

    enable = (lambda self = None: self._init_notifications()for event in iterkeys(self._GENERAL_EVENTS):
CGSRegisterConnectionNotifyProc(self._context, self._general_event_callback, event)window_list = CGSGetWindowList(self._context, capacity = self._WINDOW_CAPACITY)self._watched = (lambda .0: pass# WARNING: Decompyle incomplete
)(window_list())
            CGSRequestNotificationsForWindows(self._context, list(iterkeys(self._watched)))
            TRACE('Activated focus notifications')
            for event in self._POSITION_EVENTS:
                CGSRegisterConnectionNotifyProc(self._tracking_context, self._position_event_callback, event)
                TRACE('Activated position notifications')
                return None
)()
    disable = (lambda self = None: TRACE('Unregistering for window notifications.')for event in iterkeys(self._GENERAL_EVENTS):
CGSRemoveConnectionNotifyProc(self._context, self._general_event_callback, event)self._watched.clear()TRACE('Unregistering for position notifications.')for event in self._POSITION_EVENTS:
CGSRemoveConnectionNotifyProc(self._tracking_context, self._position_event_callback, event)self._tracked = 0None)()
    
    def _handle_general_event(self, event, window):
        should_register = False
        mark_hidden = False
        mark_destroyed = False
        possible_focus_event = False
        if event == self._EVENT_CREATED:
            self._watched.pop(window, None)
            if len(self._watched) == self._WINDOW_CAPACITY:
                self._watched.popitem(last = False)
            self._watched[window] = None
            should_register = True
            possible_focus_event = True
        elif event == self._EVENT_DESTROYED:
            self._watched.pop(window, None)
            possible_focus_event = True
            mark_destroyed = True
        elif event in (self._EVENT_ORDERED_FRONT, self._EVENT_ORDERED_IN, self._EVENT_ORDERED_IN_OLD):
            possible_focus_event = True
        elif event in (self._EVENT_ORDERED_OUT, self._EVENT_ORDERED_OUT_OLD):
            possible_focus_event = True
            mark_hidden = True
        if should_register:
            CGSRequestNotificationsForWindows(self._context, list(iterkeys(self._watched)))
        if mark_hidden:
            self._marked_hidden.add(window)
        elif mark_destroyed:
            self._marked_destroyed.add(window)
        if mark_hidden or mark_destroyed:
            self._refresh_hidden()
        if possible_focus_event:
            self._handle_possible_cg_focus_events(window, mark_destroyed)
            return None

    
    def _handle_possible_cg_focus_events(self = None, window = None, is_destroy_event = None):
        
        try:
            frontmost_application = NSWorkspace.sharedWorkspace().frontmostApplication()
            if not frontmost_application:
                return None
            if None._app_whitelist_enabled and frontmost_application.bundleIdentifier() not in self._app_whitelist:
                return None
            if None and window == self._last_focus:
                self._last_focus = 0
                self._window_focused_handler.run_handlers()
                return None
            if None._is_wid_in_frontmost_app(window, frontmost_application):
                self._last_focus = window
                self._window_focused_handler.run_handlers()
                return None
            return None
        except CFError:
            exc = None
            if exc.errno != procNotFound:
                raise 
            exc = None
            del exc
            return None
            exc = None
            del exc


    
    def _handle_position_events(self):
        if not self._refreshing_position:
            self._refreshing_position = True
            self._refresh_position()
            self._window_moved_handler.run_handlers(done = False, wid = self._tracked)
            return None
        self._position_invalid = None

    _refresh_hidden = (lambda self = None: hidden = tuple(self._marked_hidden)destroyed = tuple(self._marked_destroyed)self._marked_hidden.clear()self._marked_destroyed.clear()if hidden:
self._windows_hidden_handler.run_handlers(hidden)if destroyed:
self._windows_destroyed_handler.run_handlers(destroyed)None)()
    _refresh_position = (lambda self = None: if self._position_invalid:
self._position_invalid = Falseself._refresh_position()Noneself._refreshing_position = Noneself._window_moved_handler.run_handlers(done = True, wid = self._tracked))()
    
    def get_active_application(self = None):
        autoreleasepool()
        running_application = NSWorkspace.sharedWorkspace().frontmostApplication()
        if not running_application:
            raise StateNotAvailableError('No currently running application.', stage = 'nothing', severity = SEVERITY_BENIGN)
        pid = running_application.processIdentifier()
        if pid == self._pid:
            raise StateNotAvailableError('Focused on ourselves.', stage = 'self', severity = SEVERITY_BENIGN)
        aid = running_application.bundleIdentifier()
        if not aid:
            raise StateNotAvailableError('Application is not bundle-based.', stage = 'no-bundle', severity = SEVERITY_BENIGN)
        bundle_url = running_application.bundleURL()
        if not bundle_url:
            raise StateNotAvailableError('Application has no bundle url.', stage = 'no-bundle-url', severity = SEVERITY_BENIGN)
        bundle = NSBundle.bundleWithURL_(bundle_url)
        if not bundle:
            raise StateNotAvailableError('Application has no valid bundle.', stage = 'bundle-invalid', severity = SEVERITY_BENIGN)
        version = bundle.objectForInfoDictionaryKey_('CFBundleVersion')
        short_version = bundle.objectForInfoDictionaryKey_('CFBundleShortVersionString')
        if application_supports_coauthoring(ApplicationID(aid), version):
            supports_coauthoring = office_license_supports_coauthoring()
            None(None, None)
            return 
        with None:
            if not application_supports_coauthoring(ApplicationID(aid), version):
                pass

    unfocus_window = (lambda self = None: NSApp().activateIgnoringOtherApps_(True))()
    focus_window = (lambda self = None, window = None: app = NSRunningApplication.runningApplicationWithProcessIdentifier_(window.pid)if app:
app.activateWithOptions_(0)None)()
    focus_window_by_id = (lambda self = None, id = None: app = NSRunningApplication.runningApplicationWithProcessIdentifier_(id)if app:
app.activateWithOptions_(0)None)()

