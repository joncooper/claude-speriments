# Source Generated with Decompyle++
# File: gating.pyc (Python 3.11)

from typing import cast, Dict, List, Optional, Sequence, Set, Text, Tuple
from build_number.features import feature_enabled
from build_number.platform import IS_LINUX, IS_MAC, IS_WINDOWS
from backup_instance.gating import BackupInstanceFeature
from backup_instance.utils import is_regular_engine_on_fp
from sync_everything.gating import safe_get_variants_all_accounts
from constants import EBD_QUOTA_EXEMPT_IC_NO_OP, EDB_CAROUSEL_UPSELL_FEATURE_NAME, EDB_CONTEXT_MENU_KILL_SWITCH_NAME, EDB_CUSTOM_FOLDERS_FEATURE_NAME, EDB_DA_DEFAULT_MIN_CAPACITY, EDB_DA_EVENT_EARLY_SUPPRESS_NAME, EDB_DA_MIN_CAPACITY_NAME, EDB_DA_RATELIMIT_DEFAULT_MAX, EDB_DA_RATELIMIT_MAX_EVENT_NAME, EDB_DBXIGNORE_FEATURE_NAME, EDB_DELAY_FULL_DRIVE_OVERQUOTA_CHECK, EDB_DISK_ARBITRATION_FEATURE_FLAG, EDB_DISK_ARBITRATION_USER_STORMCROW_NAME, EDB_EVENT_ONBOARDING_EARLY_SUPPRESS_SEC_DEFAULT, EDB_EVENT_ONBOARDING_FEATURE_NAME, EDB_EVENT_ONBOARDING_MAX_PROMPTS_NAME, EDB_EVENT_ONBOARDING_MAX_USAGE_NAME, EDB_EVENT_ONBOARDING_MIN_CAPACITY_NAME, EDB_EXFAT_FILESYSTEM_SUPPORT_ENABLED, EDB_FAT_FILESYSTEM_SUPPORT_ENABLED, EDB_FEATURE_NAME, EDB_FEATURE_OFF_VARIANTS, EDB_FISSION_MIGRATION_ALLOWED_NAME, EDB_FISSION_MIGRATION_DISK_PERC_THRESHOLD_DEFAULT, EDB_FISSION_MIGRATION_DISK_PERC_THRESHOLD_NAME, EDB_FISSION_MIGRATION_MAX_NUM_BACKUPS_NAME, EDB_FISSION_MIGRATION_SCHEDULE_INTERVAL_NAME, EDB_FISSION_MIGRATION_VMEM_PERC_THRESHOLD_DEFAULT, EDB_FISSION_MIGRATION_VMEM_PERC_THRESHOLD_NAME, EDB_FP_MIGRATION_ALLOWED_NAME, EDB_FP_MIGRATION_PREFER_BASIC_FIZ_MIGRATION, EDB_HIDE_FILES_IN_CFS, EDB_NUCLEUS_EXTENDED_FS_ALLOWED_NAME, EDB_ONBOARDING_NUCLEUS_VALIDATION_FEATURE_NAME, EDB_ONBOARDING_UPSELL_FEATURE_NAME, EDB_ONE_QUOTA_EXEMPT_IC_RUN_NAME, EDB_PERIODIC_BACKUP_INTERVAL_MINUTES, EDB_PERIODIC_BACKUP_INTERVAL_MINUTES_DEFAULT, EDB_PREFERENCES_PANE_ADD_BACKUP_SURFACE_ENABLED, EDB_PREFERENCES_PANE_ENABLED_NAME, EDB_REBIND_TILL_SYNCED_CURSOR_ATTEMPTS, EDB_REMEDIATE_FAT_ON_VENTURA, EDB_REMEDIATE_LARGE_DRIVE_SCHEDULE, EDB_SCHEDULE_BACKUP_POLLING_INTERVAL_MINUTES, EDB_SCHEDULE_BACKUP_POLLING_INTERVAL_MINUTES_DEFAULT, EDB_SEAMLESS_MIGRATION_BASIC_SCHEDULE_INTERVAL, EDB_SEAMLESS_MIGRATION_MAX_NUM_DRIVES_DEFAULT, EDB_SEV2_REGAL_SQUIRREL_RESUME, EDB_SEV_SILLY_LABRADOR_NAME, EDB_SKIP_FAT_EXFAT_DA_ON_VENTURA, EDB_TEAM_SKU_BACKUP_ENABLED, EdbCustomFoldersVariant, EdbEventOnboardingVariant, EdbOnboardingUpsellVariant, EVENT_ONBOARDING_MAX_PROMPTS_DEFAULT, EVENT_ONBOARDING_MAX_USAGE_DEFAULT, EVENT_ONBOARDING_MIN_CAPACITY_DEFAULT, SeamlessFissionMigrationVariant
from trace import EDB_TRACE, EDB_WARN
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.external_drive_backup.fission_migration_info import FissionMigrationStatus, SeamlessFissionMigrationState
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.stormcrow.machine import MachineStormcrow
from dropbox.i18n import GB, MB
MYPY = False
if MYPY:
    from dropbox.foundation.stormcrow.user import UserStormcrow
EDBAllowedFilesystems = Dict[(str, Set[str])]

class ExternalDriveBackupFeature:
    cached_team_policy: 'Dict[AccountInterface, bool]' = dict()
    force_allowed_seamless_fission_migration_accounts: 'Set[AccountInterface]' = set()
    add_to_force_allowed_migration = (lambda account = None: ExternalDriveBackupFeature.force_allowed_seamless_fission_migration_accounts.add(account))()
    is_on_variant = (lambda variants = None: if not variants:
False# WARNING: Decompyle incomplete
)()
    is_feature_enabled = (lambda : if IS_LINUX:
Falsefeature_enabled(EDB_DISK_ARBITRATION_FEATURE_FLAG))()
    is_fission_migration_enabled = (lambda : 