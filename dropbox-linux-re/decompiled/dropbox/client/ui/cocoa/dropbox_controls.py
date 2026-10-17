# Source Generated with Decompyle++
# File: dropbox_controls.pyc (Python 3.11)

import functools
import os
import time
from abc import abstractmethod
from typing import Any, Callable, List, Optional, Text, Tuple, Union
import objc
from AppKit import NSAccessibilityLinkRole, NSAlert, NSAlertFirstButtonReturn, NSAlertSecondButtonReturn, NSApp, NSApplication, NSAttributedString, NSBackingStoreBuffered, NSBeginAlertSheet, NSBezierPath, NSButton, NSCancelButton, NSCenterTextAlignment, NSClosableWindowMask, NSColor, NSCommandKeyMask, NSCompositeSourceOver, NSCriticalAlertStyle, NSCursor, NSEvent, NSFont, NSForegroundColorAttributeName, NSHelpButtonBezelStyle, NSImageAlignRight, NSImageInterpolationNone, NSImageView, NSLayoutManager, NSLeftMouseDragged, NSLeftMouseDraggedMask, NSLeftMouseUp, NSLeftMouseUpMask, NSLineBreakByWordWrapping, NSLinkAttributeName, NSMenu, NSMenuItem, NSMomentaryPushInButton, NSMutableAttributedString, NSMutableParagraphStyle, NSNotificationCenter, NSNumber, NSNumberFormatter, NSOffState, NSOKButton, NSOnState, NSOpenPanel, NSParagraphStyleAttributeName, NSPopUpButton, NSProgressIndicator, NSProgressIndicatorBarStyle, NSRegularControlSize, NSResponder, NSScaleNone, NSSingleUnderlineStyle, NSStepper, NSStringDrawingUsesLineFragmentOrigin, NSTextContainer, NSTextField, NSTextStorage, NSTextView, NSTitledWindowMask, NSUnderlineStyleAttributeName, NSView, NSWindow, NSWindowWillCloseNotification, NSWorkspace
from Foundation import NSHeight, NSHomeDirectory, NSMakeRange, NSMakeRect, NSMaxX, NSMaxY, NSObject, NSPoint, NSPointInRect, NSRect, NSSize, NSURL, NSWidth, NSZeroRect
from objc import ivar, NO, typedSelector, YES
from PyObjCTools import AppHelper
from constants import Colors
from dynamic_layouts import CONTENT_BORDER, help_button, NEARBY_CONTROL_BORDER
from util import edit_attributed_string, guarded, protected_action_method, resize_image, save_graphics_state
from dropbox.client.authentication.account import Account
from dropbox.client.move_dropbox_folder import MountPathValidationError, MountPathValidationErrorCode, validate_parent_mount_path
from dropbox.client.ui.cocoa.styles import COLOR_DROPBOX_LIGHT_BLACK
from dropbox.client.ui.common.constants import ResizeMethod
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client.ui.common.preferences import UNSUPPORTED_FS_HELP_URL
from dropbox.client.ui.common.strings import AccountString
from dropbox.client.ui.common.uikit import on_ui_thread
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.gui import assert_message_queue, event_handler, message_sender, spawn_thread_with_name
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

class EFFlippedView(NSView):
    
    def __new__(cls, frame):
        return EFFlippedView.alloc().initWithFrame_(frame)

    
    def initWithFrame_(self, frame):
        self = objc.super(EFFlippedView, self).initWithFrame_(frame)
        return self

    
    def isFlipped(self):
        return YES



class FlippedTextView(NSTextView):
    
    def __new__(cls, frame):
        return FlippedTextView.alloc().initWithFrame_(frame)

    
    def initWithFrame_(self, frame):
        self = objc.super(FlippedTextView, self).initWithFrame_(frame)
        return self

    
    def isFlipped(self):
        return YES



class FlippedButton(NSButton):
    
    def isFlipped(self):
        return YES



class WindowLifetimeHandlingView(NSView):
    viewWillMoveToWindow_ = (lambda self = None, window = objc.typedSelector(b'v@:@'): notification_center = NSNotificationCenter.defaultCenter()self._on_view_window_closed()notification_center.removeObserver_name_object_(self, NSWindowWillCloseNotification, self.window())# WARNING: Decompyle incomplete
)()()
    windowWillCloseNotification_ = (lambda self = None, _ = objc.typedSelector(b'v@:@'): self._on_view_window_closed())()()
    
    def _on_view_moved_to_window(self = None):
        pass

    
    def _on_view_window_closed(self = None):
        pass



