# Source Generated with Decompyle++
# File: reporting.pyc (Python 3.11)

import errno
import platform
import random as insecure_random
import sys
import textwrap
import traceback
from datetime import datetime, timezone
from types import FrameType, TracebackType
from typing import Any, Callable, Dict, List, Optional, Text, Type, TypeVar
from uuid import uuid4
import sentry_sdk
from apex.context import ApexContext
from apex.metrics import Metric
from apex.util import process_architecture, system_architecture
from build_number import BUILD_KEY, BUILDID, get_build_channel, is_frozen, is_prod, VERSION
from dropbox.account_context import deduce_account
from dropbox.assertions import register_assertion_reporters
from dropbox.callbacks import set_default_handler_handle_exc
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.linked_host_telemetry import get_linked_host_ids_for_telemetry, has_mti_team_accounts
from dropbox.client.rtrace_api import delayed_report_unsent_exceptions, get_rtrace_account, get_rtrace_sync_engine_version, is_rtrace_available, report_unsent_exceptions
from dropbox.client.unsent_exceptions import _unsent_exceptions, _unsent_exceptions_lock, UnsentExceptionInfo
from dropbox.client_api.exceptions import is_transient_error
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception import ExcWithSentryTags
from dropbox.exception.exception_constants import ImportCycleAttrs
from dropbox.exception.exceptions import BadAssumptionError, BootError, ComponentError, JavascriptError, NucleusPanicException, PythonBridgeError, RareEvent, SuppressedExceptionMixin, UnexpectedNoneError
from dropbox.exception.persistence import maybe_save_to_disk
from dropbox.exception.severity import get_severity, Severity
from dropbox.handler_registries import run_exception_handlers
from dropbox.observable import set_default_observable_handle_exc
from dropbox.platform import IS_LINUX, IS_MAC, IS_WINDOWS, platform as dropbox_platform
from dropbox.sqlite3_exceptions import ConnectionClosedError
from dropbox.sync_root.types import get_sync_root_value_from_engine_version
from dropbox.trace import TRACE, trace_locals as trace_locals_func
from dropbox.trace_report import ExceptionCounter, make_real_javascript_report, make_report, MAX_REPORT_LENGTH
if IS_MAC:
    from pymac.dlls.CoreServices import OSStatusError
elif IS_WINDOWS:
    from _ctypes import COMError
    import pywintypes
MYPY = False
if MYPY:
    from sentry_sdk._types import ExcInfo
_exception_counter = ExceptionCounter()
_REPORT_CONNECTION_CLOSED = True
DEFAULT_FULL_STACK_TRACEBACK_SIZE = 50
SENTRY_APP_START_TIME = datetime.now(timezone.utc).isoformat()

def stop_reporting_connection_closed():
    global _REPORT_CONNECTION_CLOSED
    _REPORT_CONNECTION_CLOSED = False

_apex_context: 'Optional[ApexContext]' = None
_client_session_id: 'Optional[str]' = None
_exception_context_provider: 'Optional[Callable[[Optional[AccountInterface]], ImportCycleAttrs]]' = None
_ui_present_provider: 'Optional[Callable[[], bool]]' = None

def initialize_exception_reporting(apex_context = None, session_id = None, exception_context_provider = None, ui_present_provider = ('apex_context', 'ApexContext', 'session_id', 'str', 'exception_context_provider', 'Callable[[Optional[AccountInterface]], ImportCycleAttrs]', 'ui_present_provider', 'Callable[[], bool]', 'return', 'None')):
    global _apex_context, _client_session_id, _exception_context_provider, _ui_present_provider
    _apex_context = apex_context
    _client_session_id = session_id
    _exception_context_provider = exception_context_provider
    _ui_present_provider = ui_present_provider
    register_assertion_reporters(report_assertion_error, report_exception)
    set_default_observable_handle_exc(report_exception)
    set_default_handler_handle_exc((lambda : report_exception(severity = Severity.CRITICAL, component = DesktopComponent.CRASH_AND_EXCEPTION_REPORTING)))


def _trace_locals(exc_tb_frame = None):
    if exc_tb_frame:
        TRACE('!! locals of %s:', exc_tb_frame.f_code.co_name)
        trace_locals_func(exc_tb_frame.f_locals)
        return None


def _get_exception_message(exc_val = None):
    pass
# WARNING: Decompyle incomplete


def _record_exception_metric(severity = None, component = None):
    pass
# WARNING: Decompyle incomplete


def report_js_exception(severity = None, exc_val = None, exc_traceback = None, use_message_for_legacy_hash = (None, False, None), component = ('severity', 'Severity', 'exc_val', 'JavascriptError', 'exc_traceback', 'Optional[TracebackType]', 'component', 'Optional[DesktopComponent]', 'return', 'None')):
    pass
# WARNING: Decompyle incomplete

_persistent_exceptions = {
    'out_of_memory': False,
    'out_of_disk': False }

def report_exception(*, severity, exc_type, exc_val, exc_traceback, component, use_message_for_legacy_hash, trace_locals, account, save_me_maybe, exclude_from_metrics, use_electron_transport, sentry_correlation_id):
    pass
