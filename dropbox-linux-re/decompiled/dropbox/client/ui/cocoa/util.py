# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import, division
import re
import sys
from contextlib import contextmanager
from functools import wraps
from typing import Any, Callable, Dict, Optional, Text, Tuple
import objc
from AppKit import NSApp, NSApplication, NSBezierPath, NSColor, NSCompositeCopy, NSCompositeSourceOver, NSControl, NSFont, NSFontAttributeName, NSForegroundColorAttributeName, NSGraphicsContext, NSImage, NSKernAttributeName, NSMakePoint, NSMakeRect, NSMakeSize, NSScreen, NSSize, NSURL, NSUserDefaults
from Foundation import NSAttributedString, NSPointInRect, NSRect, NSZeroRect
from macffi.CoreGraphics import CGError
from macffi.CoreGraphicsServices import CGSGetWindowBounds
from objc import typedSelector
from dropbox.client.background_worker import on_background_thread
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.ui.cocoa.styles import COLOR_NOTIFICATION_BADGE, COLOR_NOTIFICATION_BADGE_DARK
from dropbox.client.ui.common.constants import ResizeMethod
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.functions import lrudict
from dropbox.gui import assert_message_queue
from dropbox.i18n import trans
from dropbox.mac.internal import autoreleasepool
from dropbox.mac.version import BIG_SUR, MAC_VERSION
from dropbox.trace import TRACE
get_window_rect = (lambda wid = None: context = NSApp().contextID()try:
rect = CGSGetWindowBounds(context, wid)NSMakeRect(rect.origin.x, rect.origin.y, rect.size.width, rect.size.height)except CGError:
e = Noneraise KeyError('Error getting window bounds: %s' % e.errno)e = Nonedel e)()

class TrayIcon:
    _icon_map = {
        TrayIconStatus.PAUSED: 'paused',
        TrayIconStatus.CAM: 'cam',
        TrayIconStatus.BROKEN: 'broken',
        TrayIconStatus.CONNECTING: 'connecting',
        TrayIconStatus.BUSY: 'busy',
        TrayIconStatus.IDLE: 'idle' }
    _cache: 'Dict[str, NSImage]' = { }
    get_image_for_state = (lambda cls = None, state = None: cls.get_image_for_label(cls._icon_map[state]))()
    get_image_for_label = (lambda cls = None, label = None: image = cls._cache.get(label)# WARNING: Decompyle incomplete
)()
    get_icon_for_badge_count = (lambda cls = None, count = None: pass# WARNING: Decompyle incomplete
)()
    _is_dark_mode = (lambda : defaults = NSUserDefaults.standardUserDefaults()str(defaults.objectForKey_('AppleInterfaceStyle')) == 'Dark')()


class ImageCache(object):
    __instance: "Optional['ImageCache']" = None
    sharedCache = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    
    def __init__(self):
        self._images = lrudict(cache_size = 100)

    
    def get(self = None, url = None, callback = classmethod, size = (None,)):
        pass
    # WARNING: Decompyle incomplete



def add_accessibility_identifier(control = None, identifier = None):
    control.setAccessibilityIdentifier_(identifier)


def convert_structs(sig = None):
    size_pattern = b'{(_NSSize|_NSPoint|CGSize|CGPoint)=[fd]{2}}'
    make_bytes = make_bytes
    import dropbox.functions
    _cgfloat = make_bytes(objc._C_CGFloat)
    replacement_pattern = b'{\\1=' + _cgfloat + _cgfloat + b'}'
    result = re.sub(size_pattern, replacement_pattern, sig)
    if sys.maxsize > 0x100000000:
        result = result.replace(b'_NSRect', b'CGRect')
        result = result.replace(b'_NSSize', b'CGSize')
        result = result.replace(b'_NSPoint', b'CGPoint')
    else:
        result = result.replace(b'CGRect', b'_NSRect')
        result = result.replace(b'CGSize', b'_NSSize')
        result = result.replace(b'CGPoint', b'_NSPoint')
    return result


def guarded(sig = None):
    pass
# WARNING: Decompyle incomplete


def protected_action_method(action_method):
    pass
# WARNING: Decompyle incomplete

save_graphics_state = (lambda : pass# WARNING: Decompyle incomplete
)()
edit_attributed_string = (lambda attributed_string: pass# WARNING: Decompyle incomplete
)()
edit_text_view = (lambda text_view: pass# WARNING: Decompyle incomplete
)()

def screen_from_point(point):
    pass
# WARNING: Decompyle incomplete


def screen_rect_from_point(x, y):
    frame = screen_from_point((x, y)).visibleFrame()
    origin = frame.origin
    size = frame.size
    return (origin.x, origin.y, origin.x + size.width, origin.y + size.height)


def get_main_screen_rect():
    screen_frame = None
    
    try:
        screen_frame = NSScreen.mainScreen().frame()
    except Exception:
        report_exception(component = DesktopComponent.UI_KIT)

# WARNING: Decompyle incomplete


def get_origin_of_centered_window(screen_frame, window_size):
    return NSMakePoint(screen_frame.origin.x + screen_frame.size.width / 2 - 0.5 * window_size.width, screen_frame.origin.y + screen_frame.size.height / 2 - 0.5 * window_size.height)


def resize_image(source_img, dimensions, method = (ResizeMethod.FIT,)):
    pass
# WARNING: Decompyle incomplete

