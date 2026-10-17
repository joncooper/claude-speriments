# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import Dict, List, Optional, Sequence, Set, Text
from build_number.features import feature_enabled
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.wrapper import MachineConfigurationWrapper
from dropbox.client.features.backup_common.config_utils import is_se_migration_active
from dropbox.client.features.backup_instance.gating import BackupInstanceFeature
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.computer_backup.constants import CB_ANCHORS_FEATURE_NAME
from dropbox.client.features.sync_everything.constants import ACTPA_SYNC_EVERYTHING_PLUS_TRIAL, BACKUP_APP_BASIC_OVERQUOTA_UPSELL, BACKUP_APP_SYNC_PROGRESS, BACKUP_ENABLE_TRIALS_CHECKOUT, BACKUP_NEW_ONBOARDING_EXP, BACKUP_ONBOARDING_CAROUSEL_BACKUP_SKU_REMOVAL, BACKUP_SKU_MODAL, BACKUP_TRAY_FISSION_KILLSWITCH, BACKUP_TRAY_SYNC_CB_PROGRESS, BACKUP_TRAY_SYNC_EDB_PROGRESS, CB_FORCED_MIGRATION, CB_FULL_MIGRATION, CB_HIDE_BETA_TAG, CB_MIGRATION_PROMPT, CB_SELF_SERVE_MIGRATION, CBOA_MIGRATION_UI_MAX_TIMES_TO_SHOW, CBOA_MIGRATION_UI_MAX_TIMES_TO_SHOW_DEFAULT, CBOA_MIGRATION_UI_NUM_DAYS_BETWEEN_DISMISSED, CBOA_MIGRATION_UI_NUM_DAYS_BETWEEN_DISMISSED_DEFAULT, FIRST_SYNC_L0_HIDDEN, MoreFoldersToastType, SYNC_EVERYTHING_ADOBE_LIBRARY_CHECK_KILL_SWITCH, SYNC_EVERYTHING_ALLOW_MERGE_NON_DEFAULT_LOCATION, SYNC_EVERYTHING_BACKUP_FORCE_DISABLE_MARK_OTHERS_KILLSWITCH, SYNC_EVERYTHING_BACKUP_FORCE_DISABLE_RECOVERY_KILLSWITCH, SYNC_EVERYTHING_CALCULATE_OVERQUOTA, SYNC_EVERYTHING_CANCEL_SUPPORT, SYNC_EVERYTHING_DISABLE_SURVEY_FEATURE_NAME, SYNC_EVERYTHING_FEATURE_OFF_VARIANTS, SYNC_EVERYTHING_FOLDERS_FEATURE_NAME, SYNC_EVERYTHING_FOLDERS_UX_EXPERIMENT, SYNC_EVERYTHING_HANDLE_ROLE_CHANGE_FEATURE_NAME, SYNC_EVERYTHING_IC_FULL_KILLSWITCH_NAME, SYNC_EVERYTHING_INVARIANT_ADD_IMMUTABLE, SYNC_EVERYTHING_INVARIANT_BACKUP_SKU_REMEDIATION_NAME, SYNC_EVERYTHING_INVARIANT_CLEAR_IMMUTABLE, SYNC_EVERYTHING_INVARIANT_INTERVAL, SYNC_EVERYTHING_INVARIANT_INTERVAL_DEFAULT, SYNC_EVERYTHING_METRICS_REPORT_INTERVAL, SYNC_EVERYTHING_METRICS_REPORT_INTERVAL_DEFAULT, SYNC_EVERYTHING_MORE_FOLDERS_TOAST_NAME, SYNC_EVERYTHING_ONBOARDING_FEATURE_NAME, SYNC_EVERYTHING_PERMANENT_HIDE_FEATURE, SYNC_EVERYTHING_PRODUCT_SURVEY_EMAIL_NAME, SYNC_EVERYTHING_RESET_PERMANENT_HIDE, SYNC_EVERYTHING_ROLE_CHANGE_AUTO_REBIND, SYNC_EVERYTHING_SCREENSHOTS_ENABLED, SYNC_EVERYTHING_SEV_OPALESCENT_ALABASTER_EGRET_DISABLE, SYNC_EVERYTHING_STICKY_FEATURE_NAME, SYNC_EVERYTHING_USAGE_REPORT_INTERVAL, SYNC_EVERYTHING_USAGE_REPORT_INTERVAL_DEFAULT
from dropbox.client.gandalf import Gandalf
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.stormcrow import NoStormcrowDataError
from dropbox.foundation.stormcrow.machine import MachineStormcrow
from dropbox.foundation.stormcrow.user import UserStormcrow
from dropbox.platform import IS_LINUX
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.trace import TRACE, WARNING
if IS_MAC:
    from dropbox.mac.version import HIGH_SIERRA, MAC_VERSION

def safe_get_variants_all_accounts(machine_stormcrow = None, feature = None):
    if not machine_stormcrow.is_ready:
        return []
    return None.get_variants_all_accounts(feature)


def safe_allows_any_account(machine_stormcrow = None, feature = None, default = None, treat_control_as_off = (False, False)):
    
    try:
        return machine_stormcrow.allows_any_account(feature, treat_control_as_off = treat_control_as_off)
    except NoStormcrowDataError:
        report_exception(severity = Severity.TRACE, component = DesktopComponent.SYNC_EVERYTHING)
        return 



class SyncEverythingFeature:
    forced_allowed_accounts: 'Set[AccountInterface]' = set()
    forced_allowed_screenshots_in_se: 'Set[AccountInterface]' = set()
    cached_team_policy: 'Dict[AccountInterface, bool]' = dict()
    is_enabled = (lambda : not IS_LINUX)()
    add_to_force_allowed = (lambda account = None: SyncEverythingFeature.forced_allowed_accounts.add(account))()
    set_cached_team_policy = (lambda account = None, is_enabled = None: SyncEverythingFeature.cached_team_policy[account] = is_enabled)()
    _is_on_variant = (lambda variants = None: if not variants:
False# WARNING: Decompyle incomplete
)()
    allowed_for_user = (lambda user_context = None: 