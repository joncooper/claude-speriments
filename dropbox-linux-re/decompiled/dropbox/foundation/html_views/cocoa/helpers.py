# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

import ctypes
from typing import Optional
import objc
from AppKit import NSScreen, NSStatusItem, NSView, NSWindow
from Foundation import NSRect
from dropbox.client.ui.cocoa.dynamic_layouts import NSMakeRect
from dropbox.exception.reporting import report_bad_assumption, report_rare_event
from dropbox.foundation.html_views.common.bridge_gen.types import NativeViewHandle
from dropbox.foundation.html_views.common.content_metadata import StandaloneHtmlViewLocation
STAGGER_DISTANCE = 30

def _get_screen_frame(window = None):
    screen = window.screen() if window else NSScreen.mainScreen()
# WARNING: Decompyle incomplete


def get_html_view_window_rect(view_location = None, width = None, height = None):
    if view_location != StandaloneHtmlViewLocation.CENTER_MAIN:
        raise ValueError('Only `CENTER_MAIN` is currently supported.')
    main_screen_frame = _get_screen_frame()
    if not main_screen_frame:
        return NSMakeRect(0, 0, width, height)
    width = min(main_screen_frame.size.width, width)
    height = min(main_screen_frame.size.height, height)
    x = (main_screen_frame.size.width / 2 - width / 2) + main_screen_frame.origin.x
    y = (main_screen_frame.size.height / 2 - height / 2) + main_screen_frame.origin.y
    return NSMakeRect(x, y, width, height)


def get_nsview_from_bridged_native_handle(native_handle = None):
    nsobj = objc.objc_object(c_void_p = ctypes.c_void_p(native_handle))
# WARNING: Decompyle incomplete


def get_nsstatusitem_from_bridged_native_handle(native_handle = None):
    nsobj = objc.objc_object(c_void_p = ctypes.c_void_p(native_handle))
# WARNING: Decompyle incomplete

