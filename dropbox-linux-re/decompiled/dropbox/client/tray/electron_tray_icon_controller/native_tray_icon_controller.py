# Source Generated with Decompyle++
# File: native_tray_icon_controller.pyc (Python 3.11)

import secrets
from abc import abstractmethod
from collections import OrderedDict
from itertools import chain
from typing import Callable, Dict, Iterable, Text
from build_number import BUILD_KEY
from dropbox.client.benchmarking.startup import ClientStartupBenchmarker, STARTUP_EVENT_RENDERED_TRAY
from dropbox.client.fenix.journeys.tray.tray_status_service import TrayStatusService
from dropbox.client.persist import set_gpu_disabled
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.tray.common.tray_icon_state import TrayIconState, TrayIconStatus
from dropbox.client.tray.tray_runtime_controller import TrayRuntimeController
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem, Separator
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayPopupStrings, TrayTriggerReason
from dropbox.client.ui.common.uikit import on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report_aggregate_event
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.html_views.electron.electron_context_menus import ElectronContextMenu
from dropbox.foundation.html_views.electron.host_driver import ElectronHostDriver
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc, JSONDict, SignalCallback
from dropbox.foundation.raii2.quick import Destroyable
from dropbox.foundation.runtime.exit_codes import ExitCode

class NativeTrayIconController(Destroyable):
    pass
# WARNING: Decompyle incomplete

