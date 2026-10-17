# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import os
import sys
import time
from collections import OrderedDict
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.link_thread import on_link_thread
from dropbox.client.configuration.local_configuration import LocalConfiguration
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.main import DropboxApplication
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.setup_wizard.account_link_state import LinkPreferences
from dropbox.client.status.interface import ClientStatusInterface
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.ui.common.camera import CameraUI
from dropbox.client.ui.common.dialog_constants import DialogSourceTypes, IconType
from dropbox.client.ui.common.dialogs import DummyDialogController
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayState, TrayTriggerReason
from dropbox.client.ui.common.uikit import Closeable, FrameworkProps, on_ui_thread, on_ui_thread_blocking, on_ui_thread_future, on_ui_thread_returns_none, SimpleUIKit
from dropbox.client.util import safe_print
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.i18n import trans
from dropbox.infinite import infinite_download_ui_exposed
from dropbox.infinite.download_ui import HeadlessInfiniteUI
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIKextInstallFlowSource
from dropbox.trace import TRACE
if IS_LINUX:
    from dropbox.client.util.linux import bubble_external, change_state_external, copy_text_to_clipboard_external, highlight_files, move_files, refresh_tray_menu_external
if IS_WINDOWS:
    from dropbox.client.util.win import copy_text_to_clipboard_external, highlight_files, move_files
if IS_MAC:
    from dropbox.client.util.mac import copy_text_to_clipboard_external
MYPY = False
if MYPY:
    from dropbox.client.multiaccount.selector import MultiAccountSelector

class HeadlessUIKit(SimpleUIKit):
    pass
# WARNING: Decompyle incomplete

