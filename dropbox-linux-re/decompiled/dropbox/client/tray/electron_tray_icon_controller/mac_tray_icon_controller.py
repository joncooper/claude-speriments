# Source Generated with Decompyle++
# File: mac_tray_icon_controller.pyc (Python 3.11)

from collections import OrderedDict
from typing import Callable, Dict, Optional, Text
import objc
from AppKit import NSObject, NSStatusBarButton, NSStatusItem
from dropbox.client.tray.common.tray_icon_state import TrayIconState
from dropbox.client.tray.electron_tray_icon_controller.native_tray_icon_controller import NativeTrayIconController
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.foundation.html_views.cocoa.helpers import get_nsstatusitem_from_bridged_native_handle
from dropbox.foundation.html_views.common.bridge_gen.types import NativeViewHandle
from dropbox.foundation.html_views.electron.ipc.rpc import JSONDict, SignalCallback
from dropbox.gui import event_handler

class TrayVoiceOverActionTarget(NSObject):
    _callback: 'Callable[[], None]' = 'TrayVoiceOverActionTarget'
    
    def initWithCallback_(self = None, callback = None):
        self = objc.super(TrayVoiceOverActionTarget, self).init()
    # WARNING: Decompyle incomplete

    openTrayMenu_ = (lambda self = None, _sender = objc.typedSelector(b'v@:@'): self._callback())()()


class MacTrayIconController(NativeTrayIconController):
    pass
# WARNING: Decompyle incomplete

