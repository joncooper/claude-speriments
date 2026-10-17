# Source Generated with Decompyle++
# File: dynamic_layouts.pyc (Python 3.11)

from __future__ import absolute_import, division
import math
import re
from typing import Any, Callable, List, Optional, Text, Tuple, Union
import objc
from AppKit import NSBackgroundStyleRaised, NSBoxSeparator, NSButtonCell, NSCenterTextAlignment, NSCharacterSet, NSColor, NSFont, NSFontAttributeName, NSForegroundColorAttributeName, NSHelpButtonBezelStyle, NSLinkAttributeName, NSMenuItem, NSMomentaryPushInButton, NSMutableAttributedString, NSMutableParagraphStyle, NSParagraphStyleAttributeName, NSProgressIndicatorSpinningStyle, NSRadioButton, NSRadioModeMatrix, NSRegularControlSize, NSRoundedBezelStyle, NSSmallControlSize, NSStringDrawingUsesLineFragmentOrigin, NSSwitchButton, NSTokenAttachmentCell, NSTokenFieldCell, NSURL
from Foundation import NSHeight, NSMakeRange, NSMakeRect, NSMaxX, NSMaxY, NSPoint, NSRect, NSSize, NSWidth, NSZeroRect
from objc import Category, NO, objc_object, YES
from constants import Colors, ENTER_KEY
from dropbox.client.ui.cocoa.styles import COLOR_DROPBOX_SUBTEXT_GRAY
from dropbox.client.ui.cocoa.util import convert_structs
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.gui import event_handler
from AppKit import NSAttributedString, NSBox, NSButton, NSControl, NSDatePicker, NSMatrix, NSPopUpButton, NSProgressIndicator, NSSearchField, NSSecureTextField, NSStepper, NSTextField, NSTokenField, NSView
NEARBY_CONTROL_BORDER = 8
CONTENT_BORDER = 25
INNER_BOX_MARGIN = 15
INNER_BOX_DEFAULT_HEIGHT = 120
INFINITE_DIMENSION = 10000
CHECKBOX_HEIGHT = 14
CHECKBOX_VERTICAL_SPACING = 4
BUTTON_HEIGHT = 20
BUTTON_LEFT_ALIGNMENT_OFFSET = -4
BUTTON_TO_HELP_BUTTON_ADJUSTMENT = 4
BUTTON_TO_HELP_BUTTON_ADJUSTMENT_FLIPPED = 3
SPINNER_SPACING = 3
SPINNER_VERTICAL_OFFSET = 6
STATICTEXT_TO_BUTTON_BASELINE_ADJUSTMENT = 10
STATICTEXT_TO_HELPBUTTON_BASELINE_ADJUSTMENT = 8
STATICTEXT_TO_DROPDOWN_BASELINE_ADJUSTMENT = 6
LABEL_PADDING = 8
LABEL_PADDING_WITH_CHECKBOXES = -3
BOTTOM_BUTTON_BORDER = 6
HORIZ_BUTTON_BORDER = 17
HORIZ_BUTTON_SPACING = 2
NSPOPUPBUTTON_TEXT_X_OFFSET = 8

def NSAttributedString():
    '''NSAttributedString'''
    hyperlinkFromString_withURL_font_ = (lambda cls, string, url, font = (None,): attr_str = NSMutableAttributedString.alloc().initWithString_(string)r = NSMakeRange(0, attr_str.length())# WARNING: Decompyle incomplete
)()
    linkify = (lambda cls, string, font, color = (None, None): link_re = re.compile('<a href="([^"]*)">([^<]*)</a>')parts = re.split('(<a href="[^"]*">[^<]*</a>)', string)attr_str = NSMutableAttributedString.alloc().init()# WARNING: Decompyle incomplete
)()()
    boldify = (lambda cls, string, font, bold_font, color, center, line_height = (None, None, None, False, None): link_re = re.compile('<b>([^<]*)</b>')parts = re.split('(<b>[^<]*</b>)', string)attr_str = NSMutableAttributedString.alloc().init()# WARNING: Decompyle incomplete
)()()
    createForControlWithString_font_color_ = (lambda cls, val, font, color = (None, None): pass# WARNING: Decompyle incomplete
)()

NSAttributedString = <NODE:27>(NSAttributedString, 'NSAttributedString', Category(NSAttributedString))

