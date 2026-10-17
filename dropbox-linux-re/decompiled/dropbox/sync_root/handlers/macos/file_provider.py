# Source Generated with Decompyle++
# File: file_provider.pyc (Python 3.11)

import collections
import copy
import functools
import sys
import time
import types
import uuid
from enum import Enum
from os import symlink as os_symlink
from pathlib import Path
from typing import Any, Callable, Deque, Dict, List, Optional, Set, Tuple, TypeVar, Union
from AppKit import NSURLVolumeUUIDStringKey
from CoreServices.LaunchServices import kLSSharedFileListFavoriteVolumes, LSSharedFileListCopySnapshot, LSSharedFileListCreate, LSSharedFileListItemCopyProperty
from FileProvider import NSFileProviderDomain, NSFileProviderDomainDidChange, NSFileProviderDomainRemovalModePreserveDirtyUserData, NSFileProviderDomainRemovalModePreserveDownloadedUserData, NSFileProviderDomainRemovalModeRemoveAll, NSFileProviderManager, NSFileProviderRootContainerItemIdentifier
from FinderSync import FIFinderSyncController
from Foundation import NSArray, NSError, NSFileWriteFileExistsError, NSNotification, NSNotificationCenter, NSObject, NSURL
from build_number import get_build_channel, is_frozen
from dropbox import fsutil
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.background_worker import on_background_thread
from dropbox.client.configuration.interface import LocalConfigurationInterface
from dropbox.client.util.mac import get_app_path, remove_from_sidebar
from dropbox.components.desktop_components import DesktopComponent
from dropbox.event import report, sanitize_event_extra_dict
from dropbox.exception.exception_decorators import handle_exceptions_ex_0, handle_exceptions_ex_1, handle_exceptions_ex_2
from dropbox.exception.reporting import report_exception
from dropbox.exception.severity import Severity
from dropbox.fileutils import safe_rmtree_with_retry
from dropbox.foundation.exception_info import ExcInfo
from dropbox.foundation.futures import FailedFuture, Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.futures.basic import allow_blocking_on_main_thread, BaseFuture
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.transitional.on_thread_future import make_on_thread_future_decorator
from dropbox.i18n import trans
from dropbox.mac.finder import restart as _restart_finder
from dropbox.mac.internal import autoreleasepool, MacError
from dropbox.mac.version import MAC_VERSION, SEQUOIA, SONOMA_14_1, SONOMA_14_3, VENTURA
from dropbox.sync_engine_boundary.factory import SyncEngineFactory
from dropbox.sync_root.check_merge_dropbox import check_reconnect_fp, fp_domain_fields
from dropbox.sync_root.constants import SyncRootConstants
from dropbox.sync_root.events.reporter import report_sync_root_event
from dropbox.sync_root.events.types import ExtraInfo, SyncRootEvent, SyncRootEventType
from dropbox.sync_root.fp_external_drive import check_fp_external_drive_eligibility
from dropbox.sync_root.fp_helpers import fp_get_nucleus_hidden_container_path, is_domain_lookup_error_retriable
from dropbox.sync_root.handlers.interface import _SyncRootHandler
from dropbox.sync_root.handlers.macos.mac_handler import _MacRootHandler
from dropbox.sync_root.handlers.macos.types import FileProviderDomainProperties
from dropbox.sync_root.helpers import check_dropbox_path_exists
from dropbox.sync_root.types import RemovalMode, SyncRootCreationConflict, SyncRootCreationResult, SyncRootFeatureUnsupported, SyncRootHydrationPolicy, SyncRootInconsistency, SyncRootInvalid, SyncRootMountMissing, SyncRootRepairAction, SyncRootType
from dropbox.trace import TRACE
# WARNING: Decompyle incomplete
