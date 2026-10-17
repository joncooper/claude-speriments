# Source Generated with Decompyle++
# File: server_interface.pyc (Python 3.11)

from enum import Enum
from typing import Any, Callable, cast, Dict, List, Optional, Text, Tuple, Type, Union
from build_number import BUILD_CHANNEL
from build_number.platform import IS_WINDOWS
from dropbox.api.v2.datatypes.device_sync import SyncFolderType
from dropbox.client.features.computer_backup.constants import CB_CUSTOM_FOLDER_NAME
from dropbox.client.features.sync_everything.constants import BackupDisableType, DeviceID, DeviceStatus
from dropbox.client.features.sync_everything.v3.async_tools import future_function
from dropbox.client.features.sync_everything.v3.device_state import DeviceState, KnownFolder
from dropbox.client.features.sync_everything.v3.errors import convert_to_failure, RecoveryActionType, RequestAssertion, RequestFailedException, SyncEverythingException
from dropbox.client.features.sync_everything.v3.event_label import EventLabel
from dropbox.client.features.sync_everything.v3.utils import is_offline, SyncEverythingExcludedFileList
from dropbox.client.features.sync_everything.view_model.bridge_gen.anchor_folder import AnchorFolder
from dropbox.client.features.sync_everything.view_model.bridge_gen.backup_info import BackupInfo
from dropbox.client.features.sync_everything.view_model.bridge_gen.device_sync_status import DeviceSyncStatus
from dropbox.client.features.sync_everything.view_model.bridge_gen.list_backups_result import ListBackupsResult
from dropbox.client.features.sync_everything.view_model.bridge_gen.platform_type import PlatformType
from dropbox.client.features.sync_everything.view_model.bridge_gen.redirect_request_status import RedirectRequestStatus
from dropbox.client.features.sync_everything.view_model.constants import KNOWN_FOLDER_NAME_MAP
from dropbox.client_api.exceptions import DropboxServerError, HTTP400Error, HTTP409Error, HTTP429Error, HTTP500Error, TransientNetworkError
from dropbox.exception.severity import Severity
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.foundation.transitional import make_delayed_network_call
from dropbox.foundation.types.ids import FileID
from dropbox.model.types import FileId
from dropbox.platform import IS_MAC
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.types import RegexExpectedErrorPair
ServerJSON = Dict[(Text, Any)]

class ServerParseException(SyncEverythingException):
    pass


class RestoreNotReadyException(SyncEverythingException):
    pass


class AsyncCopyTransientException(SyncEverythingException):
    pass
# WARNING: Decompyle incomplete


def os_folder_id_to_api(known_folder = None):
    if known_folder == OSFolderID.DESKTOP:
        res = SyncFolderType.desktop
    elif known_folder == OSFolderID.DOCUMENTS:
        res = SyncFolderType.documents
    elif known_folder == OSFolderID.DOWNLOADS:
        res = SyncFolderType.downloads
    elif known_folder == OSFolderID.MUSIC:
        res = SyncFolderType.music
    elif known_folder == OSFolderID.MOVIES:
        res = SyncFolderType.movies
    elif known_folder == OSFolderID.PICTURES:
        res = SyncFolderType.pictures
    elif known_folder == OSFolderID.VIDEOS:
        res = SyncFolderType.videos
    else:
        raise ValueError('invalid folder type')
    return res


def api_to_os_folder(folder_type = None):
    if folder_type.is_desktop():
        res = OSFolderID.DESKTOP
    elif folder_type.is_documents():
        res = OSFolderID.DOCUMENTS
    elif folder_type.is_downloads():
        res = OSFolderID.DOWNLOADS
    elif folder_type.is_music():
        res = OSFolderID.MUSIC
    elif folder_type.is_movies():
        res = OSFolderID.MOVIES
    elif folder_type.is_pictures():
        res = OSFolderID.PICTURES
    elif folder_type.is_videos():
        res = OSFolderID.VIDEOS
    else:
        raise ValueError('invalid folder type')
    return res


def known_folder_to_tag(known_folder = None):
    kf_map = {
        OSFolderID.MOVIES: 'movies',
        OSFolderID.VIDEOS: 'videos',
        OSFolderID.MUSIC: 'music',
        OSFolderID.DOWNLOADS: 'downloads',
        OSFolderID.PICTURES: 'pictures',
        OSFolderID.DOCUMENTS: 'documents',
        OSFolderID.DESKTOP: 'desktop' }
    return kf_map[known_folder]


