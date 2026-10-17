# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import auto, Enum
from typing import NamedTuple, Optional, Text, TypedDict, Union
from dropbox.api.v2.datatypes.device_sync import ComputerBackupFolderState, ComputerBackupState as ComputerBackupApiState
from dropbox.client.features.computer_backup.errors import RequestAssertion
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.model.types import FileId
from dropbox.sync_engine_boundary.constants import OSFolderID
CB_FEATURE_OFF_VARIANTS = [
    'OFF',
    'CONTROL']
CB_ANCHORS_FEATURE_NAME = 'desktop-computer-backup-anchors'
CB_PERIODIC_BACKUP_INTERVAL_MINUTES = 'desktop-computer-backup-periodic-backup-interval-minutes'
CB_ALLOW_ONEDRIVE = 'desktop-cba-allow-onedrive'
CB_ALLOW_GOOGLEDRIVE = 'desktop-cba-allow-googledrive'
CB_ALLOW_ICLOUD = 'desktop-cba-allow-icloud'
CB_ANCHORS_RESTORATIONS_ONBOARDING = 'desktop-computer-anchors-restorations-onboarding'
CB_CHECK_MIXED_BACKUPS = 'desktop-computer-backup-check-mixed-backups'
CB_SCHEDULE = 'desktop-computer-backup-schedule'
EDB_SCHEDULE = 'desktop-edb-schedule-backup'
CB_CUSTOM_FOLDERS_SELECTOR = 'desktop-computer-backup-custom-folders-selector'
CB_CUSTOM_FOLDERS_ANCHOR_LIMIT = 'desktop-computer-backup-custom-folders-anchor-folders-limit'
CB_CUSTOM_FOLDERS_ANCHOR_LIMIT_DEFAULT = 30
CB_RELINK_KILL_SWITCH_NAME = 'desktop-computer-backup-ic-relink-kill-switch'
CB_BREAK_ANCHORS_KILL_SWITCH_NAME = 'desktop-computer-backup-ic-break-anchors-kill-switch'
CB_ALLOW_RELINK_ON_START_UP_FEATURE_NAME = 'desktop-computer-backup-ic-relink-startup'
CB_SCHEDULED_BACKUP_POLLING_INTERVAL_MINUTES = 'desktop-computer-backup-polling-interval-minutes'
CB_RESTORE_IN_ROOT = 'desktop-computer-backup-restore-in-root'
CB_RESUME_ANCHORS_ON_RELINK_KILLSWITCH = 'desktop-computer-backup-resume-anchors-on-relink-killswitch'
CB_CANCEL_SUPPORT = 'desktop-computer-backup-cancel-support'
CB_DISABLE_BACKUP_SURVEY = 'desktop-computer-backup-disable-survey'
CB_SYNC_PROGRESS_UPDATES = 'desktop-computer-backup-sync-progress-updates'
CB_USAGE_REPORT_INTERVAL = 'desktop-sync-everything-periodic-metrics-report-interval'
CB_SEV_LAZY_CELESTE_WOODPECKER_NAME = 'desktop-computer-backup-sev-lazy-celeste-woodpecker-killswitch'
CB_DISABLE_DURING_MIGRATION_BACKUP_SURVEY_KILLSWITCH = 'desktop-cboa-migration-disable-survey-killswitch'
CB_ALLOW_BREAK_ANCHOR_ON_ONE_WAY_SYNC_REMEDIATION = 'desktop-allow-break-anchor-on-one-way-sync-remediation'
CB_ANCHOR_INVARIANT_CHECK_INTERVAL_DEFAULT = 3600
CB_IC_WAIT_AFTER_INITIAL_SETUP_SEC = 300
CB_PERIODIC_BACKUP_INTERVAL_MINUTES_DEFAULT = 17
CB_REBIND_WAIT_AFTER_INITIAL_SETUP_SEC = 30
CB_SCHEDULED_BACKUP_POLLING_INTERVAL_MINUTES_DEFAULT = 15
CB_USAGE_REPORT_INTERVAL_HOURS_DEFAULT = 24
CONFIG_KEY_COMPUTER_BACKUP_ACTIVE_ACCOUNT_ID = 'desktop-computer-backup-active-account-id'
CONFIG_KEY_COMPUTER_BACKUP_DEVICE_STATE = 'desktop-computer-backup-device-state'
CONFIG_KEY_COMPUTER_BACKUP_SYNC_CALLBACKS = 'desktop-computer-backup-persisted-sync-callbacks'
CONFIG_KEY_COMPUTER_BACKUP_IC_DISABLE_BACKUP_IC_BACKOFFS = 'desktop-computer-backup-invariant-check-disable-backup-backoffs'
CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_INITIAL_DELAY_SEC = CB_ANCHOR_INVARIANT_CHECK_INTERVAL_DEFAULT
CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_EXP_BASE = 2
CB_ANCHOR_IC_BACKUP_DISABLE_EXP_BACKOFF_MAX = 86400
CB_SYNC_PROGRESS_SERVER_CALL_QUIET_PERIOD_SEC = 30

class ComputerBackupStatus(Enum):
    ENABLED = 0
    DISABLED = 1


