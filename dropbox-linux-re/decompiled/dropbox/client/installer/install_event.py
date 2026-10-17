# Source Generated with Decompyle++
# File: install_event.pyc (Python 3.11)

import json
from abc import ABC, abstractmethod
from time import time
from typing import Dict, List, Optional, Text
from dropbox.assertions import assert_
from dropbox.client.authentication.account import Account
from dropbox.client.configuration.interface import ConfigurationManagerInterface
from dropbox.client.reporting.util import AvroTypeError, get_reporting_metadata
from dropbox.client.unlink_cookie import HOST_SECRET_KEYNAME
from dropbox.client_api.dropbox_connection import DropboxConnection
from dropbox.client_api.exceptions import HTTP429Error, is_transient_error
from dropbox.client_typing import JSONable
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import TABLE_NAME_REGEXP
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.monotonic_time import get_monotonic_time_seconds
from dropbox.trace import TRACE

class EventReportingException(Exception):
    pass


class EventReporter(ABC):
    report = (lambda self = None, data_name = None: raise NotImplementedError())()


class TimedEventReporter(EventReporter):
    
    def __init__(self = None, reporter = None):
        self._start_time = get_monotonic_time_seconds()
        self._reporter = reporter

    
    def report(self = None, data_name = None, **info):
        duration_ms = int((get_monotonic_time_seconds() - self._start_time) * 1000)
    # WARNING: Decompyle incomplete



class InstallEventReporter(EventReporter):
    pass
# WARNING: Decompyle incomplete

