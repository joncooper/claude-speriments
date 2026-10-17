# Source Generated with Decompyle++
# File: harmony_mev_session_vm.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from time import time as _time
from typing import Dict, List, Optional, Text
from dropbox.callbacks import create_weakref_callback
from dropbox.client.features.harmony_gating import desktop_editor_tracking_disabled, desktop_harmony_pass_enabled
from dropbox.client.features.presence.view_model.file_presence import FilePresenceVM
from dropbox.client.features.seen_state.seen_state_vm import get_shared_content_members_fetcher, SeenStateData, SeenStateVM, user_seen_state_string_function
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption, report_exception, Severity
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1, async_queued_method_2
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.futures import Future, FutureHelpers, ResolvedFuture, sleep_async
from dropbox.foundation.futures.basic import flatten_future
from dropbox.foundation.raii2 import destroying
from dropbox.foundation.signals import StandardSignal
from dropbox.harmony.badge.badge_preferences import BadgePreferences, BadgeVisibility
from dropbox.harmony.badge.last_revision import LastRevision
from dropbox.harmony.badge.last_seen_cache import LastSeenCache
from dropbox.harmony.coordination.model.coordination import Coordination
from dropbox.harmony.coordination.model.types import CoordinationInfo
from dropbox.harmony.coordination.view_model.conflicted_copy import ConflictVM
from dropbox.harmony.coordination.view_model.coordination import CoordinationVM
from dropbox.harmony.logger.event_types import HarmonyRegressionMetrics
from dropbox.harmony.logger.logging import Logger
from dropbox.harmony.models.harmony_session_state import BadgeVersion, FlyoutState, HarmonyMEVSessionState, SeenStateInfo
from dropbox.harmony.models.harmony_user import HarmonyUser
from dropbox.harmony.models.types import DocumentSession, DocumentSessionID, WindowID
from dropbox.harmony.presence.editor_tracking import EditorTracking, EditorTrackingStub
from dropbox.harmony.presence.presence_writing import PresenceWriting
from dropbox.harmony.utility.constants import BeaconPlatform
from dropbox.harmony.window_tracking.document_session_manager import DocumentSessionManager
from dropbox.platform import IS_MAC, IS_WINDOWS
from dropbox.sharing.shared_content_members_fetcher import SharedContentMember, SharedContentMembersFetcher
from dropbox.sync_engine_adapter.wrapper import SyncEngineWrapper
from dropbox.sync_root.gating import file_provider_supported
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.mac.version import CATALINA, MAC_VERSION

class HarmonyMEVSessionVM(Actor):
    pass
# WARNING: Decompyle incomplete

