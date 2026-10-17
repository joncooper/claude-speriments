# Source Generated with Decompyle++
# File: constants.pyc (Python 3.11)

from __future__ import absolute_import
import errno
from enum import Enum, IntEnum
from typing import cast, Optional, Tuple
from dropbox.attrs import Attributes
from dropbox.client.cloud_docs.constants import DROPBOX_CLOUD_CONTENT_ONLY_KEY, DROPBOX_CLOUD_CONTENT_ONLY_PLAT
from dropbox.shared.relocation_stats import OPERATION_META_FILE
MYPY = False
if MYPY:
    from datatypes.file_cache_entry import FileCacheEntryBase

class ReindexDirtyType(object):
    ADD = 'add'
    DELETE = 'delete'
    EDIT = 'edit'
    EDIT_ATTR = 'edit_attr'
    FORCED_EDIT = 'forced_edit'


class ReindexStrategy(object):
    COMPARE_TREES = 'compare_trees'

IGNORED_FILES = set(('desktop.ini', 'thumbs.db', '.ds_store', 'icon\r', '.dropbox', '.dropbox.attr', '.dropbox.cache', OPERATION_META_FILE))
RECONSTRUCT_TEMP_FILE_PREFIX = '.dbtmp-'
UNWATCHED_FILE_PATTERNS = [
    '~$*',
    '~*.tmp',
    '.~*',
    RECONSTRUCT_TEMP_FILE_PREFIX + '*']
HASH_EMPTY_FILE_MTIME_PAST_BUFFER = 3
HASH_EMPTY_FILE_MTIME_FUTURE_BUFFER = 1
UNRECONSTRUCTABLE_UNIX_ERRNOS = (errno.EINVAL, errno.ENAMETOOLONG, errno.EILSEQ)
DOES_NOT_EXIST_ERRNOS = (errno.ENOTDIR, errno.ENOENT)
FORCE_RETAG_FOLDERS_ON_REVISION_KEY_NAME = 'force-retag-folders-on-revision-change'
FORCE_RETAG_FOLDERS_ON_REVISION_CHANGE_CURRENT = 2

class PrehasherEventType(object):
    NORMAL = 1
    DELETE = 2
    ALL_EVENTS = (NORMAL, DELETE)


class DeletedFileStatus(IntEnum):
    DELETED = 1
    INSIDE_DROPBOX = 2
    INSIDE_DROPBOX_UNDER_CACHE = 3
    INSIDE_DROPBOX_IGNORED = 4
    OUTSIDE_DROPBOX = 5


class ConflictedCopyReason(Enum):
    UNKNOWN = 0
    CASE = 1
    DOT_DROPBOX = 2
    WHITE_SPACE = 3
    SELECTIVE_SYNC = 4
    DELETED_FILE_CACHE = 5
    UNICODE_ENCODING = 6
    PHOTO_IMPORTER = 7
    EDIT = 8
    PERMISSION = 9
    INACCESSIBLE_PATH = 10
    TMF_RENAME = 11


class SyncType(IntEnum):
    NORMAL = cast('SyncType', 1)
    HIDDEN = cast('SyncType', 2)
    PLACEHOLDER = cast('SyncType', 3)


class SyncPolicy(Enum):
    NORMAL_FILE = (False, SyncType.NORMAL, None)
    PLACEHOLDER_FILE = (False, SyncType.PLACEHOLDER, None)
    HIDDEN_FILE = (False, SyncType.HIDDEN, None)
    NORMAL_FOLDER = (True, SyncType.NORMAL, SyncType.NORMAL)
    INFINITE_FOLDER = (True, SyncType.NORMAL, SyncType.PLACEHOLDER)
    STUB_FOLDER = (True, SyncType.PLACEHOLDER, SyncType.HIDDEN)
    HIDDEN_FOLDER = (True, SyncType.HIDDEN, SyncType.HIDDEN)
    UNKNOWN_FOLDER = (True, SyncType.NORMAL, None)
    is_dir = (lambda self = None: self.value[0])()
    sync_type = (lambda self = None: self.value[1])()
    folder_policy = (lambda self = None: self.value[2])()
    from_parts = (lambda cls = None, is_dir = None, sync_type = classmethod, folder_policy = ('is_dir', 'bool', 'sync_type', 'SyncType', 'folder_policy', 'Optional[SyncType]', 'return', "'SyncPolicy'"): tup = (is_dir, sync_type, folder_policy)for policy in cls:
if policy.value == tup:
None, policyraise ValueError('The tuple (%r, %r, %r) is not a valid SyncPolicy' % tup))()
    from_entry_local = (lambda cls = None, entry = None: cls.from_parts(is_dir = entry.local_dir, sync_type = entry.local_sync_type, folder_policy = entry.local_folder_policy))()
    from_entry_updated = (lambda cls = None, entry = None: cls.from_parts(is_dir = entry.updated_dir, sync_type = entry.updated_sync_type, folder_policy = entry.updated_folder_policy))()

MOVE_DROPBOX_STOP_TIMEOUT = 30
FILTER_IGNORED_NSES_WITH_CONSISTENCY_CHECK = 'ON_WITH_CONSISTENCY_CHECK'
FILTER_IGNORED_NSES_WITHOUT_CONSISTENCY_CHECK = 'ON_WITHOUT_CONSISTENCY_CHECK'
DROPBOX_SYMLINK_PLAT = 'dropbox'
DROPBOX_SYMLINK_KEY = 'symlink'
NUCLEUS_SYMLINK_MIGRATION_PLAT = 'nucleus_symlink_migration'
NUCLEUS_SYMLINK_MIGRATION_KEY = 'symlink_migration'
DROPBOX_CLOUD_CONTENT_ONLY_PLAT = DROPBOX_CLOUD_CONTENT_ONLY_PLAT
DROPBOX_CLOUD_CONTENT_ONLY_KEY = DROPBOX_CLOUD_CONTENT_ONLY_KEY

class SyncAttrs:
    is_cloud_content = (lambda attrs = None: if attrs and attrs.lookup_key(DROPBOX_CLOUD_CONTENT_ONLY_PLAT, DROPBOX_CLOUD_CONTENT_ONLY_KEY):
True)()

SYMLINK_MIGRATION_HOST_INT = 0x8653DBA30
LACONIC_GRASSHOPPER_RECOVERY_NEEDED = 'LACONIC_GRASSHOPPER_RECOVERY_NEEDED'
HOST_HAS_RUN_SPARSE_FILES_MIGRATION = 'HOST_HAS_RUN_SPARSE_FILES_MIGRATION'
HOST_HAS_RUN_CLOUD_DOCS_MIGRATION = 'HOST_HAS_RUN_CLOUD_DOCS_MIGRATION'
MIN_TIME_FOR_WATER_HAMMER_RECALL = 'MIN_TIME_FOR_WATER_HAMMER_RECALL'
