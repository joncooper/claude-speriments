# Source Generated with Decompyle++
# File: uikit.pyc (Python 3.11)

import random as insecure_random
import threading
import time
import traceback
import uuid
from collections import OrderedDict
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
import objc
from AppKit import NSApp, NSApplication, NSApplicationDelegateReplySuccess, NSMenu, NSNotification
from ExceptionHandling import NSExceptionHandler, NSLogAndHandleEveryExceptionMask
from Foundation import NSException, NSObject, NSString, NSURL
from PyObjCTools import AppHelper
from build_number import dropbox_version, is_electron_application, is_frozen
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.features.sharing_modal.constants import ShareModalInitialScreen
from dropbox.client.fenix.constants import UserJourneyNames
from dropbox.client.fenix.utils import convert_to_local_account
from dropbox.client.file_activation.constants import FileOpenStage
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId
from dropbox.client.setup_wizard.setup_wizard_controller import SetupWizardController
from dropbox.client.status.interface import ClientStatusInterface
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.tray.logging.pap_logging_helpers import log_finder_view_from_dock_icon
from dropbox.client.ui.cocoa.application_delegate import ApplicationDelegateInterface
from dropbox.client.ui.cocoa.bug_report import BugReportWindow
from dropbox.client.ui.cocoa.camera import CocoaCameraUI
from dropbox.client.ui.cocoa.cert_pinning import register_protocol
from dropbox.client.ui.cocoa.cocoa_basekit import CocoaUIBaseKit
from dropbox.client.ui.cocoa.dialogs import show_office_addin_prompt
from dropbox.client.ui.cocoa.dropbox_controls import DropboxDefaultMenuDelegate
from dropbox.client.ui.cocoa.tray_popup.tray_controller import ElectronMacTrayController
from dropbox.client.ui.common.common_ui_kit import CommonUIKit
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.email_verification_window.email_verification_controller import EmailVerificationController
from dropbox.client.ui.common.office import OfficeAddInStrings
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.tray_popup_constants import TrayState, TrayTriggerReason
from dropbox.client.ui.common.tray_ui_controller import TrayUiControllerBase
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread, on_ui_thread_blocking, on_ui_thread_future, on_ui_thread_returns_none, report_ui_framework_event, show_remote_share_fallback_with_email_verification
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context import Context
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.navigation_service.window_manager_delegate.foreground_process_tracker import ForegroundManagementBehavior
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.runtime import ExitCode
from dropbox.gui import event_handler
from dropbox.infinite import infinite_download_ui_exposed
from dropbox.infinite.download_ui import InfiniteUIKit
from dropbox.mac.shutdown_notification_handler import ShutDownNotificationHandler
from dropbox.mac.version import MAC_VERSION, SIERRA
from dropbox.metrics.camera_upload import CameraEvent
from dropbox.model.types import FileId
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIKextInstallFlowSource
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.location_props import LocationProperties
from dropbox.threadutils import SafeValue
from dropbox.tiburon_log import make_tiburon_log_event_callback
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class PyObjCExceptionDelegate(NSObject):
    isPythonException = (lambda exception = None: 