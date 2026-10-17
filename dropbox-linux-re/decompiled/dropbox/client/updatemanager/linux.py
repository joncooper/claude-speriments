# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

import contextlib
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from time import sleep
from typing import Any, Callable, Dict, Optional, Text
from apex.auto_updater import AutoUpdaterClient as ApexAutoUpdaterClient
from apex.metrics import Metric, MetricsReporter
from six import reraise
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict
from dropbox.client.constants.linux import UPDATE_ROOT
from dropbox.client.flow_tracker import FlowTracker
from dropbox.client.gandalf import Gandalf
from dropbox.client.high_trace import force_flush
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.updatemanager.base import BaseUpdateManager, get_user_engagement_wait_time
from dropbox.client.updatemanager.constants import DESKTOP_RELEASE_AMP_NAMESPACE, PermissionError, RESTART_WAIT_TIME_SECONDS, RestartFailureError, StrOrText
from dropbox.client.util.linux import running_dropbox_instances
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import can_write_file
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.trace import TRACE
FileSystem = Any
VIABILITY_CHECK_TIMEOUT = 30

class UpdateManager(BaseUpdateManager):
    pass
# WARNING: Decompyle incomplete

