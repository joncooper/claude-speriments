# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from functools import lru_cache
from subprocess import run as _subprocess_run
from time import time as _time
from typing import Optional, Tuple
from build_number import is_full_msix, is_store_managed
from build_number.features import feature_enabled
from interface import SyncRootType
from types import SyncRootHydrationPolicy
from dropbox.client.features.file_provider_migration.constants import FP_BY_DEFAULT_FILE_COUNT_LIMIT_STORMCROW
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.authentication.account_interface import AccountInterface
    from dropbox.client.gandalf import Gandalf
ROOT_TYPE_CALL_TIMEOUT_SECONDS = 5
SYSTEM_EXTENSION_LIST_TTL_SECONDS = 300
_list_system_extensions = (lambda : list_command = [
'/usr/bin/systemextensionsctl',
'list']command_timeout_in_seconds = 5try:
result = _subprocess_run(list_command, capture_output = True, check = True, timeout = command_timeout_in_seconds)(_time(), result.stdout.decode('utf-8'))except Exception:
e = Nonereport_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_ROOT_MANAGER)TRACE('Listing system extensions failed - %s', e)del eNoneNone = del e)()

def _is_running_crowdstrike():
    crowdstrike_identifier = 'crowdstrike'
    (result_time, running_extensions) = _list_system_extensions()
    if _time() - result_time > SYSTEM_EXTENSION_LIST_TTL_SECONDS:
        _list_system_extensions.cache_clear()
        (_, running_extensions) = _list_system_extensions()
    if running_extensions and crowdstrike_identifier not in running_extensions:
        return False


def is_fp_ineligible_due_to_crowdstrike_check():
    MAC_VERSION = MAC_VERSION
    VENTURA_13_3 = VENTURA_13_3
    import dropbox.mac.version
    if MAC_VERSION < VENTURA_13_3:
        return _is_running_crowdstrike()


def file_provider_supported():
    if not IS_MAC:
        return False
    MAC_VERSION = MAC_VERSION
    MONTEREY = MONTEREY
    import dropbox.mac.version
    return MAC_VERSION >= MONTEREY


def file_provider_eligible(gandalf = None, account = None):
