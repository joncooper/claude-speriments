# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

import uuid
from enum import auto, Enum
from typing import Dict, List, Text, Tuple
from dropbox.client.features.computer_backup.constants import CBFolderId
from dropbox.client.features.users.bridge_gen.role import Role
from dropbox.sync_engine_boundary.constants import OSFolderID
SYNC_EVERYTHING_FEATURE_OFF_VARIANTS = ('OFF', 'CONTROL')
SYNC_EVERYTHING_ONBOARDING_FEATURE_NAME = 'desktop-sync-everything-onboarding'
SYNC_EVERYTHING_STICKY_FEATURE_NAME = 'desktop-sync-everything-onboarding-sticky'
SYNC_EVERYTHING_EXPLORER_AUTO_REBIND_KILLSWITCH_NAME = 'desktop-sync-everything-explorer-auto-rebind-killswitch'
SYNC_EVERYTHING_CALCULATE_OVERQUOTA = 'desktop-sync-everything-calculate-overquota'
SYNC_EVERYTHING_CANCEL_SUPPORT = 'desktop-sync-everything-cancel-support'
SYNC_EVERYTHING_IC_FULL_KILLSWITCH_NAME = 'desktop-sync-everything-ic-full-killswitch'
SYNC_EVERYTHING_BACKUP_FORCE_DISABLE_RECOVERY_KILLSWITCH = 'desktop-sync-everything-backup-force-disable-recovery-killswitch'
SYNC_EVERYTHING_BACKUP_FORCE_DISABLE_MARK_OTHERS_KILLSWITCH = 'desktop-sync-everything-force-disable-mark-others-killswitch'
SYNC_EVERYTHING_INVARIANT_ADD_IMMUTABLE = 'desktop-sync-everything-invariant-check-add-immutable'
SYNC_EVERYTHING_INVARIANT_CLEAR_IMMUTABLE = 'desktop-sync-everything-invariant-check-clear-immutable'
SYNC_EVERYTHING_INVARIANT_BACKUP_SKU_REMEDIATION_NAME = 'desktop-sync-everything-ic-backup-remediation'
SYNC_EVERYTHING_INVARIANT_INTERVAL = 'desktop-sync-everything-invariant-check-interval'
SYNC_EVERYTHING_INVARIANT_INTERVAL_DEFAULT = 900
SYNC_EVERYTHING_METRICS_REPORT_INTERVAL = 'desktop-sync-everything-periodic-metrics-report-interval'
SYNC_EVERYTHING_METRICS_REPORT_INTERVAL_DEFAULT = 86400
SYNC_EVERYTHING_DISABLE_SURVEY_FEATURE_NAME = 'desktop-sync-everything-disable-survey'
SYNC_EVERYTHING_USAGE_REPORT_INTERVAL = 'desktop-sync-everything-usage-report-interval'
SYNC_EVERYTHING_USAGE_REPORT_INTERVAL_DEFAULT = 3600
SYNC_EVERYTHING_DEVICE_CONFLICT_NAME_OVERRIDE = 'desktop-sync-everything-device-conflict-name-override'
SYNC_EVERYTHING_FOLDERS_FEATURE_NAME = 'desktop-sync-everything-folders'
SYNC_EVERYTHING_FOLDERS_UX_EXPERIMENT = 'desktop-sync-everything-folders-ux-experiment'
SYNC_EVERYTHING_ALLOW_MERGE_NON_DEFAULT_LOCATION = 'desktop-sync-everything-allow-merge-non-default-location'
SYNC_EVERYTHING_HANDLE_ROLE_CHANGE_FEATURE_NAME = 'desktop-sync-everything-handle-role-change'
SYNC_EVERYTHING_PERMANENT_HIDE_FEATURE = 'desktop-sync-everything-permanent-hide'
SYNC_EVERYTHING_RESET_PERMANENT_HIDE = 'desktop-sync-everything-reset-permanent-hide'
SYNC_EVERYTHING_SCREENSHOTS_ENABLED = 'desktop-sync-everything-screenshots-enabled'
SYNC_EVERYTHING_MORE_FOLDERS_TOAST_NAME = 'desktop-sync-everything-more-folders-toast'
DEVICE_SYNC_PNM_VARIANT = 'desktop-device-sync-pnm-variant'
SYNC_EVERYTHING_ADOBE_LIBRARY_CHECK_KILL_SWITCH = 'desktop-sync-everything-adobe-library-check-kill-switch'
SYNC_EVERYTHING_PRODUCT_SURVEY_EMAIL_NAME = 'desktop-sync-everything-product-survey-email'
SYNC_EVERYTHING_ROLE_CHANGE_AUTO_REBIND = 'desktop-sync-everything-role-change-auto-rebind'
SYNC_EVERYTHING_SEV_OPALESCENT_ALABASTER_EGRET_DISABLE = 'desktop-sync-everything-sev-opalescent-alabaster-egret-disable'
ACTPA_SYNC_EVERYTHING_PLUS_TRIAL = 'desktop-actpa-sync-everything-plus-trial'
CB_HIDE_BETA_TAG = 'desktop-cboa-hide-beta-tag'
CB_SELF_SERVE_MIGRATION = 'desktop-cboa-self-serve-migration'
CB_FORCED_MIGRATION = 'desktop-cboa-forced-migration'
CB_MIGRATION_PROMPT = 'desktop-cboa-migration-prompt'
CB_FULL_MIGRATION = 'desktop-cboa-full-migration'
CBOA_MIGRATION_UI_NUM_DAYS_BETWEEN_DISMISSED = 'desktop-cboa-ui-num-days-dismissed'
CBOA_MIGRATION_UI_MAX_TIMES_TO_SHOW = 'desktop-cboa-max-times-to-show'
CBOA_MIGRATION_UI_NUM_DAYS_BETWEEN_DISMISSED_DEFAULT = 15
CBOA_MIGRATION_UI_MAX_TIMES_TO_SHOW_DEFAULT = 1
CBOA_FORCED_MIGRATION_MAX_PROMPTS = 3
CBOA_FORCED_MIGRATION_PROMPTS_ROLLING_WINDOW_DAYS = 60
BACKUP_APP = 'desktop-backup-app'
BACKUP_APP_BASIC_OVERQUOTA_UPSELL = 'desktop-backup-app-basic-overquota-upsell'
BACKUP_APP_SYNC_PROGRESS = 'desktop-backup-sync-progress'
BACKUP_TRAY_SYNC_EDB_PROGRESS = 'desktop-backup-tray-sync-edb-progress'
BACKUP_TRAY_SYNC_CB_PROGRESS = 'desktop-backup-tray-sync-cb-progress'
BACKUP_TRAY_FISSION_KILLSWITCH = 'desktop-backup-tray-fission-killswitch'
BACKUP_RESTORATIONS_ONBOARDING = 'desktop-backup-restorations-onboarding'
BACKUP_SKU_MODAL = 'desktop-backup-sku-modal'
BACKUP_ENABLE_TRIALS_CHECKOUT = 'desktop-backup-enable-trials-checkout'
BACKUP_ONBOARDING_CAROUSEL_BACKUP_SKU_REMOVAL = 'desktop-onboarding-carousel-backup-sku-removal'
BACKUP_NEW_ONBOARDING_EXP = 'desktop-backup-use-new-onboarding-experience'
CONFIG_KEY_COMPUTER_BACKUP_PRE_MIGRATION_DEVICE_STATE = 'desktop-computer-backup-pre-migration-device-state'
CONFIG_KEY_COMPUTER_BACKUP_MIGRATION_STATE = 'desktop-computer-backup-migration-state'
CONFIG_KEY_COMPUTER_BACKUP_MIGRATE_ON_RESTART = 'desktop-computer-backup-migrate-on-restart'
CONFIG_KEY_COMPUTER_BACKUP_MIGRATION_SOURCE = 'desktop-computer-backup-migration-source'
CONFIG_KEY_SYNC_EVERYTHING_STICKY_DISMISSED = 'desktop-sync-everything-sticky-dismissed'
CONFIG_KEY_SYNC_EVERYTHING_ACTIVE_ACCOUNT_ID = 'desktop-sync-everything-active-account-id'
CONFIG_KEY_SYNC_EVERYTHING_RESTORE_FROM_LOCAL_DISABLE = 'desktop-sync-everything-restore-from-local-disable'
CONFIG_KEY_SYNC_EVERYTHING_DEVICE_STATE = 'desktop-sync-everything-device-state'
CONFIG_KEY_SYNC_EVERYTHING_PENDING_DEVICE_STATE = 'desktop-sync-everything-pending-device-state'
CONFIG_KEY_SYNC_EVERYTHING_HAS_V3_STATE = 'desktop-sync-everything-has-v3-state'
CONFIG_KEY_SYNC_EVERYTHING_INVARIANT_CHECK_MODE = 'desktop-sync-everything-invariant-check-mode'
CONFIG_KEY_SYNC_EVERYTHING_IC_BACKOFFS = 'desktop-sync-everything-invariant-check-backoffs'
CONFIG_KEY_SYNC_EVERYTHING_SYNC_CALLBACKS = 'desktop-sync-everything-persisted-sync-callbacks'
CONFIG_KEY_SYNC_EVERYTHING_EXCLUSION_FILE_LIST = 'desktop-sync-everything-exclusion-file-list'
CONFIG_KEY_SYNC_EVERYTHING_PROMPT_REBIND_ACCOUNT_ID = 'desktop-sync-everything-prompt-rebind-account-id'
CONFIG_KEY_SYNC_EVERYTHING_SEEN_MORE_FOLDERS_TOAST = 'desktop-sync-everything-seen-more-folders-toast'
CONFIG_KEY_CBOA_MIGRATION_LAST_DISMISSED = 'desktop-cboa-migration-last-dismissed'
CONFIG_KEY_CBOA_MIGRATION_NUM_DISMISSED = 'desktop-cboa-migration-num-dismissed'
CONFIG_KEY_COMPUTER_BACKUP_FORCED_MIGRATION_PROMPT_TS = 'computer-backup-forced-migration-prompts-shown-ts'
CONFIG_KEY_SYNC_EVERYTHING_RAW_CDM_MIGRATION_ACCOUNT_ID = 'desktop-sync-everything-raw-cdm-migration-account-id'
CONFIG_KEY_SYNC_EVERYTHING_BACKUP_SKU_WELCOME_SHOWN = 'desktop-sync-everything-backup-sku-welcome-shown'
CONFIG_KEY_SYNC_EVERYTHING_BACKUP_SKU_TRANSITION = 'desktop-sync-everything-backup-sku-transition'
CONFIG_KEY_SYNC_EVERYTHING_BACKUP_SKU_UNLIMITED_REMINDER_DISMISSED = 'desktop-sync-everything-backup-sku-unlimited-reminder-dismissed'
CONFIG_KEY_SYNC_EVERYTHING_OVER_QUOTA_REMINDER_DISMISSED = 'desktop-sync-everything-over-quota-reminder-dismissed'
CONFIG_KEY_SYNC_EVERYTHING_BACKUP_TRIAL_UPSELL_DISMISSED = 'desktop-sync-everything-backup-trial-upsell-dismissed'
CONFIG_KEY_SYNC_EVERYTHING_ONEDRIVE_ILLEGAL_NESTING_MODAL_DISMISSED = 'desktop-sync-everything-onedrive-illegal-nesting-modal-dismissed'
CONFIG_KEY_SYNC_EVERYTHING_BACKUP_SKU_NEW_UPGRADE_SHOWN__DEPRECATED = 'desktop-sync-everything-backup-sku-new-upgrade-shown'
CONFIG_KEY_SYNC_EVERYTHING_ROLE_CHANGE_AUTO_REBIND_DATA = 'desktop-sync-everything-role-change-auto-rebind-data'
CONFIG_KEY_ACCOUNT_ID = 'account_id'
CONFIG_KEY_COMPUTER_BACKUP_LAST_BACKED_UP_TS_MS = 'desktop-computer-backup-last-backed-up-ts-ms'
CONFIG_KEY_SHADOW_MIGRATION_CBOS_REBIND_DONE = 'desktop-shadow-cbos-rebind-done'
FIRST_SYNC_NONE = 'NONE'
FIRST_SYNC_L0_HIDDEN = 'L0_HIDDEN'
EXP_BACKOFF_BASE = 2
INVARIANT_CHECKER_REBIND_NUM_ATTEMPTS = 5
INVARIANT_CHECKER_REBIND_DELAY_SEC = 1
MAX_FOLDER_RESTORE_ATTEMPTS = 3
FOLDER_RESTORE_DELAY_SEC = 0.5
MAX_COMPLETE_RESTORE_ATTEMPTS = 12
MAX_START_RESTORE_ATTEMPTS = 12
COMPLETE_RESTORE_DELAY_SECS = 2
START_RESTORE_DELAY_SECS = 2
DEFAULT_BACKUP_OPERATION_RETRY_COUNT = 3
DEFAULT_BACKUP_OPERATION_RETRY_DELAY = 2
IC_EXP_BACKOFF_INITIAL_DELAY_SEC = SYNC_EVERYTHING_INVARIANT_INTERVAL_DEFAULT
IC_EXP_BACKOFF_EXP_BASE = 2
IC_EXP_BACKOFF_MAX = 86400
IC_FOLDER_MISSING_MAX_BACKOFF = 4
MAX_DESTROY_BLOCKING_TIME_SEC = 10
FREE_SPACE_BUFFER = 10485760
SE_BLOCK_UNLINK_BLOCK_TIME = 15
FOLDER_METADATA_UX_UPDATE_FREQUENCY = 500

