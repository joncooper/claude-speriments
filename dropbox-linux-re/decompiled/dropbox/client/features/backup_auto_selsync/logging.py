# Source Generated with Decompyle++
# File: logging.pyc (Python 3.11)

from typing import Any, Callable, Dict, Optional, TypeVar
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_auto_selsync.types import BackupAutoSelSyncEvent, BackupAutoSelSyncEventLabel
from dropbox.client.features.backup_common.backup_logging import BackupLogger
from dropbox.client.features.backup_common.logging_helpers import common_account_tags, label_backup_event, quota_tags
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import ResolvedFuture
_AMP_NAMESPACE = 'desktop_backup_auto_selsync'
_DefaultType = TypeVar('_DefaultType')
_ReportHandler = Callable[([
    Exception,
    ExcInfo], ResolvedFuture[_DefaultType])]

def _common_hive_tags(account = None):
    return { }


def _report_event(account = None, event_name = None, session_id = None, sync_engine_build_number = (None,), action_surface = ('account', 'Optional[AccountInterface]', 'event_name', 'str', 'session_id', 'str', 'sync_engine_build_number', 'Optional[str]', 'action_surface', 'Optional[str]', 'extras', 'Any', 'return', 'None'), **extras):
    account_role = common_account_tags(account)['account_role']
    account_subscription = common_account_tags(account)['account_subscription']
    quota_percent = quota_tags(account)['quota_percent']
    quota_bucket = quota_tags(account)['quota_bucket']
    extra_dict = sanitize_event_extra_dict(extras)
    extra_dict.update(_common_hive_tags(account))
    report('backup-auto-selsync-events-restricted', account = account, event_name = event_name, session_id = session_id, action_surface = action_surface, quota_percent = quota_percent, quota_bucket = quota_bucket, account_role = account_role, account_subscription = account_subscription, sync_engine_build_number = sync_engine_build_number, extra = extra_dict)

report_exception_and_ignore = (lambda report_severity = None, default = None: pass# WARNING: Decompyle incomplete
)()

def AutoSelSyncLogger():
    '''AutoSelSyncLogger'''
    get_amp_namespace = (lambda cls = None: _AMP_NAMESPACE)()
    report_event = (lambda cls, account, event_name = None, session_id = None, event_label = classmethod, action_surface = (None, None, None), source = ('account', 'Optional[AccountInterface]', 'event_name', 'BackupAutoSelSyncEvent', 'session_id', 'Optional[str]', 'event_label', 'Optional[str]', 'action_surface', 'Optional[None]', 'source', 'Optional[None]', 'extras', 'Any', 'return', 'None'): sync_engine_build_number = cls.get_backup_engine_version(account) if account else None# WARNING: Decompyle incomplete
)()

AutoSelSyncLogger = <NODE:27>(AutoSelSyncLogger, 'AutoSelSyncLogger', BackupLogger[(BackupAutoSelSyncEvent, BackupAutoSelSyncEventLabel, None, None)])
