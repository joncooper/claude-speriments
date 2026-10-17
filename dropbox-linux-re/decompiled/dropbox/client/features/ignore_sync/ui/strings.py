# Source Generated with Decompyle++
# File: strings.pyc (Python 3.11)

from typing import NamedTuple
from dropbox.client.ui.common.strings import UI, UIStrings
from dropbox.sync_engine_boundary.types import SetPathIgnoredStateErrorReason

class BackupIgnoreSyncAlert(UIStrings):
    headline = UI('Don’t sync to dropbox.com?')
    headline_shared = UI('Don’t sync shared item to dropbox.com?')
    description = UI("%(name)s won’t be available on your other devices. Also, it won't take up Dropbox storage space.")
    description_shared = UI('%(name)s won’t be available to other members or on your other devices. ')
    confirm = UI("Don't sync")
    cancel = UI('Cancel')


class BackupUnIgnoreSyncAlert(UIStrings):
    headline = UI('Start syncing to dropbox.com again?')
    description = UI('%(name)s will be available on your other devices and take up Dropbox storage space.')
    description_shared = UI('%(name)s will be available on your other devices. Also, it will be shared with previous members.')
    confirm = UI('Start syncing')
    cancel = UI('Cancel')


class BackupAlertStrings(NamedTuple):
    cancel: 'UI' = 'BackupAlertStrings'


def backup_ignore_alert_strings(ignore_state = None, is_shared = None):
    return {
        True: {
            True: BackupAlertStrings(BackupIgnoreSyncAlert.headline_shared, BackupIgnoreSyncAlert.description_shared, BackupIgnoreSyncAlert.confirm, BackupIgnoreSyncAlert.cancel),
            False: BackupAlertStrings(BackupIgnoreSyncAlert.headline, BackupIgnoreSyncAlert.description, BackupIgnoreSyncAlert.confirm, BackupIgnoreSyncAlert.cancel) },
        False: {
            True: BackupAlertStrings(BackupUnIgnoreSyncAlert.headline, BackupUnIgnoreSyncAlert.description_shared, BackupUnIgnoreSyncAlert.confirm, BackupUnIgnoreSyncAlert.cancel),
            False: BackupAlertStrings(BackupUnIgnoreSyncAlert.headline, BackupUnIgnoreSyncAlert.description, BackupUnIgnoreSyncAlert.confirm, BackupUnIgnoreSyncAlert.cancel) } }[ignore_state][is_shared]


class IgnoreSyncConfirmation(UIStrings):
    headline = UI('Don’t sync to dropbox.com?')
    description = UI('Are you sure you want %(name)s to stop syncing to dropbox.com?')
    confirm = UI("Don't sync")
    cancel = UI('Cancel')
    checkbox_description = UI("Don't warn me again")


class IgnoreSyncError(UIStrings):
    headline = UI('%(name)s will continue syncing')
    acknowledge = UI('Ok')
    is_placeholder_reason = UI("Online-only files cannot stop syncing until they're made available offline.")
    has_placeholders_reason = UI('This folder has online-only files. Make them available offline to stop syncing to the cloud.')
    is_cloud_doc_reason = UI('Cloud document files cannot stop syncing because their contents can’t be made available offline.')
    has_cloud_docs_reason = UI('This folder has cloud document files. Move the cloud document files to a different location and try again.')


def get_ignore_sync_error_reason_string(error_reason = None):
    if error_reason == SetPathIgnoredStateErrorReason.IS_PLACEHOLDER:
        return IgnoreSyncError.is_placeholder_reason
    if None == SetPathIgnoredStateErrorReason.IS_CLOUD_DOC:
        return IgnoreSyncError.is_cloud_doc_reason
    if None == SetPathIgnoredStateErrorReason.HAS_PLACEHOLDERS:
        return IgnoreSyncError.has_placeholders_reason
    return None.has_cloud_docs_reason

