# Source Generated with Decompyle++
# File: exception_context.pyc (Python 3.11)

from typing import Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.rtrace_api import get_rtrace_sync_engine_version
from dropbox.client.unlink_cookie import get_insecure_unique_host_ints
from dropbox.client.util import is_app_hard_exiting
from dropbox.exception.exception_constants import ImportCycleAttrs
from dropbox.foundation.platform_version import PLATFORM_VERSION

def get_import_cycle_attrs(account = None):
    during_shutdown = is_app_hard_exiting()
    machine_id = str(UNSAFE_get_raw_machine_uuid())
    platform_version = PLATFORM_VERSION
    seen_hosts = list(get_insecure_unique_host_ints())
    sync_engine_version = get_rtrace_sync_engine_version(account)
    return ImportCycleAttrs(during_shutdown, machine_id, platform_version, seen_hosts, sync_engine_version)

