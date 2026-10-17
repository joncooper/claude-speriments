# Source Generated with Decompyle++
# File: helpers.pyc (Python 3.11)

import json
import os
from typing import Dict, List, Mapping, Optional, Set, Text, Tuple
import psutil
from build_number import BUILD_KEY
from dropbox import fsutil
from dropbox.client.authentication.account import Account
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.authentication.interface import AccountManagerInterface
from dropbox.client.configuration.interface import ConfigurationManagerInterface, LocalConfigurationInterface
from dropbox.client.features.file_provider_migration.constants import FILE_COUNTS_STORMCROW_UNLIMITED_VARIANT, FILE_PROVIDER_MIGRATION_BETA_EXITED_FROM_MOUNTED, FILE_PROVIDER_MIGRATION_EXTERNAL_DRIVE_STORMCROW, FILE_PROVIDER_MIGRATION_HIDDEN_SET_CONFIG_KEY
from dropbox.client.features.file_provider_migration.state_machine import ReadOnlyStateMachine
from dropbox.client.lib.stormcrow.constants import VARIANT_OFF
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.account_manager.account_model import AccountModel
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.fsutil import FileSystem
from dropbox.i18n import format_time_interval
from dropbox.model.types import FileId
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_engine_boundary.file_system_exceptions import FileSystemError
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_root.fp_external_drive import check_fp_external_drive_eligibility, FP_EXTERNAL_DRIVE_STORMCROW, is_account_fp_external_drive_eligible
from dropbox.sync_root.interface import SyncRootManagerInterface
from dropbox.sync_root.types import SyncRootType
from dropbox.trace import TRACE
LINKED_ACCOUNTS_SYNCED_TIMEOUT_SECONDS = 45

def take_fp_migration_preserved_hidden_set(local_config = None):
    if local_config.config_dict or FILE_PROVIDER_MIGRATION_HIDDEN_SET_CONFIG_KEY in { }:
        
        try:
            hidden_set_to_restore = json.loads(local_config.config_dict[FILE_PROVIDER_MIGRATION_HIDDEN_SET_CONFIG_KEY])
            TRACE('Preserved FP migration hidden set taken: %r', hidden_set_to_restore)
            del local_config.config_dict[FILE_PROVIDER_MIGRATION_HIDDEN_SET_CONFIG_KEY]
            return set(hidden_set_to_restore)
        except json.JSONDecodeError:
            report_exception(severity = Severity.CRITICAL, component = DesktopComponent.FILE_PROVIDER)
            
            try:
                del local_config.config_dict[FILE_PROVIDER_MIGRATION_HIDDEN_SET_CONFIG_KEY]
                return None
                
                try:
                    pass
                except:
                    del local_config.config_dict[FILE_PROVIDER_MIGRATION_HIDDEN_SET_CONFIG_KEY]
                    return None





def is_path_on_eligible_volume(file_system = None, stormcrow = None, root_mount_path = None):
    
    try:
        if fsutil.is_path_on_home_volume(file_system, root_mount_path):
            return (True, None)
    except FileSystemError:
        return (False, None)
        if not stormcrow.allows(FILE_PROVIDER_MIGRATION_EXTERNAL_DRIVE_STORMCROW):
            TRACE('[FPMigration] External drive: migration stormcrow is off')
            return (False, None)
        if not is_account_fp_external_drive_eligible(stormcrow.get_variant(FP_EXTERNAL_DRIVE_STORMCROW)):
            TRACE('[FPMigration] External drive: account not eligible')
            return (False, None)
        
        try:
            eligibility_info = check_fp_external_drive_eligibility(root_mount_path)
        except Exception:
            e = None
            TRACE('[FPMigration] External drive: error check drive eligibility error=%r', e)
            e = None
            del e
            return (False, None)
            e = None
            del e

        if not eligibility_info.is_eligible:
            TRACE('[FPMigration] External drive: drive is not eligible reason=%r', eligibility_info.unsupported_reason)
        return (eligibility_info.is_eligible, eligibility_info.unsupported_reason)



def get_fp_storage_locations(account_manager = None, machine_context = None):
    pass
# WARNING: Decompyle incomplete


def get_num_files(user_context = None):
    nucleus_wrapper = destroying(NucleusWrapper.from_context(user_context))
    None(None, None)
    return 
    with None:
        if not None, nucleus_wrapper().get_bugreporter_stats().then((lambda bug_reporter_stats: ResolvedFuture(parse_bug_reporter_stats(bug_reporter_stats)))):
            pass


def get_num_files_per_account(machine_context = None):
    context_to_num_files_fut = { }
    TRACE('get_num_files_per_account for accounts: %r', machine_context.account_manager.account_models.keys())
    for account_model in machine_context.account_manager.account_models.values():
        user_context = account_model.user_context
        context_to_num_files_fut[user_context.account] = get_num_files(user_context)
        return Future.all_mapping(context_to_num_files_fut)


def get_total_num_files_in_dbx(domain_to_num_files = None):
    total_num_files = 0
    for num_files_as_str in domain_to_num_files.values():
        if num_files_as_str:
            total_num_files += int(num_files_as_str)
        return total_num_files


def get_time_estimate(machine_context = None):
    context_to_time_estimate_fut = { }
    for account_model in machine_context.account_manager.account_models.values():
        user_context = account_model.user_context
        nucleus_wrapper = destroying(NucleusWrapper.from_context(user_context))
        fut = nucleus_wrapper().estimate_fp_migration_duration()
        context_to_time_estimate_fut[user_context.account] = fut
        None(None, None)
    with None:
        if not None:
            pass
    continue
    return Future.all_mapping(context_to_time_estimate_fut)


def get_total_time_estimate(domain_to_minutes = None):
    total_time_in_minutes = 0
    for minutes in domain_to_minutes.values():
        total_time_in_minutes += minutes
        return total_time_in_minutes


def get_formatted_time_estimate(total_time_in_minutes = None):
    minimum_minutes_to_display = 5
    total_time_in_minutes = max(minimum_minutes_to_display, total_time_in_minutes)
    total_time_in_seconds = total_time_in_minutes * 60
    return format_time_interval(total_time_in_seconds)


def parse_bug_reporter_stats(bug_reporter_stats = None):
    if bug_reporter_stats[0][0] != 'Tree sizes':
        report_bad_assumption('[FP Migration] bug reporter stats return has changed! Cannot get number of local files for logging')
        return None
    return None[0][1].split(': ')[1].split(',')[0]


def get_linked_accounts_to_synced(account_models = None):
    pass
# WARNING: Decompyle incomplete


def battery_too_low_for_migration():
    battery_info = psutil.sensors_battery()
    if battery_info:
        battery_percent = battery_info[0]
        plugged_in = battery_info[2]
        if not battery_percent < 10 and plugged_in:
            TRACE('[FP Migration] Battery power too low for migration, battery percentage: %r', battery_percent)
            return True
    TRACE('[FP Migration] Failed to get battery info')
    return False


def should_initialize_fp_migration_controller(config_manager = None, root_manager = None, account = None):
