# Source Generated with Decompyle++
# File: linux.pyc (Python 3.11)

from __future__ import absolute_import, print_function
import errno
import fcntl
import os
import pwd
import select
import shutil
import subprocess
import sys
import tempfile
from typing import Optional, Text
import build_number
from build_number import BUILD_KEY, BuildVersion
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.cli import start_control_thread, start_tprt_control_endpoint
from dropbox.client.cli.control_thread import ControlThread
from dropbox.client.constants import AppDataPaths
from dropbox.client.constants.linux import UPDATE_ROOT
from dropbox.client.file_permissions.posix import check_and_fix_permissions
from dropbox.client.signal_handler.linux import SignalHandler
from dropbox.client.util import hard_exit
from dropbox.client.util.linux import get_contents_root, kill_other_instances
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, report_rare_event
from dropbox.exception.severity import Severity
from dropbox.foundation.runtime.exit_codes import ExitCode
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.configuration.interface import LocalConfigurationInterface
    from dropbox.client.main import DropboxApplication

def install_early_in_boot(client_session_id = None):
    SignalHandler(client_session_id).register()


def get_rss():
    
    try:
        statfile = open('/proc/self/stat')
        
        try:
            None(None, None)
            return 
            with None:
                if not None, int(statfile.readline().split()[23]) * 4096:
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            return -1






def check_other_version():
    home_install_path_version = os.path.join(UPDATE_ROOT, 'VERSION')
    if os.path.exists(home_install_path_version):
        f = open(home_install_path_version)
        version = f.read().strip()
        None(None, None)
    else:
        with None:
            if not None:
                pass
    TRACE('Current version %s, found version %s in %s', build_number.VERSION, version, UPDATE_ROOT)
    
    try:
        other_version = BuildVersion(version)
    except Exception:
        report_exception(severity = Severity.WARN, component = DesktopComponent.INITIALIZATION)
        TRACE('!! Ignoring invalid version %s in %s', version, UPDATE_ROOT)
        return None

    if other_version > build_number.dropbox_version:
        return UPDATE_ROOT


def limit_to_one_instance(app = None, appdata_path = None):
    pass
# WARNING: Decompyle incomplete


def pre_appdata_use_startup(_appdata_path = None):
    return check_and_fix_permissions(_appdata_path)


def pre_network_startup(app = None):