def NSBox():
    '''NSBox'''
    
    def verticalPadding(self):
        return 8

    
    def verticalTitleAdjustment(self):
        return 12

    
    def useDropboxTitle(self):
        current_title = self.title()
        self.setTitle_('')
        dropbox_title = NSTextField.createLabelWithText_(current_title)
        dropbox_title.setFont_(NSFont.systemFontOfSize_(13))
        self.superview().addSubview_(dropbox_title)
        new_origin = (self.frame().origin.x, self.frame().origin.y - 1)
        dropbox_title.setFrameOrigin_(new_origin)


NSBox = <NODE:27>(NSBox, 'NSBox', Category(NSBox))

class DropboxHorizontalLine(NSBox):
    
    def verticalPadding(self):
        return 12

    
    def horizontalPadding(self):
        return 12

    
    def __new__(cls, width):
        return cls.alloc().initForParentWidth_(width)

    
    def initForParentWidth_(self, width):
        self = objc.super(DropboxHorizontalLine, self).initWithFrame_(NSRect((0, 0), (width - self.horizontalPadding() * 2, 1)))
    # WARNING: Decompyle incomplete



def NSButton():
    '''NSButton'''
    
    def verticalPadding(self):
        if self.bezelStyle() == 0:
            return 6

    
    def baselineOffset(self):
        if self.bezelStyle() == NSHelpButtonBezelStyle:
            return 4

    
    def flippedBaselineOffset(self):
        return 5

    
    def insetRect(self):
        if self.bezelStyle() == NSHelpButtonBezelStyle:
            return NSMakeRect(-3, -4, -6, -5)
        if None.bezelStyle() == NSRoundedBezelStyle:
            return NSMakeRect(-3, -8, -12, -12)

    
    def setTextColor_(self, textColor):
        attr_str = NSMutableAttributedString.alloc().initWithAttributedString_(self.attributedTitle())
        r = NSMakeRange(0, attr_str.length())
        attr_str.addAttribute_value_range_(NSForegroundColorAttributeName, textColor, r)
        attr_str.fixAttributesInRange_(r)
        self.setAttributedTitle_(attr_str)

    
    def sizeToFitWithPadding(self):
        self.sizeToFit()
        new_frame = self.frame()
        new_frame.size.width = max(96, NSWidth(new_frame) + 12)
        self.setFrame_(new_frame)

    createColoredRoundButtonWithTitle_ = (lambda cls, title: cls.createColoredRoundButtonWithTitle_default_(title, False))()
    createColoredRoundButtonWithTitle_default_ = (lambda cls, title, default: cls.createColoredRoundButtonWithTitle_default_origin_(title, default, (0, 0)))()
    createColoredRoundButtonWithTitle_default_origin_ = (lambda cls, title, default, origin: button = cls.createNormalRoundButtonWithTitle_default_origin_(title, default, origin)button.setBordered_(NO)button.cell().setBackgroundColor_(NSColor.grayColor())button)()
    createNormalRoundButtonWithTitle_ = (lambda cls, title: cls.createNormalRoundButtonWithTitle_default_(title, False))()
    createNormalRoundButtonWithTitle_default_ = (lambda cls, title, default: cls.createNormalRoundButtonWithTitle_default_origin_(title, default, (0, 0)))()
    createNormalRoundButtonWithTitle_default_origin_ = (lambda cls, title, default, origin: if isinstance(cls, objc_object):
cls = cls.__class__button = cls.alloc().initWithFrame_(NSRect(origin, (0, 0)))button.setBezelStyle_(NSRoundedBezelStyle)button.setButtonType_(NSMomentaryPushInButton)button.setFont_(NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize)))if default:
button.setKeyEquivalent_(ENTER_KEY)button.setTitle_(title)button.sizeToFitWithPadding()button)()
    createNormalCheckboxWithTitle_ = (lambda cls, title: cls.createNormalCheckboxWithTitle_origin_(title, (0, 0)))()
    createNormalCheckboxWithTitle_origin_ = (lambda cls, title, origin: if isinstance(cls, objc_object):
cls = cls.__class__button = cls.alloc().initWithFrame_(NSRect(origin, (0, 0)))button.setButtonType_(NSSwitchButton)button.setFont_(NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize)))button.setAttributedTitle_(NSAttributedString.linkify(title))button.sizeToFit()button)()
    createRadioButtonWithTitle_tag_origin_ = (lambda cls, title, tag, origin: if isinstance(cls, objc_object):
cls = cls.__class__button = cls.alloc().initWithFrame_(NSRect(origin, (0, 0)))button.setButtonType_(NSRadioButton)button.cell().setControlSize_(NSRegularControlSize)button.setFont_(NSFont.fontWithName_size_(button.cell().font().fontName(), NSFont.systemFontSize()))button.setTitle_(title)# WARNING: Decompyle incomplete
)()
    
    def placeLeftOfButton_(self, button):
        button_frame = button.frame()
        self.setFrameOrigin_(NSPoint(button_frame.origin.x - NSWidth(self.frame()), button_frame.origin.y))


