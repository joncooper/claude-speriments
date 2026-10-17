# Source Generated with Decompyle++
# File: uikit.pyc (Python 3.11)

import random as insecure_random
import uuid
from collections import OrderedDict
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.features.sharing_modal.constants import ShareModalInitialScreen
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId
from dropbox.client.status.interface import ClientStatusInterface
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.ui.common.common_ui_kit import CommonUIKit
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.email_verification_window.email_verification_controller import EmailVerificationController
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayState, TrayTriggerReason
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread, on_ui_thread_blocking, on_ui_thread_future, on_ui_thread_returns_none, report_ui_framework_event, show_remote_share_fallback_with_email_verification
from dropbox.client.ui.native.tray_popup.tray_controller import DQTrayController
from dropbox.client.ui.win32.base_uikit import BaseWinUIKit
from dropbox.client.ui.win32.camera import WinCameraUI
from dropbox.client.ui.win32.tray_icon import Win32TrayIcon
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.runtime import ExitCode
from dropbox.gui import assert_message_queue
from dropbox.model.types import FileId
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.tiburon_log import log_tiburon_event_with_fileid, make_tiburon_log_event_callback
from dropbox.trace import TRACE
from dropbox.win32.version import WIN10, WINDOWS_VERSION
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.ui.common.tray_ui_controller import TrayUiControllerBase

class RichWinUIKit(CommonUIKit, BaseWinUIKit):
    pass
# WARNING: Decompyle incomplete

