# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from enum import auto, Enum, IntEnum
HASH_ACCESS = 'access'
HASH_BUSY = 'busy'
HASH_DROP = 'drop'
HASH_EDP_MISMATCH = 'edp_identity_mismatch'
HASH_NEEDS_REINDEX = 'needs-reindex'
HASH_PROTECTED = 'protected'
HASH_SUCCESS = 'success'
HASH_EXTERNAL_RECALL = 'awaiting_external_recall'
HASH_UNKNOWN = 'unknown'
HASH_DELETE_HONEYPOT_PLACEHOLDER = 'delete_honeypot_placeholder'
HASH_KEXT_PROTECTED = 'hash_kext_protected'
HASH_IGNORE_INVALID_FILENAME_CODE = 'invalid filename'
UNMOUNT_CAUSE_MOVE = 'move'
UNMOUNT_CAUSE_DELETE = 'delete'
P2P_STOP_SUSPEND = 'suspended'
RECONSTRUCT_POSSIBLE_CORRUPTION_CODE = 'possible_corruption'
RECONSTRUCT_UNRECONSTRUCTABLE_CODE = 'unreconstructable'
RECONSTRUCT_DIRECTORY_NOT_EMPTY_CODE = 'directory_not_empty'
RECONSTRUCT_NO_PARENT_FOLDER_CODE = 'no parent folder'
RECONSTRUCT_NO_HASHES_CODE = 'no hashes'
RECONSTRUCT_HASHES_NOT_READY_CODE = 'hashes not ready'
RECONSTRUCT_IN_PROGRESS_CODE = 'in_progress'
RECONSTRUCT_BAD_LOCAL_DETAILS_CODE = 'bad_local_details'
RECONSTRUCT_SUCCESS_CODE = 'success'
RECONSTRUCT_BUSY_CODE = 'busy'
RECONSTRUCT_PREDICTABLE_CODE = 'predictable'
RECONSTRUCT_PERMISSION_DENIED_CODE = 'permission_denied'
RECONSTRUCT_LOW_DISK_SPACE_CODE = 'low disk space'
RECONSTRUCT_READ_ONLY_FS_CODE = 'read-only filesystem'
RECONSTRUCT_UNKNOWN_CODE = 'unknown'
RECONSTRUCT_BLOCKED_BY_LIST_CODE = 'blocked_by_list'
RECONSTRUCT_IGNORE_INVALID_FILENAME_CODE = 'invalid filename'
UPLOAD_SUCCESS_CODE = 'success'
UPLOAD_IGNORED_CODE = 'ignored'
UPLOAD_CONFLICT_CODE = 'conflict'
UPLOAD_DIRECTORY_NOT_EMPTY_CODE = 'extended_directory_not_empty'
UPLOAD_QUOTA_CODE = 'quota'
UPLOAD_INVALID_PATH_CODE = 'invalid_path'
UPLOAD_NEED_BLOCKS_HASHING_CODE = 'nb_hashing'
UPLOAD_NEED_BLOCKS_CODE = 'nb'
UPLOAD_NO_ACCESS_CODE = 'no_access'
UPLOAD_NO_WRITE_ACCESS_CODE = 'extended_no_write_perm'
UPLOAD_EXT_NO_ACCESS_PERM_CODE = 'extended_no_access_perm'
UPLOAD_DELAYED_SHARED_FOLDER_ADD = 'upload_delayed_add'
UPLOAD_DELAYED_SHARED_FOLDER_DELETE = 'upload_delayed_delete'
UPLOAD_DELAYED_SHARED_FOLDER_MOUNT = 'upload_delayed_mount'
UPLOAD_DELAYED_SYMLINK_MOUNT = 'upload_delayed_symlink_mount'
UPLOAD_DELAYED_SHARED_FOLDER_UNMOUNT = 'upload_delayed_unmount'
UPLOAD_DELETED_CODE = 'deleted'
UPLOAD_DIRECTORY_HELD = 'upload_directory_held'
UPLOAD_PARENT_NS_REASSOCIATE = 'parent_ns_reassociate'
UPLOAD_SYMLINK_REJECTED_CODE = 'symlink_rejected'
UPLOAD_ATTEMPTED_UNTAG_RELOCATE_CODE = 'upload_failed_untag_relocated'
UPLOAD_FAILED_RELOCATE_CODE = 'upload_failed_relocate'
UPLOAD_BLOCKED_BY_LIST = 'blocked_by_list'
UPLOAD_TMF_BLOCKED = 'tmf_mount_blocked'
MIN_FREE_SPACE = 1073741824
MIN_FREE_FRACTION = 0.1
REINDEX_CONFIG_NUM_FILES_KEY = 'sec_last_reindex_num_files'
INFINITE_PLACEHOLDER_COUNT_KEY = 'infinite_placeholder_count'
BOUNDARY_FUTURE_COMPLETION_THREAD_POOL = 'BOUNDARY_FUTURE_COMPLETION_THREAD_POOL'
BOUNDARY_PUBLISHED_EVENTS_THREAD_POOL = 'BOUNDARY_PUBLISHED_EVENTS'
LOOKUP_BY_FILEID_BATCH_ENABLED_STORMCROW = 'desktop-lookup-by-fileid-batch-enabled'
NamespacePropertySet = int