NSButton = <NODE:27>(NSButton, 'NSButton', Category(NSButton))

def NSControl():
    '''NSControl'''
    
    def placeRelativeToLabel_(self, label):
        label_frame = label.frame()
        if label.isFlipped():
            bl_offset = 0
            if hasattr(self, 'flippedBaselineOffset'):
                bl_offset = self.flippedBaselineOffset()
            self.setFrameOrigin_(NSPoint(NSMaxX(label_frame) + LABEL_PADDING + self.insetRect().origin.x, label_frame.origin.y - bl_offset))
            return None
        bl_offset = None
        if hasattr(self, 'baselineOffset'):
            bl_offset = self.baselineOffset()
        self.setFrameOrigin_(NSPoint(label_frame.origin.x + NSWidth(label_frame) + LABEL_PADDING + self.insetRect().origin.x, (label_frame.origin.y + NSHeight(label_frame) - NSHeight(self.frame())) + bl_offset))

    
    def nextControlY(self):
        return NSMaxY(self.frame()) + self.verticalPadding()


NSControl = <NODE:27>(NSControl, 'NSControl', Category(NSControl))

def NSDatePicker():
    '''NSDatePicker'''
    
    def verticalPadding(self):
        return 8

    
    def baselineOffset(self):
        return 3


NSDatePicker = <NODE:27>(NSDatePicker, 'NSDatePicker', Category(NSDatePicker))

class WrappingNSButtonCell(NSButtonCell):
    
    def init(self):
        self.max_width = 0
        self.baseline = 0
        return objc.super(WrappingNSButtonCell, self).init()

    
    def cellSize(self):
        orig_size = objc.super(WrappingNSButtonCell, self).cellSize()
        if self.max_width:
            max_text_width = self.max_width - self.image().size().width - 4
            text_rect = self.attributedTitle().boundingRectWithSize_options_(NSSize(max_text_width, 0), NSStringDrawingUsesLineFragmentOrigin)
            ret = NSSize(int(math.ceil(NSWidth(text_rect))) + 4 + self.image().size().width, max(NSHeight(text_rect), self.image().size().height))
            self.baseline = int((ret.height - orig_size.height) / 2)
            return ret

    drawTitle_withFrame_inView_ = (lambda self, title, frame, view: if self.max_width:
title.drawWithRect_options_(frame, NSStringDrawingUsesLineFragmentOrigin)frameobjc.super(WrappingNSButtonCell, self).drawTitle_withFrame_inView_(title, frame, view))()
    drawImage_withFrame_inView_ = (lambda self, image, frame, view: if self.max_width and self.baseline:
frame = NSRect((frame.origin.x, frame.origin.y - self.baseline), (frame.size.width, frame.size.height))objc.super(WrappingNSButtonCell, self).drawImage_withFrame_inView_(image, frame, view))()
    
    def setMaxWidth_(self, max_width):
        self.max_width = max_width



def NSMatrix():
    '''NSMatrix'''
    
    def verticalPadding(self):
        return 12

    
    def baselineOffset(self):
        return 0

    createRadioGroup_ = (lambda cls, choices: NSMatrix.createRadioGroup_verticalSpacing_maxWidth_(choices, 4, None))()
    createRadioGroup_verticalSpacing_maxWidth_ = (lambda cls, choices, vertical_spacing, max_width: matrix = NSMatrix.alloc().initWithFrame_mode_cellClass_numberOfRows_numberOfColumns_(NSZeroRect, NSRadioModeMatrix, WrappingNSButtonCell, 0, 1)matrix.setIntercellSpacing_(NSSize(2, vertical_spacing))cell_font = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))for x, text in enumerate(choices):
cell = matrix.makeCellAtRow_column_(x, 1)cell.setLineBreakMode_(0)cell.setWraps_(YES)cell.setTitle_(text)cell.setButtonType_(NSRadioButton)cell.setFont_(cell_font)cell.setTag_(x)cell.setMaxWidth_(max_width)matrix.addRowWithCells_([
cell])matrix.selectCellAtRow_column_(1, 1)matrix.sizeToFit()matrix)()
    createTaggedRadioGroup_verticalSpacing_maxWidth_ = (lambda cls = classmethod, tagged_choices = classmethod, vertical_spacing = classmethod, max_width = ('tagged_choices', 'List[Tuple[int, Text]]', 'vertical_spacing', 'Union[int, float]', 'max_width', 'Union[int, float]', 'return', 'NSMatrix'): matrix = NSMatrix.alloc().initWithFrame_mode_cellClass_numberOfRows_numberOfColumns_(NSZeroRect, NSRadioModeMatrix, WrappingNSButtonCell, 0, 1)matrix.setIntercellSpacing_(NSSize(2, vertical_spacing))cell_font = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))for tag, text in enumerate(tagged_choices):
