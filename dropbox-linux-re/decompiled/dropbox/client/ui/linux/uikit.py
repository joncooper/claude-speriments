# Source Generated with Decompyle++
# File: uikit.pyc (Python 3.11)

import ctypes
import os
import random as insecure_random
import threading
import uuid
from collections import OrderedDict
from ctypes import c_int, c_void_p, CDLL
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
from build_number import BUILD_KEY, is_frozen
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.sharing_modal.constants import ShareModalInitialScreen
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.events import report_show_bubble
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId
from dropbox.client.quit_handlers import QuitHandlerPriorities
from dropbox.client.setup_wizard.setup_wizard_controller import SetupWizardController
from dropbox.client.status.interface import ClientStatusInterface
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.dropbox_menu import MenuComponent, MenuItem
from dropbox.client.ui.common.email_verification_window.email_verification_controller import EmailVerificationController
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayState, TrayTriggerReason
from dropbox.client.ui.common.uikit import ExternalUIKit, FrameworkProps, on_ui_thread, on_ui_thread_blocking, on_ui_thread_future, on_ui_thread_returns_none, report_ui_framework_event, show_remote_share_fallback_with_email_verification
from dropbox.client.ui.linux.gtk_lib_app_indicator_loader import get_gtk_libappindicator_loader
from dropbox.client.ui.linux.preferences import LinuxPreferencesController
from dropbox.client.ui.low_ui.mixin import LowUIMixin
from dropbox.client.ui.native.tray_popup.tray_controller import DQTrayController
from dropbox.client.util import get_contents_root
from dropbox.client.util.linux import bubble_external, highlight_files, move_files
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.runtime import ExitCode
from dropbox.gui import assert_message_queue
from dropbox.i18n import trans
from dropbox.infinite import infinite_download_ui_exposed
from dropbox.infinite.download_ui import InfiniteUIKit
from dropbox.model.types import FileId
from dropbox.native_threading import NativeMutex
from dropbox.sharing.utils.content_util import ContentType, get_content
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIKextInstallFlowSource
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.threadutils import SafeValue
from dropbox.tiburon_log import log_tiburon_event_with_fileid, make_tiburon_log_event_callback
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
    from dropbox.client.ui.common.camera import CameraUI
    from dropbox.client.ui.common.tray_ui_controller import TrayUiControllerBase

class LinuxUIKit(ExternalUIKit, LowUIMixin):
    pass
# WARNING: Decompyle incomplete