class InvariantCheckMode(Enum):
    MONITOR = 'monitor'
    FULL = 'full'

ROLE_CHANGE_TIMEOUT = 600
REMOTE_ACCOUNT_DELETE_TIMEOUT = 600
OQ_MAX_RUNTIME = 10
ACTIVE_ACCOUNT_UNLINK_TIMEOUT = 30
ADMIN_POLICY_REFRESH_DELAY_SEC = 3600
SYNC_EVERYTHING_INVARIANT_RUNS_FOR_CHECK_QUOTA_EXEMPT = 4
FIFTEEN_MINUTES_AS_SECONDS = 900
CONTROLLER_START_UP_TIMEOUT = 30
FP_MIGRATION_UNMERGE_TIMEOUT = 180
TWO_WEEKS_AS_SECONDS = 1209600
ONE_MONTH_AS_SECONDS = 2592000
STRING_TO_ROLE = {
    'PERSONAL': Role.PERSONAL,
    'BUSINESS': Role.BUSINESS }

class MoreFoldersToastType(Enum):
    OFF = auto()
    CURRENTLY_BOUND = auto()
    PREVIOUSLY_BOUND = auto()
    BOTH = auto()

DeviceID = uuid.UUID

class DeviceStatus(Enum):
    ENABLED = 0
    DISABLED = 1
    ERROR_DISABLED = 2


class BackupDisableType(Enum):
    QUOTA_EXEMPT = 'quota_exempt'

KnownFolderRequest = Tuple[(OSFolderID, Text)]
CustomFolderRequest = Tuple[(Text, Text)]
FolderIgnorePaths = Dict[(CBFolderId, List[Text])]
