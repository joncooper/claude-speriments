# Source Generated with Decompyle++
# File: coordination.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
import os
import time
from enum import Enum
from typing import Any, cast, List, Optional, Text, Union
from dropbox import fsutil
from dropbox.client.features.apollo_alerts.model.apollo_alerts import AlertResult, ApolloAlerts
from dropbox.client.ui.common.harmony import HarmonyStrings
from dropbox.client.util import launch_app
from dropbox.components.desktop_components import DesktopComponent
from dropbox.dbexceptions import TimeoutError
from dropbox.exception.reporting import report_bad_assumption, report_exception
from dropbox.exception.severity import Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import CancelledFutureException, Future, IncompleteFutureException, ResolvedFuture
from dropbox.foundation.raii2.arc import Arc, Weak
from dropbox.foundation.signals import StandardSignal
from dropbox.functions import make_bytes
from dropbox.harmony.badge.badge_errors import BadgeErrors
from dropbox.harmony.coordination.model.conflict_cache import ConflictCache
from dropbox.harmony.coordination.model.types import CoordinationStage, CoordinationState, CoordinationUpdate
from dropbox.harmony.logger.event_types import CoordinationEvent
from dropbox.harmony.logger.logging import Logger
from dropbox.harmony.models.types import DocumentSession, DocumentSessionID
from dropbox.harmony.plugins.base import BasicCoordinatingPlugin, EditorStatusTracker, HarmonyPlugin
from dropbox.harmony.plugins.broker import PluginBroker
from dropbox.harmony.window_tracking.document_session_manager import DocumentSessionManager
from dropbox.i18n import trans
from dropbox.model.types import FileId
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.shared.local_path import LocalPath
from dropbox.shared.server_path import MRCasedServerPath, MRLowerServerPath
from dropbox.sync_engine_adapter.wrapper import NucleusWrapper, SyncEngineWrapper
from dropbox.sync_engine_boundary.constants import SyncDirection, SyncEventType
from dropbox.sync_engine_boundary.types import CallbackRemovalToken, ConflictResolutionAttempt, MoveToDeletedCache
from dropbox.sync_engine_boundary.types.sync_completion import SyncCompletedSummary
from dropbox.sync_engine_boundary.types.sync_failures import SyncOpFailed
from dropbox.sync_engine_boundary.types.sync_progress import SyncPhase, SyncProgress
from dropbox.sync_root.gating import file_provider_supported
from dropbox.threading import Condition
from dropbox.trace import TRACE
if IS_MAC:
    from macffi.CoreServices import is_automation_enabled
    from dropbox.mac.system_preferences import open_automation_preferences
    from dropbox.mac.version import MAC_VERSION, MOJAVE

class CoordinationError(Exception):
    pass
# WARNING: Decompyle incomplete


class _CoordinationFlow(Enum):
    Coordination = 'coordination'
    ConflictResolution = 'conflict-resolution'


class Coordination(Actor):
    pass
# WARNING: Decompyle incomplete

