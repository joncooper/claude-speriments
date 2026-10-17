# Source Generated with Decompyle++
# File: tray_popup_constants.pyc (Python 3.11)

from enum import IntEnum
from typing import Optional
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.components.desktop_components import DesktopComponent
from dropbox.enum_utils import auto, AutoNameEnum, AutoNameJsonEnum, StrAsPrefixlessValueTrait
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
CONFIG_KEY_TRAY_LAST_OPENED_TS = 'tray_last_opened_ts'

class TrayPopupViewType(AutoNameEnum):
    UNKNOWN = auto()
    LOADING = auto()
    CONTENT = auto()
    SIGNIN = auto()
    QUITTING = auto()
    ERROR = auto()


class TrayState(IntEnum):
    INITIALIZING = 0
    LINKING = 1
    ACTIVE = 2
    SEARCH = 3


class TrayPopupStrings(UIStrings):
    quit_dropbox = UI('Quit %s', windows = UI('Exit %s'))
    disable_gpu = UI('Hardware Acceleration (GPU)')
    tray_content_error = UI("Couldn't Load Content")
    open_in_menu_bar = UI('Open Dropbox in Menu Bar', windows = UI('Open Dropbox in system tray'))


class TrayContentStrings(UIStrings):
    dropbox_is_quitting = UI('Dropbox is closing...')


class TrayPerformanceMetrics:
    TRAY_CONTENT_LOAD = 'tray_content_load_time'
    TRAY_CONTENT_INITIAL_LOAD = 'tray_content_initial_load_time'
    TRAY_ICON_CLICK = 'tray_icon_click'
    TRAY_RUN_ICON_CLICK = 'tray_run_icon_click'
    TRAY_CONTEXT_MENU_UPDATE = 'tray_context_menu_update'
    TRAY_RECENTS_LOCAL_CHANGE = 'tray_recents_local_change'
    TRAY_MARK_STICKY = 'tray_mark_sticky'


class TrayTriggerReason(AutoNameJsonEnum, StrAsPrefixlessValueTrait):
    TRAY_ICON_CLICK = auto()
    TRAY_RUN_ICON_CLICK = auto()
    TRAY_MENU = auto()
    NOTIFICATIONS = auto()
    LEGACY_UI_LAUNCHER = auto()
    LEGACY_VIEW_MANAGER = auto()
    LEGACY_NOTIFICATIONS = auto()
    LEGACY_POPUP_ALT_MENU = auto()
    TRAY_DEBUG = auto()
    DROPBOX_LAUNCHER_CLICK = auto()
    SETUP_WIZARD = auto()
    MEV_TRAY_NOTIFICATIONS = auto()
    parse_or_default = (lambda reason = None, default = None: 