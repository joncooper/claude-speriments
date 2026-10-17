# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

import re
from typing import Dict
from dropbox.client.features.backup_app.view_model.bridge_gen.backup_schedule import BackupSchedule
from dropbox.client.features.backup_app.view_model.bridge_gen.schedule_detail import ScheduleDetail
from dropbox.client.features.backup_app.view_model.bridge_gen.schedule_type import ScheduleType
from dropbox.proto.nucleus.device_anchor_pb2 import BreakBackupReason
from dropbox.sync_engine_boundary.types import DeviceAnchorUnbindReason
DAYS_OF_THE_WEEK = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday']
CB_ANCHOR_EXTENSION = '.dbx-computer-backup'
EDB_ANCHOR_EXTENSION = '.dbx-external-drive'
SYNC_DBXIGNORE = 'desktop-nucleus-sync-dbxignore'
DBXIGNORE_FILENAME = '.dbxignore'
DEFAULT_IGNORED_GLOBS = ('.dropbox.device', '.localized', '.volumeicon.icns', '.fseventsd', '.spotlight-v100', '.documentrevisions-v100', '.temporaryitems', '.trashes', '.com.apple.timemachine.donotpresent', 'system volume information', '$recycle.bin', 'filehistory', 'toolkit', '.dbxignore', '**/*.paper', '**/*.gdoc', '**/*.gsheet', '**/*.gslides', '**/._*')
DEFAULT_IGNORED_GLOBS_WITH_DBXIGNORE = DEFAULT_IGNORED_GLOBS + (DBXIGNORE_FILENAME,)
NUCLEUS_UNSYNCED_FILENAMES_REGEX = re.compile('\n    ^(?:\\.dropbox\\.cache)\n    |(?:icon\\r)\n    |(?:\\.dropbox)\n    |(?:\\.dropbox\\.attr)\n    |(?:\\.ds_store)\n    |(?:desktop\\.ini)\n    |(?:thumbs\\.db)\n    |(?:\\.dbtmp-.*)\n    |(?:\\.~.*)\n    |(?:~.*\\.tmp)\n    |(?:~\\$.*)\n    $\n', re.VERBOSE | re.IGNORECASE)
CLOUD_DOCS_REGEX = re.compile('\n    (?:.*\\.paper$)\n    |(?:.*\\.gdoc$)\n    |(?:.*\\.gsheet$)\n    |(?:.*\\.gslides$)\n', re.VERBOSE | re.IGNORECASE)
APPLE_DOUBLE_REGEX = re.compile('\n    (?:\\._.*$)\n', re.VERBOSE | re.IGNORECASE)
CONFIG_KEY_COMPUTER_BACKUP_SCHEDULE = 'desktop-cboa-schedule'
CONFIG_KEY_COMPUTER_BACKUP_SCHEDULE_LAST_VALUES = 'desktop-cboa-schedule-last-value'
CONFIG_KEY_COMPUTER_BACKUP_LAST_JOB_TIME = 'desktop-cboa-last-job-time'
CONFIG_KEY_EXTERNAL_DRIVE_BACKUP_SCHEDULE = 'desktop-edb-schedule'
CONFIG_KEY_EXTERNAL_DRIVE_BACKUP_SCHEDULE_LAST_USER_SELECTION_VALUES = 'desktop-edb-schedule-last-user-selection-value'
CONFIG_KEY_EXTERNAL_DRIVE_BACKUP_LAST_JOB_TRIGGERED_TIME = 'desktop-edb-last-job-triggered-time'
DEFAULT_SCHEDULE = BackupSchedule(type = ScheduleType.PERIODIC, schedule = ScheduleDetail(cadence = 15, custom = []))
DEFAULT_LARGE_DRIVE_SCHEDULE = BackupSchedule(type = ScheduleType.DAILY, schedule = ScheduleDetail([], None, None, 9, 0))
BREAK_BACKUP_REASON_TO_DEVICE_ANCHOR_UNBIND_REASON: 'Dict[BreakBackupReason.V, DeviceAnchorUnbindReason]' = {
    BreakBackupReason.CBOA_ONE_WAY_SYNC_CONFLICTED_ANCHOR: DeviceAnchorUnbindReason.CBOA_ONE_WAY_SYNC_CONFLICTED_ANCHOR,
    BreakBackupReason.CBOA_ABANDONED_ANCHORS: DeviceAnchorUnbindReason.CBOA_ABANDONED_ANCHORS,
    BreakBackupReason.SEAMLESS_FISSION_MIGRATION_REQUESTED: DeviceAnchorUnbindReason.SEAMLESS_FISSION_MIGRATION,
    BreakBackupReason.FP_PREMIGRATION_REQUESTED: DeviceAnchorUnbindReason.FILE_PROVIDER_MIGRATION }