class FlippedWindowLifetimeHandlingView(WindowLifetimeHandlingView):
    
    def isFlipped(self = None):
        return YES



class PrefView(WindowLifetimeHandlingView):
    initWithContext_DropboxApp_width_ = (lambda self = None, context = objc.typedSelector(b'@@:@@i'), dropbox_app = event_handler, width = ('context', 'MachineContext', 'dropbox_app', 'DropboxApplication', 'width', 'int', 'return', "'PrefView'"): self = objc.super(PrefView, self).initWithFrame_(NSZeroRect)# WARNING: Decompyle incomplete
)()()
    userNeedsHelp_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): self.window().userNeedsHelp_(sender))()()
    settingsChanged = (lambda self = None: pass)()()
    initialHeightNeeded_ = (lambda self = None: height_needed = CONTENT_BORDERself.helpButton.setFrameOrigin_(NSPoint(0, height_needed))self.helpButton.alignRightToOffset_(self._width - CONTENT_BORDER)item_height = self.helpButton.frame().size.heightheight_needed += item_height - NEARBY_CONTROL_BORDERheight_needed)()()
    flagsChanged_ = (lambda self = None, event = None: pass)()


class DropboxDefaultMenuDelegate(NSObject):
    first_responder_map = {
        'x': 'cut:',
        'c': 'copy:',
        'v': 'paste:',
        'a': 'selectAll:' }
    window_map = {
        'w': 'performClose:' }
    ESCAPE_KEY = 53
    menuHasKeyEquivalent_forEvent_target_action_ = (lambda self = None, menu = objc.typedSelector(b'Z@:@@o^@o^:'), event = event_handler: to_ret = (NO, None, None)chars = event.characters()window = NSApplication.sharedApplication().keyWindow()if not window:
to_ret# WARNING: Decompyle incomplete
)()()


class ProgressSheet(NSWindow):
    messageToDisplay = ivar('messageToDisplay')
    progressMessage = ivar('progressMessage')
    progressBar = ivar('progressBar')
    button = ivar('button')
    
    def __new__(cls, width):
        return ProgressSheet.alloc().initWithWidth_(width)

    initWithWidth_ = (lambda self, width: self = objc.super(ProgressSheet, self).initWithContentRect_styleMask_backing_defer_(NSZeroRect, NSTitledWindowMask | NSClosableWindowMask, NSBackingStoreBuffered, YES)# WARNING: Decompyle incomplete
)()()
    layoutForWidth_ = (lambda self, width: current_frame = self.frame()current_frame.size.width = widthself.setFrame_display_animate_(current_frame, NO, NO)height_needed = CONTENT_BORDER# WARNING: Decompyle incomplete
)()()
    setButtonTitle_target_action_ = (lambda self, title, target, action: pass# WARNING: Decompyle incomplete
)()()
    removeButton = (lambda self: pass# WARNING: Decompyle incomplete
)()()
    setDisplayedMessage_ = (lambda self, message: self.progressMessage.setStringValue_(message)self.layoutForWidth_(self.contentView().frame().size.width))()()
    beginModalForWindow_ = (lambda self, window: self.progressBar.startAnimation_(self)NSApp().beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_(self, window, self, self.progressDidEnd_returnCode_contextInfo_.selector, 0))()()
    progressDidEnd_returnCode_contextInfo_ = (lambda self, sheet, returnCode, ctx: self.progressBar.stopAnimation_(self)self.orderOut_(self))()()


class MoveProgressSheet(ProgressSheet):
    lastUserUpdate = ivar('lastUserUpdate')
    filesMoved = ivar('filesMoved')
    approxFileCount = ivar('approxFileCount')
    initWithWidth_ = (lambda self, width: self = objc.super(MoveProgressSheet, self).initWithWidth_(width)self.setDisplayedMessage_(PrefStrings.loc_changer_move_progress_indeterminate)# WARNING: Decompyle incomplete
)()()
    setApproxTotalFileCount_ = (lambda self, approxFileCount: self.approxFileCount = approxFileCount)()()
    innerOneFile = (lambda self: time.time() = self, self.filesMoved += 1, .filesMovedif t - self.lastUserUpdate > 0.1:
self.lastUserUpdate = tself.setDisplayedMessage_(PrefStrings.loc_changer_move_progress_determinate_t % dict(completed = self.filesMoved, total = self.approxFileCount))if self.progressBar.isIndeterminate():
self.progressBar.setIndeterminate_(NO)self.progressBar.setMinValue_(0)self.progressBar.setMaxValue_(self.approxFileCount)self.progressBar.setDoubleValue_(float(self.filesMoved))None)()()


