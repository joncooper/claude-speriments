# Source Generated with Decompyle++
# File: unlink_handlers.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from dropbox.event import report
from dropbox.exception.exception_decorators import handle_exceptions
from dropbox.trace import TRACE

class UnlinkReason(Enum):
    UNKNOWN = 'Unknown'
    HOST_ID_CHANGED = 'HostIdChanged'
    MULTIACCOUNT_DISABLED = 'MultiaccountDisabled'
    REMOTE_UNLINK = 'RemoteUnlink'
    SECONDARY_UNPAIRED = 'SecondaryUnpaired'
    USER_REQUESTED = 'UserRequested'
    ERR_MISMATCH_SECONDARY_UID = 'ErrorMismatchSecondaryUid'
    ERR_NO_SYNC_ROOT = 'ErrorMissingSyncRoot'
    ERR_SYNC_ROOT_FAILED_TRANSITION = 'ErrorFailedTransitionSyncRoot'
    ERR_SYNC_ROOT_FAILED_MIGRATION = 'ErrorFailedConvertSyncRoot'
    ERR_SHADOW_MIGRATION_CUTOVER_FAILED = 'ErrorShadowMigrationCutoverFailed'
    ERR_MISSING_FOLDER_USERPROMPT = 'ErrorMissingFolderUserPromptedRelink'
    ERR_MISSING_DRIVE_USERPROMPT = 'ErrorMissingDriveUserPromptedRelink'
    ERR_MISSING_FOLDER = 'ErrorMissingDropboxFolder'
    ERR_BAD_FOLDER = 'ErrorBadLocation'
    ERR_REALLY_BAD_MOVE = 'ErrorReallyBadMoveDropboxFolder'
    ERR_MOVECRASHED = 'ErrorMoveCrashedDropboxFolder'
    ERR_SECONDARY_MOVE_FAILED = 'ErrorSecondaryFolderMoveFailed'
    ERR_MISMATCH_PRI_SEC_LINKSTATE = 'ErrorActiveSecondaryWithUnlinkedPrimary'
    CERT_PINNING_DISABLED = 'CertPinningDisabled'
    ERR_WHEN_CHECK_MERGE = 'ErrorWhenCheckMerge'
    ERR_WHEN_LINKING = 'ErrorWhenLinking'
    ERR_INVALID_SYNC_ROOT = 'ErrorInvalidSyncRoot'
    ERR_SYNC_ROOT_CONFLICT = 'ErrorSyncRootConflict'
    ERR_OAUTH_EXCHANGE_FAILED = 'ErrorOAuthExchangeFailed'

report_unlink_event = (lambda reason_code, is_primary = (True,): TRACE('Reporting client-unlink_event to clogger, reason code %s for %s account', reason_code.value, 'primary' if is_primary else 'secondary')report('unlink_event', reason_code = reason_code.value, is_primary = is_primary))()
