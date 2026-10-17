# Source Generated with Decompyle++
# File: mounted.pyc (Python 3.11)

from typing import Callable, List, Optional
from pynt.constants import COM_ERROR_NOT_FOUND
from build_number import BUILD_KEY
from build_number.features import feature_enabled
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.features.cloud_files_migration.helpers import is_nested_under_cloud_files_root
from dropbox.client.util.win import get_sid_string
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.sync_root.events.reporter import report_sync_root_event
from dropbox.sync_root.events.types import ExtraInfo, SyncRootEvent, SyncRootEventType
from dropbox.sync_root.gating import cloud_files_capable
from dropbox.sync_root.handlers.interface import _SyncRootHandler
from dropbox.sync_root.helpers import check_dropbox_path_exists
from dropbox.sync_root.interface import SyncRootType
from dropbox.sync_root.types import RemovalMode, SyncRootHydrationPolicy, SyncRootRepairAction
from dropbox.trace import TRACE

class WindowsMountedRootInconsistencyType:
    MULTIPLE_OWNERS_WITH_CONFLICTING_ROOT = 'multiple_owners_with_conflicting_root'
    SYNC_ROOT_NESTED_IN_CLOUD_FILES_ROOT = 'sync_root_nested_in_cloud_files_root'


class _WindowsMountedRootHandler(_SyncRootHandler):
    pass
# WARNING: Decompyle incomplete

