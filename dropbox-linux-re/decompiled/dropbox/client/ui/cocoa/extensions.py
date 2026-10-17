# Source Generated with Decompyle++
# File: extensions.pyc (Python 3.11)

from __future__ import absolute_import
from functools import partial
from typing import Callable, Optional, Text
import objc
from AppKit import CIFilter, CIImage, NSAttributedString, NSButton, NSButtonCell, NSCenterTextAlignment, NSCIImageRep, NSClockAndCalendarDatePickerStyle, NSColor, NSData, NSDatePicker, NSEvent, NSFont, NSFontAttributeName, NSForegroundColorAttributeName, NSImage, NSImageOnly, NSImageView, NSMomentaryChangeButton, NSMutableParagraphStyle, NSNotification, NSObject, NSParagraphStyleAttributeName, NSPopover, NSPopoverBehaviorSemitransient, NSSmallSquareBezelStyle, NSTimer, NSView, NSViewController, NSYearMonthDayDatePickerElementFlag
from Cocoa import NSMaxXEdge
from Foundation import NSLocale, NSMakeRect, NSRect
from Quartz import CGColorCreateGenericGray
from dropbox.client.ui.cocoa.styles import COLOR_DROPBOX_BLUE
from dropbox.client.ui.cocoa.util import ImageCache
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.gui import assert_message_queue, event_handler
from dropbox.i18n import get_current_code
from dropbox.mac.version import MAC_VERSION, SIERRA
if MAC_VERSION >= SIERRA:
    
    try:
        from AppKit import NSEventMaskLeftMouseDown, NSEventTypeLeftMouseDown
    except ImportError:
        from AppKit import NSLeftMouseDown as NSEventMaskLeftMouseDown, NSLeftMouseDown as NSEventTypeLeftMouseDown
    except:
        from AppKit import NSLeftMouseDown as NSEventMaskLeftMouseDown, NSLeftMouseDown as NSEventTypeLeftMouseDown

    
    def NSTimer():
        '''NSTimer'''
        scheduledTimerWithTimeInterval_block_repeats_ = (lambda cls = None, interval = None, block = classmethod, repeats = ('interval', 'float', 'block', 'Callable', 'repeats', 'bool', 'return', 'NSTimer'): NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(interval, cls, cls.doInvokeBlock_, block, repeats))()
        timerWithTimeInterval_block_repeats_ = (lambda cls, interval, block, repeats: NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_(interval, cls, cls.doInvokeBlock_, block, repeats))()
        doInvokeBlock_ = (lambda cls, timer: try:
block = timer.userInfo()block()Noneexcept Exception:
report_exception(component = DesktopComponent.UI_KIT)None)()

    NSTimer = <NODE:27>(NSTimer, 'NSTimer', objc.Category(NSTimer))
    
    class EFImageView(NSImageView):
        
        def initWithFrame_(self, frame):
            self = objc.super(EFImageView, self).initWithFrame_(frame)
            if not self:
                return None
            self._callback_id = None
            return self

        setImageUrl_ = (lambda self = None, imageUrl = None, is_greyscale = objc.python_method: pass# WARNING: Decompyle incomplete
)()

    
    class EFButton(NSButton):
        COLOR_DEFAULT_BACKGROUND = CGColorCreateGenericGray(0, 0)
        COLOR_DEFAULT_TEXT = COLOR_DROPBOX_BLUE
        COLOR_DEFAULT_BORDER = COLOR_DROPBOX_BLUE
        DEFAULT_CORNER_RADIUS = 3
        DEFAULT_BORDER_WIDTH = 1
        COLOR_DEFAULT_BACKGROUND_PRESSED = COLOR_DROPBOX_BLUE
        COLOR_DEFAULT_TEXT_PRESSED = CGColorCreateGenericGray(1, 1)
        COLOR_DEFAULT_BORDER_PRESSED = COLOR_DROPBOX_BLUE
        PADDING_HORIZONTAL = 20
        PADDING_VERTICAL = 10
        FONT = NSFont.fontWithName_size_('Helvetica', 14)
        initWithFrame_ = (lambda self, frame: self = objc.super(EFButton, self).initWithFrame_(frame)if not self:
Noneself._cornerRadius = None.DEFAULT_CORNER_RADIUSself._borderWidth = self.DEFAULT_BORDER_WIDTHself._backgroundColor = self.COLOR_DEFAULT_BACKGROUNDself._borderColor = self.COLOR_DEFAULT_BORDERself._pressedColor = self.COLOR_DEFAULT_BACKGROUND_PRESSEDself._pressedBorderColor = self.COLOR_DEFAULT_BORDER_PRESSEDself._pressed = Falseself._title = ''self.setBordered_(False)self.setButtonType_(NSMomentaryChangeButton)self.setBezelStyle_(NSSmallSquareBezelStyle)self.setWantsLayer_(True)self)()
        
        def intrinsicContentSize(self):
            result = objc.super(EFButton, self).intrinsicContentSize()
            if result.width >= 0:
                pass
            if result.height >= 0:
                pass
            return result

        
        def mouseDown_(self, event):
            objc.super(EFButton, self).mouseDown_(event)
            self.updateLayer()

        
        def mouseUp_(self, event):
            objc.super(EFButton, self).mouseUp_(event)
            self.updateLayer()

        
        def updateLayer(self):
            rootLayer = self.layer()
            rootLayer.setCornerRadius_(self._cornerRadius)
            rootLayer.setMasksToBounds_(True)
            rootLayer.setBorderWidth_(self._borderWidth)
            if self.cell().isHighlighted():
                rootLayer.setBackgroundColor_(self._pressedColor)
                rootLayer.setBorderColor_(self._pressedBorderColor)
                return None
            None.setBackgroundColor_(self._backgroundColor)
            rootLayer.setBorderColor_(self._borderColor)

        
        def setNormalBackgroundColor_(self, value):
            self._backgroundColor = value
            self.updateLayer()

        
        def normalBackgroundColor(self):
            return self._backgroundColor

        
        def setBorderColor_(self, value):
            self._borderColor = value
            self.updateLayer()

        
        def borderColor(self):
            return self._borderColor

        
        def setPressedBackgroundColor_(self, value):
            self._pressedColor = value
            self.updateLayer()

        
        def pressedBackgroundColor(self):
            return self._pressedColor

        
        def setPressedBorderColor_(self, value):
            self._pressedBorderColor = value
            self.updateLayer()

        
        def pressedBorderColor(self):
            return self._pressedBorderColor

        
        def setCornerRadius_(self, radius):
            self._cornerRadius = radius
            self.updateLayer()

        
        def cornerRadius(self):
            return self._cornerRadius

        
        def setBorderWidth_(self, width):
            self._borderWidth = width
            self.updateLayer()

        
        def borderWidth(self):
            return self._borderWidth

        
        def setTitle_(self, title):
            self.setTitle_withColor_(title, NSColor.colorWithCGColor_(self.COLOR_DEFAULT_TEXT))

        
        def setTitle_withColor_(self, title, color):
            self.setTitle_withColor_font_(title, color, self.FONT)

        
        def setTitle_withColor_font_(self, title, color, font):
            self._title = title
            textStyle = NSMutableParagraphStyle.alloc().init()
            textStyle.setLineSpacing_(0)
            textStyle.setMinimumLineHeight_(13)
            textStyle.setMaximumLineHeight_(13)
            textStyle.setAlignment_(NSCenterTextAlignment)
            attrsDict = {
                NSParagraphStyleAttributeName: textStyle,
                NSForegroundColorAttributeName: color,
                NSFontAttributeName: font }
            attrTitle = NSAttributedString.alloc().initWithString_attributes_(title, attrsDict)
            self.setAttributedTitle_(attrTitle)


    
    class EFImageOnlyButton(NSButton):
        
        def initWithImage_(self = None, image = None):
            width = image.size().width
            height = image.size().height
            self = objc.super(EFImageOnlyButton, self).initWithFrame_(NSRect((0, 0), (width, height)))
        # WARNING: Decompyle incomplete


    
    class EFDropdownButtonCell(NSButtonCell):
        
        def menuLocationFromEvent_andRect_(self, event, cellFrame):
            return (NSEvent.mouseLocation(), None)

        
        def trackMouse_inRect_ofView_untilMouseUp_(self, event, cellFrame, controlView, untilMouseUp):
            if event.type() == NSEventTypeLeftMouseDown and self.menu():
                (location, targetView) = self.menuLocationFromEvent_andRect_(event, cellFrame)
                self.menu().popUpMenuPositioningItem_atLocation_inView_(None, location, targetView)
                return True
            return objc.super(EFDropdownButtonCell, self).trackMouse_inRect_ofView_untilMouseUp_(event, cellFrame, controlView, untilMouseUp)


    
    class EFDatePickerWithPopover(NSDatePicker):
        CALENDAR_BORDER = 24
        CALENDAR_SIZE = 144
        
        def init(self = None):
            self = objc.super(EFDatePickerWithPopover, self).init()
        # WARNING: Decompyle incomplete

        
        def acceptsFirstResponder(self = None):
            return self.isEnabled()

        
        def becomeFirstResponder(self = None):
            if self.isEnabled():
                self.open_popover()
            return objc.super(EFDatePickerWithPopover, self).becomeFirstResponder()

        
        def resignFirstResponder(self = None):
            self.popover.close()
            return objc.super(EFDatePickerWithPopover, self).resignFirstResponder()

        
        def mouseDown_(self = None, event = None):
            objc.super(EFDatePickerWithPopover, self).mouseDown_(event)
            if self.isEnabled():
                self.open_popover()
                return None

        
        def popoverDateChanged_(self = None, sender = None):
            self.setDateValue_(self.calendar_view.dateValue())
            if self.action():
                self.sendAction_to_(self.action(), self.target())
                return None

        
        def open_popover(self = None):
            self.calendar_view.setDateValue_(self.dateValue())
            self.popover.showRelativeToRect_ofView_preferredEdge_(self.bounds(), self, NSMaxXEdge)
            self.popover_showing = True

        popoverWillClose_ = (lambda self = None, notification = objc.typedSelector(b'v@:@'): self.popover_showing = False)()()

    return None
