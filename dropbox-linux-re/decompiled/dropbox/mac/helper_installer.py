# Source Generated with Decompyle++
# File: helper_installer.pyc (Python 3.11)

from __future__ import absolute_import
import errno
import grp
import hashlib
import os
import platform
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
from os import stat_result
from subprocess import PIPE, Popen
from typing import Any, Dict, List, Optional, Text
from apex.metrics import Metric, MetricsReporter
from macffi.CoreFoundation import CFError
from macffi.Security import errAuthorizationCanceled, request_authorization_from_user_and_run
from six import iteritems
import build_number
from build_number.helper_tools import get_keys_for_helper, MissingSignature, SignedFile
from internal import find_instances, groupname_to_gid, raise_application, username_to_uid
from dropbox.client.updatemanager.constants import DESKTOP_RELEASE_AMP_NAMESPACE, PromoteFromHelperResult
from dropbox.client.util.mac import get_resources_dir
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import retry, RetryException
from dropbox.i18n import trans
from dropbox.trace import TRACE
MYPY = False
BUILD_KEY = build_number.BUILD_KEY
BASE_HELPERS_DIR = '/Library/DropboxHelperTools'
if MYPY and sys.platform.startswith('win'):
    REL_HELPERS_DIR = ''
else:
    REL_HELPERS_DIR = '%s_u%d' % (BUILD_KEY, os.getuid())
HELPERS_DIR = os.path.join(BASE_HELPERS_DIR, REL_HELPERS_DIR)
HELPER_INSTALLER_PATH = '/Library/DropboxHelperTools/DropboxHelperInstaller'

class InstallError(Exception):
    pass


def verify_and_extract_installer(fn = None, path = None):
    f_obj = SignedFile(fn, 'rb')
    t_obj = tarfile.open(fileobj = f_obj, mode = 'r|*')
    t_obj.extractall(path = path)
    f_obj.verify(get_keys_for_helper(fn))
    None(None, None)
    return None
    with None:
        if not None:
            pass


def _report_helper_install_event(event = None, metrics_reporter = None, helper_installer_hash = None):
    pass
# WARNING: Decompyle incomplete


def _report_helper_update_event(event = None, metrics_reporter = None, helper_installer_hash = None):
    pass
# WARNING: Decompyle incomplete


def _get_helper_tgz_hash(metrics_reporter = None):
    tgz_full = _get_helper_path('DropboxHelperInstaller')
    
    try:
        f = open(tgz_full, 'rb')
        
        try:
            None(None, None)
            return 
            with None:
                if not None, hashlib.sha1(f.read()).hexdigest():
                    
                    try:
                        
                        try:
                            return None
                        except Exception:
                            _report_helper_install_event('installer_not_found', metrics_reporter, None)
                            return None






class HelperInstallerError(Exception):
    pass


def install_dropbox_helper_installer(metrics_reporter = None, auth_text = None, keep_focus = None):
    tmpdir = tempfile.mkdtemp()
    helper_tgz_hash = _get_helper_tgz_hash(metrics_reporter)
# WARNING: Decompyle incomplete


def check_perm(st = None, uid = None, gid = None, mode = ('st', 'stat_result', 'uid', 'int', 'gid', 'Optional[List[int]]', 'mode', 'int', 'return', 'bool')):
    if st.st_uid == uid:
        if gid is None or st.st_gid in gid:
            pass
    return stat.S_IMODE(st.st_mode) == mode


def check_helper_installer():
    
    try:
        st = os.stat(BASE_HELPERS_DIR)
        if not (stat.S_ISDIR(st.st_mode) or check_perm(st, 0, None, 493)) and check_perm(st, 0, [
            grp.getgrnam('admin').gr_gid,
            0], 509):
            raise Exception(f'''Bad Perms on {BASE_HELPERS_DIR!s} {st!r}''')
        st = os.stat(HELPER_INSTALLER_PATH)
        if stat.S_ISREG(st.st_mode) and st.st_uid != 0 or stat.S_IMODE(st.st_mode) != 2377:
            raise Exception(f'''Bad Perms on {HELPER_INSTALLER_PATH!s} {st!r}''')
        return True
    except OSError:
        e = None
        if e.errno != errno.ENOENT:
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
        e = None
        del e
        return False
        e = None
        del e
        except Exception:
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
            return False



def update_helper_installer(metrics_reporter = None):
    helper_tgz_hash = _get_helper_tgz_hash(metrics_reporter)
    
    try:
        if check_helper_installer():
            install_dropbox_helper('DropboxHelperInstaller')
            _report_helper_update_event('success', metrics_reporter, helper_tgz_hash)
            return True
        _report_helper_update_event('no_installer', metrics_reporter, helper_tgz_hash)
        return False
    except OSError:
        e = None
        if e.errno != errno.ENOENT:
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
        _report_helper_update_event('os_error', metrics_reporter, helper_tgz_hash)
        e = None
        del e
        return False
        e = None
        del e
        except InstallError:
            _report_helper_update_event('install_error', metrics_reporter, helper_tgz_hash)
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
            return False
        except Exception:
            _report_helper_update_event('error', metrics_reporter, helper_tgz_hash)
            report_exception(severity = Severity.WARN, component = DesktopComponent.UNKNOWN)
            return False



def _get_dependencies_dir():
    return 'mac_dependencies'


def _get_helper_path(name = None):
    if hasattr(sys, 'frozen'):
        return os.path.join(get_resources_dir(), name + '.tgz')
    return None.path.abspath(os.path.join(_get_dependencies_dir(), f'''{name!s}.{platform.machine()!s}.tgz'''))


def install_dropbox_helper(package = None, fullpath = None):
    if not os.path.exists(HELPER_INSTALLER_PATH):
        raise InstallError('no installer')
# WARNING: Decompyle incomplete


def promote_from_helper(app_bundle_path = None, existence_checker_path = None):
    if not check_helper_installer():
        TRACE('[AutoUpdater] No helper installer found')
        return PromoteFromHelperResult.NO_HELPER
    TRACE('[AutoUpdater] Promoting from helper with command: install-system-updater %s %s %s', app_bundle_path, existence_checker_path, build_number.VERSION)
    
    try:
        out = subprocess.check_output([
            HELPER_INSTALLER_PATH,
            'install-system-updater',
            app_bundle_path,
            existence_checker_path,
            build_number.VERSION], stderr = subprocess.STDOUT, timeout = 60)
        if out:
            TRACE('[AutoUpdater] Helper installer output: %s', out)
        TRACE('[AutoUpdater] Helper installer successfully returned 0')
        return PromoteFromHelperResult.SUCCESS
    except subprocess.CalledProcessError:
        e = None
        if e.output:
            TRACE('[AutoUpdater] Helper installer output: %s', e.output)
        TRACE('[AutoUpdater] Helper installer failed with return code %d', e.returncode)
        del e
        return None
        None = 
        del e
        except subprocess.TimeoutExpired:
            e = None
            TRACE('[AutoUpdater] Helper installer failed with a timeout: %s', e)
            del e
            return None
            None = 
            del e


install_and_assert_mode = (lambda b = None, info = None: b_path = os.path.join(HELPERS_DIR, b).encode('utf8')# WARNING: Decompyle incomplete
)()

def install_dropbox_helpers_with_fallback(b_perm_info = None):
    for b, info in iteritems(b_perm_info):
        install_and_assert_mode(b, info)
        return True

