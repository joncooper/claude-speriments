# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import auto, Enum
from typing import Callable, Dict, List, Optional, Text, Union
from dropbox.api.v2.datatypes.external_drive_backup import ExternalDriveBackupStateEnum
from dropbox.client.features.external_drive_backup.errors import RequestAssertion
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.i18n import GB, MB, trans
from dropbox.sync_engine_boundary.types import DeviceAnchorState
EDB_DISK_ARBITRATION_FEATURE_FLAG = 'desktop-external-backup-disk-arbitration'
EDB_DISK_ARBITRATION_USER_STORMCROW_NAME = 'desktop-external-backup-disk-arbitration-enabled'
EDB_FEATURE_NAME = 'desktop-external-drive-backup'
EDB_EVENT_ONBOARDING_FEATURE_NAME = 'desktop-external-drive-backup-event-onboarding'
EDB_EVENT_ONBOARDING_MAX_USAGE_NAME = 'desktop-external-drive-backup-event-onboarding-max-usage-gb'
EDB_EVENT_ONBOARDING_MAX_PROMPTS_NAME = 'desktop-external-drive-backup-event-onboarding-max-prompts'
EDB_EVENT_ONBOARDING_MIN_CAPACITY_NAME = 'desktop-external-drive-backup-event-onboarding-min-capacity-gb'
EDB_PREFERENCES_PANE_ENABLED_NAME = 'desktop-external-backup-preferences-pane'
EDB_DA_RATELIMIT_MAX_EVENT_NAME = 'desktop-external-drive-backup-da-max-event-ratelimit'
EDB_DA_MIN_CAPACITY_NAME = 'desktop-external-drive-backup-da-min-capacity-mb'
EDB_DBXIGNORE_FEATURE_NAME = 'desktop-external-drive-backup-dbxignore'
EDB_NEW_WINDOW_PER_DRIVE_FEATURE_NAME = 'desktop-external-drive-backup-new-window-per-drive'
EDB_DA_EVENT_EARLY_SUPPRESS_NAME = 'desktop-external-drive-backup-event-onboarding-early-suppress-sec'
EDB_NOTIFICATION_ON_ARRIVAL_FEATURE_NAME = 'desktop-external-drive-backup-notification-on-arrival'
EDB_CAROUSEL_UPSELL_FEATURE_NAME = 'desktop-external-drive-backup-upsell'
EDB_CUSTOM_FOLDERS_FEATURE_NAME = 'desktop-external-drive-backup-custom-folders-selector'
EDB_HIDE_FILES_IN_CFS = 'desktop-external-drive-backup-hide-files-in-cfs'
EDB_ONBOARDING_UPSELL_FEATURE_NAME = 'desktop-external-drive-backup-onboarding-upsell'
EDB_REBIND_TILL_SYNCED_CURSOR_ATTEMPTS = 'desktop-external-drive-backup-synced-cursor-attempts'
EDB_ONBOARDING_NUCLEUS_VALIDATION_FEATURE_NAME = 'desktop-external-drive-backup-onboarding-nucleus-validation'
EDB_PERIODIC_BACKUP_INTERVAL_MINUTES = 'desktop-external-drive-backup-periodic-backup-interval-minutes'
EDB_ONE_QUOTA_EXEMPT_IC_RUN_NAME = 'desktop-external-drive-backup-one-quota-exempt-ic-run'
EBD_QUOTA_EXEMPT_IC_NO_OP = 'desktop-external-drive-backup-quota-exempt-ic-no-op'
EDB_SEV2_REGAL_SQUIRREL_RESUME = 'desktop-external-drive-backup-sev2-regal-squirrel-resume'
EDB_FAT_FILESYSTEM_SUPPORT_ENABLED = 'desktop-external-drive-backup-fat-filesystem-support-enabled'
EDB_EXFAT_FILESYSTEM_SUPPORT_ENABLED = 'desktop-external-drive-backup-exfat-filesystem-support-enabled'
EDB_FP_MIGRATION_ALLOWED_NAME = 'desktop-external-drive-backup-fp-migration-allowed'
EDB_FP_MIGRATION_PREFER_BASIC_FIZ_MIGRATION = 'desktop-external-drive-backup-fp-migration-prefer-basic'
EDB_FISSION_MIGRATION_ALLOWED_NAME = 'desktop-external-drive-backup-fission-migration-allowed'
EDB_FISSION_MIGRATION_VMEM_PERC_THRESHOLD_NAME = 'desktop-external-drive-backup-fission-migration-vmem-perc-threshold'
EDB_FISSION_MIGRATION_DISK_PERC_THRESHOLD_NAME = 'desktop-external-drive-backup-fission-migration-disk-perc-threshold'
EDB_FISSION_MIGRATION_SCHEDULE_INTERVAL_NAME = 'desktop-external-drive-backup-fission-migration-scheduler-interval'
EDB_FISSION_MIGRATION_MAX_NUM_BACKUPS_NAME = 'desktop-external-drive-backup-fission-migration-max-num-drives'
EDB_NUCLEUS_EXTENDED_FS_ALLOWED_NAME = 'desktop-nucleus-device-anchor-extended-filesystems'
EDB_CONTEXT_MENU_KILL_SWITCH_NAME = 'desktop-external-drive-backup-context-menu-kill-switch'
EDB_PREFERENCES_PANE_ADD_BACKUP_SURFACE_ENABLED = 'desktop-enable-edb-setup-from-desktop-surface'
EDB_TEAM_SKU_BACKUP_ENABLED = 'desktop-backup-team-sku-idaho-feature'
EDB_DELAY_FULL_DRIVE_OVERQUOTA_CHECK = 'desktop-delay-full-drive-overquota-check-after-start-backup'
EDB_SKIP_FAT_EXFAT_DA_ON_VENTURA = 'desktop-skip-fat-exfat-da-on-ventura'
EDB_REMEDIATE_FAT_ON_VENTURA = 'desktop-edb-remediate-fat-on-ventura'
EDB_REMEDIATE_LARGE_DRIVE_SCHEDULE = 'desktop-edb-remediate-large-drive-schedule'
EDB_SCHEDULE_BACKUP = 'desktop-edb-schedule-backup'
EDB_SCHEDULE_BACKUP_POLLING_INTERVAL_MINUTES = 'desktop-edb-schedule-backup-polling-interval-minutes'
EDB_SEV_SILLY_LABRADOR_NAME = 'desktop-external-drive-backup-sev-silly-labrador-killswitch'
EDB_FEATURE_OFF_VARIANTS = ('OFF', 'CONTROL')
CONFIG_KEY_EDB_ONBOARDING_DO_NOT_SHOW_UUIDS = 'desktop-edb-onboarding-do-not-show-uuids'
CONFIG_KEY_EDB_PERSISTED_SYNC_CALLBACKS = 'desktop-edb-persisted-sync-callbacks'
CONFIG_KEY_EDB_ONBOARDING_UUIDS_COUNTS = 'desktop-edb-onboarding-uuids-counts'
CONFIG_KEY_EDB_PAUSED_BUBBLE_COUNTER = 'desktop-edb-paused-bubble-counter'
CONFIG_KEY_EDB_PREF_SUPPRESSED = 'desktop-edb-pref-suppressed'
CONFIG_KEY_EDB_REMEDIATED_UUIDS = 'desktop-edb-remediated-uuids'
CONFIG_KEY_EDB_UNBIND_ALERT_SHOWN_UUIDS = 'desktop-edb-unbind-alert-shown-uuids'
CONFIG_KEY_EDB_SEV2_REGAL_SQUIRREL_RESUMED_UUIDS = 'desktop-edb-sev2-regal-squirrel-resumed-uuids'
CONFIG_KEY_EDB_USE_BACKUP_INSTANCE = 'desktop-edb-use-backup-instance'
CONFIG_KEY_EDB_FISSION_MIGRATION_INFO = 'desktop-edb-fission-migration-info'
CONFIG_KEY_EDB_SEAMLESS_FISSION_MIGRATION_INFO = 'desktop-edb-seamless-fission-migration-info'
CONFIG_KEY_EDB_FAT_VENTURA_CAPACITY_UPDATED_UUIDS = 'desktop-edb-fat-ventura-capacity-updated'
CONFIG_KEY_EDB_ANCHOR_FILEID_DISPLAY_NAME = 'desktop-edb-anchor-fileid-display-name'
CONFIG_KEY_EDB_ANCHOR_USAGE = 'desktop-edb-anchor-fileid-usage'
CONFIG_KEY_EDB_ONBOARDING_SHOWN_DRIVE_UUIDS_DEPRECATED = 'desktop-edb-onboarding-shown-drive-uuids'
EDB_DA_RATELIMIT_PERIOD_SEC = 3600
EDB_DA_HANDLER_TITLE = 'windows_edb_devicenotify'
EDB_DA_RATELIMIT_DEFAULT_MAX = 512
EDB_DA_DEFAULT_MIN_CAPACITY = 128 * MB
EDB_DA_MOST_COMMON_ERROR_SAMPLE_RATE = 0.0001
EDB_DA_COMMON_ERROR_SAMPLE_RATE = 0.001
EDB_DA_RARE_ERROR_SAMPLE_RATE = 0.1
EDB_DA_ERROR_REPORT_ALL = 1
MAX_PAUSED_PROMPT = 2
ADMIN_POLICY_REFRESH_DELAY_SEC = 3600
EDB_DEFAULT_NAME = 'External Drive'
PERSONAL_ROLE = 'PERSONAL'
BUSINESS_ROLE = 'BUSINESS'
HELP_CENTER_ARTICLE_URL = 'https://help.dropbox.com/installs-integrations/sync-uploads/external-drive'
LINK_UNLINK_DROPBOX_ACCOUNTS_URL = 'https://help.dropbox.com/accounts-billing/multiple-accounts/link-unlink-two-accounts'
EDB_REMOTE_UPLOAD_SAMPLE_SIZE = 10
EVENT_ONBOARDING_MAX_USAGE_DEFAULT = 32 * GB
EVENT_ONBOARDING_MAX_PROMPTS_DEFAULT = 3
EVENT_ONBOARDING_MIN_CAPACITY_DEFAULT = 64 * GB
EDB_EVENT_ONBOARDING_EARLY_SUPPRESS_SEC_DEFAULT = 30
EDB_ANCHOR_INVARIANT_CHECK_INTERVAL_DEFAULT = 3600
EDB_PERIODIC_BACKUP_INTERVAL_MINUTES_DEFAULT = 60
EDB_PERIODIC_USAGE_REPORTER_DEFAULT = 21600
EDB_IC_WAIT_AFTER_SETUP_SEC = 5
EDB_SCHEDULE_BACKUP_POLLING_INTERVAL_MINUTES_DEFAULT = 15
EDB_SEAMLESS_MIGRATION_WAIT_FOR_FISSION_TIMEOUT = 60
EDB_SEAMLESS_MIGRATION_LONG_POLL_INTERVAL = 180
EDB_SEAMLESS_MIGRATION_BASIC_SCHEDULE_INTERVAL = 21600
EDB_SEAMLESS_MIGRATION_MAX_NUM_DRIVES_DEFAULT = 5
EDB_FISSION_MIGRATION_VMEM_PERC_THRESHOLD_DEFAULT = 50
EDB_FISSION_MIGRATION_DISK_PERC_THRESHOLD_DEFAULT = 100
MAX_DESTROY_BLOCKING_TIME_SEC = 10
MAX_LIST_BACKUPS_BLOCKING_TIME_SEC = 10
OQ_MAX_RUNTIME = 10
FREE_SPACE_BUFFER = 10485760
EXP_BACKOFF_BASE = 2
PING_SERVER_NUM_ATTEMPTS = 3
CREATE_BACKUP_NUM_ATTEMPTS = 3
RETRY_DELAY_BASE_SECOND = 0.5
IS_ELIGIBLE_SEAMLESS_NUM_ATTEMPTS = 3
SETUP_SEAMLESS_NUM_ATTEMPTS = 3
START_SEAMLESS_NUM_ATTEMPTS = 3
REFRESH_SEAMLESS_NUM_ATTEMPTS = 3
FSS_ANCHOR_BREAK_COMPLETE_NUM_ATTEMPTS = 3
FSS_ANCHOR_DELETE_COMPLETE_NUM_ATTEMPTS = 3
FISSION_UNPAUSED_ANCHOR_NUM_ATTEMPTS = 3
UPDATE_SEAMLESS_NUM_ATTEMPTS = 3

