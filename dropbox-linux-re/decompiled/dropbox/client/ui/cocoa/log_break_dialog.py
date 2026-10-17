# Source Generated with Decompyle++
# File: log_break_dialog.pyc (Python 3.11)

from typing import Callable, Text
import objc
from AppKit import NSApp, NSBackingStoreBuffered, NSButton, NSClosableWindowMask, NSFloatingWindowLevel, NSMakeRect, NSTextField, NSTitledWindowMask, NSView, NSWindow
from dropbox.client.ui.cocoa.constants import ENTER_KEY
from dropbox.client.ui.cocoa.util import add_accessibility_identifier
from dropbox.gui import assert_message_queue, event_handler
from dropbox.mac.internal import autoreleasepool
_FIELD_ORIGIN_X = 12
_FIELD_WIDTH = 240
_BUTTON_WIDTH = 80
_CONTROL_HEIGHT = 24
_CONTROL_Y = 12
_PADDING = 6
_WINDOW_WIDTH = _FIELD_ORIGIN_X + _FIELD_WIDTH + _PADDING + _BUTTON_WIDTH + _PADDING
_WINDOW_HEIGHT = _CONTROL_Y * 2 + _CONTROL_HEIGHT

class LogBreakView(NSView):
    __new__ = (lambda cls = None, on_insert = None: self = LogBreakView.alloc().initWithFrame_(NSMakeRect(0, 0, _WINDOW_WIDTH, _WINDOW_HEIGHT))if self:
self.on_insert = on_insertself.counter = 0self.field = NSTextField.alloc().initWithFrame_(NSMakeRect(_FIELD_ORIGIN_X, _CONTROL_Y, _FIELD_WIDTH, _CONTROL_HEIGHT))self.field.setEditable_(True)self.field.setSelectable_(True)self.field.setBezeled_(True)self.addSubview_(self.field)button = NSButton.alloc().initWithFrame_(NSMakeRect(_FIELD_ORIGIN_X + _FIELD_WIDTH + _PADDING, _CONTROL_Y, _BUTTON_WIDTH, _CONTROL_HEIGHT))button.setTitle_('Insert')button.setBezelStyle_(1)button.setTarget_(self)button.setAction_(self.insertClicked_)button.setKeyEquivalent_(ENTER_KEY)self.addSubview_(button)self._reset_field()self)()
    _reset_field = (lambda self = None: self.field.setStringValue_('break_%d' % self.counter)self.field.selectText_(self))()
    insertClicked_ = (lambda self = None, button = objc.typedSelector(b'v@:@'): autoreleasepool()if not self.field.stringValue():
label = 'break_%d' % self.counterself.on_insert(label)self._reset_field()None(None, None)Nonewith None:
if not self.field.stringValue():
pass)()()


class LogBreakDialog(object):
    
    def __init__(self = None, on_insert = None):
        autoreleasepool()
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(NSMakeRect(0, 0, _WINDOW_WIDTH, _WINDOW_HEIGHT), NSTitledWindowMask | NSClosableWindowMask, NSBackingStoreBuffered, True)
        self.window.setTitle_('Log Break')
        self.window.setLevel_(NSFloatingWindowLevel)
        self.window.setReleasedWhenClosed_(False)
        self.view = LogBreakView(on_insert)
        self.window.setContentView_(self.view)
        add_accessibility_identifier(self.window, 'dropboxLogBreakDialog')
        self.window.center()
        self.window.makeKeyAndOrderFront_(None)
        self.window.makeFirstResponder_(self.view.field)
        NSApp.activateIgnoringOtherApps_(True)
        None(None, None)
        return None
        with None:
            if not None:
                pass


