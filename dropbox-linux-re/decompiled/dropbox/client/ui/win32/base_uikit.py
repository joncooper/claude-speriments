# Source Generated with Decompyle++
# File: base_uikit.pyc (Python 3.11)

import random as insecure_random
import sys
from typing import Any, Callable, Dict, List, Optional, Tuple
import pywintypes
import win32con
import win32gui
from apex.metrics import Metric
from pynt.dlls.user32 import user32
from winerror import ERROR_NOT_ENOUGH_QUOTA
from build_number import BUILD_KEY
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.apollo_pathway_origins.bridge_gen.apollo_pathway_origin import ApolloPathwayOrigin
from dropbox.client.setup_wizard.setup_wizard_controller import SetupWizardController
from dropbox.client.ui.common.dialogs import DialogController
from dropbox.client.ui.common.email_verification_window.email_verification_controller import EmailVerificationController
from dropbox.client.ui.common.uikit import ExternalUIKit, FrameworkProps, on_ui_thread_blocking, on_ui_thread_future, on_ui_thread_returns_none
from dropbox.client.util import hard_exit
from dropbox.client.util.win import copy_text_to_clipboard_external, get_text_from_clipboard_external, highlight_files, move_files
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions_ex_5
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.infinite import infinite_download_ui_exposed
from dropbox.infinite.download_ui import InfiniteUIKit
from dropbox.metrics.camera_upload import CameraEvent
from dropbox.native_threading import NativeMutex
from dropbox.sync_engine_boundary.infinite.ui_types import InfiniteUIKextInstallFlowSource
from dropbox.threadutils import SafeValue
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication

class BaseWinUIKit(ExternalUIKit):
    pass
# WARNING: Decompyle incomplete

