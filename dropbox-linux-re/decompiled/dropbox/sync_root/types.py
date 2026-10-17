# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

import enum
import re
from enum import StrEnum
from typing import NamedTuple, Optional
from dropbox.proto.nucleus.sync_engine_pb2 import CLOUD_FILES as CLOUD_FILES_V, DEBUG as DEBUG_V, FILE_PROVIDER as FILE_PROVIDER_V, MOUNTED as MOUNTED_V, SyncRootType as SyncRootTypeProto

class SyncRootHydrationPolicy(StrEnum):
    FULL = enum.auto()
    STREAMING = enum.auto()


class SyncRootType(enum.Enum):
    MOUNTED = 'mounted'
    FILE_PROVIDER = 'file_provider'
    CLOUD_FILES = 'cloud_files'
    DEBUG = 'debug'
    FP_SHADOW_MIGRATION = 'fp_shadow'
    
    def display_name(self = None):
        return self.value.replace('_', ' ').title()

    
    def abbreviation(self = None):
        return {
            SyncRootType.FP_SHADOW_MIGRATION: 'fps',
            SyncRootType.DEBUG: 'd',
            SyncRootType.CLOUD_FILES: 'cf',
            SyncRootType.FILE_PROVIDER: 'fp',
            SyncRootType.MOUNTED: 'm' }.get(self, 'u')

    
    def to_sync_engine_arg(self = None):
        if self == SyncRootType.MOUNTED:
            return MOUNTED_V
        if None == SyncRootType.FILE_PROVIDER:
            return FILE_PROVIDER_V
        if None == SyncRootType.CLOUD_FILES:
            return CLOUD_FILES_V
        if None == SyncRootType.FP_SHADOW_MIGRATION:
            return MOUNTED_V



class SyncRootTypeReason(enum.Enum):
    UNKNOWN = 'unknown'
    NOT_ELIGIBLE = 'not_eligible'
    TEAM_ADMIN_DISABLED = 'team_admin_disabled'
    ELIGIBLE = 'eligible'
    OPT_OUT = 'opt_out'
    FILE_COUNT_LIMIT = 'file_count_limit'
    EXISTING_ROOT = 'existing_root'
    MATCH_PRIMARY = 'primary'
    INVAID_PRIMARY = 'invalid_primary'
    CUSTOM_PATH = 'custom_path'
    FP_BY_DEFAULT_COHORT_FP = 'fp_by_default_cohort_fp'
    FP_BY_DEFAULT_COHORT_MOUNTED = 'fp_by_default_cohort_mounted'

_SYNC_ENGINE_VERSION_REGEX = re.compile('[0-9\\.]+[n|i]([a-z]+)$')

def get_sync_root_from_engine_version(sync_engine_version = None):
    result = _SYNC_ENGINE_VERSION_REGEX.match(sync_engine_version)
# WARNING: Decompyle incomplete


def get_sync_root_value_from_engine_version(sync_engine_version = None):
    pass
# WARNING: Decompyle incomplete


class SyncRootInfo(NamedTuple):
    root_mount_path: 'Optional[str]' = 'SyncRootInfo'


class SyncRootCreationResult(NamedTuple):
    did_create_symlink: 'bool' = 'SyncRootCreationResult'


class SyncRootFeatureUnsupported(Exception):
    pass


class SyncRootUnsafeMerge(Exception):
    pass


class SyncRootTypeInvalid(Exception):
    pass
# WARNING: Decompyle incomplete


class SyncRootNotInitialized(Exception):
    pass


class SyncRootInvalid(Exception):
    pass


class SyncRootMountMissing(Exception):
    pass


class SyncRootDriveMissing(Exception):
    pass
# WARNING: Decompyle incomplete


class SyncRootCreationConflict(Exception):
    pass


class RemovalMode(enum.Enum):
    PRESERVE = enum.auto()
    DESTROY = enum.auto()
    ARCHIVE = enum.auto()
    ARCHIVE_DIRTY_ONLY = enum.auto()


class SyncRootInconsistency(StrEnum):
    LOCATIONS_LINK_HIDDEN = 'locations_link_hidden'
    LOCATIONS_LINK_MISSING = 'locations_link_missing'


class SyncRootRepairAction(StrEnum):
    FP_DISABLE_TRASH_SYNC = 'disable_trash_sync'
    FP_RECONNECT_TO_DOMAIN = 'reconnect_to_domain'
    CF_REREGISTER_SYNC_ROOT = 'cf_reregister_sync_root'
    CF_SET_HYDRATION_POLICY = 'cf_set_hydration_policy'