class DBSingletonObject(NSObject):
    __the_instance: "Optional['DBSingletonObject']" = None
    sharedInstance = (lambda klass: pass# WARNING: Decompyle incomplete
)()


class DropboxSheetErrorFactory(DBSingletonObject):
    ctxMap = ivar('ctxMap')
    index = ivar('index')
    init = (lambda self: self = objc.super(DropboxSheetErrorFactory, self).init()# WARNING: Decompyle incomplete
)()()
    nextIndex = (lambda self: this_index = self.indexself.index = (self.index + 1) % 65536this_index)()()
    
    def alertShowHelp_(self = event_handler, alert = objc.typedSelector(b'i@:')):
        help_link = alert.helpAnchor()
    # WARNING: Decompyle incomplete

    
    def alertForWindow_withCaption_message_onSuccess_onCancel_successLabel_cancelLabel_helpLink_(self, window, caption, message, on_success, on_cancel, success_label, cancel_label, help_link):
        context = { }
        alert = NSAlert.alloc().init()
        ret_map = [
            NSAlertFirstButtonReturn,
            NSAlertSecondButtonReturn]
        n = 0
        for btn_label, btn_action in ((success_label, on_success), (cancel_label, on_cancel)):
            if btn_action:
                context[ret_map[n]] = btn_action
                alert.addButtonWithTitle_(btn_label)
                n += 1
            alert.setMessageText_(caption)
            alert.setAlertStyle_(NSCriticalAlertStyle)
            if message:
                alert.setInformativeText_(message)
        alert.setShowsHelp_(True)
        alert.setHelpAnchor_(help_link)
        alert.setDelegate_(self)
        self.ctxMap[alert] = context
        alert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_(window, self, 'alertDidEnd:returnCode:contextInfo:', 0)

    
    def alertForWindow_withCaption_message_onSuccess_onCancel_successLabel_cancelLabel_(self, window, caption, message, on_success, on_cancel, success_label, cancel_label):
        context = { }
        alert = NSAlert.alloc().init()
        ret_map = [
            NSAlertFirstButtonReturn,
            NSAlertSecondButtonReturn]
        n = 0
        for btn_label, btn_action in ((success_label, on_success), (cancel_label, on_cancel)):
            if btn_action:
                context[ret_map[n]] = btn_action
                alert.addButtonWithTitle_(btn_label)
                n += 1
            alert.setMessageText_(caption)
            if message:
                alert.setInformativeText_(message)
        self.ctxMap[alert] = context
        alert.beginSheetModalForWindow_modalDelegate_didEndSelector_contextInfo_(window, self, 'alertDidEnd:returnCode:contextInfo:', 0)

    
    def alertForWindow_withCaption_message_onSuccess_onCancel_(self, window, caption, message, on_success, on_cancel):
        self.alertForWindow_withCaption_message_onSuccess_onCancel_successLabel_cancelLabel_(window, caption, message, on_success, on_cancel, MiscStrings.ok_button, MiscStrings.cancel_button)

    alertDidEnd_returnCode_contextInfo_ = (lambda self, alert, returnCode, ctx: alert.window().orderOut_(alert.window())try:
context = self.ctxMap.pop(alert)context[returnCode]()Noneexcept Exception:
report_exception(component = DesktopComponent.UI_KIT)None)()()


