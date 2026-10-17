# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from build_number.environment import SECONDS_PER_DAY

class SyncRootConstants:
    CONFIG_KEY_SYNC_ROOT_TYPE = 'sync_root_type'
    CONFIG_KEY_ACCOUNT_UID = 'sync_root_account_uid'
    CONFIG_KEY_SYNC_ROOT_CREATION_TIMESTAMP = 'sync_root_creation_ts'
    CONFIG_KEY_FP_DOMAIN_ID = 'fp_domain_identifier'
    CONFIG_KEY_SHADOW_FP_DOMAIN_ID = 'fp_shadow_domain_identifier'
    CONFIG_KEY_SHADOW_TO_MOUNTED_SOCKET_PATH = 'fp_shadow_to_mounted_socket_path'
    CONFIG_KEY_MOUNTED_TO_SHADOW_SOCKET_PATH = 'fp_mounted_to_shadow_socket_path'
    CONFIG_KEY_FP_SHADOW_CUTOVER_START_TIME = 'fp_shadow_cutover_start_time'
    CONFIG_KEY_FP_SYMLINK_PATH = 'fp_symlink_path'
    CONFIG_KEY_FP_SHADOW_MIGRATION_DRYRUN_GENERATION = 'fp_shadow_migration_dryrun_generation'
    CONFIG_KEY_FP_SHADOW_DOMAIN_CREATION_TIME = 'fp_shadow_creation_time'
    CONFIG_KEY_FP_SHADOW_UNMIGRATED_FILES_PATH = 'fp_shadow_unmigrated_files_path'
    CONFIG_KEY_FP_SHADOW_UNMIGRATED_FILES_COUNT = 'fp_shadow_unmigrated_files_count'
    CONFIG_KEY_FP_SHADOW_RUN_POST_MIGRATION_ACTIONS = 'fp_shadow_run_post_migration_actions'
    CONFIG_KEY_FP_SHADOW_MIGRATION_INITIAL_INVARIANTS = 'fp_shadow_migration_initial_invariants'
    CONFIG_KEY_FP_SHADOW_MIGRATION_LAST_ATTEMPT_START_TIME = 'fp_shadow_migration_last_attempt_start_time'
    CONFIG_KEY_CDM_RELOCATE_INCOMPLETE = 'cdm_relocate_fresh_link'
    CONFIG_KEY_CDM_ARCHIVE_LOCATION = 'cdm_relocate_archive_location'
    ROOT_CONSISTENCY_INTERVAL_SECONDS = SECONDS_PER_DAY
    FP_DOMAIN_PATH_LOOKUP_RETRIES = 4
    FP_DOMAIN_PATH_LOOKUP_RETRIES_MAX_DELAY = 30
    FP_DOMAIN_PATH_LOOKUP_RETRIES_INITIAL_DELAY = 5
    DOMAIN_CHANGE_NOTIFICATIONS_TIME_LIMIT_SECS = 3600
    DOMAIN_CHANGE_NOTIFICATIONS_LIMIT = 25
    FP_DFC_DATABASE_PATH_KEY = 'FP_DFC_DATABASE_PATH'
    FP_DFC_PATH_KEY = 'FP_DFC_PATH'