cell = matrix.makeCellAtRow_column_(x, 1)cell.setLineBreakMode_(0)cell.setWraps_(YES)cell.setTitle_(text)cell.setButtonType_(NSRadioButton)cell.setFont_(cell_font)cell.setTag_(tag)cell.setMaxWidth_(max_width)matrix.addRowWithCells_([
cell])matrix.selectCellAtRow_column_(1, 1)matrix.sizeToFit()matrix)()
    createTaggedRadioGroup_horizontalSpacing_maxWidth_ = (lambda cls = None, tagged_choices = None, horizontal_spacing = classmethod, max_width = ('tagged_choices', 'List[Tuple[int, Text]]', 'horizontal_spacing', 'int', 'max_width', 'Union[int, float]', 'return', 'NSMatrix'): matrix = NSMatrix.alloc().initWithFrame_mode_cellClass_numberOfRows_numberOfColumns_(NSZeroRect, NSRadioModeMatrix, WrappingNSButtonCell, 1, 0)matrix.setIntercellSpacing_(NSSize(horizontal_spacing, 2))cell_font = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))for tag, text in enumerate(tagged_choices):
cell = matrix.makeCellAtRow_column_(1, column)cell.setLineBreakMode_(0)cell.setWraps_(YES)cell.setTitle_(text)cell.setButtonType_(NSRadioButton)cell.setFont_(cell_font)cell.setTag_(tag)cell.setMaxWidth_(max_width)matrix.addColumnWithCells_([
cell])matrix.selectCellAtRow_column_(1, 1)matrix.sizeToFit()matrix)()
    createRadioGroup_verticalSpacing_cellClass_cellInitializer_ = (lambda cls, choices = None, vertical_spacing = None, cell_class = classmethod, cell_initializer = ('choices', 'List[Text]', 'vertical_spacing', 'Union[int, float]', 'cell_class', 'Any', 'cell_initializer', 'Callable', 'return', 'None'): matrix = NSMatrix.alloc().initWithFrame_mode_cellClass_numberOfRows_numberOfColumns_(NSZeroRect, NSRadioModeMatrix, cell_class, 0, 1)matrix.setIntercellSpacing_(NSSize(2, vertical_spacing))# WARNING: Decompyle incomplete
)()
    
    def removeAllRows(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def addChoices_cellInitializer_(self = None, choices = None, cell_initializer = None):
        pass
    # WARNING: Decompyle incomplete


NSMatrix = <NODE:27>(NSMatrix, 'NSMatrix', Category(NSMatrix))

def NSPopUpButton():
    '''NSPopUpButton'''
    
    def insetRect(self):
        return NSZeroRect

    
    def verticalPadding(self):
        return 16

    
    def flippedBaselineOffset(self):
        return 3

    
    def baselineOffset(self):
        return 6

    createNormalPopUpButtonWithChoices_default_ = (lambda cls, choices, default: cls.createNormalPopUpButtonWithChoices_default_origin_(choices, default, (0, 0)))()
    createNormalPopUpButtonWithChoices_default_origin_ = (lambda cls, choices, default, origin: choice = cls.alloc().initWithFrame_(NSRect(origin, (0, 0)))choice.addItemsWithTitles_(choices)choice.selectItemAtIndex_(default)choice.sizeToFit()choice)()
    createNoBorderPopUpButtonWithChoices_default_ = (lambda cls, choices, default: cls.createNoBorderPopUpButtonWithChoices_default_origin_(choices, default, (0, 0)))()
    createNoBorderPopUpButtonWithChoices_default_origin_ = (lambda cls, choices, default, origin: choice = cls.createNormalPopUpButtonWithChoices_default_origin_(choices, default, origin)choice.setBordered_(NO)choice)()
    
    def applyAttributes_(self, attrs_dict):
        for item in self.itemArray():
            title = item.title()
            attrTitle = NSAttributedString.alloc().initWithString_attributes_(title, attrs_dict)
            item.setAttributedTitle_(attrTitle)
            return None

    
    def addTitle_withTag_(self = classmethod, title = classmethod, tag = classmethod):
        menu_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(title, None, '')
        menu_item.setTag_(tag)
        self.menu().addItem_(menu_item)

    
    def addTitlesWithTags_(self = None, titles_with_tags = None):
        for title, tag in titles_with_tags:
            self.addTitle_withTag_(title, tag)
            return None


NSPopUpButton = <NODE:27>(NSPopUpButton, 'NSPopUpButton', Category(NSPopUpButton))

def NSProgressIndicator():
    '''NSProgressIndicator'''
    createSmallSpinner = (lambda cls: pi = NSProgressIndicator.alloc().initWithFrame_(NSZeroRect)pi.setStyle_(NSProgressIndicatorSpinningStyle)pi.setControlSize_(NSSmallControlSize)pi.setIndeterminate_(YES)pi.sizeToFit()pi)()
    createRegularSpinner = (lambda cls: progress_indicator = NSProgressIndicator.alloc().initWithFrame_(NSZeroRect)progress_indicator.setStyle_(NSProgressIndicatorSpinningStyle)progress_indicator.setControlSize_(NSRegularControlSize)progress_indicator.setIndeterminate_(YES)progress_indicator.sizeToFit()progress_indicator)()

NSProgressIndicator = <NODE:27>(NSProgressIndicator, 'NSProgressIndicator', Category(NSProgressIndicator))

def NSSecureTextField():
    '''NSSecureTextField'''
    createNormalSecureTextField = (lambda cls: NSSecureTextField.createNormalSecureTextFieldWithFont_(None))()
    createNormalSecureTextFieldWithFont_ = (lambda cls, font: cls.createNormalSecureTextFieldWithFont_initialValue_placeholder_(font, '', None))()
    createNormalSecureTextFieldWithFont_initialValue_placeholder_ = (lambda cls, font, initialValue, placeholder = ('', None): pass# WARNING: Decompyle incomplete
)()

NSSecureTextField = <NODE:27>(NSSecureTextField, 'NSSecureTextField', Category(NSSecureTextField))

def NSSearchField():
    '''NSSearchField'''
    
    def horizontalPadding(self):
        return 8

    createSearchFieldWithWidth_ = (lambda cls, width: sf = NSSearchField.alloc().initWithFrame_(NSZeroRect)sf.sizeToFit()f = sf.frame()f.size.width = widthsf.setFrame_(f)sf)()

NSSearchField = <NODE:27>(NSSearchField, 'NSSearchField', Category(NSSearchField))

def NSStepper():
    '''NSStepper'''
    
    def baselineOffset(self):
        return 4

    
    def horizontalPadding(self):
        return LABEL_PADDING


NSStepper = <NODE:27>(NSStepper, 'NSStepper', Category(NSStepper))

def NSTextField():
    '''NSTextField'''
    
    def horizontalPadding(self):
        return LABEL_PADDING

    
    def verticalPadding(self):
        return 10

    
    def baselineOffset(self):
        if self.drawsBackground():
            return 2

    placeButtonToRight = (lambda self, button: padding = 4button.sizeToFitWithPadding()my_frame = self.frame()button_origin = NSPoint(my_frame.origin.x + my_frame.size.width + padding, my_frame.origin.y - STATICTEXT_TO_BUTTON_BASELINE_ADJUSTMENT)button.setFrameOrigin_(button_origin)NSSize(my_frame.size.width + padding + button.frame().size.width, max(my_frame.size.height + STATICTEXT_TO_BUTTON_BASELINE_ADJUSTMENT, button.frame().size.height)))()
    placeDropdownToRight = (lambda self, dropdown: padding = 4dropdown.sizeToFitWithPadding()my_frame = self.frame()dropdown_origin = NSPoint(my_frame.origin.x + my_frame.size.width + padding, my_frame.origin.y - STATICTEXT_TO_DROPDOWN_BASELINE_ADJUSTMENT)dropdown.setFrameOrigin_(dropdown_origin)NSSize(my_frame.size.width + padding + dropdown.frame().size.width, max(my_frame.size.height + STATICTEXT_TO_DROPDOWN_BASELINE_ADJUSTMENT, dropdown.frame().size.height)))()
    
    def sizeForWidth_(self, width):
        infinite_height_frame = self.frame()
        infinite_height_frame.size.width = width - infinite_height_frame.origin.x
        infinite_height_frame.size.height = INFINITE_DIMENSION
        return self.cell().cellSizeForBounds_(infinite_height_frame)

    
    def wrapToWidth_(self, width):
        proper_size = self.sizeForWidth_(width)
        self.setFrameSize_(proper_size)
        return proper_size

    
    def balancedWrapToWidth_(self, width):
        largest_size = self.sizeForWidth_(INFINITE_DIMENSION)
        cur_size = self.sizeForWidth_(width)
    # WARNING: Decompyle incomplete

    createLabelWithText_ = (lambda cls = objc.python_method, text = objc.python_method: font = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))NSTextField.createLabelWithText_font_(text, font))()
    createLabelWithText_origin_ = (lambda cls = None, text = None, origin = classmethod: font = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))NSTextField.createLabelWithText_font_maxWidth_origin_(text, font, None, origin))()
    createLabelWithText_font_ = (lambda cls = None, text = None, font = classmethod: NSTextField.createLabelWithText_font_maxWidth_(text, font, None))()
    createLabelWithText_maxWidth_ = (lambda cls = None, text = None, max_width = classmethod: font = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))NSTextField.createLabelWithText_font_maxWidth_(text, font, max_width))()
    createLabelWithText_font_maxWidth_ = (lambda cls = None, text = None, font = classmethod, max_width = (None,): NSTextField.createLabelWithText_font_maxWidth_origin_(text, font, max_width, (0, 0)))()
    createLabelWithText_font_maxWidth_origin_ = (lambda cls = None, text = None, font = classmethod, max_width = (None, (0, 0)), origin = ('text', 'str', 'font', 'NSFont', 'max_width', 'Optional[int]', 'origin', 'Tuple[int, int]', 'return', 'NSTextField'): label = NSTextField.alloc().initWithFrame_(NSRect(origin, (0, 0)))label.setAllowsEditingTextAttributes_(YES)label.setBezeled_(NO)label.setDrawsBackground_(NO)label.setEditable_(NO)label.setFont_(font)label.setSelectable_(NO)label.setStringValue_(text)label.sizeToFit()# WARNING: Decompyle incomplete
)()
    createNormalTextField = (lambda cls: f = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))cls.createNormalTextFieldWithFont_(f))()
    createNormalTextFieldWithPlaceholder = (lambda cls, placeholder: f = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))cls.createNormalTextFieldWithFont_initialValue_placeholder_(f, '', placeholder))()()
    createNormalTextFieldWithFont_ = (lambda cls, font: cls.createNormalTextFieldWithFont_initialValue_placeholder_(font, '', None))()
    createNormalTextFieldWithFont_initialValue_placeholder_ = (lambda cls, font, initialValue, placeholder = ('', None): tf = NSTextField.alloc().initWithFrame_(NSZeroRect)tf.setBezeled_(YES)tf.setDrawsBackground_(YES)tf.setEditable_(YES)tf.setFont_(font)tf.setRefusesFirstResponder_(NO)tf.setSelectable_(YES)tf.setStringValue_(initialValue)# WARNING: Decompyle incomplete
)()
    createSubtitle_ = (lambda cls, text: font = NSFont.systemFontOfSize_(11)text_field = NSTextField.createLabelWithText_font_(text, font)text_field.setTextColor_(NSColor.colorWithCGColor_(COLOR_DROPBOX_SUBTEXT_GRAY))text_field.setEmbossed()text_field)()
    createSubtitle_width_balanced_ = (lambda cls, text, width, balanced: text = cls.createSubtitle_(text)text.setAlignment_(NSCenterTextAlignment)if balanced:
text.balancedWrapToWidth_(width)else:
text.wrapToWidth_(width)text)()
    
    def setEmbossed(self):
        self.cell().setBackgroundStyle_(NSBackgroundStyleRaised)

    
    def placeRelativeToControl_(self, control):
        bl_offset = 0
        if hasattr(control, 'baselineOffset'):
            bl_offset = control.baselineOffset()
        self.setFrameOrigin_(NSPoint(control.frame().origin.x - NSWidth(self.frame()) - LABEL_PADDING, control.frame().origin.y + bl_offset))