class BaseDropboxLocationSheetMixin(object):
    _care_about_existing_dropbox = False
    _cancelled: 'Any' = None
    _account = (lambda self = None: pass)()()
    _action = (lambda self = None: pass)()()
    _dropbox_app = (lambda self = None: pass)()()
    _sync_engine_adapter = (lambda self = None: pass)()()
    targetPath = (lambda self = None: pass# WARNING: Decompyle incomplete
)()()
    window = (lambda self = None: pass)()()
    changeLocation_ = (lambda self = None, sender = None: pass)()
    getFolderName = (lambda self = None: pass)()
    check_invalid_dropbox_location = (lambda self = None, path = None: pass)()
    _changeLocation_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): self.open_panel = NSOpenPanel.openPanel()open_panel = NSOpenPanel.openPanel()open_panel.setCanChooseDirectories_(YES)open_panel.setCanCreateDirectories_(YES)open_panel.setCanChooseFiles_(NO)open_panel.setResolvesAliases_(YES)open_panel.setAllowsMultipleSelection_(NO)open_panel.setTitle_(PrefStrings.loc_changer_select_title)open_panel.setPrompt_(PrefStrings.loc_changer_select_button)text = self.render(PrefStrings.loc_changer_select_message1) + '\n' + PrefStrings.loc_changer_select_message2 % {
'folder_name': self.getFolderName() }open_panel.setMessage_(text)None(open_panel.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_, self.initialSelection, None, self.window(), self, self.openPanelDidEnd_returnCode_contextInfo_, 0))()()
    openPanelDidEnd_returnCode_contextInfo_ = (lambda self = None, sheet = None, returnCode = abstractmethod, ctx = ('sheet', 'NSOpenPanel', 'returnCode', 'int', 'ctx', 'int', 'return', 'None'): pass)()
    _openPanelDidEnd_returnCode_contextInfo_ = (lambda self = None, sheet = objc.typedSelector(b'v@:@i@'), returnCode = event_handler, ctx = ('sheet', 'NSOpenPanel', 'returnCode', 'int', 'ctx', 'int', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()()
    
    def render(self = None, string = None, **kw):
        account = self._account
    # WARNING: Decompyle incomplete

    _on_unsupported_fs_type_help_clicked = (lambda self = None: TRACE("Clicked 'System Requirements' button from unsupported FS warning from Move Dropbox")help_url = self._dropbox_app.dropbox_url_info.construct_full_url(UNSUPPORTED_FS_HELP_URL)self._dropbox_app.dropbox_url_info.launch_full_url(help_url)if self._cancelled:
self._cancelled()None)()
    _show_unsupported_fs_type_warning = (lambda self = None: TRACE('Selected location from Move Dropbox is in an unsupported location, prompting user')DropboxSheetErrorFactory.sharedInstance().alertForWindow_withCaption_message_onSuccess_onCancel_successLabel_cancelLabel_(self.window(), PrefStrings.unsupported_fs_title, PrefStrings.unsupported_fs_body_mac, functools.partial(self.changeLocation_, self), self._on_unsupported_fs_type_help_clicked, PrefStrings.unsupported_fs_ok_button, PrefStrings.unsupported_fs_help_button))()


class DropboxLocationSheetMixin(BaseDropboxLocationSheetMixin):
    _secondary = False
    
    def getFolderName(self):
        return self._account.folder_name

    
    def check_invalid_dropbox_location(self = None, path = None):
        config_manager = self._dropbox_app.config_manager
    # WARNING: Decompyle incomplete



class BaseLocationChangeHandler(object):
    targetPath = (lambda self = None: pass)()()
    window = (lambda self = None: pass)()()
    render = (lambda self = None, string = None: pass)()
    confirmMoveDropbox_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): TRACE('Move dropbox confirmed')confirm_message = self.render(PrefStrings.loc_changer_move_confirm_message, folder_name = self.targetPath)DropboxSheetErrorFactory.sharedInstance().alertForWindow_withCaption_message_onSuccess_onCancel_successLabel_cancelLabel_(self.window(), PrefStrings.loc_changer_move_confirm_caption, confirm_message, self.startMoveProgress_, (lambda : pass), PrefStrings.loc_changer_move_confirm_button, MiscStrings.cancel_button)
)()()
    
    def stopMoveProgressSuccess_(self, value):
        AppHelper.callAfter(self.innerStopMoveProgressSuccess_, value)

    innerStopMoveProgressSuccess_ = (lambda self, value: NSApp().endSheet_(self.moveProgressSheet)self.moveProgressSheet = Noneif value:
DropboxSheetErrorFactory.sharedInstance().alertForWindow_withCaption_message_onSuccess_onCancel_(self.window(), PrefStrings.loc_changer_error_moving, Text(value), self.reloadChoices, None)NoneNone.reloadChoices())()()
    
    def stopMoveProgressError_withExcInfo_(self, exc, exc_info):
        AppHelper.callAfter(self.innerStopMoveProgressError_withExcInfo_, exc, exc_info)

    innerStopMoveProgressError_withExcInfo_ = (lambda self, exc, exc_info: NSApp().endSheet_(self.moveProgressSheet)self.moveProgressSheet = NoneDropboxSheetErrorFactory.sharedInstance().alertForWindow_withCaption_message_onSuccess_onCancel_(self.window(), PrefStrings.loc_changer_error_moving, PrefStrings.loc_changer_unexpected_error, self.reloadChoices, None))()()
    innerSwapInWarnSheet_hasCancel_ = (lambda self, message, has_cancel: try:
self.moveWarningEvent.clear()NSApp().endSheet_(self.moveProgressSheet)DropboxSheetErrorFactory.sharedInstance().alertForWindow_withCaption_message_onSuccess_onCancel_(self.window(), PrefStrings.loc_changer_moving_warning, message, self.innerSwapOutWarnSheet(), None)Noneexcept Exception:
report_exception(component = DesktopComponent.UI_KIT)None)()()
    innerSwapOutWarnSheet = (lambda self: self.moveProgressSheet.progressBar.startAnimation_(self)NSApp().beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_(self.moveProgressSheet, self.window(), self, self.moveProgressDidEnd_returnCode_contextInfo_, 0)self.moveWarningEvent.set())()()
    
    def warnExternal_(self, message, has_cancel):
        
        try:
            AppHelper.callAfter(self.innerSwapInWarnSheet_hasCancel_, message, has_cancel)
            self.moveWarningEvent.wait()
            return None
        except Exception:
            report_exception(component = DesktopComponent.UI_KIT)
            return None


    startMoveProgress_ = (lambda self: self.moveProgressSheet = MoveProgressSheet.alloc().initWithWidth_(350)try:
file_count = self._sync_engine_adapter.get_dropbox_file_count(self._account)except Exception:
report_exception(severity = Severity.WARN, component = DesktopComponent.UI_KIT)file_count = 0self.moveProgressSheet.setApproxTotalFileCount_(file_count)self.moveProgressSheet.progressBar.startAnimation_(self)NSApp().beginSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_(self.moveProgressSheet, self.window(), self, self.moveProgressDidEnd_returnCode_contextInfo_, 0)self.do_move())()()
    _moveProgressDidEnd_returnCode_contextInfo_ = (lambda self, sheet, returnCode, ctx: self.moveProgressSheet.progressBar.stopAnimation_(self)sheet.orderOut_(self))()()


