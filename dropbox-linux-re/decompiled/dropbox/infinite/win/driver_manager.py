# Source Generated with Decompyle++
# File: driver_manager.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function, unicode_literals
from typing import Any
from build_number import is_frozen
from lib.wininfinitedrivers.driver_installation import DriverNotInstalledError, IncompatibleDriverArchitectureError, IncompatibleDriverSignatureError, InfiniteDriverInstaller, InsufficientDriverInstallationPrivilegesError, OmahaFailedToConnectError, OmahaInterfaceMismatchError
from dropbox.exception.reporting import report_bad_assumption, report_rare_event
from dropbox.infinite import InfiniteReleaseChannel
from dropbox.infinite.blacklist import InfiniteModuleBlacklist
from dropbox.infinite.constants import InfiniteEventType
from dropbox.infinite.kernel_component_manager import KernelComponentManager
from dropbox.infinite.pager import PagerMissingElevationError, PagerNotLoadedError
from dropbox.infinite.util import report_infinite_event
from dropbox.infinite.win.service_proxy import InfiniteService, ServiceFailedToConnectError
from dropbox.infinite.win.util import get_kernel_memory_usage, get_running_version, retrieve_loaded_drivers
from dropbox.install_type import get_dropbox_install_type, InstallType
from dropbox.trace import TRACE
VERSION = 4
SUPPORTED_VERSIONS = (2, 3, 4)

class DriverManager(KernelComponentManager):
    
    def __init__(self = None, release_channel = None):
        self._should_report_events = False
        self._machine_install_popup_shown = False
        self._release_channel = release_channel

    
    def enable_kernel_components_if_needed(self = None):
        self._should_report_events = True
    # WARNING: Decompyle incomplete

    
    def disable_kernel_components_if_needed(self = None):
        self._should_report_events = False
        status = InfiniteService.unload_driver()
        TRACE('disable_kernel_components_if_needed: InfiniteService.unload_driver returns %r.', status)
        status = InfiniteService.uninstall_driver()
        if status:
            report_rare_event('InfiniteService.uninstall_driver failed: %r', status)
            return None
        TRACE('disable_kernel_components_if_needed: InfiniteService.uninstall_driver succeeded.')

    _report_installed_kernel_modules = (lambda : driver_to_version = retrieve_loaded_drivers()report_infinite_event(InfiniteEventType.INFINITE_LOADED_DRIVERS, versions = repr(driver_to_version)))()
    _kernel_components_compatible = (lambda module_blacklist = None: 