NSTextField = <NODE:27>(NSTextField, 'NSTextField', Category(NSTextField))

def NSTokenField():
    '''NSTokenField'''
    createTokenFieldWithPlaceholder_ = (lambda cls, placeholder = (None,): NSTokenField.setCellClass_(DBTokenFieldCell)font = NSFont.systemFontOfSize_(NSFont.systemFontSizeForControlSize_(NSRegularControlSize))NSTokenField.createTokenFieldWithFont_placeholder_(font, placeholder))()
    createTokenFieldWithFont_placeholder_ = (lambda cls, font, placeholder = (None,): tf = NSTokenField.alloc().initWithFrame_(NSZeroRect)tf.setBezeled_(YES)tf.setFont_(font)tf.setCompletionDelay_(0.5)# WARNING: Decompyle incomplete
)()

NSTokenField = <NODE:27>(NSTokenField, 'NSTokenField', Category(NSTokenField))

class DBTokenFieldCell(NSTokenFieldCell):
    setUpTokenAttachmentCell_forRepresentedObject_ = (lambda self, aCell, reprObject: display_string = Noneif isinstance(reprObject, dict):
display_string = reprObject.get('display_string')# WARNING: Decompyle incomplete
)()


class DBAttachmentCell(NSTokenAttachmentCell):
    
    def setUp(self):
        self.size = None
        self.strokeColorUnselected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.521569, 0.682353, 0.8, 1)
        self.fillColorUnselected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.768627, 0.905882, 1, 1)
        self.strokeColorSelected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0, 0.329412, 0.6, 1)
        self.fillColorSelected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0, 0.494118, 0.901961, 1)
        
        try:
            reprObject = self.representedObject()
            if 'warn_level' in reprObject or reprObject['warn_level']:
                if reprObject['warn_level'] == 'error':
                    self.strokeColorUnselected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.898039, 0.584314, 0.584314, 1)
                    self.fillColorUnselected = NSColor.colorWithCalibratedRed_green_blue_alpha_(1, 0.8, 0.8, 1)
                    self.strokeColorSelected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.568627, 0.176471, 0.176471, 1)
                    self.fillColorSelected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.815686, 0.25098, 0.25098, 1)
                    return None
                self.strokeColorUnselected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.85098, 0.74902, 0.45098, 1)
                self.fillColorUnselected = NSColor.colorWithCalibratedRed_green_blue_alpha_(1, 0.933333, 0.733333, 1)
                self.strokeColorSelected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.741176, 0.435294, 0.00784314, 1)
                self.fillColorSelected = NSColor.colorWithCalibratedRed_green_blue_alpha_(0.941176, 0.556863, 0.00392157, 1)
                return None
            return None
            return None
        except Exception:
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UI_KIT)
            return None


    tokenBackgroundColor = (lambda self: try:
if self.getDrawSelected():
self.strokeColorSelectedNone.strokeColorUnselectedexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UI_KIT))()
    
    def getDrawSelected(self):
        
        try:
            if type(self.representedObject() == dict):
                return self.representedObject().get('selected', False)
            return None
        except Exception:
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UI_KIT)
            return False


    tokenForegroundColor = (lambda self: try:
attr_string = self.attributedStringValue()if len(attr_string) == 0:
self.fillColorUnselected(attrs, r) = None.attributesAtIndex_effectiveRange_(0, None)new_attr_string = NSMutableAttributedString.alloc().initWithString_attributes_(attr_string.string(), attrs)if self.getDrawSelected():
new_attr_string.setAttributes_range_({
'NSColor': NSColor.whiteColor() }, NSMakeRange(0, attr_string.length()))self.setAttributedStringValue_(new_attr_string)self.fillColorSelectedNone.setAttributes_range_({
'NSColor': NSColor.blackColor() }, NSMakeRange(0, attr_string.length()))self.setAttributedStringValue_(new_attr_string)self.fillColorUnselectedexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UI_KIT))()
    cellSizeForBounds_ = (lambda self, bounds: try:
if self.size:
self.sizeself.size = objc.super(DBAttachmentCell, self).cellSizeForBounds_(bounds)self.size.height = min((18, self.size.height + 2))self.sizeexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UI_KIT))()
    drawingRectForBounds_ = (lambda self, bounds: try:
drawingRect = objc.super(DBAttachmentCell, self).drawingRectForBounds_(bounds)if drawingRect.size.height > 18:
18 = drawingRect.size, drawingRect.size.height -= 2, .heightdrawingRectexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UI_KIT))()
    titleRectForBounds_ = (lambda self, bounds: try:
titleRect = objc.super(DBAttachmentCell, self).titleRectForBounds_(bounds)if titleRect.size.height > 18:
18 = titleRect.size, titleRect.size.width += 2, .widthtitleRectexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.UI_KIT))()


