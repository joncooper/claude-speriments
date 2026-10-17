# Source Generated with Decompyle++
# File: strings.pyc (Python 3.11)

from typing import cast, List, Optional, Text
from dropbox.client.features.sync_error.model.common import SyncErrorType, SyncStuckEvents
from dropbox.client.features.sync_error.model.sync_error_logger import SyncErrorLogger
from dropbox.client.features.utils.open_program_name import open_program_name
from dropbox.client.ui.common.strings import AccountString, UI, UIStrings
from dropbox.exception.reporting import report_assertion_error
from dropbox.foundation.context.user import UserContext
from dropbox.i18n import trans, ungettext
from dropbox.sync_engine_boundary.constants import SyncDirection

class SyncErrorStrings(UIStrings):
    ACCOUNT_TITLE = AccountString('<Personal>')
    ENTRY_LEARN_BUTTON_TEXT = UI('Learn more')
    ENTRY_VIEW_FILE_BUTTON_TEXT = UI('View file')
    ENTRY_OPEN_FOLDER_BUTTON_TEXT = UI('Go to folder')
    ENTRY_SHOW_IN_FOLDER_BUTTON_TEXT = UI('Show in folder')
    OPEN_PERMISSIONS_BUTTON = UI('Open permissions')
    ERROR_DESC_INVALID_UPLOAD = UI("Couldn't upload this file. Remove special characters like  /\\.”<>:|?* from filename.")
    ERROR_DESC_INVALID_DOWNLOAD = UI("Couldn't download this file. Remove special characters like  /\\.”<>:|?* from filename.")
    ERROR_FILEPROVIDER_UNHANDLED = UI("Dropbox can't sync this file or folder.")
    ERROR_FILEPROVIDER_NO_PERMISSIONS = UI("Dropbox can't access or modify this file or folder.")
    ERROR_FILEPROVIDER_CONFLICT = UI("Dropbox can't sync this file or folder. Rename this file or folder, or move it out of Dropbox.")
    ERROR_LISTING_CLIENT_KEY_ENROLLMENT = UI("Encrypted Folder enrollment pending. Your Dropbox won't sync until your client is enrolled.")
    ERROR_IN_USE = UI('Unable to sync while file is in use by %(program)s. Close the file to resume syncing.')
    ERROR_IN_USE_FALLBACK = UI('Unable to sync while file is in use. Close the file to resume syncing.')
    ERROR_IN_USE_FOLDER = UI('Unable to sync while file in this folder is in use by %(program)s. Close the file to resume syncing.')
    ERROR_IN_USE_FOLDER_FALLBACK = UI('Unable to sync while file in this folder is in use. Close the file to resume syncing.')
    ERROR_HARDWARE = UI('Hardware error—unable to sync. Click Learn more to resolve the issue.')
    ERROR_VIRUS_DETECTED = UI('Your virus software prevented this file from syncing. Adjust the software settings to resume.')
    ERROR_PERMISSIONS = UI('To sync this file, give Dropbox permission to access it.')
    ERROR_PERMISSIONS_FOLDER = UI('To sync this folder, give Dropbox permission to access it.')
    ERROR_CLOUD_DOC_IN_ENCRYPTED_FOLDER = UI('Cloud docs are not supported in encrypted folders. In this location it can not be uploaded to your Dropbox. Move the file to a different location.')
    ERROR_ENCRYPTED_FILE_CONFLICT = UI('This encrypted file was modified locally and/or remotely. Move the local version to a secure location to download the remote version.')
    ERROR_ENCRYPTED_FOLDER_CONFLICT = UI('This encrypted folder was modified locally and/or remotely. Move the local version to a secure location to download the remote version.')
    ERROR_SYMLINK_IN_ENCRYPTED_FOLDER = UI('Symlinks are not supported in encrypted folders. In this location it can not be uploaded to your Dropbox. Move it to a different location.')
    ERROR_FILE_TOO_LARGE = UI('Unable to sync this file because it exceeds the size limit of 2TB.')
    ERROR_CLOUDFILES_PROVIDER_INTERFERENCE = UI("Dropbox can't sync this file because it already belongs to another sync provider. Move your Dropbox to another location and try again.")
    ERROR_CLOUDFILES_PROVIDER_INTERFERENCE_FOLDER = UI("Dropbox can't sync this folder because it already belongs to another sync provider. Move your Dropbox to another location and try again.")
    ERROR_OVER_QUOTA = UI("Can't sync file—not enough storage")
    ERROR_OQ_COMMIT_PREVENTED = UI("Can't sync file—not enough storage")
    ERROR_TEAM_FOLDER_OVER_QUOTA = UI("Can't sync file—not enough space in folder")
    get_error_count_string = (lambda error_count = None: if error_count == 0:
trans('No issues')ungettext('%(error_count)s issue', '%(error_count)s issues', error_count) % dict(error_count = error_count))()
    get_error_description = (lambda type, direction = None, fs_path = None, is_directory = staticmethod, open_program_names = ('type', 'SyncErrorType', 'direction', 'int', 'fs_path', 'Text', 'is_directory', 'bool', 'open_program_names', 'Optional[List[str]]', 'return', 'Text'): if type == SyncErrorType.PERMISSION_DENIED:
if is_directory:
SyncErrorStrings.ERROR_PERMISSIONS_FOLDERNone.ERROR_PERMISSIONSif None == SyncErrorType.INVALID_FILENAME:
SyncErrorStrings.ERROR_DESC_INVALID_UPLOAD if direction == SyncDirection.UP else SyncErrorStrings.ERROR_DESC_INVALID_DOWNLOADif None == SyncErrorType.FILEPROVIDER_UNHANDLED:
SyncErrorStrings.ERROR_FILEPROVIDER_UNHANDLEDif None == SyncErrorType.FILEPROVIDER_NO_PERMISSIONS:
SyncErrorStrings.ERROR_FILEPROVIDER_NO_PERMISSIONSif None == SyncErrorType.FILEPROVIDER_CONFLICT:
SyncErrorStrings.ERROR_FILEPROVIDER_CONFLICTif None == SyncErrorType.LISTING_CLIENT_KEY_ENROLLMENT:
SyncErrorStrings.ERROR_LISTING_CLIENT_KEY_ENROLLMENTif None == SyncErrorType.VIRUS_DETECTED:
SyncErrorStrings.ERROR_VIRUS_DETECTEDif None == SyncErrorType.FILE_CORRUPTION_OR_HARDWARE_ERROR:
SyncErrorStrings.ERROR_HARDWARE# WARNING: Decompyle incomplete
)()


def get_actor_account_label(context = None):
    return context.account.render_string(AccountString('[<personal>]'))

