# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

import threading
import time
from collections import OrderedDict
from typing import Any, Callable, Dict, List, Optional, Text, Tuple
import objc
from AppKit import NSApp, NSApplication, NSApplicationDelegateReplySuccess, NSNotification
from ExceptionHandling import NSExceptionHandler, NSLogAndHandleEveryExceptionMask
from Foundation import NSObject, NSString, NSURL
from PyObjCTools import AppHelper
from build_number import dropbox_version, is_frozen
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.file_activation.constants import FileOpenStage
from dropbox.client.file_activation.events import FileOpenInfo
from dropbox.client.gandalf import Gandalf
from dropbox.client.notifications.loud_notifications.bubble_context import BubbleContext
from dropbox.client.notifications.loud_notifications.loud_notification import LoudNotification, LoudNotificationId
from dropbox.client.tray.common.tray_icon_state import TrayIconStatus
from dropbox.client.ui.cocoa.application_delegate import ApplicationDelegateInterface
from dropbox.client.ui.cocoa.cocoa_basekit import CocoaUIBaseKit
from dropbox.client.ui.cocoa.tray_popup.native_tray_controller import EFNativeTrayController
from dropbox.client.ui.cocoa.uikit import PyObjCExceptionDelegate
from dropbox.client.ui.common.camera import CameraUI
from dropbox.client.ui.common.dropbox_menu import MenuComponent
from dropbox.client.ui.common.pathways.folder_opener_controller import FolderOpenerController
from dropbox.client.ui.common.tray_menu_controller import TrayMenuController
from dropbox.client.ui.common.tray_menu_options import TrayOptionID
from dropbox.client.ui.common.uikit import FrameworkProps, on_ui_thread, on_ui_thread_blocking, on_ui_thread_future, on_ui_thread_returns_none, report_ui_framework_event
from dropbox.client.ui.low_ui.common import LowUIBaseKit
from dropbox.components.desktop_components import DesktopComponent
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.native_file_opener.bridge_gen.file_open_origin import FileOpenOrigin
from dropbox.foundation.navigation_service.window_manager_delegate.foreground_process_tracker import ForegroundManagementBehavior
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.runtime import ExitCode
from dropbox.gui import event_handler
from dropbox.mac.shutdown_notification_handler import ShutDownNotificationHandler
from dropbox.mac.version import MAC_VERSION, SIERRA
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIKextInstallFlowSource
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class LowUIKit(LowUIBaseKit):
    pass
# WARNING: Decompyle incomplete

