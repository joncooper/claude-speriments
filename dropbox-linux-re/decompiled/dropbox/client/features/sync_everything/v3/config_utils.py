# Source Generated with Decompyle++
# File: config_utils.pyc (Python 3.11)

from typing import Dict, Optional
from apex.metrics import MetricsReporter
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.sync_everything.constants import CONFIG_KEY_SYNC_EVERYTHING_ACTIVE_ACCOUNT_ID, CONFIG_KEY_SYNC_EVERYTHING_DEVICE_STATE, CONFIG_KEY_SYNC_EVERYTHING_PROMPT_REBIND_ACCOUNT_ID, CONFIG_KEY_SYNC_EVERYTHING_RAW_CDM_MIGRATION_ACCOUNT_ID, CONFIG_KEY_SYNC_EVERYTHING_RESTORE_FROM_LOCAL_DISABLE, DeviceStatus
from dropbox.client.features.sync_everything.gating import SyncEverythingFeature
from dropbox.client.features.sync_everything.v3.nodep_utils import SE_TRACE
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingErrorName, SyncEverythingLogger
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.machine import MachineContext
MYPY = False
if MYPY:
    from dropbox.client.features.sync_everything.v3.device_state import DeviceState, KnownFolder
    from dropbox.sync_engine_boundary.constants import OSFolderID

def se_is_active_account(machine_context = None, account = None):
    if not machine_context.primary_account_config:
        return False
    return None.primary_account_config.sync_everything_active_account_id == account.account_id


def se_is_active(machine_context = None, account = None):
    if not SyncEverythingFeature.is_enabled():
        return False
    for model in None.account_manager.account_models.values():
        if not model.user_context.account == account and SyncEverythingFeature.allowed_for_user(model.user_context):
            return False
        return se_is_active_account(machine_context, account)


def se_active_device_name(machine_context = None, account = None, suppress_bad_assumption = None):
    if not se_is_active(machine_context, account):
        return None
    if not None.primary_account_config:
        return None
    device_state = None.primary_account_config.sync_everything_device_state
    if device_state or device_state.status == DeviceStatus.DISABLED:
        if not suppress_bad_assumption:
            report_bad_assumption('Active device found in local config, but no enabled state in LC', full_stack = True)
        else:
            SE_TRACE('Active device found in local config, but no enabled state in LC', None)
        return None
    return None.name


def se_pending_device_name(machine_context = None, account = None):
    if not se_is_active(machine_context, account):
        return None
    if not None.primary_account_config:
        return None
    device_state = None.primary_account_config.sync_everything_pending_device_state
    if device_state or device_state.status == DeviceStatus.DISABLED:
        SE_TRACE('no pending device name for account %r', None, account)
        return None
    return None.name


def se_active_device_folders(machine_context = None, account = None):
    if not se_is_active(machine_context, account):
        return { }
    if not None.primary_account_config:
        return { }
    device_state = None.primary_account_config.sync_everything_device_state
    if device_state or device_state.status == DeviceStatus.DISABLED:
        report_bad_assumption('Active device found in local config, but no enabled state in LC', full_stack = True)
        return { }
    return None.folders.copy()


def se_active_device_state_raw(primary_config = None, account = None):
    active_account_id = primary_config[CONFIG_KEY_SYNC_EVERYTHING_ACTIVE_ACCOUNT_ID]
    if active_account_id or active_account_id != account.account_id:
        SE_TRACE('account does not match enabled account; %r vs %r', None, account, active_account_id)
        return None
    device_state = None[CONFIG_KEY_SYNC_EVERYTHING_DEVICE_STATE]
    if device_state or device_state.status == DeviceStatus.DISABLED:
        report_bad_assumption('Active device found in local config, but no enabled state in LC', full_stack = True)
        return None
    return None.clone()


def write_sync_everything_cdm_flag_if_needed(primary_config = None, account = None, metrics_reporter = None):
    legacy_local_disable_value = primary_config[CONFIG_KEY_SYNC_EVERYTHING_RESTORE_FROM_LOCAL_DISABLE]
    prompt_rebind_value = primary_config[CONFIG_KEY_SYNC_EVERYTHING_PROMPT_REBIND_ACCOUNT_ID]
    if not legacy_local_disable_value is True:
        manager_handled = prompt_rebind_value == account.account_id
        if manager_handled:
            SE_TRACE('manager already handled migration, skipping. legacy_local_disable=%r, prompt_rebind=%r', None, legacy_local_disable_value, prompt_rebind_value)
            return None
        if None[CONFIG_KEY_SYNC_EVERYTHING_RAW_CDM_MIGRATION_ACCOUNT_ID] == account.account_id:
            SE_TRACE('raw CDM migration flag already written for account, skipping', None)
            return None
        active_account_id = None[CONFIG_KEY_SYNC_EVERYTHING_ACTIVE_ACCOUNT_ID]
        if active_account_id or active_account_id != account.account_id:
            return None
        if None:
            SyncEverythingLogger.report_error_count_incl_hive(metrics_reporter, account, SyncEverythingErrorName.raw_cdm_migration_flag_written)
        else:
            SyncEverythingLogger.report_event(account, SyncEverythingErrorName.raw_cdm_migration_flag_written.name, None)
    SE_TRACE('writing %r to raw cdm migration key', None, account.account_id)
    primary_config.config_dict[CONFIG_KEY_SYNC_EVERYTHING_RAW_CDM_MIGRATION_ACCOUNT_ID] = account.account_id

