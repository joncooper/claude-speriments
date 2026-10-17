# Source Generated with Decompyle++
# File: kext_manager.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
import errno
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from collections import defaultdict
from os import walk as _walk
from time import sleep
from typing import Any, Callable, DefaultDict, Dict, List, Optional, Text
from Foundation import NSBundle
from macinfinite.common import connected_bouncer_sysctl_options, connected_clients_sysctl_options, connected_logging_clients_sysctl_options, DBKEXTD_IDENTIFIER, fsplaceholder_connected_clients_sysctl_options, fsplaceholder_connected_logging_clients_sysctl_options, INFINITE_KEXT_IDENTIFIER, installed_fsplaceholder_kext_version_string
from macinfinite.dbkext import install_kext, load_fsplaceholder_kext, remove_dbkextd_job, retrieve_kernel_memory_info, retrieve_loaded_kexts, submit_dbkextd_job, uninstall_kext, unload_fsplaceholder_kext
from macinfinite.kern_control import ENABLE_INFINITE_PROXY_HELPER
from macinfinite.quicklook import quicklook_plugin_version
from six.moves import range
import build_number
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.util.mac import get_resources_dir
from dropbox.components.desktop_components import DesktopComponent
from dropbox.db_thread import db_thread
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.functions import make_unicode
from dropbox.infinite import InfiniteReleaseChannel
from dropbox.infinite.blacklist import InfiniteModuleBlacklist
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.kernel_component_manager import KernelComponentManager
from dropbox.infinite.mac.kext_logging import KextLogReportingThread
from dropbox.infinite.mac.util import InfiniteComponent, InfiniteVersion, installed_kext_version, is_any_kext_version_installed, is_any_kext_version_running, is_kext_validating_client_signature, is_latest_dbkextd_version_running, is_latest_kext_version_installed, latest_kext_version, running_dbkextd_version
from dropbox.infinite.pager import KextNotApprovedError, PagerNotLoadedError
from dropbox.infinite.util import report_infinite_event
from dropbox.mac.helper_installer import HELPERS_DIR, install_dropbox_helpers_with_fallback
from dropbox.mac.internal import autoreleasepool, binaries_ready, BINARIES_READY_TIMEOUT, MacError
from dropbox.mac.version import BIG_SUR, EL_CAPITAN, HIGH_SIERRA, MAC_VERSION, MONTEREY_1203
from dropbox.threading import Lock
from dropbox.trace import TRACE
KERNEL_PANICS_FOLDER_PATH = '/Library/Logs/DiagnosticReports'
OLDEST_SUPPORTED_KEXT_VERSION = '1.6.0'
KEXT_POLICY_PATH = '/var/db/SystemPolicyConfiguration/KextPolicy'
KEXT_IDENTIFIER = 'com.getdropbox.dropbox.kext'
TEAM_IDENTIFIER = 'G7HH3F8CAK'
MDM_OUTPUT_LOCK = Lock()
MDM_OUTPUT: 'Optional[Text]' = None

def parse_legacy_panic_file(content = None):
    return content


def parse_ips_panic_file(content = None):
    first_line_end = content.find('\n')
    if first_line_end == -1:
        return None
    
    try:
        _ = json.loads(content[:first_line_end])
        body = json.loads(content[first_line_end + 1:])
        return body['macOSPanicString']
    except (KeyError, json.JSONDecodeError):
        return None



def guess_panic_format_parser(base = None, name = None):
    name = name.lower()
    if name.startswith('kernel_') and name.endswith('.panic'):
        return parse_legacy_panic_file
    if None.startswith('panic-') and name.endswith('.ips'):
        return parse_ips_panic_file


def kext_versions_in_panic(content = None):
    versions = { }
    is_parsing_kext_in_backtrace = False
    for line in content.split('\n'):
        line = line.strip()
        if is_parsing_kext_in_backtrace:
            if line == '':
                is_parsing_kext_in_backtrace = False
            else:
                paren_index = line.find('(')
                if paren_index >= 0:
                    kext = line[:paren_index]
                    ver = line.partition('(')[2].partition(')')[0]
                    versions[kext] = ver
        if line == 'Kernel Extensions in backtrace:':
            is_parsing_kext_in_backtrace = True
        return versions


def truncate_kext_version(ver = None):
    parts = ver.split('.')
    if len(parts) > 2:
        parts = parts[:2]
    return '.'.join(parts)


class PanicInfo:
    
    def __init__(self = None, content = None):
        self.content = content
        self.kexts = kext_versions_in_panic(content)

    
    def infinite_version(self = None):
        return self.kexts.get('com.getdropbox.dropbox.kext')

    
    def fsplaceholder_version(self = None):
        return self.kexts.get('com.apple.fsplaceholder.kext')



def retrieve_kernel_panics(timestamp = None, folder = None):
    panics = []
# WARNING: Decompyle incomplete


def report_kext_panics(version_dict = None, kext = None):
    for version, count in version_dict.items():
        report_infinite_event(InfiniteEventType.INFINITE_MAC_KEXT_LOAD_PANIC, kext_version = version, kext = kext, count = count)
        return None


class PanicCounts:
    
    def __init__(self = None, panic_list = None):
        infinite = defaultdict(int)
        fsplaceholder = defaultdict(int)
    # WARNING: Decompyle incomplete

    with_infinite_counts = (lambda counts = None: res = PanicCounts([])new_dict = defaultdict(int)for ver, count in counts.items():
dict(new_dict) = Noneres)()
    
    def report_panics(self = None):
        report_kext_panics(self.infinite, 'infinite')
        report_kext_panics(self.fsplaceholder, 'fsplaceholder')



def retrieve_infinite_panic_counts(timestamp = None, folder = None):
    return PanicCounts(retrieve_kernel_panics(timestamp, folder))


class KextManager(KernelComponentManager):
    
    def __init__(self = None, release_channel = None):
        self._release_channel = release_channel
        self._kext_logging_lock = Lock()
        self._should_report_events = False
        self._kext_logging = None
        self._panic_counts = None

    
    def enable_kernel_components_if_needed(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def disable_kernel_components_if_needed(self = None):
        self._should_report_events = False
        if not build_number.is_run_box():
            self.uninstall_quicklook_plugin_if_needed()
        if not is_any_kext_version_installed():
            TRACE('Kext is not installed, no need to uninstall')
            return None
        None.stop_logging_thread_if_needed()
        if is_latest_dbkextd_version_running():
            TRACE('dbkextd is up to date')
        elif build_number.is_run_box():
            TRACE("!! TO YOU, THE DEVELOPER: You're using run-box, and dbkextd cannot be installed Please manually uninstall the kext")
            raise PagerNotLoadedError('Infinite Kext cannot be uninstalled in run-box')
        self.start_dbkextd()
        TRACE('Kext Uninstalling')
        if ENABLE_INFINITE_PROXY_HELPER:
            self._unload_fsplaceholder_kext()
        self.uninstall_infinite_kext()
        self.stop_dbkextd()

    _kernel_components_compatible = (lambda module_blacklist = None: 