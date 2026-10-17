# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import
import re
from enum import Enum
from typing import Optional, Text
MYPY = False
if MYPY:
    from dropbox.client.features.transfer.types import FileTransfersApiResponse
TRANSFER_ONBOARDING_CONFIG = 'transfer_onboarding_config'
UNSYNCED_FILENAMES_REGEX = re.compile('\n    ^(?:\\.dropbox\\.cache)\n    |(?:icon\\r)\n    |(?:\\.dropbox)\n    |(?:\\.dropbox\\.attr)\n    |(?:\\.ds_store)\n    |(?:desktop\\.ini)\n    |(?:thumbs\\.db)\n    |(?:\\.dbtmp-.*)\n    |(?:\\.~.*)\n    |(?:~.*\\.tmp)\n    |(?:~\\$.*)\n    $\n', re.VERBOSE | re.IGNORECASE)
TRANSFER_MAX_FILE_NUM = 80
MAX_CONCURRENT_BLOCK_UPLOADS = 6
MAX_FILES_TO_COMMIT = 10
MAX_BLOCKS_TO_COMMIT = 128
MAX_UPLOAD_RATE_SAMPLES = 5
MIN_UPLOAD_RATE_SAMPLES = 1
LOCAL_PATH_TO_LOOKUP_BATCH_SIZE = 500
DEFAULT_TRANSFER_TTL_DAYS = 7
BYTES_IN_GB = 1073741824
UPLOAD_NUM_FILES_WARNING_THRESHOLD = 500
SEND_BY_EMAIL_LIMIT_NUM_RECIPIENTS = 50
SEND_BY_EMAIL_LIMIT_MESSAGE_LENGTH = 150
EXPIRATION_OPTION_METADATA_NAME = 'FILE_TRANSFER_EXPIRATION_OPTION'
SHOULD_NOTIFY_CREATOR_ON_DOWNLOAD_METADATA_NAME = 'FILE_TRANSFER_SHOULD_NOTIFY_CREATOR_ON_DOWNLOAD'

class FileTransferEntryPoint(Enum):
    FINDER_CONTEXT_MENU = 'finder_context_menu'
    FILE_TRANSFER_MODAL = 'file_transfer_modal'


class TransferInadequatePermissionsError(Exception):
    pass


class TransferTooManyItemsError(Exception):
    pass


class TransferUnsyncedItemsError(Exception):
    pass


class TransferEventType(Enum):
    TRANSFER_ADD_MENU_ITEM_EXPOSED = 'transfer_add_menu_item_exposed'
    TRANSFER_ADD_MENU_ITEM_CLICKED = 'transfer_add_menu_item_clicked'
    TRANSFER_ADD_MENU_ITEM_FAILED = 'transferS_add_menu_item_failed'


class FileTransfersFileNotFoundError(Exception):
    pass


class FileTransfersApiErrorBase(Exception):
    pass
# WARNING: Decompyle incomplete


class FileTransfersApiServerError(FileTransfersApiErrorBase):
    pass


class FileTransfersApiTooManyEmailsError(FileTransfersApiErrorBase):
    pass


class FileTransfersApiTransientError(FileTransfersApiErrorBase):
    pass


class FileTransfersApiUnknownError(FileTransfersApiErrorBase):
    pass

