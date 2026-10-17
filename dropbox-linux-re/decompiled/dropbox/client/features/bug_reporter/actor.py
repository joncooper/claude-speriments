# Source Generated with Decompyle++
# File: actor.pyc (Python 3.11)

import base64
import json
import pprint
from time import time as _time
from typing import Any, Dict, Optional
from event_reporter import BugReporterEventName, BugReporterEventReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.bug_reporter import BUG_INFORMATION_PROVIDERS
from dropbox.client.features.bug_reporter.types import BugTime, BugType, ErrorDetails
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.futures.basic import Future
from dropbox.foundation.performance import PerfSession
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.functions import make_bytes
from dropbox.legacy_crypto.dropboxy import encrypt_blob_with_new_session_key
from dropbox.platform import IS_WINDOWS
from dropbox.trace import TRACE

class BugReportSubmissionError(Exception):
    pass


class BugReporter(Actor):
    pass
# WARNING: Decompyle incomplete

