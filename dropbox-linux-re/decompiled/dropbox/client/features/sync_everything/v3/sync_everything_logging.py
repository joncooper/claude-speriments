# Source Generated with Decompyle++
# File: sync_everything_logging.pyc (Python 3.11)

from __future__ import division
from datetime import timedelta
from enum import auto, Enum, unique
from typing import Any, Dict, Optional, Text
from apex.metrics import Metric, MetricsReporter
from mypy_extensions import TypedDict
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.logging_helpers import amp_tag_extras, bucket_quota_percent, non_pii_extras, try_get_host_id
from dropbox.client.features.sync_everything.v3.event_label import EventLabel
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.multiaccount.role import Roles
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.foundation.context.machine import MachineContext
MYPY = False
if MYPY:
    from dropbox.sync_engine_boundary.constants import OSFolderID
SyncEverythingEvent = <NODE:12>()
SyncEverythingErrorName = <NODE:12>()
SyncEverythingErrorRateEvent = <NODE:12>()

class SyncEverythingUsage(TypedDict):
    kf_movies_size: 'Optional[int]' = 'SyncEverythingUsage'

SyncEverythingUnlinkType = <NODE:12>()
_AMP_NAMESPACE = 'desktop_sync_everything'

def _account_tags(account = unique):
    if account:
        role = Roles.to_str(account.role) if account.role else 'unknown'
        subscription_type = account.subscription_type if account.subscription_type else 'unknown'
    else:
        role = 'unknown'
        subscription_type = 'unknown'
    return {
        'account_role': role,
        'account_subscription': subscription_type }


def _common_amp_tags(account = None):
    tags = _account_tags(account)
    if IS_WINDOWS:
        tags['platform'] = 'win'
    elif IS_MAC:
        tags['platform'] = 'mac'
    else:
        tags['platform'] = 'linux'
    return tags


def _common_hive_tags(account = None):
    tags = _account_tags(account)
    if account and account.quota_info:
        quota_percent = int(account.quota_info.home_usage_percentage())
        quota_percent_str = str(quota_percent)
        quota_bucket = bucket_quota_percent(quota_percent)
    else:
        quota_percent_str = 'unknown'
        quota_bucket = 'unknown'
    tags.update(quota_percent = quota_percent_str, quota_bucket = quota_bucket)
    return tags


def _report_event(account = None, event = None, session_id = None, action_surface = ('account', 'Optional[AccountInterface]', 'event', 'str', 'session_id', 'str', 'action_surface', 'Optional[str]', 'extra_dict', 'Any'), **extra_dict):
    no_pii_extras = sanitize_event_extra_dict(non_pii_extras(extra_dict))
    no_pii_extras.update(_common_hive_tags(account))
    report('sync-everything-events', account = account, event = event, session_id = session_id, action_surface = action_surface, extra = no_pii_extras)
    extra_dict = sanitize_event_extra_dict(extra_dict)
    extra_dict.update(_common_hive_tags(account))
    report('sync-everything-events-restricted', account = account, event = event, session_id = session_id, action_surface = action_surface, extra = extra_dict)


def _report_usage(account = None, usage = None):
    pass
# WARNING: Decompyle incomplete


