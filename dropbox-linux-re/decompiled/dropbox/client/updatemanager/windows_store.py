# Source Generated with Decompyle++
# File: windows_store.pyc (Python 3.11)

import time
from typing import Callable, Optional, Text
import win32gui
import win32process
from apex.auto_updater import AutoUpdaterClient as ApexAutoUpdaterClient
from apex.metrics import MetricsReporter
from build_number import BUILD_CHANNEL, VERSION
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.config import ConfigDict
from dropbox.client.gandalf import Gandalf
from dropbox.client.high_trace import force_flush
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.ui.common.uikit import ensure_on_ui_thread
from dropbox.client.updatemanager.base import BaseUpdateManager
from dropbox.client.updatemanager.constants import RESTART_WAIT_TIME_SECONDS, RestartFailureError
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.platform_version import PLATFORM_VERSION
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.fsutil import FileSystem
from dropbox.platform import platform
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.trace import TRACE
from dropbox.win32.version import WIN10, WINDOWS_VERSION
from dropbox.win32.win_client_info import get_process_creation_time
if WINDOWS_VERSION.version_number() >= WIN10.version_number():
    import _bowbow
# WARNING: Decompyle incomplete