# WARNING: Decompyle incomplete


def _record_and_trace_exception(account = None, report = None, _hash = None, severity = ('account', 'Optional[AccountInterface]', 'report', 'str', '_hash', 'str', 'severity', 'Severity', 'return', 'None')):
    (should_trace_stack, exc_count) = _exception_counter.record_exception(_hash)
    if should_trace_stack:
        sync_engine_version = str(get_rtrace_sync_engine_version(account))
        sync_engine_version_debug = ', sync_engine=%s' % sync_engine_version if sync_engine_version else ''
        '\n'.join((lambda .0: pass# WARNING: Decompyle incomplete
)([
            '%d instance(s) of exception (build=%s, legacy_hash=%s%s, %s):' % (exc_count, VERSION, _hash, sync_engine_version_debug, severity)] + report.split('\n')()))
        return None
    last_nonempty_line = None.strip().split('\n')[-1]
    TRACE('!! Exception (legacy_hash=%s) encountered: %s', _hash, last_nonempty_line)


def exception_cpu_family():
    cpu_family = platform.machine().lower()
    if cpu_family == 'x86_64':
        cpu_family = 'amd64'
    return cpu_family


def _format_stack_for_traces(stack = None):
    return textwrap.indent(''.join(stack), '!! ')

_executing_queue_to_server = False

def _queue_exception_report_to_server(exc_type, exc_val, exc_traceback, severity, component, _hash, report, message, ui_present, account, exc_tb_frame, save_me_maybe = None, report_type = None, exclude_from_metrics = None, use_electron_transport = (False, None, False, False, None), sentry_correlation_id = ('exc_type', 'Optional[Type[BaseException]]', 'exc_val', 'Optional[BaseException]', 'exc_traceback', 'Optional[TracebackType]', 'severity', 'Severity', 'component', 'Optional[DesktopComponent]', '_hash', 'str', 'report', 'str', 'message', 'Text', 'ui_present', 'bool', 'account', 'Optional[AccountInterface]', 'exc_tb_frame', 'Optional[FrameType]', 'save_me_maybe', 'bool', 'report_type', 'Optional[Text]', 'exclude_from_metrics', 'bool', 'use_electron_transport', 'bool', 'sentry_correlation_id', 'Optional[Text]', 'return', 'None')):
    global _executing_queue_to_server
    if _executing_queue_to_server:
        TRACE('!! Recursive call to _queue_exception_report_to_server!')
        TRACE('%s', _format_stack_for_traces(traceback.format_stack()))
        return None
    _executing_queue_to_server = None
# WARNING: Decompyle incomplete


def report_with_stack_trace(cls = None, default_severity = None):
    pass
# WARNING: Decompyle incomplete

report_bad_assumption = report_with_stack_trace(BadAssumptionError, Severity.CRITICAL)
report_unexpected_none = report_with_stack_trace(UnexpectedNoneError, Severity.CRITICAL)
report_assertion_error = report_with_stack_trace(AssertionError, Severity.CRITICAL)
report_boot_error = report_with_stack_trace(BootError, Severity.FATAL)
report_rare_event = report_with_stack_trace(RareEvent, Severity.DEBUG)
MaybeType = TypeVar('MaybeType')

def assert_not_none(val = None):
    pass
# WARNING: Decompyle incomplete


def _severity_to_sentry_level(severity = None):
    if severity in (Severity.TRACE, Severity.DEBUG):
        return 'debug'
    if None in (Severity.WARN, Severity.LEGACY_WARN):
        return 'warning'
    if None == Severity.CRITICAL:
        return 'error'
    if None == Severity.FATAL:
        return 'fatal'


def get_sentry_contexts(info = None):
    return {
        'app': {
            'build_type': BUILDID,
            'app_name': f'''{BUILD_KEY} Desktop''',
            'app_version': VERSION,
            'in_foreground': info.ui_present,
            'app_start_time': SENTRY_APP_START_TIME },
        'extra': {
            'legacy_hash': info.exc_hash,
            'seen_hosts': info.seen_hosts,
            'linked_host_ids_for_telemetry': info.linked_host_ids_for_telemetry } }


def get_sentry_tags_from_exc_info(info = None, account = None):
    fields = info.as_dict()
# WARNING: Decompyle incomplete


def derive_sentry_tags_from_exception(exc_val = None):
    if isinstance(exc_val, ExcWithSentryTags):
        return exc_val.extra_sentry_tags()
    tags = _get_platform_error_code_tags(exc_val)
# WARNING: Decompyle incomplete


def _get_platform_error_code_tags(exc_val = None):
    pass
# WARNING: Decompyle incomplete


def report_exception_to_sentry(exc_info, severity = None, account = None, tags = None, contexts = ('exc_info', 'ExcInfo', 'severity', 'Severity', 'account', 'Optional[AccountInterface]', 'tags', 'Dict[str, Any]', 'contexts', 'Dict[str, Dict[str, Any]]', 'return', 'None')):
    sentry_level = _severity_to_sentry_level(severity)
    user = None
# WARNING: Decompyle incomplete

