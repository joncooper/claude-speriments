# Source Generated with Decompyle++
# File: fp_shadow_migration.pyc (Python 3.11)

from typing import Optional
from FileProvider import NSFileProviderDomain, NSFileProviderDomainRemovalModeRemoveAll, NSFileProviderManager
from Foundation import NSError, NSURL
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_rmtree_with_retry
from dropbox.foundation.futures import FailedFuture, Future, ResolvedFuture
from dropbox.mac.internal import autoreleasepool
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.events.reporter import report_sync_root_event
from dropbox.sync_root.events.types import ExtraInfo, SyncRootEvent, SyncRootEventType
from dropbox.sync_root.fp_helpers import fp_get_nucleus_hidden_container_path
from dropbox.sync_root.handlers.interface import _SyncRootHandler
from dropbox.sync_root.handlers.macos.file_provider import _DomainMethod, _ReportContext, FileProviderHandlerFuture
from dropbox.sync_root.handlers.macos.mounted import _MacMountedRootHandler
from dropbox.sync_root.types import RemovalMode, SyncRootCreationResult, SyncRootHydrationPolicy, SyncRootInvalid, SyncRootType
from dropbox.trace import TRACE

class _FPShadowMigrationRootHandler(_MacMountedRootHandler):
    pass
# WARNING: Decompyle incomplete

