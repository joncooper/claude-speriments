# Source Generated with Decompyle++
# File: pump_loop_helper.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from AppKit import NSApp, NSApplication, NSApplicationDefined, NSApplicationDidFinishLaunchingNotification, NSEvent, NSNotificationCenter
from Foundation import NSNotification, NSZeroPoint

def pump_event_loop():
    
    def handleApplicationDidFinishLaunching_(_ = None):
        NSApp.stop_(None)
        empty_event = NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(NSApplicationDefined, NSZeroPoint, 0, 0, 0, None, 0, 0, 0)
        NSApp.postEvent_atStart_(empty_event, True)

    observer = NSNotificationCenter.defaultCenter().addObserverForName_object_queue_usingBlock_(NSApplicationDidFinishLaunchingNotification, None, None, handleApplicationDidFinishLaunching_)
    application = NSApplication.sharedApplication()
    application.run()
    NSNotificationCenter.defaultCenter().removeObserver_(observer)

