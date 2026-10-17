# Source Generated with Decompyle++
# File: desktop_logger.pyc (Python 3.11)

import uuid
from typing import Dict, Literal, NamedTuple, Optional, Union
from apex.analytics import AccountInformation
from apex.metrics import Metric
from dropbox.client.analytics import log_pap_event
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.logging_helpers import common_account_tags, try_get_host_id
from dropbox.client.features.desktop_logging.event_enums import EventState
from dropbox.client.features.desktop_logging.logging_event import _GenericLoggingEvent, NonUserLoggingEvent, PAPLoggingEvent, UDCL_EVENTS_AMP_NAMESPACE, UserEventLoggingEvent
from dropbox.client.features.desktop_logging.UDCL import UDCLSpanManager
from dropbox.client.multiaccount.role import Roles
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.trace import WARNING
EndEventState = Union[(Literal[EventState.SUCCESS], Literal[EventState.FAILED], Literal[EventState.CANCELED], Literal[EventState.REJECTED])]
AccountInfo = NamedTuple('AccountInfo', [
    ('role', str),
    ('quota_bucket', str),
    ('quota_percent', str),
    ('subscription_type', str)])
UDCLMetadata = NamedTuple('UDCLMetadata', [
    ('start_ts_ms', int),
    ('end_ts_ms', int),
    ('measure_id', Optional[str])])
USER_EVENTS_CONSOLIDATED_TABLE_NAME = 'desktop-consolidated_user-events'
ALL_EVENTS_CONSOLIDATED_TABLE_NAME = 'desktop-consolidated_all-events'
LEGACY_ENG_HIVE_TABLE = 'desktop-consolidated_eng-events'

class DesktopLogger:
    _machine_context: 'Optional[MachineContext]' = None
    log_event = (lambda cls = None, event = None, account = classmethod, udcl_meta = (None,): pass# WARNING: Decompyle incomplete
)()
    log_start = (lambda cls = None, event = None, account = classmethod, key = (None,): try:
key = generate_event_key(event, key)UDCLSpanManager.start_span(key)event.set_event_state(EventState.START)event.is_time_to_resolution_event = Truecls.log_event(event, account)Noneexcept Exception:
report_exception(severity = Severity.CRITICAL, component = DesktopComponent.FENIX)None)()
    log_end = (lambda cls = None, event = None, account = classmethod, event_state = (None,), key = ('event', '_GenericLoggingEvent', 'account', 'Optional[AccountInterface]', 'event_state', 'EndEventState', 'key', 'Optional[str]', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    register_machine_context = (lambda cls = None, machine_context = None: cls._machine_context = machine_context)()
    _get_fallback_account = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    _log_event = (lambda cls = None, event = None, account = classmethod: pass# WARNING: Decompyle incomplete
)()
    _report_event_amp = (lambda cls = None, event = None, account = classmethod: if not cls._machine_context:
Nonemetric_name = None.metric_nametags = _common_amp_tags(account)tags.update(event.extra_amis_tags)cls._report_amp_metric(metric_name = metric_name, tags = tags, event = event, account = account))()
    _report_udcl_event_amp = (lambda cls = None, event = None, account = classmethod: if not cls._machine_context:
Noneif isinstance(event, PAPLoggingEvent):
passelif isinstance(event, UserEventLoggingEvent):
passevent_type = 'eng'# WARNING: Decompyle incomplete
)()
    _report_amp_metric = (lambda cls, metric_name = None, tags = None, event = classmethod, account = ('metric_name', 'str', 'tags', 'Dict[str, str]', 'event', '_GenericLoggingEvent', 'account', 'Optional[AccountInterface]', 'return', 'None'): if not cls._machine_context:
Noneif not None.amis_value:
value = 1cls._machine_context.metrics_reporter.create_stats(Metric(_get_amis_namespace(event), metric_name), tags).record(value)host_id = try_get_host_id(account, cls._machine_context)if value > 0 or host_id:
set_metric = Metric(_get_amis_namespace(event), metric_name + '__host_count')cls._machine_context.metrics_reporter.create_set(set_metric, tags).observe(str(host_id))NoneNoneNone.amis_value)()


def _get_amis_namespace(event = None):
    return event.amis_namespace


def _common_amp_tags(account = None):
    tags = common_account_tags(account)
    account_info = _account_info_tags(account)
    tags.update({
        'quota_bucket': account_info.quota_bucket })
    return tags


def _account_info_tags(account = None):
    quota_percent = None
    quota_bucket = 'unknown'
    if account and account.quota_info:
        quota_percent = int(account.quota_info.home_usage_percentage())
        quota_bucket = _bucket_quota_percent(quota_percent)
    role = 'unknown'
# WARNING: Decompyle incomplete


def _bucket_quota_percent(quota_percent = None):
    buckets = [
        10,
        50,
        80,
        90,
        95,
        100]
    if quota_percent < buckets[0]:
        return f'''0-{buckets[0]}'''
    if None >= buckets[-1]:
        return f'''{buckets[-1]}+'''
    for i in range(0, len(buckets) - 1):
        lower = buckets[i]
        upper = buckets[i + 1]
        if  <= lower, quota_percent or lower, quota_percent < upper:
            pass
        
        
        return None, f'''{lower}-{upper}'''
        report_bad_assumption("couldn't bucket quota")
        return 'error'


def generate_event_key(event = None, manual_key = None):
    event_type = ''
    if not manual_key:
        pass
    event_name = event.event_name
    if isinstance(event, PAPLoggingEvent):
        event_type = 'pap'
    if isinstance(event, UserEventLoggingEvent):
        event_type = 'user'
        if not manual_key:
            event_name = f'''{event.event_class}.{event.event_object}.{event.event_action}'''
            if isinstance(event, NonUserLoggingEvent):
                event_type = 'eng'
    return f'''{event_type}:{event_name}'''


def generate_udcl_measure_id():
    return uuid.uuid4().hex

UDCLSpanManager.register_logger(DesktopLogger.log_event)
