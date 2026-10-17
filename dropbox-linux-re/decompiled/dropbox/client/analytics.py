# Source Generated with Decompyle++
# File: analytics.pyc (Python 3.11)

from collections import deque
from time import time, time_ns
from typing import Any, Deque, Dict, List, Optional, Tuple
from uuid import uuid4
from apex.analytics import AccountInformation, AnalyticsClient
from google.protobuf.empty_pb2 import Empty
from google.protobuf.json_format import MessageToJson
from google.protobuf.message import Message
from google.protobuf.timestamp_pb2 import Timestamp
from mypy_extensions import TypedDict
import build_number
from build_number import is_test
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.linked_host_telemetry import get_linked_host_ids_for_telemetry, has_mti_team_accounts
from dropbox.client.product_span import ProductSpan
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.i18n import get_current_code
from dropbox.pap_event_logging.utils import EventFieldParser, to_snake_case
from dropbox.proto.event_logging.legacy.legacy_clogger_event_pb2 import AvroList, AvroMap, AvroValue, DesktopGenericCloggerEvent
from dropbox.proto.hql_events.extensions_pb2 import event_identity
from dropbox.proto.hql_events.taxonomy_pb2 import TaxonomyAction, TaxonomyClass, TaxonomySubclass
from dropbox.proto.pap.event_state_pb2 import EventState
from dropbox.proto.pap_event_logging.event_client_pb2 import ClientEventData, PredefinedEvent
from dropbox.threading import Lock
from dropbox.trace import TRACE

class HqlDebugEvent(TypedDict):
    team_id: 'Optional[int]' = 'HqlDebugEvent'

_TypescriptPAPEventBase = TypedDict('_TypescriptPAPEventBase', {
    'action': str,
    'object': str,
    'class': str })

def TypescriptPAPGenericEventProperties():
    '''TypescriptPAPGenericEventProperties'''
    eventState: 'str' = 'TypescriptPAPGenericEventProperties'

TypescriptPAPGenericEventProperties = <NODE:27>(TypescriptPAPGenericEventProperties, 'TypescriptPAPGenericEventProperties', _TypescriptPAPEventBase, total = False)

def TypescriptPAPEvent():
    '''TypescriptPAPEvent'''
    properties: 'TypescriptPAPGenericEventProperties' = 'TypescriptPAPEvent'

TypescriptPAPEvent = <NODE:27>(TypescriptPAPEvent, 'TypescriptPAPEvent', _TypescriptPAPEventBase, total = False)
_GLOBAL_ANALYTICS_CLIENT: 'Optional[AnalyticsClient]' = None
_GLOBAL_DEFAULT_ANALYTICS_ACCOUNT: 'Optional[Tuple[AccountInformation, Optional[int]]]' = None
_GLOBAL_ANALYTICS_CLIENT_LOCK: 'Lock' = Lock()
_GLOBAL_ANALYTICS_STARTUP_EVENTS_BUFFER: 'List[Tuple[Message, Optional[AccountInformation], Optional[str]]]' = []
_GLOBAL_ANALYTICS_HQL_LOG_EXPLORER_EVENTS_BUFFER: 'Deque[HqlDebugEvent]' = deque(maxlen = 200)
_GLOBAL_CLIENT_SESSION_ID: 'Optional[str]' = None

def _log_event_to_apex_and_log_explorer(analytics_client = None, event = None, account_info = None, session_id = ('analytics_client', 'AnalyticsClient', 'event', 'Message', 'account_info', 'Optional[AccountInformation]', 'session_id', 'Optional[str]')):
    if event.DESCRIPTOR.name in ('ClientEventData', 'DesktopGenericCloggerEvent'):
        analytics_client.log_event(event, account_info, session_id)
    else:
        report_bad_assumption(f'''{event.DESCRIPTOR.name} is a deprecated HQL event type, please remove the callsites.''')
# WARNING: Decompyle incomplete


def initialize_global_analytics_client(client = None, default_account = None, client_session_id = None):
    if is_test():
        TRACE('!! Not initializing globals during test')
        return None
