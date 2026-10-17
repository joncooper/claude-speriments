# Source Generated with Decompyle++
# File: backup_instance_logging.pyc (Python 3.11)

from typing import Any, Dict, Optional
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.backup_logging import BackupLogger
from dropbox.client.features.backup_common.logging_helpers import common_account_tags, label_backup_event, quota_tags
from dropbox.client.features.backup_instance.types import BackupInstanceActionSurface, BackupInstanceEvent, BackupInstanceEventLabel
from dropbox.event import report, sanitize_event_extra_dict
_AMP_NAMESPACE = 'desktop_backup_instance'

def _common_hive_tags(account = None):
    return { }


def _report_event(account = None, event_name = None, session_id = None, sync_engine_build_number = ('account', 'Optional[AccountInterface]', 'event_name', 'str', 'session_id', 'str', 'sync_engine_build_number', 'Optional[str]', 'extras', 'Any', 'return', 'None'), **extras):
    account_role = common_account_tags(account)['account_role']
    account_subscription = common_account_tags(account)['account_subscription']
    quota_percent = quota_tags(account)['quota_percent']
    quota_bucket = quota_tags(account)['quota_bucket']
    extra_dict = sanitize_event_extra_dict(extras)
    extra_dict.update(_common_hive_tags(account))
    report('backup-instance-events-restricted', account = account, event_name = event_name, session_id = session_id, quota_percent = quota_percent, quota_bucket = quota_bucket, account_role = account_role, account_subscription = account_subscription, sync_engine_build_number = sync_engine_build_number, extra = extra_dict)


def BackupInstanceLogger():
    '''BackupInstanceLogger'''
    get_amp_namespace = (lambda cls = None: _AMP_NAMESPACE)()
    report_event = (lambda cls, account, event_name = None, session_id = None, event_label = classmethod, action_surface = (None, None, None), source = ('account', 'Optional[AccountInterface]', 'event_name', 'BackupInstanceEvent', 'session_id', 'Optional[str]', 'event_label', 'Optional[str]', 'action_surface', 'Optional[BackupInstanceActionSurface]', 'source', 'Optional[None]', 'extras', 'Any', 'return', 'None'): pass# WARNING: Decompyle incomplete
)()

BackupInstanceLogger = <NODE:27>(BackupInstanceLogger, 'BackupInstanceLogger', BackupLogger[(BackupInstanceEvent, BackupInstanceEventLabel, BackupInstanceActionSurface, None)])
