# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import Enum
from string import ascii_letters, digits
from typing import Text, Union
MAX_CLOUD_DOCS_FILE_SIZE = 10485760
MAX_CLOUD_DOCS_RECALL_TIME = 30
HOST_ID_HASH_LENGTH = 7
CLOUD_DOC_ID_LENGTH = 21
CLOUD_DOC_ID_CHARS = ascii_letters + digits + '-_'
DROPBOX_CLOUD_CONTENT_ONLY_PLAT = 'dropbox_cloud_content'
DROPBOX_CLOUD_CONTENT_ONLY_KEY = 'type'
CLOUD_DOC_URL_PATH_PREFIX = '/cloud_docs/view/'
CLOUD_DOCS_PERF_METRICS_NAMESPACE = 'cloud_docs_perf'

class CloudDocsValidationErrorCode(Enum):
    FILE_NOT_EXIST = 'file_not_exist'
    FILE_TOO_BIG = 'file_too_big'
    INVALID_EXTENSION = 'invalid_extension'
    INVALID_JSON = 'invalid_json'
    INVALID_PATH = 'invalid_path'
    MALFORMED_CLOUD_DOCS_URL = 'malformed_cloud_docs_url'
    NO_FILEID = 'no_fileid'
    NO_URL = 'no_url'
    OPEN_ERROR = 'open_error'
    OPEN_TIMEOUT = 'open_timeout'
    UNKNOWN_EXCEPTION = 'unknown_exception'
    UNKNOWN_URL = 'unknown_url'


class CloudDocsEventName(Enum):
    OPEN = 'open'
    OPEN_FAILURE = 'open_failure'
    CREATE = 'create'
    FSW_MOVE = 'fsw_move'
    MOVE_TO_TRASH = 'move_to_trash'
    WINDOWS_INSTALL = 'windows_install'


class CloudDocsFileLocation(Enum):
    ROOT_NAMESPACE = 'root_namespace'
    SHARED_FOLDER = 'shared_folder'
    TRASH = 'trash'
    DOWNLOADS = 'downloads'
    APP_DATA = 'app_data'
    OUTSIDE_DROPBOX = 'outside_dropbox'


class CloudDocsUrlType(Enum):
    DROPBOX_CLOUD_DOC = 'dropbox_cloud_doc'
    DROPBOX_DEV_CLOUD_DOC = 'dropbox_dev_cloud_doc'
    DROPBOX_UNKNOWN = 'dropbox_unknown'
    UNKNOWN = 'unknown'


class CloudDocsOpenMiscFailure(Enum):
    DISABLED = 'disabled'
    SHORT_PATH = 'win_short_path_error'
    TIMEOUT = 'timeout'
    UNKNOWN = 'unknown'

CloudDocsOpenFailureReason = Union[(CloudDocsValidationErrorCode, CloudDocsOpenMiscFailure)]

class CloudDocsWindowsInstallationStatus(Enum):
    INSTALLED = 'installed'
    REPAIRED = 'repaired'
    VALIDATION_FAILED = 'validation_failed'
    REPAIR_VALIDATION_FAILED = 'repair_validation_failed'
    REPAIR_FAILED = 'repair_failed'
    REPAIR_FAILED_SILENTLY = 'repair_failed_silently'


class CloudEditor(Enum):
    GOOGLE_DOCS = 'gdoc'
    GOOGLE_SLIDES = 'gslides'
    GOOGLE_SHEETS = 'gsheet'
    MICROSOFT_WORD = 'word'
    MICROSOFT_POWERPOINT = 'powerpoint'
    MICROSOFT_EXCEL = 'excel'
    
    def to_apiv2_stone_text(self = None):
        mapping = {
            CloudEditor.MICROSOFT_EXCEL: 'excel_online',
            CloudEditor.MICROSOFT_POWERPOINT: 'powerpoint_online',
            CloudEditor.MICROSOFT_WORD: 'word_online',
            CloudEditor.GOOGLE_SHEETS: 'google_sheets',
            CloudEditor.GOOGLE_SLIDES: 'google_slides',
            CloudEditor.GOOGLE_DOCS: 'google_docs' }
        return mapping[self]