class ExternalDriveArrivalEvent:
    optional_fields = [
        'num_partitions',
        'device_internal',
        'device_vendor',
        'media_name',
        'media_ejectable',
        'volume_network',
        'bus_name',
        'device_protocol',
        'media_removable',
        'volume_kind',
        'media_writable',
        'device_model',
        'media_content',
        'media_kind',
        'media_icon',
        'volume_mountable',
        'device_path',
        'media_uuid']
    
    def __init__(self, vol_name, serial_id, path, fs_type, capacity, usage, is_writable, is_remote, num_partitions, device_internal, device_vendor, media_name, media_ejectable, volume_network, bus_name, device_protocol, media_removable, volume_kind, media_writable, device_model, media_content, media_kind = None, volume_mountable = None, media_icon = None, device_path = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None), media_uuid = ('vol_name', 'Text', 'serial_id', 'str', 'path', 'Text', 'fs_type', 'Text', 'capacity', 'int', 'usage', 'int', 'is_writable', 'bool', 'is_remote', 'bool', 'num_partitions', 'Optional[int]', 'device_internal', 'Optional[bool]', 'device_vendor', 'Optional[Text]', 'media_name', 'Optional[Text]', 'media_ejectable', 'Optional[bool]', 'volume_network', 'Optional[bool]', 'bus_name', 'Optional[Text]', 'device_protocol', 'Optional[Text]', 'media_removable', 'Optional[bool]', 'volume_kind', 'Optional[Text]', 'media_writable', 'Optional[bool]', 'device_model', 'Optional[Text]', 'media_content', 'Optional[Text]', 'media_kind', 'Optional[Text]', 'volume_mountable', 'Optional[bool]', 'media_icon', 'Optional[Text]', 'device_path', 'Optional[Text]', 'media_uuid', 'Optional[Text]', 'return', 'None')):
        self.vol_name = vol_name
        self.serial_id = serial_id
        self.path = path
        self.fs_type = fs_type
        self.capacity = capacity
        self.usage = usage
        self.is_writable = is_writable
        self.is_remote = is_remote
        self.num_partitions = num_partitions
        self.device_internal = device_internal
        self.device_vendor = device_vendor
        self.media_name = media_name
        self.media_ejectable = media_ejectable
        self.volume_network = volume_network
        self.bus_name = bus_name
        self.device_protocol = device_protocol
        self.media_removable = media_removable
        self.volume_kind = volume_kind
        self.media_writable = media_writable
        self.device_model = device_model
        self.media_content = media_content
        self.media_kind = media_kind
        self.volume_mountable = volume_mountable
        self.media_icon = media_icon
        self.device_path = device_path
        self.media_uuid = media_uuid

    
    def get_all_optional_fields(self = None):
        res = { }
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        required_fields = f'''vol_name={self.vol_name}, serial_id={self.serial_id}, path={self.path}, fs_type={self.fs_type}, capacity={self.capacity}, usage={self.usage}, is_remote={self.is_remote}, is_writable={self.is_writable}, '''
        optional_field_pairs = self.get_all_optional_fields().items()()
        return required_fields + ', '.join(optional_field_pairs)


