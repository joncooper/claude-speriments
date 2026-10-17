# Source Generated with Decompyle++
# File: alert_dialog.pyc (Python 3.11)

from typing import Callable, List, Optional, Text, Tuple
import objc
from AppKit import NSApp, NSBackingStoreBuffered, NSBoldFontMask, NSButton, NSColor, NSCompositeSourceOver, NSFloatingWindowLevel, NSFont, NSFontAttributeName, NSFontBoldTrait, NSForegroundColorAttributeName, NSImage, NSImageNameCaution, NSMakeRect, NSMutableAttributedString, NSNormalWindowLevel, NSOnState, NSProgressIndicator, NSProgressIndicatorBarStyle, NSString, NSTextEncodingNameDocumentOption, NSTextView, NSTitledWindowMask, NSUTF16StringEncoding, NSView, NSWidth, NSWindow, NSWindowBelow, NSWindowStyleMaskFullSizeContentView
from Foundation import NSHeight, NSMakeRange, NSMakeRect, NSRect, NSSize, NSWidth, NSZeroRect
from dropbox.client.ui.cocoa.dropbox_controls import NonBlurryImageView
from dropbox.client.ui.cocoa.dynamic_layouts import CONTENT_BORDER, HORIZ_BUTTON_SPACING
from dropbox.client.ui.cocoa.util import add_accessibility_identifier
from dropbox.exception.reporting import report_assertion_error
from dropbox.gui import assert_message_queue, event_handler
HORIZONTAL_PADDING = 10
VERTICAL_PADDING = 10
WINDOW_VERTICAL_PADDING = 15
CHECKBOX_PADDING = 5
ICON_SIZE = 56
DROPBOX_ICON_SIZE = 32
MIN_BUTTON_GAP = 50
MIN_DIALOG_WIDTH = 500

def createIndeterminateProgressBar():
    progress_bar = NSProgressIndicator.alloc().initWithFrame_(NSZeroRect)
    progress_bar.setStyle_(NSProgressIndicatorBarStyle)
    progress_bar.setIndeterminate_(objc.YES)
    return progress_bar


def createTextViewWithAttributedString(attr_string = None, width = None, selectable = None):
    text_view = NSTextView.alloc().initWithFrame_(NSMakeRect(0, 0, width, 0))
    text_view.setDrawsBackground_(objc.NO)
    text_view.setEditable_(False)
    text_view.setSelectable_(selectable)
    text_view.textStorage().setAttributedString_(attr_string)
    text_view.setHorizontallyResizable_(False)
    text_view.sizeToFit()
    return text_view


def createTextViewWithString(original_string = None, width = None, is_bold = None, selectable = (True,)):
    attr_string = NSMutableAttributedString.alloc().initWithString_attributes_(original_string, {
        NSFontAttributeName: NSFont.systemFontOfSize_(0) })
    attr_string.addAttribute_value_range_(NSForegroundColorAttributeName, NSColor.labelColor(), NSMakeRange(0, len(original_string)))
    if is_bold and len(original_string) > 0:
        attr_string.applyFontTraits_range_(NSBoldFontMask, NSMakeRange(0, len(original_string)))
    return createTextViewWithAttributedString(attr_string, width, selectable)


def _attributedStringWithHTML(htmlString = None):
    htmlData = NSString.stringWithString_(htmlString).dataUsingEncoding_(NSUTF16StringEncoding)
    htmlOptions = {
        NSTextEncodingNameDocumentOption: NSString.stringWithString_('UTF-16') }
    (attr_string, document_attributes) = NSMutableAttributedString.alloc().initWithHTML_options_documentAttributes_(htmlData, htmlOptions, None)
# WARNING: Decompyle incomplete


class CocoaAlertView(NSView):
    
    def createAndAddButtonwithButtonText_shortcut_idx_callback_(self, buttonText = None, shortcut = None, idx = None, callback = ('buttonText', 'Text', 'shortcut', 'Text', 'idx', 'int', 'callback', 'Callable', 'return', 'None')):
        button = self.addNormalRoundButtonWithTitle_action_(buttonText, callback)
        button.cell().setRepresentedObject_(idx)
    # WARNING: Decompyle incomplete

    __new__ = (lambda cls, caption, message, left_button_list, right_button_list, checkbox = None, callback = None, no_warning = assert_message_queue, show_indeterminate_progress_bar = ('caption', 'Text', 'message', 'Optional[Text]', 'left_button_list', 'List[Tuple[Text, Optional[Text]]]', 'right_button_list', 'List[Tuple[Text, Optional[Text]]]', 'checkbox', 'Tuple[Optional[Text], bool]', 'callback', 'Optional[Callable[[int, bool], None]]', 'no_warning', 'bool', 'show_indeterminate_progress_bar', 'bool', 'return', "'CocoaAlertView'"): self = CocoaAlertView.alloc().initWithFrame_(NSZeroRect)# WARNING: Decompyle incomplete
)()
    buttonClicked_ = (lambda self = None, button = objc.typedSelector(b'v@:@'): checked = self.checkbox.state() == NSOnState if self.checkbox else Falsebutton_index = button.cell().representedObject()if self.callback:
self.callback(button_index, checked)None)()()
    
    def isFlipped(self = None):
        return True



class CocoaAlertDialog(object):
    
    def __init__(self, caption, message, left_button_list, right_button_list, checkbox_text, callback = None, checkbox_state = None, accessibility_identifier = None, no_warning = (False, None, False, False), show_indeterminate_progress_bar = ('caption', 'Text', 'message', 'Optional[Text]', 'left_button_list', 'List[Tuple[Text, Optional[Text]]]', 'right_button_list', 'List[Tuple[Text, Optional[Text]]]', 'checkbox_text', 'Optional[Text]', 'callback', "Optional[Callable[[int, bool, 'CocoaAlertDialog'], None]]", 'checkbox_state', 'bool', 'accessibility_identifier', 'Text', 'no_warning', 'bool', 'show_indeterminate_progress_bar', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    
    def activate(self = None):
        self.window.orderWindow_relativeTo_(NSWindowBelow, 0)
        self.window.makeKeyAndOrderFront_(None)
        NSApp.activateIgnoringOtherApps_(True)
        self._showing = True

    
    def setFloating_(self = None, value = None):
        self.window.setLevel_(NSFloatingWindowLevel if value else NSNormalWindowLevel)

    
    def isShowing(self = None):
        return self._showing

    
    def close(self = None):
        if self.window:
            self.window.orderOut_(None)
        self.alert_view = None
        self.window = None
        self.callback = None
        self._showing = False


