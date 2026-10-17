# Source Generated with Decompyle++
# File: logging_helpers.pyc (Python 3.11)

from enum import Enum
from typing import Any, Dict, Optional, Union
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.linked_host_telemetry import has_mti_team_accounts_tag, linked_host_count_tag
from dropbox.client.features.computer_backup.constants import CB_CUSTOM_FOLDER_NAME, CB_CUSTOM_FOLDER_VALUE, CBFolderId
from dropbox.client.multiaccount.role import Roles
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.machine import MachineContext
from dropbox.sync_engine_boundary.constants import OSFolderID
MYPY = False
if MYPY:
    from dropbox.client.features.backup_common.backup_logging import EventLabelType, EventType

def bucket_quota_percent(quota_percent = None):
    buckets = [
        10,
        50,
        80,
        90,
        95,
        100]
    if quota_percent < buckets[0]:
        return '0-{}'.format(buckets[0])
    if None >= buckets[-1]:
        return '{}+'.format(buckets[-1])
    for i in range(0, len(buckets) - 1):
        lower = buckets[i]
        upper = buckets[i + 1]
        if  <= lower, quota_percent or lower, quota_percent < upper:
            pass
        
        
        return None, '{}-{}'.format(lower, upper)
        report_bad_assumption("couldn't bucket quota")
        return 'error'


def non_pii_extras(extras = None):
    no_pii_extras = { }
    for k, v in extras.items():
        if k.startswith('nopii_'):
            new_key = k[len('nopii_'):]
            no_pii_extras[new_key] = v
        return no_pii_extras


def amp_tag_extras(extras = None):
    amp_tags = { }
    for k, v in extras.items():
        if k.startswith('amptag_'):
            new_key = k[len('amptag_'):]
            amp_tags[new_key] = str(v)
        return amp_tags


def common_account_tags(account = None):
    if account:
        role = 'unknown'
        
        try:
            role = Roles.to_str(account.role) if account.role else 'unknown'
        except Exception:
            pass

        subscription_type = account.subscription_type if account.subscription_type else 'unknown'
    else:
        role = 'unknown'
        subscription_type = 'unknown'
    tags = {
        'account_role': role,
        'account_subscription': subscription_type }
    tags.update(linked_host_count_tag())
    tags.update(has_mti_team_accounts_tag())
    return tags


def quota_tags(account = None):
    if account and account.quota_info:
        quota_percent = int(account.quota_info.home_usage_percentage())
        quota_percent_str = str(quota_percent)
        quota_bucket = bucket_quota_percent(quota_percent)
    else:
        quota_percent_str = 'unknown'
        quota_bucket = 'unknown'
    return {
        'quota_percent': quota_percent_str,
        'quota_bucket': quota_bucket }


def nameify(val = None):
    if isinstance(val, str):
        return val.lower()
    return None.name.lower()


def label_backup_event(event_name = None, label = None):
    name = nameify(event_name)
    if label:
        return '{}_{}'.format(name, nameify(label))


def _get_primary(machine_context = None):
    for account in machine_context.account_manager.linked_accounts:
        if account.is_primary:
            
            return None, account
        return None


def try_get_host_id(account = None, machine_context = None):
    host_id = None
    if account:
        host_id = account.host_int
    if host_id and machine_context:
        primary_account = _get_primary(machine_context)
        if primary_account:
            host_id = primary_account.host_int
    return host_id


def convert_folder_id_to_nopii_name(folder_id = None):
    return folder_id.name if isinstance(folder_id, OSFolderID) else CB_CUSTOM_FOLDER_NAME


def convert_folder_id_to_nopii_value(folder_id = None):
    return folder_id.value if isinstance(folder_id, OSFolderID) else CB_CUSTOM_FOLDER_VALUE

