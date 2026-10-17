# Source Generated with Decompyle++
# File: backup_logging.pyc (Python 3.11)

from datetime import timedelta
from typing import Any, Dict, Generic, Optional, Set, Tuple, TypeVar, Union
from apex.metrics import Metric, MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_auto_selsync.types import BackupAutoSelSyncEvent, BackupAutoSelSyncEventLabel
from dropbox.client.features.backup_common.logging_helpers import amp_tag_extras, common_account_tags, label_backup_event, try_get_host_id
from dropbox.client.features.backup_instance.types import BackupInstanceActionSurface, BackupInstanceEvent, BackupInstanceEventLabel
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event_label import ComputerBackupEventLabel
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_action_surface import EdbActionSurface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.event_label import EventLabel
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.foundation.context.machine import MachineContext
from dropbox.sync_engine_boundary.constants import SyncEngineGeneration
EventType = TypeVar('EventType', bound = Union[(ExternalBackupEvent, ComputerBackupEvent, BackupInstanceEvent, BackupAutoSelSyncEvent)])
EventLabelType = TypeVar('EventLabelType', bound = Union[(EventLabel, ComputerBackupEventLabel, BackupInstanceEventLabel, BackupAutoSelSyncEventLabel)])
ActionSurfaceType = TypeVar('ActionSurfaceType', bound = Union[(EdbActionSurface, ActionSurface, BackupInstanceActionSurface, None)])
SourceType = TypeVar('SourceType', bound = Union[(EdbSource, Source, None)])

