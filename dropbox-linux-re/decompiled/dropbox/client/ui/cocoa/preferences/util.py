# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import
from typing import List, Tuple
import objc
from AppKit import NSTextField, NSView
from Foundation import NSHeight, NSMaxX, NSObject, NSWidth
from dropbox.client.ui.cocoa.dropbox_controls import LocationButton
from dropbox.client.ui.cocoa.dynamic_layouts import CONTENT_BORDER
from dropbox.client.ui.common.preferences import report_prefs_interaction
PREF_WINDOW_WIDTH = 530
BUTTON_HORIZONTAL_PADDING = 12
BOX_CONTENT_BORDER = 10
OPEN_ACCESSIBILITY_DIALOG_CONSTANT = 'OPEN_ACCESSIBILITY_DIALOG_CONSTANT'
OPEN_KEXT_WIZARD_CONSTANT = 'OPEN_KEXT_WIZARD_CONSTANT'
OPEN_AUTOMATION_PERMISSIONS_CONSTANT = 'OPEN_AUTOMATION_PERMISSIONS_CONSTANT'

def set_button_width(button = None, width = None):
    new_frame = button.frame()
    new_frame.size.width = max(width, NSWidth(new_frame) + BUTTON_HORIZONTAL_PADDING)
    button.setFrame_(new_frame)


def right_align_label_with_subview(items = None, label_width = None, min_width = None, initial_y = ('items', 'List[Tuple[NSTextField, NSView, int]]', 'label_width', 'int', 'min_width', 'int', 'initial_y', 'int', 'return', 'Tuple[int, int]')):
    width_needed = min_width
    height_needed = initial_y
    for label, control, offset in items:
        label.setFrameOrigin_((label_width - NSWidth(label.frame()), height_needed))
        control.placeRelativeToLabel_(label)
        width_needed = max(width_needed, NSMaxX(control.frame()))
        padding = max(CONTENT_BORDER, control.verticalPadding()) - offset
        height_needed += NSHeight(control.frame()) + padding
        return (width_needed, height_needed)


def helpForPane_DropboxApp_(pane = None, dropbox_app = None):
    help_url = f'''prefs/mac/{pane!s}'''
    dropbox_app.dropbox_url_info.launch_full_url(dropbox_app.dropbox_url_info.help_url(help_url))


class PrefsLocationButton(LocationButton):
    changeLocation_ = (lambda self = None, sender = None: objc.super(PrefsLocationButton, self).changeLocation_(sender))()

