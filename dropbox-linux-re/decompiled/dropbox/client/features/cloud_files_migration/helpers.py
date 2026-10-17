# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

import enum
import time
from pathlib import Path
from typing import cast, Optional
from build_number.features import feature_enabled
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.cloud_files_migration.constants import CLOUD_FILES_FILE_COUNT_LIMIT_STORMCROW, CLOUD_FILES_MIGRATION_START_TIME_CONFIG_KEY, FILE_COUNTS_STORMCROW_FALLBACK_VALUE, FILE_COUNTS_STORMCROW_UNLIMITED_VARIANT
from dropbox.client.features.cloud_files_migration.logger import CloudFilesMigrationEvent
from dropbox.client.features.cloud_files_migration.types import CloudFilesAccountMigrationState
from dropbox.client.features.file_provider_migration.helpers import get_num_files, get_num_files_per_account
from dropbox.client.gandalf import Gandalf
from dropbox.client.lib.stormcrow.constants import VARIANT_OFF
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.sync_root.events.reporter import report_sync_root_event
from dropbox.sync_root.events.types import ExtraInfo, SyncRootEvent, SyncRootEventType, SyncRootType
from dropbox.sync_root.gating import cloud_files_capable
from dropbox.trace import TRACE
STATE_TO_EVENT_MAP = {
    CloudFilesAccountMigrationState.OPTED_OUT: CloudFilesMigrationEvent.OPTED_OUT,
    CloudFilesAccountMigrationState.MARKED_NOT_ELIGIBLE: CloudFilesMigrationEvent.MARKED_NOT_ELIGIBLE,
    CloudFilesAccountMigrationState.COMPLETE: CloudFilesMigrationEvent.COMPLETE,
    CloudFilesAccountMigrationState.IN_PROGRESS: CloudFilesMigrationEvent.IN_PROGRESS,
    CloudFilesAccountMigrationState.ELIGIBLE: CloudFilesMigrationEvent.ELIGIBLE,
    CloudFilesAccountMigrationState.CHECK_ELIGIBILITY: CloudFilesMigrationEvent.CHECK_ELIGIBILITY }

def get_local_config(machine_context = None, account = None):
    if feature_enabled('multi-team-accounts-prod'):
        account_models = machine_context.account_manager.account_models_all
    else:
        account_models = machine_context.account_manager.account_models
    account = cast(Account, account)
    account_model = account_models.get(account)
# WARNING: Decompyle incomplete


def set_cf_migration_start_time(local_config = None):
    TRACE('[Cloud Files] Setting migration start time for migration')
    return local_config.update_preferences({
        CLOUD_FILES_MIGRATION_START_TIME_CONFIG_KEY: int(time.time()) })


def get_cf_migration_start_time(local_config = None):
    return local_config.config_dict.get(CLOUD_FILES_MIGRATION_START_TIME_CONFIG_KEY, -1)


def get_file_count_limit(account = None, gandalf = None):
    max_num_files_variant = gandalf.get_variant(CLOUD_FILES_FILE_COUNT_LIMIT_STORMCROW, account)
    TRACE('[Cloud Files] Checking file counts stormcrow variant for user. Variant: %s', max_num_files_variant)
    if max_num_files_variant == FILE_COUNTS_STORMCROW_UNLIMITED_VARIANT:
        return None
    file_count_limit = None
# WARNING: Decompyle incomplete


def within_file_count_limit(account = None, gandalf = None, machine_context = None):
    file_count_limit = get_file_count_limit(account, gandalf)
# WARNING: Decompyle incomplete


def state_to_logger_event(state = None):
    if state in STATE_TO_EVENT_MAP:
        return STATE_TO_EVENT_MAP[state]
    return None.INVALID_STATE_CONVERSION


def has_multiple_owners_for_same_path(dropbox_path = None):
    pass
# WARNING: Decompyle incomplete


def check_ancestors_reparse_tag_for_cloud_files(path = None):
    pass
# WARNING: Decompyle incomplete


def _report_one_drive_root_not_detected(path = None, is_cf_sync_root = None, has_cf_reparse_tag = None):
    report_sync_root_event(SyncRootEvent(sync_root_type = SyncRootType.CLOUD_FILES, event_type = SyncRootEventType.ONE_DRIVE_NOT_DETECTED, extra_info = ExtraInfo(mount_path = path, is_cf_sync_root = is_cf_sync_root, has_cf_reparse_tag = has_cf_reparse_tag)))


def _report_cf_invalid_function(path = None):
    report_sync_root_event(SyncRootEvent(sync_root_type = SyncRootType.CLOUD_FILES, event_type = SyncRootEventType.CF_INVALID_FUNCTION, extra_info = ExtraInfo(mount_path = path)))


def is_cf_sync_root_check(path = None):