class LocationChangeHandler(BaseLocationChangeHandler, DropboxLocationSheetMixin):
    
    def do_move(self = None):
        new_path = os.path.abspath(os.path.normpath(self.targetPath))
        move_controller = self._dropbox_app.move_controller
    # WARNING: Decompyle incomplete



class ChoiceButton(NSPopUpButton):
    initWithDropboxApp_ = (lambda self = None, dropbox_app = objc.typedSelector(b'v@:@'): self = objc.super(ChoiceButton, self).initWithFrame_(NSZeroRect)# WARNING: Decompyle incomplete
)()()
    _dropbox_app = (lambda self = None: self._ChoiceButton__dropbox_app)()
    changeLocation_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): self._changeLocation_(sender))()()
    openPanelDidEnd_returnCode_contextInfo_ = (lambda self, sheet, returnCode, ctx: self._openPanelDidEnd_returnCode_contextInfo_(sheet, returnCode, ctx))()()
    moveProgressDidEnd_returnCode_contextInfo_ = (lambda self, sheet, returnCode, ctx: self._moveProgressDidEnd_returnCode_contextInfo_(sheet, returnCode, ctx))()()
    drawRect_ = (lambda self = objc.typedSelector(b'v@:@i@'), rect = event_handler: graphics_context = save_graphics_state()graphics_context.setImageInterpolation_(NSImageInterpolationNone)objc.super(ChoiceButton, self).drawRect_(rect)None(None, None)Nonewith None:
if not None:
pass)()
    
    def reloadChoices(self = None):
        choices = self.get_choices()
        self.removeAllItems()
        menu = self.menu()
    # WARNING: Decompyle incomplete

    
    def get_choices(self):
        return []

    
    def get_enabled(self):
        return True

    
    def get_index(self):
        return 0