def NSView():
    '''NSView'''
    
    def insetRect(self):
        return NSZeroRect

    
    def alignRightInSuperview(self, offset = (CONTENT_BORDER,)):
        parent_bounds = self.superview().bounds()
        self.setFrameOrigin_(NSPoint(parent_bounds.origin.x + NSWidth(parent_bounds) - NSWidth(self.frame()) - offset - self.insetRect().origin.x, self.frame().origin.y))

    
    def alignLeftInSuperview(self, offset = (CONTENT_BORDER,)):
        parent_bounds = self.superview().bounds()
        self.setFrameOrigin_(NSPoint(parent_bounds.origin.x + offset + self.insetRect().origin.x, self.frame().origin.y))

    
    def alignRightToOffset_(self, offset):
        self.setFrameOrigin_(NSPoint(offset - NSWidth(self.frame()) - self.insetRect().origin.x, self.frame().origin.y))

    
    def alignLeftToOffset_(self, offset):
        self.setFrameOrigin_(NSPoint(offset + self.insetRect().origin.x, self.frame().origin.y))

    
    def offsetFrame_(self, offset):
        f = self.frame()
        self.setFrameOrigin_(NSPoint(f.origin.x + offset.x, f.origin.y + offset.y))

    
    def alignBottomInSuperview(self, offset = (CONTENT_BORDER,)):
        parent_bounds = self.superview().bounds()
        if not self.superview().isFlipped():
            self.setFrameOrigin_(NSPoint(self.frame().origin.x, parent_bounds.origin.y + offset + self.insetRect().origin.y))
            return None
        None.setFrameOrigin_(NSPoint(self.frame().origin.x, parent_bounds.origin.y + NSHeight(parent_bounds) - offset - NSHeight(self.frame()) - self.insetRect().origin.y))

    
    def addNormalRoundButtonWithTitle_action_(self, title, action):
        button = NSButton.createNormalRoundButtonWithTitle_(title)
        button.setTarget_(self)
        button.setAction_(action)
        self.addSubview_(button)
        return button

    
    def addColoredRoundButtonWithTitle_action_(self, title, action):
        button = NSButton.createColoredRoundButtonWithTitle_(title)
        button.setTarget_(self)
        button.setAction_(action)
        self.addSubview_(button)
        return button

    
    def addNormalTextFieldWithLabel_(self = None, text = None):
        label = NSTextField.createLabelWithText_(text)
        self.addSubview_(label)
        return label

    
    def centerInSuperview(self):
        if self.superview():
            self.centerHorizontallyInSuperview()
            self.centerVerticallyInSuperview()
            return None

    
    def centerHorizontallyInSuperview(self):
        parent_bounds = self.superview().bounds()
        self.setFrameOrigin_(NSPoint(parent_bounds.origin.x + NSWidth(parent_bounds) / 2 - NSWidth(self.frame()) / 2, self.frame().origin.y))

    
    def centerVerticallyInSuperview(self):
        parent_bounds = self.superview().bounds()
        self.setFrameOrigin_(NSPoint(self.frame().origin.x, parent_bounds.origin.y + NSHeight(parent_bounds) / 2 - NSHeight(self.frame()) / 2))

    
    def clearSubviews(self = None):
        subviews = list(self.subviews())
        for view in subviews:
            view.removeFromSuperview()
            return None


