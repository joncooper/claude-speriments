# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import errno
import subprocess
from enum import Enum
from typing import Optional, Text
from build_number import is_run_box
from macinfinite.common import DBKEXTD_VERSION, INFINITE_KEXT_IDENTIFIER, INFINITE_KEXT_VERSION_CANARY, INFINITE_KEXT_VERSION_DEV, INFINITE_KEXT_VERSION_STABLE, installed_dropbox_kext_version_string, installed_fsplaceholder_kext_version_string, run_box_debug_sysctl_option, skip_placeholder_protections_sysctl_option
from macinfinite.dbkext import running_dbkextd_version_string
from macinfinite.kern_control import ENABLE_INFINITE_PROXY_HELPER
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.infinite import InfiniteReleaseChannel
from dropbox.trace import TRACE

class InfiniteComponent(Enum):
    DROPBOX_KEXT = 'dropbox_kext'
    FSPLACEHOLDER_KEXT = 'fsplaceholder_kext'
    DBKEXTD = 'dbkextd'


class InfiniteVersion(object):
    
    def __init__(self = None, kind = None, version_string = None):
        comps = version_string.split('.')()
    # WARNING: Decompyle incomplete

    
    def __eq__(self = None, other = None):
        if isinstance(other, InfiniteVersion):
            pass
        return self.comps == other.comps if self.kind == other.kind else False

    
    def __ne__(self = None, other = None):
        if isinstance(other, InfiniteVersion):
            pass
        return self.comps != other.comps if self.kind != other.kind else True

    
    def __lt__(self = None, other = None):
        return self.comps < other.comps

    
    def __le__(self = None, other = None):
        return self.comps <= other.comps

    
    def __gt__(self = None, other = None):
        return self.comps > other.comps

    
    def __ge__(self = None, other = None):
        return self.comps >= other.comps

    
    def __repr__(self = None):
        return f'''<InfiniteVersion: {self.kind!r} {self._version_string!r}>'''

    
    def version_string(self = None):
        return self._version_string



def installed_kext_version():
    version_string = installed_fsplaceholder_kext_version_string()
    if version_string:
        return InfiniteVersion(InfiniteComponent.FSPLACEHOLDER_KEXT, version_string)
    version_string = installed_dropbox_kext_version_string()
    if version_string:
        return InfiniteVersion(InfiniteComponent.DROPBOX_KEXT, version_string)


def latest_kext_version(release_channel = None):
    if release_channel == InfiniteReleaseChannel.DEV:
        return InfiniteVersion(InfiniteComponent.DROPBOX_KEXT, INFINITE_KEXT_VERSION_DEV)
    if None == InfiniteReleaseChannel.CANARY:
        return InfiniteVersion(InfiniteComponent.DROPBOX_KEXT, INFINITE_KEXT_VERSION_CANARY)
    return InfiniteVersion(InfiniteComponent.DROPBOX_KEXT, INFINITE_KEXT_VERSION_STABLE)


def is_any_kext_version_running():
    return installed_kext_version() is not None


def is_any_kext_version_installed():
    if ENABLE_INFINITE_PROXY_HELPER:
        return True
    
    try:
        kext_path = subprocess.check_output([
            'kextfind',
            '-b',
            INFINITE_KEXT_IDENTIFIER])
        return bool(kext_path)
    except subprocess.CalledProcessError:
        report_exception(severity = Severity.TRACE, component = DesktopComponent.INFINITE)
        return False



def is_latest_kext_version_installed(release_channel = None):
    return latest_kext_version(release_channel) == installed_kext_version()


def is_kext_validating_client_signature():
    return run_box_debug_sysctl_option() == 0


def is_kext_protecting_placeholders():
    return skip_placeholder_protections_sysctl_option() == 0


def running_dbkextd_version():
    (version_string, _) = running_dbkextd_version_string()
    return InfiniteVersion(InfiniteComponent.DBKEXTD, version_string) if version_string else None


def latest_dbkextd_version():
    return InfiniteVersion(InfiniteComponent.DBKEXTD, DBKEXTD_VERSION)


def is_latest_dbkextd_version_running():
    return latest_dbkextd_version() == running_dbkextd_version()


def check_unsigned_run_box_access_error(err_no = None):
    if err_no == errno.EACCES:
        run_box_error = is_run_box()
        if run_box_error:
            TRACE("!! TO YOU, THE DEVELOPER: You're using run-box, and the (unsigned) Dropbox process cannot connect to the kext. Please enable the `run_box` sysctl debug option on the command line: '$ sudo sysctl -w dropbox.infinite.run_box=1'")
    return run_box_error

