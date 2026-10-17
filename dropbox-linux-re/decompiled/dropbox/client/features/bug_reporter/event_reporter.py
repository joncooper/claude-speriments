# Source Generated with Decompyle++
# File: event_reporter.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from typing import Dict, Optional, Text
from dropbox.event import report
from dropbox.event_names import HTML_VIEWS_BUG_REPORTER_EVENT

class BugReporterEventName(Enum):
    FINISH_COLLECTING = 'finish_collecting_info'
    INITIALIZED = 'bug_reporter_initialized'
    RECEIVED_SERVER_RESPONSE = 'received_server_response'
    RECEIVED_UNEXPECTED_SERVER_RESPONSE = 'received_unexpected_server_response'
    SENDING_REPORT = 'sending_bug_report'
    START_COLLECTING = 'start_collecting_info'
    STARTED = 'start_report_portal'
    SUCCESS_RESULT_WITHOUT_ISSUE_LINK = 'success_result_without_issue_link'


class BugReporterEventReporter:
    
    def report(self = None, event_name = None, event_details = None, **details):
        pass
    # WARNING: Decompyle incomplete


