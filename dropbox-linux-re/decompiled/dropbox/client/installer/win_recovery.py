# Source Generated with Decompyle++
# File: win_recovery.pyc (Python 3.11)

import os
import subprocess
from build_number.features import feature_enabled
from dropbox.client.constants.win import DROPBOX_OMAHA_GUID
from dropbox.trace import TRACE
from dropbox.win32.version import WIN10, WINDOWS_VERSION

def install_elevation_service(contents_root = None):
    if WINDOWS_VERSION.version_number() < WIN10.version_number():
        return None
    if not feature_enabled('omaha4-recovery'):
        return None
    out = _run_command(contents_root, '--install-elevation-service')
    TRACE('Elevation service successfully installed: %s', out)


def uninstall_elevation_service(contents_root = None):
    if WINDOWS_VERSION.version_number() < WIN10.version_number():
        return None
    if not feature_enabled('omaha4-recovery'):
        return None
    out = _run_command(contents_root, '--uninstall-elevation-service')
    TRACE('Elevation service successfully uninstalled: %s', out)


def _run_command(contents_root = None, command = None):
    update_client_exe = os.path.join(contents_root, 'DropboxUpdateClient.exe')
    args = [
        update_client_exe,
        command,
        f'''--appid={DROPBOX_OMAHA_GUID}''',
        '--enable-logging',
        '--vmodule=*/dropbox/update_client/*=2']
    return subprocess.check_output(args, stderr = subprocess.STDOUT, timeout = 15)