class BaseLocationButton(ChoiceButton):
    initWithDropboxApp_account_ = (lambda self = None, dropbox_app = objc.typedSelector(b'v@:@@'), account = event_handler: self._BaseLocationButton__account = accountself._BaseLocationButton__action = None# WARNING: Decompyle incomplete
)()()
    _account = (lambda self = None: self._BaseLocationButton__account)()
    _action = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _sync_engine_adapter = (lambda self = None: self._BaseLocationButton__sync_engine_adapter)()
    
    def get_choices(self = None):
        nucleus_api = self._sync_engine_adapter.nucleus_api(self._account)
        if nucleus_api and nucleus_api.is_ready():
            curr = os.path.dirname(self.get_dropbox_path())
        else:
            curr = NSHomeDirectory()
        return [
            (None, NSWorkspace.sharedWorkspace().iconForFile_(curr), os.path.basename(curr)),
            (None, None, None),
            (None, self.locationChange_, PrefStrings.other_dotdotdot)]

    
    def locationChange_(self = None, sender = None):
        if self.indexOfSelectedItem() == 0:
            return None
        self.initialSelection = None.path.dirname(self.get_dropbox_path())
        self._care_about_existing_dropbox = True
        self._BaseLocationButton__action = self.confirmMoveDropbox_
        self.changeLocation_(sender)
        self.selectItemAtIndex_(0)



class LocationButton(LocationChangeHandler, BaseLocationButton):
    
    def get_dropbox_path(self = None):
        local_config = self._dropbox_app.config_manager.local_config(self._account)
        return local_config['dropbox_path']

    
    def get_enabled(self = None):
        if self._account:
            pass
        linked = self._account.linked
        return YES if linked else NO



class BackgroundImageView(NSView):
    
    def __new__(cls, frame, image, bottom_align = (False,)):
        return BackgroundImageView.alloc().initWithFrame_image_bottomAlign_(frame, image, bottom_align)

    
    def initWithFrame_image_bottomAlign_(self, frame, image, bottom_align):
        self = objc.super(BackgroundImageView, self).initWithFrame_(frame)
        if self:
            self._image = image
            self._bottom_align = bottom_align
            self.set_defaults()
        return self

    
    def set_defaults(self):
        self._alpha = 1

    
    def setImage_(self, image):
        self._image = image
        self.setNeedsDisplay_(YES)

    
    def setImageSize_(self, size):
        if self._image.size() != size:
            self._image = resize_image(self._image, (size.width, size.height), method = ResizeMethod.CROP)
            return None

    
    def image(self):
        return self._image

    
    def setAlpha_(self, alpha):
        self._alpha = alpha
        self.setNeedsDisplay_(YES)

    
    def alpha(self):
        return self._alpha

    
    def setBottomAlign_(self, value):
        self._bottom_align = value
        self.setNeedsDisplay_(YES)

    
    def bottomAlign(self):
        return self._bottom_align

    
    def drawRect_(self, rect):
        objc.super(BackgroundImageView, self).drawRect_(rect)
        if self._bottom_align:
            image_origin = NSPoint(0, 0)
        else:
            image_origin = NSPoint(0, self.bounds().size.height / 2 - self._image.size().height / 2)
        self._image.drawAtPoint_fromRect_operation_fraction_(image_origin, NSZeroRect, NSCompositeSourceOver, self._alpha)



class PassthroughImageView(NSImageView):
    
    def __new__(cls, frame):
        return PassthroughImageView.alloc().initWithFrame_(frame)

    
    def initWithFrame_(self, frame):
        self = objc.super(PassthroughImageView, self).initWithFrame_(frame)
    # WARNING: Decompyle incomplete

    
    def mouseDown_(self, event):
        self.nextResponder().mouseDown_(event)

    
    def mouseUp_(self, event):
        self.nextResponder().mouseUp_(event)



