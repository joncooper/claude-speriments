# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

import plistlib
from enum import Enum, unique
from dropbox.client.features.backup_instance.types import RootValidationResult
from dropbox.client.ui.common.strings import UI, UIStrings
TEST_ONLY_BI_FEATURE_GATE_NAME = 'desktop-backup-instance-test-only'
TEST_ONLY_DISABLED_VARIANT = 'DISABLED'
BI_FEATURE_OFF_VARIANTS = ('OFF', 'CONTROL')
CBOA_PAUSE_ON_RELINK_KILLSWITCH = 'desktop-computer-backup-pause-on-relink-kill-switch'
BILocalConfigKeys = <NODE:12>()
BI_SYNC_FOLDER = 'bi_sync'
BACKUP_INSTANCE_SHUTDOWN_PAUSE_TIME_SEC = 5
BACKUP_INSTANCE_AUTO_RELINK_INTERVAL_DEFAULT = 900
ACCEPTABLE_NEW_INSTANCE_VALIDATION_RESULTS = (RootValidationResult.MISSING_FOLDER, RootValidationResult.EMPTY_FOLDER, RootValidationResult.EMPTY_DOT_DROPBOX, RootValidationResult.MATCHING_DOT_DROPBOX)
BI_ROOT_INVALID_HC_ARTICLE_URL = 'https://help.dropbox.com/installs-integrations/desktop/dropbox-backup-faq#stoppedworking'

class BackupInstanceStrings(UIStrings):
    root_invalid_dialog_title = UI('Dropbox Backup has stopped working')
    root_invalid_dialog_body = UI("Don't worry—your files are safe. Follow the steps in the help center to get back up and running.")
    root_invalid_not_now_btn = UI('Not now')
    root_invalid_help_center_btn = UI('Help center')

APPLE_TIME_MACHINE_EXCLUDE_ATTR_NAME = 'com.apple.metadata:com_apple_backup_excludeItem'
APPLE_TIME_MACHINE_EXCLUDE_ATTR_VALUE = plistlib.dumps('com.apple.backupd', fmt = plistlib.PlistFormat.FMT_BINARY)
