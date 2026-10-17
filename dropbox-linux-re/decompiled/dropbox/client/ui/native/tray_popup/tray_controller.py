# Source Generated with Decompyle++
# File: tray_controller.pyc (Python 3.11)

import itertools
import os
import shutil
import subprocess
from collections import OrderedDict
from typing import Optional, Text, Tuple, Union
from build_number import BUILD_KEY, is_electron_application
from dropbox.client.background_worker import on_background_thread
from dropbox.client.benchmarking.startup import STARTUP_EVENT_RENDERED_TRAY
from dropbox.client.rtrace_api import get_rtrace_account
from dropbox.client.status.label import StatusLabel
from dropbox.client.tray.common.tray_icon_state import TrayIconState, TrayIconStatus
from dropbox.client.tray.events import TrayEventReporter
from dropbox.client.tray.tray_controller import ElectronTrayController
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayPopupStrings, TrayTriggerReason
from dropbox.client.ui.common.tray_ui_controller import TrayUiControllerBase
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread, report_ui_framework_event
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.gui import assert_message_queue
from dropbox.i18n import trans
from dropbox.platform import IS_LINUX, IS_WINDOWS
from dropbox.stopwatch import global_sw
from dropbox.trace import TRACE
if IS_LINUX:
    from dropbox.client.ui.linux.app_indicator_dbus_next import AppIndicatorDbusNextTrayIcon, maybe_show_desktop_environment_warning, maybe_show_missing_libappindicator_warning, should_load_app_indicator_tray_icon_dbus_next
    from dropbox.client.util.linux import change_state_external, refresh_tray_menu_external
    from dropbox.system_info import get_linux_system_info
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    TrayIcon = Union[AppIndicatorDbusNextTrayIcon]

class BadAppIndicatorDetection(Exception):
    pass


class DQTrayController(TrayUiControllerBase):
    pass
# WARNING: Decompyle incomplete