NSView = <NODE:27>(NSView, 'NSView', Category(NSView))

class ManagedRadioButton(NSButton):
    
    def __new__(cls, frame, title, tag):
        return ManagedRadioButton.alloc().initWithFrame_title_tag_(frame, title, tag)

    
    def initWithFrame_title_tag_(self, frame, title, tag):
        self = objc.super(ManagedRadioButton, self).initWithFrame_(frame)
    # WARNING: Decompyle incomplete

    
    def acceptsFirstResponder(self):
        return False

    
    def mouseDown_(self, event):
        pass
    # WARNING: Decompyle incomplete

    
    def mouseUp_(self, event):
        pass
    # WARNING: Decompyle incomplete



def help_button(x, y):
    button = NSButton.alloc().initWithFrame_(NSRect((x, y), (0, 0)))
    button.setTitle_('')
    button.setBezelStyle_(NSHelpButtonBezelStyle)
    button.cell().setControlSize_(NSRegularControlSize)
    button.sizeToFit()
    return button


def height_for_fixed_width(theControl, width):
    infinite_height_frame = theControl.frame()
    infinite_height_frame.size.width = width - infinite_height_frame.origin.x
    infinite_height_frame.size.height = INFINITE_DIMENSION
    proper_frame = theControl.cell().cellSizeForBounds_(infinite_height_frame)
    theControl.setFrame_(NSRect((infinite_height_frame.origin.x, infinite_height_frame.origin.y), (proper_frame.width, proper_frame.height)))
    return proper_frame.height


def align_center_to_offset(theControl, offset):
    new_frame = theControl.frame()
    new_frame.origin.x = offset - new_frame.size.width / 2
    theControl.setFrame_(new_frame)