class NamespaceProperty(object):
    EMPTY_PROPERTIES = 0
    CAN_MOUNT_SHARED_FOLDERS = 1
    IS_TEAM_SHARED_FOLDER = 4
    IN_TEAM_FOLDER = 8
    IS_CONFIDENTIAL = 32
    DISALLOW_CONFIDENTIAL_CREATION = 64
    ONLY_OWNER_CAN_UPDATE_ACL = 128
    FORBID_NON_TEAM_SHARING = 256
    IS_USER_ON_SAME_TEAM_AS_OWNER = 512
    VALID_PROPERTIES = frozenset([
        CAN_MOUNT_SHARED_FOLDERS,
        IS_TEAM_SHARED_FOLDER,
        IN_TEAM_FOLDER,
        IS_CONFIDENTIAL,
        DISALLOW_CONFIDENTIAL_CREATION,
        ONLY_OWNER_CAN_UPDATE_ACL,
        FORBID_NON_TEAM_SHARING,
        IS_USER_ON_SAME_TEAM_AS_OWNER])
    MOUNT_ENTRY_PROPERTIES = -1 & ~DISALLOW_CONFIDENTIAL_CREATION


class FixPermissionStatus(object):
    FAILED = 0
    SUCCESS = 1
    NOTEXIST = 2
    NOTNEEDED = 3
    NOTTRIED = 4


class SyncDirection(IntEnum):
    UP = 0
    DOWN = 1
    BLANK = 2


class SyncEventType(IntEnum):
    DELETE = 0
    ADD = 1
    EDIT = 2
    SYNC_POLICY_CHANGE = 3
    RECALL = 4
    MOVE = 5
    LIST = 6


