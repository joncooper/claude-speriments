# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

import random as insecure_random
from typing import Any, Callable, Dict, List, Optional, Text, TypeVar
from build_number import BUILD_KEY
from build_number.platform import IS_MAC
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.main import DropboxApplication
from dropbox.client.multiaccount.selector import MultiAccountSelector
from dropbox.client.setup_wizard.setup_wizard_controller import SetupWizardController
from dropbox.client.status.interface import ClientStatusInterface
from dropbox.client.ui.common.dialog_constants import DialogEventTypes, DialogFrameworkTypes, DialogSourceTypes, IconType
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.dropbox_menu import MenuItem
from dropbox.client.ui.common.email_verification_window.email_verification_controller import EmailVerificationController
from dropbox.client.ui.common.screenshots import ScreenshotsStrings
from dropbox.client.ui.common.tray_menu_options import TrayOption
from dropbox.client.ui.common.tray_popup_constants import TrayPopupStrings, TrayState, TrayTriggerReason
from dropbox.client.ui.common.uikit import Closeable, ExternalUIKit, on_ui_thread_future, on_ui_thread_returns_none
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context import Context
from dropbox.foundation.futures import Future
from dropbox.foundation.html_views.electron.electron_dialog_constants import ElectronDialogCallbackInfo
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.runtime import ExitCode
from dropbox.infinite import infinite_download_ui_exposed
from dropbox.infinite.download_ui import InfiniteUIKit
from dropbox.metrics.camera_upload import CameraEvent
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
_T = TypeVar('_T')

class LowUIBaseKit(ExternalUIKit):
    pass
# WARNING: Decompyle incomplete

