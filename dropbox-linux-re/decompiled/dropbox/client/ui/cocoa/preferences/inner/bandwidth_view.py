# Source Generated with Decompyle++
# File: bandwidth_view.pyc (Python 3.11)

from typing import Any
import objc
from AppKit import NSMatrix, NSTextField, NSView, NSWindow
from Foundation import NSHeight, NSMaxX, NSMaxY, NSObject, NSSize, NSWidth, NSZeroRect
from dropbox.client.ui.cocoa.constants import ENTER_KEY, ESCAPE_KEY
from dropbox.client.ui.cocoa.dropbox_controls import NumericStepper
from dropbox.client.ui.cocoa.dynamic_layouts import BUTTON_TO_HELP_BUTTON_ADJUSTMENT_FLIPPED, CONTENT_BORDER, help_button, HORIZ_BUTTON_SPACING, NEARBY_CONTROL_BORDER
from dropbox.client.ui.cocoa.preferences.util import helpForPane_DropboxApp_
from dropbox.client.ui.common.pref_strings import PrefStrings
from dropbox.client.ui.common.selective_sync_v2 import selsync_strings
from dropbox.foundation.context.machine import MachineContext
from dropbox.gui import event_handler
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class InnerBandwidthView(NSView):
    SPACE_BEFORE_STEPPER = 20
    
    def __new__(cls = None, context = None, dropbox_app = None):
        return cls.alloc().initWithContext_DropboxApp_(context, dropbox_app)

    
    def initWithContext_DropboxApp_(self = None, context = None, dropbox_app = None):
        self = objc.super(InnerBandwidthView, self).initWithFrame_(NSZeroRect)
    # WARNING: Decompyle incomplete

    
    def isFlipped(self = None):
        return True

    windowOk_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): if not self.downloadStyle() == 2 and self.isDownloadValid():
self.downloadStepper.tickleAlertSheet()Noneif not None.uploadStyle() == 2 and self.isUploadValid():
self.uploadStepper.tickleAlertSheet()NoneNone.relevantSheet.savePreferences()self.relevantSheet.close())()()
    windowCancel_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): self.relevantSheet.close())()()
    sheetDidEnd_returnCode_contextInfo_ = (lambda self = None, sheet = objc.typedSelector(b'v@:@i@'), returnCode = event_handler, contextInfo = ('sheet', 'NSWindow', 'returnCode', 'int', 'contextInfo', 'Any', 'return', 'None'): sheet.orderOut_(self))()()
    
    def sizeToFit(self = None):
        height_needed = CONTENT_BORDER
        width_needed = 0
        self.downloadLabel.setFrameOrigin_((CONTENT_BORDER, height_needed))
        self.downloadMatrix.placeRelativeToLabel_(self.downloadLabel)
        width_needed = max(width_needed, NSMaxX(self.downloadMatrix.frame()))
        height_needed += NSHeight(self.downloadMatrix.frame()) + self.downloadMatrix.verticalPadding()
        self.uploadLabel.setFrameOrigin_((NSMaxX(self.downloadLabel.frame()) - NSWidth(self.uploadLabel.frame()), height_needed))
        self.uploadMatrix.placeRelativeToLabel_(self.uploadLabel)
        width_needed = max(width_needed, NSMaxX(self.uploadMatrix.frame()))
        height_needed += NSHeight(self.uploadMatrix.frame()) + self.uploadMatrix.verticalPadding()
        width_needed += 5
        width_needed_for_radio = max(NSWidth(self.downloadMatrix.frame()), NSWidth(self.uploadMatrix.frame()))
        download_limit_cell = self.downloadMatrix.cells()[-1]
        dl_stepper_adjust = width_needed_for_radio - download_limit_cell.cellSize().width
        self.downloadStepper.setFrameOrigin_(((width_needed - dl_stepper_adjust) + self.SPACE_BEFORE_STEPPER, NSMaxY(self.downloadMatrix.frame()) + self.downloadStepper.baselineOffset() - NSHeight(self.downloadStepper.frame())))
        upload_limit_cell = self.uploadMatrix.cells()[-1]
        ul_stepper_adjust = width_needed_for_radio - upload_limit_cell.cellSize().width
        self.uploadStepper.setFrameOrigin_(((width_needed - ul_stepper_adjust) + self.SPACE_BEFORE_STEPPER, NSMaxY(self.uploadMatrix.frame()) + self.uploadStepper.baselineOffset() - NSHeight(self.uploadStepper.frame())))
        width_needed = max(width_needed, NSMaxX(self.downloadStepper.frame()), NSMaxX(self.uploadStepper.frame()))
        height_needed += NEARBY_CONTROL_BORDER
        self._cancelButton.setFrameOrigin_((CONTENT_BORDER, height_needed))
        button_size = self._okButton.frame().size
        self._okButton.setFrameOrigin_((width_needed - button_size.width, height_needed))
        height_needed += button_size.height + 10
        width_needed += CONTENT_BORDER
        self.setFrameSize_(NSSize(width_needed, height_needed))
        self.helpButton.alignLeftInSuperview()
        self.helpButton.alignBottomInSuperview()
        y = self.helpButton.frame().origin.y - BUTTON_TO_HELP_BUTTON_ADJUSTMENT_FLIPPED
        self._okButton.alignRightInSuperview()
        x = self._okButton.frame().origin.x
        self._okButton.setFrameOrigin_((x, y))
        x -= self._cancelButton.frame().size.width + HORIZ_BUTTON_SPACING
        self._cancelButton.setFrameOrigin_((x, y))

    
    def radioGroupAction_(self = None, sender = None):
        if sender is self.downloadMatrix:
            self.downloadStepper.setEnabled_(sender.selectedCell().tag() == 1)
            return None
        None.uploadStepper.setEnabled_(sender.selectedCell().tag() == 2)

    
    def setDownloadSpeed_(self = None, speed = None):
        self.downloadStepper.setIntValue_(speed)

    
    def downloadSpeed(self = None):
        return float(self.downloadStepper.intValue())

    
    def setUploadSpeed_(self = None, speed = None):
        self.uploadStepper.setIntValue_(speed)

    
    def uploadSpeed(self = None):
        return float(self.uploadStepper.intValue())

    
    def setDownloadStyle_(self = None, style = None):
        pass
    # WARNING: Decompyle incomplete

    
    def downloadStyle(self = None):
        return 2 if self.downloadMatrix.selectedCell().tag() == 1 else 0

    
    def setUploadStyle_(self = None, style = None):
        pass
    # WARNING: Decompyle incomplete

    
    def uploadStyle(self = None):
        return self.uploadMatrix.selectedCell().tag()

    
    def isDownloadValid(self = None):
        return self.downloadStepper.isValid()

    
    def isUploadValid(self = None):
        return self.uploadStepper.isValid()

    userNeedsHelp_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): helpForPane_DropboxApp_('bandwidth', self._dropbox_app))()()

