# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from enum import Enum, unique
from typing import Set
from dropbox.client.ui.common.strings import UI, UIStrings
TOP_LEVEL_NAMES_TO_IGNORE: 'Set[str]' = {
    'icon',
    '.dropbox',
    '.ds_store',
    '.localized',
    'desktop.ini',
    '.dropbox.cache'}
BI_CONFLICTED_ENTRY_SYNCING_DEFER_TIME_GATE_NAME = 'desktop-backup-auto-selsync-conflicts-syncing-defer-minutes'
BI_CONFLICTED_ENTRY_MAX_SELSYNCS_GATE_NAME = 'desktop-backup-auto-selsync-conflicts-max-selsyncs'
BI_AUTO_SEL_SYNC_FEATURE_OFF_VARIANTS = ('OFF', 'CONTROL')
BI_AUTO_SEL_SYNC_INVARIANT_INTERVAL_DEFAULT = 900
BI_CONFLICTED_ENTRY_SYNCING_DEFER_TIME_SEC_DEFAULT = 14400
BI_CONFLICTED_ENTRY_MAX_SELSYNCS_DEFAULT = 5
AUTO_SEL_SYNC_GATE_NAME = 'desktop-backup-auto-selsync-fss'
AUTO_SEL_SYNC_FEATURE_OFF_VARIANTS = ('OFF', 'CONTROL')
AUTO_SEL_SYNC_INVARIANT_INTERVAL_DEFAULT = 3600
AutoSelsyncLocalConfigKeys = <NODE:12>()

class AutoSelSyncUIStrings(UIStrings):
    close_button = UI('Close')
    sel_sync_alert_title = UI('Backups from other devices are no longer accessible in Finder', windows = UI('Backups from other devices are no longer accessible in Explorer'), linux = UI('Backups from other devices are no longer accessible locally'))
    sel_sync_alert_body = UI("You can still view all your backups at once on dropbox.com/backup/all or in Backup settings. <a href='https://help.dropbox.com/installs-integrations/desktop/how-to-use-dropbox-backup'>Learn more</a>")
    sel_sync_alert_backup_on_web_btn = UI('Backup on web')
    sel_sync_alert_backup_setting_btn = UI('Backup settings')

