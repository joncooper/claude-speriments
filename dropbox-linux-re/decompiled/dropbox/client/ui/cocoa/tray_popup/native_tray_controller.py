# Source Generated with Decompyle++
# File: native_tray_controller.pyc (Python 3.11)

from __future__ import absolute_import
from collections import OrderedDict
from typing import Optional, Text, Tuple
import objc
from AppKit import NSDistributedNotificationCenter, NSEvent, NSImage, NSImageView, NSMenu, NSObject, NSStatusBar, NSStatusBarButton, NSStatusItem, NSVariableStatusItemLength
from build_number import BUILD_KEY
from dropbox.client.gandalf import Gandalf
from dropbox.client.quit_handlers import QuitHandlerPriorities
from dropbox.client.status.label import StatusLabel
from dropbox.client.tray.common.tray_icon_state import TrayIconState, TrayIconStatus
from dropbox.client.tray.events import TrayEventReporter, TrayMenuReason
from dropbox.client.tray.logging.pap_logging_helpers import log_view_desktop_surface_tray_assistant_low_ui
from dropbox.client.ui.cocoa.menu import EFMenu
from dropbox.client.ui.cocoa.util import TrayIcon
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayPopupStrings, TrayTriggerReason
from dropbox.client.ui.common.tray_popup_utils import report_tray_oq_view_events
from dropbox.client.ui.common.tray_ui_controller import TrayUiControllerBase
from dropbox.client.ui.common.uikit import ensure_on_ui_thread, on_ui_thread
from dropbox.client.ui.common.utils import is_low_ui_mode
from dropbox.event import report_aggregate_event
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.gui import assert_message_queue, event_handler
from dropbox.mac.typed_objc import typed_python_method
from dropbox.mac.version import BIG_SUR, MAC_VERSION
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

def NSStatusBarButton():
    '''NSStatusBarButton'''
    mouseDown_ = (lambda self = None, event = objc.typedSelector(b'v@:@'): target = self.target()if not isinstance(target, EFNativeTrayController):
objc.super(NSStatusBarButton, self).mouseDown_(event)None.hide_tray_popup()self.cell().performClick_(None))()()
    rightMouseDown_ = (lambda self = None, event = objc.typedSelector(b'v@:@'): target = self.target()if not isinstance(target, EFNativeTrayController):
objc.super(NSStatusBarButton, self).rightMouseDown_(event)None.statusBarButtonClicked_(self))()()

NSStatusBarButton = <NODE:27>(NSStatusBarButton, 'NSStatusBarButton', objc.Category(NSStatusBarButton))

class EFNativeTrayController(TrayUiControllerBase, NSObject):
    STATUS_ITEM_TO_POPOVER_GAP = 5
    
    def initWithApp_(self = None, app = None):
        pass
    # WARNING: Decompyle incomplete

    tray_icon_state = (lambda self = None: self._tray_icon_state)()
    is_tray_pinned = (lambda self = None: self._pinned)()
    _configure_tray = (lambda self = None: pass)()()
    _refresh_status_item_button = (lambda self = None: pass# WARNING: Decompyle incomplete
)()()
    _update_status_item_menu_descriptor = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    update_options = (lambda self = None, options = None: self._status_item_options = options# WARNING: Decompyle incomplete
)()
    update_tray_icon = (lambda self = None, *, icon_state: self._tray_icon_state = TrayIconState(status = icon_state, tooltip = tooltip, badge_count = badge_count, snoozed = snoozed, label = StatusLabel.LABEL_BLANK.value)# WARNING: Decompyle incomplete
)()
    darkModeChanged_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): state = self._tray_icon_stateself.update_tray_icon(icon_state = state.status, badge_count = state.badge_count, tooltip = state.tooltip, snoozed = state.snoozed))()()
    load_status_item = (lambda self = None: pass# WARNING: Decompyle incomplete
)()()
    statusBarButtonClicked_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): report_aggregate_event('tray-icon-click', {
'left_click': 1 }, approx_timeout = 1800)self.on_tray_icon_click(TrayTriggerReason.TRAY_ICON_CLICK))()()
    menuWillOpen_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): TrayEventReporter.new_session()self._update_status_item_menu_descriptor()self._status_item_menu_open = Truereason = TrayMenuReason.USER_INITIATEDTrayEventReporter.menu_shown(reason)TrayEventReporter.os_menu_did_show()if is_low_ui_mode():
active_account = Noneif self._app.tray_menu_controller:
active_account = self._app.tray_menu_controller._active_account_tracker_arc().active_accountlog_view_desktop_surface_tray_assistant_low_ui(account = active_account, session_id = self._app.client_session_id, tray_trigger_reason = TrayTriggerReason.TRAY_ICON_CLICK)# WARNING: Decompyle incomplete
)()()
    menuDidClose_ = (lambda self = None, sender = objc.typedSelector(b'v@:@'): TrayEventReporter.os_menu_did_hide()self._status_item_menu_open = False)()()