class SyncEverythingLogger:
    _machine_context: 'Optional[MachineContext]' = None
    register_machine_context = (lambda cls = None, machine_context = None: cls._machine_context = machine_context)()
    _report_amp_metric = (lambda cls, metrics_reporter, metric_name = None, tags = None, value = classmethod, account = ('metrics_reporter', 'MetricsReporter', 'metric_name', 'str', 'tags', 'Dict[str, str]', 'value', 'int', 'account', 'Optional[AccountInterface]', 'return', 'None'): metrics_reporter.create_stats(Metric(_AMP_NAMESPACE, metric_name), tags).record(value)host_id = try_get_host_id(account, cls._machine_context)if value > 0 or host_id:
set_metric = Metric(_AMP_NAMESPACE, metric_name + '__host_count')metrics_reporter.create_set(set_metric, tags).observe(str(host_id))NoneNone)()
    report_event = (lambda account = None, event = None, session_id = staticmethod: pass# WARNING: Decompyle incomplete
)()
    report_first_sync_event = (lambda account = None, event = None, session_id = staticmethod, first_sync_time = ('account', 'Optional[AccountInterface]', 'event', 'str', 'session_id', 'str', 'first_sync_time', 'int', 'return', 'None'): _report_event(account, event, session_id, None, first_sync_time = first_sync_time, nopii_first_sync_time = first_sync_time))()
    report_operation_event_hive = (lambda event = None, account = None, session_id = staticmethod: pass# WARNING: Decompyle incomplete
)()
    report_operation_event_amp = (lambda metrics_reporter = None, event = None, account = staticmethod, count = (None,), extra_tags = ('metrics_reporter', 'MetricsReporter', 'event', 'str', 'account', 'Optional[AccountInterface]', 'count', 'int', 'extra_tags', 'Optional[Dict[str, str]]', 'return', 'None'): tags = _common_amp_tags(account)if extra_tags:
tags.update(extra_tags)SyncEverythingLogger._report_amp_metric(metrics_reporter, 'operation_event/' + event, tags, count, account))()
    report_folder_event_amp = (lambda folder, metrics_reporter, account, event = None, label = None, error = staticmethod, count = ('folder', 'OSFolderID', 'metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'SyncEverythingEvent', 'label', 'EventLabel', 'error', 'Optional[RedirectRequestStatus]', 'count', 'int', 'return', 'None'): event_key = event.nameif event == SyncEverythingEvent.enable_sanity_op_per_folder_future:
event_key = 'sanity_check'elif event == SyncEverythingEvent.enable_op_per_folder_future:
event_key = 'enable'elif event == SyncEverythingEvent.update_op_per_folder_future:
event_key = 'update'elif event == SyncEverythingEvent.unbinding_folder:
event_key = 'unbind'name = '{}_{}'.format(event_key, label.name)# WARNING: Decompyle incomplete
)()
    report_boundary_event_amp = (lambda metrics_reporter = None, account = None, event = staticmethod, count = (1, None), extra_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'Text', 'count', 'int', 'extra_tags', 'Optional[Dict[str, str]]'): tags = _common_amp_tags(account)extra_tags = extra_tags if extra_tags else { }tags.update(extra_tags)SyncEverythingLogger._report_amp_metric(metrics_reporter, 'boundary_event/' + event, tags, count, account))()
    report_performance = (lambda metrics_reporter, account = None, name = None, time = staticmethod, extra_tags = (None, None), additional_perf_events = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'name', 'Text', 'time', 'timedelta', 'extra_tags', 'Optional[Dict[str, str]]', 'additional_perf_events', 'Optional[Dict[str, timedelta]]', 'return', 'None'): tags = _common_amp_tags(account)if extra_tags:
tags.update(extra_tags)metrics_reporter.create_stats(Metric(_AMP_NAMESPACE, 'perf/' + name), tags).record_duration(time)if additional_perf_events:
for additional_timed_event, timer_value in additional_perf_events.items():
metrics_reporter.create_stats(Metric(_AMP_NAMESPACE, f'''perf/{name}_{additional_timed_event.lower()}'''), tags).record_duration(timer_value)NoneNone)()
    report_oneoff_event_amp = (lambda metrics_reporter = None, account = None, name = staticmethod, count = (1, None), extra_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'name', 'SyncEverythingEvent', 'count', 'int', 'extra_tags', 'Optional[Dict[str, str]]', 'return', 'None'): tags = _common_amp_tags(account)if extra_tags:
