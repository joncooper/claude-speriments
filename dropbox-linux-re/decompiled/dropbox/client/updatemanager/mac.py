# Source Generated with Decompyle++
# File: mac.pyc (Python 3.11)

import contextlib
import os
import shutil
import signal
import subprocess
import sys
import tarfile
import tempfile
import time
from time import sleep
from typing import Any, Callable, List, Optional, Text
from apex.auto_updater import AutoUpdaterClient as ApexAutoUpdaterClient, UpdatePriority
from apex.metrics import MetricsReporter
from AppKit import NSURL, NSWorkspace, NSWorkspaceLaunchConfigurationArguments, NSWorkspaceLaunchDefault
from six import reraise
from build_number import BUILD_KEY, dropbox_version, is_frozen
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.config import ConfigDict
from dropbox.client.constants.mac import get_alt_install_path, get_alt_install_path_base
from dropbox.client.flow_tracker import FlowTracker
from dropbox.client.gandalf import Gandalf
from dropbox.client.high_trace import force_flush
from dropbox.client.status.interface import StatusControllerInterface
from dropbox.client.updatemanager.base import BaseUpdateManager, DROPBOX_GUID, get_user_engagement_wait_time
from dropbox.client.updatemanager.constants import PermissionError, RESTART_WAIT_TIME_SECONDS, RestartFailureError
from dropbox.client.updatemanager.util import get_update_client_path, is_omaha4_supported, report_updater_install, UpdaterInstallType
from dropbox.client.util.mac import get_app_path, get_contents_root, get_helpers_dir, get_resources_dir, get_update_manager_id
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.event_names import AUTO_UPDATE_RESTART_EVENT
from dropbox.exception.exceptions import BadAssumptionError
from dropbox.exception.reporting import report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.fileutils import can_write_file
from dropbox.foundation.environment import is_integration_tests
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.mac.internal import find_instances
from dropbox.mac.version import MAC_VERSION, VENTURA
from dropbox.sync_engine_adapter.adapter import SyncEngineAdapter
from dropbox.trace import TRACE
FileSystem = Any
ALT_INSTALL_BLOCK_USER_PATH = os.path.expanduser('~/Library/Application Support/Dropbox/disable_dual_install.dbx')
ALT_INSTALL_BLOCK_SYSTEM_PATH = '/Library/Application Support/Dropbox/disable_dual_install.dbx'
SYSTEM_UPDATER_UID_PATH = '/Library/Application Support/Dropbox/DropboxUpdater/uid'

class UpdateManagerFailure(Exception):
    pass


class UpdateManagerCrash(Exception):
    pass


def check_call_with_exception_handling(args = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def num_update_manager_processes():
    
    try:
        instances = list(find_instances(UpdateManager.UPDATE_MANAGER_BINARY_REL_PATH, unhandled_exc_handler = report_exception))
        if len(instances) > 5:
            for pid in instances:
                TRACE('Killing %s', pid)
                os.kill(pid, signal.SIGKILL)
                
                try:
                    continue
                    except Exception:
                        report_exception(severity = Severity.WARN, component = DesktopComponent.AUTO_UPDATE)
                        
                        try:
                            continue
                            
                            try:
                                return len(instances)
                            except Exception:
                                report_exception(severity = Severity.WARN, component = DesktopComponent.AUTO_UPDATE)
                                return 0






class UpdateManager(BaseUpdateManager):
    pass
# WARNING: Decompyle incomplete

