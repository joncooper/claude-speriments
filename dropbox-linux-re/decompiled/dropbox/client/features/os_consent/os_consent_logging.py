# Source Generated with Decompyle++
# File: os_consent_logging.pyc (Python 3.11)

from enum import Enum, unique
from string import hexdigits
from typing import Dict, Optional, Text
from mypy_extensions import TypedDict
from dropbox.event import report
from dropbox.exception.reporting import report_bad_assumption
from dropbox.sync_root.interface import SyncRootType
OSConsentEvent = <NODE:12>()

def report_os_consent_flow_event(event_name = None, flow_id = None, sync_root_type = unique, extra = (None, None)):
    pass
# WARNING: Decompyle incomplete


def report_os_consent_event(event_name = None, sync_root_type = None):
    _report_os_consent_event(_OSConsentEventDict(consent_flow_session = None, event_name = event_name.value, sync_engine_root_type = sync_root_type.value if sync_root_type else None))

_OSConsentEventDict = TypedDict('_OSConsentEventDict', {
    'consent_flow_session': Optional[Text],
    'event_name': Text,
    'sync_engine_root_type': Optional[Text],
    'extra': Dict[(Text, Text)] }, total = False)

def _report_os_consent_event(event = None):
    pass
# WARNING: Decompyle incomplete