def tag_to_known_folder(tag = None):
    tag_map = {
        'desktop': OSFolderID.DESKTOP,
        'documents': OSFolderID.DOCUMENTS,
        'pictures': OSFolderID.PICTURES,
        'downloads': OSFolderID.DOWNLOADS,
        'music': OSFolderID.MUSIC,
        'videos': OSFolderID.VIDEOS,
        'movies': OSFolderID.MOVIES }
    return tag_map[tag]


def tag_to_ux_folder(tag = None):
    inv_known_folder_name_map = KNOWN_FOLDER_NAME_MAP.items()()
    folder = tag_to_known_folder(tag)
    return inv_known_folder_name_map.get(folder, None)


def tag_to_device_sync_status(tag = None):
    tag_map = {
        'enabled': DeviceSyncStatus.ENABLED,
        'disabled': DeviceSyncStatus.DISABLED }
    return tag_map[tag]


def tag_to_platform_type(tag = None):
    tag_map = {
        'unknown': PlatformType.UNKNOWN,
        'mac': PlatformType.MAC,
        'win': PlatformType.WIN }
    return tag_map.get(tag, PlatformType.UNKNOWN)


class ApiError:
    pass


class EmailType(Enum):
    SETUP_COMPLETE = 'setup_complete'
    FIRST_SYNC_COMPLETE = 'first_sync_complete'
    CB_SETUP_COMPLETE_PRODUCT_SURVEY = 'cb_setup_complete_product_survey'


class FolderLookupError(Enum, ApiError):
    value: 'str' = 'FolderLookupError'
    MALFORMED_PATH = 'malformed_path'
    NOT_FOUND = 'not_found'
    NOT_FILE = 'not_file'
    NOT_FOLDER = 'not_folder'
    RESTRICTED_CONTENT = 'restricted_content'
    UNSUPPORTED_CONTENT_TYPE = 'unsupported_content_type'
    from_error = (lambda cls = None, error = None: tag_map = cls.__members__.values()()tag_map[error['folder_lookup_error']['.tag']])()


class DeviceInvalidError(ApiError):
    from_error = (lambda cls = None, error = None: cls())()


class DeviceNotFoundError(ApiError):
    from_error = (lambda cls = None, error = None: cls())()


class DeviceDisabledError(ApiError):
    from_error = (lambda cls = None, error = None: cls())()


class InternalError(ApiError):
    from_error = (lambda cls = None, error = None: cls())()


class DeviceConflictError(Enum, ApiError):
    value: 'str' = 'DeviceConflictError'
    ACCOUNT = 'account'
    NAME = 'name'
    FOLDER = 'folder'
    from_error = (lambda cls = None, error = None: tag_map = cls.__members__.values()()tag_map[error['device_conflict']['.tag']])()


class UpdateConflict(ApiError):
    from_error = (lambda cls = None, error = None: cls())()


class InvalidRequestError(Enum, ApiError):
    value: 'str' = 'InvalidRequestError'
    INVALID_DEVICE_NAME = 'invalid_device_name'
    INVALID_SYNC_FOLDER_NAME = 'invalid_sync_folder_name'
    NO_SYNC_FOLDERS = 'no_sync_folders'
    DUPLICATE_SYNC_FOLDERS = 'duplicate_sync_folders'
    from_error = (lambda cls = None, error = None: tag_map = cls.__members__.values()()tag_map[error['invalid_request']['.tag']])()


class FolderUpdateError(Enum, ApiError):
    value: 'str' = 'FolderUpdateError'
    MALFORMED_PATH = 'malformed_path_update'
    CONFLICT = 'conflict'
    NO_WRITE_PERMISSION = 'no_write_permission'
    INSUFFICIENT_SPACE = 'insufficient_space'
    DISALLLOWED_NAME = 'disallowed_name'
    TEAM_FOLDER = 'team_folder'
    TOO_MANY_WRITE_OPERATIONS = 'too_many_write_operations'
    from_error = (lambda cls = None, error = None: tag_map = cls.__members__.values()()tag_map[error['folder_update_error']['.tag']])()