DriveArrivalCallback = Callable[([
    ExternalDriveArrivalEvent], None)]
DriveDepartureCallback = Callable[([
    Text], None)]

class ExternalDriveBackupUIStrings(UIStrings):
    close_button = UI('Close')
    unbind_alert_title = UI("There is an issue with your '%(drive_name)s' backup.")
    unbind_alert_title_no_name = UI('There is an issue with your external drive backup.')
    unbind_alert_remediated_body = UI("The files on your external drive and in your backup are safe. We're creating a new, duplicate backup to solve this issue.")
    unbind_alert_body = UI("The files on your external drive and in your backup are safe. However, future updates to your drive won't be reflected in your backup.")
    unbind_alert_learn_more_btn = UI('Learn More')
    unbind_alert_dismiss_btn = UI('Okay')
    synced_alert_title = UI("Your '%(drive_name)s' is up to date")
    synced_alert_title_no_name = UI('Your backup is up to date')
    synced_alert_body = UI('Go to Dropbox to view your uploaded files')
    default_anchor_name = UI('External Drive')
    drive_arrival_title_no_name = UI('Back up your external drive')
    drive_arrival_title = UI("Back up '%(drive_name)s'")
    drive_arrival_body = UI('Dropbox will back up this drive until it’s unplugged.')
    drive_arrival_setup_btn = UI('Set up')
    drive_arrival_never_again_btn = UI('Never for this drive')
    drive_native_arrival_body = UI("Dropbox will regularly back up this drive in the background while it’s plugged in. <a href='{}'>More Info</a>".format(HELP_CENTER_ARTICLE_URL))
    drive_native_arrival_body_personal_one_click = UI("Dropbox will regularly back up this drive to your personal account. <a href='{}'>More Info</a>".format(HELP_CENTER_ARTICLE_URL))
    drive_native_arrival_header = UI("Back up '%(drive_name)s' to Dropbox?")
    drive_native_arrival_header_no_name = UI('Back up your drive to Dropbox?')
    drive_native_start_btn = UI('Start backup')
    drive_native_cancel_btn = UI('Not now')
    drive_native_dont_ask_again_checkbox = UI("Don't ask me again")
    drive_native_custom_folder_arrival_body = UI('This entire drive will back up while plugged in. Or, you can choose specific folders to back up instead.')
    drive_native_idaho_arrival_body_paired = UI('This entire drive will back up while plugged in. Or, you can choose specific folders to back up instead. <br/><br/>Check the box below if you want to back up this device to your company Dropbox instead of your personal             Dropbox.')
    drive_native_select_team_checkbox = UI("Back up to my '%(team_name)s' Dropbox")
    drive_native_custom_folders_v1_start_btn = UI('Choose folders')
    drive_native_custom_folders_v2_start_btn = UI('Set up')
    drive_native_custom_folders_v4_backup_btn = UI('Back up')
    drive_native_custom_folders_v4_choose_folders_btn = UI('Choose folders')
    drive_native_arrival_upsell_v3_body = UI('Try Plus for 2,000GB of space & more. Free 14-day trial, no credit card needed.')
    drive_native_arrival_upsell_v3_paired_body = UI('Try Plus for your personal account and get 2,000GB of space & more. Free 14-day trial, no credit card needed.')
    drive_native_arrival_upsell_v3_header = UI('Backup has started! However, some of your drive won’t fit in your Basic plan.')
    drive_native_upsell_v3_try_plus_btn = UI('Try for free')
    drive_native_upsell_v3_continue_anyway_btn = UI('Continue anyway')
    trial_success_post_backup_success_bubble_header = UI('Plus trial has started!')
    trial_success_post_backup_success_bubble_body = UI('Your free Plus trial ends in 14 days.')
    trial_success_post_backup_success_bubble_body_view_progress_btn = UI('View progress')
    drive_native_upsell_trial_success_backup_fail_body = UI("The trial has started and your files are safe in your external drive. Go to <a href='https://help.dropbox.com/installs-integrations/sync-uploads/external-drive'>Help Center</a> to learn more.")
    drive_native_upsell_trial_success_backup_fail_header = UI("There was an issue backing up '%(drive_name)s'.")
    drive_native_upsell_trial_success_backup_fail_header_no_name = UI('There was an issue backing up drive.')
    drive_native_upsell_trial_success_backup_fail_dismiss_btn = UI('Okay')
    drive_native_upsell_trial_success_backup_success_body = UI("Your free Plus trial ends in 14 days. Your backup will be called '%(drive_name)s' in your Dropbox. Back up will continue until the drive is unplugged.")
    drive_native_upsell_trial_success_backup_success_body_no_name = UI('Your free Plus trial ends in 14 days. Your backup will be in your Dropbox. Back up will continue until the drive is unplugged.')
    drive_native_upsell_trial_success_backup_success_header = UI('Backup has started!')
    drive_native_upsell_trial_success_backup_success_dismiss_btn = UI('Dismiss')
    drive_native_upsell_trial_success_backup_success_view_progress_btn = UI('View progress')
    drive_native_upsell_trial_fail_backup_success_body = UI('Backup will stop once you reach your storage limit. You can always upgrade to Plus later.')
    drive_native_upsell_trial_fail_backup_success_header = UI('Couldn’t start trial, but your backup has started!')
    drive_native_upsell_trial_fail_backup_success_dismiss_btn = UI('Dismiss')
    drive_native_upsell_trial_fail_backup_success_view_progress_btn = UI('View progress')
    drive_native_upsell_trial_fail_backup_fail_body = UI("Your files are safe in your external drive. Go to <a href='https://help.dropbox.com/installs-integrations/sync-uploads/external-drive'>Help Center</a> to learn more.")
    drive_native_upsell_trial_fail_backup_fail_header = UI("There was an issue backing up '%(drive_name)s'.")
    drive_native_upsell_trial_fail_backup_fail_header_no_name = UI('There was an issue backing up drive.')
    drive_native_upsell_trial_fail_backup_fail_dismiss_btn = UI('Okay')
    basic_backup_success_bubble_header = UI('Backup has started!')
    basic_backup_success_bubble_body = UI('Backup will update while plugged-in')
    basic_backup_success_bubble_body_view_progress_btn = UI('View progress')
    basic_backup_success_dialog_header = UI("Backing up '%(drive_name)s'...")
    basic_backup_success_dialog_header_no_name = UI('Backing up your drive...')
    basic_backup_success_dialog_body = UI('The first backup might take some time. Just use your %(os_platform)s normally while this happens.')
    basic_backup_success_dialog_close_btn = UI('Done')
    basic_backup_success_dialog_manage_btn = UI('Manage Backup')
    resume_backup_success_bubble_header = UI("Resuming backup of '%(drive_name)s'")
    resume_backup_success_bubble_header_no_name = UI('Resuming backup of drive')
    resume_unplugged_backup_success_bubble_header = UI('Automatic backup turned on')
    resume_backup_success_bubble_body_no_name = UI('A copy of your drive is uploading to Dropbox.')
    resume_unplugged_backup_success_bubble_body = UI("Your backup will resume when '%(drive_name)s' is replugged.")
    resume_unplugged_backup_success_bubble_body_no_name = UI('Your backup will resume when drive is replugged.')
    resume_backup_pause_btn = UI('Pause')
    pause_backup_success_bubble_header = UI("Backup paused for '%(drive_name)s'")
    pause_backup_success_bubble_header_no_name = UI('Pausing backup of drive')
    pause_backup_success_bubble_body_no_name = UI('Future updates to the drive won’t be uploaded to Dropbox')
    pause_backup_success_bubble_undo_btn = UI('Undo')
    paused_backup_bubble_header = UI("Resume backup of '%(drive_name)s'?")
    paused_backup_bubble_header_no_name = UI('Resume backup of your external drive?')
    paused_backup_bubble_body_no_name = UI('Any changes made on the drive while unplugged will be reflected in Dropbox.')
    paused_backup_resume_btn = UI('Resume')
    trial_success_backup_success_bubble_header = UI('Backup has started!')
    trial_success_backup_success_bubble_body = UI('Your free Plus trial ends in 14 days.')
    trial_success_backup_success_bubble_body_view_progress_btn = UI('View progress')
    unplug_error_bubble_header = UI("You’ve unplugged '%(drive_name)s'. Plug it back in to finish set up.")
    unplug_error_bubble_header_no_name = UI("You've unplugged drive. Plug it back in to finish set up.")
    unplug_error_bubble_body = UI('Once you plug in your drive, select "Try again" to back up a copy to Dropbox.')
    unplug_error_bubble_body_dismiss_btn = UI('Cancel setup')
    unplug_error_bubble_body_try_again_btn = UI('Try again')
    offline_error_bubble_header = UI('Internet connection was lost')
    offline_error_bubble_body = UI("We can't begin set up for your '%(drive_name)s' until connection resumes. Try reconnecting and then click <b>Try again</b>.")
    offline_error_bubble_body_no_name = UI("We can't begin set up for your drive until connection resumes. Try reconnecting and then click <b>Try again</b>.")
    one_way_sync_remediation_bubble_header = UI('Changes reverted in Dropbox')
    one_way_sync_remediation_bubble_body = UI("Your backup will remain a mirror copy of '%(drive_name)s'.")
    sel_sync_dialog_error_header = UI('Unable to hide this folder')
    sel_sync_dialog_error_body = UI('Selective Sync is not supported on backup folders. Move your external drive backup out of this folder and retry.')
    sel_sync_dialog_error_action = UI('Dismiss')
    team_admin_disabled_edb_header = UI("Your admin hasn't enabled external device backups for '%(team_name)s' Dropbox")
    team_account_unable_to_backup_body = UI('You can, however, back up this device to your personal account. Go to <b>Backup settings</b> and choose your personal account')
    team_license_cap_reached_header = UI("You've reached the device limit for '%(team_name)s' Dropbox")
    team_admin_disabled_edb_body = UI('You can, however, back up this device to your personal account. Go to <b>Backup settings</b> and choose your personal account')
    team_backup_dialog_settings_btn = UI('Backup settings')
    team_backup_dialog_find_out_how_btn = UI('Find out how')
    fission_migr_in_progress_broken_header = UI("Your files are safe, but we need to make a copy of your '%(drive_name)s' backup.")
    fission_migr_in_progress_broken_body = UI("This copy will replace your existing backup. Do you want to keep or delete the original backup? <a href='https://help.dropbox.com/installs-integrations/sync-uploads/external-drive'>Learn more.</a>")
    fission_seamless_migr_in_progress_broken_header = UI('We need to make a duplicate copy of your backup')
    fission_seamless_migr_in_progress_broken_body = UI('Your files are safe. Want to keep version history? Keep both copies. If not, feel free to delete the original backup.')
    fission_migr_in_progress_broken_keep_both = UI('Keep both')
    fission_migr_in_progress_broken_delete = UI('Delete original backup')
    fission_migr_in_progress_delete_conf_header = UI('Delete original backup?')
    fission_migr_in_progress_delete_conf_body = UI("If you change your mind, you can access the original in <b>Deleted files</b> for 30 days. <a href='https://help.dropbox.com/files-folders/restore-delete/recover-deleted-files-folders'>Learn more.</a>")
    fission_migr_in_progress_delete_conf_delete = UI('Delete')
    fission_migr_delete_err_header = UI("Couldn't delete original backup")
    fission_migr_delete_err_body = UI("You can try again or delete it on <a href='https://www.dropbox.com/'>dropbox.com.</a> <a href='https://help.dropbox.com/files-folders/restore-delete/delete-files'>Learn more.</a>")
    fission_migr_delete_err_try_again = UI('Try again')
    fission_migr_delete_err_ok = UI('OK')
    local_conflicts_consuming_disk_space_body = UI('Free up storage space in Dropbox and on your computer by deleting any restored files you no longer need.')
    local_conflicts_consuming_disk_space_close_btn = UI('Close')
    local_conflicts_consuming_disk_space_action_btn = UI('Review restored files')
    dbxignore_header_lines = (lambda : line1 = trans('Hey there! This file was made by your friends at Dropbox to prevent syncing unnecessary files your computer generates.')line2 = trans('Learn more about this here: https://help.dropbox.com/installs-integrations/sync-uploads/external-drive')line3 = ''[
line1,
line2,
line3])()
    anchor_name_with_suffix = (lambda anchor_name = None: trans('%(anchor_name)s (New)') % dict(anchor_name = anchor_name))()


