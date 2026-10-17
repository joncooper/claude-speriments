# Source Generated with Decompyle++
# File: bug_report.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import objc
from AppKit import NSBackingStoreBuffered, NSClosableWindowMask, NSFont, NSMiniaturizableWindowMask, NSTextView, NSTitledWindowMask, NSWindow, NSZeroRect
from Foundation import NSRect
from dropbox.client.ui.cocoa.dropbox_controls import EFFlippedView
from dropbox.client.ui.cocoa.dynamic_layouts import NSButton, NSMakeRect, NSTextField
from dropbox.client.ui.cocoa.styles import CGColorCreateHex, NSColor

class BugReporterView(EFFlippedView):
    WIDTH = 600
    HEIGHT = 350
    BORDER = 20
    TELL_US_HEIGHT = 200
    PADDING = 10
    
    def initWithOnFinished_(self, on_finished):
        self = objc.super(BugReporterView, self).init()
        if not self:
            return None
        cur_height = None.BORDER
        self.setFrame_(NSMakeRect(0, 0, self.WIDTH, self.HEIGHT))
        self._on_finished = on_finished
        tell_us_label = NSTextField.createLabelWithText_('Tell us what happened:')
        tell_us_label.setFrameOrigin_((self.BORDER, self.BORDER))
        self.addSubview_(tell_us_label)
        cur_height += tell_us_label.frame().size.height
        self.tell_us_field = NSTextView.alloc().initWithFrame_(NSRect((0, 0), (self.WIDTH - self.BORDER * 2, self.TELL_US_HEIGHT)))
        self.tell_us_field.textStorage().setFont_(NSFont.labelFontOfSize_(14))
        self.tell_us_field.textStorage().setForegroundColor_(NSColor.whiteColor())
        self.tell_us_field.setFrameOrigin_((self.BORDER, cur_height + self.PADDING))
        self.addSubview_(self.tell_us_field)
        submit_button = NSButton.createColoredRoundButtonWithTitle_('Report Bug')
        submit_button.cell().setBackgroundColor_(NSColor.colorWithCGColor_(CGColorCreateHex(32485)))
        submit_button.setTextColor_(NSColor.whiteColor())
        submit_button.setTarget_(self)
        submit_button.setAction_(self.onFinished_)
        submit_button_size = submit_button.frame().size
        submit_button.setFrameOrigin_((self.WIDTH - self.BORDER - submit_button_size.width, self.HEIGHT - self.BORDER - submit_button_size.height))
        self.addSubview_(submit_button)
        return self

    onFinished_ = (lambda self, sender: tell_us = self.tell_us_field.textStorage().string()self._on_finished(tell_us)self.window().close())()


class BugReportWindow(NSWindow):
    
    def initWithOnFinished_(self, on_finished):
        self = objc.super(BugReportWindow, self).initWithContentRect_styleMask_backing_defer_(NSZeroRect, NSTitledWindowMask | NSClosableWindowMask, NSMiniaturizableWindowMask | NSBackingStoreBuffered, True)
    # WARNING: Decompyle incomplete