class LinkTrackingHelper(object):
    
    def __init__(self, control, selector, url_opener, auto_layout = (None, False)):
        self._control = control
        self._selector = selector
        self._url_opener = url_opener
        self._auto_layout = auto_layout
        self._tracking_rect_tags = []
        self._tool_tip_tags = []

    setup_tracking = (lambda self, offset: self._cursor_rects = []self._link_ranges = []self._is_tracking = Falseself.clear_tracking()attr_str = self._selector()text_storage = NSTextStorage.alloc().initWithAttributedString_(attr_str)layout_manager = NSLayoutManager.alloc().init()NSTextContainer.alloc().initWithContainerSize_(s) = s, s.height += 20, .height if self._auto_layout else s, s.width += 20, .widthlayout_manager.addTextContainer_(text_container)text_storage.addLayoutManager_(layout_manager)title_rect = self._control.cell().titleRectForBounds_(self._control.bounds())i = 0# WARNING: Decompyle incomplete
)()
    clear_tracking = (lambda self: for tag in self._tracking_rect_tags:
self._control.removeTrackingRect_(tag)self._tracking_rect_tags = []for tag in self._tool_tip_tags:
self._control.removeToolTip_(tag)self._tool_tip_tags = []None)()
    
    def resetCursorRects(self):
        for rect in self._cursor_rects:
            self._control.addCursorRect_cursor_(rect, NSCursor.pointingHandCursor())
            return None

    highlight_link_index = (lambda self, idx: pass# WARNING: Decompyle incomplete
)()
    unhighlight_link_index = (lambda self, idx: pass# WARNING: Decompyle incomplete
)()
    get_tooltip = (lambda self, idx: if idx <= len(self._link_ranges):
attr_str = self._selector()(l, lrange) = attr_str.attribute_atIndex_effectiveRange_(NSLinkAttributeName, self._link_ranges[idx].location, None)l.absoluteString())()
    mouse_down_helper = (lambda self, mouse_loc, highlight, unhighlight: attr_str = self._selector()# WARNING: Decompyle incomplete
)()


class OptionalDropdown(EFFlippedView):
    ROW_SPACING = 6
    
    def __new__(cls, label, enabled, choices, default):
        return cls.alloc().initWithLabel_enabled_choices_default_(label, enabled, choices, default)

    
    def initWithLabel_enabled_choices_default_(self, label, enabled, choices, default):
        self = objc.super(OptionalDropdown, self).initWithFrame_(NSZeroRect)
    # WARNING: Decompyle incomplete

    
    def layoutControls(self):
        self._checkbox = NSButton.createNormalCheckboxWithTitle_(self._label)
        self._checkbox.setState_(NSOnState if self._enabled else NSOffState)
        self.addSubview_(self._checkbox)
        self._chooser = (lambda .0: [ label for _, label in .0 ])(self._choices(), self._default)
        self._chooser.setEnabled_(self._enabled)
        self.addSubview_(self._chooser)
        self._checkbox.setTarget_(self)
        self._checkbox.setAction_(self.updateCheckbox_)
        self._chooser.setTarget_(self)
        self._chooser.setAction_(self.updateChoice_)
        self.sizeToFit()

    
    def sizeToFitForWidth_(self, width):
        if NSMaxX(self._chooser.frame()) > width:
            self.setFrameSize_(NSSize(width, 0))
            self._checkbox.setFrameOrigin_(NSPoint(0, 0))
            self._checkbox.centerHorizontallyInSuperview()
            self._chooser.setFrameOrigin_(NSPoint(0, NSHeight(self._checkbox.frame()) + self.ROW_SPACING))
            width_needed = max(NSWidth(self._checkbox.frame()), NSWidth(self._chooser.frame()))
            self.setFrameSize_(NSSize(width_needed, NSMaxY(self._chooser.frame())))
            self._checkbox.centerHorizontallyInSuperview()
            self._chooser.centerHorizontallyInSuperview()
            return None

    
    def sizeToFit(self):
        self._checkbox.setFrameOrigin_(NSPoint(0, 4))
        self._chooser.setFrameOrigin_(NSPoint(NSWidth(self._checkbox.frame()), 0))
        width_needed = (lambda .0: pass# WARNING: Decompyle incomplete
)((self._checkbox, self._chooser)())
        height_needed = (lambda .0: pass# WARNING: Decompyle incomplete
)((self._checkbox, self._chooser)())
        self.setFrameSize_(NSSize(width_needed, height_needed))

    updateCheckbox_ = (lambda self, sender: enabled = sender.state() == NSOnStateif enabled:
self._chooser.setEnabled_(YES)(value, label) = self._choices[self._chooser.indexOfSelectedItem()]self._handler(value)NoneNone._chooser.setEnabled_(NO)self._handler(None))()()
    updateChoice_ = (lambda self, sender: if self._checkbox.state() != NSOnState:
None(value, label) = None._choices[sender.indexOfSelectedItem()]self._handler(value))()()
    
    def setHandler_(self, handler):
        self._handler = handler

    setState_ = (lambda self, state: pass# WARNING: Decompyle incomplete
)()()
    setEnabled_ = (lambda self, enabled: 