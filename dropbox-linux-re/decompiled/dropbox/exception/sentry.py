# Source Generated with Decompyle++
# File: sentry.pyc (Python 3.11)

import gzip
import io
import os
import threading
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
import sentry_sdk
from apex.metrics import Metric, MetricsReporter
from apex.util import process_architecture
from sentry_sdk.envelope import Envelope, Item
from sentry_sdk.integrations.argv import ArgvIntegration
from sentry_sdk.integrations.modules import ModulesIntegration
from sentry_sdk.integrations.stdlib import StdlibIntegration
from sentry_sdk.session import Session
from sentry_sdk.transport import Transport
from build_number import get_build_channel, is_test, VERSION
from dropbox.client.authentication.linked_host_telemetry import has_mti_team_accounts_tag, linked_host_count_tag
from dropbox.client.constants import AppDataPaths
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.high_trace import _assert_on_rtrace_thread, _on_rtrace_thread_returns_none, report_bad_assumption, RtraceThread
from dropbox.client_api.exceptions import DropboxServerError
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report
from dropbox.exception.dbx_dedup import DbxDedupeIntegration
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.environment import is_under_automation
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.threading import Lock
from dropbox.trace import TRACE
MYPY = False
if MYPY:
    from sentry_sdk._types import Event, EventDataCategory
    from dropbox.client.device_info import DeviceInfo
    from dropbox.client.main import DropboxApplication
    from dropbox.client.main_utility import DropboxApplicationUtility
DROPBOX_APP_IDENTIFIER = 'com.getdropbox.dropbox'
DISABLE_SENTRY_STORMCROW = 'desktop-disable-sentry-python'
SENTRY_ENVELOPE_EXTENSION = '.exc'
EXCEPTION_UPLOAD_INTERVAL_SECS = 60

def sentry_exception_dir():
    return os.path.join(AppDataPaths.dropbox_appdata_path, 'sentry_exceptions')


class DropboxConnectionSentryTransport(Transport):
    pass
# WARNING: Decompyle incomplete


def _SENTRY_TRANSPORT: 'Transport'(platform_name = None):
    if platform_name == 'mac':
        return 'macOS'
    if None == 'win':
        return 'Windows'
    if None == 'linux':
        return 'Linux'


def capture_raw_sentry_envelope(envelope_bytes = None):
    envelope = Envelope.deserialize(envelope_bytes)
    _SENTRY_TRANSPORT.capture_envelope(envelope)


def initialize_sentry(app, hostname, machine_id, platform_name = None, platform_version = None, model = None, device_info = ('app', 'Union[DropboxApplication, DropboxApplicationUtility]', 'hostname', 'str', 'machine_id', 'str', 'platform_name', 'str', 'platform_version', 'str', 'model', 'str', 'device_info', 'Optional[DeviceInfo]', 'return', 'None')):
    global _SENTRY_TRANSPORT
    TRACE('Initialize Sentry SDK')
    _SENTRY_TRANSPORT = DropboxConnectionSentryTransport(app, { })
    _SENTRY_TRANSPORT.send_exceptions_periodically()
    sentry_release = f'''{DROPBOX_APP_IDENTIFIER}@{VERSION}'''
    sentry_environment = get_build_channel()
    sentry_sdk.init(transport = _SENTRY_TRANSPORT, traces_sample_rate = 1, default_integrations = False, integrations = [
        DbxDedupeIntegration(app = app),
        StdlibIntegration(),
        ModulesIntegration(),
        ArgvIntegration()], environment = sentry_environment, release = sentry_release, include_local_variables = False, auto_session_tracking = False)
    device_context = {
        'name': hostname,
        'model': model,
        'uuid': machine_id,
        'arch': process_architecture(),
        'boot_time': datetime.fromtimestamp(time.time() - get_monotonic_time_seconds(), timezone.utc).isoformat() }
# WARNING: Decompyle incomplete