class AuditLogError(ApiError):
    from_error = (lambda cls = None, error = None: cls())()


class QuotaExemptError(Enum, ApiError):
    value: 'str' = 'QuotaExemptError'
    NOT_ALLOWED = 'not_allowed'
    UNEXEMPT_EXISTING = 'unexempt_existing'
    LOOKUP_DEVICES = 'lookup_devices'
    from_error = (lambda cls = None, error = None: tag_map = cls.__members__.values()()tag_map[error['quota_exempt_error']['.tag']])()


class RestoreBackupError(Enum, ApiError):
    value: 'str' = 'RestoreBackupError'
    NOT_FOUND = 'not_found'
    BACKUP_DISABLED = 'backup_disabled'
    BACKUP_ID_CONFLICT = 'backup_id_conflict'
    MISSING_FOLDER = 'missing_folder'
    DESTINATION_EXISTS = 'destination_exists'
    ASYNC_COPY_FAILED = 'async_copy_failed'
    ASYNC_COPY_TRANSIENT = 'async_copy_transient'
    ASYNC_COPY_INVALID = 'async_copy_invalid'
    RETRY_MISSING_ROOT = 'retry_missing_root'
    RESTORE_NOT_STARTED = 'restore_not_started'
    RESTORE_NOT_READY = 'restore_not_ready'
    from_error = (lambda cls = None, error = None: tag_map = cls.__members__.values()()tag_map[error['restore_backup_error']['.tag']])()


class EnableDeviceError(ApiError):
    from_response = (lambda cls = None, response = None: try:
error = response['error']tag = error['.tag']if tag == 'invalid_request':
error = InvalidRequestError.from_error(error)elif tag == 'device_conflict':
error = DeviceConflictError.from_error(error)elif tag == 'folder_lookup_error':
error = FolderLookupError.from_error(error)elif tag == 'folder_update_error':
error = FolderUpdateError.from_error(error)elif tag == 'update_conflict':
error = UpdateConflict.from_error(error)elif tag == 'audit_log_error':
error = AuditLogError.from_error(error)elif tag == 'internal_error':
error = InternalError.from_error(error)elif tag == 'quota_exempt_error':
error = QuotaExemptError.from_error(error)elif tag == 'restore_backup_error':
error = RestoreBackupError.from_error(error)else:
raise Exception('Unknown error tag')errorexcept Exception:
raise ServerParseException())()


class DisableDeviceError(ApiError):
    from_response = (lambda cls = None, response = None: try:
error = response['error']tag = error['.tag']if tag == 'device_conflict':
error = DeviceConflictError.from_error(error)elif tag == 'folder_lookup_error':
error = FolderLookupError.from_error(error)elif tag == 'folder_update_error':
error = FolderUpdateError.from_error(error)elif tag == 'device_not_found':
error = DeviceNotFoundError.from_error(error)elif tag == 'update_conflict':
error = UpdateConflict.from_error(error)elif tag == 'audit_log_error':
error = AuditLogError.from_error(error)elif tag == 'internal_error':
error = InternalError.from_error(error)else:
raise Exception('Unknown error tag')errorexcept Exception:
raise ServerParseException())()


class DeviceStatusError(ApiError):
    from_response = (lambda cls = None, response = None: try:
error = response['error']tag = error['.tag']if tag == 'folder_lookup_error':
error = FolderLookupError.from_error(error)elif tag == 'device_invalid':
error = DeviceInvalidError.from_error(error)elif tag == 'device_not_found':
error = DeviceNotFoundError.from_error(error)elif tag == 'internal_error':
error = InternalError.from_error(error)else:
raise Exception('Unknown error tag')errorexcept Exception:
raise ServerParseException())()


class SetQuotaExemptError(ApiError):
    from_response = (lambda cls = None, response = None: try:
error = response['error']tag = error['.tag']if tag == 'device_not_found':
error = DeviceNotFoundError.from_error(error)elif tag == 'device_disabled':
error = DeviceDisabledError.from_error(error)elif tag == 'quota_exempt_error':
error = QuotaExemptError.from_error(error)else:
raise Exception('Unknown error tag')errorexcept Exception:
raise ServerParseException())()


