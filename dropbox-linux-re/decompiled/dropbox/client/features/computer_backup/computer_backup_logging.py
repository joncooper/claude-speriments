# Source Generated with Decompyle++
# File: computer_backup_logging.pyc (Python 3.11)

from typing import Any, Dict, Optional, Text
from apex.metrics import MetricsReporter
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_common.backup_logging import BackupLogger
from dropbox.client.features.backup_common.logging_helpers import common_account_tags, convert_folder_id_to_nopii_name, label_backup_event, non_pii_extras, quota_tags
from dropbox.client.features.computer_backup.cb_migration_state import ComputerBackupMigrationState
from dropbox.client.features.computer_backup.constants import CBFolderId, ComputerBackupUsage
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event import ComputerBackupEvent
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_event_label import ComputerBackupEventLabel
from dropbox.client.features.computer_backup.view_model.bridge_gen.computer_backup_suppression_reason import ComputerBackupSuppressionReason
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingUnlinkType
from dropbox.client.features.sync_everything.view_model.bridge_gen.action_surface import ActionSurface
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.source import Source
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.foundation.context.machine import MachineContext
_AMP_NAMESPACE = 'desktop_computer_backup'

def _report_event(account, event, session_id = None, action_surface = None, source = None, sync_engine_build_number = ('account', 'Optional[AccountInterface]', 'event', 'str', 'session_id', 'str', 'action_surface', 'Optional[str]', 'source', 'Optional[str]', 'sync_engine_build_number', 'Optional[str]', 'extra_dict', 'Any'), **extra_dict):
    account_tags = common_account_tags(account)
    quota_tags_ = quota_tags(account)
    no_pii_extras = sanitize_event_extra_dict(non_pii_extras(extra_dict))
    report('computer-backup-events', account = account, event = event, session_id = session_id, action_surface = action_surface, source = source, quota_percent = quota_tags_['quota_percent'], quota_bucket = quota_tags_['quota_bucket'], account_subscription = account_tags['account_subscription'], account_role = account_tags['account_role'], sync_engine_build_number = sync_engine_build_number, extra = no_pii_extras)
    extra_dict = sanitize_event_extra_dict(extra_dict)
    report('computer-backup-events-restricted', account = account, event = event, session_id = session_id, action_surface = action_surface, source = source, quota_percent = quota_tags_['quota_percent'], quota_bucket = quota_tags_['quota_bucket'], account_subscription = account_tags['account_subscription'], account_role = account_tags['account_role'], sync_engine_build_number = sync_engine_build_number, extra = extra_dict)


def _report_anchor_state(account, state_name, over_quota, sync_paused, was_fully_synced, anchor_fileid, target_path = None, device_anchor_path = None, sync_engine_build_number = None, extra_dict = ('account', 'AccountInterface', 'state_name', 'str', 'over_quota', 'bool', 'sync_paused', 'bool', 'was_fully_synced', 'bool', 'anchor_fileid', 'Optional[str]', 'target_path', 'Optional[Text]', 'device_anchor_path', 'Optional[Text]', 'sync_engine_build_number', 'Optional[str]', 'extra_dict', 'Any', 'return', 'None')):
    sanitized_extra_dict = sanitize_event_extra_dict(extra_dict)
    account_tags = common_account_tags(account)
    quota_tags_ = quota_tags(account)
    report('computer-backup-anchor-state-restricted', account = account, state_name = state_name, over_quota = over_quota, sync_paused = sync_paused, was_fully_synced = was_fully_synced, anchor_fileid = anchor_fileid, target_path = target_path, device_anchor_path = device_anchor_path, quota_percent = quota_tags_['quota_percent'], quota_bucket = quota_tags_['quota_bucket'], account_subscription = account_tags['account_subscription'], account_role = account_tags['account_role'], sync_engine_build_number = sync_engine_build_number, extra = sanitized_extra_dict)


def ComputerBackupLogger():
    '''ComputerBackupLogger'''
    pass
# WARNING: Decompyle incomplete

ComputerBackupLogger = <NODE:27>(ComputerBackupLogger, 'ComputerBackupLogger', BackupLogger[(ComputerBackupEvent, ComputerBackupEventLabel, ActionSurface, Source)])