class DiskArbitrationErrorOrigin(Enum):
    UNPACK_DA_EVENTS = auto()
    DA_THREAD_LOOP = auto()
    DA_THREAD_OUTER = auto()
    DERIVE_DRIVE_PATH = auto()
    RETRIEVE_VOLUME_INFO = auto()
    DA_CONTROLLER = auto()
    WMI_EXTRA_INFO = auto()
    WMI_NOT_IMPORTED = auto()
    READ_WINDOWS_DACL = auto()
    HANDLE_MULTIPLE_PARTITIONS = auto()
    OTHER = auto()

DA_ERROR_LOCATION_SAMPLE_MAP = {
    DiskArbitrationErrorOrigin.OTHER: EDB_DA_ERROR_REPORT_ALL,
    DiskArbitrationErrorOrigin.HANDLE_MULTIPLE_PARTITIONS: EDB_DA_COMMON_ERROR_SAMPLE_RATE,
    DiskArbitrationErrorOrigin.READ_WINDOWS_DACL: EDB_DA_COMMON_ERROR_SAMPLE_RATE,
    DiskArbitrationErrorOrigin.WMI_NOT_IMPORTED: EDB_DA_RARE_ERROR_SAMPLE_RATE,
    DiskArbitrationErrorOrigin.WMI_EXTRA_INFO: EDB_DA_COMMON_ERROR_SAMPLE_RATE,
    DiskArbitrationErrorOrigin.DA_CONTROLLER: EDB_DA_ERROR_REPORT_ALL,
    DiskArbitrationErrorOrigin.RETRIEVE_VOLUME_INFO: EDB_DA_COMMON_ERROR_SAMPLE_RATE,
    DiskArbitrationErrorOrigin.DERIVE_DRIVE_PATH: EDB_DA_COMMON_ERROR_SAMPLE_RATE,
    DiskArbitrationErrorOrigin.DA_THREAD_OUTER: EDB_DA_ERROR_REPORT_ALL,
    DiskArbitrationErrorOrigin.DA_THREAD_LOOP: EDB_DA_MOST_COMMON_ERROR_SAMPLE_RATE,
    DiskArbitrationErrorOrigin.UNPACK_DA_EVENTS: EDB_DA_MOST_COMMON_ERROR_SAMPLE_RATE }
DISABLED_EDB_STATE_ENUMS = (ExternalDriveBackupStateEnum.deleted, ExternalDriveBackupStateEnum.broken_server_deleted, ExternalDriveBackupStateEnum.broken, ExternalDriveBackupStateEnum.permanently_failed)

class EdbOnboardingUpsellVariant(Enum):
    V3 = auto()


class EdbCustomFoldersVariant(Enum):
    V1 = auto()
    V2 = auto()
    V4 = auto()


class EdbEventOnboardingVariant(Enum):
    OFF = auto()
    CONTROL = auto()
    ON = auto()
    TEAM_POLICY_DISABLED = auto()


class SeamlessFissionMigrationVariant(Enum):
    OFF = auto()
    BASIC = auto()
    SEAMLESS_P1_BASE = auto()
    SEAMLESS_P2_MULTIBKP = auto()
    SEAMLESS_P3_LINKED_ACCT = auto()
    SEAMLESS_FULL = auto()
    any_allowed_multibackup_variants = (lambda variants = None: 