class ForceDisableOtherBackupsError(ApiError):
    from_response = (lambda cls = None, response = None: try:
error = response['error']tag = error['.tag']if tag == 'device_not_found':
error = DeviceNotFoundError.from_error(error)elif tag == 'update_conflict':
error = UpdateConflict.from_error(error)elif tag == 'internal_error':
error = InternalError.from_error(error)else:
raise Exception('Unknown error tag')errorexcept Exception:
raise ServerParseException())()


def success_response_to_state(response = None):
    pass
# WARNING: Decompyle incomplete


def success_response_to_excluded_list(response = None):
    
    try:
        merge_exclusion_list = response['merge_exclusion_list']()
        unmerge_exclusion_list = response['unmerge_exclusion_list']()
        return SyncEverythingExcludedFileList(merge_exclusion_list = merge_exclusion_list, unmerge_exclusion_list = unmerge_exclusion_list)
    except Exception:
        raise ServerParseException()



def success_response_to_list_backups_result(response = None):
    pass
# WARNING: Decompyle incomplete


def success_response_to_compute_device_name_result(response = None):
    
    try:
        res = response['device_name']
        return res
    except Exception:
        raise ServerParseException()


ENABLE_DEVICE_ERRORS = {
    'invalid_request': InvalidRequestError,
    'device_conflict': DeviceConflictError,
    'folder_lookup_error': FolderLookupError,
    'folder_update_error': FolderUpdateError,
    'update_conflict': UpdateConflict,
    'audit_log_error': AuditLogError,
    'internal_error': InternalError }
DISABLE_DEVICE_ERRORS = {
    'device_not_found': DeviceNotFoundError,
    'device_conflict': DeviceConflictError,
    'folder_lookup_error': FolderLookupError,
    'folder_update_error': FolderUpdateError,
    'update_conflict': UpdateConflict,
    'audit_log_error': AuditLogError,
    'internal_error': InternalError }
DEVICE_STATE_ERRORS = {
    'folder_lookup_error': FolderLookupError,
    'device_not_found': DeviceNotFoundError,
    'device_invalid': DeviceInvalidError,
    'internal_error': InternalError }
RETRIABLE_API_ERRORS = {
    'folder_lookup_error': FolderLookupError,
    'folder_update_error': FolderUpdateError,
    'update_conflict': UpdateConflict,
    'audit_log_error': AuditLogError,
    'internal_error': InternalError,
    'unexempt_existing': QuotaExemptError,
    'lookup_devices': QuotaExemptError }
INVALID_API_ERRORS = {
    'invalid_request': InvalidRequestError,
    'device_conflict': DeviceConflictError,
    'device_not_found': DeviceNotFoundError,
    'device_invalid': DeviceInvalidError,
    'not_allowed': QuotaExemptError,
    'device_disabled': DeviceDisabledError }

def parse_apiv2_error(exception = None, error_type = None):
    response = cast(ServerJSON, exception.data)
    return error_type.from_response(response)


def parse_async_copy_failed_folders(exception = None):
    response = cast(ServerJSON, exception.data)
    
    try:
        list_folders = response['error']['restore_backup_error']['async_copy_transient']['failed_folders']
        return list_folders()
    except Exception:
        raise ServerParseException()



def is_retriable_request_exception(api_error = None):
    return type(api_error) in set(RETRIABLE_API_ERRORS.values())


def is_invalid_request_exception(api_error = None):
    return type(api_error) in set(INVALID_API_ERRORS.values())

apiv2_error_to_redirect_status = (lambda error_type = None: pass# WARNING: Decompyle incomplete
)()
_catch_and_convert_network_exceptions = (lambda fut = None, error_type = None: handled_fut = fut.catch(HTTP409Error, apiv2_error_to_redirect_status(error_type)) if error_type else futhandled_fut.catch(HTTP400Error, convert_to_failure(RedirectRequestStatus.INVALID, 'server returned HTTP 400', report_severity = Severity.TRACE)).catch(HTTP500Error, convert_to_failure(RedirectRequestStatus.RETRY, 'server returned HTTP 500', report_severity = Severity.TRACE)).catch(HTTP429Error, convert_to_failure(RedirectRequestStatus.RETRY, 'server returned HTTP 429', report_severity = Severity.TRACE)).catch(TransientNetworkError, convert_to_failure(RedirectRequestStatus.RETRY, 'transient network failure', report_severity = Severity.TRACE)).catch(DropboxServerError, convert_to_failure(RedirectRequestStatus.RETRY, 'server returned HTTP error', report_severity = Severity.TRACE)).catch(ServerParseException, convert_to_failure(RedirectRequestStatus.FATAL_UNKNOWN, 'could not parse server response', report_severity = Severity.TRACE)))()