class SyncOperationFailureReason(Enum):
    LOW_DISK_SPACE = 'low_disk_space'
    DIRECTORY_NOT_EMPTY = 'directory_not_empty'
    PLACEHOLDERS_NOT_SUPPORTED = 'placeholders_not_supported'
    PERMISSIONS = 'permissions'
    EDP_MISMATCH = 'edp_mismatch'
    INVALID_DEVICE_ANCHOR = 'invalid_device_anchor'
    OVER_QUOTA = 'over_quota'
    OQ_COMMIT_PREVENTED = 'oq_commit_prevented'
    TEAM_FOLDER_OVER_QUOTA = 'team_folder_over_quota'
    BB_MONTHLY_UPLOAD_LIMIT_EXCEEDED = 'bb_monthly_upload_limit_exceeded'
    SERVER_REJECTED = 'server_rejected'
    KEXT_PROTECTED = 'kext_protected'
    HARD_LINKS = 'hard_links'
    FILE_TOO_LARGE = 'file_too_large'
    INVALID_FILENAME_CODE = 'invalid filename'
    RECALL_NO_NETWORK = 'recall_no_network'
    RECALL_NO_DISK_SPACE = 'recall_no_disk_space'
    RECALL_ENGINE_PAUSED = 'recall_engine_paused'
    RECALL_FAILED = 'recall_failed'
    FILEPROVIDER_UNHANDLED = 'fileprovider_unhandled'
    FILEPROVIDER_NO_PERMISSIONS = 'fileprovider_no_permissions'
    FILEPROVIDER_CONFLICT = 'fileprovider_conflict'
    FILEPROVIDER_TEMPORARILY_UNAVAILABLE = 'fileprovider_temporarily_unavailable'
    FILEPROVIDER_NAME_TOO_LONG = 'fileprovider_name_too_long'
    FILEPROVIDER_RESULT_TOO_LARGE = 'fileprovider_result_too_large'
    FILEPROVIDER_OPERATION_NOT_SUPPORTED = 'fileprovider_operation_not_supported'
    FILEPROVIDER_OPERATION_NOT_PERMITTED = 'fileprovider_operation_not_permitted'
    FILEPROVIDER_FILE_WRITE_EXISTS = 'fileprovider_file_write_exists'
    FILEPROVIDER_FILE_LOCKING_ERROR = 'fileprovider_file_locking_error'
    LISTING_CLIENT_KEY_ENROLLMENT = 'listing_client_key_enrollment'
    SHARING_VIOLIATION = 'sharing_violation'
    STAT_CHANGED = 'stat_changed'
    VIRUS_DETECTED = 'virus_detected'
    FILE_CORRUPTION_OR_HARDWARE_ERROR = 'file_corruption_or_hardware_error'
    ENCRYPTED_FOLDER_CONFLICT = 'encrypted_folder_conflict'
    PRE_LOCAL_CONSTRAINT_LOOPING_FILEID = 'pre_local_constraint_looping_fileid'
    CLOUD_DOC_IN_ENCRYPTED_FOLDER = 'cloud_doc_in_encrypted_folder'
    SYMLINK_IN_ENCRYPTED_FOLDER = 'symlink_in_encrypted_folder'
    UNRECONSTRUCTABLE_SPECIAL_THIRD_PARTY_FILENAME = 'unreconstructable_special_third_party_filename'
    UNRECONSTRUCTABLE_UNIMPORTANT_FILENAME = 'unreconstructable_unimportant_filename'
    UNRECONSTRUCTABLE_FILENAME_COLLISION = 'unreconstructable_filename_collision'
    UNRECONSTRUCTABLE_INVALID_PATH = 'unreconstructable_invalid_path'
    UNRECONSTRUCTABLE_INVALID_XATTR = 'unreconstructable_invalid_xattr'
    UNRECONSTRUCTABLE_RESERVED_XATTR = 'unreconstructable_reserved_xattr'
    UNRECONSTRUCTABLE_FP_PACKAGE = 'unreconstructable_fp_package'
    UNRECONSTRUCTABLE_VIRUS_DETECTED = 'unreconstructable_virus_detected'
    UNRECONSTRUCTABLE_SYMLINK_NOT_SUPPORTED = 'unreconstructable_symlink_not_supported'
    UNRECONSTRUCTABLE_FILE_TOO_LARGE = 'unreconstructable_file_too_large'
    UNRECONSTRUCTABLE_UNSYNCABLE = 'unreconstructable_unsyncable'
    UNRECONSTRUCTABLE_PARENT_UNSYNCABLE = 'unreconstructable_parent_unsyncable'
    UNRECONSTRUCTABLE_RECALL_NON_FILE = 'unreconstructable_recall_non_file'
    UNRECONSTRUCTABLE_PLACEHOLDER_CROSS_ACCOUNT_MOVE_HYDRATION = 'unreconstructable_placeholder_cross_account_move_hydration'
    UNRECONSTRUCTABLE_BLOCKS_NOT_FOUND = 'unreconstructable_blocks_not_found'
    UNRECONSTRUCTABLE_DROPBOX_CACHE_DIR = 'unreconstructable_dropbox_cache_dir'
    UNRECONSTRUCTABLE_ROOT_TRASH = 'unreconstructable_root_trash'
    UNRECONSTRUCTABLE_APPLE_IGNORED_FILE = 'unreconstructable_apple_ignored_file'
    UNRECONSTRUCTABLE_FLEXIBLE_FILENAMES_FIXABLE = 'unreconstructable_flexible_filenames_fixable'
    UNRECONSTRUCTABLE_IGNORED_PATH = 'unreconstructable_ignored_path'
    CLOUDFILES_PROVIDER_INTERFERENCE = 'cloudfiles_provider_interference'


class SyncOperationFailureType(IntEnum):
    UNKNOWN = 0
    HASH = 1
    UPLOAD = 2
    RECONSTRUCT = 3
    RECALL = 4
    LIST = 5


class OSFolderID(Enum):
    value: 'str' = 'OSFolderID'
    DESKTOP = 'Desktop'
    DOCUMENTS = 'Documents'
    PICTURES = 'Pictures'
    DOWNLOADS = 'Downloads'
    MUSIC = 'Music'
    VIDEOS = 'Videos'
    MOVIES = 'Movies'
    SCREENSHOTS = 'Screenshots'
    TEST_SYNC_EVERYTHING_REDIRECT = 'TestSyncEverythingRedirect'


class UserAccessType(IntEnum):
    HideOnly = 0
    DenyDeleteOnly = 1
    HideAndDenyDelete = 2

ON_LIST_VALID_KEYS = set([
    'role',
    'send_trace',
    'reboot',
    'host_int',
    'is_msl_team',
    'is_user_msl_on',
    'update_to_dict',
    'quota_info',
    'in_use',
    'quota',
    'ns_p2p_key_map',
    'more_results'])
SYNC_ICON_MIN_REFRESH_MS = 16
SYNC_ICON_REFRESH_TIMEOUT_MS = 0

class SyncEngineGeneration(Enum):
    UNKNOWN = auto()
    NUCLEUS = auto()
    ISOTOPE = auto()
    CLASSIC = auto()

