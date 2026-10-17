# Source Generated with Decompyle++
# File: bridge_dicts.pyc (Python 3.11)

from typing import List, Literal, Optional, Text, TypedDict

class ContactTokenVariantWithReason(TypedDict):
    reason: 'Optional[str]' = 'ContactTokenVariantWithReason'


class ContactToken(TypedDict):
    initials: 'Optional[str]' = 'ContactToken'


class DesktopFileInfo(TypedDict):
    errorType: 'Optional[str]' = 'DesktopFileInfo'

FileTransferServiceErrorTypes = Literal[('file_not_found', 'too_many_emails', 'operation_not_permitted', 'invalid_argument', 'path_conversion_error', 'transient_error', 'email_not_verified', 'unknown_error')]

class FileTransferServiceError(TypedDict):
    errorMessage: 'str' = 'FileTransferServiceError'


class FileTransferSendEmailError(FileTransferServiceError):
    failedEmailAddresses: 'List[Text]' = 'FileTransferSendEmailError'