def BackupLogger():
    '''BackupLogger'''
    _machine_context: 'Optional[MachineContext]' = None
    _backup_engine_version: 'Dict[AccountInterface, Tuple[str, SyncEngineGeneration]]' = { }
    register_machine_context = (lambda cls = None, machine_context = None: cls._machine_context = machine_context)()
    register_backup_engine_version = (lambda cls = None, account = None, engine_version_number = classmethod, engine_generation = ('account', 'AccountInterface', 'engine_version_number', 'str', 'engine_generation', 'SyncEngineGeneration', 'return', 'None'): cls._backup_engine_version[account] = (engine_version_number, engine_generation))()
    get_backup_engine_version = (lambda cls = None, account = None: cls._backup_engine_version.get(account, (None, None))[0])()
    get_backup_engine_generation_tag = (lambda cls = None, account = None: if not account:
'none'generation = None._backup_engine_version.get(account, (None, None))[1]# WARNING: Decompyle incomplete
)()
    report_event = (lambda cls, account, event_name = None, session_id = None, event_label = classmethod, action_surface = (None, None, None), source = ('account', 'Optional[AccountInterface]', 'event_name', 'EventType', 'session_id', 'Optional[str]', 'event_label', 'Optional[str]', 'action_surface', 'Optional[ActionSurfaceType]', 'source', 'Optional[SourceType]', 'extras', 'Any', 'return', 'None'): raise NotImplementedError())()
    get_amp_namespace = (lambda cls = None: raise NotImplementedError())()
    common_amp_tags = (lambda cls = None, account = None: tags = common_account_tags(account)tags['backup_engine_generation'] = cls.get_backup_engine_generation_tag(account)tags)()
    terminal_labels = (lambda cls = None: {
'done',
'fail'})()
    _report_amp_metric = (lambda cls, metrics_reporter, metric_name = None, tags = None, value = classmethod, account = ('metrics_reporter', 'MetricsReporter', 'metric_name', 'str', 'tags', 'Dict[str, str]', 'value', 'int', 'account', 'Optional[AccountInterface]', 'return', 'None'): metrics_reporter.create_stats(Metric(cls.get_amp_namespace(), metric_name), tags).record(value)host_id = try_get_host_id(account, cls._machine_context)if value > 0 or host_id:
set_metric = Metric(cls.get_amp_namespace(), metric_name + '__host_count')metrics_reporter.create_set(set_metric, tags).observe(str(host_id))NoneNone)()
    report_operation_event_hive = (lambda cls, event_name, event_label = None, account = None, session_id = classmethod, source = ('event_name', 'EventType', 'event_label', 'str', 'account', 'Optional[AccountInterface]', 'session_id', 'str', 'source', 'Optional[SourceType]', 'extra_dict', 'Any', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    _report_operation_event_amp = (lambda cls, metrics_reporter, event = None, account = None, count = classmethod, source = (None,), extra_tags = ('metrics_reporter', 'MetricsReporter', 'event', 'str', 'account', 'Optional[AccountInterface]', 'count', 'int', 'source', 'Optional[SourceType]', 'extra_tags', 'Optional[Dict[str, str]]', 'return', 'None'): amp_namespace = cls.get_amp_namespace()tags = cls.common_amp_tags(account)if extra_tags:
tags.update(extra_tags)amp_source = source.name.lower() if source else 'Unknown'tags['source'] = amp_sourcecls._report_amp_metric(metrics_reporter, 'operation_event/' + event, tags, count, account))()
    report_operation_event_amp = (lambda cls, metrics_reporter, event, label = None, account = None, count = classmethod, source = (None,), extra_tags = ('metrics_reporter', 'MetricsReporter', 'event', 'Union[str, EventType]', 'label', 'Union[str, EventLabelType]', 'account', 'Optional[AccountInterface]', 'count', 'int', 'source', 'Optional[SourceType]', 'extra_tags', 'Optional[Dict[str, str]]', 'return', 'None'): terminal_labels = cls.terminal_labels()if label in terminal_labels:
for terminal_label in terminal_labels:
is_us = terminal_label == labelcls._report_operation_event_amp(metrics_reporter, label_backup_event(event, terminal_label), account, count if is_us else 0, source, extra_tags)Nonecls._report_operation_event_amp(metrics_reporter, label_backup_event(event, label), account, count, source, extra_tags)None)()
    report_oneoff_event_hive = (lambda cls, account, name = None, session_id = None, action_surface = classmethod, source = (None,), hive_extras = ('account', 'Optional[AccountInterface]', 'name', 'EventType', 'session_id', 'Optional[str]', 'action_surface', 'Optional[ActionSurfaceType]', 'source', 'Optional[SourceType]', 'hive_extras', 'Optional[Dict[str, str]]', 'return', 'None'): hive_extras = { } if not hive_extras else hive_extras# WARNING: Decompyle incomplete
)()
    report_oneoff_event_amp = (lambda cls, metrics_reporter, account = None, name = None, source = classmethod, count = (None, 1, None), extra_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'name', 'EventType', 'source', 'Optional[SourceType]', 'count', 'int', 'extra_tags', 'Optional[Dict[str, str]]', 'return', 'None'): amp_namespace = cls.get_amp_namespace()tags = cls.common_amp_tags(account)if extra_tags:
tags.update(extra_tags)amp_source = source.name.lower() if source else 'Unknown'tags['source'] = amp_sourcecls._report_amp_metric(metrics_reporter, 'oneoff_events/' + name.name, tags, count, account))()
    report_ui_event_hive = (lambda cls, account = None, event = None, session_id = classmethod, action_surface = (None, None), source = ('account', 'Optional[AccountInterface]', 'event', 'EventType', 'session_id', 'str', 'action_surface', 'Optional[ActionSurfaceType]', 'source', 'Optional[SourceType]', 'extra', 'Any', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    report_ui_event_amp = (lambda cls, metrics_reporter = None, account = None, event_name = classmethod, tags = (1,), count = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event_name', 'str', 'tags', 'Dict[str, str]', 'count', 'int', 'return', 'None'): amp_namespace = cls.get_amp_namespace()common_tags = cls.common_amp_tags(account)tags.update(common_tags)cls._report_amp_metric(metrics_reporter, 'ui_event/' + event_name, tags, count, account))()
    _report_boundary_event_amp = (lambda cls, metrics_reporter, account, event = None, label = None, count = classmethod, source = (None, 1, None, None), extra_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'Union[EventType, str]', 'label', 'Optional[Union[str, EventLabelType]]', 'count', 'int', 'source', 'Optional[SourceType]', 'extra_tags', 'Optional[Dict[str, str]]'): amp_namespace = cls.get_amp_namespace()tags = cls.common_amp_tags(account)event_name = label_backup_event(event, label)extra_tags = extra_tags if extra_tags else { }tags.update(extra_tags)amp_source = source.name.lower() if source else 'Unknown'tags['source'] = amp_sourcecls._report_amp_metric(metrics_reporter, 'boundary_event/' + event_name, tags, count, account))()
    report_boundary_event_amp = (lambda cls, metrics_reporter, account, event = None, label = None, count = classmethod, source = (None, 1, None, None), extra_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'EventType', 'label', 'Optional[str]', 'count', 'int', 'source', 'Optional[SourceType]', 'extra_tags', 'Optional[Dict[str, str]]'): terminal_labels = cls.terminal_labels()if label in terminal_labels:
cls._report_boundary_event_amp(metrics_reporter, account, event, None, count, source, extra_tags)for terminal_label in terminal_labels:
is_us = terminal_label == labelcls._report_boundary_event_amp(metrics_reporter, account, event, label, count if is_us else 0, source, extra_tags)Nonecls._report_boundary_event_amp(metrics_reporter, account, event, label, count, source, extra_tags)None)()
    report_performance_amp = (lambda cls, metrics_reporter, account = None, event = None, time = classmethod, extra_tags = (None, None), additional_perf_events = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'EventType', 'time', 'timedelta', 'extra_tags', 'Optional[Dict[str, str]]', 'additional_perf_events', 'Optional[Dict[str, timedelta]]', 'return', 'None'): amp_namespace = cls.get_amp_namespace()tags = cls.common_amp_tags(account)if extra_tags:
tags.update(amp_tag_extras(extra_tags))metrics_reporter.create_stats(Metric(amp_namespace, 'perf/' + event.name.lower()), tags).record_duration(time)if additional_perf_events:
for additional_timed_event, timer_value in additional_perf_events.items():
metrics_reporter.create_stats(Metric(amp_namespace, f'''perf/{event}_{additional_timed_event.lower()}'''), tags).record_duration(timer_value)NoneNone)()
    report_oneoff_event = (lambda cls, metrics_reporter, account, name, session_id, action_surface = None, source = None, amp_count = classmethod, hive_extras = (None, None, None, 1, None, None), amp_tags = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'name', 'EventType', 'session_id', 'Optional[str]', 'action_surface', 'Optional[ActionSurfaceType]', 'source', 'Optional[SourceType]', 'amp_count', 'int', 'hive_extras', 'Optional[Dict[str, Any]]', 'amp_tags', 'Optional[Dict[str, str]]', 'return', 'None'): cls.report_oneoff_event_amp(metrics_reporter, account, name, source, amp_count, amp_tags)cls.report_oneoff_event_hive(account, name, session_id, action_surface, source, hive_extras))()
    report_ui_event = (lambda cls, metrics_reporter, account = None, event = None, session_id = classmethod, action_surface = (None, None), source = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'EventType', 'session_id', 'str', 'action_surface', 'Optional[ActionSurfaceType]', 'source', 'Optional[SourceType]', 'extra', 'Any', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()
    report_performance = (lambda cls, metrics_reporter, account, event, time, session_id = None, action_surface = None, source = classmethod, extra_tags = (None, None, None, None), additional_perf_events = ('metrics_reporter', 'MetricsReporter', 'account', 'Optional[AccountInterface]', 'event', 'EventType', 'time', 'timedelta', 'session_id', 'Optional[str]', 'action_surface', 'Optional[ActionSurfaceType]', 'source', 'Optional[SourceType]', 'extra_tags', 'Optional[Dict[str, str]]', 'additional_perf_events', 'Optional[Dict[str, timedelta]]', 'return', 'None'): cls.report_performance_amp(metrics_reporter, account, event, time, extra_tags, additional_perf_events)hive_extras = extra_tags if extra_tags else { }hive_extras['nopii_perf_timer_ms'] = str(time.total_seconds() * 1000)# WARNING: Decompyle incomplete
)()

BackupLogger = <NODE:27>(BackupLogger, 'BackupLogger', Generic[(EventType, EventLabelType, ActionSurfaceType, SourceType)])