tags.update(extra_tags)SyncEverythingLogger._report_amp_metric(metrics_reporter, 'oneoff_events/' + name.name, tags, count, account))()
    report_oneoff_event_hive = (lambda account = None, name = None, session_id = staticmethod, hive_extras = (None,): hive_extras = { } if not hive_extras else hive_extras# WARNING: Decompyle incomplete
)()
    report_oneoff_event = (lambda metrics_reporter, account, name = None, session_id = None, amp_count = staticmethod, hive_extras = (None, 1, None, None), amp_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'name', 'SyncEverythingEvent', 'session_id', 'Optional[str]', 'amp_count', 'int', 'hive_extras', 'Optional[Dict[str, Any]]', 'amp_tags', 'Optional[Dict[str, str]]', 'return', 'None'): SyncEverythingLogger.report_oneoff_event_amp(metrics_reporter, account, name, amp_count, amp_tags)SyncEverythingLogger.report_oneoff_event_hive(account, name, session_id, hive_extras))()
    report_ui_event_hive = (lambda account = None, event_name = None, session_id = staticmethod, action_surface = (None,): pass# WARNING: Decompyle incomplete
)()
    report_ui_event_amp = (lambda metrics_reporter, account = None, event_name = None, session_id = staticmethod, tags = (1,), count = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event_name', 'str', 'session_id', 'str', 'tags', 'Dict[str, str]', 'count', 'int', 'return', 'None'): common_tags = _common_amp_tags(account)common_tags.update(tags)SyncEverythingLogger._report_amp_metric(metrics_reporter, 'ui_event/' + event_name, common_tags, count, account))()
    report_ui_event = (lambda metrics_reporter, account = None, event = None, session_id = staticmethod, action_surface = (None, None), backup_on_anchors = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'SyncEverythingEvent', 'session_id', 'str', 'action_surface', 'Optional[str]', 'backup_on_anchors', 'Optional[bool]', 'extra', 'Any', 'return', 'None'): if backup_on_anchors:
extra['nopii_backup_on_anchors'] = str(1)extra['amptag_backup_on_anchors'] = str(1)extra['backup_on_anchors'] = str(1)# WARNING: Decompyle incomplete
)()
    report_error_count_incl_hive = (lambda metrics_reporter, account, name = None, session_id = None, count = staticmethod, hive_extras = (None, 1, None, None), amp_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'name', 'SyncEverythingErrorName', 'session_id', 'Optional[str]', 'count', 'int', 'hive_extras', 'Optional[Dict[str, Any]]', 'amp_tags', 'Optional[Dict[str, str]]', 'return', 'None'): SyncEverythingLogger.report_error_count(metrics_reporter, account, name, count, amp_tags)hive_extras = { } if not hive_extras else hive_extras# WARNING: Decompyle incomplete
)()
    report_error_count = (lambda metrics_reporter = None, account = None, name = staticmethod, count = (1, None), extra_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'name', 'SyncEverythingErrorName', 'count', 'int', 'extra_tags', 'Optional[Dict[str, str]]', 'return', 'None'): tags = _common_amp_tags(account)if extra_tags:
tags.update(extra_tags)SyncEverythingLogger._report_amp_metric(metrics_reporter, 'error_counts/' + name.name, tags, count, account))()
    report_error_rate = (lambda metrics_reporter, account = None, event = None, num_occurred = staticmethod, num_total = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'SyncEverythingErrorRateEvent', 'num_occurred', 'int', 'num_total', 'int'): rate = num_occurred / num_totalmetrics_reporter.create_stats(Metric(_AMP_NAMESPACE, 'error_rates/' + event.name + '_occurred'), _common_amp_tags(account)).record(num_occurred)metrics_reporter.create_stats(Metric(_AMP_NAMESPACE, 'error_rates/' + event.name + '_total'), _common_amp_tags(account)).record(num_total)metrics_reporter.create_stats(Metric(_AMP_NAMESPACE, 'error_rates/' + event.name + '_rate'), _common_amp_tags(account)).record(rate))()
    report_periodic_metrics = (lambda metrics_reporter = None, account = None, usage = staticmethod: for metric, value in usage.items():
if isinstance(value, int):
metrics_reporter.create_stats(Metric(_AMP_NAMESPACE, 'periodic/' + metric), _common_amp_tags(account)).record(value)_report_usage(account, usage)None)()
    report_feature_usage_metric = (lambda metrics_reporter = None, status = None, account = staticmethod: tags = _common_amp_tags(account)tags['state'] = statusmetrics_reporter.create_stats(Metric(_AMP_NAMESPACE, 'periodic/feature_usage'), tags).record(1)if account:
host_id = str(account.host_int)metrics_reporter.create_set(Metric(_AMP_NAMESPACE, 'periodic/feature_usage_hosts'), tags).observe(host_id)None)()
    report_unlink_failure = (lambda metrics_reporter = None, account = None, unlink_type = staticmethod, reason = ('metrics_reporter', 'MetricsReporter', 'account', 'AccountInterface', 'unlink_type', 'SyncEverythingUnlinkType', 'reason', 'Text', 'return', 'None'): tags = {
'reason': reason,
'type': unlink_type.name }SyncEverythingLogger.report_error_count_incl_hive(metrics_reporter, account, SyncEverythingErrorName.unbind_fails_on_unlink, hive_extras = tags, amp_tags = tags))()

