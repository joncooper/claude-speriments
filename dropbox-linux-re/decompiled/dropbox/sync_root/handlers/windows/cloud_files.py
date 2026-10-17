# Source Generated with Decompyle++
# File: cloud_files.pyc (Python 3.11)

import os
import time
from enum import Enum
from typing import Any, Callable, Dict, List, NamedTuple, Optional, Set, Text, Tuple, TypeVar
import win32api
from cloud_files_utils import check_cloud_files_reparse_tag, get_current_sync_roots, get_sync_root_hydration_policy, get_sync_roots_from_registry, HydrationPolicy as CFHydrationPolicy, poke_connect_sync_root, register_sync_root, unregister_sync_root
from pynt.constants import COM_ERROR_NOT_FOUND, ERROR_SUCCESS, KEY_ALL_ACCESS, KEY_READ, KEY_WOW64_32KEY, KEY_WOW64_64KEY
from pynt.headers.windows import FILE_ATTRIBUTE_REPARSE_POINT
from pynt.helpers.registry import enum_registry_subkeys, enum_registry_subkeys_as_keys, enum_registry_values, key_to_str, registry_key, safe_delete_regkey, safe_read_registry_value
from six.moves.winreg import HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE
from build_number import BUILD_KEY, is_full_msix
from build_number.features import feature_enabled
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.cloud_files_migration.helpers import is_nested_under_cloud_files_root
from dropbox.client.util.win import get_install_dir, get_sid_string
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.exception_decorators import handle_exceptions_ex_1
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_engine_boundary.file_system import AbstractFileSystem
from dropbox.sync_root.events.reporter import report_sync_root_event
from dropbox.sync_root.events.types import ExtraInfo, SyncRootEvent, SyncRootEventType
from dropbox.sync_root.handlers.interface import _SyncRootHandler
from dropbox.sync_root.helpers import check_dropbox_path_exists
from dropbox.sync_root.interface import SyncRootType
from dropbox.sync_root.types import RemovalMode, SyncRootHydrationPolicy, SyncRootInvalid, SyncRootRepairAction
from dropbox.trace import TRACE
from dropbox.win32.kernel32 import GetLastError
HKCU_EXPLORER_NAME_SPACES_KEY = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\Namespace'
HKLM_SYNC_ROOT_MANAGER_KEY = 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SyncRootManager'
_T = TypeVar('_T')

class CloudFileRootInconsistencyType:
    MISSING_ROOT_IN_EXPLORER = 'missing_root_in_explorer'
    MULTIPLE_ROOTS_IN_EXPLORER = 'multiple_root_in_explorer'
    MISSING_ROOT = 'missing_root'
    MULTIPLE_ROOT = 'multiple_root'
    MISMATCHED_DISPLAY_NAME = 'mismatched_display_name'
    MISMATCHED_ROOT = 'mismatched_root'
    MULTIPLE_CONFLICTING_ROOTS = 'multiple_conflicting_roots'
    NESTED_CF_ROOT = 'nested_cf_root'

SyncRootRegistryInfo = NamedTuple('SyncRootRegistryInfo', [
    ('reg_key', str),
    ('reg_values', Dict[(str, Any)]),
    ('permission_key', str)])

class RootCleanupStage(Enum):
    FINDING_CONFLICTING_ROOTS = 1
    MOUNTED_ROOT_CLEANUP_START = 2
    CF_ROOT_CLEANUP_START = 3

_HYDRATION_POLICY_TO_CF = {
    SyncRootHydrationPolicy.STREAMING: CFHydrationPolicy.PROGRESSIVE,
    SyncRootHydrationPolicy.FULL: CFHydrationPolicy.FULL }
_CF_WINRT_HYDRATION_POLICY_TO_POLICY = {
    1: SyncRootHydrationPolicy.STREAMING,
    2: SyncRootHydrationPolicy.FULL }

class _CloudFilesRootHandler(_SyncRootHandler):
    pass
# WARNING: Decompyle incomplete

