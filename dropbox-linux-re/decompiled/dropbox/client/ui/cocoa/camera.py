# Source Generated with Decompyle++
# File: camera.pyc (Python 3.11)

from __future__ import absolute_import
import time
from typing import Callable, List, Optional, Text
import objc
from AppKit import NSAlertAlternateReturn, NSAlertDefaultReturn, NSApp, NSBackingStoreBuffered, NSBezierPath, NSColor, NSCompositeSourceOver, NSFloatingWindowLevel, NSFont, NSImage, NSImageAlignCenter, NSImageView, NSProgressIndicator, NSProgressIndicatorBarStyle, NSRunAlertPanel, NSScaleToFit, NSShadow, NSTextField, NSTitledWindowMask, NSWindow, NSWindowController
from Foundation import NSHeight, NSInsetRect, NSMakeRect, NSRect, NSZeroRect
from objc import NO, typedSelector, YES
from PyObjCTools import AppHelper
from constants import ENTER_KEY
from dropbox_controls import EFFlippedView
from util import protected_action_method, save_graphics_state
from dropbox.camera import Device
from dropbox.client.camera_upload.types import CameraSplashResponse
from dropbox.client.main import DropboxApplication
from dropbox.client.multiaccount.selector import MultiAccountSelector
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.ui.common.camera import CameraUI, rect_to_centered_square
from dropbox.client.ui.common.camera_strings import CameraStrings
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.misc import MiscStrings
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.client.ui.electron.camera import CameraSplashScreen
from dropbox.gui import assert_message_queue
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter

def get_camera_splash_screen(dialog_controller, handle_start, handle_cancel, handle_never, never_text = None, import_videos_text = None, account_selector = None, disable_never_button = (True, True), checkbox_checked = ('dialog_controller', 'DialogController', 'handle_start', 'Callable[[CameraSplashResponse], None]', 'handle_cancel', 'Callable[[], None]', 'handle_never', 'Callable[[], None]', 'never_text', 'Text', 'import_videos_text', 'Optional[Text]', 'account_selector', 'Optional[MultiAccountSelector]', 'return', 'CameraSplashScreen')):
    splash = CameraSplashScreen(dialog_controller, handle_start, handle_cancel, handle_never, never_text, disable_never_button, import_videos_text, checkbox_checked, account_selector)
    return splash


class ShadowedImage(NSImageView):
    
    def initWithFrame_(self, frame):
        self = objc.super(ShadowedImage, self).initWithFrame_(frame)
        if not self:
            return None
        self._shadow = NSShadow.alloc().init()
        return self

    
    def setShadowColor_(self, color):
        self._shadow.setShadowColor_(color)

    
    def setShadowOffset_(self, size):
        self._shadow.setShadowOffset_(size)

    
    def setShadowBlurRadius_(self, blur):
        self._shadow.setShadowBlurRadius_(blur)

    
    def drawRect_(self, theRect):
        self._shadow.set()
        objc.super(ShadowedImage, self).drawRect_(theRect)



class CameraProgressWindow(NSWindow):
    __new__ = (lambda cls, ui: CameraProgressWindow.alloc().initWithUI_(ui))()
    initWithUI_ = (lambda self, ui: self = objc.super(CameraProgressWindow, self).initWithContentRect_styleMask_backing_defer_(NSZeroRect, NSTitledWindowMask, NSBackingStoreBuffered, NO)self.setReleasedWhenClosed_(NO)self.setLevel_(NSFloatingWindowLevel)self.useOptimizedDrawing_(YES)self.setTitle_(CameraStrings.progress_title)v = CameraProgressView(ui)self.setContentView_(v)self.sizeToFit()self.center()self)()()
    sizeToFit = (lambda self: self.contentView().sizeToFit()old_frame = self.frame()new_frame = self.frameRectForContentRect_(self.contentView().frame())new_frame.origin = old_frame.origindelta_h = NSHeight(new_frame) - NSHeight(old_frame)self.setFrame_display_animate_(new_frame, YES, YES))()()


class ThumbnailBoxView(ShadowedImage):
    BORDER_INSET = 2
    IMAGE_INSET = 6
    
    def initWithFrame_(self, frame):
        self = objc.super(ThumbnailBoxView, self).initWithFrame_(frame)
        if not self:
            return None
        self.border = None
        return self

    
    def setBorder_(self, border):
        self.border = border

    
    def drawRect_(self, rect):
        if not self.border:
            return objc.super(ThumbnailBoxView, self).drawRect_(rect)
        save_graphics_state()
        self._shadow.set()
        NSColor.whiteColor().set()
        NSBezierPath.bezierPathWithRect_(NSInsetRect(rect, self.BORDER_INSET, self.BORDER_INSET)).fill()
        None(None, None)
    # WARNING: Decompyle incomplete



class CameraProgressView(EFFlippedView):
    THUMBNAIL_ORIGIN = (20, 15)
    THUMBNAIL_SIZE = (64, 64)
    THUMBNAIL_TIMEOUT = 2
    LABEL_ORIGIN = (102, 19)
    PROGRESS_ORIGIN = (102, 43)
    PROGRESS_SIZE = (388, 20)
    ESTIMATE_ORIGIN = (102, 67)
    SHADOW_OFFSET = (2, -2)
    SHADOW_BLUR = 3
    __new__ = (lambda cls, ui: CameraProgressView.alloc().initWithUI_(ui))()
    initWithUI_ = (lambda self, ui: self = objc.super(CameraProgressView, self).initWithFrame_(NSMakeRect(0, 0, 508, 122))# WARNING: Decompyle incomplete
)()()
    layoutControls = (lambda self: pass# WARNING: Decompyle incomplete
)()()
    sizeToFit = (lambda self: self.setFrame_(NSMakeRect(0, 0, self._width, 122)))()()
    handleCancelButton_ = (lambda self, event: self.ui.on_cancel())()
    handleHideButton_ = (lambda self, event: self.ui.progress_window_hide())()


class CocoaCameraUI(CameraUI):
    pass
# WARNING: Decompyle incomplete

