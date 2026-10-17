# Source Generated with Decompyle++
# File: hard_trace.pyc (Python 3.11)

import json
import urllib.request as urllib
from typing import Text
from urllib.parse import urlencode
from build_number import dropbox_version
from dropbox.client import high_trace
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client_typing import JSONable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_constants import EXC_TYPE_CRASH
from dropbox.exception.reporting import report_exception, Severity
from dropbox.functions import python_version_string
from dropbox.ssl.context import get_dropbox_ssl_context
from dropbox.trace import TRACE
from dropbox.trace_report import make_report, MAX_REPORT_LENGTH

def report_crash(hash = None, report = None, client_session_id = None):
    pass
# WARNING: Decompyle incomplete