def catch_and_convert_network_exceptions_enable_device(fut = None):
    return _catch_and_convert_network_exceptions(fut, EnableDeviceError)


def catch_and_convert_network_exceptions_disable_device(fut = None):
    return _catch_and_convert_network_exceptions(fut, DisableDeviceError)


def catch_and_convert_network_exceptions_device_status(fut = None):
    return _catch_and_convert_network_exceptions(fut, DeviceStatusError)


def catch_and_convert_network_exceptions_update_device(fut = None):
    return _catch_and_convert_network_exceptions(fut, EnableDeviceError)


def catch_and_convert_network_exceptions_exclusion_list(fut = None):
    return _catch_and_convert_network_exceptions(fut, None)


def catch_and_convert_network_exceptions_list_backups(fut = None):
    return _catch_and_convert_network_exceptions(fut, None)


def catch_and_convert_network_exceptions_compute_device_name(fut = None):
    return _catch_and_convert_network_exceptions(fut, None)


def catch_and_convert_network_exceptions_set_quota_exempt(fut = None):
    return _catch_and_convert_network_exceptions(fut, SetQuotaExemptError)


def catch_and_convert_network_exceptions_force_disable(fut = None):
    return _catch_and_convert_network_exceptions(fut, ForceDisableOtherBackupsError)


def catch_and_convert_network_exceptions_send_email(fut = None):
    return _catch_and_convert_network_exceptions(fut, None)

catch_and_convert_network_exceptions_restore_device = (lambda fut = None: pass# WARNING: Decompyle incomplete
)()
ServerFolderDesc = Tuple[(OSFolderID, Text)]

class ServerInterface:
    
    def __init__(self = None, context = None, device_id = None):
        self._account = context.account
        self._conn = context.connection
        self._device_id = device_id

    
    def _offline(self = None):
        return is_offline(self._conn)

    enable_device = (lambda self = None, device_name = None, known_folders_desc = future_function: pass# WARNING: Decompyle incomplete
)()
    disable_device = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    device_status = (lambda self = None, validate = None: pass# WARNING: Decompyle incomplete
)()
    send_email = (lambda self = None, email_type = None, device_name = future_function: pass# WARNING: Decompyle incomplete
)()
    update_device = (lambda self = None, new_state = None: pass# WARNING: Decompyle incomplete
)()
    start_restore_device = (lambda self, new_state = None, restore_device_id = None, folders = future_function, is_async_retry = ('new_state', 'DeviceState', 'restore_device_id', 'str', 'folders', 'List[KnownFolder]', 'return', 'Future[None]'): pass# WARNING: Decompyle incomplete
)()
    complete_restore_device = (lambda self = None, new_state = None, restore_device_id = future_function: pass# WARNING: Decompyle incomplete
)()
    exclusion_list = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    list_backups = (lambda self = None, include_last_ts = None: pass# WARNING: Decompyle incomplete
)()
    compute_device_name = (lambda self = None, device_name_base = None: pass# WARNING: Decompyle incomplete
)()
    set_quota_exempt = (lambda self = None, device_id = None: pass# WARNING: Decompyle incomplete
)()
    force_disable_other_backups = (lambda self = None, device_id = None, backup_disable_type = future_function: pass# WARNING: Decompyle incomplete
)()
    clear_all_quota_exempt = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _client_metrics_request(self = None, metric = None, **kv):
        pass
    # WARNING: Decompyle incomplete

    client_metrics_update_device = (lambda self = None, status = None: pass# WARNING: Decompyle incomplete
)()
    client_metrics_restore_device = (lambda self = None, status = None: pass# WARNING: Decompyle incomplete
)()
    client_metrics_disable_device = (lambda self = None, status = None: pass# WARNING: Decompyle incomplete
)()
    client_metrics_ic_remediation = (lambda self = None, ic_remediation = None, ic_mode_str = future_function: pass# WARNING: Decompyle incomplete
)()

