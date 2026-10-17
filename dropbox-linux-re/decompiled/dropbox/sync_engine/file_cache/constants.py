# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Sequence
from dropbox.sync_engine_boundary.constants import RECONSTRUCT_BAD_LOCAL_DETAILS_CODE, RECONSTRUCT_BLOCKED_BY_LIST_CODE, RECONSTRUCT_BUSY_CODE, RECONSTRUCT_DIRECTORY_NOT_EMPTY_CODE, RECONSTRUCT_HASHES_NOT_READY_CODE, RECONSTRUCT_IN_PROGRESS_CODE, RECONSTRUCT_LOW_DISK_SPACE_CODE, RECONSTRUCT_NO_HASHES_CODE, RECONSTRUCT_NO_PARENT_FOLDER_CODE, RECONSTRUCT_PERMISSION_DENIED_CODE, RECONSTRUCT_POSSIBLE_CORRUPTION_CODE, RECONSTRUCT_PREDICTABLE_CODE, RECONSTRUCT_READ_ONLY_FS_CODE, RECONSTRUCT_SUCCESS_CODE, RECONSTRUCT_UNKNOWN_CODE, RECONSTRUCT_UNRECONSTRUCTABLE_CODE, SyncEventType as FileModificationType, UPLOAD_ATTEMPTED_UNTAG_RELOCATE_CODE, UPLOAD_BLOCKED_BY_LIST, UPLOAD_CONFLICT_CODE, UPLOAD_DELAYED_SHARED_FOLDER_DELETE, UPLOAD_DELAYED_SHARED_FOLDER_MOUNT, UPLOAD_DELAYED_SHARED_FOLDER_UNMOUNT, UPLOAD_DELAYED_SYMLINK_MOUNT, UPLOAD_DELETED_CODE, UPLOAD_DIRECTORY_HELD, UPLOAD_DIRECTORY_NOT_EMPTY_CODE, UPLOAD_EXT_NO_ACCESS_PERM_CODE, UPLOAD_FAILED_RELOCATE_CODE, UPLOAD_IGNORED_CODE, UPLOAD_INVALID_PATH_CODE, UPLOAD_NEED_BLOCKS_CODE, UPLOAD_NEED_BLOCKS_HASHING_CODE, UPLOAD_NO_ACCESS_CODE, UPLOAD_NO_WRITE_ACCESS_CODE, UPLOAD_PARENT_NS_REASSOCIATE, UPLOAD_QUOTA_CODE, UPLOAD_SUCCESS_CODE, UPLOAD_SYMLINK_REJECTED_CODE, UPLOAD_TMF_BLOCKED
from dropbox.sync_engine_boundary.utils import NamespacePropertyUtils
COMMIT_BY_SJID_SOURCE_NS_ACCESS_DENIED = 'source_ns_access_denied'
COMMIT_BY_SJID_MISSING_SOURCE = 'missing_source'
COMMIT_BY_SJID_SOURCE_INVALID = 'source_invalid'
MOUNT_REQUEST_UNMOUNT = 0
MOUNT_REQUEST_MOUNT = 1
DROPBOX_FOLDER_VOLUMEID = 'dropbox_folder_volumeid'
UUID_TO_PERSISTENT_VOLUMEID_KEY = 'uuid_to_persistent_volumeid'
CONFIG_VERSION = 'version'
CONFIG_JAN_2015_INCONSISTENT_STATE_KEY = 'jan_2015_inconsistent_state_version'

class NamespacePermission(object):
    VIEW_NAME_ONLY = -2000
    TRAVERSE = -1000
    NO_ACCESS = 0
    READ_ONLY = 1
    READ_WRITE = 2
    OWNER = 3
    is_valid = (lambda cls, value: value in (cls.VIEW_NAME_ONLY, cls.TRAVERSE, cls.NO_ACCESS, cls.READ_ONLY, cls.READ_WRITE, cls.OWNER))()
    is_read_only = (lambda cls = None, permission = classmethod: not cls.can_write(permission))()
    can_write = (lambda cls = None, permission = None: if not permission is None:
passpermission in (cls.READ_WRITE, cls.OWNER))()
    is_owner = (lambda cls = None, permission = None: permission == cls.OWNER)()
    has_access = (lambda cls = None, permission = None: permission != cls.NO_ACCESS)()
    is_traverse_only = (lambda cls = None, permission = None: permission == cls.TRAVERSE)()
    is_view_name_only = (lambda cls = None, permission = None: permission == cls.VIEW_NAME_ONLY)()
    is_non_member = (lambda cls = None, permission = None: permission in (cls.VIEW_NAME_ONLY, cls.NO_ACCESS))()
    requires_resync = (lambda cls = None, old_permission = None, new_permission = classmethod: 