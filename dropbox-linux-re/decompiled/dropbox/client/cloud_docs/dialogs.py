# Source Generated with Decompyle++
# File: dialogs.pyc (Python 3.11)

from __future__ import absolute_import
from collections import defaultdict
from enum import Enum
from typing import Dict, List, NamedTuple, Sequence, Text, Tuple
from dropbox.client.cloud_docs.constants import CloudDocsOpenFailureReason, CloudDocsOpenMiscFailure, CloudDocsValidationErrorCode
from dropbox.client.cloud_docs.strings import CloudDocsErrorStrings
from dropbox.exception.reporting import report_bad_assumption
CloudDocsErrorDialog = NamedTuple('CloudDocsErrorDialog', [
    ('title', Text),
    ('caption', Text)])

class CloudDocsErrorDialogType(Enum):
    NO_FILEID = 'no_fileid'
    NO_PERMISSIONS = 'no_permissions'
    BAD_FORMAT = 'bad_format'
    NO_LONGER_EXISTS = 'no_longer_exists'
    TIMEOUT = 'timeout'
    INVALID_EXTENSION = 'invalid_extension'
    UNKNOWN_REASON = 'unknown_reason'


def get_open_failure_dialogs(open_failures = None):
    files_by_dialog_type = defaultdict(list)
    for file_name, failure_reason in open_failures:
        files_by_dialog_type[_failure_reason_to_dialog_type(file_name, failure_reason)].append(file_name)
        dialogs = []
        for dialog_type, file_names in files_by_dialog_type.items():
            dialogs.append(_dialog_type_to_dialog(dialog_type, file_names))
            return dialogs


def _failure_reason_to_dialog_type(file_name = None, failure_reason = None):
    if failure_reason == CloudDocsValidationErrorCode.NO_FILEID:
        return CloudDocsErrorDialogType.NO_FILEID
    if None == CloudDocsValidationErrorCode.OPEN_ERROR:
        return CloudDocsErrorDialogType.NO_PERMISSIONS
    if None in (CloudDocsValidationErrorCode.INVALID_JSON, CloudDocsValidationErrorCode.FILE_TOO_BIG, CloudDocsValidationErrorCode.NO_URL, CloudDocsValidationErrorCode.MALFORMED_CLOUD_DOCS_URL, CloudDocsValidationErrorCode.UNKNOWN_URL):
        return CloudDocsErrorDialogType.BAD_FORMAT
    if None == CloudDocsValidationErrorCode.FILE_NOT_EXIST:
        return CloudDocsErrorDialogType.NO_LONGER_EXISTS
    if None in (CloudDocsValidationErrorCode.OPEN_TIMEOUT, CloudDocsOpenMiscFailure.TIMEOUT):
        return CloudDocsErrorDialogType.TIMEOUT
    if None == CloudDocsValidationErrorCode.INVALID_EXTENSION:
        return CloudDocsErrorDialogType.INVALID_EXTENSION
    if None in (CloudDocsValidationErrorCode.UNKNOWN_EXCEPTION, CloudDocsValidationErrorCode.INVALID_PATH, CloudDocsOpenMiscFailure.DISABLED, CloudDocsOpenMiscFailure.SHORT_PATH, CloudDocsOpenMiscFailure.UNKNOWN):
        return CloudDocsErrorDialogType.UNKNOWN_REASON
    report_bad_assumption('Unknown failure reason %r', failure_reason)
    return CloudDocsErrorDialogType.UNKNOWN_REASON


def _dialog_type_to_dialog(dialog_type = None, file_names = None):
    if dialog_type == CloudDocsErrorDialogType.NO_FILEID:
        return CloudDocsErrorDialog(title = CloudDocsErrorStrings.no_fileid_title(file_names), caption = CloudDocsErrorStrings.no_fileid_caption(file_names))
    if None == CloudDocsErrorDialogType.NO_PERMISSIONS:
        return CloudDocsErrorDialog(title = CloudDocsErrorStrings.generic_title(file_names), caption = CloudDocsErrorStrings.no_permissions_caption(file_names))
    if None == CloudDocsErrorDialogType.BAD_FORMAT:
        return CloudDocsErrorDialog(title = CloudDocsErrorStrings.generic_title(file_names), caption = CloudDocsErrorStrings.bad_format_caption(file_names))
    if None == CloudDocsErrorDialogType.NO_LONGER_EXISTS:
        return CloudDocsErrorDialog(title = CloudDocsErrorStrings.no_longer_exists_title(file_names), caption = CloudDocsErrorStrings.no_longer_exists_caption(file_names))
    if None == CloudDocsErrorDialogType.TIMEOUT:
        return CloudDocsErrorDialog(title = CloudDocsErrorStrings.timeout_title(file_names), caption = CloudDocsErrorStrings.timeout_caption(file_names))
    if None == CloudDocsErrorDialogType.INVALID_EXTENSION:
        return CloudDocsErrorDialog(title = CloudDocsErrorStrings.generic_title(file_names), caption = CloudDocsErrorStrings.invalid_extension_caption(file_names))
    if None == CloudDocsErrorDialogType.UNKNOWN_REASON:
        return CloudDocsErrorDialog(title = CloudDocsErrorStrings.generic_title(file_names), caption = CloudDocsErrorStrings.unknown_reason_caption)
    report_bad_assumption('Unknown dialog type %r' % dialog_type)
    return CloudDocsErrorDialog(title = CloudDocsErrorStrings.generic_title(file_names), caption = CloudDocsErrorStrings.unknown_reason_caption)

