# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Dict, Optional, Sequence, Set, Text
from build_number.features import feature_enabled
from build_number.platform import IS_LINUX
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.computer_backup.constants import CB_ALLOW_BREAK_ANCHOR_ON_ONE_WAY_SYNC_REMEDIATION, CB_ALLOW_GOOGLEDRIVE, CB_ALLOW_ICLOUD, CB_ALLOW_ONEDRIVE, CB_ALLOW_RELINK_ON_START_UP_FEATURE_NAME, CB_ANCHORS_FEATURE_NAME, CB_BREAK_ANCHORS_KILL_SWITCH_NAME, CB_CANCEL_SUPPORT, CB_CHECK_MIXED_BACKUPS, CB_CUSTOM_FOLDERS_ANCHOR_LIMIT, CB_CUSTOM_FOLDERS_ANCHOR_LIMIT_DEFAULT, CB_CUSTOM_FOLDERS_SELECTOR, CB_FEATURE_OFF_VARIANTS, CB_PERIODIC_BACKUP_INTERVAL_MINUTES, CB_PERIODIC_BACKUP_INTERVAL_MINUTES_DEFAULT, CB_RELINK_KILL_SWITCH_NAME, CB_RESTORE_IN_ROOT, CB_RESUME_ANCHORS_ON_RELINK_KILLSWITCH, CB_SCHEDULED_BACKUP_POLLING_INTERVAL_MINUTES, CB_SCHEDULED_BACKUP_POLLING_INTERVAL_MINUTES_DEFAULT, CB_SEV_LAZY_CELESTE_WOODPECKER_NAME, CB_SYNC_PROGRESS_UPDATES, CB_USAGE_REPORT_INTERVAL, CB_USAGE_REPORT_INTERVAL_HOURS_DEFAULT
from dropbox.client.features.computer_backup.trace import CB_TRACE, CB_WARN
from dropbox.client.features.sync_everything.constants import SYNC_EVERYTHING_ONBOARDING_FEATURE_NAME
from dropbox.client.features.sync_everything.gating import safe_get_variants_all_accounts, SyncEverythingFeature
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext

class ComputerBackupFeature:
    force_allowed_accounts: 'Set[AccountInterface]' = set()
    custom_folders_force_allowed_accounts: 'Set[AccountInterface]' = set()
    cached_team_policy: 'Dict[AccountInterface, bool]' = { }
    set_cached_team_policy = (lambda account = None, is_enabled = None: ComputerBackupFeature.cached_team_policy[account] = is_enabled)()
    _get_interval = (lambda machine_context = None, feature_name = None, default_value = staticmethod: pass# WARNING: Decompyle incomplete
)()
    is_enabled = (lambda : if IS_LINUX:
Falsefeature_enabled(CB_ANCHORS_FEATURE_NAME))()
    add_to_force_allowed = (lambda account = None: CB_TRACE('Forcing account %r into CBoA', None, account)ComputerBackupFeature.force_allowed_accounts.add(account))()
    add_to_custom_folders_force_allowed = (lambda account = None: CB_TRACE('Forcing account %r into Custom folders allowed', None, account)ComputerBackupFeature.custom_folders_force_allowed_accounts.add(account))()
    is_on_variant = (lambda variants = None: if not variants:
False# WARNING: Decompyle incomplete
)()
    is_anchors_enabled_for_user = (lambda user_context = None, check_team_policy = None: account = user_context.accountif account in ComputerBackupFeature.force_allowed_accounts:
True# WARNING: Decompyle incomplete
)()
    is_anchors_enabled_for_all_users = (lambda machine_context = None, check_team_policy = None: for account_model in machine_context.account_manager.account_models.values():
if not ComputerBackupFeature.is_anchors_enabled_for_user(account_model.user_context, check_team_policy):
FalseTrue)()
    is_anchors_enabled_for_any_user = (lambda machine_context = None: account_models = machine_context.account_manager.account_models.values()(lambda .0: pass# WARNING: Decompyle incomplete
)(account_models())
)()
    is_migration_enabled_for_user = (lambda user_context = None: SyncEverythingFeature.is_cb_full_migration_enabled(user_context.stormcrow))()
    is_migration_enabled_for_any_user = (lambda machine_context = None: account_models = machine_context.account_manager.account_models.values()(lambda .0: pass# WARNING: Decompyle incomplete
)(account_models())
)()
    get_cb_periodic_backup_interval_seconds = (lambda machine_context = None: ComputerBackupFeature._get_interval(machine_context, CB_PERIODIC_BACKUP_INTERVAL_MINUTES, CB_PERIODIC_BACKUP_INTERVAL_MINUTES_DEFAULT) * 60)()
    get_cb_scheduled_backup_polling_interval = (lambda machine_context = None: ComputerBackupFeature._get_interval(machine_context, CB_SCHEDULED_BACKUP_POLLING_INTERVAL_MINUTES, CB_SCHEDULED_BACKUP_POLLING_INTERVAL_MINUTES_DEFAULT) * 60)()
    get_cb_usage_reporting_interval = (lambda machine_context = None: ComputerBackupFeature._get_interval(machine_context, CB_USAGE_REPORT_INTERVAL, CB_USAGE_REPORT_INTERVAL_HOURS_DEFAULT) * 60 * 60)()
    should_be_forced_active = (lambda machine_context = None, account = None: if not ComputerBackupFeature.is_enabled():
Falseif not None.primary_account_config:
FalseNone.primary_account_config.computer_backup_active_account_id == account.account_id)()
    should_allow_onedrive = (lambda user_context = None: ComputerBackupFeature.is_on_variant([
user_context.stormcrow.get_variant(CB_ALLOW_ONEDRIVE)]))()
    should_allow_google_drive = (lambda user_context = None: ComputerBackupFeature.is_on_variant([
user_context.stormcrow.get_variant(CB_ALLOW_GOOGLEDRIVE)]))()
    should_allow_icloud = (lambda user_context = None: ComputerBackupFeature.is_on_variant([
user_context.stormcrow.get_variant(CB_ALLOW_ICLOUD)]))()
    should_allow_mixed_implementation_check = (lambda user_context = None: ComputerBackupFeature.is_on_variant([
user_context.stormcrow.get_variant(CB_CHECK_MIXED_BACKUPS)]))()
    should_allow_sync_progress_updates = (lambda user_context = None: ComputerBackupFeature.is_on_variant([
user_context.stormcrow.get_variant(CB_SYNC_PROGRESS_UPDATES)]))()
    should_restore_backup_in_root = (lambda user_context = None: ComputerBackupFeature.is_on_variant([
user_context.stormcrow.get_variant(CB_RESTORE_IN_ROOT)]))()
    is_custom_folders_selector_enabled_for_user = (lambda user_context = None: 