# Source Generated with Decompyle++
# File: tray_controller.pyc (Python 3.11)

from collections import OrderedDict
from typing import Optional, Text, Tuple
from Foundation import NSUserDefaults
from dropbox.client.features.desktop_logging.desktop_logger import DesktopLogger
from dropbox.client.features.desktop_logging.event_enums import EventClass
from dropbox.client.features.desktop_logging.logging_event import NonUserLoggingEvent
from dropbox.client.tray.common.tray_icon_state import TrayIconState, TrayIconStatus
from dropbox.client.tray.events import TrayEventReporter
from dropbox.client.tray.tray_controller import ElectronTrayController
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayTriggerReason
from dropbox.client.ui.common.tray_ui_controller import TrayUiControllerBase
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
TRAY_ICON_PREFERRED_POSITION_KEY = 'NSStatusItem Preferred Position Item-0'

class ElectronMacTrayController(TrayUiControllerBase):
    pass
# WARNING: Decompyle incomplete

