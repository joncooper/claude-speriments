# Source Generated with Decompyle++
# File: external_backup_logging.pyc (Python 3.11)

import random as insecure_random
from enum import auto, Enum, unique
from typing import Any, cast, Dict, Optional, Text
from apex.metrics import Metric, MetricsReporter
from build_number.platform import IS_WINDOWS
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.backup_logging import BackupLogger
from dropbox.client.features.backup_common.logging_helpers import common_account_tags, label_backup_event, non_pii_extras, quota_tags
from dropbox.client.features.external_drive_backup.constants import DA_ERROR_LOCATION_SAMPLE_MAP, DiskArbitrationErrorOrigin, NonFissionSetupReason
from dropbox.client.features.external_drive_backup.edb_instance_wrapper import EDBInstanceWrapper
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_action_surface import EdbActionSurface
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.edb_source import EdbSource
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.event_label import EventLabel
from dropbox.client.features.external_drive_backup.view_model.bridge_gen.external_backup_event import ExternalBackupEvent
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
if IS_WINDOWS:
    import pywintypes
_AMP_NAMESPACE = 'desktop_external_backup'
ExternalBackupResearchEvent = <NODE:12>()

def account_to_context(account = None, machine_context = None):
    account = cast(Account, account)
    user_context = None
    if machine_context:
        model = machine_context.account_manager.account_models.get(account)
        if model:
            user_context = model.user_context
    return user_context


def account_to_fission_tag(account = None, machine_context = None):
    
    try:
        if not account:
            return 'unknown'
        user_context = account_to_context(account, machine_context)
        if not user_context:
            return 'unknown'
        wrapper = destroying(EDBInstanceWrapper.from_context(user_context))
        if wrapper().backup_instance_exists():
            
            try:
                None(None, None)
                return 'True'
                
                try:
                    None(None, None)
                    return 'False'
                    with None:
                        if not None:
                            
                            try:
                                
                                try:
                                    return None
                                except Exception:
                                    report_exception(severity = Severity.WARN, component = DesktopComponent.SYNC_EVERYTHING)
                                    return 'unknown-error'







def _account_tags(account = None, machine_context = None):
    tags = common_account_tags(account)
    tags['active_backup_instance'] = account_to_fission_tag(account, machine_context)
    return tags


def _common_hive_tags(account = None):
    return { }


def _report_product_reserch_event(account, machine_context, event_name, volume_uuid, volume_fs_type, volume_capacity = None, volume_usage = None, sync_engine_build_number = None, extra_dict = ('account', 'Optional[AccountInterface]', 'machine_context', 'Optional[MachineContext]', 'event_name', 'str', 'volume_uuid', 'str', 'volume_fs_type', 'str', 'volume_capacity', 'int', 'volume_usage', 'int', 'sync_engine_build_number', 'Optional[str]', 'extra_dict', 'Any', 'return', 'None')):
    account_tags = _account_tags(account, machine_context)
    account_subscription = account_tags['account_subscription']
    account_tags.pop('account_subscription', None)
    sanitized_extra_dict = sanitize_event_extra_dict(extra_dict)
    sanitized_extra_dict.update(account_tags)
    quota_tags_ = quota_tags(account)
    report('external-drive-backup-drive-research-restricted', account = account, event_name = event_name, volume_uuid = volume_uuid, volume_fs_type = volume_fs_type, volume_capacity = volume_capacity, volume_usage = volume_usage, quota_percent = quota_tags_['quota_percent'], quota_bucket = quota_tags_['quota_bucket'], account_subscription = account_subscription, sync_engine_build_number = sync_engine_build_number, extra = sanitized_extra_dict)


