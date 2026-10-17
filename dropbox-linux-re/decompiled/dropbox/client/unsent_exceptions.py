# Source Generated with Decompyle++
# File: unsent_exceptions.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import json
import sys
from threading import RLock
from typing import Dict, List, Optional, Text
from build_number import is_full_msix, is_store_managed
from dropbox.build_common import get_build_number
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_constants import EXC_TYPE_EXCEPTION
from dropbox.exception.saved_exception_handle import SavedExceptionHandle
from dropbox.exception.severity import Severity
from dropbox.functions import python_version_string
from dropbox.monotonic_time import get_monotonic_time_seconds

class UnsentExceptionInfo:
    
    def __init__(self, exc_hash, count, host_secret, exc_report, crashdash_event_id, severity, component, exc_message, during_shutdown, ui_present, out_of_memory, out_of_disk, client_session_id, machine_id, platform_version, seen_hosts, linked_host_ids_for_telemetry, report_type, sync_engine_version, buildid, exclude_from_metrics, sync_root_type, cpu_family, true_processor_arch = None, application_arch = None, sentry_correlation_id = None, channel_id = (None, None, '', False, False, False, False, None, None, None, None, None, None, None, None, False, None, None, None, None, None, None, None), build_channel = ('exc_hash', 'str', 'count', 'int', 'host_secret', 'Optional[Text]', 'exc_report', 'str', 'crashdash_event_id', 'Optional[str]', 'severity', 'Optional[Severity]', 'component', 'Optional[DesktopComponent]', 'exc_message', 'Text', 'during_shutdown', 'bool', 'ui_present', 'bool', 'out_of_memory', 'bool', 'out_of_disk', 'bool', 'client_session_id', 'Optional[str]', 'machine_id', 'Optional[str]', 'platform_version', 'Optional[str]', 'seen_hosts', 'Optional[List[int]]', 'linked_host_ids_for_telemetry', 'Optional[List[int]]', 'report_type', 'Optional[Text]', 'sync_engine_version', 'Optional[str]', 'buildid', 'Optional[str]', 'exclude_from_metrics', 'bool', 'sync_root_type', 'Optional[str]', 'cpu_family', 'Optional[str]', 'true_processor_arch', 'Optional[str]', 'application_arch', 'Optional[str]', 'sentry_correlation_id', 'Optional[str]', 'channel_id', 'Optional[str]', 'build_channel', 'Optional[str]', 'return', 'None')):