# WARNING: Decompyle incomplete


def update_global_analytics_account(account = None):
    _GLOBAL_ANALYTICS_CLIENT_LOCK
# WARNING: Decompyle incomplete


def teardown_global_analytics_client():
    global _GLOBAL_ANALYTICS_CLIENT, _GLOBAL_CLIENT_SESSION_ID, _GLOBAL_DEFAULT_ANALYTICS_ACCOUNT
    _GLOBAL_ANALYTICS_CLIENT_LOCK
    client, _GLOBAL_ANALYTICS_CLIENT = _GLOBAL_ANALYTICS_CLIENT, None
    session_id, _GLOBAL_CLIENT_SESSION_ID = _GLOBAL_CLIENT_SESSION_ID, None
    account, _GLOBAL_DEFAULT_ANALYTICS_ACCOUNT = _GLOBAL_DEFAULT_ANALYTICS_ACCOUNT, None
    _GLOBAL_ANALYTICS_STARTUP_EVENTS_BUFFER.clear()
    None(None, None)


def log_event(event = None, account_info = None):
    _log_event(event, account_info, ProductSpan.instance().get_id())


def _log_event(event = None, account_info = None, session_id = None):
    _GLOBAL_ANALYTICS_CLIENT_LOCK
# WARNING: Decompyle incomplete


def log_pap_event(event, account_info, product_name = None, validation_trace_id = None, udcl_duration_ms = None, udcl_measure_id = (None, 'core_dropbox', None, None, None, None), event_state = ('event', 'Message', 'account_info', 'Optional[AccountInformation]', 'product_name', 'str', 'validation_trace_id', 'Optional[str]', 'udcl_duration_ms', 'Optional[float]', 'udcl_measure_id', 'Optional[str]', 'event_state', 'Optional[str]', 'return', 'None')):
    _GLOBAL_ANALYTICS_CLIENT_LOCK
    session_id = _GLOBAL_CLIENT_SESSION_ID
    None(None, None)


def log_pap_event_unchecked(event = None, account_info = None, product_name = None):
    _GLOBAL_ANALYTICS_CLIENT_LOCK
    session_id = _GLOBAL_CLIENT_SESSION_ID
    None(None, None)


def _log_pap_event(event, client_session_id, account_info, product_name = None, validation_trace_id = None, udcl_duration_ms = None, udcl_measure_id = (None, 'core_dropbox', None, None, None, None), event_state = ('event', 'Message', 'client_session_id', 'Optional[str]', 'account_info', 'Optional[AccountInformation]', 'product_name', 'str', 'validation_trace_id', 'Optional[str]', 'udcl_duration_ms', 'Optional[float]', 'udcl_measure_id', 'Optional[str]', 'event_state', 'Optional[str]', 'return', 'None')):
    event_name_components = event.__class__.__name__.split('_')
    event_action = to_snake_case(event_name_components[0]) if len(event_name_components) >= 2 else None
    event_object = to_snake_case(event_name_components[1]) if len(event_name_components) >= 2 else None
    parser = EventFieldParser(event)
    event_properties = parser.event_properties()
    if validation_trace_id and 'validation_trace_id' not in event_properties:
        event_properties['validation_trace_id'] = validation_trace_id
    if udcl_duration_ms and 'udcl_duration_ms' not in event_properties:
        event_properties['udcl_duration_ms'] = str(udcl_duration_ms)
    if udcl_measure_id and 'udcl_measure_id' not in event_properties:
        event_properties['udcl_measure_id'] = udcl_measure_id
    timestamp = Timestamp()
    timestamp.FromNanoseconds(nanos = time_ns())
    event_properties['locale'] = get_current_code()
# WARNING: Decompyle incomplete


def log_legacy_event(data_name = None, event = None, account = None):
    pass
# WARNING: Decompyle incomplete


def _encode_value(data_name = None, key = None, value = None):
    pass
# WARNING: Decompyle incomplete


def get_hql_events():
    return list(_GLOBAL_ANALYTICS_HQL_LOG_EXPLORER_EVENTS_BUFFER)

