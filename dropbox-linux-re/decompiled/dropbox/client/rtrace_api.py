# Source Generated with Decompyle++
# File: rtrace_api.pyc (Python 3.11)

from typing import Callable, Optional
from dropbox.client.authentication.account_interface import AccountInterface
_get_rtrace_account: 'Optional[Callable[[], Optional[AccountInterface]]]' = None
_get_rtrace_sync_engine_version: 'Optional[Callable[[Optional[AccountInterface]], Optional[str]]]' = None
_report_unsent_exceptions: 'Optional[Callable[[], None]]' = None
_delayed_report_unsent_exceptions: 'Optional[Callable[[], None]]' = None
_is_rtrace_available: 'bool' = False

def register_rtrace_api(*, get_rtrace_account, get_rtrace_sync_engine_version, report_unsent_exceptions, delayed_report_unsent_exceptions):
    global _get_rtrace_account, _get_rtrace_sync_engine_version, _report_unsent_exceptions, _delayed_report_unsent_exceptions, _is_rtrace_available
    _get_rtrace_account = get_rtrace_account
    _get_rtrace_sync_engine_version = get_rtrace_sync_engine_version
    _report_unsent_exceptions = report_unsent_exceptions
    _delayed_report_unsent_exceptions = delayed_report_unsent_exceptions
    _is_rtrace_available = True


def unregister_rtrace_api():
    global _get_rtrace_account, _get_rtrace_sync_engine_version, _report_unsent_exceptions, _delayed_report_unsent_exceptions, _is_rtrace_available
    _get_rtrace_account = None
    _get_rtrace_sync_engine_version = None
    _report_unsent_exceptions = None
    _delayed_report_unsent_exceptions = None
    _is_rtrace_available = False


def is_rtrace_available():
    return _is_rtrace_available


def get_rtrace_account():
    pass
# WARNING: Decompyle incomplete


def get_rtrace_sync_engine_version(account = None):
    pass
# WARNING: Decompyle incomplete


def report_unsent_exceptions():
    pass
# WARNING: Decompyle incomplete


def delayed_report_unsent_exceptions():
    pass
# WARNING: Decompyle incomplete

