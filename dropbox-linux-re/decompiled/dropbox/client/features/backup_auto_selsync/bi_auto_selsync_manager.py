# Source Generated with Decompyle++
# File: bi_auto_selsync_manager.pyc (Python 3.11)

import itertools
import os
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Callable, Dict, FrozenSet, Iterable, List, Mapping, Optional, Set
from dropbox.client.device_info import UNSAFE_get_raw_machine_uuid
from dropbox.client.features.backup_auto_selsync.auto_selsync_result import BackupAutoSelSyncResult, BackupAutoSelSyncResultCode
from dropbox.client.features.backup_auto_selsync.constants import BI_AUTO_SEL_SYNC_INVARIANT_INTERVAL_DEFAULT
from dropbox.client.features.backup_auto_selsync.gating import BackupAutoSelSyncFeature
from dropbox.client.features.backup_auto_selsync.logging import report_exception_and_ignore
from dropbox.client.features.backup_auto_selsync.utils import does_non_empty_directory_exist_by_path, does_path_exist, get_local_backups, list_top_level_entries
from dropbox.client.features.backup_common.base_event_reporter import LifetimeReporter, random_session_id
from dropbox.client.features.backup_common.constants import EDB_ANCHOR_EXTENSION
from dropbox.client.features.backup_instance.event_reporter import OperationEventReporter
from dropbox.client.features.backup_instance.types import BackupInstanceEvent
from dropbox.client.features.backup_instance.utils import BI_TRACE, BI_WARN
from dropbox.client.features.backup_instance.wrapper import BackupInstanceWrapper
from dropbox.client.features.home_feed.shared.util.signals import RepeatedEventSignalWithPayload
from dropbox.client.features.sync_everything.v3.actor_daemon import ActorDaemon
from dropbox.client.features.sync_everything.v3.async_tools import async_queued_local_function, future_function, future_pipeline
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import assert_not_none, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.asynchronous.exec_ctx import async_queued_method
from dropbox.foundation.context.machine import MachineContext
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.raii2.singleton import SingletonActor
from dropbox.foundation.signals import Signal
from dropbox.model.types import FileId
from dropbox.shared.local_path import LocalPath
from dropbox.sync_engine_boundary.nucleus_interface import NucleusInterface
from dropbox.sync_engine_boundary.types.local_path import LocalPathProperties
from dropbox.sync_engine_boundary.types.remote_props import DirPnmBehaviors, RemoteLocationProperties
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
FileIdToRemoteLocationProps = Mapping[(FileId, Optional[RemoteLocationProperties])]
SelSyncResultList = List[BackupAutoSelSyncResult]

class BackupAutoSelSyncManager(SingletonActor):
    pass
# WARNING: Decompyle incomplete

