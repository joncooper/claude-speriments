# Source Generated with Decompyle++
# File: windows.pyc (Python 3.11)

import ctypes
import os
import subprocess
import time
from typing import Any, Callable, Optional, Text
import psutil
import win32api
import win32con
from apex.auto_updater import AutoUpdaterClient as ApexAutoUpdaterClient
from apex.metrics import Metric, MetricsReporter
from apex.util import process_architecture
from comtypes import CLSCTX_LOCAL_SERVER, COMError
from comtypes.client import CreateObject
from six.moves.urllib.parse import quote, urlencode
from build_number import dropbox_version
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict
from dropbox.client.gandalf import Gandalf
from dropbox.client.high_trace import force_flush
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.updatemanager.base import BaseUpdateManager, DROPBOX_GUID
from dropbox.client.updatemanager.constants import DESKTOP_RELEASE_AMP_NAMESPACE, RESTART_WAIT_TIME_SECONDS, RestartFailureError
from dropbox.client.updatemanager.util import get_update_client_path, is_omaha4_supported
from dropbox.client.util.win import get_contents_root, get_dropbox_update_path, get_update_manager_id
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exceptions import BadAssumptionError
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.install_type import get_dropbox_install_type, InstallType
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.trace import TRACE
from dropbox.win32.com_helper import initialized_com
FileSystem = Any
COM_SERVER_PREFIX = 'DropboxUpdate.Update3Web'

class UpdateManager(BaseUpdateManager):
    pass
# WARNING: Decompyle incomplete

