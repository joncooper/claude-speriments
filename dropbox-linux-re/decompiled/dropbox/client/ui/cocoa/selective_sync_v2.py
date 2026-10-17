# Source Generated with Decompyle++
# File: selective_sync_v2.pyc (Python 3.11)

import math
from typing import Any, Callable, Dict, List, Optional, Text
import objc
from AppKit import NSApp, NSBackingStoreBuffered, NSBezierPath, NSBrowser, NSBrowserCell, NSBrowserUserColumnResizing, NSButton, NSButtonCell, NSClosableWindowMask, NSColor, NSCompositeSourceOver, NSEvent, NSFocusRingTypeNone, NSFont, NSImage, NSLineBreakByTruncatingTail, NSMatrix, NSNotification, NSNotificationCenter, NSOffState, NSOnState, NSResizableWindowMask, NSSmallControlSize, NSSwitchButton, NSTextAlignmentRight, NSTextField, NSTitledWindowMask, NSView, NSViewHeightSizable, NSViewWidthSizable, NSWindow, NSWindowDidBecomeKeyNotification, NSWindowDidResignKeyNotification, NSWorkspace
from Foundation import NSFileTypeForHFSTypeCode, NSMakeRect, NSMakeSize, NSMaxX, NSMaxY, NSPoint, NSRect, NSSize, NSZeroRect
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.folder_tagger.constants import FolderTag
from dropbox.client.folder_tagger.folder_icon_mac import FolderTagIcon
from dropbox.client.selective_sync_size.folder_size_util import get_folders_total_size, human_readable_size, is_selsync_folder_size_enabled
from dropbox.client.ui.cocoa.constants import ENTER_KEY, ESCAPE_KEY
from dropbox.client.ui.cocoa.dropbox_controls import DropboxSheetErrorFactory, ImageView
from dropbox.client.ui.cocoa.dynamic_layouts import align_center_to_offset, BOTTOM_BUTTON_BORDER, height_for_fixed_width, HORIZ_BUTTON_BORDER, HORIZ_BUTTON_SPACING, NEARBY_CONTROL_BORDER
from dropbox.client.ui.cocoa.menu import EFMenu
from dropbox.client.ui.cocoa.styles import COLOR_SELSYNC_WARNING_YELLOW
from dropbox.client.ui.common.selective_sync_v2 import CheckState, log_selsync_user_action, RemoteFolder, SelectiveSyncBase, SelectiveSyncPopupWarning, SelectiveSyncScaleWarningController, SELSYNC_ERROR_HELP_URL, selsync_strings
from dropbox.client.ui.common.strings import UI as UIString
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.transitional.connection_pool import on_network_thread
from dropbox.gui import event_handler, message_sender, spawn_thread_with_name
from dropbox.infinite import infinite_exposed
from dropbox.shared.server_path import RRLowerServerPath
from dropbox.sync_engine_boundary.selsync import SelectiveSyncSet
from dropbox.sync_engine_boundary.types.local_props import FileSyncStatus
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
BROWSER_ROW_HEIGHT = 18
DEFAULT_SIMPLE_WIDTH = 630
DEFAULT_BROWSER_HEIGHT = 15 * BROWSER_ROW_HEIGHT + 2
SIZE_INFO_WIDTH = 62

class SelectiveSyncBrowserCellv2(NSBrowserCell):
    CHECK_CELL_LEFT_PADDING = 3
    isViewRelativePointInCheckCell_ = (lambda self = None, view_point = objc.typedSelector(b'i@:{NSPoint=ff}'): view_point.x < self._checkCell.cellSize().width + SelectiveSyncBrowserCellv2.CHECK_CELL_LEFT_PADDING)()()
    
    def setNode_callbackTarget_(self = None, node = None, callbackTarget = None):
        self.node = node
        self._callbackTarget = callbackTarget
        self._checkCell = NSButtonCell.alloc().init()
        self._checkCell.setButtonType_(NSSwitchButton)
        self._checkCell.setControlSize_(NSSmallControlSize)
        self._checkCell.setTitle_('')
        self._checkCell.setAllowsMixedState_(True)

    _checkstate_to_intvalue = (lambda checkstate = None: if checkstate == CheckState.Disabled or checkstate == CheckState.Unchecked:
0if None == CheckState.Mixed:
-1)()
    _intvalue_to_checkstate = (lambda intvalue = None: if intvalue == 0:
CheckState.Uncheckedif None == -1:
CheckState.MixedNone.Checked)()
    cellSizeForBounds_ = (lambda self = None, bounds = None: ret = objc.super(SelectiveSyncBrowserCellv2, self).cellSizeForBounds_(bounds)if hasattr(self, 'node'):
checksize = self._checkCell.cellSize()max(ret.height, checksize.height) = ret, ret.width += checksize.width, .widthret)()
    drawWithFrame_inView_ = (lambda self = None, frame = None, view = event_handler: pass# WARNING: Decompyle incomplete
)()
    valueForToggle = (lambda self = None: 1 if self._checkCell.intValue() == 0 else 0)()()
    intValue = (lambda self = None: self._checkCell.intValue())()()
    setIntValue_ = (lambda self = None, intValue = objc.typedSelector(NSButtonCell.setIntValue_.signature): if self.isCheckEnabled() or intValue != self._checkCell.intValue():
self._checkCell.setIntValue_(intValue)checkstate = self._intvalue_to_checkstate(intValue)self._callbackTarget.checkState_fromChild_(checkstate, self.node)NoneNone)()()
    
    def setCheckState_(self = None, new_state = None):
        current_state = self._intvalue_to_checkstate(self._checkCell.intValue())
        if self.isCheckEnabled() and new_state != current_state:
            new_intvalue = self._checkstate_to_intvalue(new_state)
            self._checkCell.setIntValue_(new_intvalue)
            return True

    setCheckHighlighted_ = (lambda self = None, boolean = objc.typedSelector(NSButtonCell.setHighlighted_.signature): self._checkCell.setHighlighted_(boolean))()()
    isCheckHighlighted = (lambda self = None: self._checkCell.isHighlighted())()()
    disable_cell = (lambda self = None: self._checkCell.setIntValue_(self._checkstate_to_intvalue(CheckState.Unchecked))self._checkCell.setEnabled_(False))()
    isCheckEnabled = (lambda self = None: self._checkCell.isEnabled())()()


class SelectiveSyncBrowserMatrixv2(NSMatrix):
    mouseDown_ = (lambda self = None, event = None: the_cell = self.selectiveSyncCellForMouseEvent_(event)if the_cell:
self.down_in_cell = the_cellthe_cell.setCheckHighlighted_(True)self.setNeedsDisplay_(True)Noneobjc.super(SelectiveSyncBrowserMatrixv2, self).mouseDown_(event)self.down_in_cell = None)()
    mouseDragged_ = (lambda self = None, event = None: the_cell = self.selectiveSyncCellForMouseEvent_(event)# WARNING: Decompyle incomplete
)()
    mouseUp_ = (lambda self = None, event = None: pass# WARNING: Decompyle incomplete
)()
    keyDown_ = (lambda self = None, event = None: 