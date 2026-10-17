# Source Generated with Decompyle++
# File: harmony_mev_owner.pyc (Python 3.11)

from __future__ import absolute_import, division, print_function
from typing import Optional, Tuple
from dropbox.client.features.harmony_gating import desktop_harmony_is_allowed, desktop_harmony_is_supported
from dropbox.client.fenix.types.harmony import DocumentSessionUpdateType, DocumentSessionView
from dropbox.components.desktop_components import DesktopComponent
from dropbox.exception.reporting import report_bad_assumption
from dropbox.foundation.actors2 import Actor
from dropbox.foundation.asynchronous.exec_ctx import assert_on_queued_thread, async_queued_method_0, async_queued_method_1
from dropbox.foundation.context.user import UserContext
from dropbox.foundation.raii2.arc import Arc
from dropbox.foundation.raii2.wrappers import Replaceable
from dropbox.foundation.signals import SignalConnection
from dropbox.functions import lrudict
from dropbox.harmony.badge.badge_preferences import BadgePreferences
from dropbox.harmony.badge.last_seen_cache import LastSeenCache
from dropbox.harmony.coordination.model.conflict_cache import ConflictCache
from dropbox.harmony.logger.event_types import MEVOwnerEvents
from dropbox.harmony.logger.logging import Logger
from dropbox.harmony.models.types import DocumentSession, DocumentSessionID
from dropbox.harmony.session_management.harmony_mev_session_view import HarmonyMEVSessionView
from dropbox.harmony.session_management.harmony_session_update_tracker import HarmonySessionUpdateTracker, HarmonyUpdateInfo
from dropbox.harmony.window_tracking.document_session_manager import DocumentSessionManager
from dropbox.harmony.window_tracking.supported_applications import harmony_supported_apps
from dropbox.platform import IS_MAC
from dropbox.sync_root.gating import file_provider_supported
from dropbox.threading import Lock
from dropbox.trace import TRACE
if IS_MAC:
    from dropbox.harmony.mac.accessibility_prompter import AccessibilityPrompter
MYPY = False
if MYPY:
    from dropbox.foundation.navigation_service.interface import NavigationServiceInterface

class HarmonyMEVOwner(Actor):
    pass
# WARNING: Decompyle incomplete

