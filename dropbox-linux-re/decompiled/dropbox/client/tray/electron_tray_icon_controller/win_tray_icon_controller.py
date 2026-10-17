# Source Generated with Decompyle++
# File: win_tray_icon_controller.pyc (Python 3.11)

from __future__ import absolute_import, division
from typing import Dict, OrderedDict, Text
from apex.metrics import MetricsReporter
from pynt.helpers.general import FormattedWindowsError
from dropbox.client.tray.common.tray_icon_state import TrayIconState
from dropbox.client.tray.common.win_tray_utils import Win32TrayIconHelper
from dropbox.client.tray.electron_tray_icon_controller.native_tray_icon_controller import NativeTrayIconController
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc, SignalCallback
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.reporting import report_app_framework_event

class WinTrayIconController(NativeTrayIconController):
    pass
# WARNING: Decompyle incomplete


class WinTrayIconGuidController(Destroyable):
    pass
# WARNING: Decompyle incomplete

