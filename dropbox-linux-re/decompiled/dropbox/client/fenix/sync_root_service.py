# Source Generated with Decompyle++
# File: sync_root_service.pyc (Python 3.11)

from pathlib import Path
from typing import Dict, List, Optional, Set, Union
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.os_consent.os_consent_logging import OSConsentEvent, report_os_consent_event, report_os_consent_flow_event
from dropbox.client.fenix.utils import get_account_linked_or_from_cache
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.html_views.electron.ipc import ElectronIpc, JSONDict
from dropbox.foundation.html_views.electron.ipc._interface import JSONish
from dropbox.foundation.html_views.electron.ipc.rpc import ElectronRpc
from dropbox.foundation.raii2.arc import Arc
from dropbox.infinite import infinite_exposed
from dropbox.infinite.preferences import get_previous_user_choice_policy_from_unlink_cookie, InfinitePolicy
from dropbox.sync_root.accessor import RootManagerAccessor
from dropbox.sync_root.fp_external_drive import FP_EXTERNAL_DRIVE_STORMCROW, get_fp_external_drives, is_account_fp_external_drive_eligible
from dropbox.sync_root.types import SyncRootInvalid, SyncRootType, SyncRootTypeReason
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from dropbox.client.main import DropboxApplication
_NS_FILE_PROVIDER_ERROR_DOMAIN = 'NSFileProviderErrorDomain'
_NS_FILE_PROVIDER_ERROR_OLDER_EXTENSION_VERSION_RUNNING = -2003
_NS_FILE_PROVIDER_ERROR_PROVIDER_NOT_FOUND = -2001
_NS_FILE_PROVIDER_ERROR_PROVIDER_DOMAIN_TEMPORARILY_UNAVAILABLE = -2012

def _is_file_provider_domain_error(exc = None, expected_errno = None):
    if getattr(exc, 'errno', None) != expected_errno:
        return False
    extra_sentry_tags = getattr(exc, 'extra_sentry_tags', None)
    if not callable(extra_sentry_tags):
        return False
    
    try:
        return extra_sentry_tags().get('mac_error_domain') == _NS_FILE_PROVIDER_ERROR_DOMAIN
    except Exception:
        return False



def _is_unreported_file_provider_error(exc = None):
    if _is_file_provider_domain_error(exc, _NS_FILE_PROVIDER_ERROR_OLDER_EXTENSION_VERSION_RUNNING):
        return True
    if not _is_file_provider_domain_error(exc, _NS_FILE_PROVIDER_ERROR_PROVIDER_NOT_FOUND):
        return False
    underlying_exc = getattr(exc, 'underlying_exc', None)
    return getattr(underlying_exc, 'errno', None) == _NS_FILE_PROVIDER_ERROR_PROVIDER_DOMAIN_TEMPORARILY_UNAVAILABLE


class SyncRootService(Actor):
    pass
# WARNING: Decompyle incomplete

