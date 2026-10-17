# Source Generated with Decompyle++
# File: fs_utils.pyc (Python 3.11)

import errno
import os
import stat
import sys
from functools import partial
from typing import Dict, List, Mapping, Optional, Text, Tuple, TYPE_CHECKING, Union
from build_number.platform import IS_MAC, IS_WINDOWS
from dropbox.client.authentication.account_interface import AccountInterface
from dropbox.client.features.backup_common.base_event_reporter import EventReporter
from dropbox.client.features.sync_everything.constants import FOLDER_METADATA_UX_UPDATE_FREQUENCY, FREE_SPACE_BUFFER, OQ_MAX_RUNTIME
from dropbox.client.features.sync_everything.v3.async_tools import future_function, future_sequence
from dropbox.client.features.sync_everything.v3.config_utils import se_active_device_name, se_pending_device_name
from dropbox.client.features.sync_everything.v3.event_reporter import PerformanceEventReporter
from dropbox.client.features.sync_everything.v3.fp_utils import allow_dataless_recall, DatalessContext
from dropbox.client.features.sync_everything.v3.nodep_utils import map_names_l, SE_TRACE, SE_WARN
from dropbox.client.features.sync_everything.v3.sync_everything_logging import SyncEverythingEvent
from dropbox.client.features.sync_everything.view_model.folder_metadata import FolderMetadata
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.fastwalk import fastwalk
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.exception_info import typed_exc_info
from dropbox.foundation.futures import Future, ResolvedFuture, sleep_async
from dropbox.foundation.futures.thread import GlobalPool
from dropbox.foundation.raii2 import destroying
from dropbox.fsutil import FileSystem, listdir
from dropbox.mac.version import CATALINA
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper
from dropbox.sync_engine_boundary.constants import OSFolderID
from dropbox.sync_engine_boundary.types.sync_failures import SyncFailureType, SyncOpFailed
if TYPE_CHECKING:
    from dropbox.client.features.sync_everything.v3.device_state import KnownFolder
if IS_MAC:
    from dropbox.mac.version import MAC_VERSION
if IS_WINDOWS:
    from winffi.kernel32.api import FILE_ATTRIBUTE_DIRECTORY, FILE_ATTRIBUTE_HIDDEN, FILE_ATTRIBUTE_SYSTEM, GetFileAttributesW

def _is_ignored_error(exc = None):