class BackupStatus(Enum):
    CREATED = auto()
    ACTIVE = auto()
    BACKUP_PAUSED = auto()
    SYNC_PAUSED = auto()
    BROKEN = auto()
    to_api = (lambda cls = None, backup_status = None: if backup_status == BackupStatus.CREATED:
ComputerBackupApiState.createdif None == BackupStatus.ACTIVE:
ComputerBackupApiState.activeif None == BackupStatus.BACKUP_PAUSED:
ComputerBackupApiState.backup_pausedif None == BackupStatus.SYNC_PAUSED:
ComputerBackupApiState.sync_pausedif None == BackupStatus.BROKEN:
ComputerBackupApiState.brokenraise RequestAssertion('unknown backup status: "{}"'.format(backup_status.name)))()
    from_api = (lambda cls = None, api_status = None: if api_status == ComputerBackupApiState.created:
BackupStatus.CREATEDif None == ComputerBackupApiState.active:
BackupStatus.ACTIVEif None == ComputerBackupApiState.backup_paused:
BackupStatus.BACKUP_PAUSEDif None == ComputerBackupApiState.sync_paused:
BackupStatus.SYNC_PAUSEDif None == ComputerBackupApiState.broken:
BackupStatus.BROKENraise RequestAssertion('unknown backup api status: "{}"'.format(api_status)))()


class ComputerBackupFolderStatus(Enum):
    CREATED = auto()
    ACTIVE = auto()
    BROKEN = auto()
    DELETED = auto()
    to_api = (lambda cls = None, folder_status = None: if folder_status == ComputerBackupFolderStatus.CREATED:
ComputerBackupFolderState.createdif None == ComputerBackupFolderStatus.ACTIVE:
ComputerBackupFolderState.activeif None == ComputerBackupFolderStatus.BROKEN:
ComputerBackupFolderState.brokenif None == ComputerBackupFolderStatus.DELETED:
ComputerBackupFolderState.deletedraise RequestAssertion('unknown folder status: "{}"'.format(folder_status.name)))()


class UpdateAnchorInfoData(NamedTuple):
    initial_timestamp_utc: 'Optional[int]' = 'UpdateAnchorInfoData'


class CbHiveAnchorState(Enum):
    ACTIVE = auto()
    DELETED = auto()
    BROKEN = auto()
    BACKUP_PAUSED = auto()
    SYNC_PAUSED = auto()
    ACCOUNT_OVERQUOTA = auto()
    OFFLINE = auto()
    PERMANENTLY_FAILED = auto()
    ERRED = auto()
    BACKUP_HUNG_TYPE_NUCLEUS_REASON_RESOLVER = auto()
    BACKUP_HUNG_TYPE_NUCLEUS_REASON_REINDEXER = auto()
    BACKUP_HUNG_TYPE_NUCLEUS_REASON_FRONTIER = auto()
    BACKUP_HUNG_TYPE_NUCLEUS_REASON_UNKNOWN = auto()
    BACKUP_HUNG_TYPE_CB_REASON_RESOLVER = auto()
    BACKUP_HUNG_TYPE_CB_REASON_REINDEXER = auto()
    BACKUP_HUNG_TYPE_CB_REASON_FRONTIER = auto()
    BACKUP_HUNG_TYPE_CB_REASON_UNKNOWN = auto()


class ComputerBackupUsage(TypedDict):
    total_file_count: 'Optional[int]' = 'ComputerBackupUsage'


class ComputerBackupUIStrings(UIStrings):
    dismiss_button = UI('Dismiss')
    view_backup_button = UI('View Backup')
    open_settings_button = UI('Open Settings')
    reenable_broken_folder_button = UI('Re-enable')
    reenable_broken_folder_button_custom_folder = UI('Re-add')
    break_single_folder_dialog_title = UI("'%(folder_name)s' has stopped backing up")
    break_single_folder_dialog_body = UI('To continue backing up this folder, move it back to it’s original location and then click <b>Re-enable</b>')
    break_single_folder_dialog_body_custom_folders = UI('To continue backing up this folder, you can re-add it on the folder selection screen')
    missing_broken_single_folder_dialog_body = UI('To continue backing up this folder, click <b>Re-enable</b>')
    break_two_folders_dialog_title = UI("'%(folder_name)s' and 1 other folder have stopped backing up")
    break_multiple_folder_dialog_title = UI("'%(folder_name)s' and '%(folder_count)s' other folders have stopped backing up")
    break_multiple_folder_dialog_body = UI('To continue backing up these folders, move them back to their original location and then click <b>Re-enable</b>')
    break_multiple_folder_dialog_body_custom_folders = UI('To continue backing up these folders, you can re-add them on the folder selection screen')
    missing_broken_multiple_folder_dialog_body = UI('To continue backing up these folders, click <b>Re-enable</b>')
    backup_folder_broken_dialog_title = UI("Your '%(folder_name)s' backup has stopped.")
    backup_folder_broken_dialog_body = UI('The files on your computer are safe. To restart your backup, open Backup Settings and re-select the folder')
    backup_broken_dialog_title = UI("Your '%(backup_name)s' backup has stopped.")
    backup_broken_dialog_body = UI('The files on your computer are safe. To restart your backup, open Backup Settings and restart your backup')
    restoration_folder_suffix = UI('Restored from')

CBFolderId = Union[(OSFolderID, Text)]
CB_CUSTOM_FOLDER_NAME = 'CUSTOM_FOLDER'
CB_CUSTOM_FOLDER_VALUE = 'CustomFolder'
PROGRAM_FILES_FOLDER_NAMES_MAP_WINDOWS = {
    'en_US': 'Program Files',
    'de_DE': 'Programme',
    'es_ES': 'Archivos de programa',
    'fr_FR': 'Programmes',
    'it_IT': 'Programmi',
    'pt_PT': 'Arquivos de Programas',
    'sv_SE': 'Program',
    'da_DK': 'Programmer',
    'no_NO': 'Programfiler',
    'ro_RO': 'Fisiere Program',
    'nl_NL': 'Program Files',
    'ru_RU': 'Program Files',
    'pl_PL': 'Program Files',
    'cs_CZ': 'Program Files',
    'zh_CN': 'Program Files' }
