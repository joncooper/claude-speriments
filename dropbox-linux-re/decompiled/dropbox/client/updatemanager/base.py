# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

import fnmatch
import functools
import os
import ssl
import time
from abc import abstractmethod
from typing import Any, Callable, Dict, Optional, Text
from apex.auto_updater import AutoUpdaterClient as ApexAutoUpdaterClient
from apex.metrics import Metric, MetricsReporter
from six.moves.urllib.request import urlopen
import build_number
from build_number.versions import BuildVersion, get_platform
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict
from dropbox.client.gandalf import Gandalf
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.status.label import StatusLabel
from dropbox.client.updatemanager.constants import DESKTOP_RELEASE_AMP_NAMESPACE, IN_APP_UPDATE_CONFIG_KEY, PermissionError, StrOrText
from dropbox.client.updatemanager.interface import UpdateManagerInterface
from dropbox.client.updatemanager.util import is_omaha4_supported
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.hashing import DROPBOX_MAX_BLOCK_SIZE, DropboxHasher, split_blocklist
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.gui import spawn_thread_with_name
from dropbox.shared.local_path import LocalPath
from dropbox.ssl.context import get_dropbox_ssl_context
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.threading import Lock
from dropbox.trace import TRACE
FileSystem = Any
IMPORTING_DELAY_TIME = 86400
DEFAULT_AUTO_UPDATE_RETRY_INTERVAL = 1800
BLOCK_SIZE = 4194304
DROPBOX_GUID = '{CC46080E-4C33-4981-859A-BBA2F780F31E}'

def get_user_engagement_wait_time():
    return 86400


class FailedDownloadError(Exception):
    pass


class BaseUpdateManager(UpdateManagerInterface):
    pass
# WARNING: Decompyle incomplete

