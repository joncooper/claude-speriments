# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from enum import Enum
from typing import Optional
from build_number import is_test
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from dropbox.sync_root.gating import cloud_files_capable, is_file_provider_root_type
from dropbox.sync_root.interface import SyncRootType
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import CATALINA, MAC_VERSION
if IS_LINUX:
    from dropbox.linux.version import LINUX_VERSION, LinuxVersion

class InvalidInfiniteReleaseChannel(Exception):
    pass


class InfiniteReleaseChannel(Enum):
    DEV = 'dev'
    CANARY = 'canary'
    STABLE = 'stable'
    DRT = 'drt'


class InfiniteAllowedContextMenus(Enum):
    NONE = 'none'
    RECALL_OR_UPSELL = 'recall_or_upsell'
    RECALL_AND_EVICT = 'recall_and_evict'


def is_kext_reboot_required(gandalf = None):