def _report_anchor_state(account, machine_context, state_name, over_quota, sync_paused, was_fully_synced, volume_uuid, anchor_fileid, target_path, device_anchor_path = None, fs_type = None, sync_engine_build_number = None, extra_dict = ('account', 'AccountInterface', 'machine_context', 'Optional[MachineContext]', 'state_name', 'str', 'over_quota', 'bool', 'sync_paused', 'bool', 'was_fully_synced', 'bool', 'volume_uuid', 'Optional[Text]', 'anchor_fileid', 'Optional[str]', 'target_path', 'Optional[Text]', 'device_anchor_path', 'Optional[Text]', 'fs_type', 'Optional[Text]', 'sync_engine_build_number', 'Optional[str]', 'extra_dict', 'Any', 'return', 'None')):
    account_tags = _account_tags(account, machine_context)
    account_subscription = account_tags['account_subscription']
    account_tags.pop('account_subscription', None)
    sanitized_extra_dict = sanitize_event_extra_dict(extra_dict)
    sanitized_extra_dict.update(account_tags)
    quota_tags_ = quota_tags(account)
# WARNING: Decompyle incomplete


def _report_anchor_usage(account, device_anchor_fileid, remote_bytes, local_physical_bytes, local_online_bytes = None, local_file_count = None, is_backup_instance = None, sync_engine_build_number = ('account', 'AccountInterface', 'device_anchor_fileid', 'Text', 'remote_bytes', 'Optional[int]', 'local_physical_bytes', 'Optional[int]', 'local_online_bytes', 'Optional[int]', 'local_file_count', 'Optional[int]', 'is_backup_instance', 'bool', 'sync_engine_build_number', 'Optional[str]', 'return', 'None')):
    report('external-drive-backup-usage', account = account, device_anchor_fileid = device_anchor_fileid, remote_bytes = remote_bytes, local_physical_bytes = local_physical_bytes, local_online_bytes = local_online_bytes, local_file_count = local_file_count, is_backup_instance = is_backup_instance, sync_engine_build_number = sync_engine_build_number)


def _report_event(account, machine_context, event_name, session_id = None, action_surface = None, source = None, sync_engine_build_number = ('account', 'Optional[AccountInterface]', 'machine_context', 'Optional[MachineContext]', 'event_name', 'str', 'session_id', 'str', 'action_surface', 'Optional[str]', 'source', 'Optional[str]', 'sync_engine_build_number', 'Optional[str]', 'extras', 'Any', 'return', 'None'), **extras):
    account_tags = _account_tags(account, machine_context)
    account_role = account_tags['account_role']
    account_subscription = account_tags['account_subscription']
    account_tags.pop('account_role', None)
    account_tags.pop('account_subscription', None)
    quota_percent = quota_tags(account)['quota_percent']
    quota_bucket = quota_tags(account)['quota_bucket']
    no_pii_extras = sanitize_event_extra_dict(non_pii_extras(extras))
    no_pii_extras.update(_common_hive_tags(account))
    no_pii_extras.update(account_tags)
    report('external-drive-backup-events', account = account, event_name = event_name, session_id = session_id, action_surface = action_surface, source = source, quota_percent = quota_percent, quota_bucket = quota_bucket, account_role = account_role, account_subscription = account_subscription, sync_engine_build_number = sync_engine_build_number, extra = no_pii_extras)
    extra_dict = sanitize_event_extra_dict(extras)
    extra_dict.update(_common_hive_tags(account))
    extra_dict.update(account_tags)
    report('external-drive-backup-events-restricted', account = account, event_name = event_name, session_id = session_id, action_surface = action_surface, source = source, quota_percent = quota_percent, quota_bucket = quota_bucket, account_role = account_role, account_subscription = account_subscription, sync_engine_build_number = sync_engine_build_number, extra = extra_dict)


def ExternalBackupLogger():
    '''ExternalBackupLogger'''
    pass
# WARNING: Decompyle incomplete

ExternalBackupLogger = <NODE:27>(ExternalBackupLogger, 'ExternalBackupLogger', BackupLogger[(ExternalBackupEvent, EventLabel, EdbActionSurface, EdbSource)])
