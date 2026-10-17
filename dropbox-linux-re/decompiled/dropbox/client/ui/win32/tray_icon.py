# Source Generated with Decompyle++
# File: tray_icon.pyc (Python 3.11)

from __future__ import absolute_import, division
import ctypes
import time as _time
from ctypes.wintypes import RECT
from itertools import count
from typing import Any, Callable, Dict, MutableMapping, NewType, Optional, OrderedDict, Text, Tuple
import commctrl
import win32api
import win32con
import win32gui
import winerror
from apex.metrics import Metric
from comtypes.GUID import GUID
from pynt.constants import NIIF_USER, NOTIFYICON_VERSION
from pynt.dlls.shell32 import shell32
from pynt.dlls.user32 import user32
from pynt.helpers.general import win_error_check, windows_error
from pynt.types import MENUITEMINFO, NOTIFYICONDATA, NOTIFYICONIDENTIFIER
from six import itervalues
from build_number import BUILD_KEY
from build_number.features import feature_enabled
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.notifications.loud_notifications.events import BubbleClickInfo, report_show_bubble
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification
from dropbox.client.notifications.loud_notifications.types import BubbleContextRef
from dropbox.client.status.label import StatusLabel
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.tray.common.win_tray_utils import Win32TrayIconHelper
from dropbox.client.tray.events import TrayEventReporter, TrayMenuReason
from dropbox.client.tray.logging.pap_logging_helpers import log_view_desktop_surface_tray_assistant_low_ui
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem, MenuRadioItems, Separator, SubMenu
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.client.ui.common.tray_popup_utils import report_tray_oq_view_events
from dropbox.client.ui.common.uikit import on_ui_thread, on_ui_thread_returns_none
from dropbox.client.ui.win32.theme import get_os_theme, WindowsOSTheme
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report_aggregate_event
from dropbox.exception.exception_decorators import handle_exceptions_ex_5
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import snippet
from dropbox.gui import assert_message_queue
from dropbox.trace import TRACE
from dropbox.win32._icon_constants import IDI_DROPBOX_TRAY_ATTENTION, IDI_DROPBOX_TRAY_ATTENTION_WIN10_DARK, IDI_DROPBOX_TRAY_ATTENTION_WIN10_LIGHT, IDI_DROPBOX_TRAY_BUSY, IDI_DROPBOX_TRAY_BUSY_WIN10_DARK, IDI_DROPBOX_TRAY_BUSY_WIN10_LIGHT, IDI_DROPBOX_TRAY_CAM, IDI_DROPBOX_TRAY_CAM_WIN10_DARK, IDI_DROPBOX_TRAY_CAM_WIN10_LIGHT, IDI_DROPBOX_TRAY_CONNECTING, IDI_DROPBOX_TRAY_CONNECTING_WIN10_DARK, IDI_DROPBOX_TRAY_CONNECTING_WIN10_LIGHT, IDI_DROPBOX_TRAY_ERROR, IDI_DROPBOX_TRAY_ERROR_WIN10_DARK, IDI_DROPBOX_TRAY_ERROR_WIN10_LIGHT, IDI_DROPBOX_TRAY_IDLE, IDI_DROPBOX_TRAY_IDLE_WIN10_DARK, IDI_DROPBOX_TRAY_IDLE_WIN10_LIGHT, IDI_DROPBOX_TRAY_PAUSED, IDI_DROPBOX_TRAY_PAUSED_WIN10_DARK, IDI_DROPBOX_TRAY_PAUSED_WIN10_LIGHT, IDI_DROPBOX_TRAY_SNOOZE, IDI_DROPBOX_TRAY_SNOOZE_WIN10_DARK, IDI_DROPBOX_TRAY_SNOOZE_WIN10_LIGHT
from dropbox.win32.version import WIN10, WINDOWS_VERSION
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
NIN_BALLOONUSERCLICK = 1029
TB_GETBUTTON = 1047
TB_GETITEMRECT = 1053
HIcon = NewType('HIcon', int)

def _destroy_icon(hicon = None):
    native_hicon = _to_native_hicon(hicon)
    TRACE('win32gui._destroy_icon(%r=%r)', hicon, native_hicon)
    
    try:
        win32gui.DestroyIcon(native_hicon)
        return None
    except Exception:
        e = None
        report_bad_assumption('Unable to destroy tray icon handle: %r=%r e=%r', hicon, native_hicon, e)
        e = None
        del e
        return None
        e = None
        del e



def _to_native_hicon(hicon = None):
    return int(hicon)


class Win32TrayIcon:
    __module__ = __name__
    __qualname__ = 'Win32TrayIcon'
    WM_D_NOTIFY = win32con.WM_USER + 20
    CLASS_NAME = BUILD_KEY + 'TrayIcon'
    BUBBLE_TIMEOUT = 10000
    FIRST_ID = 1023
# WARNING: Decompyle incomplete

